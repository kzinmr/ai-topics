---
title: Vincent Warmerdam
type: entity
created: 2026-05-20
updated: 2026-05-20
tags:
  - person
  - open-source
  - developer-tooling
  - harness-engineering
  - ai-agents
aliases:
  - Koaning
  - @koaning
sources:
  - raw/newsletters/2026-05-20-agent-harness-ipynb.md
  - https://open.substack.com/pub/hugobowne/p/agent-harnessipynb
---

# Vincent Warmerdam (@koaning)

**Vincent Warmerdam** is an Engineer at **marimo** (the reactive Python notebook platform) and a prominent voice in agentic notebook workflows. He previously worked as a Research Scientist at Rasa and created the popular "Calm Code" philosophy for building with AI agents.

## Overview

Warmerdam operates at the intersection of data science tooling, notebook environments, and AI agent workflows. His work at marimo focuses on building a reactive notebook platform that natively supports agent collaboration — where agents and humans share a live editing canvas.

## Key Contributions

### Agent-Harness.ipynb (May 2026)

In conversation with Hugo Bowne-Anderson (Vanishing Gradients podcast), Warmerdam shared deep insights on agent notebook workflows:

| Insight | Detail |
|---------|--------|
| **Shared notebook canvas** | marimo as agent-human co-existence environment — agents and humans edit the same cells |
| **marimo linter fix rate** | Dedicated linter solved ~60% of agent errors overnight |
| **Incremental generation** | Agents generate one to two cells at a time, not entire notebooks |
| **Speed models for exploration** | Faster open-weight models (Kimi K2) enhance exploratory flow, reducing iteration friction |
| **Pi agent harness** | Agents extend themselves rather than reaching for MCP — harness-first philosophy |
| **Calm as a tool** | "Calm is the most underrated tool for building well" |

### marimo Platform

marimo is an open-source reactive notebook for Python — reproducible, Git-friendly, deployable as interactive apps. Key features for agent workflows:
- Cells automatically rerun when dependencies change
- No hidden state — every cell's output reflects its current code
- Native support for collaborative editing via agents

### Rasa Research

At Rasa, Warmerdam worked on conversational AI and dialogue systems — foundational experience that informs his perspective on agent-human interaction patterns.

## Philosophy

Warmerdam advocates for:
- **Calm engineering** — building with intention, not velocity
- **Incrementalism** — agents should make small, verifiable changes
- **Co-existence over replacement** — agents augment, not replace, the developer's cognitive process

## Related

- [[entities/hugo-bowne-anderson]] — Host of Vanishing Gradients podcast; conversation partner for Agent-Harness.ipynb
- [[entities/marimo]] — Marimo reactive notebook platform
- [[concepts/agent-harness]] — Agent harness engineering
- [[concepts/notebook-agents]] — Notebook-native agent workflows
