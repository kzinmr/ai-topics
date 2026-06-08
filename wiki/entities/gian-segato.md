---
title: "Gian Segato"
type: entity
created: 2026-05-28
updated: 2026-05-28
tags:
  - blogger
  - content-creator
  - evaluation
  - methodology
  - ai-product
aliases:
  - gian-segato
  - @giansegato
sources:
  - https://giansegato.com/
  - https://giansegato.com/essays/probabilistic-era
  - https://giansegato.com/essays/agency-is-eating-the-world
  - raw/articles/2025-08_gian-segato_probabilistic-era.md
related:
  - "[[concepts/probabilistic-era-software]]"
  - "[[concepts/evals-vs-monitoring-debate]]"
  - "[[concepts/agent-evaluation-methodology]]"
  - "[[entities/ben-hylak]]"
---

# Gian Segato

AI researcher and product builder on the research team at **Anthropic**. Formerly early at **Replit**, where he trained code models, shipped the first coding agent, and led growth — joining at under $1M ARR and leaving at $150M. Author of influential essays on the ontological shift from deterministic to probabilistic software.

**Current:** Research team, Anthropic
**Previous:** Data Scientist (AI) & Growth Lead, Replit (2022–2025); Founder & CEO, Uniwhere (acquired)
**Education:** BS Economics, Università degli Studi di Padova
**Website:** [giansegato.com](https://giansegato.com/)

## Background

Segato's career spans both the classical and probabilistic eras of software. Before AI, he founded **Uniwhere**, a college-life management app used by a third of Italy's college students before its acquisition. He then joined Replit at a critical inflection point, helping grow the company from <$1M to $150M ARR by training code models, shipping the first coding agent, and leading growth engineering.

At Anthropic, he now works on the research team, contributing to evaluation methodology for coding agents. His engineering post *"Quantifying Infrastructure Noise in Agentic Coding Evals"* was published on the Anthropic Engineering blog.

## Key Ideas

### The Probabilistic Era (Aug 2025)

Segato's most influential essay, *[Building AI Products In The Probabilistic Era](https://giansegato.com/essays/probabilistic-era)*, argues that AI represents an **ontological shift** in software — from deterministic functions `F: X → Y` to probabilistic systems `F'(?)` where input space is infinite and outputs are stochastic estimates.

Core theses:
- **Funnels → Infinite Fields**: Traditional product management (Amplitude, Mixpanel, conversion funnels) relies on pre-known inputs and outputs. AI makes both unbounded.
- **Engineering → Empiricism**: The job of building software shifts from controlling known systems to scientifically observing emergent ones. "It takes a scientist to build AI products."
- **Minimum Viable Intelligence**: A balancing framework — enough control to be market-acceptable, enough freedom to preserve emergent capabilities. Over-constraining nerfs the model.
- **New Model = Reset**: Every model drop invalidates all previous assumptions. Replit rewrote its entire product in 3 weeks when Sonnet 3.7 dropped, leading to revenue inflecting from ~$20M to $100M ARR.
- **Data is the New OS**: In a world of stochastic, emergent behavior, downstream data (how users actually interact) becomes the central organizing function across engineering, product, marketing, and finance.

See [[concepts/probabilistic-era-software]] for the full framework.

### Agency is Eating the World (Apr 2025)

In *[Agency is Eating the World](https://giansegato.com/essays/agency-is-eating-the-world)*, Segato explores how AI agents are enabling individuals to do the work of entire teams. Key observations:
- Solo-founder startups have nearly doubled in recent years
- Companies with handfuls of employees now generate hundreds of millions in revenue
- The average revenue per employee at top AI companies ($2.8M) matches Apple's
- Midjourney: 40 employees, $500M yearly revenue — "a structural shift, not an anomaly"

### Infrastructure Noise in Agentic Coding Evals

Published on the [Anthropic Engineering blog](https://anthropic.com/engineering/infrastructure-noise), this work quantifies how infrastructure-level noise (network latency, sandbox startup time, file I/O variability) affects the reliability of coding agent evaluations — a critical insight for the [[concepts/evals-vs-monitoring-debate|evals vs monitoring debate]].

## Writing

- **[Building AI Products In The Probabilistic Era](https://giansegato.com/essays/probabilistic-era)** (Aug 2025) — The ontological shift from deterministic to probabilistic software
- **[Agency is Eating the World](https://giansegato.com/essays/agency-is-eating-the-world)** (Apr 2025) — AI agents and the rise of solo-founders
- **[The Dawn of a New Startup Era](https://giansegato.com/essays/dawn-of-a-new-startup-era)** (Sep 2024) — How AI changes startup economics
- **[Quantifying Infrastructure Noise in Agentic Coding Evals](https://anthropic.com/engineering/infrastructure-noise)** — Anthropic Engineering

## Ecosystem Connections

- **Ben Hylak** (Raindrop) — Hylak cited Segato's essay (as "Replit's founding engineer") in his *Thoughts on Evals* rebuttal to support the argument that eval datasets lag behind production reality. See [[concepts/evals-vs-monitoring-debate]].
- **Replit** — Segato's experience shipping the first coding agent at Replit directly informs his skepticism of static evals and advocacy for production testing
- **Anthropic** — Current research role; authored the infrastructure-noise eval methodology
- **Michele (Replit President)** — Segato cites Michele's decision to rewrite Replit from scratch when Sonnet 3.7 dropped as the canonical example of probabilistic-era thinking
