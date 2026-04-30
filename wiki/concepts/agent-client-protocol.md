---
title: "Agent Client Protocol (ACP)"
created: 2026-04-30
updated: 2026-04-30
type: concept
tags: [agent-client-protocol, acp, mcp, a2a, coding-agents, editor-integration, json-rpc]
aliases: [Agent Client Protocol, ACP (Client)]
related: [[concepts/agent-communication-protocols]], [[concepts/mcp]], [[concepts/ai-coding-agent-criticism]]
sources:
  - "https://www.philschmid.de/acp-overview"
---

# Agent Client Protocol (ACP)

## Summary

The **Agent Client Protocol (ACP)** is an open standard (JSON-RPC 2.0) that provides a common interface for editors/IDEs to interact with AI coding agents. It abstracts agent-specific events and outputs, enabling any ACP-compliant editor (Zed, JetBrains, Obsidian) to communicate with any ACP-compliant agent (Claude Code, Gemini CLI, OpenCode, Goose, Codex CLI).

**Key distinction:** ACP governs **agent-to-client (UI)** communication, whereas [[concepts/mcp]] governs **agent-to-tool** communication. They are complementary protocols serving different layers of the agent stack.

## Protocol Architecture

ACP follows a simple two-role model:

1. **Clients** (editors like Zed, JetBrains, Obsidian) — manage the user environment, display progress, and collect user input
2. **Agents** (Claude Code, Gemini CLI, OpenClaw/Clawdbot) — handle thinking, reasoning, and tool execution
3. **Transport** — communication over **stdio** (agent runs as subprocess) or **HTTP** (remote agents)

### Protocol Lifecycle

```
┌─────────┐                                    ┌──────────┐
│ Client  │                                    │  Agent   │
│(Editor) │                                    │ (Coding) │
└────┬────┘                                    └────┬─────┘
     │                                              │
     │ ── initialize ─────────────────────────────►  │
     │ ◄─ capabilities/response ────────────────── │
     │                                              │
     │ ── session/new ────────────────────────────►  │
     │ ◄─ session_id ───────────────────────────── │
     │                                              │
     │ ── session/prompt ─────────────────────────►  │
     │                                              │
     │ ◄─ session/update (streaming) ───────────── │
     │    plan                                      │
     │    agent_message_chunk                       │
     │    tool_call                                 │
     │    tool_call_update                          │
     │    thought_message_chunk                     │
     │                                              │
     │ ◄─ fs/read_text_file (request) ──────────── │
     │ ◄─ terminal/create (request) ────────────── │
     │ ◄─ terminal/output (notification) ───────── │
     │ ◄─ session/request_permission (request) ─── │
     │                                              │
     │ ── permission response ────────────────────►  │
     │                                              │
     │ ◄─ session/update: complete ─────────────── │
```

## Protocol Methods (Request-Response)

| Method | Direction | Purpose |
|---|---|---|
| `initialize` | Client → Agent | Negotiate protocol version & capabilities |
| `session/new` | Client → Agent | Create new conversation session |
| `session/load` | Client → Agent | Resume existing session |
| `session/prompt` | Client → Agent | Send user message |
| `session/set_mode` | Client → Agent | Switch agent operating mode |
| `fs/read_text_file` | Agent → Client | Read file (includes unsaved editor edits) |
| `fs/write_text_file` | Agent → Client | Write/create file |
| `terminal/create` | Agent → Client | Start shell command |
| `terminal/output` | Agent → Client | Stream command output |
| `terminal/wait_for_exit` | Agent → Client | Wait for command completion |
| `terminal/kill` | Agent → Client | Terminate running command |
| `terminal/release` | Agent → Client | Clean up terminal session |
| `session/request_permission` | Agent → Client | Request user approval for action |

## Notifications (One-Way)

| Notification | Direction | Purpose |
|---|---|---|
| `session/update` | Agent → Client | Stream progress, messages, tool calls |
| `session/cancel` | Client → Agent | Abort current operation |

## Session Update Types

| Update Type | Description |
|---|---|
| `plan` | Agent's execution plan — list of steps with status |
| `agent_message_chunk` | Streamed text response |
| `user_message_chunk` | Echo of user input |
| `thought_message_chunk` | Agent's internal reasoning |
| `tool_call` | New tool invocation — ID, title, kind, status |
| `tool_call_update` | Tool progress/result — status change, content |
| `available_commands` | Slash commands list |
| `mode_change` | Mode switch notification |

## Tool Call Status Flow

Tool calls follow a defined lifecycle:
1. `pending` → tool invocation requested
2. `running` → tool executing
3. `completed` or `failed` → final state
4. Results streamed via `tool_call_update` notifications

## Key Implementations

### Hermes Agent (this system)

Hermes implements ACP-mode for external agent integration:
- **ACP mode**: Allows Claude Code and other ACP-compliant agents to connect via stdio
- **Callback surfaces**: `tool_progress_callback`, `thinking_callback`, `clarify_callback`, `stream_delta_callback` feed ACP notifications to clients
- **Permission flow**: `session/request_permission` enables human-in-the-loop approval gates

### Toad (Will McGugan)

[Toad](https://github.com/will-mcgugan) (December 2025) is a terminal-based front-end for AI coding agents that supports **12 agent CLIs** through ACP:
- Claude Code, OpenHands, Gemini CLI, and others
- Unified interface with fuzzy file search, markdown rendering, shell integration, tab completion
- Protocol-agnostic design — any ACP-compliant agent works

## ACP vs MCP vs A2A

| Aspect | ACP | MCP | A2A |
|---|---|---|---|
| **Full Name** | Agent Client Protocol | Model Context Protocol | Agent-to-Agent Protocol |
| **Layer** | Agent ↔ Editor/UI | Agent ↔ Tools/Data | Agent ↔ Agent |
| **Transport** | stdio, HTTP | stdio, HTTP | HTTP |
| **Purpose** | UI integration for coding agents | Tool discovery and execution | Cross-agent coordination |
| **Origin** | Open standard (IBM/I Am Bee) | Anthropic | Google |
| **Status** | Alpha | Stable/Widely adopted | Beta |

**Decision:** Use **MCP** for tool integration, **A2A** for cross-organizational agent interaction, and **ACP** for editor/UI integration with coding agents.

## Significance

ACP addresses a critical fragmentation problem in the AI coding agent ecosystem:

> *"With the explosion of AI coding agents—Claude Code, Gemini CLI, OpenCode, Goose, Codex CLI—we've entered an era where every major AI lab ships their own terminal-based coding assistant. But there is one problem. Each agent has its own events or outputs."*

By standardizing the agent-client interface:
- **Editors** can support multiple agents without custom integrations
- **Agents** can focus on capabilities rather than UI concerns
- **Users** get consistent experience across different coding agents
- **Enterprise** deployments gain auditability and governance hooks

## Related Concepts

- [[concepts/agent-communication-protocols]] — Broader protocol landscape (MCP/A2A/ACP comparison)
- [[concepts/mcp]] — Model Context Protocol for agent-to-tool communication
- [[entities/will-mcgugan]] — Creator of Toad, multi-agent terminal UI via ACP
- [[concepts/ai-coding-agent-criticism]] — Critical perspectives on AI coding agents
- [[concepts/agent-harness]] — Infrastructure layer wrapping raw models

## Sources

- [The Agent Client Protocol Overview](https://www.philschmid.de/acp-overview) — Philipp Schmid (2026-02-01)
- [Agent Client Protocol Specification](https://agentclientprotocol.com/get-started/introduction)
