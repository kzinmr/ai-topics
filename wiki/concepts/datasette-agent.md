---
title: datasette-agent
type: concept
created: 2026-05-25
updated: 2026-05-25
tags:
  - ai-agents
  - datasette
  - tool
  - database
  - sqlite
  - open-source
  - plugins
sources:
  - raw/articles/simonwillison.net--2026-may-24-datasette-agent--ec49f1cf.md
---

# datasette-agent

**datasette-agent** is an AI agent plugin for [[entities/datasette|Datasette]] that enables natural language interaction with SQLite databases. It integrates directly into the Datasette UI, allowing users to ask questions and explore data conversationally through an agent chat interface.

| | |
|---|---|
| **Repository** | [simonw/datasette-agent](https://github.com/simonw/datasette-agent) |
| **Latest Release** | 0.1a4 (May 2026) |
| **Created by** | [[entities/simon-willison|Simon Willison]] |
| **Live Demo** | [agent.datasette.io](https://agent.datasette.io) |

## Features

### Jump to Menu Integration (0.1a4)

The latest release takes advantage of Datasette 1.0a30's new `makeJumpSections()` JavaScript plugin hook. Pressing `/` in Datasette now shows a "Start a new agent chat" option in the Jump to menu, providing instant access to the AI agent from anywhere in the Datasette interface.

### GitHub Auth
Users sign into [agent.datasette.io](https://agent.datasette.io) using their GitHub account.

## Ecosystem Context

datasette-agent is part of the Datasette plugin ecosystem, alongside:
- **[[entities/datasette|Datasette]]** — The open-source multi-tool for exploring and publishing data (SQLite-backed)
- **datasette-fixtures** — Plugin for test fixture databases (0.1a0, May 2026)
- **datasette-llm-limits** — LLM rate limiting for Datasette

## Related

- [[entities/datasette]] — The parent project
- [[entities/simon-willison]] — Creator of Datasette and datasette-agent
- [[concepts/ai-agents]] — Broader AI agent ecosystem
