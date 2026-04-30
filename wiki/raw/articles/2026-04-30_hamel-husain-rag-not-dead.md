---
title: "Stop Saying RAG Is Dead"
source: https://hamel.dev/notes/llm/rag/not_dead.html
author: Hamel Husain, Ben Clavié
date: 2025-07-12
type: article
---

# Stop Saying RAG Is Dead

Why the future of RAG lies in better retrieval, not bigger context windows.

**Authors:** Hamel Husain, Ben Clavié
**Published:** July 12, 2025

Hamel Husain and Ben Clavié put together an open 7-part series discussing why RAG is not dead, and what the future of RAG looks like.

The oversimplified version from 2023 deserves the criticism: chuck documents into a vector database, do cosine similarity, call it a day. That approach fails because compressing entire documents into single vectors loses critical information. But retrieval itself is more important than ever. LLMs are frozen at training time. Million-token context windows don't change the economics of stuffing everything into every query.

## What We Learned

- **Nandan Thakur** — Traditional IR metrics optimize for finding the #1 result. RAG needs different goals: coverage (getting all the facts), diversity (corroborating facts), and relevance.
- **Orion Weller** — Retrievers that understand instructions like "find documents about data privacy using metaphors." Rank1 system generates explicit reasoning traces about relevance.
- **Antoine Chaffin** — Late-interaction models like ColBERT preserve token-level detail instead of single vector compression. 150M parameter models outperforming 7B alternatives on reasoning tasks.
- **Bryan Bischof & Ayush Chaurasia** — Multiple representations. Art search demo finds the same painting through literal descriptions, poetic interpretations, or similar images.
- **Kelly Hong** — "Context Rot": LLM performance degrades significantly as input length increases, even on simple tasks.
- **Jo Kristian Bergum** — You don't need a graph database for GraphRAG. A CSV or Postgres works fine. Vector search already uses graphs (HNSW).

## 7-Part Series

| Part | Title | Expert | Key Focus |
|------|-------|--------|-----------|
| 1 | I don't use RAG, I just retrieve documents | Ben Clavié | Why naive single-vector search is dead, not RAG |
| 2 | Modern IR Evals For RAG | Nandan Thakur | FreshStack: continuously updated benchmarks |
| 3 | Optimizing Retrieval with Reasoning Models | Orion Weller | Retrievers that reason about relevance |
| 4 | Late Interaction Models For RAG | Antoine Chaffin | ColBERT-style models overcoming single-vector limits |
| 5 | RAG with Multiple Representations | B. Bischof & A. Chaurasia | Multiple specialized indices vs one perfect embedding |
| 6 | Context Rot | Kelly Hong | LLM performance degradation with longer inputs |
| 7 | You Don't Need a Graph DB (Probably) | Jo Kristian Bergum | Graph databases usually overkill for RAG |
