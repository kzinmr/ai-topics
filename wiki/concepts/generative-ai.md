---
title: "Generative AI"
type: concept
aliases:
  - generative-ai
created: 2026-04-25
updated: 2026-11-15
tags:
  - concept
  - generative-ai
  - ai-industry
  - multimodal
sources:
  - wiki/concepts/ai-image-generation.md
  - wiki/concepts/ai-video-generation-2026.md
  - wiki/concepts/diffusion-language-models.md
---

# Generative AI

**Generative AI** is the family of models that *produce* new content — text, code, images, audio, video, 3D, and (increasingly) actions — by learning distributions over data and sampling from them. From a 2026 vantage point the term names the 2022–2023 inflection (Diffusion image models + ChatGPT) and the industry it spawned, while technically it unifies: autoregressive transformers, diffusion/flow-matching models, and world models under one sampling-from-distributions frame.

## Modality Map

| Modality | Dominant architecture | Key artifacts in this wiki |
|----------|--------------------|-----------------------------|
| Text | Autoregressive Transformer ([[concepts/transformer-architecture]]) | [[entities/openai]], [[entities/anthropic]], [[concepts/open-source-llms]] |
| Code | Autoregressive + agent harness | [[concepts/ai-coding-tools]], [[entities/cursor-ai]] |
| Image | Diffusion / flow matching, autoregressive hybrids | [[concepts/ai-image-generation]], [[entities/midjourney]], [[entities/black-forest-labs]], DALL·E lineage ([[entities/alec-radford|CLIP/DALL·E]]) |
| Video | Diffusion transformers, DiT | [[concepts/ai-video-generation-2026]], Sora, Veo |
| Audio/Speech | Neural codecs + LM + diffusion heads | [[concepts/speech]], TTS/ASR pages |
| World/Action | Video-pretrained world models, VLAs | [[concepts/embodied-ai]], [[concepts/jepa-world-models]], [[concepts/physical-ai]] |

## Unifying Ideas

- **Scale + sampling**: all modalities converged on large-parameter models trained to predict/score noise, decoded with tunable sampling (temperature, guidance) — the [[concepts/rich-suttons-bitter-lesson]] and scaling-laws research thesis generalized beyond language.
- **Conditioning is the product**: prompt → control (text conditioning, IP-Adapters, LoRAs, style refs). "Prompt engineering" ([[concepts/prompt-engineering]]) was generative AI's first user-facing skill.
- **Autoregressive–diffusion cross-pollination**: language experiments with diffusion ([[concepts/diffusion-language-models]], [[entities/nvidia-nemotron-labs-diffusion]]) and image models adopting AR/tokenizer designs — the two families are converging.
- **From content to action**: the generative stack is being reused as a *world simulator* — video models as world models ([[concepts/world-models-science]]) and action generators ([[concepts/vla-models]]), making [[concepts/embodied-ai]] generative AI's current frontier.

## Socioeconomic Layer

Generative AI's defining controversies are distinct from classic ML: labor displacement and the "absorption frontier" ([[concepts/ai-labor-displacement]], [[concepts/killed-by-gpt]]), copyright and provenance ([[concepts/ai-content-transparency]], Authors Guild v OpenAI), AI-slop and information-ecosystem degradation ([[concepts/ai-slop]]), and the [[concepts/ai-bubble-economics]] valuation debate. [[entities/ethan-mollick]] documents adoption economics; [[concepts/generative-app-evolution]] and [[concepts/generative-ui]] track the application layer.

## Related Concepts

- [[concepts/multimodal]] — models spanning several rows of the table above
- [[concepts/frontier-models-comparison-april-2026]] — the labs and economics of the text tier
- [[concepts/ai-slop]] — the misuse shadow of image/video generation
- [[concepts/ai-image-generation]] / [[concepts/ai-video-generation-2026]] — modality deep-dives

## Sources

- Synthesized from existing wiki modality pages: ai-image-generation, ai-video-generation-2026, diffusion-language-models, generative-ui, midjourney, world-labs, ethan-mollick (2026)
