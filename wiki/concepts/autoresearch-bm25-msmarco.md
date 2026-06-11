---
title: Autoresearch for BM25 Optimization on MSMarco
created: 2026-05-19
updated: 2026-05-19
type: concept
tags:
  - autoresearch
  - agent-loop
  - bm25
  - lexical-search
  - search
  - evaluation
  - methodology
  - overfitting
sources: [raw/articles/2026-05-17_softwaredoug-com_autoresearching-better-msmarco-bm25.md]
---

# Autoresearch for BM25 Optimization on MSMarco

A concrete case study by [[softwaredoug|Doug Turnbull]] (May 2026) applying **autoresearch** — using a coding agent to iteratively optimize a BM25 ranking function — on the MSMarco passage retrieval dataset. This is a domain-specific application of the broader [[autonomous-component-optimization]] pattern, focused on **search relevance tuning**.

## Method: Dual-Gate Agentic Optimization

The agent uses two evaluation gates to balance exploration with guardrails:

| Gate | Visibility | Purpose |
|------|-----------|---------|
| `try_out_patch` (Training Sandbox) | Full per-query visibility | Explore ideas freely |
| `apply_patch` (Validation Gate) | Only pass/fail signal | Prevent overfitting to training data |

### Agent Architecture
- Custom coding agent talks directly to OpenAI (not off-the-shelf tools)
- Submits code patches to the ranking function `rerank_minimarco`
- Has access to: `fielded_bm25` (search primitives), `get_corpus` (raw index stats), `run_reranker` (single-query debugging)
- Can revert states and grep past round logs

### Dataset Strategy
- **Minimarco**: smaller sampled MSMarco subset for fast iteration
- **Full MSMarco**: used only for final measurement
- 8 rounds, each starting from prior round's best code

## Results

### Performance
- **Minimarco**: steady NDCG improvement across all 8 rounds
- **Full MSMarco**: plateaued after round 1 — most gains in MRR (~0.2), then marginal

### Agent's Discoveries
The agent did **not** invent a new BM25 variant. It applied "encyclopedic" tuning tricks from its training data:

1. **Stopword removal** — for queries with >3 tokens, with fallback logic
2. **Phrase/bigram boost** — `0.08 × termfreq` of each consecutive query bigram
3. **Constant term boost** — `+0.25 × (tf > 0)` after BM25 (reward any document containing a query term)

## The Overfitting Trap

Despite the validation gate, the agent overfit to minimarco. The stopword list included **`medicin`** and **`vacat`** — words that happen to be useful to ignore on the minimarco sample but are meaningless for the full dataset.

This demonstrates a subtle form of **data leakage**: any validation gate in a brute-force optimization loop can leak sample-specific information into the final solution. The validation set itself becomes a target for optimization.

> **Key insight**: Smaller proxy datasets accelerate iteration but risk overfitting. Final solutions must always be re-evaluated on full data.

## Relationship to Broader Autoresearch

This experiment sits at the intersection of two trends:

1. **[[karpathy-loop|Karpathy's autoresearch]]**: autonomous loops for ML hyperparameter optimization
2. **[[concepts/coding-agents/pi-autoresearch|Shopify's pi-autoresearch]]**: generalizing autoresearch beyond ML to arbitrary metrics

Doug's work applies the pattern specifically to **search ranking**, where the metric (NDCG) and the optimization surface (BM25 parameters + heuristics) differ from ML training loops.

## Practical Value

Despite the overfitting issues, Doug argues the approach is a **useful tuning tool** for teams focused on a single dataset. Most search teams only care about one corpus, and agent-driven tuning can find small but meaningful improvements faster than manual experimentation.

## Open Questions

1. How to give the agent per-query insights without overwhelming context — the "forest vs trees" problem
2. Whether using the full MSMarco dataset (vs minimarco) would produce more generalizable results
3. Whether a multi-agent architecture (subagents per query group → orchestrator) could improve results

## See Also

- [[softwaredoug]] — Doug Turnbull entity page
- [[autonomous-component-optimization]] — The broader pattern of agent-driven metric optimization
- [[karpathy-loop]] — Karpathy's original autoresearch concept
- [[concepts/coding-agents/pi-autoresearch]] — Shopify's generalized autoresearch
- [[ndcg]] — Normalized Discounted Cumulative Gain, the metric used
- [[concepts/harness-engineering/agentic-loop]] — The underlying agent loop pattern
