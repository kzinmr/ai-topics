---
title: "Reasoning Retrieval"
type: concept
created: 2026-04-30
updated: 2026-04-30
tags:
  - concept
  - rag
  - reasoning
  - information-retrieval
aliases:
  - reasoning-retrieval
  - promptriever
  - rank1
  - p3-optimizing-retrieval-with-reasoning
sources:
  - path: raw/articles/2026-04-30_hamel-husain-rag-p3-reasoning.md
  - https://hamel.dev/notes/llm/rag/p3_reasoning.html
status: active
---

# Reasoning Retrieval

The paradigm of embedding instruction-following and reasoning capabilities directly into the retrieval process, moving beyond static keyword or vector matching. Introduced by **Orion Weller** (Johns Hopkins University) in **Part 3** of the [[concepts/rag-not-dead-series|RAG Is Not Dead series]].

## The Core Problem

RAG retrieval is stuck in a 1999 keyword-matching paradigm. LLMs are used only to rewrite queries or summarize results — the retrieval step itself is "instruction-blind."

## Two Complementary Models

### Promptriever: Instruction-Aware Bi-Encoder

A fast embedding model that follows instructions during the **initial retrieval** phase.

**Key innovation: Instruction Negatives** — Training examples where a document is relevant to a query but *not* its specific instruction (e.g., "find a document using a metaphor"). Forces the model to encode abstract instructions into the query embedding.

**Features:**
- Zero-shot hyperparameter tuning via natural language (e.g., "prioritize high recall")
- Low variance across paraphrased prompts compared to BM25 or RepLLaMA
- Documents pre-processed as standard embeddings; instructions appended at query time

### Rank1: Reasoning-Based Reranker

A cross-encoder using **Test-Time Compute** (Chain-of-Thought) to judge document relevance.

**Key features:**
- Verbalizes reasoning logic (e.g., "But wait, this mentions X but query requires Y") before scoring
- Trained via SFT on reasoning chains from DeepSeek R1 — no RL needed
- 7B model outperforming much larger baselines on 10x less data

**Performance:**
- BRIGHT benchmark: nearly doubled performance
- NevIR (Negation): more than doubled
- **10-point gain** from including reasoning traces vs training on same data without them

## The Retrieval Paradigm Spectrum

| Paradigm | Mechanism | Limitation |
|----------|-----------|------------|
| Keyword Search | Exact lexical matching | Fails on synonyms/semantics |
| Semantic Search | Vector/Embedding | Ignores stylistic/logical instructions |
| Instruction Search | Promptriever (Bi-Encoder) | Fast, lacks deep reasoning |
| Reasoning Search | Rank1 (Cross-Encoder) | Powerful, higher latency |

## "Invisible Documents" — The Long Tail

Rank1 scores poorly on old benchmarks (DL19/DL20) because it finds **relevant documents that human annotators missed** — older datasets were built using results from simpler retrievers (pre-BERT). After manual re-judging, Rank1 became top performer, revealing a "long tail" of previously invisible relevant content.

## Graph Structure Query

```
[reasoning-retrieval] ──author──→ [entity: Orion Weller]
[reasoning-retrieval] ──part-of──→ [rag-not-dead-series]
[reasoning-retrieval] ──includes──→ [Promptriever]
[reasoning-retrieval] ──includes──→ [Rank1]
[reasoning-retrieval] ──contrasts──→ [keyword-search]
[reasoning-retrieval] ──contrasts──→ [semantic-search]
[reasoning-retrieval] ──hosted-by──→ [hamel-husain]
```

## Related Concepts

- [[concepts/rag-not-dead-series]] — The 7-part series this is part of
- [[concepts/modern-retrieval-toolkit]] — Part 1: the broader modern retrieval toolkit that reasoning retrieval extends
- [[concepts/freshstack-benchmark]] — Part 2: evaluation dimension; reasoning retrievers need new eval approaches
- [[concepts/llm-as-judge]] — Parallel to Rank1's judge-like reasoning; both use LLMs for evaluation
- [[concepts/harness-engineering]] — Measure-first; reasoning traces make retrieval auditable

## Sources

- [P3: Optimizing Retrieval with Reasoning Models — Hamel's Blog](https://hamel.dev/notes/llm/rag/p3_reasoning.html)
- [Raw article](raw/articles/2026-04-30_hamel-husain-rag-p3-reasoning.md)
- [Promptriever paper (arXiv)](https://arxiv.org/abs/2409.11136)
- [Rank1 paper (arXiv)](https://arxiv.org/abs/2502.18418)
