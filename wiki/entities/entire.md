---
title: Entire
type: entity
created: 2026-05-08
updated: 2026-05-08
status: L2
tags:
  - company
  - coding-agents
  - infrastructure
  - search
  - protocol
website: https://entire.io
github: https://github.com/entireio
sources:
  - https://entire.io
  - [[raw/articles/2026-05-06_entire-improving-agentic-search-in-coding-agents]]
aliases: [entire.io, Entire Inc, entireio]
---

# Entire — AI Agent Observability & Search

Entire is a company building infrastructure for AI agent observability and search. Its core product captures AI agent traces (called **checkpoints** — containing user prompts, agent responses, tool calls, and code diffs) and makes them searchable and shareable across agents and teammates.

## Core Products

| Product | Description |
|---------|-------------|
| **Entire Platform** | Agent trace capture, search, and sharing (hundreds of thousands of checkpoints collected) |
| **Entire CLI** | Open-source CLI for agent interaction ([github.com/entireio/cli](https://github.com/entireio/cli)) |
| **pgr** | Open-source Rust MCP agentic search tool — definitions-first, path-aware ranking ([github.com/entireio/pgr](https://github.com/entireio/pgr)) |

## Key Research

Entire published a landmark study (May 2026) on agentic code search, analyzing 1,983 real coding-agent checkpoints (~202K tool calls) from their open-source `entireio/cli` repo:

- **48.8% of all agent tool calls are search-related**
- **Faster search (fff: 14.7ms → 1.7ms) only modestly improves end-to-end (38.57s → 36.99s)**
- **Better ranking (pgr) improves first-query Hit@1 from 26% → 34% (implementation tasks: 14.3% → 42.9%)**
- **Tool execution is only ~0.4% of total agent wall clock** — the bottleneck is model inference + planning, not search speed

This research is one of the first public, data-driven analyses of how coding agents spend their time and what actually improves their effectiveness.

## People

- **Evis Drenova** — Author of the agentic search study
- See: [[entities/evis-drenova]]

## See Also

- [[concepts/pgr]] — The agentic search tool built by Entire
- `fff` — Fast indexed MCP search server by Dmitry Kovalenko
- `ripgrep` — Baseline grep tool
