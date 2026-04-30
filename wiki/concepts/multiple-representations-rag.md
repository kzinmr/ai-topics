---
title: "Multiple Representations RAG"
type: concept
created: 2026-04-30
updated: 2026-04-30
tags:
  - concept
  - rag
  - retrieval
  - information-retrieval
  - architecture
aliases:
  - multiple-representations-rag
  - map-is-not-the-territory
  - curving-space
  - p5-multiple-representations
sources:
  - https://hamel.dev/notes/llm/rag/p5_map.html
  - path: raw/articles/2026-04-30_hamel-husain-rag-p5-map.md
status: active
---

# Multiple Representations RAG

The philosophy that effective retrieval is not about finding **one perfect embedding**, but about creating **multiple specialized maps** of the same data, each optimized for different user intents. Presented by **Bryan Bischof** and **Ayush Chaurasia** in **Part 5** of the [[concepts/rag-not-dead-series|RAG Is Not Dead series]].

## Bryan Bischof's Unique Framework

Bischof has a distinctive intellectual style — drawing from **philosophy, mathematics, and first-principles engineering** to reframe RAG problems:

### 🗺️ "The Map is Not the Territory"

The central metaphor, borrowed from **general semantics (Alfred Korzybski)**. Any data representation (embedding, vector index, BM25 inverted index) is a *map* — it is *not* the real data (*territory*). This recognition is liberating: you're free to create **as many maps as needed**, each optimized for a specific terrain (user intent).

> *"Models and embeddings are our maps, and we can create many different maps of the same territory to serve different purposes."*

**The trap:** Engineers try to "fix" a single embedding model when it fails on certain queries. The solution isn't a better universal embedding — it's more maps.

### 🌌 "Curving Space"

Bischof's term for **intentionally shaping indices** to bring relevant items closer together. It's a physics-of-search metaphor: instead of accepting the latent space as given, you *curve* it by:
- Creating auxiliary representations (summaries, entity lists, tables)
- Pre-computing different "views" of documents
- Routing queries to the curved space that best fits

This reframes index engineering from a passive concern ("just embed and search") to an **active spatial design problem**.

### 🔧 Deconstructing Buzzwords to Pipelines

Bischof strips RAG marketing jargon down to its **actual pipeline operations**:

| Buzzword | What It Actually Is |
|----------|-------------------|
| Agentic RAG | A **query enrichment pipeline** — LLM chooses *how* to search |
| Hybrid RAG | Vector search + keyword (BM25) — nothing more |
| Graph RAG | Relationship hierarchy used for retrieval improvement |
| Multi-Modal RAG | Multiple data types searched across modes |
| HyDE | A **document enrichment pipeline** — rewrite docs for searchability |
| Rank Fusion | **Multi-stage processing** combining results from different methods |

This deconstruction is characteristic of Bischof's **first-principles engineering philosophy**: don't buy into brand names, understand the actual transformation happening in the pipeline.

### 🚲 The Bicycle Analogy

> *"You need different bikes for different terrains."*

Don't try to build one "perfect" all-terrain bike (embedding). Build a road bike for paved queries and a mountain bike for complex ones, then route to the right bike.

## The Three Responsibilities of an IR Engineer

Bischof frames IR engineering not as tool selection but as **three distinct responsibilities**:

1. **Predicting User Intent** — What is the user actually trying to find? (Not just what they typed.)
2. **Generating Multiple Representations** — Create summaries, entity lists, tables, and other "maps" ahead of time.
3. **Matching Intent to Representation** — Route each query to the map best suited for that intent.

This is a **responsibility-driven design** — you define the *what* before choosing the *how*.

## Practical Implementation

**Document enrichment:** For a financial document corpus, create maps for summaries, data tables, named entities, and form types.

**Routing:** LLM tool-calling for few routes; fine-tuned classifier for many routes at scale.

**Dynamic updates:** Detect document changes and re-index affected parts — embeddings go "stale" over time.

**Demo (Semantic Dot Art):** Art indexed via 4 maps (literal, poetic, mood, image). A poetic query goes to the poetic index; an image uses multimodal embeddings.

## Relationship to Other Parts

| Paradigm | Relationship |
|----------|-------------|
| **Part 1 (Modern Toolkit)** | Multiple representations are a key part of the modern toolkit — BM25, ColBERT, and semantic are different maps |
| **Part 3 (Reasoning)** | Reasoning models act as **query enrichment** — adding context to vague queries before routing |
| **Part 4 (Late-Interaction)** | ColBERT creates diversity *within* a single model (token-level vectors = multiple modes in latent space) |
| **Part 6 (Context Rot)** | Better routing → fewer distractors → less context rot |

## Graph Structure Query

```
[multiple-representations-rag] ──author──→ [entity: Bryan Bischof]
[multiple-representations-rag] ──coauthor──→ [entity: Ayush Chaurasia]
[multiple-representations-rag] ──part-of──→ [rag-not-dead-series]
[multiple-representations-rag] ──inspired-by──→ ["The Map is Not the Territory" (Korzybski)]
[multiple-representations-rag] ──contrasts──→ [universal-embedding-search]
[multiple-representations-rag] ──relates-to──→ [modern-retrieval-toolkit]
[multiple-representations-rag] ──relates-to──→ [reasoning-retrieval]
```

## Related Concepts

- [[concepts/rag-not-dead-series]] — Part 5 of the series
- [[concepts/modern-retrieval-toolkit]] — Part 1: the modern toolkit; multiple maps complement the single-vector critique
- [[concepts/reasoning-retrieval]] — Part 3: reasoning models act as query enrichment for routing
- [[concepts/late-interaction-retrieval]] — Part 4: token-level vectors create internal diversity
- [[concepts/graph-db-overengineering-rag]] — Part 7: graph relationships as one type of map

## Sources

- [P5: RAG with Multiple Representations — Hamel's Blog](https://hamel.dev/notes/llm/rag/p5_map.html)
- [Raw article](raw/articles/2026-04-30_hamel-husain-rag-p5-map.md)
