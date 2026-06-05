---
title: Doug Turnbull (softwaredoug)
created: 2026-05-17
updated: 2026-05-28
type: entity
tags:
  - person
  - search
  - blogger
  - company
  - open-source
  - rag
  - evaluation
sources:
  - raw/articles/2026-05-17_softwaredoug_search-evaluation-ndcg.md
  - raw/articles/2026-05-17_softwaredoug-com_autoresearching-better-msmarco-bm25.md
  - raw/articles/2025-09-18_softwaredoug_bm25f-from-scratch.md
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

## Notable Blog Posts (2025–2026)

- "BM25F from scratch" (2025-09-18) — Full derivation of multi-field BM25: building blocks, IDF distortion problem, TF double-counting, two-step correction. Foundation for Elasticsearch `cross_fields` and beyond.
- "Autoresearching BM25 on MSMarco" (2026-05-17) — Agent-driven BM25 tuning on passage retrieval, dual-gate evaluation, overfitting lessons
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

## Talks & Presentations (2026)

### AutoReSEARCH — Ranking Coded by Agents (HaystackConf 2026, May 14)

Turnbull's signature 2026 presentation, demonstrating how coding agents can iteratively generate and optimize search ranking code. Key contributions from this talk:

- **Agent-coded rankers with dependency injection** — agents assemble ranking functions from injected primitives (BM25, vector search) rather than modifying search infrastructure
- **The overfitting problem in agent-generated code** — without guardrails, agents produce query-specific lookup tables; Turnbull identified three guardrails: LLM-based overfit detection, patch size limits (10 lines, 120 chars), and train/validation/holdout splits
- **Focused composition** — a staged approach where each round narrows scope (first optimize retrieval, then add query rewriting), preventing combinatorial overwhelm
- **AutoReSEARCH IS machine learning** — the central thesis: "We still need to take our eval data, have good splits, and control the visibility of that data to the model"
- **The Erdos analogy** — agents exhaustively explore human knowledge (like LLMs finding forgotten proofs), picking the "least offensive" solution within defined boundaries

> *"I've done search at like probably a hundred places in some capacity in the past. I like to say I'm still trying to figure out how search works, because it's honestly something that keeps changing all the time."*

### RAG is the What. Agentic Search is the How. (April 22)

Turnbull's central thesis talk arguing that RAG was just a "thicc daddy search system" and the paradigm has shifted to agentic search where complexity moves from the retrieval layer to the agent+harness layer. Core argument progression: structured attributes → tool calling → agent reasoning → dumb retrievers. Key quote: *"Don't waste too much time on the original RAG paradigm. AI has moved on."*

### Why 2026 is The Year of Agentic Search (May 1, with Jo Kristian Bergum)

Joint talk with Vespa.ai's Jo Kristian Bergum (now CEO of Hornet) making the case that 2026 is the breakout year for agentic search. Covers LLM query understanding, AutoReSEARCH, search harnesses, and LLM-as-judge. Turnbull hosts weekly Maven events roughly once a week, featuring guests from across the search community.

## Teaching Philosophy

From the transcripts, Turnbull's teaching approach is characterized by:
- **"Embarrassing myself as a service"** — he prioritizes honesty and transparency, openly sharing what doesn't work alongside what does
- **"Grug-brained" simplicity** — start with the dumbest thing that can work, then iterate
- **Practical over theoretical** — his HaystackConf talk included live demos of overfitting behavior and guardrail failures, not just success stories
- **Course structure: "Cheat at Search"** — Maven-based lightning lessons, each ~1 hour, covering topics from NDCG to coding agents; the AutoReSEARCH material appears in Lesson 7 (Coding Agents & Auto Research)

## See Also

- [[ndcg]] — Detailed concept page on NDCG and search evaluation metrics
- [[autoresearch-bm25-msmarco]] — Case study of autoresearch applied to BM25 optimization
- [Doug Turnbull's Blog](http://softwaredoug.com) — Regular posts on search, BM25, RAG, and agents
