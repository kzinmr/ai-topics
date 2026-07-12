---
title: Fastino Labs
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [company, ai-research, open-source, small-language-model, encoder-model, inference, fine-tuning, named-entity-recognition]
sources:
  - https://fastino.ai
  - https://pioneer.ai/blog/introducing-pioneer
  - https://pioneer.ai/blog/behind-pioneer
---

# Fastino Labs

**Fastino Inc.** (Fastino Labs) is an applied research lab specializing in frontier research and inference infrastructure for Small Language Models (SLMs). Its flagship products are [[entities/pioneer-ai]] (SLM fine-tuning & inference platform) and [[concepts/gliner-model-family]] (open-source encoder model family).

## Company Overview

| Item | Details |
|---|---|
| **Legal Name** | Fastino Inc. |
| **Brand Name** | Fastino Labs |
| **Headquarters** | United States |
| **Key Products** | [[entities/pioneer-ai]], [[concepts/gliner-model-family\|GLiNER]] series |
| **Research Areas** | SLM optimization, encoder architecture, synthetic data generation, adaptive inference |
| **License** | Apache 2.0 (open-source models) |

## Technical Vision

Fastino's core belief is that **"specialized SLMs will become the primary building blocks of production AI."** They advocate for a hybrid architecture that leverages the versatility and reasoning capabilities of frontier LLMs while deploying SLMs for tasks requiring high throughput, low latency, and deterministic accuracy.

> "The most effective agentic architectures use both: LLMs for reasoning and planning, and SLMs for high-volume, latency-sensitive tasks that require deterministic accuracy."

## Product Portfolio

### Pioneer (Platform)
→ See [[entities/pioneer-ai]] for details

An automated SLM fine-tuning and adaptive inference platform. Offers Agent Mode (interactive) and Research Mode (fully autonomous). Continuous model improvement from production inference data (Adaptive Inference) is a key differentiator.

### GLiNER Series (Models)
→ See [[concepts/gliner-model-family]] for details

| Model | Parameters | Primary Use | Release |
|---|---|---|---|
| GLiNER (v1) | 50-205M | Zero-shot NER | 2023 |
| GLiNER2 | 205M | NER + Relation Extraction + JSON Extraction + Text Classification | 2025 |
| GLiGuard | 300M | Content Moderation & Safety Classification | 2026-05 |
| GLiNER2-PII | 300M | PII Detection & Masking (42 Entity Types) | 2026-05 |

## Research Achievements

- **3M+ monthly downloads** (cumulative for GLiNER series)
- **3,200+ GitHub Stars**
- GLiNER-based systems serving **1B+ daily end users**
- **AdaptFT-Bench**: A new benchmark proposed for evaluating model improvement under production conditions
- Paper: "Pioneer Agent: Continual Improvement of Small Language Models in Production" (arXiv:2604.09791)

## Key Milestones

| Date | Event |
|---|---|
| 2023-11 | GLiNER v1 release (arXiv:2311.08526) |
| 2025 | GLiNER2 release (arXiv:2507.18546) |
| 2026-01 | GLiNER for Modern NER blog post |
| 2026-02 | GLiNER2 for Agentic Extraction blog post |
| 2026-04 | Pioneer platform launch, Pioneer Agent paper release |
| 2026-05 | GLiGuard release (arXiv:2605.07982) |
| 2026-05 | GLiNER2-PII release (arXiv:2605.09973) |

## Related Pages

- [[entities/pioneer-ai]] — Fine-tuning & Inference Platform
- [[concepts/gliner-model-family]] — GLiNER/GLiNER2/GLiGuard/GLiNER2-PII Model Family
- [[concepts/small-language-models]] — SLM Design Philosophy (Related Concept)
