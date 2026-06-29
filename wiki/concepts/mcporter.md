---
title: MCPorter
created: 2026-06-27
updated: 2026-06-27
type: concept
tags:
  - mcp
  - tool
  - developer-tooling
  - agent-tooling
  - open-source
sources:
  - raw/articles/2026-06-26_openclaw_mcporter-mcp-typescript-tool.md
---

# MCPorter

## Overview

MCPorter is a TypeScript runtime, CLI, and code-generation toolkit for the Model Context Protocol ([[concepts/mcp|MCP]]), created by [[entities/peter-steinberger|Peter Steinberger]] (openclaw / steipete). It enables developers to discover the MCP servers already configured on their system, call them directly from the command line or programmatically, compose richer automations in TypeScript, and mint single-purpose CLIs when they need to share a tool — all without boilerplate or manual schema exploration.

The project was designed to lean into Anthropic's "Code Execution with MCP" guidance, making MCP tool calling practical for both ad-hoc CLI use and production-grade automation. With 4.7k stars, 315 forks, and 42 releases as of June 2026, MCPorter has become one of the most popular tools in the MCP ecosystem. It is MIT-licensed and available via npm (`mcporter`) and Homebrew (`steipete/tap/mcporter`), with a dedicated website at [mcporter.sh](https://mcporter.sh).

MCPorter matters for the MCP ecosystem because it bridges the gap between MCP server configuration (spread across Cursor, Claude, Codex, Windsurf, OpenCode, and VS Code configs) and actual usable tool access. Instead of requiring users to manually set up MCP clients for each tool, MCPorter auto-discovers servers and provides a unified interface for calling them — whether through one-liner CLI commands, typed TypeScript APIs, or generated standalone CLIs.

## Key Features

- **Multi-Editor Config Discovery**: Auto-imports MCP servers from Cursor, Claude Desktop/Code, Codex, Windsurf, OpenCode, and VS Code config files. The `createRuntime()` function merges home config, project config, and editor imports, expands `${ENV}` placeholders, and pools connections for reuse across multiple calls. Config precedence follows import array order.

- **One-Command MCP Calling**: `npx mcporter call server.tool` supports colon-delimited flags, JavaScript-like call syntax, and auto-correction of near-miss tool names. Works via `npx` with zero installation, or global install.

- **Programmatic API**: `createRuntime()` initializes the MCP connection pool; `createServerProxy()` exposes tools as ergonomic camelCase methods, automatically applies JSON-schema defaults, validates required arguments, and returns a `CallResult` with `.text()`, `.markdown()`, `.json()`, `.images()`, and `.content()` helpers.

- **Code Generation**: `mcporter generate-cli` turns any MCP server definition into a standalone TypeScript CLI (with optional Rolldown/Bun bundling). `mcporter emit-ts` emits `.d.ts` type interfaces or ready-to-run client wrappers for strong TypeScript typing without hand-written plumbing.

- **Production Features**: Daemon for keep-alive servers (chrome-devtools, mobile-mcp, etc.) with `start`/`stop`/`restart` lifecycle management; OAuth/token support with automatic credential caching; record/replay fixtures via `mcporter record`/`replay` for deterministic offline debugging and redacted repros; bridge mode (`mcporter serve`) that exposes all daemon-managed servers as one MCP stdio bridge; tool filtering; ad-hoc connections to any MCP endpoint (HTTP or stdio) without touching config.

## Stats

- **Stars**: 4,722
- **Forks**: 315
- **Watchers**: 18
- **License**: MIT
- **Releases**: 42 (latest: v0.12.2, June 27, 2026)
- **Language**: TypeScript (95.3%), JavaScript (4.5%), Shell (0.2%)
- **Distribution**: npm (`mcporter`), Homebrew (`steipete/tap/mcporter`)
- **Website**: [mcporter.sh](https://mcporter.sh)

## See Also

- [[concepts/mcp]]
- [[entities/peter-steinberger]]
- [[concepts/agent-tooling]]
