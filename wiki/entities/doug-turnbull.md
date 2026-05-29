---
title: "Doug Turnbull (softwaredoug)"
type: entity
description: "Doug Turnbull is a search and information retrieval expert, author of the softwaredoug.com blog and the 'Cheat at Search' methodology. Known for advocating metadata-driven retrieval as a distinct paradigm and for making search problems tractable via LLM-powered query understanding."
category: entities
sub_category: People
tags:
  - person
  - information-retrieval
  - search
  - metadata-retrieval
  - explainable-ranking
  - blogger
  - ai-researcher
  - educator
status: complete
created: 2026-05-29
updated: 2026-05-29
sources:
  - https://softwaredoug.com/blog/2026/04/21/metadata-the-3rd-kind-of-retrieval
  - https://softwaredoug.com
  - https://maven.com/softwaredoug/cheat-at-search
---

# Doug Turnbull (softwaredoug)

## Overview

Doug Turnbull is a search engineer, blogger, and educator focused on making search problems tractable through attribute-driven retrieval and LLM-powered query understanding. He runs the **softwaredoug.com** blog and newsletter ("Doug's Daily Search Tips"), and teaches the **"Cheat at Search with Agents"** course on Maven.

## Key Contributions

### Metadata as the 3rd Kind of Retrieval (April 2026)

Turnbull's most notable framework argues that alongside **lexical search** (BM25) and **embedding/semantic search**, **metadata retrieval** constitutes a distinct third paradigm. In this approach:
- Queries and documents are decomposed into structured attributes (color, material, category, recency, etc.)
- Each attribute has its own domain-specific similarity function
- Ranking becomes **explainable, testable, and stakeholder-driven**

This framework connects directly to TurboPuffer's [[concepts/turbopuffer-rank-by-attribute]] infrastructure, which provides the technical mechanism for mixing metadata into first-stage BM25 scoring.

### "Cheat at Search" Methodology

Turnbull's core thesis: LLMs have made query/content classification dramatically easier, enabling search teams to "cheat" by solving problems through attribute extraction rather than complex NLP pipelines. His Maven course teaches using agents in search, building better RAG, and LLM-powered query understanding.

### Explainable Ranking Philosophy

> *"What we're really talking about is explainable ranking: ranking in a way that could evoke a conversation."*

Key tenets:
- Ranking correctness should be **objectively definable** and unit-testable
- Stakeholders can describe what's broken in their own language — no user eval studies needed
- Each attribute becomes a problem to solve independently (color similarity, material hierarchy, category taxonomy)

## Online Presence

- **Blog**: [softwaredoug.com](https://softwaredoug.com) — "Doug's Daily Search Tips"
- **Course**: [Cheat at Search with Agents](https://maven.com/softwaredoug/cheat-at-search) (Maven, starting May 2026)
- **Topics**: Search, lexical retrieval, embedding retrieval, metadata retrieval, RAG, query understanding, agentic retrieval

## Related Pages

- [[concepts/metadata-retrieval]] — The retrieval paradigm Turnbull advocates
- [[concepts/turbopuffer-rank-by-attribute]] — Infrastructure implementation of metadata scoring
- [[concepts/bm25]] — Lexical retrieval baseline
- [[concepts/query-understanding]] — The upstream problem metadata retrieval depends on
- [[concepts/reranking]] — The traditional multi-stage alternative
