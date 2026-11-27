---
title: "Jevons Paradox and Token Demand"
created: 2026-11-27
updated: 2026-11-27
type: concept
tags:
  - economics
  - ai-economics
  - token-economics
  - agent-economics
  - ai-bubble-economics
  - ai-adoption
sources:
  - "raw/articles/2026-11-25_martinalderson_has-jevons-paradox-broken-down.md"
  - "https://martinalderson.com/posts/has-jevons-paradox-broken-down/"
related:
  - "[[concepts/token-economics]]"
  - "[[concepts/ai-bubble-economics]]"
  - "[[entities/martin-alderson]]"
  - "[[concepts/dark-factory-software-factory]]"
---

# Jevons Paradox and Token Demand

**Jevons paradox** — making a resource cheaper increases *total* consumption of it — became a load-bearing assumption of AI-industry revenue forecasts in 2025–2026: falling per-token prices would be outpaced by exploding token volumes. In November 2026 the assumption came under its first serious empirical challenge.

## The "Jevons broke" claim

On a YC podcast, Ramp CEO **Eric Glyman** claimed "over the last two months, Jevons paradox broke." Ramp sees real corporate card / spend-management data from tens of thousands of businesses: **token-spend growth fell from 42% (July) to 1.5% across August and September combined**. Caveats: Ramp's data skews to venture-backed tech companies, misses direct-contract and cloud-provider token purchases, and is noisy.

## Alderson's counter-thesis: steps, not prices

[[entities/martin-alderson]] (ClickHouse engineer and AI-cost blogger) argues Jevons hasn't broken — **within** each adoption step cheaper tokens do raise usage, but growth requires moving *up a step*, which is an organizational problem, not a pricing problem. His four steps of AI adoption:

| Step | Description | Token volume/person |
|---|---|---|
| 1. LLM chat | Occasional chat; most businesses are here | ~50K tokens/day |
| 2. Ad hoc agents | Claude Code et al; SWE far ahead, non-SWE lagging (often blocked on access control) | ~3M/session (his median Claude Code session: 2.6M) |
| 3. Engineered agents | Defined autonomous agents running long, repeatable business processes; mostly startups only | 100s of millions/day |
| 4. Autonomous agents | Self-spawning agentic processes ("software factory"), extended to non-SWE business departments | billions/day |

Since almost everyone is at steps 1–2, he still expects **~4 orders of magnitude** of token-growth headroom.

## Supply-side constraints on demand

Alderson's personal-usage observations, echoed by many practitioners:

- **Idea exhaustion**: "running out of stuff to actually build" — prototypes of a decade of ideas built; featureitis discipline caps new work.
- **Attention caps the burn**: his rule of one hour/day launching "new" agent work, the rest reviewing output — *"it's my attention, not the models, limiting how many tokens I get through."*
- **Burnout**: the pace (product-strategy mulling time down from weeks to hours) is making people sick; the adrenaline is wearing off.
- **Software disposability**: when models turn weeks of engineering into minutes, the motivating grind disappears and finished projects feel disposable — reducing motivation to keep burning.

## The real question

With token prices falling fast (faster per unit of intelligence), the industry's economics hinge on: **does organizational change (agent adoption → token demand) outpace the price decline?** Alderson is genuinely uncertain:

- Ramp's top 1% of spenders = 80% of token spend, so heavy-user plateaus show up directly in the numbers.
- Glyman himself thinks most frontier-model spend could run on simpler models (accelerating the price decline).
- Efficiency gains may hit diminishing returns — his analogy is video compression: staggering 90s improvements, then flattening ("no idea if we are at the MPEG1 stage or the H.264 stage").

## Related

- [[concepts/token-economics]] — price-per-token trends this debate rides on
- [[concepts/ai-bubble-economics]] — the demand-growth assumption underpinning valuations
- [[concepts/dark-factory-software-factory]] — step 4 of the ladder
- [[entities/martin-alderson]] — author; see also "The Coming AI Compute Crunch"
