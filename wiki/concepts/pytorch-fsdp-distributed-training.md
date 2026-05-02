---
title: "PyTorch FSDP — Distributed Training"
type: concept
created: 2026-04-25
updated: 2026-05-01
tags:
  - concept
  - training
  - fsdp
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

> PyTorch Fully Sharded Data Parallel (FSDP) は、モデルパラメータ・勾配・optimizer状態を全GPU間でシャーディングすることで、大規模モデルのトレーニングを可能にする分散学習戦略。

## Overview

FSDPはDeepSpeed ZeRO-3に触発されたPyTorchネイティブの分散学習手法。従来のDDP（Data Distributed Parallel）が各GPUに完全なモデルコピーを保持するのに対し、FSDPはパラメータをシャードして全GPUに分散する。これにより、単一GPUのVRAM制限を数十倍に拡張できる。

### Core Concept: Parameter Sharding

DDP: `[params A][params A][params A][params A]` — 各GPUが完全なコピー
FSDP: `[p1][p2][p3][p4]` — パラメータが分割されて分散

### Sharding Strategies

| Strategy | Shard対象 | メモリ節約 | 通信コスト | いつ使うか |
|----------|----------|-----------|-----------|-----------|
| `NO_SHARD` | なし（DDP相当） | 0% | 低 | モデルが1GPUに収まる |
| `SHARD_GRAD_OP` | optimizer状態 + 勾配 | ~50% | 中 | 7-13Bモデル |
| `FULL_SHARD` | パラメータ + 勾配 + optimizer | ~70%+ | 高 | 13B+モデル推奨 |

### Memory Savings Example (70B model, 8x H100 80GB)

DDP: 各GPUに140GBのパラメータ → VRAM超過 ❌
FSDP FULL_SHARD: 各GPUに140GB/8 = 17.5GBのパラメータ ✅

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

FSDPは、GPU VRAMが不足する場合にパラメータをCPUメモリにオフロードできる:
```python
from torch.distributed.fsdp import CPUOffload

fsdp_model = FSDP(
    model,
    cpu_offload=CPUOffload(offload_params=True),
    ...
)
```
- 70Bモデルを1台のH100で学習可能になるが、速度はCPU⇔GPU転送で制限（約1/10〜1/30）

## Relationship to DeepSpeed

| 観点 | FSDP | DeepSpeed ZeRO-3 |
|------|------|-----------------|
| **エコシステム** | PyTorchネイティブ | 独立ライブラリ |
| **設定** | Python API | ds_config.json |
| **CPUオフロード** | あり | ZeRO-Offload / Infinity |
| **MoE** | なし | DeepSpeed-MoE |
| **オーバーラップ** | forward_prefetch | ZeRO-3設定で自動 |
| **コミュニティ** | 広い | 大規模学習で実績 |

## When to Use

- **Model 7B-70B on 4-64 GPUs**: FSDP FULL_SHARD
- **Model 70B+ on many GPUs**: FSDP + Tensor Parallel (3D)
- **Single consumer GPU**: FSDP + CPU Offload (遅いが可能)
- **MoE models**: DeepSpeed-MoE推奨（FSDP非対応）

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
