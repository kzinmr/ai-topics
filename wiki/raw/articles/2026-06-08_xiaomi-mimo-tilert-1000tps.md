---
title: "MiMo-V2.5-Pro-UltraSpeed: Pushing 1T-Parameter Model Generation Speed to 1000 TPS"
url: https://mimo.xiaomi.com/blog/mimo-tilert-1000tps
author: Xiaomi MiMo Team
date: 2026-06-08
type: article
tags: [inference, tilert, mimo, xiaomi, speculative-decoding, fp4, quantization, speed]
---

# MiMo-V2.5-Pro-UltraSpeed: Pushing 1T-Parameter Model Generation Speed to 1000 TPS

**Source:** https://mimo.xiaomi.com/blog/mimo-tilert-1000tps
**Author:** Xiaomi MiMo Team
**Date:** 2026-06-08

## Summary

Xiaomi MiMo-V2.5-Pro-UltraSpeed, in collaboration with TileRT, breaks **1000 tokens/s decode speed on a 1-trillion-parameter model** for the first time on commodity GPUs through extreme model-system codesign. This is achieved not with specialized hardware (like Cerebras or Groq) but through algorithmic + system co-optimization on standard 8-GPU nodes.

## Key Technical Points

### 1. Speed as a Paradigm Shift
- Speed transmutes into intelligence: within same wall-clock time, model can run dozens of reasoning paths in parallel (Best-of-N / Tree Search)
- Unleashes Coding Agent productivity ceiling
- Trillion-parameter models can enter real-time decision loops (trading, anti-fraud, medical)
- 3× the price, 10× the output experience

### 2. FP4 Quantization
- FP4 (MXFP4) quantization targeting bandwidth bottleneck
- Selective quantization: only MoE Experts to FP4, all other modules preserve original precision
- FP4 QAT (Quantization-Aware Training) keeps capability essentially on par with FP8
- Dramatically reduces model size and maximizes hardware bandwidth utilization

### 3. DFlash Speculative Decoding
- **DFlash**: block-level masked parallel prediction method (arXiv:2602.06036)
- Draft model fills entire block of masked positions in single forward pass — eliminates serial constraint of autoregressive drafting
- Block size limited to 8 to reduce verification overhead and increase concurrency
- Acceptance lengths: Coding 6.30, Math/Reasoning 5.56, Agent 4.29
- Draft model uses Sliding Window Attention (SWA), aligned with MiMo-V2 series design
- Muon second-order optimizer + model self-distillation for training

### 4. TileRT Ultra-Low-Latency Inference System
- **Persistent Engine Kernel**: entire compute pipeline persistently resident on GPU, launched once
- **Warp Specialization**: heterogeneous pipeline collaboration at tile level
- Full-pipeline continuous prefetching — while current Tile computes, next data already flowing through memory hierarchy
- Microsecond-scale hardware-software deep convergence (codesign)

### 5. Open Source
- MiMo-V2.5-Pro-FP4-DFlash checkpoint open-sourced on HuggingFace: https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash
- UltraSpeed support for MiMo-V2.5 coming soon

### 6. Access
- API: https://platform.xiaomimimo.com/ultraspeed
- Chat: https://ultraspeed.xiaomimimo.com
- Trial period: June 9-23, 2026 (application-based)
- Contact: business-mimo@xiaomi.com

### References
- [1] OCP Microscaling Formats (MX) v1.0 Spec
- [2] DFlash: https://arxiv.org/abs/2602.06036
