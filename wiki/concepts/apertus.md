---
title: "Apertus"
created: 2026-06-22
updated: 2026-06-22
type: concept
tags:
  - apertus
  - open-source
  - foundation-models
  - sovereign-ai
  - eu-ai-act
  - model
  - training
  - hn-popular
sources:
  - raw/articles/2026-06-21_apertus-open-foundation-model-sovereign-ai.md
---

# Apertus

**Apertus** is an open foundation model for [[concepts/sovereign-ai|sovereign AI]], described by its creators as "Apertus is to AI as Open is to Source." It is a fully open release — training data, code, weights, methods, and alignment principles are all documented and reproducible. The model is designed to serve as a global foundation for sovereign AI development, with explicit compliance with the [[concepts/eu-ai-act|EU AI Act]].

## Core Principles

Apertus is built around a philosophy of radical openness. Unlike many "open" models that release only weights while keeping training data and methods proprietary, Apertus releases every component:

- **Training data** — fully documented and reproducible
- **Code** — all training and inference code
- **Weights** — full model weights at both scales
- **Methods** — training methodology, architecture decisions, and alignment techniques
- **Alignment principles** — explicitly documented safety and alignment approach

This follows the [[concepts/open-source-ai|open-source AI strategy]] philosophy of transparency enabling audit, adaptation, and trust.

## Technical Specifications

Apertus is available at two parameter scales:

| Scale | Description |
|-------|-------------|
| **8B** | Smaller model, suitable for on-device deployment and [[concepts/model-distillation|distillation]] |
| **70B** | Full-scale model, competitive with top open models at equivalent size |

Both scales are **multilingual from day one**, trained on **1,000+ languages** — a deliberate design choice to avoid the English-first approach common in other foundation models.

### Distillation Models

Alongside the main models, the Apertus project released **16 small language models** specifically designed to demonstrate [[concepts/model-distillation|distillation]] and quantization techniques. These serve as research artifacts for the community to study model compression and efficiency.

## EU AI Act Compliance

Apertus is among the first major foundation models explicitly built to meet **[[concepts/eu-ai-act|EU AI Act]]** requirements:

- **Opt-out respect**: The model respects data opt-out requests from individuals and rights-holders
- **PII removal**: Personally identifiable information is systematically removed from training data
- **Memorization prevention**: Training methodology designed to prevent verbatim memorization of training data
- **Transparency**: Full documentation of data sources, training methods, and model capabilities

This compliance positioning makes Apertus particularly significant for European governments, institutions, and enterprises that must operate under EU AI Act regulations.

## Significance for Sovereign AI

Apertus represents a milestone in the [[concepts/sovereign-ai|sovereign AI]] movement. While [[entities/mistral-ai|Mistral AI]] has positioned itself as Europe's sovereign AI champion with open-weight models, Apertus goes further by releasing the full pipeline — data, code, and methods. This enables nations and organizations to:

- Audit the entire model pipeline for security and bias
- Reproduce training from scratch with their own data
- Adapt and fine-tune with full understanding of the base model's provenance
- Deploy without dependency on a single corporate provider

## Comparison to Other Open Models

Apertus differentiates itself from other prominent open-source AI initiatives:

| Aspect | Apertus | [[entities/mistral-ai|Mistral]] | [[entities/meta|Llama]] | [[entities/deepseek|DeepSeek]] |
|--------|---------|--------|-------|----------|
| Weights | Open | Open | Open | Open |
| Training data | Fully open | Not disclosed | Not disclosed | Partially disclosed |
| Training code | Open | Not disclosed | Not disclosed | Not disclosed |
| Multilingual (day one) | Yes (1000+ languages) | Limited | Limited | Limited |
| EU AI Act compliance | Explicit | Implicit | No | No |
| Distillation models | 16 released | Some | Some | Some |

## Open Questions

- Will Apertus achieve the adoption necessary to become a genuine global foundation for sovereign AI?
- Can a fully open model maintain competitiveness with proprietary frontier models over time?
- How will the EU AI Act compliance claims be validated by independent auditors?
- Will other model providers follow Apertus's lead in full pipeline transparency?

## Related Pages

- [[concepts/sovereign-ai]] — The broader movement for national and regional AI independence
- [[concepts/open-source-ai]] — Open-source strategy in AI development
- [[concepts/eu-ai-act]] — European Union AI regulation framework
- [[concepts/model-distillation]] — Techniques for compressing large models into smaller ones
- [[entities/apertus]] — The organization behind the Apertus model

## Overview
The Apertus project releases foundation models at 8B and 70B parameter scales, along with 16 smaller models for distillation and quantization research. All components — training data, code, weights, methods, and alignment principles — are fully documented and released openly.

Apertus is distinguished by being the first major foundation model explicitly built for [[concepts/eu-ai-act|EU AI Act]] compliance, respecting data opt-outs, removing PII, and preventing memorization of training data. The model is trained on 1,000+ languages from day one, positioning it as a truly global foundation.


## Key Facts
| Field | Detail |
|-------|--------|
| **Website** | [apertvs.ai](https://apertvs.ai/) |
| **Announced** | June 2026 |
| **Model Scales** | 8B and 70B parameters |
| **Languages** | 1,000+ (multilingual from day one) |
| **Small Models** | 16 released for distillation/quantization research |
| **Key Differentiator** | Full pipeline openness: data, code, weights, methods, alignment |
| **Compliance** | EU AI Act (opt-outs, PII removal, anti-memorization) |
| **HN Reception** | 406 points, 136 comments on [Hacker News](https://news.ycombinator.com/item?id=48622778) |


## Relationship to Sovereign AI Ecosystem
Apertus enters a landscape where [[entities/mistral-ai|Mistral AI]] has been the primary European sovereign AI champion. Where Mistral releases open-weight models but keeps training data and methods proprietary, Apertus goes further by making the entire pipeline reproducible. This positions Apertus as a potential foundation for governments and institutions that require full auditability.

The project aligns with the [[concepts/sovereign-ai|sovereign AI]] movement's goals of reducing dependency on a small number of US-based AI providers and enabling nations to build AI capabilities on auditable, transparent foundations.

