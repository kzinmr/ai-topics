---
title: "FrontierHarness Eval"
created: 2026-11-19
updated: 2026-11-19
type: concept
tags:
  - harness-evaluation
  - agent-harness
  - benchmark
  - agent-evaluation
  - model-routing
  - cost-optimization
status: L3
confidence: medium
aliases: [FrontierHarness, FrontierHarness Eval v1.1, frontier harness eval]
sources:
  - raw/articles/2026-11-17_runta.com_frontierharness-eval-v1-1.md
  - https://news.ycombinator.com/item?id=50412266
---

# FrontierHarness Eval

**FrontierHarness Eval** is a harness-and-model leaderboard built by Runta (with Baseten for v1.1) that measures a question the model-only benchmarks don't answer: **for a given model, which agent harness gives the best value, and how much of the cost is created by the harness itself?** The headline finding — *the same model on different harnesses can differ dramatically in cost-per-pass* — makes the harness, not just the model, a first-class cost/quality control surface. The v1.1 release posted to Hacker News on 2026-11-17 as "What is the best harness for each model?" (418 points).

## What it is

A matrix benchmark over real coding tasks that varies the **harness** (the scaffolding around the model: prompts, tool APIs, loop/control logic) independently of the **model**, and scores **cost per passed task** as well as pass rate.

| Version | Scale |
|---|---|
| v1.0 (Sept 2026, HN 82p) | 9 harnesses, single model (Kimi K3), cost-per-pass ranking |
| v1.1 (Nov 17 2026, HN 418p) | **22 harnesses × 5 models × 62 tasks × 4 attempts** (~76× v1.0), 83B tokens across 27,280 agent runs |

The two questions v1.1 set out to answer:
1. When you switch your model, should you also switch your harness?
2. What is the best harness for each model?

## Key findings

- **The harness changes the cost.** Switching harnesses while holding the model fixed materially changes cost-per-pass — early v1.0 coverage ("Claude Code cost 5.6× for the same pass") was the motivating result. A "worse" harness can silently multiply spend for identical task outcomes.
- **Harness choice should be co-optimized with model choice.** Because the cost/quality frontier differs per (model, harness) pair, a model migration is also a harness-migration decision; the best harness for model A is not automatically the best for model B.
- **Simpler harnesses tend to cost less**, but the relationship is model-dependent — there is no single cheapest-and-best harness across the matrix.
- The leaderboard surfaces a **best-value frontier** per model rather than a global winner, reinforcing [[concepts/agent-native-tool-fallacy|the harness-tax / tool-fallacy line of work]].

## Why it matters

Most agent evaluation reports accuracy only, treating the harness as fixed scaffolding. FrontierHarness makes harness cost an explicit, comparable dimension — directly useful for [[concepts/model-routing|model routing]] and [[concepts/token-economics|token economics]] decisions in production agent deployments, where the harness is often the controllable variable (you can change your scaffolding more easily than your provider).

**Confidence caveat:** results are Runta/Baseten-published; task set (62 coding tasks) and scoring are their design, and "cost" depends on their chosen token-price assumptions and attempt protocol. Treat rankings as one team's measured benchmark, not an neutral standard — comparable in spirit to [[concepts/ai-benchmarks/hyper-tau-bench]] and the harbor harness ecosystem.

## Related pages

- [[concepts/agent-harnesses]] — the harness category the benchmark evaluates
- [[concepts/agent-native-tool-fallacy]] — harness/tax critique literature
- [[concepts/model-routing]] — co-optimizing model + harness
- [[concepts/ai-benchmarks/hyper-tau-bench]] — sibling agent benchmark
- [[concepts/token-economics]] — cost-per-task as the operational metric
