---
title: "Megakernel for LLM Inference"
type: concept
status: draft
created: 2026-04-23
updated: 2026-08-05
tags:
  - inference
  - optimization
  - local-llm
  - model-training
  - fused-kernels
  - mixture-of-experts
sources:
  - https://www.lucebox.com/blog/megakernel
  - raw/newsletters/2026-08-05-ainews-megakernels-are-so-dead-and-so-back.md
related:
  - lucebox.md
  - sandro-puppo.md
  - davide-ciffa.md
  - qwen-models.md
  - llama-cpp.md
  - megakernel-for-llm-inference.md
---

# Megakernel for LLM Inference

A CUDA kernel optimization that fuses all layers of an LLM into a single dispatch, eliminating CPU round-trips between layer boundaries.

## Overview

Developed by Lucebox for Qwen 3.5-0.8B (a hybrid DeltaNet + Attention model), the megakernel approach achieves 1.8x the throughput of Apple M5 Max while matching its energy efficiency on a 2020 RTX 3090.

## Key Results

| Metric | RTX 3090 (llama.cpp) | M5 Max | RTX 3090 (Megakernel @220W) |
|--------|---------------------|--------|---------------------------|
| tok/s | 267 | 229 | 411 |
| Power | 350W | ~130W | 220W |
| tok/J | 0.76 | 1.76 | 1.87 |
| GPU price | $700 | $2,499+ (system) | $700 |

## Architecture

The megakernel fuses all 24 layers of Qwen 3.5-0.8B into a single CUDA dispatch:
- **82 blocks, 512 threads** — all SMs on RTX 3090 stay occupied
- **BF16 weights, BF16 activations, FP32 accumulation**
- **DeltaNet recurrence runs natively** — warp-cooperative state updates in F32 registers
- **Full attention with online softmax** — fused QKV, RoPE, causal attention, output projection
- **Zero inter-layer overhead** — cooperative grid sync replaces kernel launches

## Performance Breakdown

| Setup | Prefill (pp520) | Decode (tg128) |
|-------|-----------------|----------------|
| Megakernel | 37,800 tok/s | 413 tok/s |
| llama.cpp BF16 | 11,247 tok/s | 267 tok/s |
| PyTorch HuggingFace | 7,578 tok/s | 108 tok/s |

**3.4x faster prefill, 1.55x faster decode** vs llama.cpp on same hardware.

## Power Sweep

| Power Limit | Clock | Draw | tok/s | tok/J | vs Stock |
|-------------|-------|------|-------|-------|----------|
| 420W (stock) | 1980 MHz | 314W | 433 | 1.38 | baseline |
| 300W | 1935 MHz | 299W | 432 | 1.44 | 99.8% speed, 5% less power |
| 220W | 1635 MHz | 220W | 411 | 1.87 | 95% speed, 30% less power |
| 150W | 405 MHz | 150W | 194 | 1.29 | too aggressive |

The optimal point is 220W: 95% of stock speed with 30% less power consumption.

## Why It Matters

Traditional inference frameworks launch ~100 kernels per token across 24 layers. Each layer boundary means:
1. Return control to CPU
2. Dispatch next kernel
3. Re-fetch weights from global memory
4. Synchronize threads

The megakernel eliminates these inter-layer overheads, keeping data in registers and shared memory throughout the forward pass.

For hybrid architectures like Qwen 3.5 (18 DeltaNet + 6 Attention layers), no existing framework had fused kernels optimized for this pattern.

## Megakernel Debate (Aug 2026)

> *Source: [[raw/newsletters/2026-08-05-ainews-megakernels-are-so-dead-and-so-back.md|AINews — "Megakernels are so dead and so back", Aug 5 2026]]*

A sharp debate erupted in August 2026 over whether hand-written fused kernels are a dead end for production inference:

### "Megakernels are dead" (Ali / waterloo_intern)

Ali (waterloo_intern, on Latent Space's Inference Engineering Masterclass + follow-up post) argued the case for abandoning hand-fused megakernels:

- **No serious inference provider runs a 67k LOC hand-fused forward-pass kernel in production** — teams doing so are research-only
- The theoretical gains (launch overhead, inter-kernel overlap) are eroded by **PDL (programmatic dependent launch)** and **straggler CTA** issues — partial blocks complete at different times, forcing coordination overhead
- **TensorRT-LLM / modular kernels are faster in practice**: each component is individually optimized and can parallelize with each other
- Even a fused kernel cannot eliminate communication for nonlinearities (e.g., softmax needs the full row across GPUs in tensor parallelism)

### Rubin's Tile-Level Dependency Triggers (Kyle Kranen)

NVIDIA's Rubin GPU is designed to "kill megakernels": **Kyle Kranen announced tile-level dependency triggers** (July 21, 2026) — finer-grained kernel coordination where *"as soon as the data to begin working on part of an operation is available, the kernels to execute it can start."* This removes the pipeline-blockage justification for kernel fusion.

### Cursor's Mixture-of-Kittens (MoK) — "so back"

Counter-evidence arrived the same week: **Cursor open-sourced Mixture-of-Kittens (MoK)**, its **MoE training megakernel for NVL72s** (Aug 4, 2026):

- Fuses **all Mixture-of-Experts communication and computation into a single, fully deterministic kernel**
- **Up to 2.37x faster than the strongest public baselines**; headline: **41% increase in overall tokens per second**
- At scale, translates to **billions of dollars of savings**
- Led by **Stuart Sul** — a **co-author of Ben Spector's original megakernel** work (ThunderKittens reference), part of Dan Fu's group

The debate's resolution: hand-fused **forward-pass inference kernels** (Lucebox-style, single-model) are losing to modular kernels + hardware-level dependency triggers, while **training-side MoE megakernels** (MoK) remain high-value. See also the stub [[concepts/megakernel-for-llm-inference|megakernel-for-llm-inference]] (redirects here).

## Sources

- [Megakernel blog post](https://www.lucebox.com/blog/megakernel) — Lucebox, April 2026
- [Hazy Research Intelligence Per Watt](https://hazyresearch.stanford.edu/blog/2025-11-11-ipw) — power measurement methodology
- [Qwen 3.5 architecture](https://github.com/QwenLM) — hybrid DeltaNet/Attention model
