---
title: "AI Economics"
type: concept
created: 2026-06-18
updated: 2026-08-17
tags:
  - economics
  - agi
  - inference
  - company
  - platform-economics
  - token-economics
related:
  - [[entities/alex-imas]]
  - [[entities/phil-trammell]]
  - [[concepts/reverse-information-paradox]]
  - [[entities/satya-nadella]]
sources:
  - https://www.dwarkesh.com/p/alex-imus-phil-trammell
  - raw/articles/seangoedecke.com--ai-inference-is-obviously-profitable--ac8d2cd6.md
  - raw/articles/2026-07-12_satya-nadella_reverse-information-paradox.md
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

## Reverse Information Paradox (Nadella, July 2026)

Satya Nadella's second major AI economics framework (after Token Capital) addresses the structural knowledge asymmetry created by AI consumption. Inverting Kenneth Arrow's classic information paradox, Nadella argues that AI model providers accumulate intelligence exhaust from every enterprise interaction — prompts, corrections, tool usage patterns — creating a one-way flow of tacit knowledge from buyers to sellers.

Key economic implications:

- **Asymmetric learning flow**: If model providers learn from customer usage but restrict distillation rights, economic value converges toward learning infrastructure owners rather than knowledge creators
- **The trust boundary problem**: Cloud-era data protection is insufficient; AI-era protection must cover learning mechanisms (traces, evals, adapted weights)
- **Five imperatives for enterprise sovereignty**: Control, Capability, Choice, Cost, Compound — forming a continuous learning loop that compounds AI investment
- **Distributed learning infrastructure**: Nadella argues for distributing learning infrastructure to every firm rather than centralizing it in model providers

This framework extends the inference economics analysis by identifying a **structural cost** beyond GPU pricing: the leakage of proprietary organizational knowledge through normal AI use.

See: [[concepts/reverse-information-paradox]], [[concepts/token-capital]], [[entities/satya-nadella]]

## Token Brokers & the AI Credit Resale Economy (Aug 2026)

Vectoral's threat-research piece (Matt Lenhard, Aug 10, 2026, HN 301pts on Aug 16) documented a growing **secondary market for AI inference credits** — "token brokers" buying unused credits from startups and reselling them at steep discounts:

- **Market mechanics**: Startups with pre-paid API credits (often from accelerator/VC deals or volume commitments) sell unused allocation at **40–50% off list**; brokers act as proxy relays, pooling provider keys and forwarding requests rather than handing over credentials. One broker offered **$100k/day in spend**.
- **Infrastructure**: Dedicated marketplaces, bulk-discount routers, and message boards now list off-market inference; the practice is being "commercialized" beyond informal startup-forum swaps.
- **Why it matters economically**: Resale arbitrage reveals the gap between **list price and marginal cost** of frontier inference — consistent with the inference-economics analysis above (70–80% gross margins leave room for a secondary market), and creates new risks for providers (ToS violations, key revocation, fraud laundering) and for buyers (no provider guarantees, ToS exposure).

This is the inference-layer analogue of the "credit resale" pattern in cloud/GPU markets and signals maturing (and arbitrage-heavy) token economics.

Sources: [Vectoral — Who Are the Token Brokers?](https://vectoral.com/blog/who-are-the-token-brokers) / [HN discussion](https://news.ycombinator.com/item?id=49329755)

## Sources
- [Alex Imas and Phil Trammell - What remains scarce after AGI?](https://www.dwarkesh.com/p/alex-imus-phil-trammell)
- [Sean Goedecke - AI inference is obviously profitable](https://seangoedecke.com/ai-inference-is-obviously-profitable/)
