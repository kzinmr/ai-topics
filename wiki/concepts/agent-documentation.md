---
title: "agent-documentation"
type: concept
aliases:
  - agent-documentation
created: 2026-04-25
updated: 2026-07-02
tags:
  - concept
  - coding-agents
  - documentation
  - context-engineering
  - agents-md
sources:
  - raw/articles/2026-07-01_bracesproul_openwiki-langchain.md
  - https://x.com/karpathy/status/2040470801506541998
---

# Agent Documentation

## Overview

Agent documentation refers to the practice of creating and maintaining structured documentation that enables AI coding agents to understand codebases. As agents take on larger roles in software engineering, the quality and freshness of repo documentation directly impacts agent effectiveness.

## Key Insight

> Agents write better code when they understand the repo they're working in. They need to know where key logic lives, how files connect, and which patterns the codebase expects.

Documentation serves as **durable context** for agents — it persists across sessions and scales beyond what can fit in a single instruction file.

## Approaches

### Instruction Files (`AGENTS.md`, `CLAUDE.md`)

Most coding agents read instruction files like `AGENTS.md` or `CLAUDE.md` for repo-specific guidance. These files are useful for high-level instructions and conventions, but they are **not the right place** to store hundreds of pages of repo documentation. They should instead **point** to structured documentation.

### Wiki-as-Context Pattern

The wiki-as-context pattern separates concerns:
- **Instruction files** → short pointers to documentation
- **Wiki pages** → structured, searchable, maintainable documentation
- **Automated updates** → CI/CD keeps docs fresh as code changes

This pattern was pioneered by projects like DeepWiki, Karpathy's LLM Wiki concept, and most recently [OpenWiki](openwiki.md).

## Tools

| Tool | Approach |
|------|----------|
| [OpenWiki](openwiki.md) | LangChain's open-source agent/CLI; generates wiki, connects via AGENTS.md/CLAUDE.md refs, GitHub Action for updates |
| DeepWiki | Codebase wiki generator |
| Factory Wiki | Factory.ai CLI wiki feature |
| Karpathy's LLM Wiki | Concept of wiki-structured knowledge for LLMs |

## Related Pages

- [[concepts/openwiki]] — Primary tool implementation
- [[concepts/context-engineering]] — Broader discipline of context design for agents
- [[entities/coding-agents]] — Coding agent ecosystem
- [[concepts/agentic-engineering]] — Agent engineering practices
- [[entities/andrej-karpathy]] — LLM Wiki concept originator
