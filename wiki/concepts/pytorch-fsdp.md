---
title: "PyTorch FSDP (Fully Sharded Data Parallel)"
type: concept
created: 2026-05-04
updated: 2026-05-04
tags:
  - distributed-training
  - pytorch
  - fsdp
  - sharding
  - memory-optimization
aliases: [fsdp, fully-sharded-data-parallel, zero3, zero-redundancy-optimizer]
related:
  - concepts/fine-tuning/pytorch-fsdp
  - concepts/qlora
  - concepts/deepspeed
  - concepts/peft-fine-tuning
sources:
  - raw/articles/2024-03_answerai-fsdp-qlora-benchmarks.md
  - raw/articles/2026-05-04_phil-schmid-fsdp-qlora-llama3.md
  - https://github.com/AnswerDotAI/fsdp_qlora
---

# PyTorch FSDP (Fully Sharded Data Parallel)

PyTorch FSDP (Fully Sharded Data Parallel) implements the **ZeRO (Zero Redundancy Optimizer) Stage 3** algorithm to shard model parameters, gradients, and optimizer states across multiple GPUs. By eliminating redundant memory copies, FSDP enables training models that would otherwise exceed single-GPU memory limits — scaling from consumer GPUs to large clusters.

FSDP is the successor to FairScale's FSDP, integrated directly into PyTorch core since PyTorch 2.0. It leverages PyTorch's SDPA (Scaled Dot Product Attention) with Flash Attention v2 for efficient attention computation.

---

## Architecture: ZeRO‑3 and Sharding Strategies

### How FSDP Works

At each step during training, FSDP performs a **scatter-gather** cycle:

1. **Forward pass:** Each GPU gathers (all-gather) the sharded parameters for the current layer, computes the forward pass, then discards (reshards) non-owned parameters — keeping only the current layer's parameters in GPU memory.
2. **Backward pass:** Parameters are gathered again for gradient computation. Gradients are reduced and sharded across GPUs, so each GPU stores only its assigned gradient shard.
3. **Optimizer step:** Each GPU updates only its own parameter shard using its local optimizer state — no optimizer state duplication.

### Sharding Strategies

| Strategy | ZeRO Level | What's Sharded | Memory Savings | Communication Cost |
|---|---|---|---|---|
| `full_shard` | ZeRO‑3 | Parameters, gradients, optimizer states | Highest (scales linearly with N GPUs) | Highest |
| `shard_grad_op` | ZeRO‑2 | Gradients, optimizer states only | Medium | Medium |
| `hybrid_shard` | Hybrid | Sharding within nodes, DDP across nodes | Tunable | Tunable |
| `NO_SHARD` | DDP | Nothing | None (DDP equivalent) | None |

#### `full_shard` (ZeRO‑3)
The default and most aggressive sharding. Each GPU holds only `1 / N` of the model. Parameters are re-gathered on demand during forward/backward passes. Best for models that don't fit in single-GPU memory.

#### `shard_grad_op` (ZeRO‑2)
Keeps full model parameters on every GPU (redundant) but shards gradients and optimizer states. Useful when model parameters fit in GPU memory but optimizer states (e.g., Adam momentum + variance) cause OOM.

#### `hybrid_shard`
Combines FSDP sharding within each node and DDP across nodes. Reduces inter-node communication overhead while still saving memory. Ideal for multi-node training with slower inter-node networking (e.g., 8 GPUs per node with NVLink, Ethernet between nodes).

---

## Memory Hierarchy & Tradeoffs

FSDP's sharding introduces a fundamental tradeoff: **memory savings vs. communication overhead**.

### Theoretical Memory Scaling

For a model with `P` parameters and `N` GPUs, using ZeRO‑3:

```
Total activation memory ≈ O(batch × seq_len × hidden_dim)
Total parameter memory ≈ 2P / N     (parameters + gradients)
Total optimizer memory ≈ 8P / N     (Adam: fp32 states)
```

### Practical Memory Tradeoffs — Llama 3 70B

| Configuration | Minimum GPUs | GPU Memory Per Card | Training Throughput |
|---|---|---|---|
| Full Fine-tuning (bf16) | ~16 × 80 GB (A100/H100) | ~80 GB | Baseline |
| FSDP + LoRA | ~8 × 80 GB | ~30-40 GB | ~1.5-2× (fewer params updated) |
| FSDP + Q-LoRA | ~2 × 40 GB (A100) | ~35 GB | ~2-3× (quantized + LoRA) |
| FSDP + Q-LoRA + CPU Offload | 4 × 24 GB (RTX 4090 / L40S) | ~20 GB | ~1.5× baseline (CPU transfer bottleneck) |

> **Key insight:** FSDP makes it feasible to fine-tune 70B-class models on consumer hardware (RTX 4090, 24 GB) when combined with quantization and CPU offloading.

---

## FSDP v2 (torch.distributed.fsdp)

PyTorch's native FSDP (FSDP v2, also called FSDP2) is the recommended implementation. Key features:

- **`auto_wrap_policy`:** Automatically determines which submodules to wrap as separate FSDP units. Common policies:
  - `transformer_auto_wrap_policy` — Wraps transformer blocks (recommended for most LLMs)
  - `default_auto_wrap_policy` — Wraps modules based on layer size (good fallback)
  - Custom policies for non-transformer architectures
- **`backward_prefetch`**: `'backward_pre'` prefetches sharded parameters during backward pass, reducing communication latency.
- **`forward_prefetch`**: Prefetches next layer's parameters during forward pass for additional optimization.
- **`state_dict_type`**: `FULL_STATE_DICT` (full checkpoint) vs. `SHARDED_STATE_DICT` (per-GPU sharded checkpoint — reduces memory peak during save).

### Minimal Usage

```python
from torch.distributed.fsdp import (
    FullyShardedDataParallel as FSDP,
    MixedPrecision,
    CPUOffload,
    BackwardPrefetch,
)
from torch.distributed.fsdp.wrap import transformer_auto_wrap_policy

model = FSDP(
    model,
    auto_wrap_policy=transformer_auto_wrap_policy,
    mixed_precision=MixedPrecision(
        param_dtype=torch.bfloat16,
        reduce_dtype=torch.bfloat16,
        buffer_dtype=torch.bfloat16,
    ),
    cpu_offload=CPUOffload(offload_params=True),
    backward_prefetch=BackwardPrefetch.BACKWARD_PRE,
)
```

---

## CPU Offloading

When GPU memory is extremely constrained, FSDP can offload sharded parameters to CPU RAM:

- **Effect:** Only the currently active layer's parameters occupy GPU memory; all other shards live in CPU RAM and are swapped in on demand.
- **Tradeoff:** CPU ↔ GPU transfers add latency (PCIe bandwidth bottleneck). Training can be 2–3× slower.
- **Configuration:** `CPUOffload(offload_params=True)` in FSDP constructor.
- **Memory savings:** A 70B model in bf16 requires ~140 GB GPU memory for parameters alone. With CPU offload and 8 GPUs, each GPU holds only ~17.5 GB of active parameters — the rest lives in system RAM (~140 GB total).

### Memory-Efficient Loading

Setting the environment variable `FSDP_CPU_RAM_EFFICIENT_LOADING=1` enables memory-efficient checkpoint loading when using CPU offloading. This prevents double-buffering of parameters during checkpoint restore, reducing peak CPU RAM usage.

---

## Integration with Hugging Face Ecosystem

FSDP is deeply integrated with Hugging Face's training stack:

### Accelerate

The `accelerate` library provides a simplified FSDP configuration interface:

```yaml
# accelerate config (FSDP plugin)
compute_environment: LOCAL_MACHINE
distributed_type: FSDP
fsdp_config:
  fsdp_auto_wrap_policy: TRANSFORMER_BASED_WRAP
  fsdp_transformer_layer_cls_to_wrap: LlamaDecoderLayer
  fsdp_state_dict_type: FULL_STATE_DICT
  fsdp_sharding_strategy: FULL_SHARD
  fsdp_offload_params: true
  fsdp_cpu_ram_efficient_loading: true
  fsdp_activation_checkpointing: true
```

Activate with: `ACCELERATE_USE_FSDP=1`

### Transformers + TRL

FSDP works seamlessly with the `Trainer` (SFTTrainer, DPOTrainer) through Accelerate:

```bash
ACCELERATE_USE_FSDP=1 \
FSDP_CPU_RAM_EFFICIENT_LOADING=1 \
torchrun --nproc_per_node=8 train.py
```

### Axolotl

Axolotl provides a YAML-based FSDP configuration (see [[concepts/fine-tuning/pytorch-fsdp]] for specific config examples).

---

## Comparison with DeepSpeed

| Feature | FSDP (PyTorch Native) | DeepSpeed ZeRO‑3 |
|---|---|---|
| **Integration** | Built into PyTorch, no extra dependency | Separate package (`deepspeed`) |
| **Sharding granularity** | Module-level via `auto_wrap_policy` | Configurable via `zero_optimization` config |
| **CPU offloading** | Yes (`CPUOffload`) | Yes (NVMe offloading also available) |
| **Mixed precision** | Via `MixedPrecision` class | Automatic (bf16/fp16 config) |
| **Activation checkpointing** | `torch.utils.checkpoint` | `activation_checkpointing` |
| **Learning rate scheduler** | Native PyTorch scheduler | DeepSpeed's optimizer/scheduler |
| **Ease of use** | Lower complexity, minimal config | Higher complexity, more tuning knobs |
| **ZeRO stages** | 2 (shard_grad_op), 3 (full_shard) | 1, 2, 3, 3‑offload, Infinity |
| **Pipeline parallelism** | No | Yes (ZeRO + Pipeline) |
| **Autotuning** | Manual | `ds_report` + auto‑tuning |
| **Community support** | PyTorch ecosystem | Broad, mature ecosystem |

**When to choose FSDP:**
- You want minimal dependencies (PyTorch-only)
- Simpler integration with Hugging Face ecosystem
- Single-node or small multi-node training
- LoRA / Q-LoRA fine-tuning on consumer GPUs

**When to choose DeepSpeed:**
- You need ZeRO-3 offload with NVMe
- Pipeline parallelism across many nodes
- Fine-grained tuning of overlapping computation/communication
- Existing investment in DeepSpeed configs

---

## Related Concepts

- **[[concepts/qlora]]** — Combines 4-bit quantization (QLoRA) with FSDP for fine-tuning on consumer GPUs
- **[[concepts/fine-tuning/pytorch-fsdp]]** — Fine-tuning-specific FSDP configuration guide (Axolotl, common issues, NCCL testing)
- **[[concepts/peft-fine-tuning]]** — Parameter-Efficient Fine-Tuning methods (LoRA, Q-LoRA) commonly used alongside FSDP
- **[[concepts/deepspeed]]** — DeepSpeed ZeRO, the alternative distributed training framework
- **[[concepts/fsdp-qlora]]** — The specific technique combining FSDP with QLoRA for memory-efficient training

---

## Common Issues & Troubleshooting

| Problem | Likely Cause | Solution |
|:---|---|---|---|
| OOM during forward | Batch size too large; activation memory peaks | Reduce batch size, enable activation checkpointing |
| OOM during backward | Gradient accumulation buffers | Gradient accumulation, CPU offloading |
| Slow inter-node training | Low NCCL bandwidth | Use `hybrid_shard` to minimize inter-node all-gathers |
| State dict save OOM | `FULL_STATE_DICT` on large model | Use `SHARDED_STATE_DICT` (sharded checkpoint) |
| CUDA out of memory on CPU offload | CPU RAM exhausted under double-buffering | Set `FSDP_CPU_RAM_EFFICIENT_LOADING=1` |
| RuntimeError: unshard expected | Wrong `auto_wrap_policy` for model architecture | Match `transformer_layer_cls_to_wrap` to actual model class |

## DDP vs FSDP: When to Use Which

Answer.AI's benchmark research establishes a clear guideline:

> **If the model + QLoRA fits on a single GPU, use Distributed Data Parallel (DDP) instead of FSDP.** FSDP's all-gather communication overhead for shard reconstruction exceeds its benefits when the model already fits in GPU memory. QLoRA's 4-bit quantization reduces memory footprint enough that many models (7B, 13B) that previously required FSDP now work with DDP on consumer GPUs.

### Progressive Optimization Strategy

Answer.AI recommends escalating memory-saving techniques step by step — never add more than needed:

| Step | Configuration | Method | When to Use |
|:-----|:-------------|:-------|:------------|
| 1 | **Vanilla DDP** | Batch size 1, no memory options | Starting point (model fits single GPU) |
| 2 | **Gradient Checkpointing** | Recompute activations during backward | First memory bottleneck |
| 3 | **SHARD_GRAD_OP (ZeRO-2)** | Shard gradients + optimizer only | Parameters fit GPU, optimizer states OOM |
| 4 | **FULL_SHARD (ZeRO-3)** | Shard params + gradients + optimizer | Model doesn't fit single-GPU memory |
| 5 | **CPU Offloading** | Move shards to CPU RAM when inactive | Extreme VRAM constraints (24GB cards for 70B) |
| 6 | **Activation Offloading** | Move intermediate activations to CPU RAM | Last resort (single 16GB GPU) |

> **Key strategy:** Once stable at batch size 1, try increasing batch size. Moving to a heavier memory-saving step may be faster overall if it enables a significantly larger effective batch size.

---

## Sources

- [PyTorch FSDP Documentation](https://pytorch.org/docs/stable/fsdp.html)
- [FSDP2 (FSDP v2) RFC](https://github.com/pytorch/pytorch/issues/114299)
- Phil Schmid, "FSDP + Q-LoRA + Llama 3" (raw/articles/2026-05-04_phil-schmid-fsdp-qlora-llama3.md)
- [Hugging Face Accelerate FSDP Guide](https://huggingface.co/docs/accelerate/usage_guides/fsdp)
- [FairScale FSDP Origin](https://fairscale.readthedocs.io/en/latest/api/fairscale.nn/fsdp.html)
