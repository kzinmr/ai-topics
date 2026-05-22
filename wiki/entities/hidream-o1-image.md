---
title: HiDream-O1-Image
created: 2026-05-22
updated: 2026-05-22
type: entity
tags: [entity, model, image-generation, open-source, multimodal, huggingface, text-generation]
sources: [raw/articles/2026-05-08_hidream-o1-image-generation.md, https://github.com/HiDream-ai/HiDream-O1-Image, https://arxiv.org/abs/2605.11061]
---

# HiDream-O1-Image

Open-source image generative foundation model (8B parameters, MIT license) using a **Pixel-level Unified Transformer (UiT)**. Released May 8-14, 2026. Ranks #8 on the Artificial Analysis Text to Image Arena — the leading open-weights text-to-image model.

## Architecture Innovation

Unlike traditional diffusion models (DiTs) that require external VAEs and text encoders, HiDream-O1-Image's UiT encodes **raw pixels, text, and task conditions** in a single shared token space — end-to-end on pixels.

## Key Features

- **Resolution**: Up to 2048×2048
- **License**: MIT
- **Tasks**: Text-to-image, image editing, subject-driven personalization (IP), storyboard generation, long-text rendering
- **Prompt Agent**: Built-in reasoning-driven agent that resolves layout, physical logic, and text rendering before generation (v1: [[entities/gemma|Gemma-4-31B]], v2: custom Prompt-Refine)
- **Efficiency**: 8B scale rivals/outperforms larger DiTs and leading closed-source models

## Variants

| Variant | Steps | Notes |
|---|---|---|
| HiDream-O1-Image (full) | 50 | Undistilled |
| HiDream-O1-Image-Dev | 28 | Distilled, faster |
| HiDream-O1-Image-Dev-2604 | 28 | Latest (May 14), with prompt refiner |

## Benchmarks (8B Model)

| Benchmark | Score | Comparison |
|---|---|---|
| GenEval | 0.90 | Best open model (Pro: 0.92) |
| DPG-Bench | 89.83 | Qwen-Image: 88.32 |
| HPSv3 | 10.37 | GPT Image 2: 10.21 |
| CVTG-2K (4-region text) | 0.9128 | GPT Image 2: 0.9003 |
| LongText-Bench (EN) | 0.979 | FLUX.2: 0.963 |
| LongText-Bench (ZH) | 0.978 | FLUX.2: 0.757 |

## Significance

HiDream-O1-Image demonstrates that a **unified pixel-space Transformer at 8B** can compete with and even surpass large proprietary/DiT-based models across multiple dimensions — compositional generation, dense prompt alignment, human preference, and multilingual text rendering. The MIT license makes it a major open-source alternative to [[entities/flux|FLUX]] and [[entities/gpt-image|GPT Image]].

## Related

- [[concepts/image-generation|Image Generation]]
- [[concepts/diffusion|Diffusion Models]]
- [[entities/flux|FLUX]]
- [[entities/stable-diffusion|Stable Diffusion]]
- [[entities/gpt-image|GPT Image 2]]
