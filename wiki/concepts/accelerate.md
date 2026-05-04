---
title: "Hugging Face Accelerate"
type: concept
created: 2026-05-04
updated: 2026-05-04
tags:
  - distributed-training
  - huggingface
  - accelerate
  - fsdp
  - deepspeed
  - launcher
aliases:
  - accelerate
  - hf-accelerate
  - huggingface-accelerate
  - accelerate-launch
related:
  - concepts/pytorch-fsdp
  - concepts/fsdp-qlora
  - concepts/qlora
  - concepts/fine-tuning/peft-lora-qlora
  - concepts/fine-tuning/pytorch-fsdp
  - concepts/deepspeed
  - concepts/ai-infrastructure-engineering/distributed-training
  - entities/zach-mueller
sources:
  - raw/articles/2026-05-04_accelerate-fsdp-deepspeed-guide.md
  - https://huggingface.co/docs/accelerate
  - https://huggingface.co/docs/accelerate/en/concept_guides/fsdp_and_deepspeed
---

# Hugging Face Accelerate

**Accelerate** is Hugging Face's unified distributed training library that enables the same PyTorch training code to run on any hardware configuration — single GPU, multi-GPU, CPU, or TPU — with zero code changes. It serves as the **abstraction layer that makes [[concepts/pytorch-fsdp]] and [[concepts/deepspeed]] interchangeable**, allowing practitioners to swap between them via a single CLI flag.

Created and led by **[[entities/zach-mueller|Zach Mueller]]**, a Machine Learning Software Engineer at Hugging Face, Accelerate is the backbone of Hugging Face's training stack — used by Transformers Trainer, TRL SFTTrainer, and PEFT under the hood.

> "Write your training loop once, run it anywhere." — Hugging Face Accelerate motto

---

## How It Works

Accelerate uses a **CLI-driven configuration workflow**:

### 1. Configuration (`accelerate config`)

The CLI prompts for hardware setup and distributed strategy, producing a `default_config.yaml`:

```bash
accelerate config
```

This interactively asks about:
- Machine type (single-node, multi-node, TPU)
- Number of GPUs
- Mixed precision (fp16, bf16, fp8, no)
- Distributed strategy (FSDP vs DeepSpeed vs DDP vs no)
- Strategy-specific options (sharding stage, offload, auto-wrap policy, etc.)

### 2. Launch (`accelerate launch`)

The configured script runs on the target hardware:

```bash
accelerate launch train.py
```

### 3. In-Code Usage

The core abstraction is the `Accelerator` object, which handles device placement, mixed precision, gradient accumulation, and distributed synchronization:

```python
from accelerate import Accelerator

accelerator = Accelerator()
model, optimizer, dataloader = accelerator.prepare(
    model, optimizer, dataloader
)
for batch in dataloader:
    outputs = model(**batch)
    loss = outputs.loss
    accelerator.backward(loss)
    optimizer.step()
    optimizer.zero_grad()
```

This same code runs on CPU, single GPU, multi-GPU DDP, FSDP, DeepSpeed, or TPU — switched entirely by the `accelerate config` output.

### Ecosystem Integration

Accelerate is the **underlying engine** for Hugging Face training tools:
- **Transformers `Trainer`** — Uses Accelerate for distributed training under the hood
- **TRL `SFTTrainer`** — TRL's supervised fine-tuning trainer builds on Accelerate
- **PEFT** — Works alongside Accelerate for parameter-efficient methods like LoRA/QLoRA

---

## FSDP vs DeepSpeed Integration

Accelerate's concept guide defines a **direct mapping** between FSDP arguments and DeepSpeed arguments within the Accelerate CLI. This mapping enables one-to-one migration between the two strategies.

### Configuration Mapping Table

| Feature | FSDP Argument | DeepSpeed Argument | Notes |
| :--- | :--- | :--- | :--- |
| **Strategy/Stage** | `--fsdp_sharding_strategy` | `--zero_stage` | FSDP `FULL_SHARD` ≈ ZeRO Stage `3` |
| **Offloading** | `--fsdp_offload_params` | `--offload_param_device` | FSDP is "all-or-nothing"; DS allows granular offload |
| **RAM Efficiency** | `--fsdp_cpu_ram_efficient_loading` | `--zero3_init_flag` | Only relevant for ZeRO 3 / Full Shard mode |
| **Checkpointing** | `--fsdp_state_dict_type` | `--zero3_save_16bit_model` | DS consolidates to single rank if `true` |
| **Prefetching** | `--fsdp_forward_prefetch` | (Automatic / Config-based) | FSDP requires explicit flags |
| **Auto-Wrapping** | `--fsdp_auto_wrap_policy` | (Transparent) | FSDP needs to know transformer layer boundaries |

### Key Functional Differences

#### Checkpointing
- **FSDP:** Supports `FULL_STATE_DICT` (consolidated, memory-intensive) and `SHARDED_STATE_DICT` (per-rank shards, faster for large models).
- **DeepSpeed:** Use `--zero3_save_16bit_model true` to consolidate to a single rank (slow for large models). For speed, save sharded checkpoints and use `zero_to_fp32.py` for post-conversion.

#### Offloading
- **FSDP:** "All-or-nothing" — parameters, gradients, and optimizer states must all be offloaded together or all stay on GPU. No granular control.
- **DeepSpeed:** Independent offloading of parameters vs. optimizer states, plus **NVMe offload** support for extreme memory pressure scenarios.

#### Model Loading & Wrapping
- **FSDP:** Requires explicit `fsdp_auto_wrap_policy: TRANSFORMER_BASED_WRAP` so the framework knows how to shard across transformer layers.
- **RAM Efficiency:** FSDP needs an explicit `--fsdp_cpu_ram_efficient_loading` flag; DeepSpeed ZeRO 3 activates RAM-efficient initialization automatically via the `transformers` integration.

#### Training Parameters
- **DeepSpeed:** Requires explicit `"auto"` directives in its config: `gradient_accumulation_steps: "auto"`, `gradient_clipping: "auto"`.
- **FSDP:** These parameters are handled transparently — no special flags needed.

---

## Memory & Precision Differences

One of the most important but subtle differences between FSDP and DeepSpeed within Accelerate is **how they handle model precision** during initialization and optimization:

| Process | FSDP | DeepSpeed |
| :--- | :--- | :--- |
| **Model Preparation** | Created in `torch_dtype` (e.g., bf16, fp16) | **Disregards** `torch_dtype` — created in **fp32** |
| **Optimizer Initialization** | Parameters in `torch_dtype` | Parameters in **fp32** (upcast) |
| **Optimizer Step** | Occurs in `torch_dtype` | Occurs in **fp32** |

**Key Implications:**
- **DeepSpeed has higher memory overhead on small GPU counts** due to the fp32 upcast of all parameters during optimizer initialization and stepping.
- **FSDP is more memory-efficient** when using bf16/fp16 from the start, but the optimizer step happens in reduced precision, which can affect convergence on some tasks.
- **Rule of Thumb:** For stable training with automatic mixed precision (AMP), all trainable parameters should be in `torch.float32`. When using DeepSpeed, this is automatic; when using FSDP, consider whether reduced-precision optimizer steps impact your training stability.

**Torch Compile Compatibility:**
- FSDP requires `fsdp_use_orig_params: True` for `torch.compile` to work.
- DeepSpeed's `torch.compile` support depends on the ZeRO stage and is more experimental.

---

## Plugin System (Python API)

Beyond the CLI, Accelerate offers a Python plugin API for programmatic configuration of FSDP and DeepSpeed.

### FSDP Plugin

```python
from accelerate import FullyShardedDataParallelPlugin
from torch.distributed.fsdp import ShardingStrategy

fsdp_plugin = FullyShardedDataParallelPlugin(
    sharding_strategy=ShardingStrategy.FULL_SHARD,
    cpu_offload=True,
    auto_wrap_policy="TRANSFORMER_BASED_WRAP",
)
```

### DeepSpeed Plugin

```python
from accelerate import DeepSpeedPlugin

ds_plugin = DeepSpeedPlugin(
    zero_stage=3,
    gradient_accumulation_steps="auto",
    gradient_clipping="auto",
)
```

### Using with Accelerator

```python
from accelerate import Accelerator

accelerator = Accelerator(
    fsdp_plugin=fsdp_plugin,
    # OR:
    deepspeed_plugin=ds_plugin,
)
```

The `DeepSpeedPlugin` also accepts an `hf_ds_config` parameter for advanced users who want to pass a full DeepSpeed configuration dictionary directly.

---

## FSDP vs DeepSpeed: Decision Guide (Within Accelerate)

When using Accelerate as the launcher, both FSDP and DeepSpeed work identically from the user's perspective (`accelerate launch train.py`). The choice depends on workload characteristics:

| Dimension | FSDP (via Accelerate) | DeepSpeed (via Accelerate) |
| :--- | :--- | :--- |
| **Setup Complexity** | Minimal — unopinionated defaults | Higher — needs explicit config directives (`"auto"` flags) |
| **Memory Efficiency** | Better on small GPU counts (preserves `torch_dtype`) | Upcasts to fp32, higher baseline memory |
| **Offload Granularity** | All-or-nothing (params + gradients + optimizer) | Granular (param vs. optimizer offload, NVMe support) |
| **Checkpointing** | `FULL_STATE_DICT` or `SHARDED_STATE_DICT` | Consolidation via `zero3_save_16bit_model` or `zero_to_fp32.py` |
| **Prefetching** | Manual flag (`--fsdp_forward_prefetch`) | Automatic / config-based |
| **Model Wrapping** | Requires `auto_wrap_policy` (explicit layer knowledge) | Transparent — no wrapping needed |
| **Extreme Scaling** | Good up to moderate multi-node (>8 nodes favors DS) | ZeRO-Infinity + pipeline parallelism for extreme scale |
| **Hugging Face Fit** | Native — built for transformers ecosystem | Slightly less native (needs `"auto"` directives) |

### When to Choose FSDP

- You want minimal dependencies and simpler config — especially for **LoRA / Q-LoRA fine-tuning** on consumer GPUs.
- Your model fits in GPU memory at bf16/fp16 after sharding — FSDP's `torch_dtype` preservation saves memory.
- You are already in the PyTorch ecosystem and want **PyTorch-native** sharding without extra packages.
- You are doing single-node or small multi-node training (<8 nodes).

### When to Choose DeepSpeed

- You need **ZeRO-3 offload with NVMe** for extreme memory pressure (e.g., fitting 70B+ models on very few GPUs).
- You need **pipeline parallelism** across many nodes for large-scale training.
- You want **fine-grained control** over overlapping computation and communication.
- You already have an existing DeepSpeed configuration and want to reuse it within Accelerate.
- You need **ZeRO-Stage-1 or 2** (FSDP only offers ZeRO-2/3 equivalents; DeepSpeed offers all three).

---

## Relationship to Existing Wiki Pages

Accelerate connects multiple existing concept pages as the **unified orchestration layer**:

- **[[concepts/pytorch-fsdp]]** — Covers native PyTorch FSDP sharding strategies, architecture, and has a DeepSpeed comparison table (native, not Accelerate-specific). Accelerate is the recommended launcher for FSDP in Hugging Face workflows.
- **[[concepts/fsdp-qlora]]** — Uses Accelerate (`accelerate launch`) as the launcher for FSDP+QLoRA training. The `accelerate config` step is critical for setting sharding strategy and CPU offload.
- **[[concepts/qlora]]** — Mentions Accelerate integration for distributed Q-LoRA training.
- **[[concepts/fine-tuning/peft-lora-qlora]]** — PEFT works alongside Accelerate; the `Accelerator` prepares model, optimizer, and dataloader for distributed PEFT training.
- **[[concepts/fine-tuning/pytorch-fsdp]]** — Fine-tuning-specific FSDP configs (Axolotl) that run via Accelerate's launch system.
- **[[concepts/ai-infrastructure-engineering/distributed-training]]** — Higher-level overview of DDP/FSDP/DeepSpeed paradigms; Accelerate is the tool that operationalizes them.
- **[[concepts/inference/vllm]]** — Mentions Accelerate for FSDP configuration in training workflows that feed into vLLM serving.

---

## Related Concepts

- **[[concepts/pytorch-fsdp]]** — PyTorch FSDP sharding strategies, architecture, and DeepSpeed comparison
- **[[concepts/fsdp-qlora]]** — Combining FSDP with Q-LoRA for memory-efficient fine-tuning, launched via Accelerate
- **[[concepts/qlora]]** — Quantized Low-Rank Adaptation, often used with Accelerate for distributed training
- **[[concepts/fine-tuning/peft-lora-qlora]]** — PEFT methods that integrate with Accelerate's distributed training
- **[[concepts/fine-tuning/pytorch-fsdp]]** — FSDP configuration for fine-tuning workflows (Axolotl, etc.)
- **[[concepts/ai-infrastructure-engineering/distributed-training]]** — Higher-level overview of DDP, FSDP, and DeepSpeed paradigms
- **[[concepts/inference/vllm]]** — Production inference serving (Accelerate for FSDP training → vLLM serving pipeline)

---

## Sources

- Hugging Face Accelerate Documentation: [https://huggingface.co/docs/accelerate](https://huggingface.co/docs/accelerate)
- Hugging Face Accelerate FSDP vs DeepSpeed Concept Guide: [https://huggingface.co/docs/accelerate/en/concept_guides/fsdp_and_deepspeed](https://huggingface.co/docs/accelerate/en/concept_guides/fsdp_and_deepspeed)
- Raw Article: `raw/articles/2026-05-04_accelerate-fsdp-deepspeed-guide.md`
- Hugging Face Accelerate GitHub: [https://github.com/huggingface/accelerate](https://github.com/huggingface/accelerate)
