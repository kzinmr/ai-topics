---
title: Doug Turnbull - Key Projects & Works
type: entity-sub
parent: doug-turnbull
created: 2026-04-10
updated: 2026-06-05
tags:
  - person
  - methodology
  - open-source
  - writing
sources:
  - https://www.youtube.com/watch?v=OGnW2Pu2uVE
  - https://www.youtube.com/watch?v=h370222tnAQ
  - https://www.youtube.com/watch?v=Jd2_7sVXUxA
---

# Doug Turnbull: Key Projects & Works

## Books

### *Relevant Search* (Manning, 2016)
Co-authored with John Berryman, foreword by Trey Grainger. The definitive practical guide to search relevance engineering using Elasticsearch and Solr. Covers relevance scoring, query parsing, analyzers, synonym handling, learning-to-rank, and evaluation methodologies. 360 pages. Still considered essential reading for search practitioners.

### *AI-Powered Search* (Manning, 2025)
Co-authored with Trey Grainger and Max Irwin, foreword by Grant Ingersoll. 520 pages covering the integration of LLMs into search architectures: RAG, semantic search, hybrid retrieval, learning-to-rank, click models, knowledge graphs, multimodal search, and practical deployment patterns. Turnbull contributed chapters 10–12 on "Learning to Rank," "Automated Learning to Rank with Click Models," and "Overcoming Bias in Learned Relevance Models."

## Open-Source Projects

### Quepid (o19s/quepid)
Open-source (Apache 2.0) search relevance testing workbench. 339 stars. Supports Elasticsearch, Solr, OpenSearch, Vectara, Algolia, and custom backends. Features include test cases, human judgment gathering, NDCG calculation, query snapshots, and team collaboration. Originally a closed-source product, Turnbull's team at OpenSource Connections open-sourced it in 2019 with a free hosted tier.

### Elasticsearch Learning to Rank Plugin (o19s/elasticsearch-learning-to-rank)
Open-source plugin enabling machine learning-based ranking within Elasticsearch. Used in production at Yelp, Wikipedia, Snag, and others. Turnbull co-created it with Erik Bernhardson, David Causse, and Daniel Worley. Includes the hello-ltr sandbox for experimentation.

### SearchArray (softwaredoug/searcharray)
Pandas extension array for BM25-powered lexical search. 304 stars. Makes search relevance experiments possible in a single Colab notebook without standing up a search engine. Includes Cython-optimized phrase search with roaring-like bitmap intersections.

### local-llm-judge (softwaredoug/local-llm-judge)
Python project enabling local LLMs to serve as search relevance judges. 28 stars. Runs hundreds of relevance judgment pairs per minute on a MacBook, democratizing search evaluation without cloud API costs.

## Training & Consulting

### Cheat at Search (Maven Course)
Live, cohort-based training course on search engineering with LLMs and agents. Rated 4.7/5 from 74+ reviews. Covers information retrieval as an agentic process, LLM query understanding, BM25 + lexical retrieval, embedding retrieval, hybrid search, evaluation/NDCG, and agentic search. Priced at $1,300 per student with free "Essentials" lightning lessons available.

**Course structure (2026 cohort, starting May 18):**

| Lesson | Topic | Core Content |
|--------|-------|-------------|
| Essentials 1 | **Search Evaluation (NDCG)** | Judgment lists, graded relevance (0-1), DCG, NDCG, precision@k, MAP, MRR. "How should search results be evaluated?" [[raw/articles/2026-05-17_softwaredoug_search-evaluation-ndcg]] |
| Essentials 2 | **Lexical Search & BM25** | Tokenization (whitespace → intelligent with stemming/synonyms/entities), query processing (AND/OR, Elasticsearch DSLs), scoring evolution (TF → TF×IDF → BM25), multi-field search (naive sum vs. DisMax), BM25 parameters (k1 saturation, b length bias), BM25F. Key insight: "BM25 ≈ Relevance Given Match." Uses [[concepts/searcharray]] library. [[raw/articles/2026-05-13_softwaredoug_lexical-search-bm25]] |
| Essentials 3 | **Vector Search & Embeddings** | Embeddings primer (triples training, dot product/cosine similarity, sigmoid + contrastive loss), Two-Tower architecture, transformer sentence embeddings, vector search algorithms (k-means, HNSW, ScANN/DiskANN), filtered similarity (pre-/post-/native filtering, ACORN1), embedding pitfalls (hubness/collapse, Similarity ≠ Relevance). Key insight: "Split by strategy, not by index type — BM25 + vector as tools for agents." [[raw/articles/2026-05-13_softwaredoug_vector-search-embeddings]] |
| Lesson 1 | **LLM Query Understanding** | Using LLMs for query understanding in e-commerce: structured attribute extraction from free-text queries, synonym extraction with Pydantic+BM25 boosting, deep multi-label category classification (10K+ labels) with dynamic Pydantic enums, caching strategies. 12% NDCG improvement (0.541 → 0.608) on Wayfair queries. Key insight: "BM25 narrows the label space, enabling cheap LLM classification, which then boosts BM25 scores." [[raw/articles/2026-05-20_softwaredoug_llm-query-understanding-cheat-at-search]] |
| Lesson 3 | **Steering Lost Agents** | Agentic design patterns for search: two-loop architecture (agentic loop + harness control plane), carrot-and-stick steering model, seven steering patterns (Ralph loop, rule-based validation, LLM-as-Judge, reranker-in-response, few-shot priming, tool guards, subagent delegation), filesystem-like search tools (`ls_wands`/`grep_wands`/`cat_wands`), BEAM search for exhaustive exploration. Key insight: "The agent picks the tools, you control how the tools respond — tool responses ARE prompt engineering." [[raw/articles/2026-05-27_softwaredoug_cheat-at-search-steering-lost-agents]] |
| Lesson 4 | **LLM as a Judge** | Automated search relevance evaluation with LLMs. Principled rubric design, "grug-brained evals" (simple thumbs-up/thumbs-down from coworkers), combined with engagement-based ground truths for production validation. [[raw/articles/2026-05-28_softwaredoug_cheat-at-search-llm-as-judge]] |
| Lesson 5 | **Long Running Search Agents** | Progressive strategies for agents running unattended for hours/days/weeks: 7 strategies (single context, cron job, context compaction, local index/memory, frontier prompt, non-agentic query model, agent self-querying). Key finding: local index yields 3.7x improvement over naive restart patterns. Two-loop design separating exploration planning from execution. [[raw/articles/2026-06-02_softwaredoug_long-running-search-agents]] |
| Lesson 6 | **Agents That Code Their Own Search (RLMs & Ranker Coding)** | Two-part lecture. Part 1: RLMs applied to search — Python REPL as agent's sole tool, stateful variables, recursive `llm_query()` calls, expert-finding from patent literature. Part 2: Agent-Driven Ranker Optimization — coding agent iteratively patches `rerank_wands()` function, NDCG evaluation on train/test splits, guardrails (overfitting detection, length limits, holdout validation). Key insight: "AI coding IS model development." [[raw/articles/2026-06-04_softwaredoug_search-with-agents-lesson6-rlms]] |
| Lesson 7 | **AutoReSEARCH — Ranking Coded by Agents** | Using coding agents to iteratively optimize search ranking code. Dependency injection pattern (inject BM25/vector primitives, let agent assemble ranking functions), three guardrails against overfitting, focused composition (narrow scope per round), MS Marco BM25 experiment. Conference version presented at HaystackConf 2026. [[raw/articles/2026-05-14_softwaredoug_autoresearch-ranking-coded-by-agents-haystackconf]] |

**Slide deck series (2026):**
- Part 1: [[raw/articles/2026-05-17_softwaredoug_search-evaluation-ndcg|NDCG / Search Evaluation]] — graded relevance, DCG, NDCG, precision@k, MAP, MRR (see also [[concepts/ndcg]])
- Part 2: [[raw/articles/2026-05-20_softwaredoug_llm-query-understanding-cheat-at-search|LLM Query Understanding]] — structured attribute extraction from free-text queries
- Part 3: [[raw/articles/2026-05-27_softwaredoug_cheat-at-search-steering-lost-agents|Steering Lost Agents]] — agentic design patterns for search
- Part 4: [[raw/articles/2026-05-28_softwaredoug_cheat-at-search-llm-as-judge|LLM as a Judge]] — automated search relevance evaluation with LLMs (see also [[concepts/llm-search-judge]])
- Part 5: [[raw/articles/2026-06-02_softwaredoug_cheat-at-search-long-running-search|Long Running Search Agents]] — persistent agent strategies, context compaction, frontier prompts. Companion: [[transcripts/2026-06-02_softwaredoug_cheat-at-search-long-running-search-lecture]]

### Consulting & Training
Turnbull offers $12,000 team training courses (up to 12 participants) covering:
- Traction on Search Relevance at Your Organization
- Lexical + Vector → Hybrid Search
- Generative AI Augmented Retrieval

He describes himself as available as a "fractional search team lead" for organizations needing search expertise.

### Free Courses
- **Search Essentials (Search 101)**: Free 3-hour sessions with notebooks covering core search concepts — "What is BM25? What is an embedding? How do we evaluate search results?" Available at softwaredoug.com/search101. Referenced in the "Why 2026 is The Year of Agentic Search" fireside chat.
- **AutoReSEARCH Workshop**: One-day workshop on Maven (maven.com/softwaredoug/autoresearch) covering agent-coded ranking optimization. Announced during the "Why 2026 is The Year of Agentic Search" fireside chat.

## Related

- [[entities/doug-turnbull]] — Main entity page
- [[concepts/quepid]] — Search relevance testing workbench
- [[concepts/searcharray]] — Pandas-based BM25 search library
