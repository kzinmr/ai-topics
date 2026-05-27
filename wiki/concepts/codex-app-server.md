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
---

# Codex App Server

**`codex app-server`** is the JSON-RPC 2.0 protocol and server interface that powers rich Codex clients — including the official **Codex VS Code extension** and any third-party product embedding a full Codex experience. It provides a bidirectional, transport-agnostic communication layer for authentication, conversation history, approvals, and streamed agent events.

The implementation is open-source in the [openai/codex](https://github.com/openai/codex) repository under `codex-rs/app-server`.

> **When to use `codex app-server`:** when embedding a **full Codex experience** inside your product (IDE, web app, custom client).
> **When NOT to use it:** for automating jobs or running Codex in CI — use the **Codex SDK** instead. For simple one-shot tasks, use the [[concepts/codex-goal|Codex CLI]] directly.

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
