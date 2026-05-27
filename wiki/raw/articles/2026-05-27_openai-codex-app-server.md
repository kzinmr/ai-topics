---
title: "App Server – Codex | OpenAI Developers"
source_url: "https://developers.openai.com/codex/app-server"
source_type: "official-documentation"
author: "OpenAI"
publication: "OpenAI Developers"
date: "2026-05-27"
tags: ["codex", "openai", "protocol", "api", "cli", "coding-agents"]
---

# Codex App Server – OpenAI Developers

`codex app-server` is the interface Codex uses to power rich clients (e.g., the Codex VS Code extension). Use it for deep integration: authentication, conversation history, approvals, and streamed agent events. The implementation is open source in the openai/codex repository (`codex-rs/app-server`).

**When to use:** Use `codex app-server` when embedding a full Codex experience inside your product. For automating jobs or running Codex in CI, use the *Codex SDK* instead.

## Protocol

- JSON-RPC 2.0 messages (header `"jsonrpc":"2.0"` omitted on the wire)
- **Transports:**
  - `stdio` (default) – newline-delimited JSON (JSONL)
  - `websocket` (experimental) – one JSON-RPC per WebSocket text frame
  - Unix socket – WebSocket over Unix socket via HTTP Upgrade
  - `off` – no local transport

**WebSocket health probes** (when using `--listen ws://IP:PORT`):
- `GET /readyz` → `200 OK` when listener accepts connections
- `GET /healthz` → `200 OK` if no `Origin` header; `403` with `Origin` header

**WebSocket auth** (for remote exposure):
- `--ws-auth capability-token --ws-token-file /absolute/path`
- `--ws-auth capability-token --ws-token-sha256 HEX`
- `--ws-auth signed-bearer-token --ws-shared-secret-file /path` (plus issuer, audience, clock-skew flags)
- Clients present `Authorization: Bearer <token>` during handshake.

**Overload behaviour:** Bounded queues; when request ingress is full, server rejects with JSON-RPC error `-32001` (`"Server overloaded; retry later."`). Clients should retry with exponential backoff and jitter.

## Message Schema

- **Request:** `{ "method": "...", "id": <number|string>, "params": {...} }`
- **Response:** `{ "id": <id>, "result": {...} }` or `{ "id": <id>, "error": { "code": <int>, "message": "..."} }`
- **Notification:** `{ "method": "...", "params": {...} }` (no `id`)

Schema generation:
```bash
codex app-server generate-ts --out ./schemas
codex app-server generate-json-schema --out ./schemas
```

## Core Primitives

- **Thread** – conversation between user and agent; contains turns
- **Turn** – a single user request + agent work; contains items, streams updates
- **Item** – a unit of input/output (user/agent message, command run, file change, tool call, etc.)

## Lifecycle Overview

1. **Initialize** once per connection (`initialize` request + `initialized` notification). All other methods rejected before this.
2. **Start or resume a thread** (`thread/start`, `thread/resume`, `thread/fork`).
3. **Begin a turn** (`turn/start` with threadId and input; optional model, personality, cwd, sandbox overrides).
4. **Steer an active turn** (`turn/steer` to append more input without starting a new turn).
5. **Stream events** – read notifications on stdout: `thread/*`, `turn/*`, `item/*`.
6. **Finish the turn** – `turn/completed` with final status, or after `turn/interrupt`.

Similar to MCP, `codex app-server` supports bidirectional communication using JSON-RPC 2.0 messages.
