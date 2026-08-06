---
title: "Castform Retrieval System (Neon)"
created: 2026-08-06
updated: 2026-08-06
type: concept
tags: [retrieval, benchmark, gpt, open-source, cost-optimization, neural-reranking, neon]
sources:
  - raw/articles/2026-08-05_neon_castform-beats-gpt56-retrieval.md
---

# Castform Retrieval System

**Castform** is Neon's open-source retrieval system that achieves GPT-5.6 Sol-level retrieval quality at approximately 100x lower cost, announced in August 2026. It combines semantic search with neural reranking, built on Neon's serverless Postgres infrastructure with pgvector.

## Architecture

Castform uses a two-stage retrieval pipeline:

1. **Candidate Retrieval (pgvector)**: Initial broad retrieval using pgvector's HNSW index on Neon's serverless Postgres. This stage leverages Neon's compute-storage separation to scale vector search independently of the database.

2. **Neural Reranking (cross-encoder)**: A lightweight open-source cross-encoder model reranks the top candidates, improving precision. The reranker is deployed alongside the database to minimize network latency.

## Benchmark Results

Against GPT-5.6 Sol (OpenAI's frontier retrieval model), Castform achieves:

| Metric | GPT-5.6 Sol | Castform | Delta |
|--------|------------|----------|-------|
| NDCG@10 | competitive | competitive | near-parity |
| Cost per query | $0.01-0.05 | ~$0.0001-0.0005 | ~100x cheaper |
| Latency (p50) | ~500ms | ~50ms | ~10x faster |

The key insight: frontier LLMs like GPT-5.6 Sol are overkill for retrieval tasks. A purpose-built pipeline with a small reranker achieves comparable quality at a fraction of the cost.

## Technology Stack

- **Database**: Neon serverless Postgres with pgvector HNSW indexing
- **Reranker**: Open-source cross-encoder model (deployed in same region as database)
- **Embedding Model**: Configurable — supports OpenAI, Cohere, and open-source embeddings
- **Deployment**: Runs on Neon's infrastructure, co-located with user databases to eliminate data transfer costs

## Economics

Castform's 100x cost advantage challenges the assumption that frontier LLMs are necessary for high-quality retrieval. At scale, the savings compound: a system handling 1M queries/day would cost $10,000-50,000/day with GPT-5.6 Sol vs. $100-500/day with Castform. This makes semantic search viable for cost-sensitive applications that previously relied on keyword search.

## Related Pages

- [[entities/neon-database]] — Neon, serverless Postgres provider
- [[concepts/information-retrieval]] — Information retrieval techniques
- [[concepts/information-retrieval]] — Neural reranking in search pipelines
- [[concepts/vector-search]] — Vector search and HNSW indexing
- [[concepts/coding-agents/ai-coding-cost-optimization]] — LLM cost optimization strategies
