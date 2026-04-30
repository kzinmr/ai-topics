---
title: "Can agents replace the search stack?"
source: "https://softwaredoug.com/blog/2026/04/28/search-apis-replaced-by-agents.html"
authors:
  - Doug Turnbull
  - softwaredoug.com
date: 2026-04-28
---

# Can Agents Replace the Search Stack?

**Source:** https://softwaredoug.com/blog/2026/04/28/search-apis-replaced-by-agents.html
**Author:** Doug Turnbull
**Date:** April 28, 2026

## Benchmark Results (Amazon ESCI)

| Strategy | NDCG |
|----------|------|
| BM25 (baseline) | 0.289 |
| e5_embedding | 0.314 |
| GPT-5-mini + e5 | 0.359 |
| GPT-5-mini + BM25 | 0.385 |
| GPT-5-mini + Both | 0.410 |
| **GPT-5 (Full) + Both** | **0.453** |

A jump from 0.289 to 0.453 simply by using a high-quality model with basic retrievers — no data-specific tuning needed.

## Intelligent Query Refinement

Agents naturally recognize result mismatches and refine queries:

```
Search: "pvc coupler" → networking results (RJ45)
→ "Those are RJ45 couplers... probably asking about PVC pipe couplers"
→ Search: "PVC pipe coupler" (correct)
```

## Encouraged Exploration

Minimum 4 tool calls + similarity threshold (0.9) improved NDCG from 0.410 → 0.4308.

## Key Limitation

Agentic search works for **finding things** (entities: products, jobs, documents) where the agent can judge relevance from metadata. It fails to improve **information retrieval** (MSMarco passages) — "the LLM can't evaluate what it doesn't know."
