---
title: "Semantic IDs"
created: 2026-06-08
updated: 2026-06-08
type: concept
tags:
  - semantic-ids
  - generative-retrieval
  - model
  - search
  - tokenization
  - rag
  - dense-retrieval
sources:
  - raw/articles/2025-09-18_spotify-research_semantic-ids-generative-sr.md
---

# Semantic IDs

Semantic IDs are a method of representing items as discrete token sequences derived from learned embeddings, designed for use in LLM-based generative retrieval and recommendation systems. Unlike traditional approaches that assign unique or sequential identifiers to items, Semantic IDs encode meaningful semantic relationships — items with similar embeddings share token prefixes, enabling generalization to unseen items and better handling of cold-start scenarios.

## How Semantic IDs Work

1. **Embedding**: Items are encoded into dense vector representations using a model (content-based, search-tuned, or recommendation-tuned)
2. **Discretization**: Continuous embeddings are converted to discrete token sequences, typically using **RQ-KMeans** (Residual Quantization with K-Means clustering) or similar hierarchical quantization
3. **Generation**: An LLM generates these token sequences autoregressively as item identifiers in search/recommendation tasks

The key insight is that the *quality* of the Semantic IDs depends entirely on the underlying embedding space. Different task objectives (search vs. recommendation) produce fundamentally different token assignments.

## Approaches to Multi-Task Semantic IDs

When building a unified generative model for both search and recommendation, several strategies exist for constructing shared Semantic IDs:

| Approach | Description | Trade-off |
|----------|-------------|-----------|
| **Task-specific** | Separate Semantic IDs per task | Best single-task performance, poor cross-task generalization |
| **Separate tokens** | Each task has its own ID token set | No shared structure between tasks |
| **Fused SVD** | Embeddings reduced and concatenated | Moderate cross-task transfer |
| **Multi-task bi-encoder** | Joint fine-tuning for both tasks | Pareto-optimal balance across tasks |

Spotify Research (Penha et al., RecSys 2025) showed that multi-task bi-encoder Semantic IDs achieve the best trade-off on the Pareto frontier — no other cross-task method can improve one task without degrading the other.

## Relation to Generative Retrieval

Semantic IDs are a core component of the **generative retrieval** paradigm, where an LLM directly generates item identifiers rather than performing traditional index-based retrieval. This connects to:

- [[concepts/dense-retrieval]] — Semantic IDs encode dense embeddings into discrete tokens
- [[concepts/information-retrieval]] — Generative retrieval is an emerging subfield of IR
- [[concepts/tokenization]] — RQ-KMeans and similar methods are specialized tokenization for item representations
- [[entities/embeddings]] — The quality of the embedding space directly determines Semantic ID effectiveness

## Open Questions

- Can Semantic IDs scale to billions of items while maintaining quality?
- How do Semantic IDs interact with [[rag]] pipelines?
- What is the optimal granularity of the discrete token vocabulary?
- Can hierarchical Semantic IDs capture multi-faceted item semantics (genre + style + recency)?
- How do Semantic IDs compare to traditional inverted index approaches in production latency?
