---
title: "OpenWiki"
type: concept
created: 2026-07-02
updated: 2026-08-27
tags:
  - coding-agents
  - developer-tooling
  - agent-documentation
  - langchain
  - open-source
  - context-engineering
  - agents-md
  - wiki
  - deep-agents
  - search
related:
  - "[[concepts/okf-open-knowledge-format]]"
  - "[[concepts/wiki-memory]]"
sources:
  - raw/articles/2026-07-01_bracesproul_openwiki-langchain.md
  - raw/articles/2026-07-16_langchain_openwiki-0.2-okf.md
  - raw/articles/2026-08-26_langchain_openwiki-wikibench.md
  - https://github.com/langchain-ai/openwiki
  - https://x.com/LangChain/status/2092631796252839949
---

# OpenWiki

## Overview

OpenWiki is an open-source agent and CLI tool developed by [LangChain](../entities/langchain.md) for generating and maintaining documentation wikis for codebases. Released July 2026, it automates the creation of structured repo documentation and keeps it updated as code changes, enabling coding agents to better understand the repos they work in.

## Core Design

OpenWiki addresses a fundamental problem: **agents write better code when they understand the repo**, but documentation is expensive to write and quickly becomes stale. The tool:

1. **Generates** a wiki from the codebase using LLM-powered analysis
2. **Connects** the wiki to coding agents via `AGENTS.md` / `CLAUDE.md` instruction file references
3. **Updates** the wiki incrementally using git diffs via a GitHub Action

### Architecture: Wiki-as-Context

OpenWiki follows a **wiki-as-context** pattern rather than dumping all documentation into a single instruction file:

- The wiki lives as a structured directory of files (potentially hundreds)
- Agent instruction files (`AGENTS.md`, `CLAUDE.md`) contain a **short reference** pointing to the wiki
- Coding agents discover and retrieve relevant wiki pages on demand

This avoids the context-window bloat of embedding all docs in instructions while giving agents structured access to deep repo knowledge.

## Inspiration & Lineage

OpenWiki draws from several predecessors:

| Project | Relationship |
|---------|-------------|
| [DeepWiki](https://deepwiki.com/) | Codebase wiki generator; conceptual predecessor |
| AutoWiki | Automated wiki generation approach |
| [Karpathy's LLM Wiki](../entities/karpathy-ideas.md) | Concept of wiki-structured knowledge for LLMs |
| Factory Wiki | [Factory.ai](https://docs.factory.ai/cli/features/wiki/overview) CLI wiki feature |

## Technical Details

- **Built on**: [DeepAgents](https://docs.langchain.com/oss/python/deepagents/overview) (LangChain's agent framework)
- **Install**: `npm install -g openwiki`
- **Init**: `openwiki --init` (prompts for model provider + API key)
- **Supported providers**: OpenRouter, Fireworks, Baseten, OpenAI, Anthropic
- **Default**: OpenRouter with an open model
- **Tracing**: LangSmith integration for inspecting agent runs
- **CI/CD**: GitHub Action for scheduled wiki updates (checks git diffs since last run)

## OpenWiki 0.2 — OKF Integration (July 2026)

OpenWiki 0.2 adopts **[[OKF (Open Knowledge Format)|concepts/okf-open-knowledge-format]]**, a proposed standard from Google Cloud for structuring knowledge wikis. This brings structured metadata to generated documentation:

### What Changed

- **YAML frontmatter** — Every wiki page now includes `type`, `title`, `description`, `tags`, and `resource` fields, following the OKF spec
- **`index.md` conventions** — Directory summaries are generated from frontmatter descriptions, enabling deterministic navigation
- **`logs.md` changelog** — An append-only change log tracks each run's updates, so agents and developers can see what changed without re-reading the full wiki

### Agent Retrieval Impact

OKF structured metadata enables **deterministic search** — agents can filter by type, category, or tag rather than relying entirely on open-ended semantic search. This is both faster and cheaper for simple lookups while keeping agentic search available for complex queries.

### Ecosystem Compatibility

Because OKF is an open format, OpenWiki wikis work with community-built viewers, renderers, linters, and Google's open-source wiki visualizer. This replaces one-off integrations with a standardized, interoperable documentation layer.

## Relation to Agent Documentation Patterns

OpenWiki operationalizes the pattern where [coding agents](../concepts/coding-agents.md) use instruction files as entry points:

- `AGENTS.md` / `CLAUDE.md` → pointer to wiki context
- Wiki pages → structured, searchable, maintainable documentation
- GitHub Action → automated freshness guarantee

This is complementary to [[concepts/context-engineering]] — OpenWiki generates the context that agents consume.

## Evaluation: WikiBench (Aug 2026)

LangChain built **WikiBench**, a benchmark for measuring whether a generated wiki actually helps coding agents — and whether OpenWiki itself is improving. The motivation is twofold: (1) does a wiki genuinely help coding agents, and (2) do changes to OpenWiki actually make it better?

### Design: Reader-Agent Verifier

WikiBench runs on **Harbor**, a framework for evaluating agents on long-running tasks. A Harbor task has three components — environment, agent, verifier:

- **Environment**: a repository checked out at a pinned commit
- **Agent**: runs OpenWiki initialization on that repo and produces the initial wiki
- **Verifier**: a "reader agent" that attempts to answer questions about the repository, using the generated wiki (sometimes with source code, sometimes by itself). The wiki is judged by how much it actually helps the reader agent on real tasks.

This framing is key: it also lets them test whether the wiki helps *at all* by giving the reader agent the raw source directly and asking it to answer the same questions.

### Question Generation

Questions are generated automatically against the pinned commit, by identifying larger thematic areas (packages, subsystems). Two types:

- **Coverage questions** — a shared template: "I need to make a change to how [area] works. Where in this repository does that live, what does it interact with that I should know about before touching it, and how would I check I didn't break something?"
- **Retrieval questions** — written individually around specific behavior (e.g., "A tool call in a Deep Agents run returns far more output than fits in context. What does the model actually receive in place of it, where does the real content go, and how is that path different from what happens when the whole conversation grows too large?").

Each question ships with a JSON rubric: a list of facts the answer should contain.

### Scoring

A series of LLM judges score each fact in the rubric:
1. One judge checks whether the fact is **present** in the answer.
2. A second judge checks whether the fact is **grounded** in pages the agent actually read.

An answer earns credit only if it is both correct *and* grounded. The per-question score is the fraction of facts correct (e.g., 3 of 5 → 0.6); the overall wiki score is the average across all questions.

### Results

**Benchmarking different harnesses** — three harnesses (Bare DeepAgents, OpenWiki 0.2.5, OpenWiki 0.3.0) compared. High-performing runs diverge widely in cost and time: GLM 5.2 at $9.18 / 50 min vs Luna at $0.44 / 11 min. DeepSeek Flash and GLM 5.2 both perform well but at very different cost points (Flash ~1/6 the cost of GLM 5.2).

**Where the extra cost/time goes** — DeepSeek and GLM read roughly **3× as many files** as Luna but write only **1.2–1.5× as many pages**. Their extra work goes into understanding more of the repository, not producing more output.

**Does the wiki help?** — the reader agent was run under three setups:
1. Wiki only
2. Source (raw code) only
3. Both

**Combining wiki + source produced the highest mean score at lower cost than source alone.** The wiki acts as an **index**: it gives the reader a starting point instead of making it reconstruct the repository from scratch. The wiki *alone* performed much worse — it works best as a **guide, not a replacement** for the source. Together, the wiki and source made the reader both more accurate and more cost-efficient.

### Why It Matters

WikiBench is a reusable signal: because the verifier is a reader agent, the same benchmark measures both the *value* of a wiki (vs. raw source) and the *quality delta* between wiki versions. LangChain uses it actively to guide OpenWiki development. It extends the "standardized internal evals" direction Harrison Chase outlined for the LangChain ecosystem (see [[entities/langchain]]).

## Related Pages

- [[concepts/okf-open-knowledge-format]] — OKF spec adopted in OpenWiki 0.2
- [[entities/langchain]] — Parent organization
- [[concepts/agent-documentation]] — Agent documentation patterns
- [[concepts/wiki-memory]] — Wiki-as-context pattern for agent memory
- [[concepts/context-engineering]] — Context engineering discipline
- [[entities/coding-agents]] — Coding agent ecosystem
- [[entities/andrej-karpathy]] — LLM Wiki concept originator
