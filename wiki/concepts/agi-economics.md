---
title: AGI Economics
type: concept
created: 2026-06-05
updated: 2026-06-05
tags:
  - economics
  - agi
  - labor
  - podcast
sources:
  - raw/articles/dwarkesh.com--p-alex-imas-phil-trammell--f12d8644.md
---

# AGI Economics

AGI Economics is an emerging subfield at the intersection of economics and AI research that studies the economic implications of advanced artificial intelligence — including labor share, capital distribution, optimal taxation, sectoral transformation, and the nature of scarcity in a post-AGI world. Key contributors include **Alex Imas** (Director of AGI Economics at Google DeepMind / University of Chicago) and **Phil Trammell** (Head of Economics at Epoch / Stanford).

## Core Questions

The field addresses several fundamental questions about economic structure in a world with AGI-capable automation:

### What Remains Scarce After AGI?

The central question: if AI can automate most productive tasks, what will be the scarce inputs that determine where economic value accrues?

**The Relational Sector** (Imas): Services and goods where the fact that a human is in the loop is part of the value — therapy, live performance, personal care, human-delivered diagnosis. Humans are intrinsically scarce by biology, so if automation saturates almost everything else, relational services retain scarcity value.

**Capital satiation vs. capital accumulation**: Whether wealthy individuals (or AIs) have satiable demand for capital determines whether capital share of GDP converges toward 100%. Historical evidence suggests some agents (Elon Musk, Mark Zuckerberg) have near-unsatiable demand for capital accumulation — preferring to invest in data centers rather than consume.

**Computational scarcity**: The H100 costs more to rent now than three years ago despite technological improvement — because as models get smarter, the opportunity cost of compute increases. Unlike Moore's Law (where transistor value halved every 18 months), AI compute may be the first technology where demand for the underlying resource grows faster than supply improvements.

### Labor Share Dynamics

The labor share of GDP has remained remarkably stable at ~60% for centuries, despite waves of automation (a [Kaldor fact](https://en.wikipedia.org/wiki/Kaldor%27s_growth_model)). Key questions:

- **Will labor share collapse?** If AGI can replace most human cognitive labor, the network-adjusted capital share of some goods may approach 100% for the first time.
- **Structural change buffering**: Historically (phone operators 1920-1940), automated workers were reabsorbed into the economy — but at lower salaries and underemployment (the "messy middle" scenario).
- **Task-based models**: Jobs are bundles of tasks. If AI automates 9/10 tasks, the remaining task becomes more productive (O-ring theory), potentially increasing demand for labor in the complementary role.

### Tax and Redistribution

Multiple policy mechanisms for distributing AGI-generated wealth have been discussed:

| Mechanism | Mechanism | Strengths | Risks |
|-----------|-----------|-----------|-------|
| **UBI** | Universal cash payment | Immediate floor | Political dependence on elected officials; inflation risk |
| **Negative Income Tax** | Tax credit floor + phase-out | Incentive-compatible; automatic | Same political dependency as UBI |
| **Universal Basic Capital** | Ownership shares in capital assets | Property rights, no political dependency | Targeting problem (which assets to hold); valuation risk |
| **Wealth Tax** | Tax on capital holdings | Direct | Political escalation (starts low, increases); investment distortion |
| **Consumption Tax (VAT)** | Tax on consumption → buy stocks → distribute | Broad base; less distortion | Distribution mechanism complexity |

Imas warns: *"If people are just dependent on a check, it really matters who's in power. When we are at the mercy of the elected official for basic needs, that feels like a power-sharing arrangement that's really dangerous."* Universal Basic Capital (ownership shares) may avoid this, but faces the targeting problem — what happens if Anthropic fails but a different AI company dominates?

### Sectoral Transformation

**The Messy Middle scenario** (Molly Kinder): A slow drip of automation where displaced workers are reabsorbed at lower wages — creating political friction without emergency-level unemployment that would trigger a strong fiscal response. Imas notes that even a 2% rapid unemployment uptick would become a national emergency (per Andy Hall's political economy analysis), but slow degradation may not.

**Jevons Paradox**: As something gets cheaper, total consumption may increase. Applies to AI if software demand is highly elastic. But elasticity varies — agriculture production exploded while labor share collapsed; oil demand is inelastic in the short run.

**O-ring automation theory** (Gans & Goldfarb): If AI can automate 9/10 of a job but to lower quality than the human, you may not automate at all — because the one unreliable component can destroy the entire output. Symmetrically, humans may become hard to integrate into fully automated supply chains because their slower/human speed degrades the whole system.

### AGI and Political Economy

- **Demand collapse scenarios**: Despite viral essays predicting AI-driven recession, Imas argues that negative economic growth requires implausible conditions — bounded demand and zero reinvestment — when the technological frontier is expanding.
- **Data poverty**: Imas advocates for a "Manhattan Project for data" on consumer demand elasticities — citing the O\*NET database as rarely updated and low quality. Without elasticity data, economic models of AGI's impact are speculative.
- **AI preferences and capital share**: If AIs themselves become economic agents with preferences (evolved through selection), they may have near-unsatiable demand for compute, driving capital share toward 100%.

## Key Frameworks

### The Pessimistic Moore's Law

Phil Trammell's framing: *"Every 18 months, the value of computation halves."* Traditionally, we run out of uses for computation as fast as it improves — sustaining Moore's Law as a demand-side phenomenon. AI may disrupt this: if model intelligence creates new uses for compute faster than hardware improvements, compute becomes increasingly scarce (rising rental prices for H100s despite manufacturing improvements).

### Increasing Variety and Satiation

Whether capital share collapses or persists depends on whether new varieties of automated goods are created faster than humans satiate on existing ones. Historical example: if a 14th-century Mongolian economist predicted that horse-transport automation would leave everyone spending all their money on singers, they would have been wrong — because new varieties (cars, planes, video calls) expanded the capital-consumption set. The same question applies to post-AGI: will new AI-generated goods and services keep expanding consumption possibilities faster than satiation?

### Man-Not-Horse Principle

The key question for the relational sector: is a human a **horse** (an input into a production process where you only care about the output, and replacement doesn't change value) or a **source of intrinsic value** (where replacement degrades the product)? Imas's experimental evidence: people pay more for art prints made by humans vs. AI (controlled), and this premium disappears when the human-made print is one of 500 rather than unique — suggesting the value comes from perceived connection, not just scarcity.

## Related Concepts

- [[concepts/recursive-self-improvement]] — The economic implications of RSI (Anthropic's thesis) vs. AGI
- [[concepts/agent-stakhanovite-economics]] — Related analysis of AI-driven productivity
- [[concepts/scaling-economics]] — Scaling laws and their economic implications
- [[entities/dwarkesh-patel]] — Podcast host who extensively covers this topic
- [[entities/epoch-ai]] — Phil Trammell's affiliation; tracks AI compute trends

## Sources

- [Dwarkesh Podcast: Alex Imas and Phil Trammell — What remains scarce after AGI?](https://www.dwarkesh.com/p/alex-imas-phil-trammell) (June 2026)
