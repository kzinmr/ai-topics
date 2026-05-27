---
title: "GPU / VRAM Fundamentals"
type: concept
created: 2026-05-01
updated: 2026-05-26
tags:
  - concept
  - inference
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
  - "[[concepts/ai-infrastructure-engineering/pytorch-gpu-memory-profiling]]"
---

# GPU / VRAM Fundamentals

> A systematic overview covering GPU architecture basics, VRAM computation for LLM inference, memory bandwidth impact, and the economics of quantization and batch processing.

## Why This Matters

In LLM inference, the GPU is not just a "fast calculator." **Memory bandwidth** is the primary constraint on throughput, and **VRAM capacity** determines the model size, batch size, and context length that can be processed simultaneously. Without understanding these physical constraints, production system optimization is impossible.

## Outline

### 1. GPU Memory Hierarchy

- **HBM (High Bandwidth Memory)** — GPU primary memory; trade-off between capacity and bandwidth
- **SRAM / L1/L2 Cache** — On-chip cache hierarchy
- **Register File** — Fastest but smallest
- HBM specification comparison across GPU generations

| GPU | HBM Generation | VRAM | Memory Bandwidth | Compute (FP8 TFLOPS) |
|-----|---------|------|------------------|---------------------|
| A100 (80GB) | HBM2e | 80 GB | 2.0 TB/s | 624 |
| H100 (SXM) | HBM3 | 80 GB | 3.35 TB/s | 1979 |
| B200 | HBM3e | 144 GB | 8.0 TB/s | 4500 |
| Rubin (2026) | HBM4 | ~288 GB | ~10 TB/s | TBD |

### 2. VRAM Requirements for LLMs

- **VRAM consumption breakdown during inference**:
  - **Model weights**: `params × bytes_per_param` (70B @ FP16 = 140GB)
  - **KV Cache**: `2 × layers × num_heads × head_dim × seq_len × batch × precision_bytes`
  - **Activations**: Temporary storage for intermediate computations
  - **Overhead**: CUDA context, scheduler buffers

- Minimum VRAM calculation formulas by model size
- Impact of quantization on VRAM requirements

### 3. Memory Bandwidth Bound vs Compute Bound

- **Roofline Model**: Inference time = max(compute_time, memory_time)
- Memory bandwidth bound: At low batch sizes, weight fetch is the bottleneck
- Compute bound: At high batch sizes, matrix operations are the bottleneck
- Batch size B crossover occurs at `B > 300 x (total_params / active_params)` (DeepSeek V3: B > 2400)

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

- **Static batching**: Process fixed-size batches simultaneously
- **Continuous batching**: Adopted by vLLM; adds new requests to a batch without waiting for each sequence to complete
- **Chunked prefill**: Splits long prefills to interleave with decoding
- **Batch Size Economics**: Throughput saturation curve as batch size increases
- **20ms Batch Train**: HBM capacity / HBM bandwidth approximates a 15-20ms natural constant (Reiner Pope)

### 6. GPU Selection Guide

- Recommended GPUs by use case
  - **Training (70B+)**: H100/B200, 8-GPU clusters
  - **Production Serving**: A100/H100 with large batch sizes
  - **Local / Dev**: RTX 4090 (24GB), RTX 5090 (32GB), M-series Ultra
  - **Budget**: RTX 3090 (24GB), M4 Max

### 7. Multi-GPU Topologies

- **NVLink / NVSwitch**: High-speed GPU interconnect
- **PCIe**: Bandwidth differences across generations can be a bottleneck
- **InfiniBand / RoCE**: Cluster interconnect
- **NUMA Affinity**: Optimizing CPU-GPU memory placement

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

- [[concepts/ai-infrastructure-engineering/pytorch-gpu-memory-profiling]] — PyTorch built-in GPU memory debugging tool
- [[concepts/llm-inference]] — Roofline analysis, batch size economics
- [[concepts/local-llm/inference-hardware]] — Consumer hardware specifics
- [[concepts/model-quantization]] — Quantization methods & tradeoffs
- [[concepts/kv-cache]] — Major consumer of VRAM
- [[concepts/ai-infrastructure-engineering/_index]] — Parent page
