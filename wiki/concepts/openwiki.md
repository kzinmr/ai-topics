---
title: "OpenWiki"
type: concept
created: 2026-07-02
updated: 2026-07-17
tags:
  - coding-agents
  - documentation
  - agent-documentation
  - langchain
  - open-source
  - context-engineering
  - agents-md
  - wiki
  - cli
  - deep-agents
  - knowledge-management
  - okf
related:
  - "[[concepts/okf-open-knowledge-format]]"
  - "[[concepts/wiki-memory]]"
sources:
  - raw/articles/2026-07-01_bracesproul_openwiki-langchain.md
  - raw/articles/2026-07-16_langchain_openwiki-0.2-okf.md
  - https://github.com/langchain-ai/openwiki
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

## Related Pages

- [[concepts/okf-open-knowledge-format]] — OKF spec adopted in OpenWiki 0.2
- [[entities/langchain]] — Parent organization
- [[concepts/agent-documentation]] — Agent documentation patterns
- [[concepts/wiki-memory]] — Wiki-as-context pattern for agent memory
- [[concepts/context-engineering]] — Context engineering discipline
- [[entities/coding-agents]] — Coding agent ecosystem
- [[entities/andrej-karpathy]] — LLM Wiki concept originator
