---
title: "Codex App Server vs Claude Agent SDK"
created: 2026-05-27
updated: 2026-05-27
type: comparison
tags:
  - protocol
  - agent-architecture
  - coding-agents
  - codex
  - openai
  - anthropic
  - comparison
aliases:
  - codex-app-server-vs-claude-agent-sdk
related:
  - concepts/codex-app-server
  - concepts/codex-agent-loop
  - concepts/agent-client-protocol
  - comparisons/codex-app-server-vs-agent-protocols
sources:
  - raw/articles/2026-05-27_openai-codex-app-server.md
  - raw/articles/2026-02-04_openai-unlocking-the-codex-harness.md
  - https://code.claude.com/docs/en/agent-sdk/overview
---

# Codex App Server vs Claude Agent SDK

Both are **single-vendor agent integration surfaces** — but they take fundamentally different architectural approaches. App Server is a **wire protocol + server process**; Claude Agent SDK is an **in-process library**.

---

## 30-Second Summary

| | Codex App Server | Claude Agent SDK |
|---|---|---|
| **Type** | Wire protocol + long-lived server process | In-process library (Python/TypeScript) |
| **Architecture** | Separate binary, JSON-RPC over stdio/WS | `npm install` / `pip install`, bundled native binary |
| **Language support** | **Any language** (JSON-RPC client) | Python, TypeScript only |
| **Agent** | Codex only (GPT-5.x-codex) | Claude only (Opus/Sonnet/Haiku) |
| **Built-in tools** | Codex harness tools (shell, file edit, plan, web search, MCP) | 8 built-in: Read, Write, Edit, Bash, Glob, Grep, WebSearch, WebFetch |
| **MCP support** | ✅ Via tool execution in agent loop | ✅ First-class, attach servers directly |
| **Streaming** | Event notifications (`item/*`, `turn/*`) | `async for` iterator over `SDKMessage` objects |
| **State model** | Thread → Turn → Item (persisted, reconnectable) | Session-scoped (in-process; `query()` = fresh, `ClaudeSDKClient` = persistent) |
| **Hooks/middleware** | ❌ Not exposed at protocol level | ✅ Hooks system (PreToolUse, PostToolUse, Stop, SessionStart...) |
| **Permission model** | Sandbox modes + approval policy (per-connection) | Permission modes (acceptEdits, dontAsk, bypassPermissions) + `canUseTool` callback |
| **Schema generation** | `generate-ts` / `generate-json-schema` | N/A (library API, typed) |
| **Deployment** | Bundled binary as subprocess OR remote server | Import in your application code |
| **Use case** | **Embed Codex into a product** (IDE, web app, desktop app) | **Build a custom agent** in your own codebase |

---

## Architecture Comparison

### Codex App Server: Protocol-First

```
┌──────────────────┐     JSON-RPC (stdio/WS)     ┌──────────────────────┐
│  Your Product    │ ←─────────────────────────→ │  codex app-server    │
│  (any language)  │    Thread/Turn/Item events   │  (Rust binary)       │
└──────────────────┘                              │  ┌────────────────┐ │
                                                  │  │ Codex Core     │ │
                                                  │  │ (Agent Loop)   │ │
                                                  │  └────────────────┘ │
                                                  └──────────────────────┘
```

- **Separate process** — the App Server binary runs independently. Your client communicates over a transport (stdio, WebSocket, Unix socket).
- **Language-agnostic** — any language can implement a JSON-RPC client.
- **Versioned, schema-generatable protocol** — `generate-ts` and `generate-json-schema` produce typed bindings.
- **Server manages state** — Threads persist; clients can disconnect and reconnect.

### Claude Agent SDK: Library-First

```
┌──────────────────────────────────────────────┐
│  Your Application (Python or TypeScript)      │
│  ┌──────────────────────────────────────────┐ │
│  │  from claude_agent_sdk import query      │ │
│  │                                          │ │
│  │  Bundled Claude Code binary (native)     │ │
│  │  ┌────────────────────────────────────┐  │ │
│  │  │ Claude Agent Loop                  │  │ │
│  │  │ (Read→Write→Bash→WebSearch→Repeat) │  │ │
│  │  └────────────────────────────────────┘  │ │
│  └──────────────────────────────────────────┘ │
└──────────────────────────────────────────────┘
```

- **In-process** — the SDK is a library imported directly into your Python/TypeScript code. Bundles a native Claude Code binary as optional dependency.
- **Language-locked** — Python and TypeScript only.
- **Typed API** — `async for` iterator, `ClaudeSDKClient` class, hooks system.
- **Session is in-process** — state lives as long as your process; no reconnection protocol.

---

## When Each Makes Sense

### Use Codex App Server when:
- You're building a **product** (IDE, desktop app, web platform) that embeds Codex
- You need **language flexibility** (your frontend is Kotlin/Swift/Go — not Python/TS)
- You want **decoupled release cycles** (update the App Server binary without touching your client)
- You need **multi-connection, persistent state** (multiple clients connecting to shared threads)
- You're targeting **several surfaces** (VS Code + web + desktop from one integration)
- **Example**: JetBrains IDE plugin, Xcode integration, a SaaS coding platform

### Use Claude Agent SDK when:
- You're building a **custom agent application** (internal tool, automation script, prototype)
- Your stack is **Python or TypeScript** and you want a simple `import`
- You need **hooks for behavioral control** (PreToolUse, PostToolUse, Stop)
- You want **8 built-in tools** without implementing tool execution yourself
- You want **frictionless MCP server attachment** (one config line)
- **Example**: Internal on-call SRE agent, code review bot, data analysis pipeline, custom CLI tool

---

## Feature Deep-Dive

### Streaming & Event Model

| | Codex App Server | Claude Agent SDK |
|---|---|---|
| **Model** | Server-pushed notifications (`item/started`, `turn/completed`) | Client-pulled `async for` iterator |
| **Granularity** | Item-level (every tool call, file edit, reasoning step) | Message-level (tool use blocks, text deltas) |
| **Mid-turn control** | `turn/steer` (append input), `turn/interrupt` | `query.interrupt()`, `setPermissionMode()` |
| **Reconnection** | ✅ Reconnect to existing thread | ❌ Session lost on process exit |

### Permission & Safety

Both have sandboxed execution, but differ in the control surface:

| | Codex App Server | Claude Agent SDK |
|---|---|---|
| **Sandbox** | OS-enforced (macOS Seatbelt, Linux/WSL) | Container-based (via Claude Code binary) |
| **Approval flow** | Server-initiated request, client responds allow/deny | `canUseTool` callback or permission mode preset |
| **Granularity** | Per-action (file edit, shell command, network access) | Per-tool + per-mode (acceptEdits, dontAsk, bypassPermissions) |
| **Model classifier** | ❌ (binary allow/deny) | ✅ `auto` mode uses classifier for approval decisions |

### Tool Ecosystem

| | Codex App Server | Claude Agent SDK |
|---|---|---|
| **Built-in** | Shell, file ops, plan, web search (via agent loop) | Read, Write, Edit, Bash, Glob, Grep, WebSearch, WebFetch |
| **Custom tools** | Via MCP servers (external process) | Via MCP servers OR inline Python/TS `tool()` functions |
| **MCP client** | Agent loop invokes MCP tools; deterministic enumeration | First-class; attach by URL or command; auto-negotiation |
| **Skills** | ✅ Skill system (`skills/list`, `SKILL.json`) | ❌ Not a first-class concept (use system prompt) |

---

## What They're NOT

Both are **single-vendor** — they don't compete with multi-agent standards:

| Need | Solution |
|------|----------|
| Multi-agent, vendor-agnostic client↔agent | [[concepts/agent-client-protocol\|ACP]] |
| Agent↔agent task delegation | A2A |
| Agent↔frontend streaming (any agent) | AG-UI |
| Agent↔tools (open standard) | MCP |

---

## Migration Considerations

### Claude Agent SDK → Codex App Server
- **Why**: You need language flexibility, multi-surface deployment, or persistent reconnectable state
- **Cost**: Rewrite integration code from Python/TS SDK calls to JSON-RPC client; lose hooks system; gain versioned schema
- **Good for**: Product teams graduating from prototype to platform

### Codex App Server → Claude Agent SDK
- **Why**: You want simpler in-process integration, hooks, or built-in tools without implementing tool execution
- **Cost**: Lock into Python/TypeScript; lose language flexibility; gain hooks and inline custom tools
- **Good for**: Teams who only need Claude and want faster iteration

---

## Verdict

**They serve different integration philosophies:**

- **App Server = "I have a product, give me a Codex server I can talk to."** Protocol-first, language-agnostic, multi-surface. The right choice when the agent is a **service** your product consumes.

- **Claude Agent SDK = "I'm writing code, give me an agent I can import."** Library-first, Python/TS-native, hooks-rich. The right choice when the agent is a **dependency** of your application.

If you're building a **platform** that embeds coding agents → App Server. If you're building a **specific agent application** → Claude Agent SDK.
