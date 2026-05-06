---
title: "Flue"
created: 2026-05-06
updated: 2026-05-06
type: entity
tags:
  - entity
  - devtools
  - framework
  - ai-agents
  - open-source
  - typescript
aliases:
  - "Flue.js"
related:
  - [[entities/anthropic]]
  - [[concepts/harness-engineering]]
sources:
  - raw/newsletters/2026-05-05-codex-is-gaining-steam.md
  - https://open.substack.com/pub/bensbites/p/codex-is-gaining-steam
---

# Flue

**Flue** is a **TypeScript framework** for building coding agents in the style of Claude Code. Announced in May 2026, it enables developers to construct agentic workflows that autonomously read, edit, and manage codebases.

## Overview

| Detail | Value |
|--------|-------|
| **Language** | TypeScript |
| **Style** | Claude Code-style agent architecture |
| **Category** | Coding Agent Framework |
| **Announced** | May 2026 (via Ben's Bites) |

## Positioning

Flue enters a rapidly growing ecosystem of agent frameworks:

| Framework | Language | Style |
|-----------|----------|-------|
| **Flue** | TypeScript | Claude Code-style agents |
| **OpenAI Agents SDK** | Python, TypeScript | OpenAI-native agent harness |
| **Claude Code** | TypeScript | Anthropic's CLI coding agent |
| **OpenCode** | Go | Multi-model coding agent CLI |
| **AgentCraft** | TypeScript | RTS-style orchestrator |

### What "Claude Code-Style" Means

Claude Code uses an agent loop where the model:
1. Reads files and codebase context
2. Plans edits (multiple files)
3. Applies changes via tools (bash, edit, write)
4. Iterates based on results and errors

Flue provides this pattern as a reusable framework, allowing developers to build custom coding agents with the same architecture but targeting specific workflows or custom tool integrations.

## Ecosystem Context

The TypeScript coding agent ecosystem is expanding rapidly, driven by:
- **Node.js ecosystem familiarity** among web developers
- **Claude Code** being TypeScript-native (available as both npm package and VS Code extension)
- **OpenAI Agents SDK for TypeScript** launching in May 2026

Flue represents the "framework-ification" of coding agent patterns — moving from proprietary implementations (Claude Code) to reusable building blocks (Flue).

## Related Concepts

- [[concepts/harness-engineering]] — Broader agent execution framework philosophy
- [[entities/anthropic]] — Claude Code (the reference architecture Flue emulates)

## Sources

- [Codex is gaining steam (Ben's Bites)](https://open.substack.com/pub/bensbites/p/codex-is-gaining-steam) — May 5, 2026
