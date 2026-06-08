---
title: "Sentra.app"
type: entity
created: 2026-05-12
updated: 2026-05-19
tags:
  - company
  - memory-systems
  - ai-agents
  - rag
aliases: ["Sentra", "sentra-app"]
sources:
  - https://sentra.app
  - raw/articles/2026-05-17_rent-intelligence-own-context.md
---

# Sentra.app

| | |
|---|---|
| **Website** | [sentra.app](https://sentra.app) |
| **Founded** | 2024 |
| **Founders** | Jae Gwan Park (CEO), Andrey Starenky (CTO), [[entities/ashwingop]] |
| **Funding** | $5M Seed (a16z Speedrun, Together Fund) |
| **HQ** | Palo Alto, CA |
| **Category** | Enterprise General Intelligence (EGI) |

## Overview

Sentra.app is an Enterprise General Intelligence (EGI) platform that builds a **collective memory** for organizations. Rather than treating AI as a separate tool, Sentra integrates with existing workflows (Slack, Jira, meetings) to create a living, searchable knowledge graph that learns what matters based on use.

The platform's architecture is heavily inspired by the **Reflexion** paper (NeurIPS 2023), co-authored by co-founder Ashwin Gopinath, which demonstrated how AI agents can improve through verbal self-reflection on their mistakes. Sentra scales this principle from a single agent to an entire organization — building systems that don't just store information, but learn what matters, surface the right context at the right time, and evolve as the organization does.

Raised $5M seed in 2026, backed by **a16z Speedrun** and **Together Fund**.

## Core Features

1. **Searchable Memory** — Every meeting, message, and document becomes a living record searchable instantly
2. **Risk Awareness** — Conflicting priorities and missed commitments are flagged before they become real problems
3. **Autonomous Agents** — Weekly reports, meeting prep, follow-ups handled by AI agents
4. **Smarter Meeting Notes** — Real-time capture, structure, and enrichment of meeting notes
5. **Business Reviews** — On-demand weekly summaries of team activity
6. **Decision Timeline** — Persistent history of every decision and commitment

## Architecture

Sentra's key architectural principle: **memory as shared state, not memory as a service**. This aligns with [[entities/ashwingop]]'s [[concepts/contextmaxxing]] thesis — the company needs one unified substrate rather than fragmented per-tool memory.

The platform implements:
- **Knowledge Graph** — Dynamic graph of entities, relationships, events, decisions
- **Ontology Layer** — Rules for what kinds of things exist, how they relate, what they mean
- **Context Graph** — Shaped by ontology, exposing what matters for each query
- **Agent Integration** — Agents act from the shared state rather than local memory

## Security & Deployment

- SOC 2 and ISO 27001 compliant
- On-premise / isolated VPC / air-gapped deployment options
- Data never leaves customer infrastructure for sensitive deployments

## Related Concepts

- [[concepts/contextmaxxing]] — The architectural philosophy behind Sentra's memory design
- [[concepts/context-lock-in]] — The competitive risk Sentra solves: enterprises that outsource context to model vendors face irreversible lock-in. Sentra provides the neutral, owned context layer. [[entities/ashwingop]]'s thesis: "Rent the Intelligence. Own the Context."
- [[concepts/tokenmaxxing]] — The approach Sentra explicitly counters with shared state
- [[entities/ashwingop]] — Co-founder and architectural visionary

## Sources

- [Sentra.app](https://sentra.app) — Official website
- [Sentra.app Raises $5M](https://finance.yahoo.com/news/sentra-app-raises-5m-build-170000454.html) — Yahoo Finance (2026)
- [Rent the Intelligence. Own the Context.](https://x.com/i/article/2056142316713472000) — Ashwin Gopinath, X Article (May 17, 2026). Framing of Sentra as the neutral context layer: "A company brain, like the one we are building at Sentra, is the memory infrastructure that lets humans and agents act from the same organizational state." [[raw/articles/2026-05-17_rent-intelligence-own-context.md|Raw article]]
