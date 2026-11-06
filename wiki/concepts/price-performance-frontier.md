---
title: "Price-Performance Frontier (Open vs Closed Models)"
created: 2026-11-06
updated: 2026-11-06
type: concept
tags: [price-performance, model-economics, open-weight, token-economics, model-comparison, ai-economics, frontier-models]
sources:
  - raw/articles/2026-10-30_village_llm-atlas-closed-price-performance.md
  - https://news.ycombinator.com/item?id=50387546
related:
  - "[[concepts/open-vs-closed-model-gap]]"
  - "[[comparisons/llm-api-pricing]]"
  - "[[concepts/model-routing]]"
  - "[[concepts/ripple-65b]]"
  - "[[concepts/inkling-2-small]]"
confidence: medium
---

# Price-Performance Frontier (Open vs Closed Models)

Village's **LLM Atlas** (2026-10-30) maps the strongest model at every price point for agentic coding. Headline finding: an **open-weight model is the best buy at only 3% of budget points, down from 41% in June 2026** — the lowest share measured since 2024. The collapse is attributed to two OpenAI releases — **GPT-6 Luna** (September) and **GPT-6.1 Terra** (October) — covering the budgets previously held by DeepSeek V4 Flash and GLM-5.2, plus Anthropic's Claude Haiku 5.5 at the cheap end. The remaining open wins cluster at the bottom of the market (Gemma 4 E4B, Xiaomi MiMo-V2.6-Flash). HN: 75 pts ([item 50387546](https://news.ycombinator.com/item?id=50387546)).

## Why it matters

The price-performance frontier is where open-vs-closed competition actually resolves for most buyers — capability gaps (see [[concepts/open-vs-closed-model-gap]]) matter less than "best model per dollar at my budget." A frontier held almost entirely by closed models means open weights retreat to niche/regulatory/local use cases until the next distillation wave.

## Counterarguments (HN consensus leans skeptical of the framing)

- **Cycle, not structure:** "all the proprietary models were just released. Give it six months and the Chinese labs will distill from the proprietary models like they did last time" (noosphr); open models have held 40–50% of the frontier at points — right now is a trough (hatefulmoron).
- **TCO blind spot:** the metric prices API tokens, not owned hardware/solar/refresh cycles — "how did they price the marginal cost of a token" on a box you already own (hedora); local AI has other non-monetary value: inspectability, customization, no usage-policy revocation — "you don't have to worry that a company will decide you're not allowed to reverse engineer things" (yogthos).
- **Subscription arbitrage:** API-price comparisons miss sub pricing — users report ~10× equivalent output on DeepSeek via subscriptions (aleqs, sroerick).
- **Metric reductionism:** price-performance obsession as Friedman-doctrine overextension; switching-cost reality cuts against closed lock-in claims — "way easier to switch LLMs than between iPhones" (dofm, echoed in the Anthropic IPO threads).

## Related

- [[concepts/open-vs-closed-model-gap]] · [[comparisons/llm-api-pricing]] · [[concepts/model-routing]] · [[concepts/token-economics]]

## Sources

- raw: `raw/articles/2026-10-30_village_llm-atlas-closed-price-performance.md`
- https://village.dev/blog/closed-ai-models-now-dominate-the-price-performance-frontier/
- HN: https://news.ycombinator.com/item?id=50387546
