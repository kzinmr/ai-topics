---
title: Napkin Math For Finetuning
type: concept
created: 2026-05-07
updated: 2026-05-07
tags:
  - fine-tuning
  - training
  - hardware
  - quantization
related_concepts:
  - fine-tuning/peft-lora-qlora
  - qlora
  - fine-tuning/quantization-overview
  - flashattention-pytorch-educational
  - fine-tuning/instruction-fine-tuning
related_entities:
  - jonathan-whitaker
related_articles:
  - 2026-05-07_johnowhitaker_napkin-math-finetuning
sources:
  - https://docs.google.com/presentation/d/1Ye_6zeatCWkq-fx8A--yK34uwU8oC2YQtMSTV1DgkSI/edit
---

# Napkin Math For Finetuning

A framework and methodology for estimating memory and compute requirements when fine-tuning large language models, presented by [[jonathan-whitaker]] (@johnowhitaker).

## Overview

The core insight of the napkin math approach is that we can make useful back-of-the-envelope estimates about fine-tuning costs (memory, time, hardware requirements) by understanding a few key factors:

1. **What takes up memory?** — model weights, activations, gradients, optimizer states, data
2. **What takes up time?** — compute (FLOPs) and data movement (memory bandwidth)
3. **What knobs can we turn?** — batch size, context length, LoRA rank, quantization level, gradient checkpointing, CPU offloading

## Key Techniques Catalog

| Technique | Memory Impact | Compute Impact | Use Case |
|-----------|--------------|----------------|----------|
| **Full Fine-tuning** | Highest (weights + gradients + optimizer states) | Highest | Maximum accuracy, sufficient GPU |
| **LoRA** | Low (only adapter params) | Lower (fewer params to update) | Limited GPU memory, fast iteration |
| **QLoRA** | Very low (4-bit quantized base + LoRA) | Slightly higher (dequantization overhead) | Consumer GPUs (RTX 3090/4090) |
| **Gradient Checkpointing** | Reduces activation memory (from O(n²) to O(n)) | ~33% recompute overhead | Long context, large batch sizes |
| **CPU Offloading** | Frees GPU memory by storing on CPU | Significant (PCIe bandwidth bottleneck) | When batch size matters more than speed |
| **Flash Attention** | Reduces attention memory from O(n²) to O(n) | Faster (fused kernel, less HBM access) | Long context training/inference |
| **FSDP (Fully Sharded Data Parallel)** | Distributes optimizer states across GPUs | Communication overhead | Multi-GPU setups |
| **Quantization (INT8/FP8/NF4)** | Reduces weight memory by 2-4x | Dequantization overhead | Fitting larger models on limited VRAM |

## Memory Breakdown

For a single training step with batch size `B`, sequence length `S`, model dimension `d`, and `L` layers:

| Component | Memory Estimate | Notes |
|-----------|----------------|-------|
| **Model weights** | ~2 bytes × params (in FP16/BF16) | Base cost |
| **Optimizer states** | ~8-12 bytes × params (Adam: 2 states + gradients) | Adam uses exp_avg + exp_avg_sq + gradients |
| **Activations** | O(B × S × d × L) — dominates at long context | Can be reduced via gradient checkpointing |
| **Gradients** | Same as model weights in FP16 | Cleared after optimizer step |

## Common Configurations

| Scenario | GPU | Config | Trainable Params | Speed |
|----------|-----|--------|-----------------|-------|
| LLM 7B, full finetune | 1× A100 (80GB) | bf16, no GC, bs=1 | 7B | Slow, memory tight |
| LLM 7B, LoRA | 1× RTX 4090 (24GB) | 4-bit base, LoRA r=16 | ~16M | Fast, good accuracy |
| LLM 70B, QLoRA | 2× A100 (80GB) | NF4, LoRA r=64, FSDP | ~260M | Moderate |
| LLM 70B, full finetune | 8× H100 (80GB) | BF16, FSDP, flash attn | 70B | Fast (if well-parallelized) |

## References

- **[[jonathan-whitaker]]** — [Original slides](https://docs.google.com/presentation/d/1Ye_6zeatCWkq-fx8A--yK34uwU8oC2YQtMSTV1DgkSI/edit)
- FSDP+QLoRA Benchmarks: https://github.com/AnswerDotAI/fsdp_qlora/blob/main/benchmarks_03_2024.md
- PyTorch optimizer memory tutorial: https://pytorch.org/tutorials/intermediate/optimizer_step_in_backward_tutorial.html
- HuggingFace transformer memory estimation: https://github.com/huggingface/transformers/issues/25572
