---
title: Nemotron-Labs Diffusion
created: 2026-05-24
updated: 2026-05-24
type: concept
tags: [model, inference, diffusion, nvidia, open-source, optimization, transformer-architecture, non-transformer]
sources: [raw/articles/2026-05-23_nvidia-nemotron-labs-diffusion.md]
---

# Nemotron-Labs Diffusion

Nemotron-Labs Diffusion is NVIDIA's family of **diffusion language models (DLMs)** released May 23, 2026. DLMs break the autoregressive generation loop by generating entire token blocks in parallel via iterative denoising, achieving up to 6.4× faster inference compared to standard autoregressive decoding.

## The Memory-Bandwidth Wall

Autoregressive (AR) LLM inference is fundamentally **memory-bandwidth bound**: each token requires loading the full model weights from HBM. On an A100 80GB with a 7B FP16 model (~14GB), this imposes a ~7ms minimum per step just for weight movement. Existing optimizations — speculative decoding, quantization, FlashAttention — are incremental improvements on the same sequential loop. DLMs break this loop entirely.

## Efficient-DLM Architecture

NVIDIA's key insight: convert a **pretrained AR model** into a DLM rather than training from scratch. This preserves quality while gaining speed.

### Block-Wise Attention
- Divide sequence into non-overlapping blocks (e.g., 32 tokens)
- **Within block:** full bidirectional attention (enables parallel denoising)
- **Across blocks:** standard left-to-right causal attention
- Enables **KV caching**: for 32-token blocks on 2048-token sequences, 98.4% of KV computations come from cache

### Position-Dependent Token Masking
- Higher masking probability for later positions, matching inference patterns
- Reduces train/test mismatch

### Joint Training Objective
```
L_total = λ · L_AR + (1-λ) · L_diffusion
```
The model remains a first-class AR model while gaining diffusion capability.

## Model Family (7 checkpoints)

| Model | Parameters | Type |
|-------|-----------|------|
| Nemotron-Labs-Diffusion-3B | ~4B | Instruct |
| Nemotron-Labs-Diffusion-3B-Base | ~4B | Base |
| Nemotron-Labs-Diffusion-8B | 8B | Instruct |
| Nemotron-Labs-Diffusion-8B-Base | 8B | Base |
| Nemotron-Labs-Diffusion-14B | 14B | Instruct |
| Nemotron-Labs-Diffusion-14B-Base | 14B | Base |
| Nemotron-Labs-Diffusion-VLM-8B | ~9B | Vision-Language |

Training data: 1.3T tokens (pretraining) + 45B tokens (SFT). License: NVIDIA Nemotron Open Model License. Serving: SGLang.

## Three Generation Modes

1. **Autoregressive (AR):** standard left-to-right (fallback mode)
2. **Semi-autoregressive (SAR):** generate in blocks, AR within block
3. **Diffusion (DLM):** iterative denoising across entire block — up to 6.4× faster

## Significance

This is one of the most significant inference architecture innovations in 2026. By retrofitting pretrained AR models with diffusion capabilities, NVIDIA provides a practical path to faster inference without sacrificing model quality. The block-wise attention design is the key enabler, making KV caching compatible with diffusion.

## Related Pages

- [[concepts/diffusion]] — diffusion models in AI
- [[entities/nvidia]] — NVIDIA company
- [[concepts/inference]] — LLM inference optimization
- [[concepts/transformer-architecture]] — transformer architecture
- [[concepts/quantization]] — model quantization
- [[concepts/speculative-decoding]] — alternative inference speedup technique
