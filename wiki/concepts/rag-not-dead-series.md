---
title: "RAG Is Not Dead — 7-Part Series"
type: concept
created: 2026-04-30
updated: 2026-04-30
tags:
  - concept
  - rag
  - retrieval
  - evaluation
  - series
aliases:
  - rag-not-dead-series
  - stop-saying-rag-is-dead
  - hamel-rag-series
sources:
  - path: raw/articles/2026-04-30_hamel-husain-rag-not-dead.md
  - https://hamel.dev/notes/llm/rag/not_dead.html
  - https://hamel.dev/notes/llm/rag/p2-evals.html
  - https://hamel.dev/notes/llm/rag/p3_reasoning.html
status: active
---

# RAG Is Not Dead — 7-Part Series

A 2025-2026 open series by [[entities/hamel-husain|Hamel Husain]] and [[entities/benjamin-clavie|Ben Clavié]] arguing that RAG (Retrieval-Augmented Generation) is not dead — rather, the naive single-vector implementation from 2023 is what deserves criticism. The future of RAG lies in **better retrieval, not bigger context windows**.

> *"Claiming RAG is dead because we're now using better retrieval tools is... akin to claiming HTML is dead because we are now using CSS."* — Benjamin Clavié

## Core Thesis

The 2023 version of RAG (chunk → vector DB → cosine similarity → LLM) fails because compressing entire documents into single vectors loses critical information. But retrieval itself is more important than ever:

- LLMs are **frozen at training time** — they can't learn new information without retrieval
- Million-token context windows don't change the **economics** of stuffing everything into every query
- **Retrieval handles knowledge storage**; model weights focus on intelligence

## The 7 Parts

| Part | Title | Expert | Key Concept |
|------|-------|--------|-------------|
| 1 | [[concepts/modern-retrieval-toolkit\|I don't use RAG, I just retrieve documents]] | Ben Clavié | Why naive single-vector search is dead; the modern retrieval toolkit (BM25, ColBERT, agentic search) |
| 2 | [[concepts/freshstack-benchmark\|Modern IR Evals For RAG]] | Nandan Thakur | FreshStack: multi-dimensional eval (Coverage, Diversity, Relevance) replacing contaminated BEIR/MTEB |
| 3 | [[concepts/reasoning-retrieval\|Optimizing Retrieval with Reasoning Models]] | Orion Weller | Promptriever (instruction-aware bi-encoder) + Rank1 (reasoning-based reranker with CoT) |
| 4 | [[concepts/late-interaction-retrieval|Late Interaction Models For RAG]] | Antoine Chaffin | ColBERT-style MaxSim preserving token-level detail; 150M model outperforming 7B dense models on reasoning |
| 5 | [[concepts/multiple-representations-rag|RAG with Multiple Representations]] | Bryan Bischof & Ayush Chaurasia | "The Map is Not the Territory" — create multiple specialized maps instead of one perfect embedding |
| 6 | Context Rot | Kelly Hong | LLM performance degrades with longer inputs; context engineering is critical |
| 7 | [[concepts/graph-db-overengineering-rag\|You Don't Need a Graph DB (Probably)]] | Jo Kristian Bergum | GraphRAG is a technique, not a technology; HNSW as hidden graph |

## Key Insights Across the Series

| Insight | Description | Part |
|---------|-------------|------|
| **Single-vector compression is the root problem** | One vector per document loses nuance; late-interaction and multi-vector models preserve it | 1, 4 |
| **IR metrics misalign with RAG needs** | BEIR/MTEB measure top-1; RAG needs coverage, diversity, and corroboration | 2 |
| **Retrievers can reason** | Instruction-following retrievers (Promptriever) + reasoning-based rerankers (Rank1 with CoT) beat keyword matching | 3 |
| **Multiple representations > one perfect embedding** | Route between specialized indices instead of searching for the universal encoder | 5 |
| **Context Rot is real** | LLMs degrade with irrelevant distractors in long contexts, even on simple tasks | 6 |
| **Don't over-engineer** | Graph DBs are almost never needed; HNSW already provides graph structure | 7 |

## Part Details

### Part 2: FreshStack (Nandan Thakur)

Traditional IR metrics (MRR, NDCG) were designed for search engines ranking a single best result. RAG needs a **comprehensive evidence set**. BEIR benchmarks suffer from data contamination, leaderboard saturation (400+ models), and static/too-clean datasets.

**FreshStack** (Databricks collaboration) evaluates retrieval for technical RAG using real-time Stack Overflow data with a nuggetization pipeline (GPT-4o breaks answers into atomic facts → oracle retrieval from GitHub → support check).

**Three key metrics:**
- **Grounding (Coverage@20)** — % of unique nuggets found (completeness)
- **Diversity (alpha-nDCG@10)** — Penalizes redundant fact repetition (efficiency)
- **Relevance (Recall@50)** — Baseline on-topic check

**Surprising finding:** BM25 sometimes outperforms proprietary embedding models on technical documentation. Performance does not always scale with model size.

### Part 3: Reasoning Retrieval (Orion Weller)

RAG retrieval is stuck in a 1999 keyword-matching paradigm. Two models introduced:

**Promptriever** — Instruction-aware bi-encoder trained on "instruction negatives" (documents relevant to query but NOT its specific instruction). Enables zero-shot hyperparameter tuning via natural language.

**Rank1** — Cross-encoder using Test-Time Compute (Chain-of-Thought) to judge relevance. Trained via SFT on reasoning chains from DeepSeek R1 (no RL needed). A 7B model nearly doubled BRIGHT benchmark performance. Key finding: reasoning traces provided a **10-point gain** over training on the same data without reasoning.

**"Invisible documents":** Rank1 finds relevant documents human annotators missed in old benchmarks (DL19/DL20). After re-judging, Rank1 became top performer — revealing a "long tail" of previously invisible relevant content.

### Part 4: Late-Interaction Retrieval (Antoine Chaffin)

Dense vector search compresses all tokens into a single vector — inherently lossy. Late-interaction models (ColBERT) replace this pooling step with the **MaxSim operator**: for each query token, find its maximum similarity across all document tokens, then sum. This preserves all token-level detail and makes retrieval interpretable.

**Key results:**
- On BRIGHT benchmark: a **150M parameter** late-interaction model outperformed **7B parameter** dense models
- Fine-tuned late-interaction: **19.61 nDCG** vs 12.31 for dense on BRIGHT
- Better out-of-domain generalization and fine-tuning stability

**Tooling:** PyLate (open-source by Chaffin) makes late-interaction as easy as Sentence Transformers.

**Adoption barriers now resolved:** Quantization for storage, Vespa/Weaviate/LanceDB for VectorDB support, PyLate for tooling.

### Part 5: Multiple Representations (Bryan Bischof & Ayush Chaurasia)

**Core thesis ("The Map is Not the Territory"):** Any data representation is a *map* distinct from the real data (*territory*). Engineers can — and should — create **multiple specialized maps** of the same data instead of searching for one perfect universal embedding.

**Bryan Bischof's unique framework:**
- **"Curving Space"** — intentionally shaping indices to bring relevant items closer. Index engineering as active spatial design, not passive embedding.
- **Deconstructing buzzwords** — Agentic RAG = query enrichment pipeline, HyDE = document enrichment pipeline, Rank Fusion = multi-stage processing. Strip marketing, see actual pipeline transformations.
- **Bicycle analogy** — don't try to fix one all-terrain bike (embedding). Build specialized bikes for different terrains and route to the right one.

**Three responsibilities of an IR engineer:** Predicting user intent → generating multiple representations (summaries, entity lists, tables) → matching intent to representation.

**Demo (Semantic Dot Art):** Art indexed via 4 maps (literal, poetic, mood, image). Poetic query → poetic index; image → multimodal embeddings.

## Graph Structure Query

```
[rag-not-dead-series] ──author──→ [hamel-husain]
[rag-not-dead-series] ──coauthor──→ [benjamin-clavie]
[rag-not-dead-series] ──includes──→ [modern-retrieval-toolkit]
[rag-not-dead-series] ──includes──→ [freshstack-benchmark]
[rag-not-dead-series] ──includes──→ [reasoning-retrieval]
[rag-not-dead-series] ──includes──→ [late-interaction-retrieval]
[rag-not-dead-series] ──includes──→ [multiple-representations-rag]
[rag-not-dead-series] ──includes──→ [graph-db-overengineering-rag]
[rag-not-dead-series] ──contrasts──→ [naive-single-vector-rag]
[rag-not-dead-series] ──embodies──→ [harness-engineering]
```

## Related Concepts

- [[concepts/modern-retrieval-toolkit]] — Part 1: modern retrieval pipeline replacing naive RAG
- [[concepts/freshstack-benchmark]] — Part 2: multi-dimensional RAG evaluation
- [[concepts/reasoning-retrieval]] — Part 3: instruction-aware + reasoning-based retrieval
- [[concepts/late-interaction-retrieval]] — Part 4: ColBERT/MaxSim preserving token-level detail; 150M model beats 7B dense
- [[concepts/multiple-representations-rag]] — Part 5: "The Map is Not the Territory" — create multiple specialized maps instead of one universal embedding
- [[concepts/graph-db-overengineering-rag]] — Part 7: GraphRAG as technique, not technology
- [[concepts/harness-engineering]] — Measure-first philosophy across the series
- [[concepts/ai-evals]] — Evaluation methodology for AI systems
- [[concepts/agentic-rag]] — Broader taxonomy of agentic retrieval
- [[concepts/context-graph]] — Context engineering and "context rot"

## Sources

- [Stop Saying RAG Is Dead — Hamel's Blog](https://hamel.dev/notes/llm/rag/not_dead.html)
- [P2: Modern IR Evals For RAG](https://hamel.dev/notes/llm/rag/p2-evals.html)
- [P3: Optimizing Retrieval with Reasoning Models](https://hamel.dev/notes/llm/rag/p3_reasoning.html)
- [Raw article: P2](raw/articles/2026-04-30_hamel-husain-rag-p2-evals.md)
- [Raw article: P3](raw/articles/2026-04-30_hamel-husain-rag-p3-reasoning.md)
- [P4: Late Interaction Models For RAG](https://hamel.dev/notes/llm/rag/p4_late_interaction.html)
- [Raw article: P4](raw/articles/2026-04-30_hamel-husain-rag-p4-late-interaction.md)
- [P5: RAG with Multiple Representations](https://hamel.dev/notes/llm/rag/p5_map.html)
- [Raw article: P5](raw/articles/2026-04-30_hamel-husain-rag-p5-map.md)
