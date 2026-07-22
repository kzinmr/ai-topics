---
title: "Agent Wikis"
type: concept
created: 2026-07-22
updated: 2026-07-22
tags:
  - knowledge-management
  - memory-systems
  - agent-memory
  - context-engineering
  - wiki
  - coding-agents
  - agents
  - survey
aliases:
  - llm-wiki
  - agent wiki
  - LLM Wiki
sources:
  - raw/articles/2026-07-21_mem0ai_state-of-agent-wikis.md
  - https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
  - https://cognition.ai/blog/deepwiki
  - https://factory.ai/news/wiki
  - https://x.com/mem0ai/status/2079585032587694582
related:
  - "[[concepts/wiki-memory]]"
  - "[[concepts/openwiki]]"
  - "[[entities/mem0]]"
  - "[[entities/cognition-devin]]"
  - "[[entities/factory-ai]]"
  - "[[entities/garry-tan]]"
  - "[[concepts/context-engineering]]"
  - "[[concepts/ai-agent-memory-two-camps]]"
---

# Agent Wikis

**Agent wikis** (also called **LLM Wikis**) are a knowledge management pattern where an LLM reads a body of sources, compiles them into a maintained set of markdown pages, and keeps those pages current as the sources change. Agents then read the pages instead of re-deriving everything from raw material on every question.

The pattern was codified by **Andrej Karpathy** in April 2026, and within months four independent teams shipped implementations: [[entities/cognition-devin|Cognition]] (DeepWiki), [[entities/factory-ai|Factory]] (AutoWiki), [[entities/langchain|LangChain]] (OpenWiki), and Garry Tan (GBrain).

## Core Architectural Pattern

All implementations share a consistent **three-layer architecture**:

| Layer | Description | Mutability |
|-------|-------------|------------|
| **Raw sources** | Immutable input: articles, papers, repos, data | Never edited by the model |
| **The wiki** | LLM-generated markdown: summaries, entity pages, concept pages, cross-references | Fully owned by the model |
| **The schema** | Config file (CLAUDE.md, AGENTS.md) defining organization and workflows | Updated by humans or agents |

Three operations run on top:
1. **Ingest** — file a source across the pages it affects
2. **Query** — read the wiki (optionally file good answers back as new pages)
3. **Lint** — periodic pass hunting contradictions, stale claims, and orphaned pages

### Compile at Ingest, Not at Query

The key insight inverts the RAG approach. Instead of assembling knowledge at query time from raw chunks (where nothing accumulates), an LLM assembles it once at ingest time into durable pages, then maintains them incrementally.

> RAG re-derives knowledge on every question. A wiki derives it once and then keeps it current.

### The Maintenance Insight

Human wikis rot because the bookkeeping burden (updating cross-references, keeping summaries current, reconciling documents) is unbounded and unglamorous. LLMs do not get bored, do not forget to update a cross-reference, and can touch fifteen files in one pass. **The LLM Wiki works because it removes the maintenance cost that killed every wiki before it.**

## Implementations

### DeepWiki (Cognition)

Pointed at every public GitHub repository. Swap `github.com` for `deepwiki.com` in any public repo URL. Over 50,000 top repos indexed. The wiki serves as retrieval infrastructure for the [[entities/cognition-devin|Devin]] agent — not the product's endpoint.

### AutoWiki (Factory)

Frames documentation as a build artifact in CI terms. Two-pass analysis: structural scan (README, manifests, CI config, entry points) + semantic scan (routes, API endpoints, service classes, schemas, feature flags). Work split across specialized agents. Refreshes on every push to the default branch via CI workflow.

### OpenWiki (LangChain)

Open-source CLI for codebase wikis, later expanded with **OpenWiki Brains**: Code Brain (repos) + Personal Brain (Gmail, Notion, git, X, Hacker News, web search). Output is structured markdown optimized for LLM context — written for the reader that will actually read it (the model).

See: [[concepts/openwiki]]

### GBrain (Garry Tan)

Personal-scale open-source version. Markdown in a git repo, a schema file, and an automatically maintained graph of entity cross-links. No vector database or service — just files a model maintains and a human can read.

## Technique Matrix

| Dimension | DeepWiki | AutoWiki | OpenWiki | GBrain |
|-----------|----------|----------|----------|--------|
| Scope | Public GitHub repos | Codebases (CI-integrated) | Code + Personal sources | Personal KB |
| Substrate | deepwiki.com | GitHub Wiki tab | Filesystem / git | git repo |
| Freshness | On demand | CI (push-triggered) | On demand | On demand |
| Output target | Devin agent | Coding agents | Coding agents | Any agent |
| Source material | GitHub repos | Code repositories | Code, email, Notion, X, HN, web | Documents |

## Limitations

- **Scale** — Index-first (no embeddings) is moderate-scale (~100 sources). Beyond a few hundred pages, hybrid BM25 + vector search is required.
- **Fidelity** — Compilation at ingest can silently lose detail from sources. Every later answer inherits that loss.
- **Staleness** — A compiled page is only as current as the last refresh. A stale wiki is worse than no wiki because it is confidently wrong in an authoritative format.
- **Compile cost** — Real tokens spent up front on pages that may never be queried.

## Distinction: Wiki vs Memory

Agent wikis are **not** agent memory. Two distinct axes:

1. **Corpus knowledge** — what a wiki compiles: what a body of material contains
2. **User/experience memory** — personal preferences, past decisions, rejected approaches. Needs per-user identity, interaction-based accumulation, contradiction handling, provenance

A wiki does the first and not the second. Dedicated memory layers (like [[entities/mem0|Mem0]]) handle the second with user_id-scoped memory that follows a person across sessions, apps, and agents.

## Origins and Lineage

- **Vannevar Bush, Memex (1945)** — The idea of a curated personal store with associative trails. The unsolved problem was who maintains the trails.
- **Andrej Karpathy, LLM Wiki (April 2026)** — Formalized the pattern: "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."
- **Independent convergence (May-July 2026)** — Four teams shipped the same architecture within months, independently.

## Related Concepts

- [[concepts/wiki-memory]] — Harrison Chase's framing of wikis as an agent memory pattern (June 2026)
- [[concepts/context-engineering]] — The broader discipline of managing agent context
- [[concepts/ai-agent-memory-two-camps]] — Taxonomy of memory backends vs context substrates
- [[concepts/deep-agents]] — Long-running autonomous agents that benefit from wiki knowledge
- [[entities/hermes-agent]] — Operates on wiki memory principles with raw articles + entity/concept pages + dreaming
