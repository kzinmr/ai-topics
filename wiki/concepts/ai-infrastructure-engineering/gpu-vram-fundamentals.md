---
title: "GPU / VRAM Fundamentals"
type: concept
created: 2026-05-01
updated: 2026-05-01
tags:
  - concept
  - inference
  - vram
  - memory-bandwidth
  - hardware
  - infrastructure
status: L1
aliases:
  - gpu-vram-fundamentals
  - gpu-memory-hierarchy
  - gpu-architecture
sources: []
related:
  - "[[concepts/local-llm/inference-hardware]]"
  - "[[concepts/llm-inference]]"
  - "[[concepts/model-quantization]]"
  - "[[concepts/ai-infrastructure-engineering/_index]]"
---

# GPU / VRAM Fundamentals

> GPUアーキテクチャの基礎から、LLM推論に必要なVRAM計算、メモリ帯域幅の影響、量子化とバッチ処理の経済学までを体系的にカバーする。

## Why This Matters

LLM推論において、GPUはただの「速い計算機」ではない。**メモリ帯域幅**がスループットの主たる制約要因であり、**VRAM容量**が同時に処理できるモデルサイズ・バッチサイズ・コンテキスト長を決定する。これらの物理的制約を理解することなく、本番システムの最適化は不可能。

## Outline

### 1. GPU Memory Hierarchy

- **HBM (High Bandwidth Memory)** — GPUの主要メモリ。容量と帯域幅のトレードオフ
- **SRAM / L1/L2 Cache** — オンチップキャッシュ階層
- **Register File** — 最も高速だが最小
- GPU世代ごとのHBM仕様比較表

| GPU | HBM世代 | VRAM | Memory Bandwidth | Compute (FP8 TFLOPS) |
|-----|---------|------|------------------|---------------------|
| A100 (80GB) | HBM2e | 80 GB | 2.0 TB/s | 624 |
| H100 (SXM) | HBM3 | 80 GB | 3.35 TB/s | 1979 |
| B200 | HBM3e | 144 GB | 8.0 TB/s | 4500 |
| Rubin (2026) | HBM4 | ~288 GB | ~10 TB/s | TBD |

### 2. VRAM Requirements for LLMs

- **推論時のVRAM消費の内訳**:
  - **Model weights**: `params × bytes_per_param` (70B @ FP16 = 140GB)
  - **KV Cache**: `2 × layers × num_heads × head_dim × seq_len × batch × precision_bytes`
  - **Activations**: 中間計算の一時的な格納
  - **Overhead**: CUDA context, scheduler buffers

- モデルサイズ別最小VRAM計算式
- QuantizationがVRAM要件に与える影響

### 3. Memory Bandwidth Bound vs Compute Bound

- **Roofline Model**: 推論時間 = max(compute_time, memory_time)
- Memory bandwidth bound: 低バッチサイズ時、weight fetchが律速
- Compute bound: 高バッチサイズ時、行列演算が律速
- バッチサイズBが `B > 300 × (total_params / active_params)` でクロスオーバー（DeepSeek V3: B > 2400）

### 4. Quantization Effects on VRAM

| Precision | Bytes/Param | 70B Model | 7B Model | Quality Impact |
|-----------|-------------|-----------|----------|----------------|
| FP32 | 4 | 280 GB | 28 GB | Baseline |
| FP16/BF16 | 2 | 140 GB | 14 GB | Negligible |
| FP8 | 1 | 70 GB | 7 GB | Minimal |
| INT8 | 1 | 70 GB | 7 GB | Minimal |
| INT4 (GPTQ/AWQ) | 0.5 | 35 GB | 3.5 GB | Small (~1-2%) |
| NF4 (QLoRA) | 0.5 | 35 GB | 3.5 GB | Small |
| FP4 (MXFP4) | 0.5 | 35 GB | 3.5 GB | Very small |

### 5. Batching Fundamentals

- **Static batching**: 固定サイズのバッチを同時処理
- **Continuous batching**: vLLMが採用、各シーケンスの完了を待たずに次のリクエストをバッチに追加
- **Chunked prefill**: 長いプリフィルを分割してデコードとインターリーブ
- **Batch Size Economics**: バッチサイズ増加に伴うスループットの飽和曲線
- **20ms Batch Train**: HBM容量 / HBM帯域幅 ≈ 15-20msの自然な定数（Reiner Pope）

### 6. GPU Selection Guide

- ユースケース別推奨GPU
  - **Training (70B+)**: H100/B200, 8-GPU clusters
  - **Production Serving**: A100/H100 with large batch sizes
  - **Local / Dev**: RTX 4090 (24GB), RTX 5090 (32GB), M-series Ultra
  - **Budget**: RTX 3090 (24GB), M4 Max

### 7. Multi-GPU Topologies

- **NVLink / NVSwitch**: High-speed GPU interconnect
- **PCIe**: ボトルネックとなりうる世代間の帯域幅差
- **InfiniBand / RoCE**: クラスタ間接続
- **NUMA Affinity**: CPU-GPUメモリ配置の最適化

## Key References

- [GPU Memory Bandwidth and Roofline Analysis](https://arxiv.org/abs/2004.13742) (Reiner Pope's framework)
- NVIDIA H100/H200/B200 Technical Specifications
- vLLM documentation on PagedAttention memory savings

## TODO

- [ ] Add GPU architecture block diagrams
- [ ] Add VRAM calculator formula with examples
- [ ] Detail continuous batching implementation mechanics
- [ ] Add MIG (Multi-Instance GPU) partitioning
- [ ] Add GPU generation comparison (Ampere → Hopper → Blackwell → Rubin)
- [ ] Link to specific model VRAM requirements tables
- [ ] Add NCCL topology implications for multi-node

## Related Pages

- [[concepts/llm-inference]] — Roofline analysis, batch size economics
- [[concepts/local-llm/inference-hardware]] — Consumer hardware specifics
- [[concepts/model-quantization]] — Quantization methods & tradeoffs
- [[concepts/kv-cache]] — VRAMの主要消費源
- [[concepts/ai-infrastructure-engineering/_index]] — Parent page
