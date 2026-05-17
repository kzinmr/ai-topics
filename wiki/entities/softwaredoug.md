---
title: Doug Turnbull (softwaredoug)
created: 2026-05-17
updated: 2026-05-17
type: entity
tags: [person, search, information-retrieval, blogger, educator, consulting, open-source, rag, evaluation]
sources: [raw/articles/2026-05-17_softwaredoug_search-evaluation-ndcg.md]
---

# Doug Turnbull (softwaredoug)

Search and relevance engineering expert, Principal Engineer at Daydream, and creator of the "Cheat at Search Essentials" training series. Known for making search relevance and evaluation accessible through practical, "grug-brained" approaches.

## Bio

- **Name**: Doug Turnbull
- **Handle**: softwaredoug (GitHub, X/Twitter, domain)
- **Location**: Charlottesville, VA
- **Current**: Principal AI Engineer at Daydream (e-commerce search)
- **Previous**: Principal Engineer at Reddit, Staff Relevance Engineer at Spotify, search at Shopify, CTO at OpenSource Connections
- **Blog**: [softwaredoug.com](http://softwaredoug.com)
- **X/Twitter**: [@softwaredoug](https://twitter.com/softwaredoug)
- **GitHub**: [softwaredoug](https://github.com/softwaredoug)
- **LinkedIn**: [softwaredoug](https://linkedin.com/in/softwaredoug)

## Books

- **Relevant Search** (Manning, 2016) — co-authored with John Berryman. 360 pages covering search relevance with Solr and Elasticsearch.
- **AI-Powered Search** (Manning, 2025) — co-authored with Trey Grainger. Codebase at [treygrainger/ai-powered-search](https://github.com/treygrainger/ai-powered-search).

## Open Source

- **[Elasticsearch Learning to Rank](https://github.com/o19s/elasticsearch-learning-to-rank)** — Plugin integrating Learning to Rank (LTR) with Elasticsearch (1.5k ⭐)
- **[Quepid](https://github.com/o19s/splainer)** — Elasticsearch/Solr relevance testing sandbox
- **[searcharray](https://github.com/softwaredoug/searcharray)** — Full-text search as numpy array (302 ⭐)
- **[hello-ltr](https://github.com/softwaredoug/hello-ltr)** — Jupyter notebooks for Learning to Rank with Solr/Elasticsearch

## Training & Courses (Maven)

- **[Cheat at Search Essentials](https://maven.com/softwaredoug/cheat-at-search)** — Rethinking the search stack with LLMs
- **[Relevant Search](https://maven.com/softwaredoug/relevant-search)** — Masterclass on making Elasticsearch sing
- **[Autoresearch](https://maven.com/softwaredoug/autoresearch)** — One-day workshop on automated search evaluation

## Philosophy & Approach

Doug advocates for a pragmatic, "grug-brained" approach to search evaluation:

- **"Test in prod or live a lie"** (quoting Charity Majors) — ship behind feature flags, analyze in production rather than building complex offline testing infrastructure
- **"Grug-brained evals"** — start simple: ship → eval → analyze → iterate. Don't spend months building perfect evaluation pipelines before delivering impact
- **Side-by-sides are underrated** — have domain experts directly compare two result sets
- **Continuous delivery** — ship iterations frequently, gather clickstream data incrementally
- **NDCG answers narrow questions** — it tells you if you impacted expected queries positively, not if you improved overall search quality

## Key Concepts Covered in His Work

- [[ndcg]] — Normalized Discounted Cumulative Gain, central to search evaluation
- **BM25** — Lexical search scoring, including Bayesian BM25 and calibration
- **Click models** — COEC (clicks over expected clicks), turning user behavior into relevance judgments
- **LLM as a judge** — Using LLMs for instant search result labeling
- **Learning to Rank (LTR)** — Machine learning for search relevance
- **Hybrid search** — Combining lexical (BM25) and vector (embedding) retrieval
- **RAG** — Retrieval-Augmented Generation blind spots and agent-based fixes
- **Late interaction models** — ColBERT-style fine-grained passage scoring
- **Search management** — Manual curation as a complement to algorithmic ranking

## Notable Blog Posts (2026)

- "Agentic search models" (2026-05-11) — Agents, not APIs, as the future of search
- "Can agents replace the search stack?" (2026-04-28)
- "Stop evaluating search with queries" (2026-03-30)
- "Grug-brained evals" — referenced in the NDCG talk
- "Agents put the Resilient in RAG" (2026-03-26)
- "The tests are the code now" (2026-03-10) — on AI coding changing software engineering
- "Consider pairwise evals instead of pointwise" (2026-02-27)
- "How pointwise evals fall apart" (2026-02-23)

## Relevance to AI Agents

Doug's recent work increasingly focuses on the intersection of search and AI agents:
- Advocates for **agentic search** — agents replacing traditional query→retrieve→rank pipelines
- Explores **LLM-as-judge** for search evaluation, using structured outputs for relevance scoring
- Connects RAG blind spots to agent-based approaches for iterative retrieval
- His "Cheat at Search Essentials" course rethinks the entire search stack with LLMs

## See Also

- [[ndcg]] — Detailed concept page on NDCG and search evaluation metrics
- [Doug Turnbull's Blog](http://softwaredoug.com) — Regular posts on search, BM25, RAG, and agents
