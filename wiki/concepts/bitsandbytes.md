---
title: "bitsandbytes"
type: concept
created: 2026-05-04
updated: 2026-05-04
tags:
  - concept
  - quantization
  - library
  - cuda
  - nf4
  - qlora
status: L2
sources:
  - https://huggingface.co/docs/bitsandbytes/en/reference/nn/linear4bit
  - https://huggingface.co/blog/4bit-transformers-bitsandbytes
  - https://arxiv.org/abs/2305.14314
  - https://github.com/bitsandbytes-foundation/bitsandbytes
related:
  - "[[concepts/model-quantization]]"
  - "[[concepts/qlora]]"
  - "[[concepts/fsdp-qlora]]"
  - "[[entities/tim-dettmers]]"
  - "[[concepts/fine-tuning/peft-lora-qlora]]"
  - "[[concepts/llm-int8]]"
  - "[[entities/artidoro-pagnoni]]"
---

# bitsandbytes

> デファクトスタンダードの4-bit / 8-bit量子化ライブラリ。Hugging Face TransformersエコシステムにおけるLLM量子化のバックエンドとして、QLoRAによる4ビットファインチューニングを可能にする。Tim Dettmersによって開発され、現在は**bitsandbytes-foundation**がメンテナンス。

## Why This Matters

bitsandbytesなしには、コンシューマーGPU（24GB〜48GB VRAM）での70B級LLMのファインチューニングは事実上不可能。NF4量子化 + double quantization + ページドオプティマイザの組み合わせにより、65Bモデルが1台の48GB GPUで学習可能（Guanacoモデル、ChatGPTの99.3%性能）。

## Architecture

### Core Modules

#### `Linear4bit` — 基底クラス
4ビット量子化線形層のベース。量子化は**デバイス転送時**（`.to("cuda")`）にトリガーされる。この設計が重要：重みをロードしただけでは量子化されず、GPUにコピーするタイミングで初めて4ビットに変換される。

```python
import torch
import bitsandbytes as bnb
from bnb.nn import Linear4bit

layer = Linear4bit(4096, 4096)
layer.load_state_dict(torch.load("weights.pt"))
layer = layer.to("cuda")  # ← 量子化はここで発生
```

| パラメータ | 型 | デフォルト | 説明 |
|-----------|-----|-----------|------|
| `input_features` | int | 必須 | 入力次元数 |
| `output_features` | int | 必須 | 出力次元数 |
| `bias` | bool | True | バイアスの有無 |
| `compute_dtype` | torch.dtype | None | 計算精度（bf16推奨） |
| `compress_statistics` | bool | True | 量子化統計量の圧縮 |
| `quant_type` | str | 'fp4' | 'fp4' または 'nf4' |
| `quant_storage` | torch.dtype | uint8 | 4ビット重みの保存形式（2値/バイト） |

#### `LinearFP4` / `LinearNF4`
`Linear4bit`のサブクラス。`quant_type`を固定した専用レイヤー:
- **LinearFP4**: 標準4ビット浮動小数点
- **LinearNF4**: NormalFloat 4 — 正規分布重みに最適化

#### `Params4bit`
4ビット重みを保持する特殊なパラメータクラス。内部で`quant_storage`（uint8）に2つの4ビット値をパックして格納。`compute_dtype`で指定された精度にオンザフライで復元される。

### NF4 (NormalFloat 4) — 詳細

NF4はQLoRA論文で導入された、**正規分布する重みに最適化された4ビットデータ型**。

#### 設計原理
標準正規分布 N(0, 1) の累積分布関数（CDF）を利用:
1. N(0, 1) を16個の等面積ビン（equal-area bins）に分割
2. 各ビンのCDF値が量子化レベルに対応
3. 正規化範囲 [-1, 1] にマッピング

```
実装: create_normal_map() 関数
α = 929/960 ≈ 0.9677083  # 正規分布の裾をクリップする係数
```

#### なぜFP4より優れているか
- **FP4**: 固定の指数/仮数ビット割り当て。値の分布に関係なく均一な間隔
- **NF4**: 値が密な領域（平均値付近）で高精度、疎な領域（裾）で低精度
  - LLMの重みは正規分布 → 平均値付近にほとんどの重みが集中
  - NF4はこの分布に合わせて「解像度」を配分する

完全な対称型ではなく、0を正確に表現できない（裾が非対称のため）。John D. Cookによる分析: `α = 929/960` は2^4=16値のベストな分布を近似する経験値。

### Double Quantization
bitandbytesは量子化定数そのものにもう一段の量子化を適用:
- 最初の量子化: FP16重み → NF4（ブロック単位、ブロックサイズ64）
- 2回目の量子化: FP32量子化定数 → FP8（ブロック単位、ブロックサイズ256）
- 節約: パラメータあたり約**0.4ビット**追加削減

## Integration with Hugging Face

### Transformers統合
`BitsAndBytesConfig` で設定:

```python
from transformers import BitsAndBytesConfig
import torch

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",        # NF4 vs FP4
    bnb_4bit_use_double_quant=True,   # ダブル量子化
    bnb_4bit_compute_dtype=torch.bfloat16,
)

model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-2-70b-hf",
    quantization_config=bnb_config,
    device_map="auto",
)
```

### PEFT + TRL統合（QLoRAファインチューニング）
4ビット量子化モデルは直接訓練不可 → PEFTのLoRAアダプターを追加:

```python
from peft import LoraConfig, get_peft_model
from trl import SFTTrainer

peft_config = LoraConfig(
    r=16, lora_alpha=32,
    target_modules=["q_proj", "v_proj"],
    bias="none", task_type="CAUSAL_LM",
)

trainer = SFTTrainer(
    model=model,      # 4-bit quantized base
    peft_config=peft_config,
    ...
)
```

## Ecosystem Position

```
Hugging Face Transformers
  └── BitsAndBytesConfig (設定)
       └── bitsandbytes (CUDAカーネル)
            ├── Linear4bit → NF4/FP4 量子化
            ├── LLM.int8() → 8-bit 混合精度
            └── Params4bit → 4-bit パラメータ管理
                 └── PEFT/TRL (LoRA訓練)
```

- **競合との違い**: GPTQ/AWQは後処理量子化（PTQ）で推論特化、bitsandbytesは訓練時量子化（QAT的）でQLoRA訓練を可能にする
- **vLLM / SGLang**: bitsandbytes量子化モデルの推論はHF Transformers経由で可能だが、vLLMは独自のGPTQ/AWQカーネルを使用

## Hardware & Constraints

| 要件 | 詳細 |
|------|------|
| **GPU** | NVIDIA CUDA 11.2+、Compute Capability 7.0+ |
| **CPU** | 非対応（CUDAのみ） |
| **サポートモデル** | Accelerateローディング対応の全モデル |
| **訓練方式** | 純4ビット訓練不可 → PEFT (LoRA) アダプター必須 |
| **ストレージ** | uint8で2値パック（メモリ節約と引き換えに少しの復元オーバーヘッド） |

## Performance

T4 16GB GPUでのベンチマーク:

| モデル | FP16サイズ | 手法 | 結果 |
|-------|-----------|------|------|
| Llama-7B | 14GB | 4-bit NF4 + bf16 | **OOMなし** |
| Llama-13B | 27GB | 4-bit NF4 + fp16 + GC + DQ | **OOMなし** (seq=1024) |
| Llama-13B | 27GB | 8-bit + GC | OOM |

## Key Takeaways

- **訓練時**: QLoRA + bitsandbytesが唯一の実用的な4ビット訓練経路
- **推論時**: GPTQ/AWQ/GGUFがより高速（専用カーネル最適化済み）
- **NF4 vs FP4**: 正規分布重みならNF4が常に高精度
- **quant_storage=uint8**: 2値パックによりメモリ節約、compute時はbf16に復元
- **bitsandbytesはCUDA Only**: CPU/Apple SiliconではGGUFを使用

## Related Pages

- [[concepts/model-quantization]] — Comprehensive quantization guide
- [[concepts/qlora]] — QLoRA fine-tuning (bitsandbytes-based)
- [[concepts/fsdp-qlora]] — FSDP + QLoRA distributed training
- [[concepts/llm-int8]] — LLM.int8() 8-bit inference
- [[entities/tim-dettmers]] — bitsandbytes creator
- [[concepts/fine-tuning/peft-lora-qlora]] — PEFT integration
- [[concepts/gguf-quantization]] — CPU/Apple Silicon alternative

## Sources

- [bitsandbytes Linear4bit API Docs](https://huggingface.co/docs/bitsandbytes/en/reference/nn/linear4bit)
- [Making LLMs even more accessible with bitsandbytes (HF Blog, 2023)](https://huggingface.co/blog/4bit-transformers-bitsandbytes)
- [QLoRA: Efficient Finetuning of Quantized LLMs (Dettmers et al., 2023)](https://arxiv.org/abs/2305.14314)
- [bitsandbytes GitHub Repository](https://github.com/bitsandbytes-foundation/bitsandbytes)
- [Gaussian distributed weights for LLMs: NF4 and QLoRA (John D. Cook, 2026)](https://www.johndcook.com/blog/2026/04/18/qlora/)
