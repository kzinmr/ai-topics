---
title: "Agent Client Protocol (ACP)"
type: concept
created: 2026-04-30
updated: 2026-06-03
tags:
  - protocol
  - mcp
  - coding-agents
  - agent-communication
  - harness-engineering
aliases:
  - agent-client-protocol
  - acp-protocol
related:
  - concepts/agent-communication-protocols
  - concepts/codex-app-server
  - concepts/mcp
  - comparisons/codex-app-server-vs-agent-protocols
  - comparisons/harness-backend-routing
  - comparisons/hermes-vs-openclaw-architecture
  - entities/devin
sources:
  - https://www.philschmid.de/acp-overview
  - https://agentclientprotocol.com/get-started/introduction
  - https://docs.devin.ai/desktop/acp
  - https://docs.devin.ai/desktop/acp/building-a-custom-acp-agent
  - raw/articles/2026-02-01_philschmid_acp-overview.md
  - raw/articles/2026-06-03_devin-desktop-windsurf-rebrand-acp-agent-neutral.md
  - raw/articles/2026-05-27_openai-codex-app-server.md
---

# Agent Client Protocol (ACP)

## Summary

The **Agent Client Protocol (ACP)** is an open standard (JSON-RPC 2.0) that provides a common interface for editors/IDEs to interact with AI coding agents. It abstracts agent-specific events and outputs, enabling any ACP-compliant editor (Zed, JetBrains, Obsidian) to communicate with any ACP-compliant agent (Claude Code, Gemini CLI, OpenCode, Goose, Codex CLI).

ACP is to AI agents what **LSP (Language Server Protocol)** is to code editors — a standardized protocol that decouples the agent implementation from the host environment.

**Key distinction:** ACP governs **agent-to-client (UI)** communication, whereas [[concepts/mcp]] governs **agent-to-tool** communication. They are complementary protocols serving different layers of the agent stack.

> **⚠️ Naming conflict:** "ACP" also refers to the former **Agent Communication Protocol** (IBM/I Am Bee), which **merged into A2A** under the Linux Foundation in August 2025. This page covers **Agent Client Protocol** only. For the merged A2A standard, see [[concepts/agent-team-swarm/agent-communication-protocols]].

---

## Core Design Principles

1. **Agent-neutral**: Any ACP-compliant agent can work with any ACP-compliant host
2. **Transport simplicity**: JSON-RPC 2.0 over stdio (default), with HTTP optional
3. **Process isolation**: Host spawns agent as subprocess, manages lifecycle
4. **No network configuration**: Agents run as local processes with full filesystem access

---

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

---

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

---

## Key Implementations

### Zed + JetBrains (Open Standard)

The original ACP specification is co-maintained by **Zed** and **JetBrains** as an open standard. Key adopters:

- **Zed** — Native ACP support for AI coding agents (co-developed with Google and JetBrains)
- **JetBrains** — ACP integration across IntelliJ, PyCharm, WebStorm, etc.
- **Toad** (Will McGugan) — Terminal-based front-end supporting **12 agent CLIs** through ACP: Claude Code, OpenHands, Gemini CLI, and others. Unified interface with fuzzy file search, markdown rendering, shell integration, tab completion. Protocol-agnostic design.
- **Obsidian** — ACP plugin for note-taking AI agents

Reference: [agentclientprotocol.com](https://agentclientprotocol.com/get-started/introduction)

### OpenClaw ACP Integration

OpenClaw uses ACP for **sub-agent spawning** — treating any ACP-compliant agent as an interchangeable execution backend:

```
sessions_spawn({ runtime: "acp", agent: "claude-code" | "codex" | "gemini-cli" | "hermes" })
/acp steer    # mid-execution intervention
/acp cancel   # abort
/acp status   # inspect
```

OpenClaw's ACP implementation is the most mature for **orchestrator → executor** delegation patterns. Key capabilities:
- Parent-owned one-shot ACP sessions with completion channel back to parent
- Child runs on background lane; slow ACP harness does not block main-session work
- Full lifecycle management: spawn, steer, cancel, close, status

→ [[comparisons/hermes-vs-openclaw-architecture]]

### Hermes Agent

Hermes implements ACP-mode for external agent integration:
- **ACP mode**: Allows Claude Code and other ACP-compliant agents to connect via stdio
- **Callback surfaces**: `tool_progress_callback`, `thinking_callback`, `clarify_callback`, `stream_delta_callback` feed ACP notifications to clients
- **Permission flow**: `session/request_permission` enables human-in-the-loop approval gates
- **Dual-agent architecture**: Hermes as execution specialist, OpenClaw as orchestrator, communicating via ACP

→ [[entities/hermes-agent]]

### Devin Desktop ACP Integration (June 2026)

Devin Desktop (formerly Windsurf) implements ACP for **agent-neutral harness swapping** within the IDE:

- **Supported agents**: Devin (default), Claude Code, custom ACP agents
- **Registration**: Custom agents registered via manifest JSON (name, command, args, capabilities)
- **Agent Command Center**: Rich GUI for monitoring and controlling ACP sessions
- **Spaces**: Persistent project-level shared context across ACP sessions
- **Kanban view**: Task management with automatic agent task assignment

Devin Desktop's ACP implementation uses a slightly extended method set for their cloud-integrated architecture, but the core protocol follows the open standard.

Custom agent manifest example:
```json
{
  "name": "My Custom Agent",
  "version": "1.0.0",
  "command": "python",
  "args": ["path/to/your/agent.py"],
  "capabilities": ["code_editing", "terminal", "chat", "web_browsing"],
  "description": "A custom ACP agent for Devin Desktop"
}
```

→ [[entities/devin]]

### Mastra ACP Agents

Mastra's `@mastra/acp` package enables running ACP-compatible coding agents as tools/sub-agents within Mastra workflows:

- Supervisor delegation pattern
- Workflow step integration
- `@mastra/acp@0.1.0` (May 2026)

→ [[concepts/mastra-acp-agents]]

---

## ACP vs MCP vs A2A

| Aspect | ACP | MCP | A2A |
|---|---|---|---|
| **Full Name** | Agent Client Protocol | Model Context Protocol | Agent-to-Agent Protocol |
| **Layer** | Agent ↔ Editor/UI | Agent ↔ Tools/Data | Agent ↔ Agent |
| **Transport** | stdio, HTTP | stdio, HTTP | HTTP (REST) |
| **Purpose** | UI integration for coding agents | Tool discovery and execution | Cross-agent coordination |
| **Origin** | Open standard | Anthropic | Google + IBM (Linux Foundation, 2025 merger) |
| **Status** | Alpha | Stable/Widely adopted | Beta (with former ACP capabilities) |

**Decision:** Use **MCP** for tool integration, **A2A** for cross-organizational agent interaction, and **ACP** for editor/UI integration with coding agents.

→ [[comparisons/codex-app-server-vs-agent-protocols]]

---

## Strategic Significance: Agent-Neutral as Competitive Moat

The "agent-neutral" positioning of ACP has significant strategic implications for the agent ecosystem:

### Hedge Against Model Commoditization

If the underlying agent becomes interchangeable, the host/orchestrator layer captures more value. ACP enables this by making any ACP-compliant agent a drop-in replacement.

### The Orchestrator Wars

Multiple players are positioning as the ACP-based orchestrator:

| Player | Approach | Strength |
|--------|----------|----------|
| **OpenClaw** | Terminal/messaging orchestrator | Dynamic routing, mid-execution control, multi-platform gateway |
| **Devin Desktop** | IDE-native orchestrator | Rich GUI, Spaces, Kanban, established IDE user base |
| **Hermes Agent** | Execution specialist | Persistent memory, bidirectional MCP, skill system |

The competition is not about which agent is best — it's about **which orchestrator captures the most value** when agents become interchangeable.

→ [[comparisons/harness-backend-routing]]

---

## Building Custom ACP Agents

A custom ACP agent requires:

1. **JSON-RPC transport** — Read from stdin, write to stdout
2. **Method handlers** — Implement `initialize`, `session/new`, `session/prompt`
3. **Tool execution** — Send `terminal/create`, `fs/read_text_file` requests
4. **Agent manifest** — JSON file declaring name, command, capabilities
5. **Main loop** — Message dispatch with proper error handling

Best practices:
- Log to stderr (not stdout) to avoid interfering with JSON-RPC transport
- Send incremental `session/update` notifications for streaming
- Keep sessions lightweight and serializable for resume support
- Set reasonable timeouts for AI API calls

→ [Building a Custom ACP Agent (Devin Docs)](https://docs.devin.ai/desktop/acp/building-a-custom-acp-agent)

---

## Significance

ACP addresses a critical fragmentation problem in the AI coding agent ecosystem:

> *"With the explosion of AI coding agents—Claude Code, Gemini CLI, OpenCode, Goose, Codex CLI—we've entered an era where every major AI lab ships their own terminal-based coding assistant. But there is one problem. Each agent has its own events or outputs."*

By standardizing the agent-client interface:
- **Editors** can support multiple agents without custom integrations
- **Agents** can focus on capabilities rather than UI concerns
- **Users** get consistent experience across different coding agents
- **Enterprise** deployments gain auditability and governance hooks

---

## See Also

- [[concepts/agent-team-swarm/agent-communication-protocols]] — Broader protocol landscape (MCP/A2A/ACP comparison)
- [[concepts/agent-communication-standards]] — Standard protocols for multi-agent communication
- [[concepts/mcp]] — Model Context Protocol for agent-to-tool communication
- [[comparisons/codex-app-server-vs-agent-protocols]] — Multi-protocol landscape comparison
- [[comparisons/harness-backend-routing]] — OpenClaw vs Hermes vs Codex App Server vs Devin Desktop
- [[comparisons/hermes-vs-openclaw-architecture]] — Dual-agent architecture via ACP
- [[entities/will-mcgugan]] — Creator of Toad, multi-agent terminal UI via ACP
- [[entities/phil-schmid]] — Author of the ACP overview (2026)
- [[entities/devin]] — Devin Desktop with ACP integration
- [[concepts/mastra-acp-agents]] — ACP agents in Mastra framework
- [[concepts/ai-coding-agent-criticism]] — Critical perspectives on AI coding agents
- [[concepts/harness-engineering/agent-harness]] — Infrastructure layer wrapping raw models
