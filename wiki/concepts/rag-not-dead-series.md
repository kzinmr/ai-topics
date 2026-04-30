---
title: "RAG Is Not Dead — 7-Part Series"
type: concept
created: 2026-04-30
updated: 2026-04-30
tags:
  - concept
  - rag
  - retrieval
  - evaluation
  - series
aliases:
  - rag-not-dead-series
  - stop-saying-rag-is-dead
  - hamel-rag-series
sources:
  - path: raw/articles/2026-04-30_hamel-husain-rag-not-dead.md
  - https://hamel.dev/notes/llm/rag/not_dead.html
status: active
---

# RAG Is Not Dead — 7-Part Series

A 2025-2026 open series by [[entities/hamel-husain|Hamel Husain]] and [[entities/ben-clavie|Ben Clavié]] arguing that RAG (Retrieval-Augmented Generation) is not dead — rather, the naive single-vector implementation from 2023 is what deserves criticism. The future of RAG lies in **better retrieval, not bigger context windows**.

> *"Claiming RAG is dead because we're now using better retrieval tools is... akin to claiming HTML is dead because we are now using CSS."* — Benjamin Clavié

## Core Thesis

The 2023 version of RAG (chunk → vector DB → cosine similarity → LLM) fails because compressing entire documents into single vectors loses critical information. But retrieval itself is more important than ever:

- LLMs are **frozen at training time** — they can't learn new information without retrieval
- Million-token context windows don't change the **economics** of stuffing everything into every query
- **Retrieval handles knowledge storage**; model weights focus on intelligence

## The 7 Parts

| Part | Title | Expert | Key Concept |
|------|-------|--------|-------------|
| 1 | [[concepts/modern-retrieval-toolkit|I don't use RAG, I just retrieve documents]] | Ben Clavié | Why naive single-vector search is dead; the modern retrieval toolkit (BM25, ColBERT, agentic search) |
| 2 | Modern IR Evals For RAG | Nandan Thakur | FreshStack: continuously updated benchmarks replacing contaminated MTEB/BEIR |
| 3 | Optimizing Retrieval with Reasoning Models | Orion Weller | Rank1: retrievers that reason about relevance with explicit reasoning traces |
| 4 | Late Interaction Models For RAG | Antoine Chaffin | ColBERT-style token-level preservation outperforming 7B models on reasoning |
| 5 | RAG with Multiple Representations | Bryan Bischof & Ayush Chaurasia | Multiple specialized indices beat one perfect embedding |
| 6 | Context Rot | Kelly Hong | LLM performance degrades with longer inputs; context engineering is critical |
| 7 | [[concepts/graph-db-overengineering-rag|You Don't Need a Graph DB (Probably)]] | Jo Kristian Bergum | GraphRAG is a technique, not a technology; HNSW as hidden graph |

## Key Insights Across the Series

| Insight | Description | Part |
|---------|-------------|------|
| **Single-vector compression is the root problem** | One vector per document loses nuance; late-interaction and multi-vector models preserve it | 1, 4 |
| **IR metrics misalign with RAG needs** | BEIR/MTEB measure top-1; RAG needs coverage, diversity, and corroboration | 2 |
| **Retrievers can reason** | Instruction-following retrievers (Rank1) beat keyword matching on complex queries | 3 |
| **Multiple representations > one perfect embedding** | Route between specialized indices instead of searching for the universal encoder | 5 |
| **Context Rot is real** | LLMs degrade with irrelevant distractors in long contexts, even on simple tasks | 6 |
| **Don't over-engineer** | Graph DBs are almost never needed; HNSW already provides graph structure | 7 |

## Graph Structure Query

```
[rag-not-dead-series] ──author──→ [hamel-husain]
[rag-not-dead-series] ──coauthor──→ [ben-clavie]
[rag-not-dead-series] ──includes──→ [modern-retrieval-toolkit]
[rag-not-dead-series] ──includes──→ [graph-db-overengineering-rag]
[rag-not-dead-series] ──contrasts──→ [naive-single-vector-rag]
[rag-not-dead-series] ──embodies──→ [harness-engineering]
```

## Related Concepts

- [[concepts/modern-retrieval-toolkit]] — Part 1: the modern retrieval pipeline replacing naive RAG
- [[concepts/graph-db-overengineering-rag]] — Part 7: GraphRAG as technique, not technology
- [[concepts/harness-engineering]] — Measure-first philosophy across the series
- [[concepts/ai-evals]] — FreshStack and modern IR evaluation for RAG
- [[concepts/agentic-rag]] — Broader taxonomy of agentic retrieval
- [[concepts/context-graph]] — Context engineering and "context rot"

## Sources

- [Stop Saying RAG Is Dead — Hamel's Blog](https://hamel.dev/notes/llm/rag/not_dead.html)
- [Raw article](raw/articles/2026-04-30_hamel-husain-rag-not-dead.md)
