---
title: "Search Scaling"
created: 2026-09-29
updated: 2026-09-29
type: concept
tags:
  - ai-agents
  - test-time-scaling
  - inference
  - research-agent
  - reasoning
confidence: medium
sources:
  - raw/articles/2026-09-29_arxiv_2609.35559_search-scaling-autonomous-factor-mining.md
related:
  - test-time-compute
  - test-time-interaction-scaling
  - harness-learning
  - agents-scaffolding-composition-inference-scaling-hypothesis
---

# Search Scaling

**Search scaling** is the extension of *inference scaling* to autonomous agents: performance can be improved by increasing the agent's **search budget** — the amount of exploration it is allowed to do across a research/optimization loop — not just by making more tokens per answer.

> Introduced in "From Search to Research: Exploring Search Scaling in Autonomous Quantitative Factor Mining" (arXiv:2609.35559, Sept 2026) — Deng, Cai, Lu, Qian, Sun, Luan, Li, Jiang, Bai.

## Core Idea

Inference scaling is well-characterized for single-turn LLMs. For *autonomous research agents* the analogue is search scaling. The authors probe how search budget, model capability, and search *organization* shape the quality of an end-to-end research task.

Testbed: **50 quantitative factor-mining tasks** grounded in financial research reports. Each task requires a full research loop — interpret a hypothesis → implement it in code → evaluate → iteratively refine the resulting factor. Evaluated across **nine models**.

## Findings

1. **Model capability vs. search depth.** Initial (low-budget) performance tracks model capability most strongly, but *deeper search narrows cross-model gaps* — enough search lets weaker models catch up.
2. **Model grafting.** Transferring an *intermediate* research state from one model to another shows the **early research state materially shapes final performance** — where an agent has gotten to by mid-task is itself predictive.
3. **Parallel > sequential search.** Under the *same* iteration budget, parallel search beats sequential search, consistent with broader coverage of the search space.

Trajectory analysis adds that higher-performing models more effectively **diagnose failures, revise search directions, and preserve the intended economic hypothesis** when selecting candidates.

## Where It Fits

Search scaling is a *third* test-time axis alongside the two already documented in the wiki:

| Axis | What is scaled | Page |
|------|----------------|------|
| Reasoning tokens | CoT length | [[concepts/test-time-compute]] |
| Environment interactions | number of tool/env steps | [[concepts/test-time-interaction-scaling]] |
| **Search budget** | **exploration over a research/optimization space** | **this page** |

Like [[concepts/harness-learning]], search scaling spends extra *deployment-time compute* — but here the currency is breadth of exploration, and the new lever is *how* the budget is organized (parallel vs. sequential, and what state carries forward via grafting).

## Open Questions

- Is "model grafting" (handing off an intermediate state) a reliable tool, or does it leak the previous model's biases into the next?
- Parallel search wins under a fixed iteration budget — does it still win under a fixed *token/wall-clock* budget, where parallelism is costlier?
- The domain is finance-specific (factor mining); generality to other autonomous-research tasks is untested.

^Single source (arXiv preprint, not yet peer-reviewed; finance-domain testbed). Provisional.

## Related Concepts

- [[concepts/test-time-compute]] — the broader inference/test-time scaling landscape
- [[concepts/test-time-interaction-scaling]] — the interaction-count axis
- [[concepts/harness-learning]] — adapting the harness instead of the search budget
- [[concepts/agents-scaffolding-composition-inference-scaling-hypothesis]] — how scaffolding/composition interacts with inference scaling

## Sources

- [From Search to Research: Exploring Search Scaling in Autonomous Quantitative Factor Mining](https://arxiv.org/abs/2609.35559) — arXiv:2609.35559, 2026-09-28
