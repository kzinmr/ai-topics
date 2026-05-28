---
title: "FastPlaid — High-Performance Multi-Vector Search Engine"
source: https://github.com/lightonai/fast-plaid
date_published: 2025-06-01
author: LightOn
source_site: GitHub (lightonai/fast-plaid)
type: raw_article
topics: [fast-plaid, plaid, colbert, late-interaction, retrieval, rust, gpu]
---

# FastPlaid: High-Performance Multi-Vector Search Engine

**Repository:** lightonai/fast-plaid
**Stars:** 233 | **Forks:** 19
**License:** MIT | **Languages:** Python (55.8%), Rust (44.0%)

## Overview

Fully Rust-implemented engine implementing PLAID (Per-Token Late Interaction Dense Search) for ColBERT/ColPali retrieval. GPU acceleration, token-level similarity matrices, incremental index updates, per-query filtering.

## Quick Start

```python
from fast_plaid import search

fast_plaid = search.FastPlaid(index="index", device="cpu")  # or "cuda"
embedding_dim = 128

# Index 100 docs, each with 300 tokens of dim 128
fast_plaid.create(
    documents_embeddings=[torch.randn(300, embedding_dim) for _ in range(100)]
)

# Search 2 queries, each with 50 tokens
scores = fast_plaid.search(
    queries_embeddings=torch.randn(2, 50, embedding_dim),
    top_k=10,
)
```

## Update an Index

Incremental updates with centroid expansion: new documents accumulate in buffer, K-means creates new centroids at threshold. Small batches added immediately.

## Filtering

Per-query `subset` parameter restricts search to specific document IDs. Often speeds up search dramatically. Increase `n_ivf_probe` for recall under aggressive filtering.

## Per-Token Similarity Matrices

`search_token_scores()` returns token-level matrices for each result — enables interpretability and analysis.

## Settings Trade-offs

| Parameter | Default | Speed Impact | Accuracy Impact |
|-----------|---------|-------------|-----------------|
| `nbits` | 4 | lower = faster | lower = less precise |
| `kmeans_niters` | 4 | higher = slower indexing | higher = better clusters |
| `n_ivf_probe` | 8 | higher = slower | higher = better recall |
| `n_full_scores` | 4096 | higher = slower | higher = better ranking |
| `low_memory` | True | True = slower (GPU only) | No effect |
