---
title: "P5: RAG with Multiple Representations"
source: https://hamel.dev/notes/llm/rag/p5_map.html
author: Hamel Husain (featuring Bryan Bischof, Ayush Chaurasia)
date: 2025
type: article
---

# P5: RAG with Multiple Representations

**Presenters:** Bryan Bischof & Ayush Chaurasia
**Core Philosophy:** The Map is Not the Territory — create multiple specialized maps of the same data instead of searching for one perfect embedding.

## 1. Core Philosophy: "The Map is Not the Territory"

Data representation (the map) is distinct from real data (the territory). Create many maps of the same territory for different user intents.

> "Models and embeddings are our maps, and we can create many different maps of the same territory to serve different purposes."

## 2. Deconstructing RAG Buzzwords

| Buzzword | What It Actually Is |
|----------|-------------------|
| Agentic RAG | A query enrichment pipeline (LLM chooses *how* to search) |
| Hybrid RAG | Vector search + BM25 |
| Graph RAG | Using relationship hierarchies to improve retrieval |
| Multi-Modal RAG | Searching across multiple types or modes |
| HyDE | A document enrichment pipeline (rewrite docs for searchability) |
| Rank Fusion | Multi-stage processing combining results |

## 3. Three Responsibilities of an IR Engineer

1. **Predicting User Intent** — what is the user actually looking for?
2. **Generating Multiple Representations** — summaries, entity lists, tables, etc.
3. **Matching Intent to Representation** — route query to the right map

## 4. "Curving Space" — Shaping Indices

Bryan's term for engineering indices to improve search. Document enrichment creates multiple maps (summaries, tables, entities, form types). LLMs as routers vs fine-tuned classifiers for scale. Dynamic updates prevent stale embeddings.

## 5. Demo: Semantic Dot Art

Art indexed via 4 maps: literal descriptions, poetic descriptions, mood keywords, image content. Poetic query → poetic index. Image → multimodal embeddings.

## 6. Key Q&A

- "Fix one representation" fails → use specialized maps (bicycle analogy)
- Reasoning models = query enrichment; Late-interaction = diversity *within* the model
- Routing = classification (LLM for proof-of-concept, classifier for production)
