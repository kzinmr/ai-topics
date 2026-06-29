---
title: "OpenKnowledge"
created: 2026-06-28
updated: 2026-06-28
type: entity
tags:
  - open-source
  - tool
  - information-retrieval
  - agent-platform
  - mcp
  - product
  - claude-code
  - coding-agents
related:
  - [[concepts/mcporter]]
  - [[concepts/skill-architecture-patterns]]
  - [[entities/cursor-ai]]
  - [[concepts/claude-code/claude-code-skills]]
  - [[concepts/agent-skills]]
sources:
  - raw/articles/2026-06-28_inkeep-openknowledge-ai-knowledge-tool.md
---

# OpenKnowledge

OpenKnowledge is an open-source, AI-native markdown editor and knowledge management platform that integrates directly with coding agent harnesses including [[entities/claude-code|Claude Code]], [[entities/openai-codex|Codex]], and [[entities/cursor-ai|Cursor]]. It positions itself as an open-source alternative to Notion and Obsidian for AI-augmented knowledge work.

## Overview

- **Website**: https://openknowledge.ai
- **GitHub**: https://github.com/inkeep/open-knowledge
- **License**: GPL-3.0-or-later
- **HN Points**: 373 (June 25, 2026)
- **Platform**: macOS app + web UI + CLI (Node.js 24+)

## Key Features

### WYSIWYG Markdown Editor
Full what-you-see-is-what-you-get editing that makes markdown files feel like a Google Doc or Notion page, while remaining plain markdown on disk.

### AI Harness Integration
Collaborative AI-editing with Claude, Codex, and Cursor desktop apps. Can be used with any harness or agent via [[concepts/model-context-protocol-mcp|MCP]]/CLI, including OpenCode. Out-of-the-box MCP, skills, and agentic search capabilities.

### Git-Native Sharing
No-code team sharing and auto-sync powered by git/GitHub — changes are automatically committed and synced. This makes it compatible with existing git-based wiki workflows.

### Rich Components
Embeddable HTML and rich components for engineering specs and visualized reports. Built-in TUI and Web UI for terminal users.

## Relevance to AI Topics Wiki

OpenKnowledge is directly relevant as:

1. **AI-native knowledge management**: Built from the ground up for LLM wiki workflows, agent second brains, and knowledge graphs — the same use case as this wiki.
2. **Multi-harness integration**: One of the first open-source tools to integrate with Claude Code, Codex, and Cursor simultaneously, reflecting the [[concepts/meta-harness|meta-harness]] trend.
3. **MCP-first architecture**: Ships with MCP support out of the box, aligning with the broader [[concepts/model-context-protocol-mcp|MCP ecosystem]].
4. **Skills architecture**: Supports agent [[concepts/agent-skills|skills]] similar to Claude Code Skills, Warp Skills, and Hermes skills — connecting to [[concepts/skill-architecture-patterns|skill architecture patterns]].

## Comparison

| Aspect | OpenKnowledge | Obsidian | Notion |
|--------|---------------|----------|--------|
| AI integration | Native (Claude/Codex/Cursor) | Via plugins | Built-in AI |
| License | GPL-3.0 | Proprietary | Proprietary |
| Data format | Plain markdown | Plain markdown | Proprietary |
| Agent harness support | First-class (MCP/CLI) | None | None |
| Git-native sync | Yes (auto) | Via plugin | No |

## See Also
- [[concepts/mcporter]] — TypeScript MCP toolkit
- [[concepts/skill-architecture-patterns]] — Comparison of skill architectures
- [[concepts/agentic-knowledge-work]] — Agent-centric knowledge work paradigm
- inkeep — Creator organization (page pending — no entity page exists yet)
