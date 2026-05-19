---
title: "Information Retrieval"
type: concept
aliases:
  - information-retrieval
  - ir
created: 2026-04-25
updated: 2026-05-19
tags:
  - information-retrieval
  - search
  - evaluation
  - embeddings
  - query-understanding
status: active
sources:
  - raw/articles/2025-03-27_daniel-tunkelang_precision-recall-desirability.md
  - raw/articles/2024-04-08_daniel-tunkelang_embedding-based-retrieval-rag.md
  - raw/articles/2026-04-20_daniel-tunkelang_distilling-retrieval-pipelines.md
  - raw/articles/2023-08-07_daniel-tunkelang_semantic-equivalence-ecommerce.md
  - raw/articles/2024-12-02_daniel-tunkelang_bag-of-documents.md
---

# Information Retrieval

Information Retrieval (IR) is the discipline of finding material (usually documents) that satisfies an information need from within large collections. At its core, IR negotiates the tension between **precision** ("nothing but the truth"), **recall** ("the whole truth"), and practical constraints like latency, cost, and user experience.

## Core Framework: Precision, Recall, and Desirability

Daniel Tunkelang's framework [[raw/articles/2025-03-27_daniel-tunkelang_precision-recall-desirability.md]] systematizes the three dimensions of search quality:

### Precision

> "Precision quantifies what most people mean by relevance: the fraction of search results that satisfy or directly relate to the searcher's intent."

- **Measurement:** Human judgments (binary/graded relevance, DCG), LLM-based judgments, unsupervised coherence proxies, model-based evaluation
- **Detection of low precision:** Low CTR, frequent query reformulation, dissimilar engagement patterns
- **Fixes:** Query triage, pseudo-relevance feedback (may reduce diversity), query categorization

### Recall

> "Recall measures the fraction of relevant documents retrieved."

- **Measurement:** Retrievability analysis (document-level, weighted by query frequency), sampling-based estimation across different precision-recall tradeoffs
- **Detection of low recall:** Retrievability gaps, low-specificity queries with sparse results, null result counts
- **Fixes:** Query expansion (synonyms, stemming — needs precision guardrail), query relaxation (optional terms — needs precision guardrail), whole-query expansion (embedding-based, avoids token-level context loss)

### Desirability

> "Query-independent factors, such as popularity, quality, or recency, often determine which relevant results to present to searchers on the first page and in what order."

- **Measurement:** Engagement probability conditioned on relevance, position-bias-adjusted clicks, content-based regression models
- **Key tension:** Desirability must not override relevance — "highly desirable but irrelevant results will not satisfy users"
- **Best practice:** Combine query-dependent relevance with query-independent desirability via machine-learned ranking (LTR) models like XGBoost

## Retrieval Paradigms

### Bag-of-Words (Lexical Search)

The traditional approach: represent documents and queries as sparse vectors with one dimension per term, weighted by **TF-IDF** or **BM25**. Similarity measured via cosine similarity.

**Limitations:** Cannot handle synonyms, polysemy, or multi-word phrases. "Word-based representations break down when multiple words convey the same meaning… Search needs something better than words as units of meaning." [[raw/articles/2024-04-08_daniel-tunkelang_embedding-based-retrieval-rag.md]]

See [[concepts/lexical-search]], [[concepts/bm25]].

### Embedding-Based (Semantic Search)

Documents and queries are encoded as **dense vectors** in a shared embedding space. Similarity is measured by cosine distance. Modern embeddings (BERT, MiniLM, etc.) leverage transformer models with attention mechanisms to capture meaning beyond token overlap.

**The alignment challenge:** Queries and documents differ in length, vocabulary, and style. Misalignment is "the root cause of poor embedding-based retrieval." Solutions:
- **Two-tower models:** train separate encoders for queries and documents
- **Hypothetical Document Embeddings (HyDE):** transform queries into pseudo-document vectors
- **Bag-of-documents model:** learn query vectors from result distributions (see below)

See [[concepts/embeddings]], [[concepts/vector-search]], [[concepts/hnsw]].

### Hybrid Retrieval

Combining lexical and semantic retrieval produces largely **disjoint result sets** — and you need both. In Tunkelang's bag-of-documents pipeline, over a third of final bag members came from keyword search alone, with minimal overlap between the two methods. [[raw/articles/2026-04-20_daniel-tunkelang_distilling-retrieval-pipelines.md]]

## Bag-of-Documents Model

Introduced by **Daniel Tunkelang and Aritra Mandal** at KDD 2023 and refined through 2026, the bag-of-documents model reframes query understanding as **predicting result distributions rather than encoding text directly**.

### Core Insight

A query like "wireless keyboard" is not fundamentally about the words — it corresponds to a set of relevant products. The model represents each query as a **bag of documents** with:
- **Centroid vector** — average embedding of all relevant document titles (canonical intent)
- **Specificity score** — mean cosine similarity between centroid and bag members (narrow vs. broad queries)

**Goal:** Learn to map query text directly to the bag's centroid, effectively distilling a multi-stage retrieval pipeline into a single embedding step.

### Pretrained Model (2026)

A pretrained version built entirely with public data on a 16GB MacBook Air M4:

| Metric | Base MiniLM | Fine-tuned | Improvement |
|--------|------------|------------|-------------|
| Cosine similarity to centroid | 0.787 | **0.914** | +0.127 |
| Recall@10 | 0.367 | **0.506** | +0.139 |
| Complement retrieval rate | 14.2% | **7.7%** | -6.5% |

**Resources (MIT-licensed):** [HuggingFace](https://huggingface.co/datasets/dtunkelang/bag-of-documents) · [Demo](https://huggingface.co/spaces/dtunkelang/bag-of-documents-demo) · [Code](https://github.com/dtunkelang/bag-of-documents) · [arXiv 2308.03869](https://arxiv.org/abs/2308.03869)

The model can be understood as a **learned, amortized form of pseudo-relevance feedback** — it uses retrieved documents during training but eliminates the feedback loop at inference time.

See [[entities/daniel-tunkelang]].

## Query Similarity and Semantic Equivalence

Measuring when two queries are semantically equivalent (despite different surface forms) is central to query rewriting, deduplication, and intent classification.

Tunkelang & Mandal's approach (KDD 2023): [[raw/articles/2023-08-07_daniel-tunkelang_semantic-equivalence-ecommerce.md]]
- Aggregates **historical searcher behavior** on frequent queries to define equivalence
- Trains a **sentence transformer** to generalize to unseen queries (zero-shot)
- **Practical, behavior-driven definition** — not relying solely on lexical overlap

See [[concepts/query-understanding]] — Tunkelang's full 24-article series systematizing query understanding from character-level to conversational search.

## Retrieval-Augmented Generation (RAG)

RAG extends embedding-based retrieval with two critical steps:

1. **Query rewriting** — transform natural language queries to better capture intent (akin to prompt engineering). May decompose into multiple sub-queries.
2. **Chunking** — split documents into coherent chunks for retrieval. "If the chunks are too granular or not granular enough, or if the chunks do not preserve key information from their document context, then it is unlikely that the resulting chunk vectors will align with those from queries."

Key challenge: the **relevance trap** — a chunk may have high cosine similarity yet be unhelpful in the generated context.

See [[concepts/rag]], [[concepts/embeddings]].

## Related

- [[entities/daniel-tunkelang]] — Search consultant, Endeca co-founder, bag-of-documents model creator
- [[concepts/query-understanding]] — 24-article series systematizing query understanding
- [[concepts/lexical-search]] — Bag-of-words, TF-IDF, BM25
- [[concepts/vector-search]] — ANN algorithms, HNSW, FAISS
- [[concepts/embeddings]] — Dense vector representations for semantic search
- [[concepts/bm25]] — The classic lexical retrieval baseline
- [[concepts/rag]] — Retrieval-Augmented Generation
- [[concepts/pseudo-relevance-feedback]] — Traditional query refinement via top-K results
- [[concepts/judgment-list]] — Search relevance evaluation methodology
