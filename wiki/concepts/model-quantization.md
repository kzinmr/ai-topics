---
title: "Model Quantization"
type: concept
created: 2026-04-25
updated: 2026-05-01
tags:
  - concept
  - quantization
  - inference
  - optimization
  - model-compression
status: L1
sources: []
related:
  - "[[concepts/gguf-quantization]]"
  - "[[concepts/local-llm/model-quantization]]"
  - "[[concepts/fine-tuning/quantization-overview]]"
  - "[[concepts/ai-infrastructure-engineering/gpu-vram-fundamentals]]"
  - "[[concepts/inference/vllm]]"
  - "[[concepts/tensorrt-llm]]"
  - "[[concepts/ai-infrastructure-engineering/_index]]"
---

# Model Quantization

> モデル量子化は、ニューラルネットワークのパラメータを低精度で表現することで、メモリ使用量を削減し推論速度を向上させる手法。LLMの実用化に不可欠な基盤技術。

## Why This Matters

量子化がなければ、最新のLLM（70B〜500Bパラメータ）を実用的なハードウェアで実行することは不可能。たとえば70BモデルはFP16（2バイト/パラメータ）で140GBのVRAMが必要 — H100（80GB）にすら収まらない。INT4（0.5バイト/パラメータ）なら35GBに削減され、1台のコンシューマーGPU（RTX 4090: 24GB）でも動作可能になる。

## Summary

### 1. Precision Formats Overview

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
| 1.58-bit (BitNet) | ~1.58 (0.2 bytes) | ~14 GB | 中 | — | 研究段階 |

### 2. Main Quantization Methods

#### Weight-only Quantization (推論専用)
- **GPTQ**: 後トレーニング量子化、Hessianベースの重み調整
- **AWQ (Activation-aware Weight Quantization)**: アクティベーションの重要チャネルを保護
- **GGUF (llama.cpp quantum)**: ブロック単位の量子化、CPU最適化
- **RTN (Round-To-Nearest)**: 最も単純な丸め、精度劣化大

#### Weight+Activation Quantization
- **FP8 Inference**: H100 Transformer Engine, FP8 GEMM
- **INT8 SmoothQuant**: アクティベーションの外れ値をスムージング
- **KV Cache INT8/FP8**: Long contextでのKV Cacheメモリ削減

### 3. Quantization-Aware Training (QAT)

- トレーニング中に量子化をシミュレート → 推論時の品質劣化を最小化
- コスト: トレーニング時間が2-3倍増加

### 4. Hardware Support

| Hardware | Supported Formats |
|----------|------------------|
| NVIDIA A100 | FP16, INT8 |
| NVIDIA H100 | FP16, FP8 (Transformer Engine), INT8, INT4 |
| NVIDIA B200 | FP16, FP8, FP4 (MXFP4), INT8, INT4 |
| Apple M-series | FP16, INT8 (ANE), FP16 via ANE |
| Intel Gaudi | FP16, BF16 |
| AMD MI300X | FP16, FP8 |

### 5. Practical Tradeoff Analysis

**Accuracy vs Memory Tradeoff** (LLaMA-3 70B, MMLU benchmark):
```
Format   | MMLU | VRAM
FP16     | 82.0% | 140 GB
FP8      | 81.8% | 70 GB
INT8     | 81.7% | 70 GB
INT4 AWQ | 81.2% | 35 GB
NF4      | 80.9% | 35 GB
```
(近似値、実際のモデルと評価方法で変動)

### 6. When to Use What

| 要件 | 推奨手法 |
|------|---------|
| 最高の品質 | FP16/BF16（十分なVRAMあり） |
| 本番サーバーの効率重視 | FP8（H100/B200） |
| コスト重視のサーバー | INT8 + KV Cache INT8 |
| ローカル推論（24GB GPU） | INT4 AWQ / GGUF Q4_K_M |
| トレードオフ重視 | INT4 AWQ |
| Long context (128K+) | FP16/INT8 + KV Cache FP8 |

### 7. KV Cache Quantization (Separate from Weights)

- vLLM TurboQuant: 2-bit KV Cache → 4x capacity, < 1% quality loss
- KV Cacheは重みより量子化に対する耐性が高い（アテンション分布がスパース）
- FP8 KV Cache: ほぼ無損失で2倍のKV Cache容量

## Related Pages

- [[concepts/gguf-quantization]] — GGUF format deep-dive
- [[concepts/local-llm/model-quantization]] — Local LLM quantization specifics
- [[concepts/fine-tuning/quantization-overview]] — Fine-tuning quantization
- [[concepts/ai-infrastructure-engineering/gpu-vram-fundamentals]] — VRAM requirements by quantization
- [[concepts/inference/vllm]]#TurboQuant — vLLM 2-bit KV cache
- [[concepts/tensorrt-llm]] — NVIDIA FP8/FP4 inference
- [[concepts/ai-infrastructure-engineering/_index]] — Parent page

## Skills Reference

- `gguf-quantization` — GGUF format & quantization workflow
- `llama-cpp` — Local inference with quantized models

## TODO

- [ ] Add detailed per-method benchmark comparisons
- [ ] Add calibration dataset requirements for GPTQ/AWQ
- [ ] Add hardware-specific quantization guide
- [ ] Add KV cache quantization tradeoffs
- [ ] Add FP4 (MXFP4) architecture details
- [ ] Add BitNet/Ternary weight research frontier
