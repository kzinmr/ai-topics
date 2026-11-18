---
title: "SearchArray"
type: concept
aliases:
  - searcharray
  - softwaredoug/searcharray
created: 2026-04-25
updated: 2026-11-18
tags:
  - concept
  - search
  - information-retrieval
  - bm25
  - open-source
  - developer-tooling
  - python
sources:
  - https://github.com/softwaredoug/searcharray
  - wiki/raw/articles/2026-05-17_softwaredoug-com_autoresearching-better-msmarco-bm25.md
  - wiki/raw/articles/2026-05-13_softwaredoug_lexical-search-bm25.md
---

# SearchArray

**SearchArray** is an open-source Python library by [[entities/doug-turnbull|Doug Turnbull]] (GitHub: `softwaredoug/searcharray`, ~300 stars) that implements **full-text lexical search (BM25) as a pandas extension array**. Its thesis — "making search less weird" — is that search relevance experimentation should not require spinning up [[concepts/elasticsearch]] or Solr: you should be able to load a corpus into a DataFrame, index a text column, and run BM25/phrase/boolean queries **inside a single Colab notebook**.

## What it is technically

- A **pandas ExtensionArray** backed by an **inverted index** over the column's text values
- **Cython-optimized roaring-bitmap intersections** for fast phrase and boolean matching
- Direct **numpy-array access to corpus statistics** (term frequencies, document frequencies, document lengths), so users can compute BM25 — or any custom ranking function — by hand

That last property is what makes SearchArray notable beyond a toy: it is designed for **direct corpus interaction** ([[concepts/information-retrieval]]), the philosophy that you learn ranking by *computing* it, not by configuring a server.

## Canonical uses

1. **The Cheat at Search curriculum** — Turnbull's Maven course *Lexical Search & BM25* (and the broader "Cheat at Search Essentials" series) uses SearchArray as the hands-on library for teaching tokenization, scoring evolution (TF → TF·IDF → BM25 → BM25F), multi-field search (naive sum vs DisMax), and the k1/b parameters. Key taught insight: *"BM25 ≈ Relevance Given Match."* See [[entities/doug-turnbull-speaking]].
2. **BM25 tuning experiments** — the [[concepts/autoresearch-bm25-msmarco]] experiment (an autoresearch coding agent improving BM25 on MiniMarco/MSMARco with NDCG as the reward) uses SearchArray to fetch numpy arrays and compute BM25 manually, precisely because the agent needs raw access to term/doc statistics to propose ranking-function changes. See [[raw/articles/2026-05-17_softwaredoug-com_autoresearching-better-msmarco-bm25]].
3. **Relevance-engineering prototyping** — evaluate ranking ideas on small corpora before porting to production engines; complements Turnbull's [[entities/doug-turnbull-projects|Quepid]] (test workbench for production engines) at the earlier, notebook stage.

## Position in the retrieval landscape

| Tool | Layer | Requires server? | Good for |
|------|-------|------------------|----------|
| **SearchArray** | pandas extension array + inverted index | No | Teaching, prototyping, agent-driven ranking experiments |
| **Rank BM25 / whoosh** | Python library | No | Library-level BM25 without corpus-stat access |
| **[[concepts/elasticsearch]] / Solr / OpenSearch** | Distributed engine | Yes | Production search, aggregations |
| **[[concepts/vector-databases]]** | ANN engine | Usually | Dense semantic retrieval (SearchArray is lexical-only) |

SearchArray deliberately stays **lexical** ([[concepts/bm25]], [[concepts/lexical-search]]) — the semantic gap is where [[concepts/agentic-rag|agentic search]] and rerankers enter, a division of labor central to Turnbull's "Relevance Engineering" framing.

## Related

- [[entities/doug-turnbull]] — creator; see also [[entities/doug-turnbull-projects]], [[entities/doug-turnbull-core-ideas|SearchArray: Making Search Less Weird]]
- [[concepts/bm25]] / [[concepts/lexical-search]] — the algorithms it exposes
- [[concepts/autoresearch-bm25-msmarco]] — agent-tuned BM25 experiment built on it
- [[concepts/information-retrieval]] — parent discipline
- [[concepts/trey-grainger]] — parallel relevance-engineering educator (Searchkernel)

## Sources

- [softwaredoug/searcharray on GitHub](https://github.com/softwaredoug/searcharray)
- [[raw/articles/2026-05-13_softwaredoug_lexical-search-bm25]] — course article using the library
- [[raw/articles/2026-05-17_softwaredoug-com_autoresearching-better-msmarco-bm25]] — BM25 autoresearch baseline
