---
title: "Information Retrieval"
type: concept
aliases:
  - information-retrieval
  - ir
created: 2026-04-25
updated: 2026-05-19
tags:
  - search
  - evaluation
  - model
  - query-understanding
  - query-expansion
  - lexical-search
  - agentic-retrieval
status: active
sources:
  - raw/articles/2025-03-27_daniel-tunkelang_precision-recall-desirability.md
  - raw/articles/2024-04-08_daniel-tunkelang_embedding-based-retrieval-rag.md
  - raw/articles/2026-04-20_daniel-tunkelang_distilling-retrieval-pipelines.md
  - raw/articles/2023-08-07_daniel-tunkelang_semantic-equivalence-ecommerce.md
  - raw/articles/2024-12-02_daniel-tunkelang_bag-of-documents.md
  - raw/articles/2026-05-19_daniel-tunkelang_bag-of-documents-slides.md
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

### Loss Functions

The choice of loss function is critical to BoD training. Tunkelang's May 2026 lecture [[raw/articles/2026-05-19_daniel-tunkelang_bag-of-documents-slides.md]] compares two approaches:

| Loss | Approach | Characteristics |
|------|----------|----------------|
| **Centroid Loss** | Minimizes cosine distance between query embedding and its bag centroid | Direct, simple, good baseline |
| **MultipleNegativesRankingLoss (MNRL)** | Contrastive: treats the query's bag as positive, other queries' bags as negatives | Better retrieval performance in practice |

### Sources for Relevance Judgments

> **"Judgments are the foundation, so invest effort here!"**

| Source | Type | Notes |
|--------|------|-------|
| **Implicit** | Engagement (clicks, add-to-carts, purchases) | Conflates desirability with relevance. **Ranking ≠ Relevance!** |
| **Explicit** | Human raters (traditional qrels) | Topical relevance gold standard, but expensive |
| **Automated** | LLMs, cross-encoders | Vary widely in quality and cost; useful for scale |

### BoD for Reranking

BoD isn't only for direct retrieval. A powerful hybrid pattern:

1. Retrieve candidates using lexical (BM25) or dense retrieval
2. Score each candidate with a **BoD-trained encoder**
3. **BM25 + BoD Reranker** can outperform pure BoD-based retrieval

### Caveats: When BoD Works (and When It Doesn't)

From Tunkelang's lecture slides [[raw/articles/2026-05-19_daniel-tunkelang_bag-of-documents-slides.md]], the approach requires:

1. **Cluster hypothesis** — documents relevant to the same query must form tight clusters under the base encoder
2. **Encoder quality** — base encoder must produce meaningful document vectors
3. **Sufficient relevance data** — enough judgments per query to form reliable bags
4. **Query coverage** — training queries must cover vocabulary/patterns of unseen queries
5. **Bag quality** — relevance judgments must be accurate; garbage in, garbage out
6. **No concept drift** — query intent distribution should be stable between training and serving
7. **Computational budget** — fine-tuning and bag construction require non-trivial compute (though demonstrated on a laptop)

### Resources

- [Best Buy BoD demo](https://huggingface.co/spaces/dtunkelang/bag-of-documents-bestbuy-demo) — Additional live demo (May 2026)
- [SpeakerDeck slides](https://speakerdeck.com/dtunkelang/the-bag-of-documents-model-for-query-understanding-and-retrieval) — Guest lecture for Turnbull & Grainger's AI search class

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

## SIRA: LLM-Guided Lexical Retrieval

**SIRA** (Superintelligent Retrieval Agent) from Meta Superintelligence Labs (May 2026) introduces a new paradigm: using LLMs to bridge the vocabulary gap between queries and documents, enabling a single BM25 call to outperform both dense retrievers and multi-round agentic search. See [[entities/sira]].

### The Vocabulary Gap Problem

Users and documents speak different languages. A user might query "how to prevent AI from being jailbroken" while the relevant paper uses "adversarial robustness of alignment techniques." Dense retrieval bridges this via embedding similarity; agentic search bridges it by iteratively reading results and reformulating. SIRA bridges it **before retrieval** by enriching both sides with missing vocabulary.

### Corpus-Side Enrichment (Offline)

An LLM reads each document and proposes missing search vocabulary — synonyms, abbreviations, alternate phrasings a user might search with. A **Document-Frequency (DF) filter** prunes terms that are too common (DF > threshold) to be discriminative. Surviving terms are injected as n-grams into the BM25 index.

### Query-Side Expansion (Online)

The LLM generates an **expected-response sketch** — concepts, entities, and discriminative terms likely to appear in a relevant answer but absent from the query. Crucially, the LLM is forbidden from guessing the answer itself (to avoid bias). The DF filter validates each proposed term: if it doesn't exist in the corpus (DF=0) or is too common, it's discarded. The validated expansion is combined with the original query into a single weighted BM25 call:

```text
score(d) = BM25(q_orig, d) + w · BM25(q_exp, d)
```

### Why It Works

- **BM25 is transparent**: IDF naturally weights rare discriminative terms — the LLM just needs to surface the right ones
- **DF filter is the gatekeeper**: It prevents the LLM from injecting hallucinated or non-discriminative terms
- **One shot > multi-round**: Eliminates the context accumulation problem ("lost in the middle") and the latency of iterative search
- **No training**: Works with frozen LLMs, no supervised pairs, no relevance labels

### Comparison with Other Approaches

| Approach | LLM Usage | Retrieval | Rounds | Training |
|----------|-----------|-----------|--------|----------|
| BM25 baseline | None | Lexical | 1 | None |
| Dense (E5, BGE) | None | Embedding | 1 | Supervised |
| HyDE | Generate pseudo-doc | Embedding | 1 | None |
| Agentic (IRCoT, Search-R1) | Reasoning loop | Multi-round | 3-10+ | Prompt eng. |
| **SIRA** | Enrich both sides | Weighted BM25 | **1** | **None** |
| BoD (Tunkelang) | None (learned) | Embedding | 1 | Fine-tuned |

SIRA achieves SoTA on 10 BEIR benchmarks, outperforming all baselines including E5-supervised and multi-round agentic search.

### Limitations

- Requires LLM to read every document for corpus enrichment (offline, one-time cost)
- Benefits diminish when vocabulary gap is already small
- DF threshold τ may need corpus-specific tuning
- Dependent on LLM quality for enrichment

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
