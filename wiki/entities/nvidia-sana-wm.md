---
title: NVIDIA SANA-WM
created: 2026-05-21
updated: 2026-05-21
type: entity
tags: [model, nvidia, video-generation, world-models, open-source, diffusion, multimodal, gpu, training-efficiency]
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
