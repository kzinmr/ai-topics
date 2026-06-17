---
title: "AG2 / AutoGen"
created: 2026-06-17
updated: 2026-06-17
type: concept
tags:
  - agent-framework
  - multi-agent
  - orchestration
  - microsoft
  - open-source
  - agent-sdk
  - agent-communication
  - event-driven-architecture
  - distributed-systems
aliases:
  - AutoGen
  - AG2
  - pyautogen
sources:
  - raw/articles/2025-04-20_langchain-how-to-think-about-agent-frameworks.md
  - raw/articles/2026-04-08_microsoft-agent-framework-v1.md
  - raw/articles/2026-04-02_microsoft-agent-governance-toolkit.md
  - https://microsoft.github.io/autogen/
  - https://github.com/microsoft/autogen
---

# AG2 / AutoGen

**AutoGen** (also known as **AG2**) is an open-source, event-driven programming framework created by **Microsoft Research** for building scalable multi-agent AI systems. Using the [Actor model](https://en.wikipedia.org/wiki/Actor_model), it enables developers to define agents that communicate through asynchronous messages and can be deployed locally or distributed across cloud infrastructure.

AutoGen was originally developed under the `pyautogen` package. The project has since evolved through multiple major versions and is now known as **AG2** (AutoGen v2), reflecting its community-driven maintenance phase. As of April 2026, AutoGen is in **maintenance mode** — Microsoft has released the [[entities/microsoft-agent-framework|Microsoft Agent Framework]] as its enterprise-ready successor, with a migration path for existing AutoGen users.

- **GitHub**: [microsoft/autogen](https://github.com/microsoft/autogen)
- **Documentation**: [microsoft.github.io/autogen](https://microsoft.github.io/autogen/)
- **Package**: `autogen-agentchat`, `autogen-core`, `autogen-ext`, `autogenstudio`

---

## History

| Date | Milestone |
|------|-----------|
| 2023 | AutoGen v0.2 released — `pyautogen` package, original conversational multi-agent framework |
| 2024 | AutoGen v0.4 — Major redesign introducing **AgentChat** (high-level) and **Core** (low-level) architecture layers |
| 2025 | AG2 rebrand — Community-driven fork gains momentum; `pyautogen` deprecated in favor of `ag2` package |
| 2025-04 | Harrison Chase includes AutoGen in his [living comparison spreadsheet](https://docs.google.com/spreadsheets/d/1B37VxTBuGLeTSPVWtz7UMsCdtXrqV5hCjWkbHN8tfAo/edit?usp=sharing) of 12+ agent frameworks |
| 2026-04-08 | **Microsoft Agent Framework v1.0** released — unifies Semantic Kernel + AutoGen into a single enterprise SDK. AutoGen enters **maintenance mode**. Microsoft provides [migration tooling](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-autogen/) for existing users. |
| 2026-04-02 | Microsoft's **Agent Governance Toolkit** lists AutoGen as a supported framework for runtime security and governance |

**Status as of June 2026:** AutoGen/AG2 continues under community maintenance but will not receive new features or enhancements from Microsoft. New users are directed to [[entities/microsoft-agent-framework|Microsoft Agent Framework]]. The AG2 community fork remains active for users who prefer the AutoGen API and conversational paradigm.

---

## Architecture

AutoGen's architecture is organized into four layers:

### 1. AgentChat (High-Level API)

The primary developer-facing layer for building conversational agents. Key abstractions:

- **AssistantAgent** — Single-agent with tool access (code execution, web search, MCP tools)
- **GroupChat** — Multi-agent conversation where agents take turns based on a speaker selection strategy
- **Team** — Composed multi-agent system with a selector/manager coordinating specialized sub-agents
- **RoundRobinGroupChat** — Deterministic turn-taking pattern for multi-agent discussions
- **SelectorGroupChat** — Dynamic speaker selection using an LLM-based or rule-based selector

AgentChat supports **streaming**, **checkpointing**, and **human-in-the-loop** interruptions.

### 2. Core (Low-Level, Event-Driven)

The foundation layer implementing the **Actor model**. Key characteristics:

- **Agents as Actors** — Each agent is an isolated actor communicating via typed messages (events)
- **Event-Driven** — All agent interactions flow through an event bus; agents publish and subscribe to message types
- **Distributed by Design** — Move from local to distributed deployment by changing the runtime (single-process → gRPC-based distributed)
- **Runtime Abstraction** — `SingleThreadedAgentRuntime` for local development, `GrpcWorkerAgentRuntime` for production
- **Resilience** — Built-in message durability, agent lifecycle management, and fault tolerance

```
┌─────────────────────────────────────────┐
│              AgentChat                   │
│  (AssistantAgent, GroupChat, Team)      │
├─────────────────────────────────────────┤
│              Core                        │
│  (Actor Model, Event Bus, Runtime)      │
├─────────────────────────────────────────┤
│           Extensions                     │
│  (Model Clients, Tools, MCP, Code Exec) │
├─────────────────────────────────────────┤
│            Studio                        │
│  (No-Code GUI, Visual Debugging)        │
└─────────────────────────────────────────┘
```

### 3. Extensions

Pluggable components providing concrete implementations:

- **Model Clients** — OpenAI, Azure OpenAI, Anthropic, Google Gemini, Ollama, and any OpenAI-compatible endpoint
- **Tools** — Function tools, MCP server integration (`McpWorkbench`), code execution sandboxes
- **Code Execution** — Local command-line execution and Docker-based sandboxed execution
- **Memory** — Conversational history, vector store-backed long-term memory

### 4. AutoGen Studio

A no-code web-based GUI for:
- Visually designing agent workflows
- Testing multi-agent conversations interactively
- Exporting configurations as JSON/YAML for production deployment

---

## Key Features

### Multi-Agent Conversations

AutoGen's signature feature is its conversational multi-agent paradigm. Unlike graph-based frameworks that define explicit state transitions, AutoGen models collaboration as a **conversation** where agents take turns speaking based on a speaker selection strategy.

```python
# Multi-agent group chat example
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat

researcher = AssistantAgent("researcher", model_client=client,
    system_message="You research topics thoroughly.")
writer = AssistantAgent("writer", model_client=client,
    system_message="You write clear summaries.")
team = RoundRobinGroupChat([researcher, writer])
result = await team.run(task="Explain quantum computing")
```

### Code Execution

Agents can write and execute code in sandboxed environments (local process or Docker container). This enables:
- Data analysis workflows (agent writes Python to analyze data)
- Self-debugging loops (agent runs code, reads errors, iterates)
- Tool creation at runtime (agent generates new functions on the fly)

### Human-in-the-Loop

AutoGen supports pausing agent execution for human approval at configurable points:
- **Before tool execution** — Human reviews and approves/rejects tool calls
- **Before message delivery** — Human edits or vetoes agent messages
- **Checkpoint and resume** — Save agent state, inspect, and resume from any point

### Tool Use

Agents can access tools through multiple mechanisms:
- **Python functions** — Register any async Python function as a tool
- **MCP (Model Context Protocol)** — Connect to MCP servers via `McpWorkbench`
- **LangChain tools** — Interop with the broader tool ecosystem
- **Custom tool adapters** — Build tool connectors for any API or service

### Distributed Execution

Core's Actor model enables seamless scaling:
- **Local development** — Single-process runtime for fast iteration
- **Distributed production** — gRPC-based multi-process, multi-machine deployment
- **Cross-language** — Agents in different languages communicate through the event bus (experimental)

---

## Comparison to Alternatives

AutoGen occupies a distinct position in the [[concepts/multi-agents/agent-orchestration-frameworks|agent orchestration landscape]]. Below is a comparison with major alternatives as of June 2026:

| Dimension | AG2 / AutoGen | [[concepts/langgraph|LangGraph]] | [[concepts/crewai|CrewAI]] | [[concepts/openai/agents-sdk|OpenAI Agents SDK]] | [[entities/microsoft-agent-framework|Microsoft Agent Framework]] |
|---|---|---|---|---|---|---|
| **Paradigm** | Conversational multi-agent | Graph-based state machines | Role-based crews | Imperative agent abstraction | Enterprise orchestration |
| **Multi-Agent** | Native (GroupChat, Team) | Manual (nodes/edges) | Native (crews) | Limited (handoffs) | Native (all patterns) |
| **Complexity** | Medium-High | Medium | Low | Low | Medium |
| **State Model** | Message/event-based | Full checkpointing | Task-level | Basic memory | Full checkpointing |
| **HITL Support** | Limited | Built-in | Built-in | Basic | Built-in |
| **Distributed** | Yes (Actor model) | Platform (paid) | No | Via sandboxes | Yes (Foundry) |
| **Status** | **Maintenance mode** | Active (v1.0+) | Active | Active (v0.14+) | Active (v1.0) |

### AG2 vs LangGraph

**LangGraph** ([[entities/langchain|LangChain]]) models agentic systems as explicit graphs of nodes and edges, giving developers full control over every state transition. **AutoGen** models them as conversations between agents, abstracting away the control flow. LangGraph's philosophy is "Keras for Agents" — high-level abstractions on a low-level orchestration layer. AutoGen's is "conversations as computation" — agents coordinate through structured dialogue.

**When to use AutoGen:** Research scenarios, multi-agent debate/discussion, exploratory workflows where conversation is the natural interaction model.

**When to use LangGraph:** Production pipelines requiring explicit control, workflows with complex branching/conditionals, systems needing detailed observability at every step.

### AG2 vs CrewAI

**CrewAI** ([[concepts/crewai|CrewAI]]) uses role-based abstraction — define agents with roles, goals, and backstories, then assign tasks. AutoGen uses conversational abstraction — define agents that take turns speaking. CrewAI is more opinionated about structure (sequential/hierarchical processes). AutoGen is more flexible about conversation flow.

As of mid-2026, CrewAI is under active development by CrewAI Inc., while AutoGen is in community maintenance. Users seeking active development should evaluate CrewAI or [[entities/microsoft-agent-framework|Microsoft Agent Framework]].

### AG2 vs OpenAI Agents SDK

The [[concepts/openai/agents-sdk|OpenAI Agents SDK]] focuses on single-agent with tool-calling loops, with limited multi-agent support via handoffs. AutoGen was designed from the ground up for multi-agent conversations. The Agents SDK is simpler but less expressive for complex multi-agent topologies.

### Migration: AutoGen → Microsoft Agent Framework

Since April 2026, Microsoft provides a [migration guide](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-autogen/) for teams moving from AutoGen to Microsoft Agent Framework. Key differences:

- **AgentChat → AgentWorkflows**: Similar high-level APIs but broader orchestration patterns
- **Core → Agent Runtime**: Actor model concepts preserved but integrated with Foundry
- **GroupChat → Multi-Agent Orchestration**: All AutoGen conversation patterns available plus new ones (Magentic-One, handoff)
- **Extensions → Service Connectors**: Broader model provider support including Bedrock, Foundry

---

## Adoption & Ecosystem

### Usage Contexts

AutoGen has been widely adopted in:

- **Academic Research** — Multi-agent collaboration studies, LLM debate experiments, agent coordination research
- **Prototyping** — Rapid multi-agent system prototyping before productionizing in other frameworks
- **Code Generation** — Agents that write, execute, and debug code collaboratively (precursor pattern to modern coding agents)
- **Data Analysis** — Multi-agent pipelines for research, data exploration, and report generation

### Ecosystem Support

- **MCP Integration** — Native `McpWorkbench` for connecting to MCP tool servers
- **Agent Governance Toolkit** — Listed as a supported framework for [[concepts/microsoft-agent-governance-toolkit|runtime security and governance]]
- **Community Packages** — AG2 fork maintains independent package ecosystem (`ag2` on PyPI)
- **Framework Comparisons** — Featured in Harrison Chase's living comparison spreadsheet alongside 12+ frameworks

### Current Trajectory

AutoGen's influence lives on through the [[entities/microsoft-agent-framework|Microsoft Agent Framework]], which absorbed its multi-agent orchestration patterns (sequential, concurrent, handoff, group chat, Magentic-One). The AG2 community fork continues for users who prefer the original API. The conversational multi-agent paradigm pioneered by AutoGen has influenced the design of newer frameworks and remains a valid architectural choice for research and prototyping.

---

## Related Concepts

- [[entities/microsoft-agent-framework]] — Enterprise successor to AutoGen, v1.0 released April 2026
- [[entities/microsoft]] — Parent company and original development organization
- [[concepts/langgraph]] — Graph-based orchestration framework by LangChain
- [[concepts/crewai]] — Role-based multi-agent framework
- [[concepts/openai/agents-sdk]] — OpenAI's agent SDK
- [[concepts/multi-agents/multi-agent]] — Multi-agent AI systems concept
- [[concepts/multi-agents/agent-orchestration-frameworks]] — Comparative analysis of orchestration frameworks
- [[concepts/microsoft-agent-governance-toolkit]] — Security toolkit supporting AutoGen
- [[concepts/mcp]] — Model Context Protocol, supported by AutoGen

---

## References

1. **AutoGen Official Docs** — [microsoft.github.io/autogen](https://microsoft.github.io/autogen/) — Event-driven programming framework for multi-agent AI systems
2. **AutoGen GitHub** — [github.com/microsoft/autogen](https://github.com/microsoft/autogen) — Source code, maintenance mode notice, migration guide
3. **Microsoft Agent Framework v1.0** — [devblogs.microsoft.com](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-version-1-0/) (April 8, 2026) — Unified Semantic Kernel + AutoGen, AutoGen enters maintenance
4. **Agent Governance Toolkit** — [opensource.microsoft.com](https://opensource.microsoft.com/blog/2026/04/02/introducing-the-agent-governance-toolkit-open-source-runtime-security-for-ai-agents/) (April 2, 2026) — Lists AutoGen as supported
5. **How to Think About Agent Frameworks** — Harrison Chase, LangChain Blog (April 20, 2025) — Includes AutoGen in framework comparison spreadsheet
