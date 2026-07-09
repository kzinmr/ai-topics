---
title: "Agent Architecture Decomposition: Model / Runtime / Harness"
type: concept
tags:
sources: []
  - ai-agents
  - architecture
  - open-source
  - mcp
created: 2026-04-30
updated: 2026-05-27
---
---
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
| **Python REPL** | Python function calls | DSPy, Pydantic AI, RLM | Process-level isolation |
| **Micro-VM Interpreter** | Bytecode VM with capability grants | Pydantic Monty | Deny-by-default, explicit function exposure |
| **Browser DOM** | DOM manipulation, JS execution | Browser Use, Playwright MCP | Browser sandbox |
| **Container/MicroVM** | Full environment API | Daytona, Rivet agentOS | Hardware-level isolation |
| **Dedicated Sandboxes** | Policy-enforced execution | NVIDIA OpenShell | Deny-by-default + YAML policies |

#### Agent on REPL: Runtime Natively Suited for Python Functions

When choosing a Python REPL as the Runtime, the agent uses tools by directly calling **Python functions** rather than CLI commands.

```python
agent → call_tool(search_codebase, pattern="...")
agent → call_tool(run_tests, path="./tests/")
agent → call_tool(fetch_weather, city="London")
```

**Representative Example: RLM (Recursive Language Model)**

RLM is an architecture that delegates "context decomposition" to the model ([[mlops/agent-vs-rlm-comparison]]). It selectively extracts relevant context through code operations like `grep` and slicing within a REPL environment. The fundamental unit is **context decomposition** rather than task decomposition.

**Representative Example: Pydantic AI**

A type-safe agent framework ([[concepts/pydantic-ai]]). Registers Python functions as tools, validates inputs/outputs with Pydantic models. Also supports workflow definition via Graph API.

**Agent on REPL Advantages**:
- Type-safe: Tool parameters verifiable with Python type hints
- Structured output: Guaranteed return values via Pydantic models
- Fast: In-process execution (no IPC needed)
- State sharing: Memory space within REPL can be shared between agents

#### Micro-VM Interpreter: Runtime with Dedicated Bytecode VM

**Representative Example: Pydantic Monty**

Monty is a minimal Python interpreter written in Rust ([[concepts/monty-sandbox]]). It extends the Agent on REPL approach, but fundamentally differs by executing code on a **dedicated VM rather than CPython**.

| Property | Value |
|---|---|
| Startup latency | 0.004ms (~1/50,000 of Docker's 195ms) |
| Binary size | ~4.5MB |
| Memory overhead | ~5MB (when embedding CPython) |
| Security | Deny-by-default; only explicitly exposed external functions are accessible |

Monty embodies the design philosophy of "an **agent Runtime built for agents**." It runs only functions explicitly granted by the host, without using any standard library or third-party packages. This follows capabilities-based security principles.

**Execution Continuum** (Samuel Colvin's taxonomy):

| Approach | Control | Expressiveness | Latency | Cost |
|---|---|---|---|---|
| **Tool Calling** | High | Low | Sequential round-trips | Per-token |
| **Monty / CodeMode** | High-Medium | Medium | 0.004ms startup | In-process |
| **Sandbox Services** | Medium | High | ~1000ms+ startup | Per-execution |
| **Coding Agents** | Low | Very High | Minutes | High |
| **Full Computer Use** | None | Maximum | Minutes | Very High |

Monty sits between the "low expressiveness of sequential Tool Calling" and the "high cost/latency of Sandbox/Full Computer Use." An agent can express loops, conditionals, and parallel calls in a single code generation, with zero infrastructure cost.

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
[[concepts/pydantic-ai-harness]] is the Pydantic team's reference implementation — a modular capability library that provides CodeMode, memory, orchestration, guardrails, and more.

### Pydantic: The Full Stack (Runtime + Harness)

Pydantic is unique in providing **both** the Open Runtime and Open Harness layers as an integrated stack:

| Layer | Component | Role |
|---|---|---|
| **Open Runtime** | [Monty](https://github.com/pydantic/monty) | Secure Python bytecode VM (0.004ms startup, deny-by-default) |
| **Open Harness** | [pydantic-ai-harness](https://github.com/pydantic/pydantic-ai-harness) | Capability library (CodeMode, memory, orchestration, guards) |
| **Open Models** | Pydantic AI core | Model-agnostic — works with Claude, GPT, Gemini, Ollama |

**The coupling insight**: CodeMode in the Harness *requires* Monty as its Runtime. The Harness decides *when* to write code vs. use sequential tool calls; the Runtime executes that code safely. This is analogous to how Kubernetes (orchestration) requires container runtime (containerd) — they're separate layers but tightly coupled by design.

This contrasts with frameworks that mix Runtime and Harness concerns:
- **Claude Code / OpenClaw**: Runtime = bash, Harness = proprietary (not separable)
- **LangChain**: Runtime = container/VM (external), Harness = LangGraph (separate vendors)
- **RLM**: Runtime = Python REPL, Harness = recursive context decomposition (same repo, different abstraction levels)

Samuel Colvin's design philosophy — *"Start from nothing, then selectively grant capabilities"* — applies to both Monty (zero filesystem/network by default) and the Harness (zero tools by default — you compose what you need).

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

### Notion's Agent Composition Patterns (April 2026)

Notion's Custom Agents implement a practical multi-agent orchestration model within a productivity workspace:

- **Shared databases as primitives**: Agents compose by sharing Notion databases — this is the filesystem-equivalent for Notion's agent ecosystem
- **Agent-to-agent invocation**: Agents can call other agents directly
- **Manager agents**: A supervisor agent coordinates dozens of specialized agents
- **Memory as pages and databases**: Notion's existing data model (pages + databases) serves as persistent agent memory without requiring separate vector stores

This demonstrates how **agent composition** can leverage existing product data models rather than requiring specialized infrastructure. The key insight: agents compose through the same shared state mechanisms that humans use (databases, pages, documents).

## Sources

- [Harrison Chase's post](https://x.com/hwchase17/status/2034297125417460044) (March 2026)
- [NVIDIA OpenShell announcement](https://developer.nvidia.com/blog/) — Open Runtime reference implementation
- [LangChain Deep Agents](https://blog.langchain.dev/deep-agents/) — Open Harness reference
- [Continual learning for AI agents](https://x.com/i/article/2040467997022884194) (@hwchase17, April 2026)
- [The Definitive Guide to Harness Engineering](../raw/articles/2026-04-27_2047145274200768969_The-Definitive-Guide-to-Harness-Engineering.md)
- [Pydantic Monty: A Minimal Python Sandbox for AI Agents](https://pydantic.dev/articles/pydantic-monty) (Samuel Colvin, Feb 2026)
- [RLM Blog Post](https://alexzhang13.github.io/blog/2025/rlm/) (Alex L. Zhang, Oct 2025)
- [Language Models will be Scaffolds](https://alexzhang13.github.io/blog/2026/scaffold/) (Alex L. Zhang, Feb 2026)
- [Monty, from tool calling to computer use - PyAI Conf 2026](https://www.youtube.com/watch?v=wXjZdrS3LqA) (Samuel Colvin, 2026)

## Related

- [[entities/harrison-chase]]
- [[entities/samuel-colvin]]
- [[entities/nvidia-openshell]]
- [[concepts/harness-engineering]]
- [[concepts/deep-agents]]
- [[concepts/monty-sandbox]]
- [[concepts/pydantic-ai]]
- [[mlops/agent-vs-rlm-comparison]]
- [[entities/alex-zhang]]
