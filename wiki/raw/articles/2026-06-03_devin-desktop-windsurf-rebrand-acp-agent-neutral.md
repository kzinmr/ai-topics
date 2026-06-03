# Devin Desktop: Windsurf Rebrand + Agent-Neutral ACP Integration

**Source URLs:**
- https://devin.ai/download
- https://devin.ai/blog/windsurf-is-now-devin-desktop
- https://docs.devin.ai/desktop/acp
- https://docs.devin.ai/desktop/acp/building-a-custom-acp-agent
- https://x.com/windsurf/status/2061889084541509922

**Date:** 2026-06-03

---

## Summary

Cognition AI has rebranded Windsurf (the AI-native IDE acquired for $250M in Jul 2025) to **Devin Desktop**, positioning it as the "Agent Command Center" for managing autonomous AI agents. The key architectural innovation is the integration of the **Agent Client Protocol (ACP)**, enabling **agent-neutral harness swapping** — the ability to use any ACP-compliant agent (Devin, Claude Code, or custom agents) as the execution backend while preserving context and workspace state.

---

## What Changed

Windsurf has been rebranded to Devin Desktop. Under the hood, Devin Desktop now connects directly to Devin's Agent Control Plane (ACP), the orchestration layer powering Devin's cloud agents. The local editor can spawn, monitor, and coordinate autonomous agents in sandboxed cloud environments. Existing editor features (keybindings, extensions, workflows) are preserved.

The top banner on devin.ai/download reads: "Windsurf is now Devin Desktop. The IDE you love, with more features."

---

## Agent Command Center

A sidebar panel/dashboard showing live status of every agent:
- **Agent statuses**: Running, Paused, Waiting, Completed, Errored
- **Real-time view**: Terminal output, file changes, browser activity, code diffs
- **Quick actions**: Pause/Resume, Send Message, View PR/Changes, Stop Agent
- **Multi-session management**: Monitor and control multiple parallel agent sessions

---

## Spaces

Replace traditional project workspaces with persistent shared context:
- Codebase + shared memory/notes
- Task history and decision logs
- Configuration and integration settings
- Unit of collaboration between humans and agents
- Space-level configuration: default repository, branch preferences, integration settings
- Collaboration: shared Spaces for teams, permissions control, activity feed

---

## Kanban View

Board for managing agent tasks:
- Columns: Backlog → In Progress → Review → Done
- Cards show: task description, assigned agent, PR/branch link, status, blockers, dependency graphs
- Agents pull tasks automatically and move them when done

---

## Multi-Agent Management

- Spawning agents with different roles
- Agent-to-agent communication channels
- Dependency rules and conflict resolution policies
- **Shared-nothing architecture** by default (each agent in its own sandbox)
- Shared state goes through ACP-managed interfaces

---

## Agent Client Protocol (ACP) — Agent-Neutral Architecture

### What is ACP?

ACP is an open standard protocol that defines how AI coding agents communicate with host environments like Devin Desktop. It enables **agent-neutral harness swapping** — the ability to seamlessly switch between different AI agents while preserving context, conversation history, and workspace state.

### Protocol Details

- **Transport**: JSON-RPC 2.0 over stdio (standard input/output)
- **Default mode**: Host spawns agent as subprocess, communicates via stdin/stdout
- **No network configuration required**: Agents run as local processes with full filesystem access
- **Process lifecycle**: Managed by the host

### Core Methods

| Method | Description |
|---|---|
| `acp/createSession` | Create a new agent session with initial context |
| `acp/resumeSession` | Resume an existing session with its full history |
| `acp/sendMessage` | Send a user message to the agent |
| `acp/getState` | Query the current state of an agent session |
| `acp/listTools` | List tools available to the agent |
| `acp/cancel` | Cancel the current agent operation |
| `acp/shutdown` | Gracefully shut down the agent process |

### Notifications

| Notification | Description |
|---|---|
| `acp/message` | Agent sends a conversational message |
| `acp/toolUse` | Agent is invoking a tool (command execution, file edit, etc.) |
| `acp/toolResult` | Result of a tool invocation |
| `acp/artifact` | Agent produced an artifact (code change, file, etc.) |
| `acp/stateChange` | Agent state changed (working, waiting, complete, error) |

### Session Lifecycle

1. **Initialization**: Host spawns agent process, sends `acp/createSession`
2. **Conversation**: Messages flow back and forth via `acp/sendMessage` and `acp/message` notifications
3. **Tool Execution**: Agent requests tool use via `acp/toolUse`, host executes and returns `acp/toolResult`
4. **Completion**: Agent signals completion via `acp/stateChange`
5. **Shutdown**: Host sends `acp/shutdown` for graceful termination

### Supported Agents

- **Devin** — Cognition's flagship AI software engineer, fully integrated as the default agent
- **Claude Code** — Anthropic's agentic coding tool, available as a built-in ACP agent
- **Custom ACP Agents** — Any agent that implements the ACP specification can be registered

### Building a Custom ACP Agent

Full guide available at docs.devin.ai/desktop/acp/building-a-custom-acp-agent. Steps:
1. Implement JSON-RPC transport (stdin/stdout)
2. Handle core ACP methods (createSession, sendMessage)
3. Implement tool execution (acp/toolUse notifications)
4. Register agent via manifest JSON (name, command, args, capabilities)
5. Main message dispatch loop

Agent manifest example:
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

---

## Three-Layer Technical Architecture

```
┌─────────────────────────────────────────────────────────┐
│  Layer 1: Local Editor (VS Code-based)                  │
│  - UI, file management, extensions, terminal, local git │
│  - Agent Command Center, Spaces, Kanban view            │
├─────────────────────────────────────────────────────────┤
│  Layer 2: ACP (Cloud Service)                           │
│  - Agent lifecycle management                           │
│  - Sandbox provisioning                                 │
│  - State synchronization                                │
│  - Tool permissions                                     │
│  - gRPC API                                             │
├─────────────────────────────────────────────────────────┤
│  Layer 3: Agent Sandboxes                               │
│  - Isolated cloud Linux environments                    │
│  - Ephemeral by default or pinnable                     │
│  - Filesystem / process tree / network policy           │
└─────────────────────────────────────────────────────────┘
```

Communication:
- Local ↔ ACP: gRPC with streaming
- ACP ↔ Sandboxes: container orchestration + agent runtime SDK
- Local ↔ Sandbox: file sync mediated by ACP + SSH gateway

---

## Strategic Significance: Agent-Neutral Orchestrator

Devin Desktop's ACP integration positions Cognition not just as an agent provider, but as an **agent orchestrator platform**. By supporting any ACP-compliant agent, Devin Desktop becomes the command center for the entire agent ecosystem — similar to how OpenClaw positions itself as an orchestrator via ACP.

This is a significant strategic move:
- **From agent to platform**: Cognition moves from "Devin the agent" to "Devin Desktop the orchestrator"
- **Hedge against model commoditization**: If the underlying agent becomes interchangeable, the orchestrator layer captures more value
- **IDE as control plane**: The IDE becomes the natural place to manage multi-agent workflows
- **Competitive positioning**: Directly competes with OpenClaw's orchestrator role, but with the advantage of an established IDE user base from Windsurf

---

## Pricing and Availability

- Plans and pricing unchanged from Windsurf (including legacy Enterprise plans)
- Available on Mac (Apple Silicon + Intel), Windows (x64 + arm64), Linux
- JetBrains plugin continues as "Windsurf for JetBrains"
- Devin CLI also available (`curl -fsSL https://cli.devin.ai/install.sh | bash`)
- Devin Next (Beta) channel for early adopters

---

## FAQ Highlights

- **"What is Devin Desktop?"** — The new name for Windsurf. Agent Command Center (Spaces, Kanban view, multi-agent management) is front and center, while the full IDE experience remains fully accessible.
- **"Will I lose anything?"** — No. IDE, extensions, workflows, settings, and in-progress work all remain intact. Only the name and branding change.
- **"Does my plan or pricing change?"** — No.
