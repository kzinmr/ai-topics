---
title: "PyTorch FSDP — Distributed Training"
created: 2026-04-19
updated: 2026-04-19
tags: [fine-tuning, distributed-training, pytorch, fsdp, sharding]
related:
  - concepts/fine-tuning/_index
  - concepts/fine-tuning/axolotl
  - concepts/inference/_index
---

# PyTorch FSDP (Fully Sharded Data Parallel)

FSDP enables distributed training of large models by sharding model parameters, gradients, and optimizer states across multiple GPUs.

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

Validate network performance before distributed training:

```bash
./build/all_reduce_perf -b 8 -e 128M -f 2 -g 3
```

## Related

- [[concepts/fine-tuning/axolotl.md]] — Axolotl FSDP integration
- [[concepts/fine-tuning/unsloth.md]] — Alternative memory optimization
- [[concepts/inference/vllm.md]] — Production serving post-training

## Sources

- [PyTorch FSDP Documentation](https://pytorch.org/docs/stable/fsdp.html)
- [FSDP2 (FSDP v2) RFC](https://github.com/pytorch/pytorch/issues/114299)
- [Axolotl FSDP Guide](https://axolotl-ai-cloud.github.io/axolotl/)
