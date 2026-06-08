---
title: "Metadata Retrieval — The 3rd Kind of Retrieval"
type: concept
description: "Metadata retrieval is a distinct retrieval paradigm alongside lexical (BM25) and embedding/semantic search, where structured attributes from queries and documents are matched using explainable, testable ranking rules — made practical by LLM-powered query understanding."
category: concepts
sub_category: Information Retrieval
tags:
  - search
  - metadata-retrieval
  - explainable-ranking
  - lexical-search
  - query-understanding
status: complete
related:
  - bm25
  - vector-search
  - reranking
  - turbopuffer-rank-by-attribute
created: 2026-05-29
updated: 2026-05-29
sources:
  - raw/articles/2026-04-21_softwaredoug_metadata-third-kind-retrieval.md
  - https://softwaredoug.com/blog/2026/04/21/metadata-the-3rd-kind-of-retrieval
  - https://turbopuffer.com/blog/rank-by-attribute
---

# Metadata Retrieval: The 3rd Kind of Retrieval

## TL;DR

Doug Turnbull (April 2026) argues that **metadata-based retrieval** constitutes a distinct third retrieval paradigm alongside lexical search (BM25) and embedding/semantic search. In this paradigm, queries and documents are decomposed into structured attributes, each with its own domain-specific similarity function. The ranking becomes **explainable, testable, and stakeholder-driven** — made practical because LLMs now make query/document attribute extraction cheap ("Cheat at Search").

## The Three Retrieval Paradigms

| Paradigm | Mechanism | Strength | Weakness |
|----------|-----------|----------|----------|
| **Lexical** (BM25) | Term frequency + inverse document frequency | Fast, scalable, interpretable | Keyword-only; misses semantics |
| **Embedding** (dense vectors) | Semantic similarity in latent space | Captures meaning, synonyms, intent | Black-box; hard to debug/control |
| **Metadata** (attributes) | Structured attribute matching with domain rules | Explainable, testable, stakeholder-driven | Requires attribute extraction; domain engineering |

## How Metadata Retrieval Works

### 1. Attribute Extraction (Query Side)

A user query like `"crimson suede couch"` is decomposed into structured attributes:

| Color | Material | Category |
|-------|----------|----------|
| Red | Leather > Suede | Furniture > Living Room > Couches |

### 2. Document Classification

Documents/products are tagged with the same attribute taxonomy:

| Product | Color | Material | Category |
|---------|-------|----------|----------|
| Red suede sofa | Red | Leather > Suede | Furniture > Living Room > Couches |
| Pink barbie recliner | Pink | Leather > Imitation | Furniture > Living Room > Recliners |

### 3. Per-Attribute Similarity

Each attribute has its own notion of similarity:
- **Color**: Red is closer to Pink than to Green. Primary/secondary color relationships matter. Stripes, plaid patterns need handling.
- **Material**: Is imitation leather acceptable when searching for suede? How much worse?
- **Category**: Hierarchical matching (Living Room > Couches vs Recliners).

### 4. Explainable, Testable Ranking

The ranking is expressed in user language:

> *"Show ankle-length leggings first, then calf-length, and exclude knee-length entirely."*

This is directly testable as a unit test — no user evaluation study required. Internal stakeholders can articulate what's broken through their own use of the system.

## Why Now: LLMs Changed the Game

Historically, attribute extraction required extensive NLP research (entity recognition, taxonomy building, relationship extraction). LLMs now make this trivial:

> *"We can now **Cheat at Search** — a problem that took extensive NLP research, now can be done painlessly."* — Doug Turnbull

This enables solving a fair number of search problems, even "semantic" ones, with less sophistication — just by having a conversation with a stakeholder about what matters.

## Contrast with Multi-Stage Search

| Approach | Metadata Retrieval | Traditional Multi-Stage |
|----------|-------------------|------------------------|
| **Philosophy** | Domain rules drive ranking | BM25 → reranker pipeline |
| **Explainability** | "This is excluded because it's knee-length" | "The model scored it lower" |
| **Testing** | Unit-testable per attribute | Requires eval sets and user studies |
| **Stakeholder input** | Direct — they describe what's broken | Indirect — through relevance judgments |

## Relationship to [[concepts/turbopuffer-rank-by-attribute]]

TurboPuffer's `rank-by-attribute` (April 2026) provides the **infrastructure** for metadata retrieval. It allows mixing numeric/date attribute values directly into BM25's first-stage scoring using `Saturate` and `Decay` functions. Doug Turnbull's framework provides the **philosophical justification** and **methodology** for treating metadata as a first-class retrieval paradigm, not just a filter or reranking afterthought.

Together, they suggest a convergence: **LLMs extract attributes from queries/documents → structured metadata → scored alongside BM25 in a single, scalable, explainable retrieval stage**.

## Key Concepts

- **Explainable ranking**: Ranking that could evoke a conversation — "would imitation leather be acceptable?" → if yes, how does it relate to other attributes?
- **Attribute as problem**: Each attribute (color, material, category, recency, authority) is a retrieval problem in itself, potentially using embedding + lexical approaches internally.
- **Cheat at Search**: Doug Turnbull's course/methodology for using LLMs + agents to solve search problems by classifying queries and content into attributes.

## See Also

- [[concepts/bm25]] — Okapi BM25 text ranking algorithm
- [[concepts/turbopuffer-rank-by-attribute]] — Infrastructure for mixing metadata into BM25 scoring
- [[concepts/reranking]] — Multi-stage retrieval with cross-encoders
- [[concepts/vector-search]] — Embedding-based semantic retrieval
- [[concepts/query-understanding]] — Query parsing and intent classification
- [[entities/doug-turnbull]] — Author of "Metadata: the 3rd kind of retrieval"
