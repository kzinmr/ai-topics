---
title: "Gemma Model Family"
created: 2026-06-10
updated: 2026-06-10
type: concept
tags:
  - concept
  - google
  - model
  - open-source
  - local-llm
  - inference
  - model-card
  - gemma
aliases: ["Gemma", "Google Gemma", "open Gemma"]
sources:
  - raw/articles/2026-06-10_deepmind-model-cards-page.md
  - https://deepmind.google/models/model-cards/
---

# Gemma Model Family

**Gemma** is Google DeepMind's family of lightweight, state-of-the-art open models. Derived from Gemini research and technology, Gemma models are released under permissive licenses (Apache 2.0 for most variants) and designed for broad accessibility — from on-device deployment to research experimentation.

## Model Card Index

All Gemma model cards are published at [ai.google.dev/gemma/docs](https://ai.google.dev/gemma/) and indexed on the [DeepMind model cards page](https://deepmind.google/models/model-cards/).

| Model | Type | Updated | Model Card |
|-------|------|---------|------------|
| **Gemma 4** | LLM (5 variants: E2B/E4B/12B Unified/26B A4B/31B) | 2026-04-02 | [Model Card](https://ai.google.dev/gemma/docs/core/model_card_4) |
| **FunctionGemma** | Function calling | 2026-01-14 | [Model Card](https://ai.google.dev/gemma/docs/functiongemma/model_card) |
| **EmbeddingGemma** | Embeddings | 2025-09-25 | [Model Card](https://ai.google.dev/gemma/docs/embeddinggemma/model_card) |
| **Gemma 3** | LLM | 2025-08-14 | [Model Card](https://ai.google.dev/gemma/docs/core/model_card_3) |
| **Gemma 3n** | On-device LLM | 2025-06-17 | [Model Card](https://ai.google.dev/gemma/docs/gemma-3n/model_card) |
| **ShieldGemma 2** | Safety classifier | 2025-06-17 | [Model Card](https://ai.google.dev/gemma/docs/shieldgemma/model_card_2) |
| **Gemma 2** | LLM | 2025-02-25 | [Model Card](https://ai.google.dev/gemma/docs/model_card_2) |
| **Gemma 1** | LLM | 2025-02-25 | [Model Card](https://ai.google.dev/gemma/docs/model_card) |
| **CodeGemma** | Code generation | 2025-02-25 | [Model Card](https://ai.google.dev/gemma/docs/codegemma/model_card) |
| **PaliGemma 2** | Vision-language | 2025-02-25 | [Model Card](https://ai.google.dev/gemma/docs/paligemma/model-card-2) |
| **PaliGemma 1** | Vision-language | 2025-02-25 | [Model Card](https://ai.google.dev/gemma/docs/paligemma/model-card) |
| **RecurrentGemma** | Recurrent architecture | 2025-02-25 | [Model Card](https://ai.google.dev/gemma/docs/recurrentgemma/model_card) |
| **ShieldGemma 1** | Safety classifier | 2025-02-25 | [Model Card](https://ai.google.dev/gemma/docs/shieldgemma/model_card) |

## Model Lineage

### Generation 1 (Feb 2024)
- **Gemma 1** — First open release. 2B and 7B parameter dense models. Built from Gemini research.
- **CodeGemma** — Code-specialized variant for generation and completion tasks.
- **RecurrentGemma** — Griffin-based recurrent architecture (linear attention + local recurrence). Alternative to standard transformer.

### Generation 2 (Jun 2024)
- **Gemma 2** — Major upgrade: 2B, 9B, 27B sizes. Improved performance across benchmarks.
- **PaliGemma 1** — Vision-language model combining SigLIP vision encoder with Gemma LLM.
- **ShieldGemma 1** — Safety classification model for content filtering.

### Generation 3 (Mar–Aug 2025)
- **Gemma 3** — Latest dense LLM generation with expanded capabilities.
- **Gemma 3n** — Optimized for on-device/edge deployment (the "n" likely denotes "nano" or "native").
- **ShieldGemma 2** — Second-gen safety classifier with improved detection.
- **PaliGemma 2** — Updated vision-language model.
- **EmbeddingGemma** — Dedicated embedding model for vector representations.

### Generation 4 (Apr 2026)
- **Gemma 4** — Five variants spanning on-device to workstation: E2B (2.3B effective), E4B (4.5B effective), 12B Unified (encoder-free multimodal), 26B A4B (MoE), 31B (dense). Apache 2.0. MTP drafters for up to 3× faster inference.

### Specialized
- **FunctionGemma** — Specialized for structured function calling in agentic workflows (Jan 2026).

## Licensing

All Gemma models use **Apache 2.0** license — no usage restrictions, commercial deployment enabled, fine-tuning permitted. This positions Gemma favorably against Meta's more restrictive Llama license.

## Deployment Ecosystem

Gemma models run on:
- **Google AI Studio** — Cloud-based playground
- **Kaggle** — Model hosting and experimentation
- **Hugging Face** — Model weights and community GGUF quantizations
- **LM Studio** — Local model serving (macOS/Windows/Linux)
- **Ollama** — CLI-based local model management
- **vLLM / SGLang** — High-throughput serving
- **LiteRT-LM** — Edge/mobile deployment
- **MLX** — Apple Silicon optimized inference

## Relationships
- [[entities/deepmind]] — Developer organization
- [[entities/gemma-4]] — Detailed entity page for Gemma 4 family
- [[entities/gemini]] — Parent model family from which Gemma is derived
- [[concepts/model-cards-system-cards]] — Model card analysis framework
- [[concepts/local-llm]] — Local LLM deployment patterns
- [[concepts/speculative-decoding]] — MTP drafter technique used in Gemma 4
- [[concepts/open-weight-models]] — Open model ecosystem and licensing landscape
