---
title: "Model Quantization"
type: concept
created: 2026-04-25
updated: 2026-05-04
tags:
  - concept
  - quantization
  - inference
  - optimization
  - model-compression
  - llm-int8
  - bitnet
status: L1
sources:
  - https://timdettmers.com/2022/08/17/llm-int8-and-emergent-features/
  - https://www.maartengrootendorst.com/blog/quantization/
  - https://arxiv.org/abs/2208.07339
  - https://arxiv.org/abs/2310.11453
  - https://arxiv.org/abs/2402.17764
related:
  - "[[concepts/gguf-quantization]]"
  - "[[concepts/local-llm/model-quantization]]"
  - "[[concepts/fine-tuning/quantization-overview]]"
  - "[[concepts/ai-infrastructure-engineering/gpu-vram-fundamentals]]"
  - "[[concepts/inference/vllm]]"
  - "[[concepts/tensorrt-llm]]"
  - "[[concepts/emergent-features-llm]]"
  - "[[concepts/ai-infrastructure-engineering/_index]]"
  - "[[entities/tim-dettmers]]"
  - "[[entities/maarten-grootendorst]]"
---

# Model Quantization

> モデル量子化は、ニューラルネットワークのパラメータを低精度で表現することで、メモリ使用量を削減し推論速度を向上させる手法。LLMの実用化に不可欠な基盤技術。

## Why This Matters

量子化がなければ、最新のLLM（70B〜500Bパラメータ）を実用的なハードウェアで実行することは不可能。たとえば70BモデルはFP16（2バイト/パラメータ）で140GBのVRAMが必要 — H100（80GB）にすら収まらない。INT4（0.5バイト/パラメータ）なら35GBに削減され、1台のコンシューマーGPU（RTX 4090: 24GB）でも動作可能になる。

## 1. Numerical Representation Fundamentals (IEEE-754)

浮動小数点数は3つの要素で構成される（IEEE-754標準）:

| 成分 | 役割 | 例: FP32 |
|------|------|----------|
| **Sign** (符号) | 正/負 | 1 bit |
| **Exponent** (指数) | 値の**範囲**を決定 | 8 bits |
| **Fraction/Mantissa** (仮数) | 値の**精度**（隣接値間の距離）を決定 | 23 bits |

**Key Distinction:**
- **Dynamic Range** → Exponentによって決まる（表現可能な値の区間）
- **Precision** → Fractionによって決まる（隣接する2つの値の間隔）

### Common Data Types

| 型 | Bits | Exponent | Fraction | 特徴 |
|----|------|----------|----------|------|
| FP32 | 32 | 8 | 23 | 基準精度、トレーニング可能 |
| FP16 | 16 | 5 | 10 | 範囲が狭い（±65K） |
| BF16 | 16 | 8 | 7 | FP32と**同じ範囲**、精度は低い |
| FP8 (E4M3) | 8 | 4 | 3 | ±448、**H100 Transformer Engine** |
| FP8 (E5M2) | 8 | 5 | 2 | ±57344、E4M3より広範囲 |
| INT8 | 8 | — | — | 256値の整数マッピング |
| NF4 | 4 | — | — | 正規分布重みに最適化（QLoRA） |

> BF16はDeep Learningの"黄金比"：FP32と同じ範囲を維持しながらメモリを半分に削減できる。

## 2. Quantization Fundamentals

量子化は高精度値（FP32）を低精度値（INT8/INT4など）に写像する処理。

### Memory Formula
```
Memory (GB) ≈ (Number of Parameters × Number of Bits) / 8
```

### Linear Mapping Methods

#### Symmetric Quantization (Absmax)
ゼロを中心に対称な範囲に写像:
- **Scale:** $s = \frac{2^{b-1} - 1}{\alpha}$（α = 最大絶対値）
- **Quantize:** $x_{quant} = \text{round}(s \cdot x)$
- **Dequantize:** $x_{dequant} = x_{quant} / s$
- シンプルだが、分布が非対称な場合は非効率

#### Asymmetric Quantization (Zero-point)
最小/最大を量子化範囲全体に写像。ゼロ中心ではない:
- **Scale:** $s = \frac{\beta - \alpha}{2^{b} - 1}$
- **Zero-point:** $z = -\text{round}(s \cdot \alpha) - 2^{b-1}$
- より柔軟だが、Zero-pointの計算と保持が必要

### Clipping & Calibration

**Clipping:** 動的範囲を人為的に制限（例: [-5, 5]）して、大多数の値の精度を向上させる代わりに外れ値を切り捨てる。

**Calibration**（最適な範囲を選択するプロセス）:
| 手法 | 仕組み | 特徴 |
|------|--------|------|
| **MSE** (最小二乗誤差) | 元の値と量子化値の差を最小化 | 理論的に最適、計算コスト中 |
| **Percentile** | α/βをパーセンタイルで設定 | シンプル、外れ値の影響を受けにくい |
| **KL-divergence** | 分布のエントロピーを最大化 | 最も正確だが高コスト |
| **Min/Max** | 全範囲をそのまま使用 | 外れ値1つで精度が激減 |

## 3. Precision Formats Overview

| Format | Bits/Param | 70B Model | 品質 | 推論速度 | 主な用途 |
|--------|-----------|-----------|------|---------|---------|
| FP32 | 32 (4 bytes) | 280 GB | 基準 | 低速 | トレーニングのみ |
| FP16/BF16 | 16 (2 bytes) | 140 GB | ほぼ無損失 | 中速 | トレーニング/推論 |
| FP8 (E4M3/E5M2) | 8 (1 byte) | 70 GB | 無視できる | 高速 | H100/B200推論 |
| INT8 | 8 (1 byte) | 70 GB | 最小限 | 高速 | 汎用推論 |
| INT4 (GPTQ/AWQ) | 4 (0.5 bytes) | 35 GB | 小（1-2%） | 最速 | ローカル推論 |
| NF4 (QLoRA) | 4 (0.5 bytes) | 35 GB | 小 | 最速 | LoRA学習 |
| FP4 (MXFP4) | 4 (0.5 bytes) | 35 GB | 非常に小 | 最速 | 次世代H/W |
| 2-bit (TSM) | 2 (0.25 bytes) | 17.5 GB | 中程度 | — | 研究段階 |
| **1.58-bit (BitNet)** | ~1.58 (0.2 bytes) | **~14 GB** | 中（研究段階） | **加算のみ** | **研究段階** |

## 4. Main Quantization Methods

### Weight-only Quantization (推論専用)

#### GPTQ (GPU-focused, Frantar et al. 2023)
- **方式:** 逆ヘッセ行列（Inverse-Hessian）を用いて各重みの「重要度」を定量化
- **プロセス:** 行ごとに量子化 → 量子化誤差を**未量子化の残りの重みに再分配**
  - 「負債を隣に回す」ことでモデル全体の性能を維持
- GPU推論に最適化、バッチ推論で高スループット

#### AWQ (Activation-aware Weight Quantization, 2023)
- **方式:** アクティベーションの重要チャネルを特定し、そのチャネルの重みを保護
- GPTQより小モデルで高精度、GPTQより高速な量子化処理

#### GGUF (llama.cpp, CPU/GPU Offloading)
- **方式:** ブロック単位量子化（"super blocks" + "sub blocks"が独自のスケール因子を持つ）
- VRAM不足時に特定レイヤーをCPUにオフロード可能
- Q2_K〜Q8_0の多段階品質選択

#### RTN (Round-To-Nearest)
- 最も単純な丸め方式。精度劣化が最も大きい。
- ベースライン比較用

### Weight+Activation Quantization

| 手法 | 仕組み | 特徴 |
|------|--------|------|
| **FP8 Inference** | H100 Transformer Engine + FP8 GEMM | ネイティブH/Wサポート |
| **INT8 SmoothQuant** | アクティベーションの外れ値をスムージング | 外れ値問題を軽減 |
| **KV Cache INT8/FP8** | Long contextでのKV Cacheメモリ削減 | アテンション分布がスパースなので耐性が高い |

## 5. LLM.int8() and the Outlier Problem (Dettmers, 2022)

### The Challenge
標準的なInt8量子化は、**6.7Bパラメータ以上のモデル**で破綻する。理由は「創発的アウトライヤー特徴量」（emergent outlier features）。

### How Quantization Normally Works
1. ベクトル内の最大絶対値を発見
2. その値で正規化
3. ターゲット型の範囲にスケーリング
4. 丸め

**Outlier Problem:** >6.7Bのモデルでは特定の隠れ次元に極端に大きな値（-60〜-95）が発生し、99.9%の小さな値（-0.1〜0.5）が一緒に量子化されて情報が消失する。

### LLM.int8() Solution
2つの同時技術でゼロ劣化を達成:

#### 1. Vector-wise Quantization
テンソル全体に1つのスケール定数を使う代わりに、行列積の**各行と各列に独立したスケール定数**を使用。

#### 2. Mixed Precision Decomposition
アウトライヤーは**ごく一部の次元に体系的に集中**していることを利用:
1. **分離**: アウトライヤーを含む次元を抽出 → 高精度（FP16）で行列積を計算
2. **量子化**: 残りの99.9%の値をInt8で処理
3. **結合**: 両方の出力をマージして完全な性能を回復

```
Input Hidden States
├── Outlier Dimensions (FP16 matmul) → 少数の次元
└── Normal Dimensions (INT8 matmul)  → 99.9%の値
        ↓
Combined Output (zero degradation)
```

### The 6.7B Phase Shift

Dettmersの定義: *"ある特性の緩やかな変化が、突然フェーズシフトを起こして基質の性質を変える現象"*

| 特性 | 6.7B未満 | 6.7B以上 |
|:-----|:---------|:---------|
| **アウトライヤーの協調** | 確率的/不整合 | **100%の層が同一次元を使用** |
| **アウトライヤーの大きさ** | 小（〜15） | 大（60〜95+） |
| **影響を受ける系列** | 一部 | **75%の系列が影響** |
| **Attention** | 分散型 | 高スパース/離散的 |
| **FFNの刈り込み耐性** | ~30%削除可能 | **<5%** |
| **量子化** | 標準Int8でOK | 混合精度（LLM.int8）が必要 |

### Two Streams Theory
Dettmersは、アウトライヤーが2つの処理ストリームを管理していると理論化:
1. **Input Explanation** — データを説明する特徴量の学習
2. **Feature Removal** — アウトライヤー次元を使ってノイズや文脈と無関係な特徴量を「消音」

> 大きな値（-60〜-95）を特定の次元に保持することで、小さな重みと掛け合わせて非線形関数（Softmax/ReLU）後に他の特徴量を実質的にゼロにできる。

### Research Implications
- **<6.7Bの研究は>6.7Bに一般化できない**
- 創発はパラメータ数ではなく**perplexity**に対して指数関数的に従う
- 小型モデル（125M〜1.3B）のperplexity曲線から175B+モデルの挙動を予測可能

> "There are two types of transformers and you should not generalize from one to the other." — Tim Dettmers

## 6. Post-Training Quantization (PTQ)

トレーニング完了後にモデルを量子化。

### Weights vs Activations

| | Weights | Activations |
|--|---------|-------------|
| **性質** | 静的、既知 | 入力によって変動 |
| **量子化** | 容易（分布が安定） | 困難（分布が動的） |
| **キャリブレーション** | 不要 | キャリブレーションデータセットが必要 |

#### Dynamic Quantization
- 推論時に各層のスケール因子を計算
- 精度が高いが**低速**（オーバーヘッド大）

#### Static Quantization
- キャリブレーションデータセットで事前にスケール因子を計算
- **高速**だが、訓練データの分布を代表するデータセットが必要

### GPTQ (GPU-focused)
- 逆ヘッセ行列で重みの「重要度」を定量化
- 行ごとに量子化 → 誤差を未量子化の重みに再分配
- 高バッチスループット、GPU推論に最適

### GGUF (CPU/GPU Offloading)
- ブロック単位量子化（スーパーブロック + サブブロック）
- CPUオフロード対応、VRAM制限のある環境で柔軟

## 7. Quantization-Aware Training (QAT)

トレーニングプロセスに量子化を統合する手法。

### How It Works
**"Fake Quants"** — フォワードパス中に低ビットに量子化して即座にFP32に戻す。バックワードパスはFP32のまま（量子化は非微分可能のためSTE（Straight-Through Estimator）を使用）。

### Wide Minima Theory
- **PTQ**: FP32では低損失だが、低精度（INT4）では高損失になりうる
- **QAT**: 低精度の損失ランドスケープで**「広い谷」（wide minima）**を発見
  - 広い谷 = 量子化誤差に対してロバスト

> QAT is like training with weighted clothes — when you remove them (quantize), you still perform well because you trained under those constraints.

### QAT vs PTQ

| 基準 | PTQ | QAT |
|------|-----|-----|
| **コスト** | 数分〜数時間（キャリブレーションのみ） | トレーニング時間の2-3倍増加 |
| **INT4精度** | 良好 | **優れている**（特に小モデル） |
| **BI4精度** | 不可 | 必須 |
| **トレーニングデータ** | 数百サンプル | 全トレーニングセット |

## 8. The Frontier: 1-bit and 1.58-bit LLMs

### BitNet (1-bit, Wang et al. 2023)
標準のLinear層を**BitLinear**に置き換え:
- **Weights:** `Signum`関数で {-1, +1} に量子化
- **Activations:** INT8のまま行列積を計算
- **Scaling:** 重みの平均絶対値（β）+ 活性化の最大絶対値（α）で復元

### BitNet b1.58 (Ternary Weights, 2024)
重みに **0** を追加 → **{-1, 0, +1}**:
- **Feature Filtering:** 重み=0で特定の特徴量を無視可能
- **計算効率の革命:** 行列積が**加算と減算のみ**で完了（乗算不要）
- **量子化方式:** `absmean`量子化（平均絶対値を基準に3値化）

```
Traditional FP16 matmul: y = w₁x₁ + w₂x₂ + ... + wₙxₙ  (乗算+加算)
BitNet b1.58 matmul:     y = ±x₁ ± x₂ ... ± xₙ           (加算/減算のみ)
```

### Potential Impact
- 推論時の**消費電力が90%以上削減**される可能性
- 専用H/Wが登場すれば、CPUでも高速推論が可能に
- 小型デバイス（モバイル、IoT）へのLLM搭載が現実的に

### Current Limitations
- 現時点では研究段階（大規模実証は限定的）
- 同等のFP4/INT4モデルと比較して品質にギャップあり
- トレーニングが不安定（特に50B+スケール）

## 9. Practical Tradeoff Analysis

### Accuracy vs Memory Tradeoff (LLaMA-3 70B, MMLU benchmark)
```
Format         | MMLU | VRAM
FP16           | 82.0% | 140 GB
FP8            | 81.8% | 70 GB
INT8           | 81.7% | 70 GB
INT4 AWQ       | 81.2% | 35 GB
NF4            | 80.9% | 35 GB
```
(近似値、実際のモデルと評価方法で変動)

### When to Use What

| 要件 | 推奨手法 |
|------|---------|
| 最高の品質 | FP16/BF16（十分なVRAMあり） |
| 本番サーバーの効率重視 | FP8（H100/B200） |
| コスト重視のサーバー | INT8 + KV Cache INT8 |
| ローカル推論（24GB GPU） | INT4 AWQ / GGUF Q4_K_M |
| VRAM極限（CPU併用） | GGUF + CPU Offloading |
| トレーニング後量子化 | GPTQ（GPU） / GGUF（汎用） |
| 最高の量子化精度 | QAT（ただしコスト高） |
| Long context (128K+) | FP16/INT8 + KV Cache FP8 |

### PTQ Method Selection

| 環境 | 推奨方式 | 理由 |
|------|---------|------|
| GPUのみ（十分なVRAM） | GPTQ / AWQ | 高スループット、バッチ推論 |
| VRAM不足（CPU補助） | GGUF | ブロック単位量子化 + オフロード |
| GPUなし（CPU/Apple Silicon） | GGUF Q4_K_M以上 | llama.cpp最適化 |

## 10. KV Cache Quantization

- vLLM TurboQuant: 2-bit KV Cache → 4x capacity, < 1% quality loss
- KV Cacheは重みより量子化に対する耐性が高い（アテンション分布がスパース）
- FP8 KV Cache: ほぼ無損失で2倍のKV Cache容量

## Related Pages

- [[concepts/bitsandbytes]] — bitsandbytes: NF4/FP4 quantization library, QLoRA backend
- [[concepts/gguf-quantization]] — GGUF format deep-dive
- [[concepts/local-llm/model-quantization]] — Local LLM quantization specifics
- [[concepts/fine-tuning/quantization-overview]] — Fine-tuning quantization
- [[concepts/ai-infrastructure-engineering/gpu-vram-fundamentals]] — VRAM requirements by quantization
- [[concepts/inference/vllm]]#TurboQuant — vLLM 2-bit KV cache
- [[concepts/tensorrt-llm]] — NVIDIA FP8/FP4 inference
- [[concepts/ai-infrastructure-engineering/_index]] — Parent page
- [[entities/tim-dettmers]] — bitsandbytes, LLM.int8(), QLoRA
- [[entities/maarten-grootendorst]] — Visual quantization guide

## Skills Reference

- `gguf-quantization` — GGUF format & quantization workflow
- `llama-cpp` — Local inference with quantized models

## Sources

- [LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale (Dettmers et al., 2022)](https://arxiv.org/abs/2208.07339)
- [A Visual Guide to Quantization (Grootendorst, 2024)](https://www.maartengrootendorst.com/blog/quantization/)
- [QLoRA: Efficient Finetuning of Quantized LLMs (Dettmers et al., 2023)](https://arxiv.org/abs/2305.14314)
- [BitNet: Scaling 1-bit Transformers for Large Language Models (Wang et al., 2023)](https://arxiv.org/abs/2310.11453)
- [The Era of 1-bit LLMs: All Large Language Models are in 1.58 Bits (Ma et al., 2024)](https://arxiv.org/abs/2402.17764)
- [GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers (Frantar et al., 2023)](https://arxiv.org/abs/2210.17323)
- [AWQ: Activation-aware Weight Quantization for LLM (Lin et al., 2023)](https://arxiv.org/abs/2306.00978)

## TODO

- [x] Add LLM.int8() and emergent features section (Dettmers)
- [x] Add IEEE-754 representation fundamentals
- [x] Add symmetric/asymmetric quantization mapping
- [x] Add calibration deep-dive (MSE, KL, Percentile)
- [x] Add BitNet / 1.58-bit frontier section
- [x] Update sources with Dettmers and BitNet papers
- [ ] Add per-method benchmark comparisons (GPTQ vs AWQ vs GGUF vs vanilla)
- [ ] Add calibration dataset requirements for GPTQ/AWQ
- [ ] Add hardware-specific quantization guide per GPU generation
- [ ] Add FP4 (MXFP4) architecture details
