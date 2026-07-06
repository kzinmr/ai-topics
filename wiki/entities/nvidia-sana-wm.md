---
title: NVIDIA SANA-WM
created: 2026-05-21
updated: 2026-05-21
type: entity
tags:
  - model
  - nvidia
  - video-generation
  - world-models
  - open-source
  - diffusion
  - multimodal
  - hardware
  - training-efficiency
sources: [raw/articles/2026-05-16_nvidia-sana-wm.md]
---

# NVIDIA SANA-WM

SANA-WM is a **2.6B-parameter open-source world model** from NVIDIA that generates high-fidelity 720p, 60-second videos with precise 6-DoF camera control from a single image and camera trajectory — all on a single GPU.

## Overview

- **Parameters**: 2.6B
- **Training**: 64 H100 GPUs, ~15 days
- **Training data**: 212,975 public video clips with metric-scale 6-DoF pose annotations
- **Inference**: Distilled variant denoises a 60s 720p clip in **34 seconds** on single RTX 5090 with NVFP4 quantization
- **Throughput**: 22.0 videos/hour vs 0.6 for comparable models — **36× higher**
- **GPU memory**: Only 74.7 GB
- **License**: Apache 2.0 (code)
- **Code**: [NVlabs/Sana](https://github.com/NVlabs/Sana)
- **Paper**: arXiv:2605.15178
- **Project page**: [nvlabs.github.io/Sana/WM/](https://nvlabs.github.io/Sana/WM/)

## Architecture: Four Core Designs

### 1. Hybrid Linear Attention with Gated DeltaNet (GDN)

20 transformer blocks: 15 frame-wise GDN + 5 softmax attention blocks at layers {3, 7, 11, 15, 19}.

GDN processes one entire latent frame per recurrent step (unlike token-wise GDN in LLMs). Key innovations:
- **Decay gate γ**: Down-weights stale past frames, preventing drift over long sequences
- **Delta-rule correction**: Updates only the residual, keeping recurrent state at constant D×D size regardless of video length
- **Scaling**: `1/√(D·S)` prevents NaN divergence events observed with L2 key normalization

Softmax blocks provide exact long-range recall as a periodic complement to the linear attention backbone.

### 2. Dual-Branch Camera Control

| Camera Encoding | RotErr ↓ | TransErr ↓ | CamMC ↓ |
|---|---|---|---|
| No control | 16.93 | 0.2347 | 0.4937 |
| Plücker only | 16.02 | 0.2340 | 0.4742 |
| UCPE only | 7.73 | 0.1350 | 0.2453 |
| **UCPE + Plücker** | **6.21** | **0.1162** | **0.2047** |

- **Coarse branch (UCPE attention)**: Unified Camera Positional Encoding at latent-frame rate on geometric attention channels
- **Fine branch (Plücker mixing)**: Pixel-wise 6D Plücker raymaps from all 8 raw frames per latent token, injected via zero-initialized projection

### 3. Two-Stage Generation Pipeline

Stage-1 SANA-WM backbone → Stage-2 **17B LTX-2 refiner** (rank-384 LoRA). Uses truncated-σ flow matching: stage-1 latents perturbed with noise (σ_start=0.9), refiner maps toward high-fidelity target. Only 3 Euler denoising steps at inference.

Quality degradation (ΔIQ, first→last 10s window):
- Simple split: 3.79 → **1.17**
- Hard split: 3.09 → **0.31**

### 4. Robust Data Annotation Pipeline

Modified VIPE engine producing metric-scale 6-DoF annotations:
- **Depth backend**: Pi3X (long-sequence consistency) fused with MoGe-2 (per-frame metric scale), EMA smoothing (momentum 0.99)
- **Per-frame intrinsics**: Bundle adjustment treats focal lengths and principal points as per-frame variables for robustness on internet video

## Efficiency

SANA-WM achieves visual quality comparable to models 5× larger (LingBot-World, HY-WorldPlay) while delivering 36× higher throughput and using only 74.7 GB GPU memory. The all-softmax alternative goes OOM at 60s — only the hybrid linear attention enables minute-scale generation.

## Related Pages

- [[entities/nvidia]] — NVIDIA's AI ecosystem
- [[concepts/world-models]] — World models in AI
- [[concepts/diffusion]] — Diffusion model techniques
- [[concepts/video-generation]] — AI video generation
- [[entities/nvidia-nemotron-labs-diffusion]] — NVIDIA's tri-mode language model

### Hybrid Linear Attention- **Frame-wise Gated DeltaNet (GDN)** interleaved with periodic softmax attention (every 4th block: layers 3, 7, 11, 15, 19)
- GDN scans one latent frame per step (not per token), keeping recurrent state at constant D×D size
- **Algebraic stabilization**: key scaling with 1/√(D·S) prevents divergence at minute scale
- Memory-efficient for arbitrary-length videos — solves the memory explosion of standard softmax attention


### Dual-Branch Camera ControlCombines two complementary approaches for precise 6-DoF trajectory adherence:
1. **Latent-rate UCPE**: Ray-local geometric attention at compressed frame rate
2. **Raw-frame Plücker mixing**: Fine-grained camera conditioning at native frame rate
- Best CamMC score (0.2047) among all compared methods, including models 5× larger


### Two-Stage Generation Pipeline1. **Stage 1**: SANA DiT generates initial video
2. **Stage 2**: LTX-2 refiner (17B, rank-384 LoRA) improves full-minute fidelity
   - Cuts long-horizon visual drift ΔIQ from 3.09 → 0.31 on Hard trajectories (3 Euler denoising steps)


### Progressive Training (4 stages)1. Efficient VAE adaptation (LTX2-VAE, C=128 latents)
2. Hybrid architecture adaptation (GDN + softmax on short clips)
3. Minute-scale extension + action conditioning
4. Chunk-causal fine-tuning + self-forcing distillation to 4 steps


## Efficiency Breakthrough
| Metric | Value |
|--------|-------|
| Training time | 15 days on 64 H100s |
| Training data | ~213K public video clips |
| Bidirectional inference | 1 H100 per 60s 720p clip |
| Distilled AR + NVFP4 | 34s per 60s clip on RTX 5090 |
| Throughput vs LingBot-World | **36× higher** at comparable quality |
| Full pipeline memory | 74.7 GB (within 80 GB H100 budget) |


## Inference Variants1. **Bidirectional** — Highest quality offline synthesis (49.2 GB)
2. **Chunk-causal AR** — Sequential rollout for streaming (51.1 GB)
3. **Distilled AR + NVFP4** — Fast deployment, 34s per 60s clip on RTX 5090


## Limitations- No explicit 3D scene memory
- Can drift in dynamic scenes or rare viewpoints
- First-frame images for demos generated by external models (GPT Image 2, Nano Banana Pro)


## Relationships- [[entities/nvidia]] — NVIDIA, the creator
- [[concepts/gemini]] — Google's Gemini Omni (competing world model)
- [[concepts/world-model]] — World models concept
- [[concepts/video-generation]] — Video generation overview
- [[concepts/diffusion]] — Diffusion model foundations
- [[concepts/mixture-of-experts]] — MoE architecture (related efficiency pattern)

