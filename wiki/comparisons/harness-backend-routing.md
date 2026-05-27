---
title: "Harness Backend Routing — OpenClaw vs Hermes vs Codex App Server"
created: 2026-05-27
updated: 2026-05-27
type: comparison
tags:
  - agent-architecture
  - coding-agents
  - harness-engineering
  - agent-harness
  - comparison
aliases:
  - harness-adapter-comparison
  - harness-proxy-comparison
related:
  - concepts/codex-app-server
  - concepts/hermes-codex-app-server-runtime
  - concepts/agent-client-protocol
  - comparisons/hermes-vs-openclaw-architecture
sources:
  - raw/articles/2026-05-27_hermes-codex-app-server-runtime.md
  - https://github.com/dnakov/alleycat
  - https://github.com/kcosr/codapter
---

# Harness Backend Routing — OpenClaw vs Hermes vs Codex App Server

Evaluating the three systems as **harness adapters/proxies** — which can dynamically route to different agent backends.

---

## Verdict

**OpenClaw wins on routing alone. But the three should be stacked as layers, not treated as competitors.**

---

## Evaluation Matrix

| Requirement | OpenClaw | Hermes | Codex App Server + Codapter |
|---|---|---|---|
| **Multi-backend** | ACP (19+ agents) | 3 modes (native + Codex Runtime + ACP subagent) | Codapter: Pi(any LLM) + Codex + extensible |
| **Dynamic routing** | `sessions_spawn({ runtime })` — per-call selection | Config-level (`/codex-runtime` is static switch) | Codapter model prefix (`pi::gpt-5.4`) |
| **Mid-execution control** | `/acp steer/cancel/close/status` | delegate_task has no mid-execution intervention | N/A (is itself a backend) |
| **State management** | ACP session tracking | sessions DB + memory | Thread persistence |
| **Protocol normalization** | ACP unifies all agents | Codex events → Hermes messages (one-way) | App-server JSON-RPC (de facto standard) |
| **Tool interop** | ACP tool_call scope only | Hermes ↔ Codex bidirectional MCP | None (no cross-backend tool sharing) |
| **Gateway** | Multi-platform | Discord/Slack/Telegram | None |
| **Persistent memory** | Session-scoped | memory / session_search (cross-backend) | Thread-scoped only |
| **Backend extensibility** | Any ACP-compliant agent | Hermes-side integration needed | Codapter `IBackend` implementation |

---

## Strengths

### OpenClaw: ACP Router

```yaml
sessions_spawn({
  runtime: "acp",
  agent: "codex" | "claude-code" | "gemini-cli" | "pi" | "hermes"
})
/acp steer  # mid-execution intervention
/acp cancel # abort
/acp status # inspect
```

- `sessions_spawn` abstracts per-call backend selection
- ACP normalizes all agents to a uniform interface
- `/acp steer` is the killer feature for adapter/proxy use
- **Weakness**: Tool interop limited to ACP tool_call; no bidirectional MCP like Hermes

### Hermes: Tool Interop + Persistent Memory

- **Bidirectional MCP callbacks** (Hermes ↔ Codex) are unique
  - Codex can call Hermes' browser/vision/skills
  - Hermes receives Codex's shell/apply_patch/plugin results
- **memory / session_search** provides cross-backend persistent memory
- **Skill graph** functions as reusable procedural knowledge
- **Weakness**: Backend switching is static; no dynamic routing or mid-execution control

### Codex App Server + Codapter: De Facto Standard Hub

- App Server wire protocol is becoming an implementation standard
- Codapter enables backend extensibility (Pi with any LLM)
- Alleycat multiplexes multiple agents onto a single app-server socket
- **Weakness**: No tool interop, persistent memory, or gateway — needs other layers

---

## Ideal Architecture: 3-Layer Stack

```
+--------------------------------------------------+
| Layer 1: Routing / Control Plane                  |
| ------------------------------------------------- |
| OpenClaw                                          |
| - sessions_spawn({ runtime: "acp" })              |
| - /acp steer/cancel/status                        |
| - Task-type-based dynamic backend selection       |
| - "Which backend for this task?"                  |
+--------------------------------------------------+
| Layer 2: Memory / Tool Interop                    |
| ------------------------------------------------- |
| Hermes                                            |
| - memory / session_search (persistent memory)     |
| - skill system (reusable procedures)              |
| - multi-channel gateway                           |
| - bidirectional MCP callbacks                     |
| - "What to remember and share across backends?"   |
+--------------------------------------------------+
| Layer 3: Execution                                |
| ------------------------------------------------- |
| Codex App Server / Claude Code / Pi / ...         |
| - Codex: subscription flat-fee, item-granularity  |
| - Claude Code: Opus, hooks                        |
| - Pi: fastest lightweight runtime, any LLM        |
| - "Actually write code and run commands"           |
+--------------------------------------------------+
```

### Role Assignment

| Layer | Best Implementation | Why |
|-------|-------------------|-----|
| **Routing** | OpenClaw | ACP dynamic selection + mid-execution control is unique |
| **Memory/Tool Interop** | Hermes | memory + bidirectional MCP + skills is unique |
| **Execution** | Codex App Server | Subscription flat-fee + fine-grained events |

---

## Ecosystem Convergence

The App Server wire protocol is becoming a de facto standard:

```
Client Layer
  Codex Desktop, VS Code, JetBrains, Xcode, Alleycat clients
        |
        |  App Server JSON-RPC  <-- de facto wire standard
        |
Adapter Layer
  Codapter (model routing), Alleycat (agent multiplexing)
        |
Backend Layer
  Codex, Pi (any LLM), Hermes, Claude, OpenCode, Amp, Droid
        |
Model Proxy Layer
  codex-convert-proxy (OpenAI API -> GLM/Kimi/DeepSeek/MiniMax)
```

ACP spread spec-first; App Server protocol spreads implementation-first. The VS Code extension's usage is the biggest adoption driver.

---

## Decision Guide

- **Need dynamic routing + mid-execution control** → OpenClaw
- **Need tool interop + persistent memory** → Hermes
- **Need cheap execution backend** → Codex App Server (subscription flat-fee)
- **Need everything** → 3-layer stack
