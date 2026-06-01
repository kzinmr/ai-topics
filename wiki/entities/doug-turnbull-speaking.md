---
title: Doug Turnbull - Speaking & Community
type: entity-sub
parent: doug-turnbull
created: 2026-04-10
updated: 2026-05-27
tags:
  - person
  - writing
  - community
  - methodology
sources: []
---

# Doug Turnbull: Speaking & Community

## Conference Talks

Turnbull is a regular speaker at search industry conferences:

- **\\\\\\\"Lexical Search & BM25\\\\\\\" — Cheat at Search Essentials** (May 2026, Maven course): Live training course on the fundamentals of lexical search. Covers tokenization (whitespace → intelligent tokenizers with stemming/synonyms/entities), query processing (AND/OR matching, Elasticsearch DSLs), scoring evolution (TF → TF\\*IDF → BM25), multi-field search (naive sum vs. DisMax), BM25 parameters (k1 saturation, b length bias), and BM25F for combining fields. Key insight: \\\"BM25 ≈ Relevance Given Match\\\" — and agents handle the semantics when matching fails. Course discount code: `bm25rocks`. Uses [[entities/jxmo|searcharray]] educational library. [[raw/articles/2026-05-13_softwaredoug_lexical-search-bm25]]

- **\\\\\\\"Vector Search & Embedding Retrieval\\\\\\\" — Cheat at Search Essentials** (May 2026, Maven course): Day 3 of the Maven course. Covers embeddings primer (triples training, dot product/cosine similarity, sigmoid + contrastive loss, backpropagation), Two-Tower architecture for cold-start (user/movie encoders → dot product), transformer sentence embeddings (BERT CLS token, Q&A retrieval), vector search algorithms (k-means clustering, HNSW hierarchical graphs, ScANN/DiskANN clusters+graphs), filtered similarity (pre-/post-/native filtering, ACORN1), embedding pitfalls (hubness/collapse, compression loss, Similarity ≠ Relevance), and hybrid search strategy (multiple retrieval arms, LLM as orchestrator). Key insight: \"Split by strategy, not by index type — BM25 + vector as tools for agents.\" Discount code: `vectorsrock`. [[raw/articles/2026-05-13_softwaredoug_vector-search-embeddings]]

- **\\\\\\\"How To Build Your First Agentic Search Application\\\\\\\"** (Feb 2026, Vanishing Gradients podcast): 35-minute interview covering the practical implementation side of agentic search — passive vs active search spectrum, core tool-calling loop in code, the harness validation loop with LLM-as-Judge, long-running agents/memory compaction, and build-vs-buy decisions (Pydantic AI vs hand-rolling). [[raw/articles/2026-02-20_doug-turnbull-build-first-agentic-search-app]]

- **\"Rag is the What. Agentic search is the How.\"** (April 2026): 54-minute talk tracking the paradigm shift from classical RAG to agentic search — arguing that complexity moves from retrieval to the agent+harness, and that "dumb retrievers" (BM25, grep) work best with agent reasoning. Explicitly connects to SID-1, semantic grep, and scaffold+tool design. [[raw/articles/2026-04-22_doug-turnbull-rag-is-the-what-agentic-search-is-the-how]]

- **\"Why 2026 is The Year of Agentic Search\"** (May 2026, YouTube): 65-minute fireside chat with Jo Kristian Bergum (Vespa.ai) on the four pillars of agentic search — LLM Query Understanding at scale, Autoresearch (agents writing ranking code), Agentic Search Harnesses (feedback loops that make dumb retrievers smart), and LLM-as-a-Judge for principled evaluation. References Doug's Maven course starting May 18. [[raw/articles/2026-05-01_doug-turnbull-2026-is-the-year-of-agentic-search]]

- **\\\"LLM Query Understanding — Cheat at Search\\\"** (May 2026, guest lecture): Practical code-level guide to using LLMs for query understanding in e-commerce search. Covers embedding collapse (hubness), why structured QU beats pure embeddings for narrow domains, synonym extraction with Pydantic+BM25 boosting, deep multi-label category classification (10K+ labels) with dynamic Pydantic enums for cost optimization, and caching strategies. Demonstrates 12% NDCG improvement (0.541 → 0.608) on Wayfair queries with gpt-4.1-nano. Key insight: \"BM25 narrows the label space, enabling cheap LLM classification, which then boosts BM25 scores\" — a virtuous cycle. Complemented by [[concepts/query-understanding]] concept page enrichment. [[raw/articles/2026-05-20_softwaredoug_llm-query-understanding-cheat-at-search]]

- **\\"Long Running Search Agents — Cheat at Search\\"** (June 2026, guest lecture): Progressive strategies for search agents that run unattended for hours/days/weeks. Covers 7 strategies: single context, cron job (fresh restarts), context compaction, local index/memory, frontier prompt (guided exploration), non-agentic query model, and agent self-querying. Key empirical finding: local index yields 3.7x improvement over naive restart patterns (2.68 vs 0.72 yield/call). Introduces two-loop design separating exploration planning from execution. Colab notebook available. [[concepts/long-running-search-agents]] [[raw/articles/2026-06-02_softwaredoug_long-running-search-agents]]

- **\\"Steering Lost Agents — Cheat at Search\\"** (May 2026, guest lecture): Part 3 of the Cheat at Search series — 65-slide deep dive into agentic design patterns for search. Covers the two-loop architecture (agentic loop + harness control plane), carrot-and-stick steering model, seven steering patterns (Ralph loop, rule-based validation, LLM-as-Judge, reranker-in-response, few-shot priming, tool guards, subagent delegation), filesystem-like search tools (`ls_wands`/`grep_wands`/`cat_wands`), and BEAM search for systematic exhaustive exploration. Empirical results on WANDS dataset: BM25 0.5408 → FS Tools 0.5565 → +Few-Shot 0.5652 → +Delegation 0.5661. Key insight: \"The agent picks the tools, you control how the tools respond — tool responses ARE prompt engineering.\" Complemented by new [[concepts/agent-steering]] concept page and [[concepts/agentic-search]] enrichment. Colab notebook available. [[raw/articles/2026-05-27_softwaredoug_cheat-at-search-steering-lost-agents]]

- **\\"Will Agents Replace Search Teams? (a discussion)\\"** (Jan 2026, YouTube): 55-minute discussion with Daniel Tunkelang exploring the boundary between what agents can and cannot replace in search teams — covers the latency-feedback tradeoff, domain-specific LLM assumptions, economic disruption (EXA, Reddit), stakes-based error models, and the growing importance of critical thinking. [[raw/articles/2026-01-29_doug-turnbull_will-agents-replace-search-teams]]

- **Berlin Buzzwords / Haystack EU** (2024): "Learning to Rank for Reddit Search: A Project Retro" with Charles Njoroge

- **Elastic{ON}16** (2016): "The Ghost in the Search Machine"
- **MICES 2024** (Mix Camp E-Commerce): "Planning of E-Commerce Relevance Work"
- **Relevance Cornucopia** workshops: Intensive small-group training on "Think Like a Relevance Engineer" and "Hello LTR"

He maintains an active blog at softwaredoug.com with regular "daily search tips" — concise, practical observations about search engineering — and a newsletter with thousands of subscribers.

## Key Quotes

> "Agents put the Resilient in RAG."

> "Grug-brained evals: Big brain spend months building perfect quality metrics. Grug brain no trust, and just want dumb labels from coworkers 👍/👎."

> "The tests are the code now."

"> "Content understanding IS query understanding."

> "Embedding collapse is real. In your tiny domain, everything looks similar. Structured query understanding fixes this."

> "All search is structured now — there's no excuse for unstructured search queries in the age of LLMs."

> "If you have discipline to throw away your first idea, draft, throwaway code — you can move faster than any design doc."

> "Start with Who, not Why. Work with amazing people you love collaborating with, the rest falls out."

> "RAG isn't a vector search problem. Through market forces, embeddings became the singular framework we understood RAG. It's the wrong lens."

> "Agents turn simple keyword search into compelling search experiences. Thick APIs hide the reasoning from the agent."

> "Semantic search needs three pillars: representation, similarity, AND match criteria. Embeddings fail at the third."

> "The agent picks the tools, you control how the tools respond. Tool responses ARE prompt engineering."

## Related

- [[entities/doug-turnbull]] — Main entity page
