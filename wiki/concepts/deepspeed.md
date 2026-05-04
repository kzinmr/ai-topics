---
title: "Microsoft DeepSpeed"
type: concept
created: 2026-05-04
updated: 2026-05-04
tags:
  - distributed-training
  - deepspeed
  - microsoft
  - zeRO
  - memory-optimization
  - model-parallelism
  - moe
aliases:
  - deepspeed
  - zeRO
  - zero-redundancy-optimizer
  - deepspeed-zeRO
  - zeRO-infinity
related:
  - concepts/pytorch-fsdp
  - concepts/fsdp-qlora
  - concepts/accelerate
  - concepts/ai-infrastructure-engineering/distributed-training
  - concepts/fine-tuning/peft-lora-qlora
sources:
  - https://github.com/deepspeedai/DeepSpeed
  - https://www.deepspeed.ai/
  - raw/articles/2026-05-04_accelerate-fsdp-deepspeed-guide.md
  - https://huggingface.co/docs/accelerate/en/concept_guides/fsdp_and_deepspeed
---

# Microsoft DeepSpeed

**DeepSpeed** is an open-source deep learning optimization library developed by Microsoft as part of its **AI at Scale** initiative. It provides a comprehensive suite of memory and throughput optimizations for training and inference of large models, enabling scaling from single-GPU fine-tuning up to trillion-parameter distributed training. DeepSpeed is the distributed engine behind models such as MT-530B (Megatron-Turing NLG), BLOOM (176B), and Jurassic-1 (178B).

---

## ZeRO: Zero Redundancy Optimizer

The core innovation in DeepSpeed is the **Zero Redundancy Optimizer (ZeRO)** family of memory optimization techniques. ZeRO eliminates memory redundancy across data-parallel processes by partitioning model states — parameters, gradients, and optimizer states — instead of replicating them on every GPU.

### ZeRO Stages

| Stage | What Is Partitioned | Memory Savings | Communication Cost | Typical Use Case |
|:------|:-------------------|:---------------|:------------------|:-----------------|
| **ZeRO-1** | Optimizer states only | 4× reduction (Adam states) | Minimal | Models that fit GPU memory but OOM on optimizer states |
| **ZeRO-2** | Optimizer states + gradients | 8× reduction | Low | Training large models where gradient memory is a bottleneck |
| **ZeRO-3** | Optimizer states + gradients + parameters | Linear with N GPUs | High (all-gather per layer) | Models that don't fit in single-GPU memory |
| **ZeRO-3 Offload** | All states + CPU/NVMe offload | Beyond GPU memory limit | Very high (PCIe/disk transfer) | Gigantic models on limited GPU hardware |
| **ZeRO-Infinity** | All states + CPU + NVMe + heterogeneous memory | Unlimited (scales to any memory tier) | Highest | Trillion-parameter training across GPU, CPU, and NVMe |

#### ZeRO-1
Partitions only the **optimizer states** (e.g., Adam momentum and variance, stored in fp32). Each GPU maintains `1/N` of the total optimizer states. Parameters and gradients remain fully replicated. Best for cases where model parameters fit in GPU VRAM but the optimizer's fp32 copy causes OOM.

#### ZeRO-2
Extends ZeRO-1 by also partitioning **gradients**. Each GPU stores only its assigned gradient shard. The full gradient is reduced via a **reduce-scatter** operation (not all-reduce), eliminating redundant gradient storage. This is the sweet spot for many moderate-to-large models.

#### ZeRO-3
Also partitions **model parameters** across GPUs. During forward/backward passes, parameters are **all-gathered** on demand for the current layer and then discarded. Each GPU holds only `1/N` of the total parameters. This enables training models that exceed the memory of any single GPU.

#### ZeRO-3 Offload
Extends ZeRO-3 by offloading parameter shards, optimizer states, or both to **CPU RAM** or **NVMe storage** when not actively needed. The tradeoff is significantly higher latency for data movement across PCIe or storage buses. DeepSpeed supports **granular offloading** — choosing independently which components (parameters vs. optimizer states) to offload, unlike FSDP's "all-or-nothing" offloading.

#### ZeRO-Infinity
A breakthrough technique that **breaks the GPU memory wall** by leveraging all available memory tiers: GPU HBM, CPU DRAM, and NVMe SSD. It enables training models with hundreds of billions of parameters on as few as a single GPU by dynamically moving data across the memory hierarchy. Key innovations include:

- **Infinite offloading engine** — seamless data movement across GPU, CPU, and NVMe
- **Bandwidth-efficient partitioning** — minimizes cross-tier data movement
- **Overlapped communication** — hides data movement latency behind computation
- **Memory-centric tiling** — tiles operations to fit within GPU memory budgets

> **ZeRO-Infinity** is the engine that made trillion-parameter model training feasible with commodity hardware, not just specialized supercomputing clusters.

---

## Key Features

### 3D-Parallelism

DeepSpeed combines three forms of parallelism to scale training across thousands of GPUs:

| Parallelism | What It Does | DeepSpeed Integration |
|:------------|:-------------|:----------------------|
| **Data Parallelism (DP)** | Replicates the model across GPUs, splits batches | ZeRO-enhanced DP with partitioned states |
| **Model Parallelism (MP)** | Splits individual layers across GPUs | Tensor-slicing integration |
| **Pipeline Parallelism (PP)** | Splits layers across stages, processes micro-batches | DeepSpeed Pipeline Engine |

The combination — **3D-Parallelism** — allows scaling to thousands of GPUs by optimizing each parallelism dimension independently. DeepSpeed's pipeline scheduling (1F1B, iterative pipelining) overlaps computation across pipeline stages to minimize idle bubbles.

### DeepSpeed-MoE (Mixture of Experts)

Advanced **Mixture-of-Experts** training and inference support:

- **MoE layers** replace dense feed-forward networks with multiple expert sub-networks, routed via a learned gating function
- **PR-MoE (Pyramid-Residual MoE)** — improves expert utilization
- **ZeRO-integrated MoE** — shards expert parameters across data-parallel groups
- **Inference optimizations** — expert-parallel serving for MoE models

DeepSpeed-MoE was used to train models with trillions of parameters using sparse expert activation.

### Compression Suite

| Technique | Description |
|:----------|:------------|
| **ZeroQuant** | Post-training quantization (INT8/INT4) with minimal accuracy loss |
| **Extreme Compression** | Combines pruning, quantization, and knowledge distillation |
| **Structured Pruning** | Removes redundant heads, layers, or embedding dimensions |

### CUDA++ Optimizations

- **Fused AdamW optimizer** — kernel fusion reduces launch overhead
- **Fused compute and communication** — overlaps all-gather/reduce-scatter with computation
- **Stochastic rounding** — enables fp16 gradient accumulation without overflow
- **Sparse attention kernels** — optimized for MoE gating and sparse transformer patterns

### ZeRO++ (Communication Optimization)

- **Quantized weights** (INT8/INT4) for all-gather — reduces communication volume
- **Hierarchical partitioning** — reduces all-gather frequency
- **hpZ (hierarchical partitioning ZeRO)** — partitions parameters across both intra- and inter-node boundaries to minimize cross-node communication

---

## Accelerate Integration

Hugging Face `accelerate` provides a plugin-based integration for DeepSpeed. This is the recommended way to use DeepSpeed within the Hugging Face ecosystem.

### DeepSpeedPlugin

```python
from accelerate import Accelerator
from accelerate.utils import DeepSpeedPlugin

# Basic usage
ds_plugin = DeepSpeedPlugin(zero_stage=3)

# Full config
ds_plugin = DeepSpeedPlugin(
    zero_stage=3,
    gradient_accumulation_steps="auto",
    gradient_clipping="auto",
    offload_optimizer_device="cpu",
    offload_param_device="nvme",
    offload_param_nvme_path="/nvme/deepspeed"
)

accelerator = Accelerator(
    deepspeed_plugin=ds_plugin
)
```

Or provide a complete DeepSpeed JSON config:

```python
from accelerate import Accelerator
from accelerate.utils import DeepSpeedPlugin

ds_plugin = DeepSpeedPlugin(hf_ds_config="ds_config.json")
accelerator = Accelerator(deepspeed_plugin=ds_plugin)
```

### Accelerate Config (CLI)

```yaml
compute_environment: LOCAL_MACHINE
distributed_type: DEEPSPEED
deepspeed_config:
  zero_stage: 3
  offload_optimizer_device: cpu
  offload_param_device: nvme
  gradient_accumulation_steps: auto
  gradient_clipping: auto
  zero3_init_flag: true
  zero3_save_16bit_model: true
```

### Accelerate Configuration Mapping

| Feature | DeepSpeed Argument | FSDP Argument | Notes |
|:--------|:------------------|:--------------|:------|
| Strategy | `zero_stage` | `fsdp_sharding_strategy` | ZeRO Stage 3 ≈ FSDP FULL_SHARD |
| Offloading | `offload_param_device`, `offload_optimizer_device` | `fsdp_offload_params` | DS: granular; FSDP: all-or-nothing |
| RAM Efficiency | `zero3_init_flag` | `fsdp_cpu_ram_efficient_loading` | Only for ZeRO-3 / Full Shard |
| Checkpointing | `zero3_save_16bit_model` | `fsdp_state_dict_type` | DS consolidates to single rank if true |
| Prefetching | Automatic / Config-based | `fsdp_forward_prefetch` | DS automated, FSDP manual |
| Auto-Wrapping | Transparent | `fsdp_auto_wrap_policy` | DS handles wrapping internally |

### Memory Handling (Accelerate Comparison)

A critical difference from the Accelerate concept guide:

| Process | FSDP | DeepSpeed |
|:--------|:-----|:----------|
| **Preparation** | Created in `torch_dtype` | Disregards `torch_dtype`, created in **fp32** |
| **Optimizer Init** | Parameters in `torch_dtype` | Parameters in **fp32** |
| **Optimizer Step** | Occurs in `torch_dtype` | Occurs in **fp32** |

> **Key Insight:** DeepSpeed upcasts parameters to fp32 during model preparation, which can lead to higher memory overhead on small GPU counts compared to FSDP. This is an intentional design choice to ensure stable training with automatic mixed precision.

### Training Parameter Flags

DeepSpeed requires explicit configuration for:
- `gradient_accumulation_steps: "auto"` — set in `deepspeed_config`
- `gradient_clipping: "auto"` — set in `deepspeed_config`

These are transparent in FSDP (handled automatically by accelerate).

---

## DeepSpeed vs FSDP

### Summary Comparison

| Dimension | DeepSpeed ZeRO-3 | PyTorch FSDP |
|:----------|:-----------------|:-------------|
| **Package** | Separate (`deepspeed`) | Built into PyTorch |
| **ZeRO Stages** | 1, 2, 3, 3-offload, Infinity | 2 (`shard_grad_op`), 3 (`full_shard`) |
| **Offloading** | CPU + NVMe, granular per-component | CPU only, all-or-nothing |
| **Pipeline Parallelism** | Yes (3D-Parallelism) | No |
| **MoE Training** | Yes (DeepSpeed-MoE) | No native support |
| **Autotuning** | `ds_report` + auto-tuning | Manual tuning |
| **Ease of Use** | Higher complexity, many tuning knobs | Lower complexity, minimal config |
| **Memory Overhead** | Higher (fp32 upcast during prep) | Lower (stays in `torch_dtype`) |
| **Community** | Broad, mature ecosystem | PyTorch ecosystem |
| **Checkpointing** | `zero_to_fp32.py` post-conversion | Native `FULL_STATE_DICT` / `SHARDED_STATE_DICT` |

### When to Use DeepSpeed

- You need **ZeRO-3 offload with NVMe** storage (FSDP does not support NVMe)
- You need **pipeline parallelism** across many nodes
- You want **fine-grained offloading** control (parameters vs. optimizer independently)
- You need **autotuning** capabilities for optimal performance
- You are training **Mixture-of-Experts** models
- You have existing infrastructure and configs built around DeepSpeed

### When to Use FSDP

- You want **minimal dependencies** (PyTorch-only, no extra package)
- You prefer **simpler integration** with Hugging Face ecosystem
- You are doing single-node or small multi-node training
- **LoRA / Q-LoRA fine-tuning on consumer GPUs** (especially with [[concepts/fsdp-qlora]])
- Your priority is **lower memory overhead** on small GPU counts

---

## Notable Models Trained with DeepSpeed

| Model | Size | Milestone |
|:------|:-----|:----------|
| **MT-530B** (Megatron-Turing NLG) | 530B params | NVIDIA + Microsoft collaboration, 3D-Parallelism |
| **BLOOM** | 176B params | BigScience open-science initiative |
| **Jurassic-1** (AI21 Labs) | 178B params | Production LLM at scale |
| **GLM-130B** (Tsinghua) | 130B params | Open-source bilingual LLM |
| **GPT-NeoX-20B** (EleutherAI) | 20B params | Open-source GPT-Neo successor |

---

## Recent Research & Development (2025–2026)

| Publication | Year | Description |
|:------------|:-----|:------------|
| **ZeRO** (Original) | 2019 | Foundational paper on Zero Redundancy Optimizer |
| **ZeRO-Offload** | 2021 | Democratizing billion-scale model training |
| **DeepSpeed-Chat** | 2023 | RLHF training at scale (ChatGPT-like) |
| **Universal Checkpointing** | 2024 | Model-agnostic checkpoint format across frameworks |
| **SuperOffload** | 2026 (ASPLOS) | Next-generation offloading with learned memory tier management |
| **ZenFlow** | 2026 | CPU binding and NUMA-aware memory management for DeepSpeed |
| **Arctic Long Sequence Training** | 2026 | Training with sequences exceeding 1M tokens |

---

## Related Concepts

- **[[concepts/pytorch-fsdp]]** — PyTorch's native FSDP, the primary alternative to DeepSpeed ZeRO
- **[[concepts/fsdp-qlora]]** — FSDP combined with Q-LoRA for memory-efficient fine-tuning
- **[[concepts/accelerate]]** — Hugging Face Accelerate, which provides plugins for both FSDP and DeepSpeed
- **[[concepts/ai-infrastructure-engineering/distributed-training]]** — Distributed training methodologies overview
- **[[concepts/fine-tuning/peft-lora-qlora]]** — PEFT methods commonly used alongside DeepSpeed

---

## Key Resources

- [DeepSpeed GitHub](https://github.com/deepspeedai/DeepSpeed) — Source code, issues, releases
- [DeepSpeed Documentation](https://www.deepspeed.ai/) — Official docs, tutorials, config reference
- [Hugging Face Accelerate: FSDP vs DeepSpeed Guide](https://huggingface.co/docs/accelerate/en/concept_guides/fsdp_and_deepspeed) — Official comparison guide
- [ZeRO: Memory Optimizations Toward Training Trillion Parameter Models](https://arxiv.org/abs/1910.02054) — Original ZeRO paper (2019)
- [ZeRO-Offload: Democratizing Billion-Scale Model Training](https://arxiv.org/abs/2101.06840) — ZeRO-Offload paper (2021)
- [DeepSpeed: System Optimizations Enable Training Deep Learning Models with Over 100 Billion Parameters](https://dl.acm.org/doi/10.1145/3394486.3403203) — KDD 2020
