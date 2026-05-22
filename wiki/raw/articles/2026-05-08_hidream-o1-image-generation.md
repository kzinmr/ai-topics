2026-05-22 | github/HiDream-ai | HiDream-O1-Image: Open-Source 8B Image Generation Model
========================================================================================
Source: https://github.com/HiDream-ai/HiDream-O1-Image
Paper: arXiv:2605.11061
Date: May 8-14, 2026
License: MIT

# HiDream-O1-Image

Natively unified image generative foundation model using Pixel-level Unified Transformer (UiT).
Encodes raw pixels, text, and task conditions in a single shared token space. No external VAEs or disjoint text encoders.

## Key Features
- 8B parameters, MIT license
- Resolutions up to 2048×2048
- Tasks: text-to-image, editing, subject-driven personalization, storyboard
- #8 on Artificial Analysis Text to Image Arena (leading open-weights model)
- Reasoning-Driven Prompt Agent for layout, physical logic, text rendering

## Benchmarks
- GenEval: 0.90 (best open model; Pro 0.92)
- DPG-Bench: 89.83
- HPSv3: 10.37 (GPT Image 2: 10.21)
- CVTG-2K: 0.9128 (GPT Image 2: 0.9003)
- LongText-Bench: EN 0.979, ZH 0.978

## Variants
- HiDream-O1-Image (full, 50 steps)
- HiDream-O1-Image-Dev (distilled, 28 steps)
- HiDream-O1-Image-Dev-2604 (newest, 28 steps, May 14)
- Prompt Agent v1 (gemma-4-31B-it), v2 (HiDream-ai/Prompt-Refine)
