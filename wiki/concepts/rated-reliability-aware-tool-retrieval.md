---
title: "RATED (Reliability-Aware Tool Retrieval via Execution Dynamics)"
created: 2026-10-13
updated: 2026-10-13
type: concept
tags:
  - tool
  - mcp
  - ai-agents
  - retrieval
  - context-engineering
aliases: [RATED, EcoAgent benchmark]
sources:
  - raw/papers/2026-10-09_2610.13889_rated-reliability-aware-tool-retrieval.md
  - https://arxiv.org/abs/2610.13889
related:
  - concepts/tool-search-tool
  - concepts/tool-orchestration
  - concepts/programmatic-tool-calling
  - concepts/prompt-optimizers-unscored-requirements
  - concepts/evaluation/reward-hacking
confidence: medium
---

# RATED (Reliability-Aware Tool Retrieval via Execution Dynamics)

> **TL;DR:** Tool retrievers rank by *semantic relevance* and ignore whether a tool actually **works at runtime**. RATED adds a lightweight **contextual bandit** re-ranker on top of a frozen dual-encoder, adapting to live execution failures — **52.2% relative MRR gain** over ToolLLM's retriever and fault-selection rate cut from **86.2% → 2.9%** under 30% API outage, at **<1 ms** overhead. Introduces **EcoAgent**: 5,172 real-world tools, 210K+ query-tool pairs. (arXiv:2610.13889, CIKM 2026)

## The Gap: Relevance ≠ Availability

Tool discovery patterns like [[concepts/tool-search-tool]] and [[concepts/tool-orchestration]] select tools by embedding/lexical similarity to the query. But in real deployments (thousands of MCP servers, third-party APIs), **a semantically perfect tool that is down is worse than a slightly-off tool that responds**. Existing retrieval optimizes the wrong objective: relevance, not *expected successful execution*.

## Architecture

Two components, deliberately cheap:

1. **Frozen dual-encoder** contrastively fine-tuned for semantic matching — never retrained at runtime.
2. **Contextual bandit re-ranker** — consumes real-time execution feedback (success/failure of recent calls) and re-orders candidates. No model retraining; adaptation is an online bandit update.

The whole point is that reliability adaptation must be **online and free**: retraining an embedding model per outage is untenable, and >1ms of latency would break the agent loop.

## Results

| Metric | Baseline | RATED |
|--------|----------|-------|
| MRR (real-world queries) | ToolLLM API retriever | **+52.2% relative** |
| Fault selection rate (30% API outage) | 86.2% | **2.9%** |
| Latency overhead | — | **< 1 ms** over encode-only |

**EcoAgent benchmark:** 5,172 real-world tools, 210,000+ query-tool pairs, supports both offline retrieval eval and *dynamic reliability* eval (the latter is the novel part — no prior tool-retrieval benchmark scored fault avoidance). Code/data: `github.com/Elliotes/EcoAgent`.

## Why It Matters

- Names a failure class agent builders hit constantly: an agent confidently calling a dead API because it ranked #1 by cosine similarity. Treats **tool reliability as a first-class retrieval signal**, not a retry-loop afterthought.
- The bandit formulation (cheap, online, model-frozen) is the right complexity budget for the agent loop — matches the "context engineering" philosophy of not retraining anything mid-flight.
- EcoAgent's dynamic-reliability track gives the field a way to *measure* what [[concepts/tool-search-tool]]-style systems currently can't.

## Open questions

- Cold start: a brand-new tool has no execution history — how much does the bandit's exploration hurt early?
- Interacts with routing/cost: does reliability-weighted ranking systematically prefer cheap-but-degraded tools?

## Consequences for this wiki

RATED is not only a tool-retrieval result. It is the cleanest measured instance of a pattern the wiki keeps meeting from other directions: **an optimiser that is blind to the property you actually care about** (see [[concepts/prompt-optimizers-unscored-requirements]], [[concepts/evaluation/reward-hacking]], [[concepts/ai-benchmarks/benchmaxxing]]).

Two transfers worth writing down:

1. **A bandit re-ranker is an eval, not a guard.** Any retrieval/orchestration system can bolt on an online re-ranker over execution outcomes — but the re-ranker optimises *measured* success only. If the metric is "call returned 200", RATED will systematically steer the agent toward flaky-but-fast endpoints that return junk, exactly the failure GEPA-style prompt optimizers show on unscored requirements. EcoAgent's dynamic-reliability track is the interesting artifact here, not the +52.2% MRR: it is a benchmark for a property (fault avoidance) that previously had no scoreboard.
2. **86.2% → 2.9% fault selection is an infrastructure result dressed as a model result.** The 86.2% baseline is not a model being stupid — it is a *ranking function whose objective omits availability*. The same 83-point swing is available anywhere a team ranks candidates by relevance/quality while treating "did it actually work" as an afterthought (docs retrieval, tool selection, even hiring-style LLM ranking). That reframing matters for [[concepts/model-routing]] and [[concepts/harness-engineering/system-architecture/context-engineering|context-engineering]]-style budget arguments: reliability is the cheapest measurable signal being left out of most rankers, at <1 ms cost.

## See also

- [[concepts/tool-search-tool]] — progressive-disclosure tool discovery
- [[concepts/tool-orchestration]] — orchestration of many tools
- [[concepts/programmatic-tool-calling]]
