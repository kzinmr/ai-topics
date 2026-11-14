---
title: "Vision Models"
type: concept
aliases:
  - vision-models
created: 2026-04-25
updated: 2026-11-15
tags:
  - concept
  - vision
  - multimodal
  - vlm
  - model
sources:
  - wiki/concepts/deepseek-vision.md
  - wiki/concepts/multimodal.md
  - wiki/entities/moondream.md
---

# Vision Models

**Vision models** are neural models that take images/video as primary input — for understanding (classification → OCR → full visual reasoning in VLMs) or generation (covered under [[concepts/generative-ai]] / [[concepts/ai-image-generation]]). In the LLM era the category has collapsed into three overlapping stacks: **encoders**, **VLMs**, and **vision-adjacent generators**.

## Architectural Lineage

| Stage | Architecture | Representative |
|-------|-------------|----------------|
| Discriminative CNN (2012–2020) | ResNet/ViT classifiers, detectors | ImageNet era |
| Contrastive alignment (2021) | **CLIP** dual-encoder text↔image embedding ([[entities/alec-radford]]) | powers zero-shot classification, image search, diffusion conditioning |
| ViT backbone era (2021–) | Vision Transformer patches | SigLIP, DINOv2 |
| VLM era (2023–) | ViT encoder + projector + LLM decoder | GPT-4V, [[concepts/deepseek-vision]], Qwen-VL ([[entities/qwen]]), Pixtral ([[entities/mistral-ai]]), Gemini ([[entities/deepmind]]) |
| Native/omni multimodal (2025–) | Interleaved pretraining over all modalities, any-to-any | [[entities/nvidia-nemotron-3-nano-omni]], Gemini native image gen |

## Key Design Decisions in Modern VLMs

1. **Encoder choice**: CLIP-style (semantic, weak OCR) vs SigLIP (soft contrastive) vs DINO (spatial/grounding); many 2026 models use **dual encoders** for semantics + spatial detail.
2. **Resolution strategy**: fixed grid vs native dynamic resolution (AnyRes) vs windowed Hi-Res — the single biggest driver of OCR/document performance.
3. **Grounding**: pixel-coordinate tokenization enables detection/segmentation in-prompt ("point and ask").
4. **Vision in reasoning models**: images handled pre-CoT vs interleaved with chain-of-thought; DeepSeek's vision work ([[concepts/deepseek-vision]]) explored compositional/agent-style visual reasoning over separate specialized models rather than one monolithic VLM.

## Practical Sub-Categories

- **Document & OCR models** — [[concepts/mistral-ocr-4]], layout-aware extraction; classic OCR vs VLM-based document intelligence (OCR and [[concepts/mistral-ocr-4|document OCR]]).
- **Small/on-device vision** — [[entities/moondream]] (sub-2B VLMs for edge), relevant to [[concepts/edge-ai]].
- **Video understanding** — frame sampling vs native video tokenizers, converging with video generation ([[concepts/ai-video-generation-2026]]) and world models.
- **Vision for agents** — computer-use models reading screenshots ([[concepts/computer-use]]) and robot cameras ([[concepts/vla-models]]); vision becomes the agent's sensory harness.

## Evaluation

Classic benchmarks (ImageNet, COCO detection) have been displaced as decision-drivers by VLM suites: MMMU, MathVista, OCRBench/OCRBench v2, DocVQA, video (Video-MME, and agent-screen benchmarks).

## Related Concepts

- [[concepts/multimodal]] / [[concepts/multimodal-vision-audio-cross-modal]] — the umbrella
- [[concepts/vlm-visual-semiotics]] — semiotic framing of VLM visual reading
- [[concepts/transformer-architecture]] — ViT's shared substrate
- [[concepts/embodied-ai]] — vision as robot sensing
- [[entities/alec-radford]] — CLIP/DALL·E lineage

## Sources

- Synthesized from existing wiki pages: deepseek-vision, multimodal, moondream, mistral-ocr-4, qwen, alec-radford (2026)
