---
title: "AI Economics"
type: concept
created: 2026-06-18
updated: 2026-06-27
tags:
  - economics
  - agi
  - inference
related:
  - [[entities/alex-imas]]
  - [[entities/phil-trammell]]
sources:
  - https://www.dwarkesh.com/p/alex-imus-phil-trammell
  - raw/articles/seangoedecke.com--ai-inference-is-obviously-profitable--ac8d2cd6.md
---
# AI Economics

AI economics explores the impact of artificial intelligence on labor markets, wealth distribution, and global productivity.

## Key Concepts
- **Labor Share**: The potential for AI to reduce the share of labor in GDP.
- **Forecasting Challenges**: The difficulty of traditional economics in predicting the outcomes of radical automation.
- **Prediction Markets**: The use of aggregate wisdom to provide more accurate forecasts on AGI-related events.

## Inference Economics

Analysis of AI inference profitability based on [Sean Goedecke's article](https://seangoedecke.com/ai-inference-is-obviously-profitable/) (June 2026).

### Cost Breakdown

A single Nvidia A100 consumes 400W under full load. Running a dense 70B model on four A100s yields ~2M tokens/hour. At US industrial power prices (~$0.10/kWh), power costs ~13c/hr. With cooling (pessimistically equal to power), total energy cost is ~26c/hr, or ~13c per million output tokens. Amortizing GPU cost ($20k per A100 over a five-year lifespan) adds ~$1.80/hr, bringing total estimated inference cost to roughly **$1 per million tokens**.

### Gross Margins

OpenAI charges $4.50/MTok for GPT-5.4-mini, with stronger models priced 3–6x higher. Given the ~$1/MTok estimated cost, the claimed **70–80% gross margins** on inference are "extremely plausible."

### Open-Weight Validation

DeepSeek claims a bit over **80% profit margin** on inference for DeepSeek-R1. Since their API pricing is less than half of OpenAI/Anthropic, actual inference costs may be even lower than the ~$1/MTok estimate — economies of scale, more efficient GPUs, and cheaper cooling contribute. DeepSeek-V4-Pro's market pricing (~87c/MTok) is likely close to the actual cost of serving the model, as open-weight availability forces competitive pricing.

### Training Subsidy

AI labs (OpenAI, Anthropic) maintain high inference margins because **inference must subsidize training costs**. Subscription models ($200/month for unlimited Claude Code) are "almost certainly not profitable" — equivalent API usage would cost 10x more. The high margins fund the training arms race for new models rather than reflecting genuine inference costs.

### Inference-Only Viability

Even if OpenAI or Anthropic go bust, inference remains profitable. An inference-only provider (no training costs) can operate at much lower margins. Whoever acquires rights to frontier models can continue selling inference at a profit. **AI inference is obviously profitable** — the business model does not depend on VC subsidies or the survival of any particular AI lab.

## Sources
- [Alex Imas and Phil Trammell - What remains scarce after AGI?](https://www.dwarkesh.com/p/alex-imus-phil-trammell)
- [Sean Goedecke - AI inference is obviously profitable](https://seangoedecke.com/ai-inference-is-obviously-profitable/)
