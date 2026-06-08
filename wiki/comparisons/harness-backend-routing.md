---
title: "Harness Backend Routing — OpenClaw vs Hermes vs Codex App Server vs Devin Desktop"
created: 2026-05-27
updated: 2026-06-03
type: comparison
tags:
  - architecture
  - coding-agents
  - harness-engineering
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
  - raw/articles/2026-06-03_devin-desktop-windsurf-rebrand-acp-agent-neutral.md
  - https://github.com/dnakov/alleycat
  - https://github.com/kcosr/codapter
  - https://docs.devin.ai/desktop/acp
---

# Harness Backend Routing — OpenClaw vs Hermes vs Codex App Server

Evaluating the three systems as **harness adapters/proxies** — which can dynamically route to different agent backends.

---

## Verdict

**OpenClaw wins on routing alone. But the three should be stacked as layers, not treated as competitors.** Devin Desktop enters as a new entrant with IDE-native orchestration and ACP-based agent-neutral harness swapping.

---

## Evaluation Matrix

| Requirement | OpenClaw | Hermes | Codex App Server + Codapter | Devin Desktop |
|---|---|---|---|---|
| **Multi-backend** | ACP (19+ agents) | 3 modes (native + Codex Runtime + ACP subagent) | Codapter: Pi(any LLM) + Codex + extensible | ACP (Devin, Claude Code, custom agents) |
| **Dynamic routing** | `sessions_spawn({ runtime })` — per-call selection | Config-level (`/codex-runtime` is static switch) | Codapter model prefix (`pi::gpt-5.4`) | Agent selection at session start (Settings → Agents) |
| **Mid-execution control** | `/acp steer/cancel/close/status` | delegate_task has no mid-execution intervention | N/A (is itself a backend) | Agent Command Center (pause/resume/cancel/fork) |
| **State management** | ACP session tracking | sessions DB + memory | Thread persistence | Spaces (persistent shared context) + ACP sessions |
| **Protocol normalization** | ACP unifies all agents | Codex events → Hermes messages (one-way) | App-server JSON-RPC (de facto standard) | ACP JSON-RPC 2.0 over stdio |
| **Tool interop** | ACP tool_call scope only | Hermes ↔ Codex bidirectional MCP | None (no cross-backend tool sharing) | ACP tool_use scope (host-executed) |
| **Gateway** | Multi-platform | Discord/Slack/Telegram | None | IDE-native (Agent Command Center) |
| **Persistent memory** | Session-scoped | memory / session_search (cross-backend) | Thread-scoped only | Spaces (project-level shared context) |
| **Backend extensibility** | Any ACP-compliant agent | Hermes-side integration needed | Codapter `IBackend` implementation | Custom ACP agents via manifest JSON |
| **UI/UX** | Terminal + messaging | Terminal + messaging | VS Code extension | Full IDE (Agent Command Center, Kanban, Spaces) |

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

### Devin Desktop: IDE-Native Orchestrator

- **ACP-based agent-neutral harness swapping** — any ACP-compliant agent can be the execution backend
- **Agent Command Center** provides rich GUI for multi-agent monitoring and control
- **Spaces** offer persistent project-level shared context across sessions
- **Kanban view** for task management with automatic agent task assignment
- **VS Code-based** — full IDE experience preserved (extensions, keybindings, workflows)
- **Weakness**: Agent selection at session start (not per-call dynamic routing like OpenClaw); ACP agent ecosystem still small (Devin, Claude Code, custom)

---

## Ideal Architecture: 4-Layer Stack

```
+--------------------------------------------------+
| Layer 1: Routing / Control Plane                  |
| ------------------------------------------------- |
| OpenClaw / Devin Desktop                          |
| - OpenClaw: sessions_spawn({ runtime: "acp" })    |
| - OpenClaw: /acp steer/cancel/status              |
| - Devin Desktop: Agent Command Center, Kanban     |
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
| Layer 3: IDE / Workspace Management               |
| ------------------------------------------------- |
| Devin Desktop / Cursor / VS Code                  |
| - Spaces (persistent shared context)              |
| - Agent Command Center (multi-agent GUI)          |
| - Extension ecosystem                             |
| - "Where do engineers work?"                      |
+--------------------------------------------------+
| Layer 4: Execution                                |
| ------------------------------------------------- |
| Codex App Server / Claude Code / Pi / Devin       |
| - Codex: subscription flat-fee, item-granularity  |
| - Claude Code: Opus, hooks                        |
| - Pi: fastest lightweight runtime, any LLM        |
| - Devin: autonomous cloud sandbox                 |
| - "Actually write code and run commands"           |
+--------------------------------------------------+
```

### Role Assignment

| Layer | Best Implementation | Why |
|-------|-------------------|-----|
| **Routing** | OpenClaw | ACP dynamic selection + mid-execution control is unique |
| **Memory/Tool Interop** | Hermes | memory + bidirectional MCP + skills is unique |
| **IDE/Workspace** | Devin Desktop | Agent Command Center + Spaces + Kanban is richest GUI |
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
- **Need rich IDE + multi-agent GUI + agent-neutral harness** → Devin Desktop
- **Need everything** → 4-layer stack (OpenClaw routing + Hermes memory + Devin Desktop IDE + Codex/Devin execution)
