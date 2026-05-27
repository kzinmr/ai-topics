---
title: "OpenClaw Ecosystem Tools"
type: concept
aliases:
  - openclaw-ecosystem
  - openclaw-mcp-tools
  - steipete-tools
created: 2026-04-18
updated: 2026-04-18
tags:
  - concept
  - openclaw
  - mcp
  - developer-tooling
  - ecosystem
related:
  - concepts/openclaw/_index
  - entities/peter-steinberger
  - concepts/mcp-model-context-protocol
sources:
  - "https://github.com/steipete"
  - "elvis analysis (April 2026)"
---

# OpenClaw Ecosystem Tools

An **MCP-first developer tool ecosystem** built by Peter Steinberger (@steipete). OpenClaw at its core, with multiple CLI/MCP servers working together in an interconnected structure.

## Tool List

### Core Frameworks

| Tool | Description | Stars | URL |
|--------|------|-------|-----|
| **OpenClaw** | Personal AI agent framework. Telegram/Discord integration, resident agent | 135k+ instances | github.com/steipete/openclaw |
| **NemoClaw** | NVIDIA's enterprise OpenClaw wrapper (OpenShell sandbox, Landlock, seccomp) | — | github.com/NVIDIA/OpenClaw |

### MCP Servers

| Tool | Description | Stars |
|--------|------|-------|
| **Peekaboo** | macOS CLI + MCP server. Screenshot capture for AI agents | 3.1k |
| **mcporter** | Call MCP from TypeScript, packaged as CLI | 3.8k |
| **gogcli** | Google Suite CLI（Gmail, GCal, GDrive, Google Contacts） | 6.7k |
| **Terminator MCP** | "I'll be back... with your terminal output!" Returns terminal output to agents | — |

### Developer Utilities

| Tool | Description | Stars |
|--------|------|-------|
| **VibeTunnel** (vt.sh) | Turn any browser into a terminal. Remote agent control | — |
| **CodexBar** | OpenAI Codex / Claude Code usage stats (no login required) | 9.9k |
| **agent-rules** | Rules and knowledge base for Claude Code / Cursor | 5.7k |
| **tokentally** | Lightweight library for LLM token + cost calculation | — |
| **whatmodelispeterusing.com** | Tracks which model Steinberger is currently using | — |

### Legacy

| Tool | Description | Stars |
|--------|------|-------|
| **Aspects** | AOP (Aspect-Oriented Programming) library for Objective-C / Swift | 8.4k |
| **InterposeKit** | Modern Swift method swizzling library | — |
| **PSPDFKit** | Mobile PDF SDK (used inside Apple, deployed to 1B+ devices) | — |

## Architecture Principles

### MCP-First Design
Steinberger's ecosystem is designed around **Model Context Protocol (MCP)**:
- Each tool operates as an independent MCP server
- OpenClaw integrates these MCP servers
- Also usable directly via CLI (packaged through mcporter)

### Composable Tools
> "You don't even need to use OpenClaw to benefit from OpenClaw — the patterns will show up in everything downstream for years." — elvis

Individual tools are usable without depending on OpenClaw. Examples:
- Peekaboo standalone as a screenshot MCP
- gogcli standalone as a Google Suite CLI
- CodexBar standalone for usage visualization

### Login-Free Philosophy
Tools that require **no login** (CodexBar, VibeTunnel, etc.) are prioritized. Authentication flows become bottlenecks when agents operate autonomously.

## ClawHub Marketplace

OpenClaw skill extensions are distributed through **ClawHub**:
- New skills are first submitted to ClawHub
- Adding to core requires "strong product or security justification"
- Users install as needed
- Loaded according to the Five-Tier Skill Precedence model

## Related Pages

- [[concepts/openclaw]] — OpenClaw concept aggregation
- [[concepts/openclaw/five-tier-precedence]] — Skill priority model
- [[entities/peter-steinberger]] — Developer
-  — Model Context Protocol- [[entities/nvidia-nemoclaw]] — NVIDIA enterprise edition
- [[concepts/local-first-software]] — Local-first software movement
