---
title: "PyTorch FSDP — Distributed Training"
type: concept
created: 2026-04-25
updated: 2026-05-27
tags:
  - concept
  - training
  - pytorch
  - infrastructure
status: L1
aliases:
  - pytorch-fsdp-distributed-training
  - pytorch-fsdp
related:
  - "[[concepts/ai-infrastructure-engineering/distributed-training]]"
  - "[[concepts/fine-tuning/pytorch-fsdp]]"
  - "[[concepts/fine-tuning/peft-lora-qlora]]"
  - "[[concepts/ai-infrastructure-engineering/_index]]"
sources:
  - "https://pytorch.org/docs/stable/fsdp.html"
  - "https://pytorch.org/blog/introducing-pytorch-fully-sharded-data-parallel-api/"
---

# PyTorch FSDP — Distributed Training

> PyTorch Fully Sharded Data Parallel (FSDP) is a distributed training strategy that enables large-scale model training by sharding model parameters, gradients, and optimizer states across all GPUs.

## Overview

FSDP is a PyTorch-native distributed training method inspired by DeepSpeed ZeRO-3. While traditional DDP (Data Distributed Parallel) keeps a complete model copy on each GPU, FSDP shards parameters and distributes them across all GPUs. This can expand a single GPU's effective VRAM limit by tens of times.

### Core Concept: Parameter Sharding

DDP: `[params A][params A][params A][params A]` — Each GPU has a complete copy
FSDP: `[p1][p2][p3][p4]` — Parameters are split and distributed

### Sharding Strategies

| Strategy | Shard Target | Memory Savings | Communication Cost | When to Use |
|----------|----------|-----------|-----------|-----------|
| `NO_SHARD` | None (equivalent to DDP) | 0% | Low | Model fits on one GPU |
| `SHARD_GRAD_OP` | Optimizer state + gradients | ~50% | Medium | 7-13B models |
| `FULL_SHARD` | Parameters + gradients + optimizer | ~70%+ | High | Recommended for 13B+ models |

### Memory Savings Example (70B model, 8x H100 80GB)

DDP: 140GB of parameters per GPU → Exceeds VRAM ❌
FSDP FULL_SHARD: 140GB/8 = 17.5GB of parameters per GPU ✅

### Key Configuration Parameters

```python
from torch.distributed.fsdp import (
    FullyShardedDataParallel as FSDP,
    ShardingStrategy,
    MixedPrecision,
)

fsdp_model = FSDP(
    model,
    sharding_strategy=ShardingStrategy.FULL_SHARD,
    mixed_precision=MixedPrecision(
        param_dtype=torch.bfloat16,
        reduce_dtype=torch.bfloat16,
        buffer_dtype=torch.bfloat16,
    ),
    auto_wrap_policy=transformer_auto_wrap_policy,
    limit_all_gathers=True,
    forward_prefetch=True,
)
```

### CPU Offload

FSDP can offload parameters to CPU memory when GPU VRAM is insufficient:
```python
from torch.distributed.fsdp import CPUOffload

fsdp_model = FSDP(
    model,
    cpu_offload=CPUOffload(offload_params=True),
    ...
)
```
- Enables training a 70B model on a single H100, but speed is limited by CPU⇔GPU transfer (approximately 1/10 to 1/30)

## Relationship to DeepSpeed

| Aspect | FSDP | DeepSpeed ZeRO-3 |
|------|------|-----------------|
| **Ecosystem** | PyTorch native | Independent library |
| **Config** | Python API | ds_config.json |
| **CPU Offload** | Yes | ZeRO-Offload / Infinity |
| **MoE** | No | DeepSpeed-MoE |
| **Overlap** | forward_prefetch | Automatic in ZeRO-3 config |
| **Community** | Broad | Proven in large-scale training |

## When to Use

- **Model 7B-70B on 4-64 GPUs**: FSDP FULL_SHARD
- **Model 70B+ on many GPUs**: FSDP + Tensor Parallel (3D)
- **Single consumer GPU**: FSDP + CPU Offload (slow but possible)
- **MoE models**: DeepSpeed-MoE recommended (FSDP does not support MoE)

## Related Pages

- [[concepts/ai-infrastructure-engineering/distributed-training]] — Complete distributed training overview
- [[concepts/fine-tuning/pytorch-fsdp]] — FSDP fine-tuning specifics
- [[concepts/ai-infrastructure-engineering/gpu-vram-fundamentals]] — Hardware constraints
- [[concepts/ai-infrastructure-engineering/_index]] — Parent page

## Skills Reference

- `pytorch-fsdp` — FSDP setup and configuration
- `fine-tuning-with-trl` — TRL with FSDP

## TODO

- [ ] Add NCCL timeout and error handling patterns
- [ ] Add `limit_all_gathers` tuning guide
- [ ] Add checkpointing patterns (full-state vs sharded)
- [ ] Add hybrid sharding (FSDP + TP) configuration
- [ ] Add memory profiling with PyTorch Profiler
