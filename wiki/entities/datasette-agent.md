---
title: "Datasette Agent"
type: entity
tags:
  - entity
  - ai-agents
  - product
  - tool
  - sqlite
  - model
  - plugins
  - data-science
  - developer-tooling
status: active
description: "Extensible AI assistant for Datasette/SQLite by Simon Willison. Launched May 2026. Conversational interface for querying databases, generating charts, and building plugins. Powered by the LLM Python library."
created: 2026-05-22
updated: 2026-05-22
sources:
  - raw/articles/simonwillison.net--2026-may-21-datasette-agent--9fcb051d.md
  - raw/articles/simonwillison.net--2026-may-21-datasette-agent-2--8297d2dd.md
related: []
---

# Datasette Agent

## Overview

**Datasette Agent** is an extensible AI assistant for [[concepts/datasette]] and SQLite, announced by Simon Willison on May 14, 2026 (0.1a1) and publicly launched on May 21, 2026 (0.1a3). It represents the convergence of Willison's **LLM** Python library (3+ years of development) and **Datasette**, providing a conversational interface for querying structured data stored in Datasette instances.

**Key URLs**: [agent.datasette.io](https://agent.datasette.io) (live demo) | [GitHub](https://github.com/simonw/datasette-agent) | [#datasette-agent Discord](https://discord.gg/datasette)

## How It Works

Datasette Agent provides a chat-based interface where users ask natural-language questions about their data. The agent:

1. Interprets the question
2. Generates appropriate SQL queries against the connected SQLite/Datasette databases
3. Executes queries and returns results in natural language
4. With plugins, can generate charts, visualizations, and more

### Example

From the demo, when asked "when did Simon most recently see a pelican?", the agent generated:

```sql
SELECT title, commentary, created
FROM blog_beat
WHERE beat_type = 'sighting'
AND (title LIKE '%pelican%' OR commentary LIKE '%pelican%')
ORDER BY created DESC
LIMIT 5
```

And correctly responded: "The most recent sighting of a pelican by Simon was recorded on May 20, 2026."

### Live Demo

The [agent.datasette.io](https://agent.datasette.io) demo runs on **Gemini 3.1 Flash-Lite** — chosen for being cheap, fast, and capable of writing reliable SQLite queries. It includes example databases such as WRI's global-power-plants and a Datasette backup of Simon Willison's blog.

## Plugin Architecture

Datasette Agent follows Datasette's plugin model. Three plugins shipped at launch:

| Plugin | Version | Description |
|--------|---------|-------------|
| **datasette-agent-charts** | 0.1a2 | Generates charts from query results |
| **datasette-agent** | 0.1a3 | Core conversational agent |
| **datasette-agent-sprites** | 0.1a0 | Sprite/visual generation |

Plugins can be built using [[entities/claude-code]] or [[entities/openai-codex]] — both are reported to be "excellent at writing plugins" when pointed at the datasette-agent repo for reference.

## Local Model Support

Datasette Agent works with local open-weight models via LM Studio on Mac:

```bash
uvx --prerelease=allow \
  --with datasette-agent --with llm-lmstudio \
  datasette --internal internal.db --root \
  -s plugins.datasette-llm.default_model lmstudio/google/gemma-4-26b-a4b \
  data.db
```

The open-weight models released in the past six months (as of May 2026) are increasingly capable of reliable tool calls and SQL generation required by Datasette Agent.

## Relationship to LLM Library

Datasette Agent has already informed the **LLM 0.32a0 refactor**, a major rework of the LLM Python library. Willison plans to extract "LLM agent" abstractions from Datasette Agent into the core LLM library.

## Future Plans

- **Claude Artifacts-style plugin**: Willison's own take on interactive artifacts within Datasette
- **Personal AI assistant (Claw-like)**: Building a personal AI assistant around data imported from different parts of digital life, revisiting the Dogsheep family of tools
- **Datasette Cloud integration**: Rolling out to Datasette Cloud users
- **Additional plugins**: More prototype plugins beyond the initial three

## Related

- [[entities/datasette-llm-limits]] — Datasette LLM Limits
- [[concepts/datasette]] — Datasette (the underlying platform)
- [[concepts/sqlite]] — SQLite
- [[concepts/llm-python-library]] — Simon Willison's LLM Python library
- [[concepts/ai-agents]] — AI agents concept
- [[concepts/tool-use]] — Tool use in AI agents
