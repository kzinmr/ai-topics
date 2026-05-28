---
title: "Probabilistic Era — Building AI Products After the Ontological Shift"
type: concept
created: 2026-05-28
updated: 2026-05-28
tags:
  - methodology
  - agent-evaluation
  - ai-product
  - probabilistic-systems
  - reliability
aliases:
  - probabilistic-era
  - probabilistic-software
  - building-ai-products-probabilistic-era
sources:
  - raw/articles/2025-08_gian-segato_probabilistic-era.md
  - https://giansegato.com/essays/probabilistic-era
related:
  - "[[concepts/evals-vs-monitoring-debate]]"
  - "[[concepts/agent-evaluation-methodology]]"
  - "[[entities/gian-segato]]"
  - "[[entities/ben-hylak]]"
---

# Probabilistic Era — Building AI Products After the Ontological Shift

A framework for understanding the **fundamental ontological shift** from deterministic software (`F: X → Y`) to probabilistic AI products (`F'(?)`), articulated by [[entities/gian-segato|Gian Segato]] (Anthropic research, early Replit). The essay explains why traditional engineering, product management, and growth playbooks break down when applied to AI — and what must replace them.

> "We're leaving a world where code reliably and deterministically takes certain inputs to produce specific outputs, and entering a very different one where machines now produce statistical distributions instead." — Gian Segato

## The Ontological Shift: From Funnels to Infinite Fields

### Classical Software: F: X → Y

| Dimension | Deterministic Era | Probabilistic Era |
|---|---|---|
| **Function** | `F(x) = y` — known inputs, expected outputs | `F'(?)` — open-ended inputs, stochastic outputs |
| **Input space** | Limited, pre-determined (`X` has known cardinality) | Infinite, emergent (users can ask anything) |
| **Output** | Guaranteed correct (goal: 100% reliability) | Statistical estimate (hallucinations inherent) |
| **Marginal cost** | Near-zero | Significant and stable (intelligence has real cost) |
| **Testing** | TDD, unit tests, binary pass/fail | Statistical eval, production A/B, trajectory analysis |
| **Product paradigm** | Funnels (Amplitude, Mixpanel, conversion rates) | Infinite fields (user trajectories, state classification) |
| **Knowledge model** | Engineered — we designed it, we know it | Discovered — emergent, unknowable, "vibe" |
| **Engineering mindset** | Reliability, control, incremental building | Empiricism, managing uncertainty, tear-down-and-rebuild |

### The Funnel Mentality Breaks

The entire operating system of the modern tech industry — SLOs, TDD, funnels, conversion optimization, ratio-based decision making — relies on both input space `X` and output space `Y` being **limited and known beforehand**. This assumption is what makes counting, ratios, and optimization possible.

AI models break this assumption fundamentally:
- **Input space becomes infinite** — `F'` accepts anything; you can't enumerate possible inputs
- **Output becomes stochastic** — Same prompt yields different results (by design, randomness lets users navigate complex problem spaces)
- **Correctness becomes ambiguous** — Many questions have no single "correct" answer ("should I leave him?")

> "In moving to an AI-first world, we transitioned from funnels to infinite fields. Our products can now succeed in ways we've never even imagined, and fail in ways we never intended."

### Stochasticity Is a Feature, Not a Bug

Randomness at inference time is **purposeful**:
- It provides users a way to efficiently navigate complex problem spaces
- It lets users inject their own taste and navigate probability distributions
- Over long trajectories, small differences magnify — enabling creative exploration

This is why "reliability" in the classical sense (100% deterministic SLO) is the wrong goal for AI products. The tension between **deterministic cost** and **stochastic output** is a built-in feature, not a defect to be eliminated.

## Minimum Viable Intelligence

The core paradox of AI product building: **intelligence and control are opposing needs**. The more you constrain a model with rails and guardrails, the more you nerf its emergent capabilities.

Segato introduces **Minimum Viable Intelligence** as the balancing framework:

> "The lowest quality threshold that is both accepted by the market, while preserving the model's inherent flexibility and generalization capacity."

Too much control → the model loses the surprising capabilities that make it valuable. Claude Code refusing to add watermarks because "I can only make websites" defeats the purpose. But too little control → unacceptable failure modes.

## It Takes a Scientist: Engineering → Empiricism

The transition from deterministic to probabilistic products demands a **fundamentally different organizational mindset**:

### New Model Drops = Reset All Assumptions

> "Every time a new model drops, all previous assumptions about its behavior should be disregarded. You should even consider literally tearing down the full system, and building it back from the ground up. There are no sacred cows."

**Case study: Replit v2** — When Sonnet 3.7 dropped with novel agentic capabilities, Replit's President Michele (a scientist by trade) had the company completely rewrite the product in under 3 weeks. Revenue inflected from ~$20M ARR to $100M ARR within a quarter. The key insight: Michele **leaned into** the model's new capabilities rather than trying to control them.

### Models Have Personalities

Swapping models at the app layer is not "just an API change." Models have personalities and quirks — which makes frontier labs stickier than they appear. Gemini Pro 2.5 was not a Claude 3.5 killer despite being an exceptional model, because the integration work required is substantial.

### The Job Description Has Changed

Classical engineering skills (layering, TDD, cautious refactoring) become counterproductive. Even "simple" prompt changes require:
- Statistical testing (not binary pass/fail)
- Understanding second-order effects on tool usage, unit economics, user behavior
- Production A/B testing to capture long-tail outcomes
- Empirical mindset: "I don't know" as the only valid starting assumption

## Data is the New Operating System

Because model behavior is emergent and unknowable, **downstream data** (how users actually interact post-deployment) becomes the most critical asset.

### User Trajectories, Not Funnels

Traditional funnels assume you know what success looks like. In AI products, you don't:
- Are longer message chains "better software" or frustrated debugging?
- Are shorter messages efficiency or giving up?

The solution: aggregate **user trajectories** — paths through the field of possible tasks and model states. Use smaller models to classify user requests, segment "regions of usage," and define milestones across different paths.

### Holistic Data Function

In AI products, previously siloed functions collapse into one system:
- Customer attribution (marketing/sales)
- Observability (engineering)
- A/B testing (product/design)

A 20% shift from game-building users to professional web apps can mean the difference between sustainable unit economics and bleeding money — but this insight only emerges from analyzing AI interaction content, not traditional funnel metrics.

## Connection to the Evals vs Monitoring Debate

Segato's essay provides the **ontological foundation** for [[concepts/evals-vs-monitoring-debate|Ben Hylak's argument against eval-centric development]]:

| Segato's Insight | Hylak's Argument |
|---|---|
| "Eval dataset will constantly lag behind" (infinite input space) | Evals are adversarially selected — you only test what you already know |
| "Testing in production with traditional A/B tests is critical" | Production truth > offline evals |
| "Cardinality of input space is basically infinite" | Agents are too much to test, but not too much to monitor |
| "Every new model drop invalidates all assumptions" | Models deprecate faster than anything in software history |
| "Minimum Viable Intelligence" — control nerfs capability | "I don't know" refusals lower pass rates but increase trust |

Both arrive at the same conclusion from different angles: Segato from the **ontological nature** of the technology, Hylak from **practitioner experience** at scale.

## Practical Implications

### For Engineering Teams
- Abandon SLO-style reliability targets for AI components
- Replace binary pass/fail testing with statistical evaluation
- Build infrastructure for constant production sampling and trajectory analysis
- Be prepared to tear down and rebuild when new models drop

### For Product Teams
- Move from funnel optimization to trajectory analysis
- Classify user inputs to understand "regions of usage"
- Accept that you don't fully know what your product can do
- Ship fast and learn from production, rather than trying to pre-specify all behavior

### For Leadership
- Hire scientists, not just engineers
- Build data functions that span the entire organization (not siloed analytics)
- Budget for the "deterministic cost, stochastic output" tension
- Treat model swaps as potential full rewrites, not API changes

## Further Reading

- **[Agency is Eating the World](https://giansegato.com/essays/agency-is-eating-the-world)** — Segato on the rise of agents and solo-founder companies
- **[Quantifying Infrastructure Noise in Agentic Coding Evals](https://anthropic.com/engineering/infrastructure-noise)** — Segato's Anthropic engineering post on eval reliability
- **[[concepts/evals-vs-monitoring-debate]]** — Hylak vs Goyal on evals vs production monitoring
- **[[concepts/agent-evaluation-methodology]]** — Floor raising framework incorporating probabilistic-era insights
