---
title: "FSDP vs DeepSpeed: Accelerate Concept Guide"
source: "Hugging Face Accelerate Docs"
url: "https://huggingface.co/docs/accelerate/en/concept_guides/fsdp_and_deepspeed"
author: "Hugging Face"
date: 2026-05-04
tags:
  - accelerate
  - fsdp
  - deepspeed
  - distributed-training
  - huggingface
---

# FSDP vs DeepSpeed: Accelerate Concept Guide

This guide outlines the parallels and differences between **PyTorch FSDP** and **Microsoft DeepSpeed** within the `accelerate` ecosystem, specifically for single-node, multi-GPU scenarios.

## Core Configuration Mapping
Model tensors are split across GPUs — called *sharding* in FSDP and *partitioning* in DeepSpeed.

| Feature | FSDP Argument | DeepSpeed Argument | Notes |
| :--- | :--- | :--- | :--- |
| **Strategy/Stage** | `--fsdp_sharding_strategy` | `--zero_stage` | FSDP `FULL_SHARD` ≈ ZeRO Stage `3` |
| **Offloading** | `--fsdp_offload_params` | `--offload_param_device` | FSDP is "all-or-nothing"; DS allows granular offload |
| **RAM Efficiency** | `--fsdp_cpu_ram_efficient_loading` | `--zero3_init_flag` | Only for ZeRO 3 / Full Sharding |
| **Checkpointing** | `--fsdp_state_dict_type` | `--zero3_save_16bit_model` | DS consolidates to single rank if true |
| **Prefetching** | `--fsdp_forward_prefetch` | (Automatic/Config-based) | FSDP requires manual flags |
| **Auto-Wrapping** | `--fsdp_auto_wrap_policy` | (Transparent) | FSDP needs to know layer boundaries |

## Key Functional Differences

### Checkpointing
- **FSDP:** Can save either `FULL_STATE_DICT` or `SHARDED_STATE_DICT`. Sharded is faster for large models.
- **DeepSpeed:** Use `--zero3_save_16bit_model true` to consolidate to a single rank (slow for large models). For speed, save sharded and use `zero_to_fp32.py` for post-conversion.

### Offloading
- **FSDP:** "All-or-nothing" — params, gradients, optimizer must all be offloaded or all stay on GPU.
- **DeepSpeed:** Independent offloading of params and optimizers, plus **NVMe offload**.

### Model Loading & Wrapping
- **FSDP:** Requires `fsdp_auto_wrap_policy: TRANSFORMER_BASED_WRAP`.
- **RAM Efficiency:** FSDP requires explicit flag; DeepSpeed ZeRO 3 activates automatically via `transformers`.

### Training Parameters
- **DeepSpeed:** Requires explicit flags: `gradient_accumulation_steps: "auto"`, `gradient_clipping: "auto"`.
- **FSDP:** These are transparent.

## Data Precision & Memory Handling

| Process | FSDP | DeepSpeed |
| :--- | :--- | :--- |
| **Preparation** | Created in `torch_dtype` | Disregards `torch_dtype`, created in **fp32** |
| **Optimizer Init** | Parameters in `torch_dtype` | Parameters in **fp32** |
| **Optimizer Step** | Occurs in `torch_dtype` | Occurs in **fp32** |

**Key Insight:** DeepSpeed may have higher memory overhead on small GPU counts due to fp32 upcast.
**Torch Compile:** FSDP requires `fsdp_use_orig_params: True` for torch.compile.

## Plugin Implementation
- **DeepSpeed:** `DeepSpeedPlugin(zero_stage=..., hf_ds_config=...)`
- **FSDP:** `FullyShardedDataParallelPlugin(sharding_strategy=...)`

> Rule of Thumb: For stable training with automatic mixed precision, all trainable parameters should be in `torch.float32`.
