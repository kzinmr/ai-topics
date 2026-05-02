---
title: "Elixir/BEAM for AI Agent Orchestration"
type: concept
created: 2026-04-30
updated: 2026-04-30
tags:
  - elixir
  - beam
  - otp
  - orchestration
  - fault-tolerance
  - concurrency
  - openai-symphony
sources:
  - raw/articles/elixir-beam-agent-orchestration-2026.md
  - raw/articles/openai-symphony-codex-orchestration.md
related:
  - concepts/harness-engineering
  - concepts/openai-symphony
  - concepts/multi-agent-orchestration
  - concepts/agent-lifecycle
---

# Elixir/BEAM for AI Agent Orchestration

Using the Erlang VM (BEAM) and OTP patterns for orchestrating multi-agent systems, pioneered by Ryan Lopopolo in OpenAI Symphony.

## Why Elixir/BEAM for Agents?

### 1. Native Process Supervision

BEAM was designed for telecommunications fault tolerance — exactly the reliability profile needed for agent orchestration:

```
gen_server behavior
  ├── handle_call (synchronous messages)
  ├── handle_cast (asynchronous messages)
  └── handle_info (system messages like exits)

Supervisor tree
  ├── AgentSupervisor
  │   ├── Agent1
  │   ├── Agent2
  │   └── Agent3
  └── HarnessSupervisor
      ├── Harness1
      └── Harness2
```

**Process supervision** means:
- If an agent crashes, the supervisor restarts it
- If a harness fails, the supervisor can recover state
- The system gracefully handles partial failures

### 2. Massive Concurrency

BEAM handles millions of lightweight processes:
- Each agent is a separate process
- Each tool call can be a separate process
- Message passing between processes is fast and reliable

### 3. Fault Tolerance Patterns

```elixir
# Supervision strategy: one_for_one (restart failed child only)
defmodule AgentSupervisor do
  use Supervisor

  def start_link(init_arg) do
    Supervisor.start_link(__MODULE__, init_arg, strategy: :one_for_one)
  end

  def start_agent(supervisor, agent_config) do
    Supervisor.start_child(supervisor, [agent_config])
  end
end
```

**Key patterns:**
- `:one_for_one` — restart only the failed process
- `:one_for_all` — restart all children if any fails
- `:rest_for_one` — restart failed process and those started after it

### 4. Message Passing Concurrency

Agents communicate via message passing, not shared state:

```elixir
# Send a task to an agent
send(agent_pid, {:task, task_id, task_spec})

# Agent receives and processes
def handle_info({:task, task_id, task_spec}, state) do
  result = execute_task(task_spec)
  {:noreply, %{state | results: Map.put(state.results, task_id, result)}}
end
```

Benefits:
- No shared memory contention
- Failures isolated to message boundaries
- Natural audit trail (all messages logged)

### 5. OTP (Open Telecom Platform) Integration

Elixir's OTP provides battle-tested patterns for:
- **GenServer** — Stateful agent processes
- **Registry** — Dynamic agent discovery
- **ETS** — Shared state tables
- **Phoenix Channels** — Real-time communication

## OpenAI Symphony Architecture

OpenAI Symphony uses Elixir/BEAM to orchestrate multiple coding agents:

```
┌─────────────────────────────────────────────────────┐
│ Symphony Orchestrator (Elixir/OTP)                  │
├─────────────────────────────────────────────────────┤
│ AgentPool (dynamic, supervised)                     │
│ ┌─────────┐ ┌─────────┐ ┌─────────┐               │
│ │ Agent 1 │ │ Agent 2 │ │ Agent N │               │
│ └─────────┘ └─────────┘ └─────────┘               │
├─────────────────────────────────────────────────────┤
│ HarnessRegistry (ETS-backed)                        │
│ Maps agents to their execution harnesses            │
├─────────────────────────────────────────────────────┤
│ TaskQueue (GenStage/dispatch)                       │
│ Backpressure-aware task distribution                │
└─────────────────────────────────────────────────────┘
```

### Key Symphony Features

1. **SPEC.md-driven**: Agents receive full specification, implement in any language
2. **3-5 PR/day → 75 PR/week**: 15x improvement over manual
3. **Non-interactive**: No human in the loop after initial spec
4. **Elixir-native**: Ryan Lopopolo chose BEAM for its process supervision

### Quote from Interviews

> "The process supervision and the gen servers are super amenable to the type of process orchestration that we're doing here."

> "When we turn the spec into Elixir, where like the model takes a shortcut... it has all these primitives that it can make use of in this lovely runtime that has native process supervision."

## Relationship to Harness Engineering

Harness Engineering builds agent execution environments. Elixir/BEAM provides the **orchestration layer** for managing multiple harnesses:

| Concern | Harness Engineering | Elixir/BEAM Solution |
|---------|---------------------|----------------------|
| Agent lifecycle | Start/stop agents | Supervisor trees |
| State management | Harness state | GenServer state |
| Tool execution | MCP tools | GenServer message passing |
| Failure recovery | Restart strategies | OTP supervision strategies |
| Concurrency | Parallel agents | BEAM processes (millions) |

## When to Use BEAM for Agent Orchestration

**Good fit:**
- Multi-agent systems with 10+ concurrent agents
- Systems requiring fault tolerance and graceful degradation
- Long-running agent orchestration (hours/days)
- Systems needing natural audit trails

**Consider alternatives:**
- Single-agent workflows (Python + subprocess is simpler)
- Quick prototyping (LangGraph/AutoGen may be faster)
- When team lacks Elixir expertise

## See Also
- [[concepts/harness-engineering]]
- [[concepts/openai-symphony]]
- [[concepts/multi-agent-orchestration]]
- [[concepts/agent-lifecycle]]
- [[concepts/agent-orchestration-patterns]]