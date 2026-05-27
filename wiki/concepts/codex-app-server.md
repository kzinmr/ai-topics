---
title: "Codex App Server"
created: 2026-05-27
updated: 2026-05-27
type: concept
status: complete
tags:
  - codex
  - openai
  - coding-agents
  - protocol
  - agent-architecture
  - cli
  - api
  - developer-tooling
aliases:
  - codex-app-server
  - Codex app-server protocol
related:
  - concepts/acp
  - concepts/mcp
  - concepts/codex-goal
  - concepts/codex-prompting
  - concepts/agent-client-protocol
  - comparisons/codex-app-server-vs-agent-protocols
  - entities/openai-codex
sources:
  - raw/articles/2026-05-27_openai-codex-app-server.md
  - raw/articles/2026-02-04_openai-unlocking-the-codex-harness.md
  - https://github.com/openai/codex/pull/4471
---

# Codex App Server

**`codex app-server`** is the JSON-RPC 2.0 protocol and server interface that powers rich Codex clients — including the official **Codex VS Code extension** and any third-party product embedding a full Codex experience. It provides a bidirectional, transport-agnostic communication layer for authentication, conversation history, approvals, and streamed agent events.

The implementation is open-source in the [openai/codex](https://github.com/openai/codex) repository under `codex-rs/app-server`.

> **When to use `codex app-server`:** when embedding a **full Codex experience** inside your product (IDE, web app, custom client).
> **When NOT to use it:** for automating jobs or running Codex in CI — use the **Codex SDK** instead. For simple one-shot tasks, use the [[concepts/codex-goal|Codex CLI]] directly.

---

## Development History

The App Server's origin story reveals an organic evolution from internal hack to platform API — and an explicit rejection of MCP along the way.

### Phase 1: Internal Harness Reuse (mid-2025)

The CLI (TUI) was Codex's first surface. When the team built the **VS Code extension**, they needed to reuse the same **Codex harness** (agent loop, tool execution, persistence) without reimplementing it. They first tried exposing Codex as an **MCP server**, but:

> *"Maintaining MCP semantics in a way that made sense for VS Code proved difficult."*

MCP's tool-oriented model didn't cleanly map onto IDE needs: streaming diffs, approval flows, rich session persistence, and bidirectional server-initiated requests. Instead, they created a **JSON-RPC protocol that mirrored the TUI loop** — the "unofficial first version" of the App Server.

Crucially, at this stage: **"We didn't expect other clients to depend on the App Server, so it wasn't designed as a stable API."**

### Phase 2: The MCP Split — PR [#4471](https://github.com/openai/codex/pull/4471) (Sep 30, 2025)

The original `codex mcp serve` command was a monolith: it served both as an MCP server for tool calls AND as the application server for client integrations. PR #4471 by [@bolinfest](https://github.com/bolinfest) split it into two distinct commands:

| Before | After |
|--------|-------|
| `codex mcp serve` (everything) | `codex mcp-server` — pure MCP server (tool calls only) |
| | `codex app-server` — application server (powers VS Code, etc.) |

The PR was massive: **+1,525 / −414 lines across 49 files**. Key changes:
- Moved app-server logic from `codex-rs/mcp-server/` to new `codex-rs/app-server/`
- Broke backward compatibility: new `Initialize` handshake variant, new `SessionConfigured` notification type
- Files had intentional copypasta between `mcp-server` and `app-server` — expected to diverge later
- Integration tests previously under `mcp-server/tests/` moved to `app-server/tests/`

This split crystallized the separation of concerns: MCP server = tool execution for other agents; App Server = full Codex harness embedding.

### Phase 3: Platform Stabilization (late 2025 – early 2026)

As Codex adoption grew, internal teams and external partners needed to embed the harness:
- **JetBrains and Xcode** wanted IDE-grade agent experiences
- **Codex macOS desktop app** needed to orchestrate multiple Codex agents in parallel
- The **web app** needed a server-side runtime

These demands forced a redesign for **stability and backward compatibility**. The result: versioned schema generation (`generate-ts`, `generate-json-schema`), typed protocol enums, and a formal `initialize` handshake with `clientInfo`.

### Phase 4: Public Documentation (Feb 4, 2026)

The blog post *"Unlocking the Codex harness"* by Celia Chen formally introduced the App Server as a **platform API**. SDKs emerged in Go, Python, TypeScript, Swift, and Kotlin. The v2 protocol added filesystem RPCs, thread pagination, and a Python SDK (v0.115.0).

---

## Architecture (Internal)

The App Server is both a protocol and a **long-lived process** with four main components:

```
┌──────────────┐     ┌─────────────────┐     ┌──────────────┐     ┌──────────────┐
│  Stdio       │ ──→ │  Codex Message  │ ──→ │  Thread       │ ──→ │  Core        │
│  Reader      │     │  Processor      │     │  Manager      │     │  Threads     │
│  (JSONL)     │ ←── │  (event trans-  │ ←── │  (one session │ ←── │  (agent loop │
│              │     │   lation layer) │     │   per thread) │     │   execution) │
└──────────────┘     └─────────────────┘     └──────────────┘     └──────────────┘
```

- **Stdio Reader** — translation layer for JSON-RPC over stdio (JSONL)
- **Codex Message Processor** — translates client requests into `codex-core` operations; transforms internal events into stable, backward-compatible notifications. This is where `item/started`, `turn/completed`, etc. are produced.
- **Thread Manager** — spins up one core session per thread, manages lifecycle
- **Core Threads** — actual agent loop executions (the "harness": config loading, tool execution, sandbox enforcement, MCP server integration)

The JSON-RPC protocol is fully **bidirectional**: clients send requests, server streams notifications, and the server can also initiate requests (e.g., approval prompts that pause the turn until the client responds).

---

## Three Integration Patterns

### 1. Local Apps & IDEs (stdio)
The default pattern. The client bundles a platform-specific Codex binary, launches it as a child process, and communicates over a bidirectional stdio channel. Used by: VS Code extension, macOS desktop app, JetBrains, Xcode.

Partners can **decouple release cycles**: keep the client stable while pointing to a newer App Server binary — adopting server-side improvements without waiting for a client release.

### 2. Web Runtime (HTTP + SSE)
For browser-based Codex experiences. A worker provisions a container, launches the App Server inside it, and the browser communicates via HTTP and Server-Sent Events. The browser-side UI stays lightweight; the server is the source of truth for long-running agent tasks.

### 3. Remote Control (WebSocket / Unix Socket)
Experimental transport for non-stdio clients. Use `--listen ws://IP:PORT` for TCP WebSocket or `--listen unix://` for Unix socket. Supports health probes (`/readyz`, `/healthz`) and bearer-token auth.

---

## Protocol Overview

`codex app-server` uses **JSON-RPC 2.0** messages with the `"jsonrpc":"2.0"` header **omitted** on the wire (same convention as [[concepts/acp|ACP]]).

### Transport Options

| Transport | Flag | Status | Notes |
|-----------|------|--------|-------|
| **stdio** | `--listen stdio://` (default) | Stable | Newline-delimited JSON (JSONL) |
| **WebSocket** | `--listen ws://IP:PORT` | Experimental | One JSON-RPC per text frame; `/readyz` and `/healthz` probes |
| **Unix Socket** | `--listen unix://` or `--listen unix://PATH` | Stable | WebSocket over Unix socket via HTTP Upgrade |
| **off** | `--listen off` | — | No local transport exposed |

**WebSocket auth modes** for remote exposure:
- **Capability token**: `--ws-auth capability-token --ws-token-file /absolute/path` (preferred) or `--ws-token-sha256 HEX`
- **Signed bearer token**: `--ws-auth signed-bearer-token --ws-shared-secret-file /path` (HMAC-signed JWT/JWS) with optional `--ws-issuer`, `--ws-audience`, `--ws-max-clock-skew-seconds`

Clients present `Authorization: Bearer <token>` during the WebSocket handshake; auth is enforced **before** JSON-RPC `initialize`.

---

## Message Schema

```json
// Request
{ "method": "thread/start", "id": 1, "params": { "model": "gpt-5.4" } }

// Response (success)
{ "id": 1, "result": { "thread": { "id": "...", "status": "active" } } }

// Response (error)
{ "id": 1, "error": { "code": -32601, "message": "Method not found" } }

// Notification (no id — server → client events)
{ "method": "item/agentMessage/delta", "params": { "delta": "..." } }
```

Schema generation (version-specific outputs):
```bash
codex app-server generate-ts --out ./schemas
codex app-server generate-json-schema --out ./schemas
```

---

## Core Primitives

The API models human-agent interaction through three hierarchical types:

| Primitive | Description | Example |
|-----------|-------------|---------|
| **Thread** | A conversation between user and agent | Multi-turn coding session |
| **Turn** | One user request + agent's full response work | "Fix this bug" → Codex writes code + runs tests |
| **Item** | A unit of input or output within a turn | User message, agent reasoning, shell command, file edit, tool call |

---

## Lifecycle

```
1.  Transport connect → initialize → initialized
2.  thread/start (or thread/resume, thread/fork)
3.  turn/start (with threadId + input)
4.  ← thread/*, turn/*, item/* notifications streamed
5.  turn/steer (optional: append input mid-turn)
6.  turn/completed (or turn/interrupt)
```

### Key Constraints
- **Single `initialize` per connection** — all other methods rejected before it
- **Notification opt-out** via `capabilities.optOutNotificationMethods` (exact match, e.g., `"thread/started"`)
- **Experimental API opt-in** via `capabilities.experimentalApi: true`
- **Backpressure**: bounded ingress queues; overload → JSON-RPC error `-32001` ("Server overloaded; retry later."); clients should use exponential backoff with jitter

---

## API Surface (Selected Methods)

### Thread Management
- `thread/start` — new thread; auto-subscribes to events
- `thread/resume` — reopen existing thread by ID
- `thread/fork` — fork a thread at a specific turn
- `thread/read`, `thread/list` — read/paginate stored threads
- `thread/compact/start` — trigger context compaction

### Turn Lifecycle
- `turn/start` — add user input, begin agent generation (optional: model, personality, cwd, sandbox overrides)
- `turn/steer` — append input to active turn without starting a new one
- `turn/interrupt` — interrupt active generation

### Config & Auth
- `initialize` — client handshake with `clientInfo`
- `config/read` — read server configuration (model, sandbox, tools, profiles)
- Auth endpoints for enterprise SSO compliance

### Events (Server → Client Notifications)
- `thread/started`, `turn/started`, `turn/completed`
- `item/agentMessage/delta` — streaming agent output
- `item/shellCommand/started`, `item/fileEdit/*` — tool execution events

---

## Comparison with MCP and ACP

| Dimension | Codex App Server | [[concepts/mcp\|MCP]] | [[concepts/acp\|ACP]] |
|-----------|------------------|----------------------|----------------------|
| **Protocol** | JSON-RPC 2.0 (`,jsonrpc` omitted) | JSON-RPC 2.0 | JSON-RPC 2.0 |
| **Purpose** | Embed full Codex in a product | Tool/resource server for LLM clients | Agent-to-agent communication |
| **Core Primitives** | Thread → Turn → Item | Tools, Resources, Prompts | Agents, requests, notifications |
| **Streaming** | Event notifications (turn/started → item/* → turn/completed) | Server→client notifications | Server→client notifications |
| **Auth** | WebSocket bearer tokens, enterprise SAML/OAuth | OAuth 2.0 (Authorization) | Capability tokens, signed JWTs |
| **Transport** | stdio, WebSocket, Unix socket | stdio, Streamable HTTP | stdio, WebSocket, Unix socket |
| **Scope** | Single-agent (Codex) | Agent↔Tool/Resource | Agent↔Agent |

---

## Integration Pattern (stdio Example, Node.js)

```ts
const proc = spawn("codex", ["app-server"], { stdio: ["pipe", "pipe", "inherit"] });
const rl = readline.createInterface({ input: proc.stdout });

const send = (msg: unknown) => {
  proc.stdin.write(`${JSON.stringify(msg)}\n`);
};

rl.on("line", (line) => {
  const msg = JSON.parse(line);
  // Handle server notifications...
  if (msg.id === 1 && msg.result?.thread?.id) {
    const threadId = msg.result.thread.id;
    send({ method: "turn/start", id: 2,
      params: { threadId, input: [{ type: "text", text: "Summarize this repo." }] }
    });
  }
});

// Handshake
send({ method: "initialize", id: 0,
  params: { clientInfo: { name: "my_product", title: "My Product", version: "0.1.0" } }
});
send({ method: "initialized", params: {} });
send({ method: "thread/start", id: 1, params: { model: "gpt-5.4" } });
```

---

## Key Takeaways

1. **App Server ≠ Codex CLI.** The CLI is for humans typing prompts; the app-server is for **programmatic embedding** of a full Codex agent experience.
2. **Protocol-first design.** The JSON-RPC layer is versioned and schema-generatable — `generate-ts` and `generate-json-schema` produce version-specific types.
3. **Streaming events model.** Unlike a simple request-response API, the app-server emits a rich event stream (`thread/*`, `turn/*`, `item/*`) that maps directly to UI rendering (agent messages, tool calls, file diffs).
4. **Open-source reference.** The protocol definitions in `codex-rs/app-server-protocol/` serve as the canonical specification; the documentation page is a human-readable companion.
5. **MCP-adjacent but different.** Both use JSON-RPC, but MCP is for tool/resource servers while Codex App Server is for **embedding a specific agent** (Codex) as a service — closer in spirit to ACP's agent-to-agent communication model.
