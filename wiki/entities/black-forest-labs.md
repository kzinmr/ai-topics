---
title: Black Forest Labs (BFL)
created: 2026-07-24
updated: 2026-07-24
type: entity
tags: [company, model, multimodal, image-generation, video-generation, robotics]
sources:
  - raw/articles/2026-07-24_ainews-flux3.md
  - https://bfl.ai/blog/flux-3
  - https://bfl.ai/blog/flux-3-mimic
---

# Black Forest Labs (BFL)

**Black Forest Labs (BFL)** is a multimodal AI company founded by former Stability AI researchers, known for developing the **FLUX** family of generative models. Based in Germany (named after the Black Forest region).

## FLUX 3 — Multimodal Flow Models (July 2026)

FLUX 3 is a **unified multimodal model** spanning image, video, audio, and action prediction, built on the Self-Flow architecture. Key capabilities:

- **Text-to-video generation** with native audio.
- **Image-to-video generation**: Continuing from a starting frame ("animation") or using images as visual references.
- **Video-to-video generation**: Carrying central elements (e.g., same character) into new scenes.
- **Generative video-audio continuation** from input video and audio.
- **Keyframe-to-video generation** for controlled transitions.
- **Multilingual dialogue** generation.
- **Agentic chaining**: Chaining individual clips into longer, multi-shot sequences.
- **Strong typography generation** and animated designs.
- **Benchmarks**: Outperforms Seedance 2.0, Gemini Omni, and Grok Imagine on multimodal generation tasks.
- **Early access**: FLUX 3 Video available in early access as of July 2026.
- **Open weights**: A Dev version with open weights is planned.

### FLUX-mimic (Video-Action Robotics Model)

FLUX-mimic is a **Video-Action Model** built on FLUX 3's backbone, combining it with mimic's expertise in robot learning for dexterous manipulation. Key points:
- Trained on robot and wearable data for general-purpose dexterity.
- Deployable on a single on-prem GPU.
- Central thesis: better video world modeling transfers directly into robot control quality and sample efficiency.
- Already being tested with Audi.
- Represents BFL's expansion from media generation into physical-world action prediction.

## Model Lineage

| Model | Release | Type | Notes |
|-------|---------|------|-------|
| **FLUX 1** | 2024 | Image generation (text-to-image) | Original launch; established BFL's position in generative media |
| **FLUX 3** | July 2026 | Multimodal (image/video/audio/action) | Unified architecture; SOTA on multiple benchmarks |

## Key Insights

- FLUX 3's **unified training** (one architecture for all modalities, not a loose family of specialized generators) is its key technical differentiator.
- The model is learning a **sufficient world model** capable of driving robots, as demonstrated by FLUX-mimic.
- BFL's approach contrasts with the trend toward specialized models — they argue that a single architecture can bridge media generation and physical control.

## Relationships

- [[entities/midjourney]] — Competes in generative media
- [[entities/openai]] (Sora) — Competes in video generation
- [[entities/google]] (Gemini Omni, Veo) — Competes in multimodal generation
- [[entities/xai]] (Grok Imagine) — Competes in image generation
- [[concepts/multimodal-models]] — Broader category of multimodal models

## Sources

- BFL Blog: [FLUX 3 Announcement](https://bfl.ai/blog/flux-3)
- BFL Blog: [FLUX 3-mimic](https://bfl.ai/blog/flux-3-mimic)
- AINews coverage: [[raw/articles/2026-07-24_ainews-flux3.md]]
