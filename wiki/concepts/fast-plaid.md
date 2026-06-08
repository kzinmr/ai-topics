---
title: FastPLAID
created: 2026-05-28
updated: 2026-05-28
type: concept
tags:
  - search
  - late-interaction
  - rag
  - developer-tooling
  - open-source
  - optimization
sources:
  - raw/articles/2025-06-01_lighton_fast-plaid-github.md
  - https://github.com/lightonai/fast-plaid
status: active
---

# FastPLAID

**FastPLAID** is a high-performance multi-vector search engine implementing **PLAID** (Per-Token Late Interaction Dense Search), fully written in Rust with GPU acceleration. Built by [[entities/lighton|LightOn]], it is the retrieval engine used by [[concepts/pylate|PyLate]] for indexing and searching ColBERT/ColPali models. MIT licensed.

> "Traditional vector search relies on single, fixed-size embeddings... Multi-vector search, used in models like ColBERT or ColPali, replaces a single document or image vector with a set of per-token vectors."

## Architecture

- **Rust core** (44% of codebase) for maximum performance
- **Python bindings** (55.8%) for easy integration
- Implements PLAID algorithm with IVF (Inverted File) + product quantization
- GPU acceleration via CUDA

## Core API

### Indexing

```python
from fast_plaid import search

fast_plaid = search.FastPlaid(index="index", device="cuda")
fast_plaid.create(
    documents_embeddings=[torch.randn(300, 128) for _ in range(100)]
)
```

### Search

```python
scores = fast_plaid.search(
    queries_embeddings=torch.randn(2, 50, 128),
    top_k=10,
)
# Returns [(document_index, similarity_score), ...]
```

### Incremental Updates

```python
fast_plaid.update(
    documents_embeddings=[torch.randn(300, 128) for _ in range(100)]
)
```

- New documents accumulate in a buffer
- At `buffer_size` threshold, outliers create new centroids via K-means
- Small batches added immediately without centroid expansion

### Per-Token Similarity Matrices

```python
results = fast_plaid.search_token_scores(
    queries_embeddings=torch.randn(2, 50, 128),
    top_k=10,
)
# token_scores.shape == (50, num_doc_tokens) for each result
```

Enables interpretability — see which query tokens matched which document tokens.

### Filtering

```python
scores = fast_plaid.search(
    queries_embeddings=queries, top_k=5,
    subset=[2, 5, 10, 15, 18]  # single filter
)
# Per-query filters:
scores = fast_plaid.search(
    queries_embeddings=queries, top_k=5,
    subset=[[0,1,2], [10,11,12]]  # per-query
)
```

Often speeds up search dramatically. Increase `n_ivf_probe` for recall under aggressive filtering.

## Performance Tuning

| Parameter | Default | Trade-off |
|-----------|---------|-----------|
| `nbits` | 4 | Lower = faster, less precise |
| `kmeans_niters` | 4 | Higher = slower indexing, better clusters |
| `n_ivf_probe` | 8 | Higher = slower, better recall |
| `n_full_scores` | 4096 | Higher = slower, better ranking |
| `low_memory` | True | True = slower on GPU, lower VRAM |

## Key Facts

| Property | Value |
|----------|-------|
| **Company** | [[entities/lighton|LightOn]] |
| **License** | MIT |
| **Language** | Rust (44%) + Python (56%) |
| **Stars** | ~233 |
| **Algorithm** | PLAID (IVF + product quantization) |
| **PyTorch** | 2.7.1–2.9.0 compatible |

## Relationships

- **Framework**: [[concepts/pylate|PyLate]] (uses FastPLAID for retrieval)
- **Company**: [[entities/lighton|LightOn]]
- **Parent algorithm**: PLAID (Santhanam et al., CIKM 2022)
- **Models**: [[concepts/colbert|ColBERT]], ColPali, [[entities/denseon-lateon|LateOn]]
