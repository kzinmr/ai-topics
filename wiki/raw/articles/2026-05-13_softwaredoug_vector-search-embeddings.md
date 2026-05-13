---
title: "Vector Search + Embedding Retrieval — Cheat at Search Essentials"
url: https://docs.google.com/presentation/d/15Ij9zL1gKo8QEEGtSsSSrVUNdJZay2ioejigxQ-z4wo/edit
source: softwaredoug.com
author: Doug Turnbull (@softwaredoug)
date_ingested: 2026-05-13
type: slide_deck
tags: [embeddings, vector-search, information-retrieval, hnsw, search]
---

# Vector Search + Embedding Retrieval — Cheat at Search Essentials

Doug Turnbull's Maven course "Cheat at Search Essentials" — Vector Search & Embeddings module (Day 3).
Discount code: `vectorsrock`.
Slides 1-8 are template; slides 9+ are the teaching content.

---

## Embeddings Primer

**Core concept:** Assign coordinates to all things — embed them in space. ML moves similar things closer together, dissimilar things farther apart.

Training data: triples of (Anchor, Similar, Dissimilar).
Example: (Doug, Star Trek, Sense & Sensibility) → ML moves Doug closer to Star Trek, farther from Sense & Sensibility.

## Embedding Table

Each entity gets a vector (e.g., 3D for illustration, 768D in practice):
```
Doug:         [0.3,  0.5,  0.2]
Star Trek:    [0.4,  0.6,  0.3]
Star Wars:    [-0.4, 0.2,  0.1]
S&S:          [-0.5, -0.2, 0.0]
```

## Cosine Similarity (Dot Product)

**Normalization:** Everything on a unit sphere — divide by L2 norm:
```
[0.45, -0.31, 0.33] / 0.638 = [0.705, -0.486, 0.517]
```

**Dot product range -1 to 1:** 1 = exactly same direction, -1 = opposite.

```
0.705 * (-0.128) + (-0.486) * 0.444 + 0.517 * 0.887 = 0.584
```

## Deep Learning for Embeddings

### Training Loop
1. Create embedding for each entity in vocabulary (init to random)
2. Compare similarity to ground truth
3. If not similar enough, tweak to be closer/farther

### Sigmoid + Contrastive Loss

Dot product (-1..1) → Sigmoid → (0..1 probability)
```
Positive (should be similar): 1/(1+e^1) = 0.26,  log(0.26) = -0.58
Negative (should be dissimilar): 1/(1+e^-1) = 0.76, log(0.76) = -0.11
```

Loss function goes DOWN when dot products are similar, UP when dissimilar.
**Contrastive loss:** Sampled batch of negative dot products added to loss.

### Backpropagation

Compute derivative of loss w.r.t. each dimension, tweak weights to minimize loss.
More complex/deep neural nets propagate error back to earlier layers.

## Cold Start: What About New Users/Items?

**Option 1:** Wait for new user to interact + retrain (slow)
**Option 2:** Learn embeddings from attributes (Two-Tower Architecture)

## Two-Tower Architecture

User attributes (age, favorite movie, last watched) → **User Encoder** → 384-dim embedding
Movie attributes (year, director, star) → **Movie Encoder** → 384-dim embedding

Process:
1. Concatenate attribute embeddings → 600 dims
2. Transform via 600×384 weight matrix → 384 dims
3. Dot product between user and movie embeddings
4. Backpropagate ALL the way back through encoders

**Key insight:** Now we can encode ANYTHING — users, queries, images all get embeddings from their attributes.

## Transformers for Sentence Embeddings

BERT-style: process sentence word-by-word, CLS token becomes passage embedding.

```
"What is the best recipe for creamed spinach?" → CLS → [0.02, 0.03, ..., -0.01]
```

**Q&A Retrieval:** Encode question + answer chunks → rank by cosine similarity. Used at millions/billions scale.

## Vector Search: Finding Nearest Neighbors

Core problem: given a query vector, find closest points in high-dimensional space.

### Curse of Dimensionality
- In 3D, points can look similar
- In high dimensions, a few dims can cancel similarity out
- Grid/partitioning methods fail: clusters become empty or overloaded

### Method 1: Clustering (k-means)
Build data-sensitive clusters → route to nearest cluster → search within

### Method 2: Graph-based (HNSW)
Connect each point to neighbors → create a "map" of the space.
**HNSW (Hierarchical Navigable Small World):** Skip-graph superhighway — graph "above" the graph to skip around faster.

### Method 3: Clusters + Graphs (ScANN, DiskANN)
Route to a cluster, then use that cluster's graph. Useful at scale for routing to specific memory/node.

## Filtered Similarity

**Problem:** Queries have structured filters (company=X, year=2021). How to combine vector similarity with metadata filtering?

**Approaches:**
- **Pre-filtering:** Filter first, then vector search (may miss results)
- **Post-filtering:** Vector search first, then filter (may return too few)
- **Native filtering (turbopuffer):** Track which attributes go with which vector clusters
- **ACORN1 (Elastic/Weaviate):** Keep scanning neighbors of neighbors that satisfy filter

**Key question:** How does filtering work in YOUR VectorDB? What kinds of filters?

## Embedding Pitfalls

### Hubness / Embedding Collapse
Global model (trained on entire world) applied to tiny, specific domain → all corpus similarities collapse into a tiny region.

### Embedding Compression
Dense (768D) is a compressed view of Sparse (1B+ D). Compression is lossy.

### Similarity ≠ Relevance
Scoring function must go beyond embedding similarity:
```
f(Q, D) = embedding(Q, D.Title) × Recency(D.Date) × Popularity...
f(Q, D) = if(all_terms_match(Q, D)) then embedding(Q, D.Title) else 0
```

Real search combines multiple signals, not just vector similarity.

## Hybrid Search Strategy

**NOT this:** Magically interleave BM25 + Vector results (RRF)
**INSTEAD:** One system with vector + lexical, split by strategy, not by index type.

Use multiple retrieval arms:
```json
{
  "queries": [
    { "rank_by": [bm25_title, bm25_content], "top_k": 100 },
    { "rank_by": ["vector", "ANN", query_embedding], "top_k": 100 }
  ]
}
```

**LLM as orchestrator:** Tools/arms → hybrid strategy → composite results.

> "Usually not just hybrid OR vector but both. Split by strategy, not by index type."

## Course Links

- http://maven.com/softwaredoug/
- http://maven.com/softwaredoug/cheat-at-search?promoCode=vectorsrock ($200 off)
- Colab ACORN1: https://colab.research.google.com/drive/1H9BRpnORLTygEGemq5sH2BocUDqSThek
