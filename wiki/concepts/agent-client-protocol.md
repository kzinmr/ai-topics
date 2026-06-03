---
title: "Agent Client Protocol (ACP)"
type: concept
created: 2026-06-03
updated: 2026-06-03
tags:
  - protocol
  - agent-architecture
  - coding-agents
  - acp
  - agent-communication
  - harness-engineering
aliases:
  - agent-client-protocol
  - acp-protocol
related:
  - concepts/agent-communication-protocols
  - concepts/codex-app-server
  - comparisons/codex-app-server-vs-agent-protocols
  - comparisons/harness-backend-routing
  - entities/devin
sources:
  - https://agentclientprotocol.com/get-started/introduction
  - https://docs.devin.ai/desktop/acp
  - https://docs.devin.ai/desktop/acp/building-a-custom-acp-agent
  - raw/articles/2026-06-03_devin-desktop-windsurf-rebrand-acp-agent-neutral.md
  - raw/articles/2026-05-27_openai-codex-app-server.md
---

# Agent Client Protocol (ACP)

The **Agent Client Protocol (ACP)** is an open standard protocol that defines how AI coding agents communicate with host environments (editors, IDEs, CLIs). It enables **agent-neutral harness swapping** — the ability to seamlessly switch between different AI agents while preserving context, conversation history, and workspace state.

ACP is to AI agents what **LSP (Language Server Protocol)** is to code editors — a standardized protocol that decouples the agent implementation from the host environment.

---

## Core Design Principles

1. **Agent-neutral**: Any ACP-compliant agent can work with any ACP-compliant host
2. **Transport simplicity**: JSON-RPC 2.0 over stdio (default), with HTTP optional
3. **Process isolation**: Host spawns agent as subprocess, manages lifecycle
4. **No network configuration**: Agents run as local processes with full filesystem access

---

## Protocol Specification

### Transport

ACP uses **JSON-RPC 2.0 over stdio** (standard input/output) as the default transport. The host process spawns the agent as a subprocess and communicates via stdin/stdout.

### Core Methods

| Method | Description |
|---|---|
| `session/new` | Create a new agent session with initial context |
| `session/prompt` | Send a user message to the agent |
| `session/update` | Stream agent responses (text, tool calls, state changes) |
| `acp/permission_response` | Respond to agent permission requests |

### Notifications (Agent → Host)

| Notification | Description |
|---|---|
| `acp/message` | Agent sends a conversational message |
| `acp/tool_use` | Agent is invoking a tool (command execution, file edit, etc.) |
| `acp/tool_result` | Result of a tool invocation |
| `acp/artifact` | Agent produced an artifact (code change, file, etc.) |
| `acp/state_change` | Agent state changed (working, waiting, complete, error) |

### Session Lifecycle

1. **Initialization**: Host spawns agent process, creates session
2. **Conversation**: Messages flow via `session/prompt` and `session/update` streams
3. **Tool Execution**: Agent requests tool use, host executes and returns results
4. **Completion**: Agent signals completion via state change
5. **Shutdown**: Host terminates agent process

---

## Implementations

### Open Standard (Zed + JetBrains)

The original ACP specification is co-maintained by **Zed** and **JetBrains** as an open standard. Key adopters:

- **Zed** — Native ACP support for AI coding agents
- **JetBrains** — ACP integration across IntelliJ, PyCharm, WebStorm, etc.
- **Toad** — ACP-native agent client
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

OpenClaw's ACP implementation is the most mature for **orchestrator → executor** delegation patterns.

→ [[comparisons/hermes-vs-openclaw-architecture]]

### Devin Desktop ACP Integration (June 2026)

Devin Desktop (formerly Windsurf) implements ACP for **agent-neutral harness swapping** within the IDE:

- **Supported agents**: Devin (default), Claude Code, custom ACP agents
- **Registration**: Custom agents registered via manifest JSON (name, command, args, capabilities)
- **Agent Command Center**: Rich GUI for monitoring and controlling ACP sessions
- **Spaces**: Persistent project-level shared context across ACP sessions

Devin Desktop's ACP implementation uses a slightly extended method set:
- `acp/createSession`, `acp/resumeSession`, `acp/sendMessage`, `acp/getState`, `acp/listTools`, `acp/cancel`, `acp/shutdown`
- Notifications: `acp/message`, `acp/toolUse`, `acp/toolResult`, `acp/artifact`, `acp/stateChange`

→ [[entities/devin]]

### Mastra ACP Agents

Mastra's `@mastra/acp` package enables running ACP-compatible coding agents as tools/sub-agents within Mastra workflows:

- Supervisor delegation pattern
- Workflow step integration
- `@mastra/acp@0.1.0` (May 2026)

→ [[concepts/mastra-acp-agents]]

---

## ACP vs Other Protocols

| Dimension | ACP | Codex App Server | AG-UI | A2A |
|-----------|-----|------------------|-------|-----|
| **Layer** | Client ↔ Agent | Client ↔ Agent | Agent ↔ UI | Agent ↔ Agent |
| **Scope** | Any ACP-compliant agent | Codex-specific | Any agent → UI | Cross-org delegation |
| **Governance** | Open (Zed + JetBrains) | OpenAI (single-vendor) | Open (CopilotKit) | Open (Google/LF) |
| **Transport** | JSON-RPC 2.0 (stdio) | JSON-RPC 2.0 (stdio/WS) | SSE | HTTP |
| **Agent model** | Generic (session-based) | Codex-native (Thread/Turn/Item) | Framework-agnostic | Task delegation |

The key distinction: **ACP is agent-agnostic** (works with any agent), while **Codex App Server is agent-specific** (tightly coupled to Codex's semantic model).

→ [[comparisons/codex-app-server-vs-agent-protocols]]

---

## Strategic Significance

### Agent-Neutral as a Competitive Moat

The "agent-neutral" positioning of ACP has significant strategic implications:

1. **Hedge against model commoditization**: If the underlying agent becomes interchangeable, the host/orchestrator layer captures more value
2. **Ecosystem lock-in through UX**: Rich IDE experiences (Agent Command Center, Spaces, Kanban) create switching costs independent of the agent
3. **Orchestrator as the new control plane**: The entity that manages agent lifecycle, context, and coordination becomes the most valuable layer

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
2. **Method handlers** — Implement `createSession`, `sendMessage`, `getState`, `shutdown`
3. **Tool execution** — Send `toolUse` notifications, receive `toolResult` responses
4. **Agent manifest** — JSON file declaring name, command, capabilities
5. **Main loop** — Message dispatch with proper error handling

Best practices:
- Log to stderr (not stdout) to avoid interfering with JSON-RPC transport
- Send incremental `message` notifications for streaming
- Keep sessions lightweight and serializable for resume support
- Set reasonable timeouts for AI API calls

→ [Building a Custom ACP Agent (Devin Docs)](https://docs.devin.ai/desktop/acp/building-a-custom-acp-agent)

---

## See Also

- [[comparisons/codex-app-server-vs-agent-protocols]] — Multi-protocol landscape comparison
- [[comparisons/harness-backend-routing]] — OpenClaw vs Hermes vs Codex App Server vs Devin Desktop
- [[comparisons/hermes-vs-openclaw-architecture]] — Dual-agent architecture via ACP
- [[concepts/agent-communication-protocols]] — Broader agent communication standards
- [[entities/devin]] — Devin Desktop with ACP integration
- [[concepts/mastra-acp-agents]] — ACP agents in Mastra framework
