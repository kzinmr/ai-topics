---
title: NVIDIA Nemotron-Labs-Diffusion
created: 2026-05-21
updated: 2026-05-21
type: entity
tags:
  - model
  - nvidia
  - text-generation
  - multimodal
  - vlm
  - inference
  - optimization
  - open-source
sources: [raw/articles/2026-05-20_nvidia-nemotron-labs-diffusion.md]
---

# NVIDIA Nemotron-Labs-Diffusion

NVIDIA's tri-mode language model family (3B, 8B, 14B) that unifies **autoregressive (AR) decoding**, **diffusion-based parallel decoding**, and **self-speculation decoding** in a single set of weights. The same model switches between modes at inference time by changing the attention pattern — no separate model files or architectural modifications needed.

## Overview

- **Sizes**: 3B, 8B, 14B parameters
- **Variants**: Base, Instruct, Vision-Language (VLM)
- **Training**: Joint AR-diffusion objective on top of pretrained Ministral3 models
- **License**: NVIDIA Nemotron Open Model
- **Availability**: Hugging Face `nvidia/Nemotron-Labs-Diffusion-{{size}}`
- **Released**: May 20, 2026

## Three Decoding Modes

### 1. AR Decoding
Standard causal left-to-right generation. Best for high-concurrency cloud serving where GPU is saturated by batching.

### 2. Diffusion Decoding
Tokens are denoised in **parallel within fixed-length blocks** (e.g., 32 tokens). Bidirectional attention inside a block; causal across blocks (KV cache reusable). A lightweight sampler predicts which top-1 tokens are correct and commits them — yielding multiple tokens per forward pass. Controlled by a `threshold` parameter for accuracy-throughput tradeoff.

### 3. Self-Speculation Decoding
- **Draft**: Diffusion pathway proposes a block of k candidate tokens in parallel
- **Verify**: AR pathway verifies the longest contiguous prefix matching its own predictions
- No auxiliary draft model needed (unlike Eagle3/MTP)
- Linear variant achieves **5.99× tokens per forward** (8B, LoRA-enhanced)
- Quadratic variant achieves **6.38× TPF**

## Training

### Joint Objective
`L(θ) = L_AR(θ) + α · L_diff(θ)`, where α=0.3

Both losses improve together — no tradeoff. Ablation with α from 0.1 to 1.0 showed simultaneous peak of AR and diffusion accuracy at 0.3.

### Two-Stage Training
1. **Stage 1**: Pure AR on 1 trillion tokens — builds left-to-right linguistic priors
2. **Stage 2**: Joint objective on 300 billion tokens

**Cumulative improvement over pure diffusion**: +16.05% (AR loss: +7.48%, two-stage: +5.74%, global loss averaging: +2.12%)

### Compute
256 NVIDIA H100 GPUs. Base models initialized from pretrained Ministral3 checkpoints. Instruct fine-tuning: 45B tokens SFT with same joint objective.

## Benchmark Results

| Model/Mode | Avg Accuracy | Tokens Per Forward |
|---|---|---|
| Qwen3-8B (AR) | 62.75% | 1× |
| NLD-8B AR | 63.61% | 1× |
| NLD-8B Diffusion | 63.18% | 2.57× |
| NLD-8B Linear Self-Spec (LoRA) | 62.81% | **5.99×** |
| NLD-8B Quadratic Self-Spec | **64.04%** | **6.38×** |

On GB200 at concurrency 1: **850 tokens/sec** (self-speculation) vs 253 tokens/sec (AR). With custom CUDA kernels: **1,015 t/s** — approximately 4× faster.

## LoRA-Enhanced Self-Speculation

LoRA adapter fine-tuned on the diffusion draft pathway (rank 128, α=512, ~36M params ≈ 0.4% of backbone) to better align with AR verifier. Targets only `o_proj` layer:

- 3B: +14.4% TPF improvement
- 8B: +32.5% TPF improvement
- 14B: +27.6% TPF improvement

## Speed-of-Light Analysis

Theoretical upper bound for diffusion mode: **7.60×** TPF (oracle sampler). Current confidence-based sampling achieves ~3× — significant room for sampler improvements. Linear self-speculation real TPF is 6.02× SOL but achieves 3.41× (76.5% gap) due to needing two forward passes per cycle and only accepting contiguous prefixes.

## Significance

NVIDIA's involvement signals that non-autoregressive text generation is now a practical deployment option. The single-checkpoint tri-mode design reduces operational complexity (one model file instead of separate AR + draft models), and the throughput gains directly reduce inference costs for latency-sensitive applications.

## Related Pages

- [[entities/nvidia-nemotron-3-nano-omni]] — NVIDIA's multimodal MoE agent model
- [[entities/nemotron-cascade-2]] — NVIDIA's reasoning-focused 30B MoE
- [[concepts/speculative-decoding]] — Speculative decoding techniques
- [[entities/nvidia]] — NVIDIA's AI model and hardware ecosystem
- [[concepts/diffusion]] — Diffusion models beyond image generation
