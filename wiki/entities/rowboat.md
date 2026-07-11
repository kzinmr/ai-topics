---
title: Rowboat
created: 2026-07-10
updated: 2026-07-10
type: entity
tags: [open-source, tool, local-first, claude-code, product, agent-platform, ai-agents, coding-agents, memory-systems, knowledge-graph, typescript, hn-popular, multi-agent, mcp]
sources: [raw/articles/2026-07-10_rowboat-claude-desktop-alternative.md]
---

## Overview

Rowboat is an open-source, local-first desktop AI coworker with persistent memory, developed by Rowboat Labs. It is positioned as an alternative to [[entities/anthropic]]'s proprietary Claude Desktop, offering a local-first architecture where all data lives on the user's machine as plain Markdown files. The project was featured on Hacker News as a Show HN on July 7, 2026, earning 216 points, and has rapidly grown to over 16,000 GitHub stars and 1,600 forks.

Rowboat indexes a user's work — email, meetings, Slack conversations, and assistant interactions — into a living, backlinked knowledge graph inspired by Obsidian. This knowledge graph serves as long-lived memory that compounds over time, contrasting with most AI tools that reconstruct context on demand from transcripts or documents.

The application is built primarily in TypeScript (97.1%) and is licensed under Apache 2.0. It is available for macOS, Windows, and Linux.

## Key Features

### Brain — Knowledge Graph Memory
Rowboat's core innovation is its "Brain": a persistent knowledge graph that indexes all work artifacts (emails, meetings, Slack, assistant conversations) into an Obsidian-style backlinked system. Unlike ephemeral context windows, relationships are explicit, inspectable, and manually editable — everything lives on disk as plain Markdown.

### Built-in Work Surfaces
Rowboat includes several integrated work surfaces for human-AI collaboration:
- **Email Client**: Sorts emails by importance and auto-drafts responses using full work context
- **Meeting Notes**: Local meeting note-taker using mic/speaker capture, producing live transcripts and Markdown summaries that update the knowledge graph
- **Browser**: An isolated built-in browser for collaborative web tasks, sandboxed from the user's main browser
- **Code Mode**: Parallel coding agents driven by [[entities/claude-code]] or [[entities/codex]] with all work context available
- **Apps**: Extensible work surfaces users can build themselves, with access to all tools and integrations

### Background Agents
Users can configure background agents that trigger on events (e.g., new email) or run on schedules. Agents can connect to tools, search the web, use the browser, and write code via Claude Code or Codex.

### Model Flexibility
Rowboat supports bring-your-own-model:
- Local models via Ollama or LM Studio
- Hosted models with user-provided API keys
- Model swapping at any time without data migration

### MCP Integration
Full [[concepts/mcp]] (Model Context Protocol) support allows connection to external tools and services: Exa (web search), Twitter/X, ElevenLabs (voice), Slack, Linear/Jira, GitHub, and more.

### Local-First Design
All data stored locally as plain Markdown with no proprietary formats or lock-in. Users can inspect, edit, back up, or delete everything at any time — a core tenet of [[concepts/local-first-software]].

## Technical Architecture

Rowboat is structured as a monolithic desktop application with multiple integrated subsystems:

- **Frontend**: TypeScript-based desktop UI, likely using Electron (given `build-electron.sh` and `Dockerfile.qdrant`)
- **Knowledge Graph**: Qdrant vector database for semantic search (Docker Compose includes `Dockerfile.qdrant`), combined with Markdown-based persistence
- **Integrations**: One-click connections to popular products (Gmail, Calendar, Drive, Slack)
- **Voice**: Optional Deepgram (voice input) and ElevenLabs (voice output)
- **External Tools**: MCP server support and Composio tool integration

The repository uses Docker Compose for orchestration, with `start.sh` as the primary launcher. The architecture prioritizes local execution with no cloud dependency for core functionality.

## Comparison to Claude Desktop

Rowboat is explicitly positioned as an open-source alternative to [[entities/anthropic]]'s Claude Desktop. Key differentiators:

| Dimension | Rowboat | Claude Desktop |
|-----------|---------|----------------|
| **License** | Apache 2.0 (open-source) | Proprietary |
| **Data Storage** | Local Markdown files | Cloud-based |
| **Memory Model** | Persistent knowledge graph (compounds over time) | Session-based context |
| **Model Provider** | BYO model (Ollama, LM Studio, API keys) | Anthropic models only |
| **Extensibility** | MCP, built-in App builder, open-source | MCP support |
| **Work Surfaces** | Email, browser, meeting notes, code mode built-in | Primarily chat/code focused |
| **Background Agents** | Event-driven + scheduled | Limited |
| **Pricing** | Free / self-hosted | Paid subscription |

## Status

Rowboat is under active development with 2,015+ commits as of July 2026. The project has strong community momentum: 16k stars, 1.6k forks, 65 open issues, and 47 open pull requests. Downloads are available for macOS, Windows, and Linux from the GitHub releases page.

The project maintains an active Discord and Twitter presence for community engagement.

## Related Pages

- [[entities/claude-code]] — Primary coding agent used within Rowboat's Code Mode
- [[entities/anthropic]] — Company behind Claude Desktop, which Rowboat competes with
- [[concepts/mcp]] — Model Context Protocol used for Rowboat's extensibility
- [[concepts/open-source]] — Rowboat's licensing and development philosophy
- [[concepts/local-first-software]] — The architectural philosophy Rowboat embodies
- [[concepts/knowledge-graph-memory-agents]] — The memory paradigm Rowboat implements
- [[concepts/ai-agent-memory]] — Broader context on agent memory systems
- [[concepts/ai-agents]] — The agent ecosystem Rowboat participates in
- [[entities/codex]] — Alternative coding agent supported in Code Mode
