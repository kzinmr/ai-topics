---
title: "Unlocking the Codex harness: how we built the App Server"
source_url: "https://openai.com/index/unlocking-the-codex-harness/"
source_type: "blog-post"
author: "Celia Chen"
publication: "OpenAI Blog"
date: "2026-02-04"
tags: ["codex", "openai", "protocol", "api", "agent-architecture", "coding-agents"]
---

# Unlocking the Codex harness: how we built the App Server

*By Celia Chen, February 4, 2026*

## What is the Codex App Server?

A client-friendly, bidirectional **JSON-RPC API** that exposes the full **Codex harness**—the agent loop, configuration, tool execution, and persistence—to any product or integration. Surfaces powered: Web app, CLI, IDE extension (VS Code), macOS app, and partner IDEs (Xcode, JetBrains). All Codex experiences share the same underlying agent loop, now accessible via a stable protocol.

## Origin Story

- Originally built to **reuse the Codex harness** between the CLI (TUI) and the VS Code extension without re-implementing the agent loop.
- Early attempts with MCP server were **abandoned**; a JSON-RPC protocol that mirrored the TUI loop became the first unofficial App Server.
- At the time, **"we didn't expect other clients to depend on the App Server, so it wasn't designed as a stable API."**
- As adoption grew, internal teams and external partners (JetBrains, Xcode, desktop app) needed a stable, backward-compatible API.

## Architecture

### Codex Core (the harness)
A library + runtime that runs the core agent loop and manages persistence for one thread:
1. Thread lifecycle & persistence (create, resume, fork, archive)
2. Config & auth (loading config, "Sign in with ChatGPT", credential state)
3. Tool execution & extensions (shell/file sandbox, MCP servers, skills, policy model)

### App Server Components (long-lived process)
- **Stdio Reader**: translation layer for JSON-RPC over stdio
- **Codex Message Processor**: translates client requests into Codex core operations and transforms internal events into stable notifications
- **Thread Manager**: spins up one core session per thread
- **Core Threads**: actual agent loop executions

## Three Integration Patterns

### a) Local Apps & IDEs
Binary bundled with platform-specific binary, launched as child process, bidirectional stdio channel. Partners decouple release cycles by keeping client stable while pointing to newer App Server binary.

### b) Web Runtime
Worker provisions a container, launches App Server inside it, browser communicates via HTTP + SSE. Browser-side UI stays lightweight; server is source of truth for long-running tasks.

### c) Remote Control
Additional experimental transport allowing clients to connect to a running App Server over WebSocket or Unix socket.

## Three Core Primitives

| Primitive | Definition |
|-----------|-----------|
| **Item** | Atomic unit of input/output (typed: user message, agent message, tool execution, approval request, diff). Lifecycle: started → delta (streaming) → completed |
| **Turn** | One unit of agent work triggered by user input; contains sequence of items. Begins with turn/started, ends with turn/completed |
| **Thread** | Durable container for a Codex session; contains multiple turns. Created, resumed, forked, archived; history persisted |

## Key Quote

> "One client request can result in many event updates, and these detailed events are what allow us to build a rich UI on top of the App Server."
