---
title: "Quepid"
type: concept
aliases:
  - Quepid
  - quepid
  - QuePID
created: 2026-04-25
updated: 2026-11-24
tags:
  - open-source
  - search
  - relevance
  - developer-tooling
  - information-retrieval
sources:
  - https://github.com/o19s/quepid
  - https://www.quepidapp.com
status: active
---

# Quepid

**Quepid** is an open-source, collaborative tool for **measuring and improving
search relevance** ("search quality") across search engines. Built and maintained
by **O19S** (Oh Nineteen Oh Ess), the San Francisco search-and-recommendations
consultancy, it provides a UI where teams define queries, expected results, and
relevance ratings, then score ranking configurations against them — turning
subjective relevance work into repeatable, testable evaluation.

## What It Does

Quepid lets you:

- **Define query sets** ("cases") with a list of queries to evaluate.
- **Assign ratings** to documents (a ground-truth relevance scale).
- **Score ranking configurations** using IR metrics (nDCG, AP/pairwise accuracy,
  rank-based measures) against those ratings.
- **Compare configurations side by side** to iterate on ranking tuning and know
  whether a change helped or hurt.

It supports **OpenSearch, Elasticsearch, Solr, Vectara, Algolia**, and custom
search backends. The hosted service is **Quepid.com** (`quepidapp.com`).

## Relevance to LLM / RAG

Quepid matters to the AI agent space because **RAG retrieval quality is a search
relevance problem**. The same nDCG / graded-relevance evaluation workflow Quepid
implements is exactly what teams need when tuning embeddings, BM25/hybrid retrievers,
and rerankers feeding an LLM. Its companion project **`o19s/agent_q`** — "Headless
agent for test driven relevancy with Quepid.com" — extends this into automated,
agent-driven relevance testing, aligning with the broader wiki themes of
[[concepts/llm-trace-judge]] and [[concepts/llm-evaluation]].

O19S also maintains related relevance tooling such as **Splainer** (explains
Solr/Elasticsearch query scoring) and has authored work on search relevance
benchmarks like **BEIR**-adjacent evaluations.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Maintainer | O19S (`o19s`) |
| Language | Ruby (Rails) |
| License | Apache-2.0 |
| Stars | ~349 |
| Hosted app | quepidapp.com / quepid.com |
| Backends | OpenSearch, Elasticsearch, Solr, Vectara, Algolia, custom |

## Related Pages

- [[concepts/llm-trace-judge]] — complementary approach to output evaluation
- [[concepts/retrieval-augmented-generation]] — retrieval quality is the core thing Quepid measures
- [[concepts/information-retrieval]] — the IR discipline Quepid operationalizes
- [[concepts/llm-evaluation]] — broader evaluation theme

## Sources

- [o19s/quepid — GitHub](https://github.com/o19s/quepid) — "Improve your OpenSearch, Elasticsearch, Solr, Vectara, Algolia and Custom Search search quality." Ruby, Apache-2.0 (scraped 2026-11-24)
- [Quepid.com](https://www.quepidapp.com)
