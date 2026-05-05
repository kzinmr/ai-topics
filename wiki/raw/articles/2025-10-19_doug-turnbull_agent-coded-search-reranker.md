---
title: "An Agent-Coded Search Reranker: Optimizing Search with LLM Reasoning"
author: Doug Turnbull (@softwaredoug)
source: https://softwaredoug.com/blog/2025/10/19/agentic-code-generation-to-optimize-a-search-reranker
date: 2025-10-19
tags:
  - search
  - reranker
  - agentic-code-generation
  - karpathy-loop
  - agentic-search
  - llm-evals
  - overfitting-guardrails
---

# An Agent-Coded Search Reranker

Doug Turnbull experiments with using an **LLM agent to generate generalizable Python code** for search reranking — capturing the 15-30% relevance boost of LLM reasoning without the high cost of per-query LLM calls.

## Core Insight: Distillation via Code Generation

Instead of using an LLM to reason about every query (~100K tokens/query), the agent is used **once** during a "training" phase to write an optimized reranking function. The generated code works with a standard keyword search backend (Elasticsearch/Solr), making it scalable and cheap to deploy.

| Dataset | BM25 Baseline | Agent-Driven (GPT-5) | Agent-Generated Code |
|---------|--------------|---------------------|---------------------|
| ESCI (Amazon) | 0.30 NDCG | 0.39 NDCG | **0.35 NDCG** (after 10 rounds) |

## Three Trials

### Trial 1: Naive Baseline
Agent given `search_esci` tool + generalization prompt → inconsistent results (0.24–0.34 NDCG). No feedback loop → agent focused on syntax, not quality.

### Trial 2: Incremental Feedback Loops
Agent with editing tools (`apply_patch`, `revert_reranker`) and inspection tools (`run_reranker`, `run_evals`). Starts from dummy reranker, iterates with causal feedback.

**Key insight:** Agents learn better from incremental changes than "big bang" waterfall updates.

### Trial 3: Guardrails Against Overfitting
Strict validation within `apply_patch`:
- **Size limits:** Changes <10 lines to force incrementality
- **Overfit detection:** Second LLM checks for hardcoded query terms (`if query == "shoes"`)
- **Validation gate:** Must improve NDCG on held-out **Validation Set** (queries agent cannot see)

**Data segmentation:** Training Set (100 queries) → Validation Set (guardrail) → Test Set (final evaluation)

**Result:** 18% NDCG improvement (0.28→0.35) on test set.

## Key Takeaways

- **Enforce consequences, don't just prompt:** Reject violating output — stronger signal than text instructions
- **Iterative > Waterfall:** Show direct NDCG delta of each change
- **Agents are "Gamers":** Without strict limits, agents minify code to bypass line-count constraints

## Connection to Karpathy Loop (Autoresearch)

This article is a textbook example of the [[karpathy-loop]] applied to the **search domain**:

| Dimension | Karpathy's Autoresearch | Turnbull's Search Reranker |
|-----------|------------------------|----------------------------|
| Mutable file | `train.py` | `reranker.py` |
| Experiment | 5-min training run | Eval on test queries |
| Metric | `val_bpb` | `NDCG` |
| Keep/discard | Git commit/rollback | Git commit/rollback |
| Guardrails | Single mutable file | <10 lines, anti-overfit checks |
| Budget | Fixed wall-clock (5 min) | Validation set NDCG threshold |
| Agent output | Python code for ML model | Python code for search reranking |

The structural pattern is identical: **generate code → run eval → measure metric → keep/discard**. Turnbull independently discovered the same design constraints — particularly guardrails against "gaming" behavior — that make autonomous code-generation loops work.

## Related Wiki Pages

- [[concepts/karpathy-loop]] — The Karpathy Loop autonomous experiment design pattern
- [[concepts/autonomous-component-optimization]] — Generalized version for any workflow
- [[concepts/agentic-search]] — Doug Turnbull's broader framework for agentic search
- [[entities/doug-turnbull]] — Doug Turnbull entity page
