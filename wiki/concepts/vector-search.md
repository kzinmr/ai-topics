---
title: Vector Search
created: 2026-05-13
updated: 2026-05-13
type: concept
tags:
  - search
  - model
  - hnsw
  - ai-agents
sources: [raw/articles/2026-05-13_softwaredoug_vector-search-embeddings.md]
---

# Vector Search

Vector search is the problem of finding the **nearest neighbors** to a query vector in high-dimensional embedding space — the retrieval backbone of modern semantic search, recommendation systems, and [[concepts/rag|RAG]] pipelines.

## The Core Problem

Given:
- **N corpus vectors** (millions to billions) in d-dimensional space (384–1536 dims)
- **A query vector** q

Find the **k nearest neighbors** by cosine similarity (or Euclidean distance). Brute force O(Nd) is infeasible at scale. Approximate Nearest Neighbor (ANN) algorithms are essential.

## The Curse of Dimensionality

> "Just a few dims can cancel similarity out."

In high dimensions:
- **Sparse distribution:** Most of space is empty; points cluster in a few regions
- **Grid partitioning fails:** Uniform grid cells are either empty (99%) or overloaded (millions of points)
- **Deceptive similarity:** Two vectors can look similar in a 3D projection but be far apart in 768D

**Conclusion:** ANN algorithms must be sensitive to the data distribution — they adapt to where points actually cluster.

## ANN Algorithms

### Method 1: Clustering (k-means)

```
1. Partition vectors into k clusters via k-means
2. At query time: route to nearest cluster centroid
3. Brute-force search within that cluster
```

**Pros:** Simple, fast routing
**Cons:** Points near cluster boundaries may be missed; cluster size imbalance

### Method 2: Graph-based (HNSW)

**HNSW (Hierarchical Navigable Small World)** is the dominant graph-based approach:

```
Layer 2 (sparse):  ●──────●         ← "superhighway" — long jumps
                    │
Layer 1 (medium):  ●──●──●──●      ← medium-range connections
                    │  │
Layer 0 (dense):   ●─●─●─●─●─●    ← local neighborhood
```

**Construction:**
1. Connect each point to its nearest neighbors → build a "map" of the space
2. Build multiple layers: upper layers have fewer nodes and longer edges ("skip-graph superhighway")
3. Nodes in higher layers are randomly selected with exponentially decreasing probability

**Search:**
1. Start at the top layer entry point
2. Greedily traverse toward the query through long edges
3. At each layer, descend to the next finer-grained layer
4. At layer 0, perform local neighborhood search

**Properties:**
- **Logarithmic search time:** O(log N)
- **Memory overhead:** Each node stores M neighbors (typical M=16–64)
- **No training:** Built incrementally as vectors are inserted
- **Used in:** Weaviate, Qdrant, pgvector, Elasticsearch, Lucene

### Method 3: Clusters + Graphs (ScANN, DiskANN)

```
1. Partition into clusters (k-means or similar)
2. Build a local graph within each cluster
3. At query time: route to best cluster → graph-traverse within
```

**ScANN (Google):** Vector quantization + anisotropic scoring; tuned for maximum inner product search.
**DiskANN (Microsoft):** SSD-resident graph; graph stored on disk with RAM-cached hot nodes.

**Use case:** Billion-scale search where clusters map to different memory/nodes/servers.

## Filtered Similarity

Real queries combine vector similarity with structured metadata:

```json
{
  "query": "How much did we invest in XYZ?",
  "company": "XYZ",
  "year": 2021
}
```

### Three Approaches

| Approach | How it works | Problem |
|----------|-------------|---------|
| **Pre-filtering** | Apply metadata filter → vector search on remaining | May miss results outside filter range |
| **Post-filtering** | Vector search → apply filter to results | May return fewer than k results |
| **Native filtering** | Integrate filter into ANN traversal | Requires index-level support |

### Native Filtering (turbopuffer / ACORN1)

**turbopuffer approach:** Track which attribute values map to which vector clusters. When filtering, skip clusters that can't satisfy the filter.

**ACORN1 (Elastic/Weaviate):** During HNSW graph traversal, keep scanning neighbors-of-neighbors that satisfy the filter. Continues expanding the frontier until enough filtered matches are found.

```python
# ACORN1 pseudocode
for neighbor in current_node.neighbors:
    if neighbor satisfies filter:
        for neighbor_of_neighbor in neighbor.neighbors:
            if neighbor_of_neighbor satisfies filter:
                add to frontier + nearest_neighbors heap
```

### Key Questions for Vector DB Evaluation

1. **How does filtering work?** Pre-, post-, or native?
2. **What kinds of filters?** Metadata only? Full-text matches? Range queries?
3. **Performance under filter selectivity?** 1% filter vs 50% filter — very different behaviors

## Hybrid Search: BM25 + Vector

**Anti-pattern:** Magically interleaving BM25 and vector results (e.g., Reciprocal Rank Fusion / RRF).

**Correct approach:** Multiple retrieval arms, each with its own strategy, combined by the application logic (or an LLM agent):

```json
{
  "queries": [
    {
      "rank_by": ["bm25_title", "bm25_content"],
      "top_k": 100
    },
    {
      "rank_by": ["vector", "ANN", query_embedding],
      "top_k": 100
    }
  ]
}
```

> "Split by strategy, not by index type. Usually not just hybrid OR vector — but both."

### LLM as Orchestrator

```
Agent receives query
  → Decides: which retrieval arms to use?
    → Arm 1: BM25 for exact product name matching
    → Arm 2: Vector search for semantic category discovery
    → Arm 3: Filtered vector search for news by topic+date
  → Combines results with reasoning (not mechanical fusion)
```

## Pitfalls of Vector Search

### Embedding Collapse / Hubness

A global embedding model (trained on Wikipedia + Common Crawl) applied to a narrow domain → all corpus vectors cluster in a tiny region. Cosine similarities are all 0.85–0.95, making discrimination impossible.

**Solutions:** Domain-specific fine-tuning, dimensionality reduction, hubness-aware scoring.

### Embedding Compression

Dense embeddings (384–1536D) are a **lossy compression** of sparse bag-of-words (1B+ dimensions). Information is lost; two semantically different passages can map to nearby vectors by accident.

### Similarity ≠ Relevance

Vector similarity is ONE signal. Real ranking functions are far richer:

```
f(Q, D) = α · embed(Q, D.title) × β · recency(D.date) × γ · popularity(D)
```

Lean on similarity alone and you'll return relevant-looking but stale, unpopular, or factually wrong results.

### Training Data & ML Maintenance

Fine-tuned embeddings require:
- High-quality (query, relevant, irrelevant) triples
- ML expertise to maintain the model
- Continuous retraining as data drifts

Assume you have this data and it's good? Assume you have the skill to maintain the model?

## Vector Search in the Agent Era

> "Agents turn simple keyword search into compelling search experiences. But embeddings fail at match criteria — they have no 'why'." — Doug Turnbull

With AI agents, vector search is a **tool**, not the whole system:

1. **Agent calls vector search** for broad semantic recall
2. **Agent calls [[bm25|BM25]]** for precise term matching
3. **Agent reasons about results** — combines, verifies, filters, reranks
4. **Agent adapts strategy per query** — product name → BM25, news topic → vector+recency

## Related Pages

- [[entities/embeddings]] — How embeddings are created and trained
- [[concepts/bm25]] — Lexical scoring as complement to vector search
- [[concepts/lexical-search]] — Token-based matching fundamentals
- [[concepts/agentic-search]] — Agent-driven multi-arm retrieval
- [[entities/turbopuffer]] — Native filtered vector search
- [[entities/doug-turnbull]] — Search relevance + agentic search
