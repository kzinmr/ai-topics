---
title: "Agent Architecture Decomposition: Model / Runtime / Harness"
category: concept
tags: [ai-agent, architecture, open-models, open-runtime, open-harness, mcp]
created: 2026-04-30
updated: 2026-04-30
---

# Agent Architecture Decomposition: Model / Runtime / Harness

A three-layer framework for understanding production AI agent systems, articulated by Harrison Chase (LangChain CEO) in March 2026.

## The Three Layers

### 1. Open Models

The **intelligence layer** — the LLM that powers agent reasoning, planning, and decision-making.

**Key thesis**: No single model dominates all tasks. Production agents should be model-agnostic, selecting the best model per workload.

**Notable open-weight models**:
- NVIDIA Nemotron 3 Super (120B MoE, 1M context)
- Meta Llama 4 (MoE variants)
- Qwen 3 series

**Proprietary models used in agents**:
- Claude Opus 4.7 / Sonnet 4.5 (Anthropic)
- GPT-5.5 (OpenAI)

See: [[entities/harrison-chase]] on model optionality.

### 2. Open Runtime

The **execution environment** where agents operate. This layer determines the native tool-use interface and security boundary.

**Critical insight**: The runtime choice *constrains the natural function-calling mechanism*.

| Runtime Type | Native Tool Interface | Example Agents | Security Model |
|---|---|---|---|
| **Bash/Shell** | CLI commands (`curl`, `grep`, `python script.py`) | Claude Code, OpenClaw, Codex CLI | User-level permissions |
| **Python REPL** | Python function calls | DSPy, custom orchestration | Process-level isolation |
| **Browser DOM** | DOM manipulation, JS execution | Browser Use, Playwright MCP | Browser sandbox |
| **Container/MicroVM** | Full environment API | Daytona, Rivet agentOS | Hardware-level isolation |
| **Dedicated Sandboxes** | Policy-enforced execution | NVIDIA OpenShell | Deny-by-default + YAML policies |

#### Runtime → Tool-Use Relationship

When an agent runs **on bash**, CLI tools become the natural function-calling interface:
```
agent → execute("curl -s https://api.example.com")
agent → execute("grep -r 'pattern' /project")
```

When an agent runs **on Python REPL**, Python functions are the natural interface:
```python
agent → call_tool(search_codebase, pattern="...")
agent → call_tool(run_tests, path="./tests/")
```

This is why coding agents (Claude Code, OpenClaw) feel like "terminal users" — bash is their runtime, so shell commands are their native function-calling protocol.

#### Heterogeneous Agent Composition

For systems with multiple agents on different runtimes, **(Remote) MCP** serves as the universal adapter:

```
┌──────────┐    MCP     ┌──────────────┐
│ CLI Agent│◄──────────►│              │
│ (bash)   │            │   MCP Router │
├──────────┤            │  (Gateway)   │
│ Python   │◄──────────►│              │
│ Agent    │    MCP     └──────────────┘
├──────────┐                     ▲
│ Browser  │    MCP              │
│ Agent    │◄────────────────────┘
└──────────┘
```

This architecture is analogous to **microservices with an API gateway**:
- Each agent is an independent service with its own runtime
- MCP standardizes the interface (like gRPC/REST)
- The MCP Router handles routing, auth, and load balancing

See: [[entities/nvidia-openshell]] for the Open Runtime reference implementation.

### 3. Open Harness

The **orchestration layer** that connects the model to the runtime and manages the agent lifecycle.

**Components**:
- **Task Planning** — Breaking high-level goals into executable steps
- **Sub-agent Spawning** — Creating worker agents for parallel tasks
- **Memory Management** — Short-term context + long-term memory persistence
- **Tool Routing** — Selecting which tool/capability to invoke
- **Context Management** — Maintaining conversation history, file state, etc.

**The "Harness = Backend" thesis** (from [[concepts/harness-engineering]]#iii-platform): the harness shouldn't be separate from the backend infrastructure — it *is* the backend. When agents are treated as workers in a unified system, the distinction between "agent orchestration" and "backend services" collapses.

**Open vs Closed Harness**:
| Property | Open Harness | Closed Harness |
|---|---|---|
| Memory ownership | User-controlled (Mongo, Postgres, Redis) | Platform-controlled |
| Model selection | Pluggable / swappable | Vendor-locked |
| Tool ecosystem | Standardized (MCP, AGENTS.md) | Proprietary |
| Portability | High | Low |

LangChain Deep Agents is Chase's reference implementation of an Open Harness.

## Relationship to Traditional Architecture

The Model/Runtime/Harness decomposition maps to traditional software architecture:

| AI Agent Layer | Traditional Equivalent |
|---|---|
| Open Model | AI/ML inference service |
| Open Runtime | Container / VM / execution environment |
| Open Harness | Orchestration layer + message queue + state management |
| MCP (inter-runtime) | API Gateway / Service Mesh |
| Agent Workers | Microservices |

This mapping explains why **microservice architecture patterns** (service discovery, routing, circuit breakers, observability) directly apply to multi-agent systems.

## Sources

- [Harrison Chase's post](https://x.com/hwchase17/status/2034297125417460044) (March 2026)
- [NVIDIA OpenShell announcement](https://developer.nvidia.com/blog/) — Open Runtime reference implementation
- [LangChain Deep Agents](https://blog.langchain.dev/deep-agents/) — Open Harness reference
- [Continual learning for AI agents](https://x.com/i/article/2040467997022884194) (@hwchase17, April 2026)
- [The Definitive Guide to Harness Engineering](../raw/articles/2026-04-27_2047145274200768969_The-Definitive-Guide-to-Harness-Engineering.md)

## Related

- [[entities/harrison-chase]]
- [[entities/nvidia-openshell]]
- [[concepts/harness-engineering]]
- [[concepts/deep-agents]]
