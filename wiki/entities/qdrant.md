---
title: Qdrant
created: 2026-06-03
updated: 2026-06-03
type: entity
tags:
  - company
  - product
  - platform
  - tool
  - search
  - model
  - hnsw
  - ann
  - rag
  - infrastructure
  - developer-tooling
  - open-source
sources:
  - https://qdrant.tech/documentation/tutorials-search-engineering/branch-aware-search/
  - raw/articles/2026-06-03_zayarni-qdrant-branch-aware-vector-search.md
---

# Qdrant

**Qdrant** (read: quadrant) is an open-source, high-performance vector similarity search engine and vector database. Written in Rust, it provides a production-ready service for deploying vector search at scale with filtering capabilities.

## Overview

- **Type**: Vector database / similarity search engine
- **Language**: Rust
- **License**: Apache 2.0
- **Founded**: 2021 (Berlin, Germany)
- **Website**: [qdrant.tech](https://qdrant.tech)
- **GitHub**: [qdrant-client](https://github.com/qdrant/qdrant)

## Key Features

- **HNSW-based ANN search** with support for payload filtering
- **Nested payload filters** — enables complex filtering on structured metadata attached to vectors
- **Cloud Inference** — server-side embedding generation (free tier available)
- **Quantization** — scalar, product, and binary quantization for memory efficiency
- **Multitenancy** — payload-based tenant isolation
- **Hybrid search** — dense + sparse vectors, BM25 via FastEmbed
- **Edge deployment** — Qdrant Edge for on-device search

## Technical Architecture

Qdrant stores vectors as "points" with associated payload (metadata). Key abstractions:

- **Collections**: groups of vectors with a defined vector configuration
- **Points**: individual vectors with ID, vector data, and payload
- **Payload indexes**: keyword, integer, float, geo, text, and nested indexes for filtering
- **Nested filters**: `must`, `should`, `must_not` conditions with support for nested field queries

## Notable Tutorials

### Branch-Aware Search (2026)

A pattern for scoping vector search results to git-style branches in a versioned document corpus. Each document version is a separate point tagged with branch and sequence number; superseded versions are marked with a nested `overwritten_in` field. Query-time visibility filters enforce branch isolation.

See: [[concepts/branch-aware-search]]

### Other Search Engineering Tutorials

- Multivectors and Late Interaction (ColBERT-style)
- Relevance Feedback Retrieval
- Collaborative Filtering
- Multi-Representation Search
- Measuring ANN Recall

## Related Entities

- [[entities/pinecone]] — managed vector database competitor
- [[concepts/fast-plaid]] — vector search optimization
- [[concepts/branch-aware-search]] — Qdrant's versioned search pattern
