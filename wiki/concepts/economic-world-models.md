---
title: "Economic World Models (EWM)"
created: 2026-09-12
updated: 2026-09-12
type: concept
tags: [world-models, ai-agents, economics, simulation, research]
sources:
  - raw/articles/arxiv-2608-06020-economic-world-models.txt
confidence: medium
description: "Generative models that simulate economies from within — heterogeneous agents, beliefs, institutions — via a six-level capability ladder from rule-based agent worlds to sim-to-real economic twins. Survey finds almost all work stuck at the lower levels."
related: [world-model-taxonomy, world-models-for-agents, ai-economics, agentic-economies, ai-labor-displacement, agents-last-exam]
aliases: ["EWM", "agentic economies", "economic simulation"]
---

# Economic World Models (EWM)

**Economic World Models (EWMs)** are generative economic models that simulate how economies evolve *from within*: modeling heterogeneous agents, their beliefs and actions, and the market and institutional mechanisms through which their interactions produce aggregate outcomes. Position and implementation roadmap defined by Han et al., ["From Economic Agents to Agentic Economies: A Systems Blueprint for Economic World Models"](https://arxiv.org/abs/2608.06020) (arXiv:2608.06020, August 2026).

The framing shift: instead of estimating a reduced-form aggregate production function "AI → GDP," an EWM makes the *mechanism* — who does what work, who substitutes for whom, which institutions absorb the shock — the object of simulation.

## The six-level capability ladder

| Level | World type | Key property |
|-------|-----------|--------------|
| 1 | Fixed rule-based agent worlds | Hand-coded behaviors; classical ABM/SD lineage |
| 2 | Adaptive agent worlds | Agents learn/adjust policies within fixed rules |
| 3 | LLM-based agent worlds | Heterogeneous natural-language agents; heterogeneous beliefs emerge |
| 4 | Self-evolving agents | Agents modify their own scaffolding/prompts/memory — the [[concepts/recursive-self-improvement|RSI]] rung applied to economic actors |
| 5 | Evolving institutional worlds | Rules, markets, and norms become endogenous, not just agent parameters |
| 6 | Sim-to-real economic twins | Persistent empirical alignment with real observations; validated mechanisms |

## Survey finding (the paper's punchline)

Across a systematic literature survey organized by these levels, **existing work remains concentrated at levels 1–3**. Systems with *self-evolving agents, endogenous institutions, persistent empirical alignment, and validated economic mechanisms* (levels 4–6) remain rare. The blueprint's purpose is to convert the "agentic economies" agenda from metaphor into an engineering target list.

## Why this matters for the AI-economics debate

The wiki's existing AI-economics pages ([[concepts/ai-economics]], [[concepts/ai-labor-displacement]], [[concepts/agi-economics]]) mostly reason about *outcomes* (jobs, GDP shares, price declines). EWM is the missing *simulation substrate*:

- **Agentic-AI labor data becomes an input.** JobBench's ~44,000 real expert tasks with wages/hours/automation percentages is exactly the kind of micro-foundation a level-3 EWM needs; ALE's O*NET-anchored task taxonomy is another.
- **Agent-market phenomena need agent markets.** When agents transact with agents (Alibaba A2A, Cloudflare pay-per-crawl), the observed price formation *is* the phenomenon a level-5 EWM would model endogenously.
- **Policy sandbox.** The paper's stated aim: high-fidelity sandboxes for human decision-making before deploying labor-substituting AI into real economies.

## Open questions / critiques

- **Validation is the hard part and level 6 is empty.** Without persistent empirical alignment, EWM outputs are elaborate opinion — hence `confidence: medium` on anything these models predict. (The paper itself is a roadmap, not a validated system.)
- **LLM agents are not humans.** Level-3 agents trained on corpus averages may not reproduce the beliefs, risk preferences, or institutional knowledge that drive real markets; the survey notes this but the ladder doesn't quantify the gap.
- **Compute cost scales badly** — a level-4+ simulation with self-evolving agents at national-account granularity is enormous; the paper's roadmap is silent on tractability.
- Risk of *simulation theater*: six-level ladders can organize a field without constraining it. Watch for the first level-5 system with public, validated calibration.

## Related

- [[concepts/world-model-taxonomy]] — the six-category taxonomy of *physical/scene* world models; EWM is the economic sibling dimension
- [[concepts/world-models-for-agents]] — environment-prediction world models for single agents
- [[concepts/agents-last-exam]] — economically-valuable task measurement (micro-foundation source)
- [[concepts/ai-labor-displacement]] — the outcome literature EWM proposes to mechanize

## Sources

- Han et al. ["From Economic Agents to Agentic Economies: A Systems Blueprint for Economic World Models"](https://arxiv.org/abs/2608.06020). arXiv:2608.06020v1, August 2026. Raw: `raw/articles/arxiv-2608-06020-economic-world-models.txt`
