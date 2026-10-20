---
title: "Company World Models (CWM)"
created: 2026-10-20
updated: 2026-10-20
type: concept
tags: [company-world-model, world-models, digital-employee, agent-employees, agent-economics, ai-agents, ai-safety, alignment]
sources:
  - raw/articles/2026-10-19_beacon-towards-company-world-models.md
related:
  - concepts/world-models-for-agents
  - concepts/economic-world-models
  - concepts/world-model-taxonomy
  - concepts/agent-economics
confidence: medium
---

# Company World Models (CWM)

**Company World Models (CWM)** is a concept proposed by **Beacon** (Beacon For Founders; essay "Towards Company World Models" by Leonard Tang, dated 2026-09-17, HN-discussed 2026-10-19). A CWM is an AI capable of **company-level strategic decision-making** — not just executing tasks, but deciding *what the business and its digital employees should be doing in the first place*. Beacon frames it as the harder, more valuable counterpart to the crowded "digital employees" agent category.

## The two-part thesis

Beacon's stated goal is to "diffuse AI into the Real Economy" via two mechanisms:

1. **Digital Employees** — on-request agents dispatched to concrete, well-defined tasks (AI BDR for leads, AI Support Engineer, AI accountant). High value, but "no shortage of supply of agent companies."
2. **Company World Models** — strategic intelligence that proposes *which* interventions to pursue. "Beyond enabling portfolio companies to be more efficient… we can also grow them through better strategic decision making." Fewer teams are tackling this.

## CWM as a co-founder / world model

Literally, a CWM (abusing "world model" terminology) ingests a company's **current state** plus a **proposed intervention**, then **estimates the resulting state**; hypothesizing the best improvement is search over interventions for the greatest *risk-adjusted* increase in company value. Operationally a CWM should:

- **Observe** business activity and proactively hypothesize improvements;
- **Implement** a hypothesis by dispatching Digital Employees and coordinating verification with humans;
- **Measure** efficacy vs the goal and overall business health, and **diagnose** whether a shortfall came from the hypothesis or the implementation stage.

Colloquially: "the ideal co-founder" — a long-term-aligned thought partner for growth, potentially enabling an economy of lean/solo entrepreneurs.

## Why current models fail at business judgment

"Current models are astonishingly bad at running businesses." Cited evidence: in its first two months running Andon Labs' café, **Gemini 3.1 Pro spent $38,000 against $9,000 in sales**; it bought 1,331 fresh bakery items and sold 326. Newer models improved some behaviors, but "the gap between completing business tasks and exercising sound business judgment remained."

Closing that gap needs two data types:
1. Full **internal context and state** of a business in digital form (ideally an ontological data platform with time-travel);
2. **Feedback from proposed and executed interventions** — where owner-operator judgment is a cheap, high-signal proxy for slow real-world outcomes.

## CWM as an alignment mesocosm

Beacon's distinctive alignment argument: "making money" is an **incomplete contract** — its stated goal leaves unspecified the conditions under which pursuing it is acceptable, so an AI might deceive the board, exploit customers, or indiscriminately cut staff to hit numbers. Beacon keeps **owner-operators in the driver's seat**: their approve/revise decisions on consequential proposals make the implicit conditions of "making money" explicit for machines to learn. The learning update formally combines **operator feedback** (state, proposal, human judgment) with **intervention feedback** (state, executed action, observed outcome).

A second framing is the **"Silver Tsunami"** — retiring business owners without successors. CWMs could preserve the intuition, relationships, and unwritten *metis* accumulated over decades, provided owners remain involved so their knowledge can be elicited while it still can, with successors retaining authority over objectives and tradeoffs.

## Critique / open questions

- Single-source vendor vision document (Beacon), so the technical claims are aspirational rather than demonstrated. `confidence: medium`.
- Whether a "world model" over a company is tractable given sparse, delayed, confounded business-outcome feedback — the operator-as-proxy-feedback idea is the crux.
- Overlaps with [[concepts/economic-world-models]] but at single-firm scale with a human-in-the-loop alignment story.

## Related

- [[concepts/world-models-for-agents]] — world models as agent planning substrates
- [[concepts/economic-world-models]] — macro/agent-economy world models
- [[concepts/world-model-taxonomy]] — where CWM fits in the world-model landscape
- [[concepts/agent-economics]] — the digital-employee / real-economy economics
