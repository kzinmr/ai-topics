---
title: "PyTorch FSDP (Fully Sharded Data Parallel)"
type: concept
created: 2026-04-19
updated: 2026-05-04
tags:
  - fine-tuning
  - training
  - pytorch
  - fsdp
  - sharding
  - distributed-training
  - peft
related:
  - concepts/fine-tuning/_index
  - concepts/fine-tuning/axolotl
  - concepts/inference/_index
  - concepts/fsdp-qlora
  - concepts/qlora
aliases:
  - pytorch-fsdp
  - FSDP
sources:
  - raw/articles/2026-05-04_phil-schmid-fsdp-qlora-llama3.md
  - https://pytorch.org/docs/stable/fsdp.html
  - https://www.philschmid.de/fsdp-qlora-llama3
---

# PyTorch FSDP (Fully Sharded Data Parallel)

> **Canonical page moved up.** This subdirectory page was merged into [[concepts/pytorch-fsdp]] for the comprehensive reference. Key content retained below.

**PyTorch FSDP (Fully Sharded Data Parallel)** is a distributed training paradigm that shards model parameters, gradients, and optimizer states across multiple GPUs. It implements the **ZeRO (Zero Redundancy Optimizer) Stage 3** algorithm natively in PyTorch, enabling training of models that would otherwise exceed single-GPU memory.

## Key Features

- **Three sharding strategies:** `full_shard` (ZeRO-3), `hybrid_shard`, `shard_grad_op` (ZeRO-2)
- **CPU offloading:** Move sharded parameters to CPU RAM when not in use
- **Mixed precision:** Seamless bf16/fp16 training with automatic casting
- **SDPA integration:** Uses PyTorch's Scaled Dot Product Attention with Flash Attention v2
- **Hugging Face ecosystem:** Native integration with Accelerate, TRL SFTTrainer, Transformers

## FSDP vs DDP vs DeepSpeed

| Feature | DDP | FSDP | DeepSpeed ZeRO-3 |
|---------|-----|------|------------------|
| Parameter sharding | No | Yes | Yes |
| Gradient sharding | No | Yes | Yes |
| Optimizer state sharding | No | Yes | Yes |
| Activation checkpointing | Manual | Manual | Manual |
| CPU offloading | No | Yes | Yes |
| Complexity | Low | Medium | High |

## FSDP Configuration (Axolotl YAML)

```yaml
fsdp_version: 2
fsdp_config:
  offload_params: true
  state_dict_type: FULL_STATE_DICT
  auto_wrap_policy: TRANSFORMER_BASED_WRAP
  transformer_layer_cls_to_wrap: LlamaDecoderLayer
  reshard_after_forward: true
```

## PyTorch Native FSDP2 (FSDP v2)

```python
from torch.distributed.fsdp import FullyShardedDataParallel as FSDP
from torch.distributed.fsdp import MixedPrecision, CPUOffload

model = FSDP(
    model,
    auto_wrap_policy=transformer_auto_wrap_policy,
    mixed_precision=MixedPrecision(
        param_dtype=torch.bfloat16,
        reduce_dtype=torch.bfloat16,
        buffer_dtype=torch.bfloat16,
    ),
    cpu_offload=CPUOffload(offload_params=True),
)
```

## Memory Optimization

| Technique | Memory Savings | Performance Impact |
|-----------|---------------|-------------------|
| **Parameter sharding** | Scales with N GPUs | Communication overhead |
| **Activation checkpointing** | 4-8x reduction | 20-30% slower |
| **CPU offloading** | Unlimited (by CPU RAM) | 2-3x slower |
| **Mixed precision (bf16)** | 2x reduction | Minimal |

## Common Issues

| Problem | Solution |
|---------|----------|
| OOM during forward | Reduce batch size, enable activation checkpointing |
| OOM during backward | Gradient accumulation, CPU offloading |
| Slow training | Check NCCL bandwidth, use bf16 |
| State dict too large | Use `SHARDED_STATE_DICT` instead of `FULL_STATE_DICT` |

## NCCL Testing

```bash
./build/all_reduce_perf -b 8 -e 128M -f 2 -g 3
```

## Related

- [[concepts/fine-tuning/axolotl]] — Axolotl FSDP integration
- [[concepts/fine-tuning/unsloth]] — Alternative memory optimization
- [[concepts/inference/vllm]] — Production serving post-training

## Sources

- [[concepts/pytorch-fsdp]] — Comprehensive top-level reference
- [PyTorch FSDP Documentation](https://pytorch.org/docs/stable/fsdp.html)
- [FSDP2 (FSDP v2) RFC](https://github.com/pytorch/pytorch/issues/114299)
- [Axolotl FSDP Guide](https://axolotl-ai-cloud.github.io/axolotl/)
