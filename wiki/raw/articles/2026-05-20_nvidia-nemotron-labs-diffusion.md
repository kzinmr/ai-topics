# NVIDIA Nemotron-Labs-Diffusion: Tri-Mode Language Model

**Source:** MarkTechPost, May 20, 2026 | [Link](https://www.marktechpost.com/2026/05/20/nvidia-ai-releases-nemotron-labs-diffusion-a-tri-mode-language-model-with-6x-tokens-per-forward-over-qwen3-8b/)

## Overview

NVIDIA released Nemotron-Labs-Diffusion, a language model family (3B, 8B, 14B) that unifies autoregressive (AR) decoding, diffusion-based parallel decoding, and self-speculation decoding in a single set of weights. The same model switches modes at inference time by changing the attention pattern — no separate model files needed.

## Key Details

- **Sizes**: 3B, 8B, 14B (Base, Instruct, Vision-Language variants)
- **Training**: Joint AR-diffusion objective on top of pretrained Ministral3 models, 256 H100 GPUs
- **Two-stage training**: Stage 1 (1T tokens pure AR) → Stage 2 (300B tokens joint objective)
- **License**: NVIDIA Nemotron Open Model
- **Availability**: Hugging Face `nvidia/Nemotron-Labs-Diffusion-{size}`

## Three Decoding Modes

1. **AR Decoding**: Standard causal left-to-right, best for high-concurrency cloud serving
2. **Diffusion Decoding**: Parallel denoising within fixed-length blocks (32 tokens), bidirectional attention inside a block, multiple tokens per forward pass
3. **Self-Speculation**: Diffusion pathway drafts k candidates → AR verifies longest contiguous prefix. Achieves 5.99× TPF (8B, linear) and 6.38× TPF (quadratic)

## Performance

| Model/Mode | Avg Accuracy | TPF |
|---|---|---|
| Qwen3-8B (AR) | 62.75% | 1× |
| NLD-8B AR | 63.61% | 1× |
| NLD-8B Diffusion | 63.18% | 2.57× |
| NLD-8B Linear Self-Spec (LoRA) | 62.81% | 5.99× |
| NLD-8B Quadratic Self-Spec | 64.04% | 6.38× |

On GB200 at concurrency 1: 850 tokens/sec (self-speculation) vs 253 tokens/sec (AR) — 1,015 t/s with custom CUDA kernels.

## Training Ablation

The joint AR-diffusion pipeline outperforms pure diffusion by +16.05% cumulative: AR loss (+7.48%), two-stage training (+5.74%), global loss averaging (+2.12%).
