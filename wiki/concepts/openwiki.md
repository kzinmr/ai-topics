---
title: "OpenWiki"
type: concept
created: 2026-07-02
updated: 2026-07-02
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
sources:
  - raw/articles/2026-07-01_bracesproul_openwiki-langchain.md
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

## Relation to Agent Documentation Patterns

OpenWiki operationalizes the pattern where [coding agents](../concepts/coding-agents.md) use instruction files as entry points:

- `AGENTS.md` / `CLAUDE.md` → pointer to wiki context
- Wiki pages → structured, searchable, maintainable documentation
- GitHub Action → automated freshness guarantee

This is complementary to [[concepts/context-engineering]] — OpenWiki generates the context that agents consume.

## Related Pages

- [[entities/langchain]] — Parent organization
- [[concepts/agent-documentation]] — Agent documentation patterns
- [[concepts/context-engineering]] — Context engineering discipline
- [[concepts/coding-agents]] — Coding agent ecosystem
- [[entities/andrej-karpathy]] — LLM Wiki concept originator
