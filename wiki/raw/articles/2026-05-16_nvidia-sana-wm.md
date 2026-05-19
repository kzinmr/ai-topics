# NVIDIA SANA-WM: 2.6B Open-Source World Model, Minute-Scale 720p Video on Single GPU

**Source:** https://www.marktechpost.com/2026/05/16/nvidia-introduces-sana-wm-a-2-6b-parameter-open-source-world-model-that-generates-minute-scale-720p-video-on-a-single-gpu/
**Paper:** arXiv:2605.15178
**Date:** May 16, 2026

NVIDIA released SANA-WM, a 2.6B-parameter Diffusion Transformer world model that generates 60-second 720p video on a single GPU. Built on SANA-Video codebase (Apache 2.0).

Key architectural decisions:
1. **Hybrid Gated DeltaNet + softmax attention**: 15 GDN blocks + 5 softmax blocks at layers {3,7,11,15,19}. Frame-wise recurrence maintains constant D×D state regardless of video length.
2. **Dual-branch camera control**: Coarse UCPE attention for global trajectory + fine Plücker mixing for intra-stride motion. CamMC drops to 0.2047 (best among all methods including 5× larger models).
3. **Two-stage pipeline**: Stage-1 generator → 17B LTX-2 refiner with rank-384 LoRA, 3 Euler denoising steps. Long-horizon drift ΔIQ from 3.09 → 0.31.
4. **Distilled AR + NVFP4**: 34s per 60s clip on RTX 5090.

Training: ~18.5 days on 64 H100s, 212,975 public video clips. Throughput: 22.0 videos/hour on 8 H100s (36× higher than LingBot-World).
