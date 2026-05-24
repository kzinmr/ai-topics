# NVIDIA Nemotron-Labs Diffusion: Diffusion Language Models

**Source:** [DEV Community](https://dev.to/monuminu/diffusion-language-models-are-here-deep-dive-into-nvidias-nemotron-labs-dlm-architecture-2ke2) / [HuggingFace](https://huggingface.co/nvidia/Nemotron-Labs-Diffusion-8B) | **Date:** May 23, 2026

## Overview
NVIDIA released Nemotron-Labs Diffusion, a family of diffusion language models (DLMs) that merge autoregressive and diffusion generation for up to 6.4× faster inference. Instead of generating tokens one-by-one (autoregressive), DLMs generate entire blocks in parallel using iterative denoising.

## The Problem
- AR generation is memory-bandwidth bound — each token requires loading full model weights from HBM
- On an A100 80GB with 7B FP16 model (~14GB), ~7ms minimum per step just for weight movement
- Existing optimizations (speculative decoding, quantization, FlashAttention) are incremental
- NVIDIA's approach: break the sequential loop entirely

## Efficient-DLM Architecture
- Converts pretrained AR models into DLMs (starts from strong AR checkpoint → teaches diffusion)
- **Block-wise attention:** divide sequence into blocks, bidirectional within block, causal across blocks. Enables KV caching (98.4% from cache for 32-token blocks on 2048-token sequences)
- **Position-dependent token masking:** higher masking probability for later positions
- **Joint AR + diffusion training:** L_total = λ·L_AR + (1-λ)·L_diffusion
- Training data: 1.3T tokens (pretraining) + 45B tokens (SFT for instruct)

## Model Family (7 checkpoints on HuggingFace)
| Model | Params | Day-1 Downloads |
|-------|--------|-----------------|
| Nemotron-Labs-Diffusion-3B | ~4B | 14.7K |
| Nemotron-Labs-Diffusion-3B-Base | ~4B | 14.2K |
| Nemotron-Labs-Diffusion-8B | 8B | 24.1K |
| Nemotron-Labs-Diffusion-8B-Base | 8B | 228K |
| Nemotron-Labs-Diffusion-14B | 14B | 3.28K |
| Nemotron-Labs-Diffusion-14B-Base | 14B | 1.18K |
| Nemotron-Labs-Diffusion-VLM-8B | ~9B | 590 |

## Three Generation Modes
1. **Autoregressive (AR):** standard left-to-right (fallback)
2. **Semi-autoregressive (SAR):** generate in blocks, AR within block
3. **Diffusion (DLM):** iterative denoising across entire block, up to 6.4× faster

## License & Serving
- NVIDIA Nemotron Open Model License (commercially friendly for text models)
- Serving via SGLang (integration PR #25803)
- arXiv: 2512.14067 (Efficient-DLM paper)
