---
title: "Rabbithole"
type: concept
aliases:
  - rabbithole
  - rabbithole.ing
created: 2026-07-15
updated: 2026-07-15
tags:
  - tool
  - education
  - mcp
  - open-source
  - coding-agents
  - ai-agents
  - frontend
sources:
  - raw/articles/2026-07-13_shloked_rabbithole-infinite-canvas-learning.md
---

# Rabbithole

**Rabbithole** is an open-source infinite canvas for learning, built by [[entities/shlok-khemani|Shlok Khemani]]. It integrates with AI coding agents via an MCP server, enabling agent-assisted exploration of knowledge on a visual canvas.

## Overview

Rabbithole takes the concept of an infinite canvas (like Miro or FigJam) and applies it to AI-augmented learning. Users open documents on the canvas, select text to ask questions, and answers branch out as new documents — creating a visual, non-linear exploration of topics.

## Key Features

- **Infinite canvas UI**: Documents, selections, and answers arranged spatially
- **Selection-based Q&A**: Select text → ask question → answer appears as a new document node
- **Branching exploration**: Answers are documents that can themselves spawn new questions, creating trees of understanding
- **MCP server integration**: Works as an MCP server for Claude Code, Codex, and any MCP-compatible agent
- **Local-first privacy**: API keys stay in your browser; can run entirely on your own machine
- **Self-hostable**: Clone the repo and run locally

## Architecture

- **Browser-based canvas**: The UI runs in the browser
- **MCP server**: Agents connect via the Model Context Protocol to read from and write to the canvas
- **Privacy**: Keys never leave the browser (or your machine when self-hosted)

## Links

- **Web app**: [rabbithole.ing](https://rabbithole.ing)
- **GitHub**: [github.com/shlokkhemani/rabbithole](https://github.com/shlokkhemani/rabbithole)

## Related Pages

- [[entities/shlok-khemani]] — Creator of Rabbithole
- [[concepts/mcp]] — Model Context Protocol, which Rabbithole uses for agent integration
- [[concepts/claude-code]] — Claude Code, one of the agents Rabbithole supports
- [[concepts/ai-for-learning]] — AI-augmented learning approaches
