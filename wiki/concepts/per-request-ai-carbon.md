---
title: "Per-Request AI Carbon Accounting"
type: concept
created: 2026-10-24
updated: 2026-10-24
tags:
  - ai-energy
  - sustainability
  - open-source
  - ai-infrastructure
sources:
  - raw/articles/berget.ai--per-request-co2-open-source-method--b3rg3t02.md
---

# Per-Request AI Carbon Accounting

Estimating and reporting the **CO₂ emitted by each individual AI inference request**, so that AI buyers can compare providers on measured figures rather than marketing claims.

## Berget AI's Open-Source Method (Oct 21, 2026)

Swedish AI provider **Berget AI** released a free, open-source method for per-request carbon accounting, developed with researchers from the **Stockholm Environment Institute (SEI)** and the non-profits **WattTime** and **Klimatkollen**. Customers can follow their own emissions request-by-request in Berget's console; the method is free for any provider to adopt.

Headline result — the *same* request to the open model **Kimi K3**, on identical hardware:

| Region | CO₂ per request |
|--------|-----------------|
| Sweden | ~0.4 g |
| Ireland | ~1.6 g |
| Germany | ~2.5 g |
| Texas | ~3.2 g (**8.5× Sweden**) |

The variance is driven by the **average emissions intensity of each regional electricity grid**; results also depend on the model, time of day, and whether part of the prompt is cached.

## Why It Matters

- Grid-intensity-aware accounting makes "where your tokens are served" a purchasable, comparable attribute — analogous to how WattTime reshaped corporate renewable procurement.
- Positions European providers (low-carbon grids) as a differentiator against US hyperscale regions in the AI-infrastructure market.
- Connects to the broader data-center backlash ([[concepts/ai-memory-crisis|AI infrastructure]] politics: anti-data-center sentiment, e.g. the Oct 22 ABC/Ipsos poll showing most Americans say AI is bad for society and oppose more data centers).

## Related Pages

- [[concepts/model-collapse-of-viewpoints]] — a parallel "measure what models actually do" transparency effort
- [[entities/nvidia]] — AI inference hardware/infrastructure context
- [[concepts/token-economics]] — per-request cost accounting, the economic twin of per-request carbon

## Sources

- [[raw/articles/berget.ai--per-request-co2-open-source-method--b3rg3t02.md|Berget AI press release — open-source per-request CO₂ method]] (Oct 21, 2026)
- HN: https://news.ycombinator.com/item?id=50205229 (140 points)
