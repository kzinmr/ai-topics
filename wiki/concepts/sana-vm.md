---
title: SANA-WM
created: 2026-05-19
updated: 2026-05-19
type: concept
tags:
  - concept
  - world-models
  - video-generation
  - open-source
  - hardware
  - diffusion
  - hybrid-architecture
  - training-efficiency
  - nvidia
sources: [raw/articles/2026-05-16_nvidia-sana-wm.md, https://www.marktechpost.com/2026/05/16/nvidia-introduces-sana-wm-a-2-6b-parameter-open-source-world-model-that-generates-minute-scale-720p-video-on-a-single-gpu/]
---

# SANA-WM

**SANA-WM** is a 2.6B-parameter open-source **world model** by [[entities/nvidia]], released May 16, 2026. Built on the SANA-Video codebase (Apache 2.0), it generates **60-second 720p video** on a **single GPU** from an input image and a 6-DoF camera trajectory.

Paper: arXiv:2605.15178 | Code: github.com/NVlabs/Sana

## Why It Matters

World models require generating long, high-resolution video, but standard softmax attention has **quadratic complexity** in sequence length — at 961 latent frames for 60s 720p, this is infeasible. SANA-WM solves this with a hybrid linear attention architecture, enabling minute-scale generation without multi-GPU clusters.

## Architecture: Four Key Innovations

### 1. Hybrid Gated DeltaNet + Softmax Attention

Replaces standard attention with frame-wise **Gated DeltaNet (GDN)**:
- **20 transformer blocks**: 15 GDN blocks + 5 softmax attention blocks at layers {3, 7, 11, 15, 19}
- **Frame-wise recurrence**: One full latent frame per recurrent step, maintaining constant D×D state regardless of video length
- **Decay gate γ**: Forgets stale past frames to prevent drift
- **Delta-rule correction**: Updates only residual between target value and current prediction
- **Key scaling**: `1/√(D·S)` — prevents NaN divergence observed with standard scaling

### 2. Dual-Branch Camera Control

Two branches operating at different temporal rates:
- **Coarse (UCPE attention)**: At latent-frame rate, captures global trajectory. Reduces RotErr from 16.93→6.21, CamMC from 0.4937→0.2047
- **Fine (Plücker mixing)**: Pixel-wise Plücker raymaps from all 8 raw frames within a VAE temporal stride, restoring intra-stride camera motion

CamMC of 0.2047 is best among all compared methods, including models 5× larger.

### 3. Two-Stage Generation Pipeline

Stage-1 generator → **Stage-2 refiner** (17B LTX-2 with rank-384 LoRA, only 3 Euler denoising steps):
- Long-horizon visual drift ΔIQ: Simple 3.79→1.17, Hard 3.09→**0.31**
- 22.0 videos/hour on 8 H100s; 74.7 GB memory

### 4. Distilled Deployment

Distilled AR variant + NVFP4 quantization: **34 seconds per 60s clip on single RTX 5090**

## Training

- Hardware: 64 H100s, ~18.5 days
- Data: 212,975 public video clips (SpatialVID-HQ, DL3DV, OmniWorld, Sekai, MiraData)
- Custom annotation pipeline using Pi3X + MoGe-2 for metric-scale 6-DoF poses

## Comparison: SANA-WM vs Starchild-1

| Aspect | SANA-WM | [[concepts/starchild-1]] |
|--------|---------|--------------------------|
| Developer | [[entities/nvidia]] | [[entities/odyssey-ml]] |
| Parameters | 2.6B | Not disclosed |
| Modalities | Video only | Audio + Video |
| Generation | Offline, trajectory-based | Real-time, interactive |
| Architecture | DiT + Gated DeltaNet | Causal autoregressive |
| License | Apache 2.0 | Research preview |
| Single GPU? | Yes (34s/clip on RTX 5090) | N/A |

## Throughput Comparison

| Method | Params | GPUs | Videos/hour |
|--------|--------|------|-------------|
| SANA-WM + refiner | 2.6B + 17B | 8 H100s | 22.0 |
| LingBot-World | 14B+14B | 8 GPUs | 0.61 |
| **Throughput advantage** | — | — | **36×** |

## Related

- [[entities/nvidia]] — Developer
- [[concepts/starchild-1]] — Odyssey's multimodal world model
- [[concepts/world-models-for-agents]] — World models in agent contexts
- [[concepts/diffusion]] — Diffusion model foundations
