---
title: "FreshStack Benchmark"
type: concept
created: 2026-04-30
updated: 2026-04-30
tags:
  - concept
  - rag
  - evaluation
  - benchmark
  - information-retrieval
aliases:
  - freshstack-benchmark
  - freshstack
  - p2-modern-ir-evals
sources:
  - path: raw/articles/2026-04-30_hamel-husain-rag-p2-evals.md
  - https://hamel.dev/notes/llm/rag/p2-evals.html
status: active
---

# FreshStack Benchmark

A modern RAG evaluation benchmark developed by **Nandan Thakur** (University of Waterloo) in collaboration with **Databricks**. FreshStack evaluates retrieval for technical RAG using real-time Stack Overflow data, replacing contaminated and saturated benchmarks like BEIR/MTEB.

Presented as **Part 2** of the [[concepts/rag-not-dead-series|RAG Is Not Dead series]].

## The Problem

Traditional IR metrics (MRR, NDCG) were designed for search engines ranking a single best result. RAG needs a **comprehensive evidence set** ("minimal spanning document set") for the LLM to answer accurately. BEIR benchmarks suffer from:
- **Data contamination** — training sets included in model pipelines
- **Leaderboard saturation** — 400+ models with marginal differences
- **Static/too-clean** — HotpotQA etc. are artificial compared to real agentic needs

## Evaluation Pipeline

1. **Nuggetization** — GPT-4o breaks Stack Overflow answers into atomic facts ("nuggets")
2. **Oracle Retrieval** — Candidate documents gathered from GitHub repositories
3. **Support Check** — Judge determines which retrieved chunks support which nuggets

## Key Metrics

| Metric | What It Measures | Rationale |
|--------|-----------------|-----------|
| **Grounding (Coverage@20)** | % of unique nuggets found | Completeness — did we get all the facts? |
| **Diversity (alpha-nDCG@10)** | Penalizes redundant documents | Efficiency — don't repeat the same fact |
| **Relevance (Recall@50)** | On-topic baseline check | Are documents even relevant? |

## Key Findings

- **Massive gap to Oracle** — current retrieval techniques struggle with realistic technical tasks
- **BM25 resilience** — classic keyword search sometimes beats proprietary embedding models on technical docs
- **Size ≠ quality** — small open-source models (Stella, Qwen) are competitive with closed-source models
- **User behavior shift:** *"A traditional search user is impatient... A modern RAG user is patient, asks longer queries, and waits for a synthesized summary."*

## Graph Structure Query

```
[freshstack-benchmark] ──author──→ [entity: Nandan Thakur]
[freshstack-benchmark] ──part-of──→ [rag-not-dead-series]
[freshstack-benchmark] ──contrasts──→ [concept: BEIR]
[freshstack-benchmark] ──contrasts──→ [concept: MTEB]
[freshstack-benchmark] ──relates-to──→ [ai-evals]
[freshstack-benchmark] ──hosted-by──→ [hamel-husain]
```

## Related Concepts

- [[concepts/rag-not-dead-series]] — The 7-part series this is part of
- [[concepts/ai-evals]] — Broader AI evaluation methodology
- [[concepts/modern-retrieval-toolkit]] — Part 1: the retrieval tools being evaluated
- [[concepts/reasoning-retrieval]] — Part 3: complementary retrieval evaluation direction

## Sources

- [P2: Modern IR Evals For RAG — Hamel's Blog](https://hamel.dev/notes/llm/rag/p2-evals.html)
- [Raw article](raw/articles/2026-04-30_hamel-husain-rag-p2-evals.md)
