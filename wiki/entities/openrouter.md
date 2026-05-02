---
title: OpenRouter
type: entity
created: 2026-05-02
updated: 2026-05-02
tags:
  - entity
  - platform
  - inference
  - infrastructure
aliases:
  - openrouter.ai
related:
  - [[concepts/openrouter-state-of-ai-2025]]
  - [[entities/malika-aubakirova]]
sources:
  - raw/articles/2025-12-01_openrouter-state-of-ai-2025.md
  - https://openrouter.ai/
---

# OpenRouter

**OpenRouter** is a unified API gateway providing access to 300+ LLMs from multiple providers through a single interface. Founded by Alex Atallah (also co-founder of OpenSea), it serves as a router and abstraction layer that lets developers access models from OpenAI, Anthropic, Google, Meta, DeepSeek, Mistral, and dozens of others without managing separate API keys.

## Key Features

- **Unified API:** Single endpoint for 300+ models from competing providers.
- **Model Routing:** Intelligent request routing to the best available model based on cost, latency, and availability.
- **Fallback Chains:** Automatic failover to alternative models when primary models are unavailable.
- **Cost Management:** Per-model pricing visibility, rate limiting, and budget controls.
- **Credit System:** Prepaid credits with no monthly commitment required.

## The "State of AI 2025" Study

In December 2025, OpenRouter collaborated with a16z (Malika Aubakirova) to publish the **[[concepts/openrouter-state-of-ai-2025]]** study — an analysis of 100 trillion tokens of real-world LLM usage. Key findings include:

- The "reasoning inflection point" (December 2024, o1 release) shifted usage toward multi-step deliberation.
- Open-weight models reached ~30% market share, led by DeepSeek (14.37T tokens).
- Programming and Roleplay dominate usage, not general productivity.
- The [[concepts/glass-slipper-effect|Glass Slipper Effect]] framework for model retention.

## Platform Usage Statistics (from the study)

- **Total tokens analyzed:** 100 trillion across billions of interactions.
- **Top OSS models by tokens:** DeepSeek (14.37T), Qwen (5.59T), Meta LLaMA (3.96T), Mistral (2.92T).
- **Geographic distribution:** USA (47%), Singapore (9%), Germany (7.5%), China (6%).
- **Asia's growth:** Share doubled from 13% to 31% in 2025.

## Market Position

OpenRouter occupies a unique position in the LLM infrastructure stack — it is provider-agnostic, enabling users to benchmark and switch between models fluidly. This neutrality made its data uniquely valuable for the State of AI study, as it captures multi-provider usage patterns rather than single-provider data.

## Related

- [[concepts/openrouter-state-of-ai-2025]] — The landmark 100T token usage study
- [[concepts/glass-slipper-effect]] — Model retention framework identified by the study
- [[entities/malika-aubakirova]] — a16z researcher, co-author of the study

## Sources

- [OpenRouter State of AI 2025](https://openrouter.ai/state-of-ai) — Full study
- [OpenRouter Platform](https://openrouter.ai/) — Official website
