---
title: "Distributed Training — DDP / FSDP / DeepSpeed"
type: concept
created: 2026-05-01
updated: 2026-05-01
tags:
  - concept
  - training
  - infrastructure
status: L1
aliases:
  - distributed-training
  - ddp-fsdp-deepspeed
  - 3d-parallelism
  - model-parallelism
sources: []
related:
  - "[[concepts/pytorch-fsdp-distributed-training]]"
  - "[[concepts/post-training/pytorch-fsdp]]"
  - "[[concepts/post-training/peft-lora-qlora]]"
  - "[[concepts/llm-inference]]"
  - "[[concepts/training-infra/gpu-vram-fundamentals]]"
  - "[[concepts/training-infra/_index]]"
---

# Distributed Training — DDP / FSDP / DeepSpeed

> A comprehensive guide to parallelization strategies for large-scale LLM distributed training. Understanding the memory-efficiency and compute-efficiency tradeoffs from DDP to FSDP to DeepSpeed ZeRO.

## Why This Matters

The model size trainable on a single GPU is limited by physical VRAM constraints. Training a 70B model in BF16 requires 140GB+ of VRAM, which is barely feasible even on the largest single GPU (B200: 144GB). Distributed parallelization is essential, and selecting the right strategy directly impacts training cost and time.

## Outline

### 1. Fundamental Parallelization Dimensions (3D Parallelism)

```
                     Data Parallel
                    /      |      \
         Tensor Parallel    |    Pipeline Parallel
                    \      |      /
                 Expert Parallel (MoE only)
```

| Method | What is split | Communication | Main use case |
|------|---------|--------|-----------------|
| **Data Parallel (DDP)** | Data | Low (gradients only) | When model fits on 1 GPU |
| **FSDP (ZeRO-based)** | Parameters + gradients + optimizer | Medium (shard communication) | When model doesn't fit on 1 GPU |
| **Tensor Parallel** | Tensor dimensions | High (all activations) | Within a single node, fast NVLink |
| **Pipeline Parallel** | Transformer layers | Low (activation boundaries only) | When model is too large |
| **Expert Parallel** | MoE experts | Medium (all-to-all) | MoE models only |

### 2. Data Distributed Parallel (DDP)

- Each GPU holds a complete model copy, processing different data shards
- After independent forward/backward passes, synchronize gradients via all-reduce
- **Limitation**: Full model must fit in a single GPU's VRAM
- **Pros**: Simple implementation, low communication overhead
- **Cons**: High VRAM consumption (infeasible for 70B models)

### 3. Fully Sharded Data Parallel (FSDP)

- Shards model parameters, gradients, and optimizer states across all GPUs
- Collects only the parameters needed for each forward pass via all-gather (**unshard**)
- Discards shards after computation
- Three levels of `sharding_strategy`:
  - `NO_SHARD` = Equivalent to DDP
  - `SHARD_GRAD_OP` = Shard optimizer states only
  - `FULL_SHARD` = Shard all parameters + gradients + optimizer (equivalent to ZeRO-3)

**FSDP Trade-offs**:
- Memory savings: ~70% (140GB → 2.5GB/GPU @ 64 GPUs for a 70B model)
- Communication overhead: Approximately constant, scales well
- CPU Offload: Further memory reduction possible (but 10-30x slower)

### 4. DeepSpeed ZeRO (ZeRO-1/2/3)

Microsoft DeepSpeed's three-stage optimization:

| Stage | Shard target | Memory reduction | Communication | When to use |
|-------|-----------|-----------|--------|-----------|
| **ZeRO-1** | Optimizer states only | 4x | Low | When optimizer states dominate |
| **ZeRO-2** | Optimizer + Gradients | 8x | Medium | Recommended default |
| **ZeRO-3** | Optimizer + Gradients + Parameters | For memory-intensive models | High (all-gather per layer) | When model doesn't fit in VRAM |

**DeepSpeed Additional Features**:
- **ZeRO-Offload**: Offload optimizer states to CPU/NVMe
- **ZeRO-Infinity**: Store entire model on CPU/NVMe, load only required layers to GPU
- **Mixture of Experts (MoE)**: Expert parallelism via DeepSpeed-MoE
- **Autotuning**: Automatic parallelization strategy selection

### 5. Pipeline Parallelism

- Place different Transformer layer groups on separate GPUs
- Each GPU computes only its assigned layers
- **Problem**: How to minimize pipeline bubbles (idle time)
- **Solutions**: GPipe (micro-batch splitting), 1F1B (One-Forward-One-Backward)

### 6. Tensor Parallelism

- Split a single tensor operation (e.g., attention QKV) across GPUs
- Megatron-LM style: row/column parallel splitting
- **Setup**: Intra-node (NVLink required), needs high communication bandwidth

### 7. Strategy Selection Guide

| Model Size | Recommended Strategy | Reason |
|-------------|---------|------|
| ≤ 7B | DDP or FSDP NO_SHARD | Fits on single GPU, simple and fast |
| 7B-30B | FSDP FULL_SHARD | Balance of memory efficiency and scalability |
| 30B-100B | FSDP + Tensor Parallel | Large model, TP reduces degenerate dimensions |
| 100B+ (Dense) | FSDP + TP + PP (3D) | 3D optimization essential |
| MoE (100B+) | FSDP + TP + EP | Expert Parallel adds another dimension |

### 8. Practical Configuration Examples

- **70B model / 8x H100 (80GB)**:
  - FSDP FULL_SHARD + CPU Offload → Feasible (but slow)
  - FSDP + TP=2 → Efficient (smaller shards per GPU)
  
- **7B model / 4x A100 (40GB)**:
  - FSDP FULL_SHARD or DDP → Both feasible
  - Even more efficient with LoRA/QLoRA

- **DeepSpeed ZeRO-3 + Offload**:
  - Theoretically possible to fine-tune a 70B model on a single consumer GPU
  - Approximately 1/30th the speed of an H100

## Related Pages

- [[concepts/pytorch-fsdp-distributed-training]] — Stub → FSDP details
- [[concepts/post-training/pytorch-fsdp]] — FSDP fine-tuning specifics
- [[concepts/post-training/peft-lora-qlora]] — Combining with PEFT methods
- [[concepts/post-training/trl]] — TRL training with distributed configs
- [[concepts/training-infra/gpu-vram-fundamentals]] — GPU VRAM constraint fundamentals
- [[concepts/training-infra/_index]] — Parent page

## Skills Reference

- `pytorch-fsdp` — FSDP distributed training setup
- `axolotl` — Axolotl fine-tuning with FSDP configs
- `fine-tuning-with-trl` — TRL with distributed backends

## Key Resources

- [PyTorch FSDP Documentation](https://pytorch.org/docs/stable/fsdp.html)
- [DeepSpeed Documentation](https://www.deepspeed.ai/)
- [Megatron-LM](https://github.com/NVIDIA/Megatron-LM)
- [NVIDIA NCCL Documentation](https://developer.nvidia.com/nccl)

## TODO

- [ ] Add concrete FSDP config snippets (sharding_strategy, limit_all_gathers)
- [ ] Add DeepSpeed ZeRO config example (ds_config.json)
- [ ] Add 3D parallelism topology diagram
- [ ] Add benchmark comparison: DDP vs FSDP vs DeepSpeed for same model
- [ ] Add NCCL performance tuning tips (NVLink vs PCIe)
- [ ] Add CPU/NVMe Offload performance benchmarks
- [ ] Add DeepSpeed-MoE specific guidance
