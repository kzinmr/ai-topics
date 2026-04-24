---
status: active
type: concept
created: 2026-04-19
updated: 2026-04-19
tags: [multimodal, vision, audio, cross-modal]
sources: []
---

# Multimodal AI — Overview

AI models that process and connect multiple modalities (vision, language, audio). This page is the index for the multimodal concept cluster.

## Core Models

| Model | Modality | Description | Key Use Case |
|-------|----------|-------------|--------------|
| **CLIP** | Vision-Language | OpenAI's contrastive image-text model (400M pairs) | Zero-shot classification, semantic search |
| ~~**Whisper**~~ | ~~Audio-Text~~ | *Moved to [[concepts/speech/whisper.md]]* | — |
| **LLaVA** | Vision-Language | Large Language-and-Vision Assistant | Visual question answering, image chat |
| **Stable Diffusion** | Text-Image | Latent diffusion model for image generation | Text-to-image, image editing |
| **Segment Anything** | Vision | Meta's foundation model for image segmentation | Object detection, mask generation |
| **AudioCraft** | Text-Audio | Meta's audio generation library | Music generation, sound effects |

## Sub-pages

-  — CLIP: Contrastive Language-Image Pre-Training

> **Note:** Whisper moved to [[concepts/speech/whisper.md]] — speech models are conceptually distinct from vision-language multimodal systems.

## Key Concepts

### Zero-Shot Transfer
Multimodal models enable zero-shot capabilities by learning joint embeddings across modalities. CLIP can classify images into categories it was never explicitly trained on.

### Cross-Modal Retrieval
Using one modality to search another (text→image, image→text). Critical for semantic search systems.

### Multimodal Alignment
Contrastive learning aligns representations across modalities in shared embedding space.

## Related Concepts
- [[concepts/fine-tuning/unsloth.md]] — Fine-tuning multimodal models
- [[inference]] — Inference optimization for multimodal
- [[local-llm]] — Running multimodal models locally

## Sources
- OpenAI CLIP paper (2021)
- OpenAI Whisper paper (2022)
- Meta AI research publications
