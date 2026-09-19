---
title: "Economic Agent Benchmarks"
created: 2026-09-19
updated: 2026-09-19
type: concept
tags: [benchmark, agent-evaluation, ai-agents, long-horizon, agent-economics, agent-safety, economics, open-source]
sources:
  - raw/articles/arxiv-2606.16613-coffeebench.md
  - raw/articles/arxiv-2602.09514-ecogym.md
  - raw/articles/arxiv-2502.15840-vending-bench.md
confidence: high
related: [long-horizon-agents, decentralized-agent-orchestration, economic-world-models, agent-reliability-and-long-horizon-work]
aliases: ["CoffeeBench", "EcoGym", "Vending-Bench", "economy benchmarks"]
---

# Economic Agent Benchmarks

A distinct benchmark family that emerged in 2025–2026: instead of asking an agent to solve a task, **let it run a business inside a simulated economy and score it on money over a long horizon**. These benchmarks became the empirical proving ground for [[concepts/long-horizon-agents]] because business operation combines persistence, memory, negotiation, stochasticity, and partial observability in one score.

## The lineage

**Vending-Bench** (Backlund & Petersson, Mindware, [arXiv:2502.15840](https://arxiv.org/abs/2502.15840), Feb 2025) is the origin: an agent runs a vending-machine business for a simulated year; the headline finding was a **phase transition** — models are fine for a few weeks, then, once context windows overflow, "simply give up and stop taking actions." It became the industry's canonical long-coherence stress test and spawned a sequel series (Vending-Bench 2, TheAgentCompany comparisons, etc.).

**EcoGym** (Hu et al., [arXiv:2602.09514](https://arxiv.org/abs/2602.09514), Feb 2026) generalizes and open-sources the idea: three environments — **Vending** (an open reimplementation of the previously closed-source Vending-Bench), **Freelance**, and **Operation** — with unified interfaces and budgeted actions over 1000+ steps, scored on business outcomes (net worth, income, DAU). Two robust findings across eleven leading LLMs: **no model dominates all three environments**, and models are systematically suboptimal in *either* high-level strategy *or* efficient execution — the two layers come apart. EcoGym is explicitly positioned for studying **controllability–utility trade-offs**, connecting it to [[concepts/evaluation/miscontrol-solve-rate|miscontrol measurement]].

**CoffeeBench** (Sugiura et al., [arXiv:2606.16613](https://arxiv.org/abs/2606.16613), June 2026) adds the missing dimension: **heterogeneous multi-agent economies**. Two farmers, two roasters, two retailers run a 90-day coffee supply chain; the evaluated model controls one roaster while fixed reference agents run the rest. Success requires communicating, negotiating, and transacting, not just deciding. Findings: all tested models beat a do-nothing baseline and most earn positive net income, but **higher-performing models communicate more actively**; Claude Haiku 4.5 shows an "**idle-drift**" failure mode — coherent plans, repeated inaction.

## What the family establishes collectively

| Benchmark | Horizon | Multi-agent? | Key failure mode surfaced |
|---|---|---|---|
| Vending-Bench (2025) | ~1 year | no (passive env) | context-overflow collapse / giving up |
| EcoGym (2026) | 1000+ steps | partially | strategy↔execution split; no dominant model |
| CoffeeBench (2026) | 90 days | **yes** (6 firms) | idle drift; under-communication |

Together they support three conclusions the wiki treats as well-established:

1. **Long-horizon coherence is a separate capability from task competence** — it fails abruptly, not gracefully (see [[concepts/agent-reliability-and-long-horizon-work]]).
2. **Money is a good scalar for it** — net worth over months is hard to game compared to rubric scores.
3. **Economic interaction is where agent weaknesses compound** — negotiation, reputation, and cash-flow turn isolated failures into systemic ones, which is why these environments are also used for [[concepts/decentralized-agent-orchestration|market-mechanism evaluation]].

## Open questions

- Reference agents (CoffeeBench) are fixed — models may exploit static opponents rather than negotiate well.
- Whether "no dominant model" reflects genuine domain-specific capability or benchmark-ecosystem noise.
- Convergence risk: Vending-Bench-derived environments now dominate training curation; scores may saturate without coherence improving.

## Related

- [[concepts/long-horizon-agents]] — the capability these benchmarks operationalize
- [[concepts/economic-world-models]] — the research agenda these benchmarks instantiate (CoffeeBench/EcoGym are exactly EWM levels 3–5)
- [[concepts/decentralized-agent-orchestration]] — markets as orchestration, evaluated in these same environments
- [[concepts/vending-bench-2]] — the follow-up benchmark family
