---
title: Embeddings
created: 2026-05-13
updated: 2026-05-13
type: concept
tags:
  - model
  - search
  - training
  - transformers
sources: [raw/articles/2026-05-13_softwaredoug_vector-search-embeddings.md]
---

# Embeddings

Embeddings are dense vector representations that encode entities (words, sentences, users, products, images) as coordinates in a high-dimensional space. The fundamental property: **similar things are close together, dissimilar things are far apart.**

> "Assign coordinates to all the things." — Doug Turnbull

## Intuition

Each entity gets a fixed-length vector (typically 384–1536 dimensions). The distance or angle between vectors encodes semantic similarity:

```
Doug:       [0.3,  0.5,  0.2]   ← sci-fi fan
Star Trek:  [0.4,  0.6,  0.3]   ← close to Doug
Star Wars:  [-0.4, 0.2,  0.1]   ← moderate distance
S&S:        [-0.5, -0.2, 0.0]   ← far from Doug
```

In 3D this is easy to visualize. In 768D, the same principle holds — but the geometry is far richer and more expressive.

## Training Embeddings: Triples + Deep Learning

### The Triple Format

Training data consists of (Anchor, Similar, Dissimilar) triples:

| Anchor | Similar | Dissimilar |
|--------|---------|------------|
| Doug | Star Trek | Sense & Sensibility |
| Doug | Naked Gun | Forrest Gump |

The objective: move the anchor embedding closer to "similar" and farther from "dissimilar."

### Training Loop

1. **Initialize:** Create an embedding for each entity (random values)
2. **Compare:** Compute dot product between anchor and similar/dissimilar embeddings
3. **Tweak:** If not similar enough, adjust embeddings to reduce loss

### Similarity as a Classification Task

```
emb(user) · emb(movie) → Dot Product → Sigmoid → Probability(0..1)
```

**Sigmoid** compresses the dot product (-1..1) into a 0–1 probability: similar=1, dissimilar=0.

### Contrastive Loss

```
Positive pair (should be similar):
  dot=1.0 → sigmoid=0.26 → log(0.26) = -0.58

Negative pair (should be dissimilar):
  dot=-1.0 → sigmoid=0.76 → log(0.76) = -0.11

L = -[log(sigmoid(positive_dot)) + Σ log(1 - sigmoid(negative_dot))]
```

Loss goes **DOWN** when positive dot products are high, and **UP** when negative dot products are high. A batch of negative samples provides contrastive signal.

### Backpropagation

The derivative of the loss function with respect to each dimension tells us which direction to push each value. Weights are updated to minimize loss:

```
dL/dv[0] → tweak weight[0] up or down
```

In deeper networks, error propagates back through all layers to learn weights at every level.

## Two-Tower Architecture

For **cold-start problems** (new users/items not in the training vocabulary), we can't wait for interaction data. Instead, we learn embeddings from attributes.

### Architecture

```
User Tower:                    Movie Tower:
  Age embedding ─┐               Year embedding ─┐
  Fav movie emb ─┤               Director emb ───┤
  Last watched ──┼→ Concat →     Star emb ───────┼→ Concat →
  ...            │  600-dim       ...             │  600-dim
                 ↓                                ↓
            600×384 Matrix                    600×384 Matrix
                 ↓                                ↓
            384-dim user emb                 384-dim movie emb
                 └──── Dot Product ────────────────┘
```

### Key Properties

1. **Attribute-based:** Each attribute (age, director, genre) gets its own learnable embedding
2. **Shared embeddings:** "45 year olds" embedding is shared across all 45-year-old users
3. **End-to-end training:** Backpropagation flows ALL the way back through both towers to attribute embeddings
4. **Generalization:** Once trained, ANY new user or item can be encoded from its attributes alone

This architecture powers virtually every modern recommendation system (YouTube, Netflix, TikTok).

## Transformers for Text Embeddings

For sentences and documents, transformer models (BERT-family) generate embeddings via the **[CLS] token**:

```
"What is the best recipe for creamed spinach?" → BERT → CLS → [0.02, 0.03, ..., -0.01]
```

Each token produces a contextualized state vector. The CLS token's final state serves as the **passage-level embedding**.

### Q&A Retrieval Pattern

1. Encode question → question embedding
2. Encode all answer chunks → chunk embeddings
3. Rank by cosine similarity
4. Return top-k most similar chunks

This is the foundation of Dense Passage Retrieval (DPR) and the classic RAG pipeline. At scale (millions/billions of chunks), efficient nearest-neighbor search is needed (see [[concepts/vector-search]]).

## Normalization & Cosine Similarity

Before comparison, embeddings are L2-normalized to the unit sphere:

```
Raw:   [0.45, -0.31, 0.33]
Norm:  sqrt(0.45² + 0.31² + 0.33²) = 0.638
Unit:  [0.45/0.638, -0.31/0.638, 0.33/0.638] = [0.705, -0.486, 0.517]
```

After normalization, **cosine similarity = dot product**, ranging -1 (opposite) to 1 (identical direction).

## Embedding Quality: More Dimensions = Better Accuracy

Higher dimensions provide more capacity to encode nuance, at the cost of storage and compute:

| Dimensions | Use Case | Tradeoff |
|-----------|----------|----------|
| 128–256 | Lightweight, edge devices | Lower accuracy |
| 384 | Balanced (all-MiniLM-L6-v2) | Good for most tasks |
| 768 | Standard (BERT-base) | Industry default |
| 1024–1536 | High quality (OpenAI, Cohere) | Higher cost |
| 3072–4096 | Maximum accuracy | Storage-heavy |

## Pitfalls

### Embedding Collapse (Hubness)
A global embedding model (trained on the entire web) applied to a tiny, specific domain → all corpus similarities collapse into a narrow range. Domain-specific fine-tuning is often required.

### Compression Loss
Dense embeddings (768D) are a **lossy compression** of sparse representations (1B+ dimensions). Information is inevitably lost — embeddings can't capture everything.

### Similarity ≠ Relevance
Vector similarity is ONE signal among many. Real search scoring functions combine:
```
f(Q, D) = α · embedding_sim(Q, D) + β · recency(D.date) + γ · popularity(D) + δ · BM25(Q, D.body)
```

### Training Data Quality
Embedding quality depends entirely on the quality of (similar, dissimilar) labels. Garbage labels → garbage embeddings. But do you have this data? And the ML skill to maintain the model?

## Embeddings in the Agent Era

With AI agents, embeddings serve as one tool among many:

- **Agent uses embedding search** for semantic discovery (broad recall)
- **Agent uses [[bm25|BM25]]/lexical search** for precision matching
- **Agent combines results** with reasoning, not mechanical fusion (RRF)

> "RAG isn't a vector search problem. Embeddings became the singular framework for RAG — it's the wrong lens." — Doug Turnbull

## Related Pages

- [[concepts/vector-search]] — How to efficiently find nearest neighbors at scale
- [[concepts/bm25]] — Lexical scoring as complement to embeddings
- [[concepts/lexical-search]] — Token-based matching fundamentals
- [[concepts/rag]] — Retrieval-Augmented Generation pipeline
- [[concepts/agentic-search]] — Agent-driven search paradigm
- [[entities/voyage-ai]] — Embedding model provider (acquired by MongoDB)
- [[entities/doug-turnbull]] — Search relevance engineering
