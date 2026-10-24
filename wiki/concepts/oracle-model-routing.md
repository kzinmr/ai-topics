---
title: "Oracle Model Routing"
type: concept
created: 2026-10-23
updated: 2026-10-23
tags:
  - model-routing
  - oracle-routing
  - benchmark
  - coding-agents
  - cost-optimization
  - llm-evaluation
aliases:
  - oracle router
  - oracle routing
  - routing oracle
related:
  - "[[concepts/ai-benchmarks/deepswe-benchmark]]"
  - "[[concepts/model-routing]]"
  - "[[concepts/jagged-frontier]]"
  - "[[entities/fireworks-ai]]"
sources:
  - raw/articles/2026-10-23_fireworks-ai_llm-model-routing-deepswe.md
  - https://fireworks.ai/blog/llm-model-routing-deepswe
---

# Oracle Model Routing

**One-line summary**: On DeepSWE v1.1, an oracle that picks the best of 18 models per task scores **97.6% at $1.88/task** — 23 points above the best single model (GPT-6 Astra, 74.1% at $6.52) at under a third of its cost — so most frontier capability already exists in the pool but is stranded across models nobody pairs together.

## The measurement

Fireworks ran **18 models × 113 DeepSWE v1.1 tasks**, 4 rollouts per model-task pair (2,034 cells), DeepSWE leaderboard refreshed 2026-09-17. Policy is deliberately the simplest possible: pick one model at task start, keep it for the whole run, no mid-session switching. The **oracle** then names the per-task winner by measured pass rate, ties broken on cost.

Best fixed-model policies (accuracy ≈ 70%, $6.46–$13.41 per task):

| Model | Score | Cost / task |
|-------|-------|-------------|
| GPT-6 Astra | 74.1% | $6.52 |
| Claude Opus 5 | 73.8% | $11.84 |
| GPT-5.6 Sol | 72.6% | $6.46 |
| Claude Fable 5 | 69.9% | $13.41 |

Oracle results:

| Policy | Score | Cost / task |
|--------|-------|-------------|
| Oracle over all 18 models | **97.6%** | **$1.88** |
| Oracle over open-weight only (DeepSeek V4 Flash/Pro, GLM-5.3 / GLM-5.3 Flash, Kimi K3, Qwen3.8 Max) | **90.3%** | **$1.45** |

The open-weight-only oracle beats every closed model in the set by **16 points** while spending under a quarter of what Astra costs.

## Oracle bias (read the ceiling skeptically)

The 97.6% is a **hindsight** number. The oracle scores on the same 113 tasks it selects from, and taking a maximum over 18 noisy pass-rate estimates biases the result upward. It measures *capability present in the pool*, not achievable production routing. The companion **LLMRouterBench** (33 models, 400k+ instances) finds a handful of models covers most of what the full set can do, and larger pools add little without careful curation.

Diminishing returns are steep: the best **pair** adds +13.1 points over the best single model, the best **trio** reaches 91.2%, and going from three models to all eighteen adds only another **+6.4 points**. The actionable object is a *portfolio with complementary coverage*, not a catalog of interchangeable models.

## Why real routers fall short of the oracle

A production router has to choose **before** seeing the outcome, and a wrong pick costs far more than the few dollars it saved. Fireworks measured strictly with **pass@1** (probability a single attempt passes) rather than "did this model ever succeed across four attempts" — the latter inflates the ceiling while meaning much less.

**LLMRouterBench** is blunt: several recent routing approaches, including commercial ones, **fail to reliably beat simple baselines**, traced largely to **model recall** — even when a capable model exists in the pool, the router has to recognize when to reach for it. Consequence for practice: staying with one known model is *rational*, not conservative — a stable error distribution beats a router that unpredictably picks the wrong specialist. The bar for any routing system is to make specialization **predictable enough that changing models improves the system without making its behavior less trustworthy**.

## FireRouter (production deployment)

Fireworks' own router routes at task level across open *and* closed models and is **cache-aware**, so switching models does not silently discard context already paid for. Over four weeks of production coding traffic: **$7.42 per routed session vs $15.81 for Opus 5 alone — 53% reduction across 2,334 sessions**.

Fireworks' framing: routing is usually sold as cost optimization (cheap model for easy work). Their claim is stronger — if models are genuinely complementary, selection moves you **up the capability curve**, not merely left along the cost curve. Once several models have complementary strengths, the selection policy becomes a **first-class system component** alongside context, tools, and tests. That is why this belongs next to [[concepts/jagged-frontier]]: complementarity is jaggedness exploited rather than lamented.

## Caveat on cost figures

All cost numbers come from the DeepSWE leaderboard's **published per-model** figures. The raw `cost_usd` in the public trials file does not match what the board displays — for the DeepSeek family it differs by several times — so each model's per-task cost was scaled so its mean matches the published figure. Accuracy comes from the four raw rollouts per model-task pair. Any independent re-derivation must make the same adjustment.

## Related

- [[concepts/ai-benchmarks/deepswe-benchmark]] — the benchmark; Together AI's two-model Pro-first cascade (82.7% @ $8.28) is the cheaper 2-model sibling of this 18-model result
- [[concepts/model-routing]] — Breunig's DSPy + Jev hand-sketchable router: the "predict before the outcome" problem in miniature
- [[concepts/jagged-frontier]] — uneven per-task capability is the substrate an oracle exploits
- [[entities/fireworks-ai]] — FireRouter, Fireworks Nexus, and the model lineup the oracle draws on
- [[entities/together-ai]] — independent DeepSWE routing analyses (Kimi K3 vs GPT-5.6 Sol; DeepSeek V4 Pro 0813 vs Claude Fable 5)

## Sources

- [Model Routing for LLMs: What 18 Models Show on DeepSWE](https://fireworks.ai/blog/llm-model-routing-deepswe) — Fireworks AI, 2026-10-22
