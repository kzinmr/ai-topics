---
title: SIRA (Superintelligent Retrieval Agent)
type: entity
created: 2026-05-29
updated: 2026-05-29
tags:
  - search
  - lexical-search
  - bm25
  - query-expansion
  - agentic-retrieval
  - methodology
  - lab
  - model
  - open-source
sources:
  - raw/papers/sira-2605.06647.md
  - https://github.com/facebookresearch/sira
related:
  - concepts/information-retrieval
  - concepts/query-understanding
  - concepts/bm25
  - concepts/lexical-search
  - concepts/rag
---

# SIRA (Superintelligent Retrieval Agent)

**SIRA** (Superintelligent Retrieval Agent) is a training-free information retrieval framework from **Meta Superintelligence Labs** that uses LLMs to bridge the vocabulary gap between queries and documents, enabling a single BM25 call to outperform dense retrievers and multi-round agentic search. Released May 2026 under the MIT license.

## Overview

SIRA defines **superintelligence in retrieval** as the ability to compress multi-round exploratory search into a **single, corpus-discriminative retrieval action**. Rather than iterating through search results like current agentic systems (ReAct, IRCoT, Search-R1), SIRA formulates an expert-level retrieval query *before* reading any passages.

The core insight: an LLM knows what relevant evidence should look like, but needs **index-visible statistics** to make that knowledge discriminative against an entire corpus. SIRA provides this by:
1. Enriching documents offline with missing search vocabulary (corpus-side)
2. Predicting evidence vocabulary for each query, validated by document-frequency statistics (query-side)
3. Executing a single weighted BM25 call with the validated expansion

## Authors

- **Zeyu Yang** (Meta Superintelligence Labs) — lead author, primary GitHub contributor
- **Qi Ma** (Meta)
- **Jason Chen** (Meta)
- **Anshumali Shrivastava** (Meta / Rice University)

## Repository

- **URL**: [facebookresearch/sira](https://github.com/facebookresearch/sira)
- **Language**: Rust (61.1%), Python (38.5%)
- **License**: MIT
- **Status**: Archived (May 2026)
- **Requirements**: Python ≥3.12, CUDA GPU (tested on H100), Rust toolchain

### Pipeline Stages
1. **Data preparation** — dataset loading and preprocessing
2. **BM25 indexing** — via custom `bm25x` Rust extension (forked from LightOn/bm25x, Apache 2.0)
3. **Corpus enrichment** — LLM generates indexing phrases for each document; DF filter prunes non-discriminative terms
4. **Query expansion** — LLM generates expected-response sketch; DF filter validates terms
5. **LLM-based pointwise reranking** — optional final scoring pass

### Usage
```bash
# Full pipeline on a single dataset
python scripts/run_pipeline.py data=scifact server.auto_start=true

# Multiple datasets
python scripts/run_pipeline.py datasets='[scifact,arguana,fiqa]' server.auto_start=true

# Specific stages only
python scripts/run_pipeline.py data=scifact stages='[enrich_query,rerank]'
```

## Architecture

```
┌──────────────────────────────────────────────────────────┐
│                     OFFLINE (once per corpus)             │
│                                                          │
│  Documents ──→ LLM reads each doc ──→ proposes missing   │
│               vocabulary (synonyms, abbreviations,       │
│               alternate phrasings)                       │
│                          │                               │
│                          ▼                               │
│               DF Filter: prune terms with DF > τ·|C|     │
│               (too common = non-discriminative)          │
│                          │                               │
│                          ▼                               │
│               Inject surviving n-grams into BM25 index   │
│               → "Enriched Corpus"                        │
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│                     ONLINE (per query)                    │
│                                                          │
│  User Query ──→ LLM generates "expected-response sketch" │
│                (concepts, entities, discriminative terms  │
│                 likely in answer but absent from query)   │
│                          │                               │
│                          ▼                               │
│               DF Filter: prune terms with DF=0 (absent)  │
│               or DF > τ·|C| (too common)                 │
│                          │                               │
│                          ▼                               │
│               SIRA compiles retrieval program:           │
│               score(d) = BM25(q_orig) + w·BM25(q_exp)    │
│                          │                               │
│                          ▼                               │
│               Single BM25 call → Top-k documents         │
│                          │                               │
│                          ▼                               │
│               (Optional) LLM pointwise reranker           │
└──────────────────────────────────────────────────────────┘
```

## Key Design Decisions

| Aspect | SIRA | Dense Retrieval | Agentic Search |
|--------|------|-----------------|----------------|
| Retrieval paradigm | Lexical (BM25) | Dense (embeddings) | Multi-round lexical/dense |
| Training required | None | Requires relevance labels | Prompt engineering |
| Interpretability | Full (weighted terms) | Opaque (vector similarity) | Partial |
| Rounds per query | 1 | 1 | 3-10+ |
| Uses LLM | Yes (enrichment) | No | Yes (reasoning loop) |
| Corpus-specific | Yes (offline enrichment) | Yes (embedding index) | Learns online |

## DF Filter: The Critical Component

The Document-Frequency filter is what makes SIRA work. LLMs can propose terms, but without corpus statistics they cannot know:
- Whether a term exists in the corpus at all
- Whether a term is too common to be discriminative
- How much IDF weight a term would contribute

The DF filter eliminates:
1. **Absent terms** (DF=0) — wasted retrieval effort
2. **Overly common terms** (DF > τ·|C|) — insufficient discriminative power
3. Terms the LLM hallucinated

The threshold τ is a tunable hyperparameter controlling the precision-recall tradeoff.

## Performance

- **BEIR benchmarks**: Outperforms E5 (unsupervised and supervised), SPLADE, and multi-round agentic baselines
- **Efficiency**: One BM25 call vs. 3-10+ rounds of agentic search
- **Interpretability**: Every term in the final query is auditable — you can see exactly what was added and why
- **Training-free**: No supervised pairs, no relevance labels, no fine-tuning required

## Limitations

- Requires offline corpus enrichment (LLM must read every document once)
- Benefits diminish on corpora where vocabulary gap is small
- Dependent on LLM quality for enrichment quality
- DF filter adds a hyperparameter (τ) that may need corpus-specific tuning

## Related

- [[concepts/information-retrieval]] — Core IR concepts and retrieval paradigms
- [[concepts/query-understanding]] — Query understanding stack (Tunkelang)
- [[concepts/bm25]] — The classic lexical retrieval function
- [[concepts/lexical-search]] — Bag-of-words retrieval approaches
- [[concepts/rag]] — Retrieval-Augmented Generation
- [[concepts/pseudo-relevance-feedback]] — Traditional query refinement
- [[concepts/harness-engineering/agentic-design-patterns]] — Multi-round agentic search patterns (ReAct, IRCoT)
- [[entities/daniel-tunkelang]] — Bag-of-documents model, query understanding
