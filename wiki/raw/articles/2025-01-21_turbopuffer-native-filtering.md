---
title: "Native Filtering: CLustering-Based Index for Filtered Vector Search"
date: 2025-01-21
author: Bojan Serafimov (Engineer)
source_url: https://turbopuffer.com/blog/native-filtering
type: raw-article
tags: [turbopuffer, vector-search, filtering, spfresh, lsm-tree, ann]
---

# Native Filtering: Clustering-Based Index for Filtered Vector Search

turbopuffer introduces **native filtered vector search** using a clustering-based index built on SPFresh and the LSM tree. Achieves **>90% recall with filter** while maintaining fast query performance — compared to pre-filter (100% recall, O(n) slow) and post-filter (fast, 0%+ recall).

> "Filtered vector search is hard. Pre-filter is too slow, post-filter loses recall. Native filtering gives you both speed and accuracy."

## The Three Approaches

### Pre-Filter (Exact Filter + ANN)
1. Apply filter to exact attributes
2. Run ANN on filtered subset
3. **100% recall** — but O(n) for filter step on large datasets

### Post-Filter (ANN + Exact Filter)
1. Run ANN to find top-K candidates
2. Apply filter to candidates
3. **Fast** — but potentially 0% recall if no filtered docs in top-K

### Native Filter (turbopuffer's approach)
1. Index integrates both vector similarity and attribute constraints
2. Single traversal finds vectors that (a) match filter AND (b) are nearest neighbors
3. **>90% recall with filter**, fast query times

## Architecture

### Two-Tier Index

```
┌──────────────────────────────────────────────┐
│           Cluster-Level Index                │
│  (attribute_value, cluster_id) → bitmap      │
│  Fast bitmap intersection for filtering      │
├──────────────────────────────────────────────┤
│           Row-Level Index                    │
│  (cluster_id, vector_id) → vector data       │
│  Ann within filtered clusters                │
└──────────────────────────────────────────────┘
```

**Tier 1 — Cluster-Level Index:**
- Key: `(attribute_value, cluster_id)` → bitmap of vectors matching both
- Supports fast bitmap AND/OR operations for multi-attribute queries
- Cluster centroids store attribute statistics for early pruning

**Tier 2 — Row-Level Index:**
- Key: `(cluster_id, vector_id)` → vector embedding and metadata
- ANN search only within clusters that pass the filter
- SPFresh centroids guide the search

### LSM Storage Engine

The filter index is built on the same LSM tree architecture:

```python
# Pseudo: Key encoding for filter-aware LSM
def filter_key(attribute_value: str, cluster_id: int) -> bytes:
    return encode(attribute_value) + encode(cluster_id)

def row_key(cluster_id: int, vector_id: int) -> bytes:
    return encode(cluster_id) + encode(vector_id)
```

- **Cluster-level index uses (attribute_value, cluster_id)** as LSM key prefix
- Enables range scans by attribute value then cluster
- LSM compaction naturally optimizes for attribute groups

## Performance

| Method | Recall (with filter) | Latency | Scalability |
|:---|:---:|:---:|:---:|
| **Pre-filter** | 100% | O(n) | Poor — full scan |
| **Post-filter** | 0-60% (depends on selectivity) | Fast | Good |
| **Native (turbopuffer)** | **>90%** | **Fast** | **Good** |

> "Native filtering achieves >90% recall with filter while maintaining latency comparable to unfiltered ANN. The key is using cluster-level attribute statistics to guide the search."

## Key Insights

1. **SPFresh clustering is naturally filter-friendly** — centroids can store attribute statistics
2. **Two-tier index** separates coarse filtering (cluster-level bitmap ops) from fine-grained scoring (row-level ANN)
3. **LSM tree** enables efficient range scans by `(attribute_value, cluster_id)` order
4. **Attribute selectivity awareness** — the system can adjust cluster search order based on filter selectivity

## Key Contributors

- Bojan Serafimov (Engineer) — native filtering design and implementation

## Related

- SPFresh: Centroid-based ANN index
- [[raw/articles/2026-05-05_turbopuffer-ann-v3]] — ANN v3 improvements
- LSM tree on object storage
