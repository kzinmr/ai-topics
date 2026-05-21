# NVIDIA SANA-WM: Efficient Minute-Scale World Model

**Source:** MarkTechPost (May 16, 2026) + NVIDIA project page | [Link](https://nvlabs.github.io/Sana/WM/) | [arXiv:2605.15178](https://arxiv.org/abs/2605.15178)

## Overview

SANA-WM is a 2.6B-parameter open-source world model from NVIDIA that generates high-fidelity 720p, 60-second videos with precise 6-DoF camera control, starting from a single image and a camera trajectory — all on a single GPU.

## Key Facts

- **Parameters**: 2.6B
- **Training compute**: 64 H100 GPUs, ~15 days
- **Training data**: 212,975 public video clips with metric-scale 6-DoF pose annotations
- **Inference**: Distilled variant denoises a 60s 720p clip in 34 seconds on single RTX 5090 with NVFP4
- **Throughput**: 22.0 videos/hour vs 0.6 videos/hour for comparable models (36× higher)
- **GPU memory**: Only 74.7 GB
- **License**: Apache 2.0 (code) | **Code**: github.com/NVlabs/Sana

## Architecture: Four Core Designs

1. **Hybrid Linear Attention with Gated DeltaNet (GDN)**: 20 transformer blocks — 15 frame-wise GDN + 5 softmax attention blocks. GDN adds decay gate γ (down-weights stale frames) and delta-rule correction, preventing drift over long sequences.

2. **Dual-Branch Camera Control**: Coarse branch (UCPE attention at latent-frame rate) + Fine branch (Plücker raymaps from all 8 raw frames per latent token). Combined: CamMC 0.2047 vs 0.4937 (no control).

3. **Two-Stage Pipeline**: Stage-1 SANA-WM backbone → Stage-2 17B LTX-2 refiner (rank-384 LoRA, 3 Euler denoising steps). Reduces quality degradation (ΔIQ) from 3.79→1.17 (simple) and 3.09→0.31 (hard).

4. **Robust Annotation**: Modified VIPE engine with Pi3X + MoGe-2 depth fusion for metric-scale 6-DoF annotations from public internet video.
