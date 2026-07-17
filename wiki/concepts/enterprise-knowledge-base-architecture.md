---
title: "Enterprise Knowledge Base Architecture"
type: concept
created: 2026-07-17
updated: 2026-07-17
tags:
  - knowledge-management
  - enterprise-ai
  - rag
  - retrieval
  - vector-search
  - lexical-search
  - bm25
  - neural-reranking
  - agentic-rag
  - mcp
  - case-study
  - embeddings
  - coding-agents
  - slack
  - code-intelligence
sources:
  - raw/articles/2026-07-16_cerebras_knowledge-base-architecture.md
  - https://www.cerebras.ai/blog/how-we-built-our-knowledge-base
related:
  - "[[entities/cerebras-systems]]"
  - "[[concepts/rag]]"
  - "[[concepts/wiki-memory]]"
  - "[[concepts/context-engineering]]"
---

# Enterprise Knowledge Base Architecture

Enterprise knowledge bases face a fundamental challenge: information lives wherever it's convenient — Slack threads, code repos, Google Docs, Jira tickets — and centralizing it into a single platform rarely works in practice. The Cerebras Knowledge Base (launched 2026, handling 15,000+ queries/day) demonstrates a **meet-the-data-where-it-lives** architecture that combines hybrid search, LLM-based query planning, and MCP-exposed retrieval primitives.

## Architecture Overview

```
┌─────────────────────────────────────────┐
│            Query Interface               │
│     (Web UI + MCP Tools + Slack Bot)     │
└───────────┬─────────────────────────────┘
            │
┌───────────▼─────────────────────────────┐
│          Planner (LLM)                   │
│   Selects tools & data sources           │
└───────────┬─────────────────────────────┘
            │ Parallel fan-out
    ┌───────┼───────┬───────────┐
    ▼       ▼       ▼           ▼
┌──────┐ ┌──────┐ ┌──────┐ ┌──────────┐
│Search│ │Slack │ │Code  │ │Who Knows │
│(RRF) │ │Search│ │(rg)  │ │          │
└──┬───┘ └──┬───┘ └──┬───┘ └────┬─────┘
   │        │        │          │
   └────────┼────────┼──────────┘
            ▼
┌─────────────────────────────────────────┐
│        Reranker (small model)            │
│     Score 0-10, keep top 10              │
└───────────┬─────────────────────────────┘
            │
┌───────────▼─────────────────────────────┐
│      Synthesis LLM + Context Expansion   │
│   Neighboring sections, citations        │
└─────────────────────────────────────────┘
```

## Core Design Principles

### 1. Meet Data Where It Lives

Instead of forcing all information into one platform (the "single source of truth" dream), the system extracts data from each platform directly:
- **Slack** — Real-time WebSocket ingestion via Socket Mode; thread-aware storage
- **Code repositories** — Language-specific chunking via CocoIndex; incremental re-embedding on commits
- **Custom data sources** — Plugin scripts that emit rows matching the shared embeddings schema

All sources land in a single Postgres table with a uniform schema: embeddings, raw summaries, and metadata.

### 2. Hybrid Search (Multi-Retriever Fusion)

No single search technique is trusted on its own. The Cerebras KB combines four techniques, each compensating for the others' weaknesses:

| Technique | Strengths | Weaknesses |
|-----------|-----------|------------|
| **Full-text search** | Exact tokens (error strings, flag names, host names); Postgres GIN index | Misses paraphrases |
| **Embedding search** | Semantic similarity across vocabulary gaps ("restore hangs" ↔ "checkpoint stalls") | Short messages rank too high; noise from filler text |
| **Inverse document frequency (IDF)** | Separates signal from filler; rare tokens boost relevance | Requires corpus-level statistics |
| **Age decay** | Newer threads outrank stale infrastructure answers | Context-dependent (some knowledge doesn't expire) |

Results are fused via **Reciprocal Rank Fusion (RRF)**: `weight / (60 + rank)` for each list, with smoothing constant 60 to prioritize consensus over single strong votes. After deduplication and per-file result caps, the top 20 candidates go to a small reranker model for final scoring (0-10).

### 3. LLM Distillation Over Raw Embeddings

Slack threads are not embedded directly. Instead, an LLM extracts structured data:
- A searchable one-line question
- A short summary
- The resolution
- Systems and code references mentioned

This normalization step significantly improved accuracy in Cerebras's experiments. The additional metadata provides more useful signal than embedding raw conversational transcripts.

### 4. Bursting for Thread-Level Granularity

Important messages inside long threads can be lost in thread-level summaries. **Bursting** — embedding consecutive runs of messages from the same author — makes individual tangent messages findable. Each burst must clear a quality threshold:
- Contains a rare token (IDF ≥ 4.0)
- Combined burst ≥ 200 characters
- Message reactions provide a social signal boost

### 5. Projects for Scoped Search

As the corpus grows, "search everything everywhere" becomes useless. **Projects** are lightweight named bundles of data sources (Slack channels, repos, databases, docs) relevant to a team. The same source can belong to multiple projects. Default projects assigned during onboarding ensure new engineers get high-signal answers immediately.

## LLM Query Planning

Every query begins with a **planner** — a lightweight LLM pass that selects which tools to invoke:

| Tool | Function |
|------|----------|
| `subsystem_index` | Per-file LLM summaries |
| `search` | Unified vector pipeline (all sources, RRF-fused) |
| `search_slack` | Direct Slack thread retrieval |
| `search_code` | ripgrep over source repositories |
| `recent_prs` | Relevant pull requests |
| `who_knows` | People with demonstrated expertise on a topic |

The planner works from a compact index description — which projects exist, what sources are available, and what each source is good at. Tool calls fan out in parallel, results normalize into a shared evidence schema, and a final synthesis LLM produces the answer with citations.

## MCP Integration

The Cerebras KB exposes each retrieval primitive as an individual **MCP tool** — simple, LLM-free, and deterministic:

- `search_slack` — vector + lexical + IDF + age decay pipeline
- `search_code` — ripgrep with scoring heuristics
- `search` — unified pipeline over all sources
- `who_knows` — expertise graph lookup

Claude Code (or any MCP-compatible agent) becomes the orchestration engine — deciding which tools to call, in what order, and how to assemble results. The retrieval layer itself does not depend on LLM decisions; it returns raw evidence rows.

This is a deliberate inversion: instead of hiding retrieval behind an "answer this question" endpoint, MCP tools give agents direct access to retrieval primitives, keeping the knowledge base fast and cheap to query.

## Web UI vs MCP: Shared Core

Both the Web UI and MCP integration use the same `planner → executor → synthesizer` pattern:

| Component | Web UI | MCP |
|-----------|--------|-----|
| Planner | LLM pass on every query | Agent decides which tools to call |
| Executor | Parallel tool fan-out | Agent calls tools sequentially/parallel |
| Synthesis | Final LLM with citations | Agent assembles evidence into answer |

## Case Study: Cerebras Knowledge Base

- **Scale**: 15,000+ queries/day across data center ops, chip design, hardware, training, inference, cloud
- **Data sources**: Slack (real-time Socket Mode), 40GB+ code repos (CocoIndex), custom databases (plugin scripts)
- **Architecture**: Single Postgres table (embeddings + raw summaries + metadata) as the unified datastore
- **Team**: AI/Growth team at Cerebras (Isaac, Daniel, Zenghao Gao)

See [[entities/cerebras-systems]] for the parent company context.

## Related Concepts

- [[concepts/rag]] — Retrieval-Augmented Generation (parent category)
- [[concepts/wiki-memory]] — Wiki-as-context pattern for agent memory
- [[concepts/context-engineering]] — Discipline of structuring context for agents
- [[concepts/okf-open-knowledge-format]] — OKF structured metadata for knowledge wikis
- [[entities/cocoindex]] — Open-source code embedding framework used by Cerebras

## References

- [Cerebras: How We Built Our Knowledge Base](https://www.cerebras.ai/blog/how-we-built-our-knowledge-base) — July 2026
- Cormack, Clarke, Büttcher — Reciprocal Rank Fusion (SIGIR 2009)
- Anthropic — Contextual Retrieval (2024)
- Anthropic — Code Execution with MCP (2025)
- Cursor — Improving Agent with Semantic Search (2025)
