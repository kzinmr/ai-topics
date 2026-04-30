---
title: "Modern Retrieval Toolkit"
type: concept
created: 2026-04-30
updated: 2026-04-30
tags:
  - concept
  - rag
  - retrieval
  - search
aliases:
  - modern-retrieval-toolkit
  - beyond-single-vector-search
  - p1-dont-use-rag-just-retrieve
  - naive-rag-is-dead
sources:
  - path: raw/articles/2026-04-30_hamel-husain-rag-p1-retrieve-documents.md
  - https://hamel.dev/notes/llm/rag/p1-intro.html
status: active
---

# Modern Retrieval Toolkit

The argument that naive single-vector RAG is dead, but retrieval itself is more essential than ever. Introduced by [[entities/ben-clavie|Benjamin Clavié]] in Part 1 of the [[concepts/rag-not-dead-series|RAG Is Not Dead series]] (hosted by [[entities/hamel-husain|Hamel Husain]]).

## The Core Argument

### "RAG is Dead" is a Myth

The term "RAG" was diluted by marketing in 2023 to mean **naive single-vector semantic search** — chunk documents, embed with one vector per document, do cosine similarity, call it a day. This specific, simplistic implementation is what is "dead."

In reality, RAG is simply **providing external documents to a generative model**. If you add external documents to a context window — even via manual copy-paste — you are technically performing RAG.

> *"Claiming RAG is dead because we're now using better retrieval tools is... akin to claiming HTML is dead because we are now using CSS."*

### Single-Vector Compression is the Root Problem

Compressing entire documents into a single vector (~1000 dimensions) causes:
- **Information Loss:** Massive compression inevitably drops nuances
- **Domain Mismatch:** General-purpose embedding models (trained on public data like Bing search) fail on specialized/proprietary data
- **The "SSD" Analogy:** Modern retrieval techniques replace naive RAG by being "better RAG," not by replacing the concept of retrieval

## Why Long Context Windows Won't Kill Retrieval

Despite models offering 1M+ token windows, retrieval is permanent:

1. **Scale:** 10M tokens is still insufficient for massive enterprise knowledge bases
2. **Efficiency:** Prohibitively expensive and slow to stuff every document into every query
3. **Model Intelligence vs. Storage:** LLM weights are frozen at training time. We want weights focused on **intelligence**, while **retrieval handles knowledge storage** for up-to-date information (e.g., new libraries like `fasthtml`)

## The Modern Retrieval Toolkit

Retrieval is no longer a "one-trick pony." Effective systems combine:

| Method | Examples | When to Use |
|--------|----------|-------------|
| **Traditional Tools** | `grep`, `wget`, `BM25` | Exact matching, code search, known terms |
| **Advanced Embedding Models** | ColBERT (late-interaction), ModernBERT | Preserving token-level detail |
| **Agentic Approaches** | LLM reasoning + web search | Complex queries, multi-step information needs |
| **Multi-Vector Models** | Vector per token instead of one per document | High-fidelity retrieval for nuanced content |

### Hybrid Strategy is Best

The best results come from **combining** methods: keyword search + semantic search + reasoning.

## Relation to Other Parts of the Series

| Part | Connection to Modern Retrieval |
|------|-------------------------------|
| Part 4 (Late-Interaction) | ColBERT is a key example of multi-vector/token-level preservation |
| Part 5 (Multiple Reps) | Specialized indices extend the "don't rely on one vector" thesis |
| Part 6 (Context Rot) | Better retrieval filters distractors; context stuffing fails at scale |
| Part 7 (No Graph DB) | HNSW is the hidden graph — you already have multi-hop via neighbors |

## Graph Structure Query

```
[modern-retrieval-toolkit] ──author──→ [ben-clavie]
[modern-retrieval-toolkit] ──host──→ [hamel-husain]
[modern-retrieval-toolkit] ──part-of──→ [rag-not-dead-series]
[modern-retrieval-toolkit] ──contrasts──→ [naive-single-vector-rag]
```

## Related Concepts

- [[concepts/rag-not-dead-series]] — The 7-part series this concept is part of
- [[concepts/graph-db-overengineering-rag]] — Part 7: complementary perspective on not over-engineering retrieval
- [[concepts/context-graph]] — Context engineering; relates to "context rot" when stuffing everything
- [[concepts/harness-engineering]] — Measure-first design; retrieval should be evaluated, not assumed
- [[concepts/ai-evals]] — Evaluating retrieval quality beyond BEIR/MTEB

## Sources

- [P1: I don't use RAG, I just retrieve documents — Hamel's Blog](https://hamel.dev/notes/llm/rag/p1-intro.html)
- [Raw article](raw/articles/2026-04-30_hamel-husain-rag-p1-retrieve-documents.md)
