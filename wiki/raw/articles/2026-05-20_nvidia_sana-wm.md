---
title: "SANA-WM: Efficient Minute-Scale World Modeling"
source: https://arxiv.org/abs/2605.15178
date: 2026-05-15
author: Haoyi Zhu, Haozhe Liu, Yuyang Zhao et al. (NVIDIA)
tags: [nvidia, world-model, video-generation, open-source, model]
---

# SANA-WM: Efficient Minute-Scale World Modeling

2.6B-parameter open-source world model (Apache 2.0). Generates 720p, minute-long videos with precise 6-DoF camera control on a single GPU. Trained on 213K public video clips, 15 days on 64 H100s.

## Architecture
- **Hybrid Linear Attention**: Frame-wise Gated DeltaNet (GDN) interleaved with softmax attention (every 4th block)
- **Dual-Branch Camera Control**: Latent-rate UCPE + raw-frame Plücker mixing
- **Two-Stage Pipeline**: Stage-1 DiT + LTX-2 refiner for full-minute consistency
- **Algebraic stabilization**: Key scaling prevents divergence at minute scale

## Efficiency
- Training: 15 days on 64 H100s (vs industrial baselines needing more)
- Bidirectional: single H100 generates 60s 720p clip
- Distilled AR + NVFP4: 34s per 60s clip on single RTX 5090
- 36x higher throughput vs LingBot-World at comparable quality
- Available on HuggingFace: Efficient-Large-Model/SANA-WM_bidirectional
