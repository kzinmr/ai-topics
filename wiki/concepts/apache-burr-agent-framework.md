---
title: "Apache Burr: Agent Framework for Reliable AI Applications"
created: 2026-06-11
updated: 2026-06-11
type: concept
tags:
  - agent-framework
  - ai-agents
  - python
  - multi-agent
  - open-source
  - apache
  - dagworks
  - observability
  - decision-centric
sources:
  - raw/articles/2026-06-10_apache_burr-agent-framework.md
---

# Apache Burr: Agent Framework for Reliable AI Applications

## Overview

Apache Burr (Incubating) is a pure Python framework for building reliable AI agents and decision-making applications. Originating from [DagWorks](https://github.com/DAGWorks-Inc) and now under the Apache Incubator, Burr provides a lightweight, composable API for developing everything from simple chatbots to complex [[multi-agents/multi-agent-systems|multi-agent systems]].

The framework is named after Aaron Burr — a deliberate reference to the musical *Hamilton*, as Burr builds on **Hamilton**, DagWorks' micro-framework for defining typed dataflows. The naming convention (Hamilton → Burr) reflects Burr's architectural lineage: where Hamilton provides the data transformation layer, Burr adds the state-machine execution layer for agentic decision-making.

### Key Statistics (June 2026)
- **GitHub Stars**: 2,256
- **License**: Apache 2.0 (via Apache Incubator)
- **Language**: Python
- **Status**: Apache Incubating (not yet fully endorsed by the ASF)

## Architecture & Design

Burr models applications as **state machines** composed of `action` functions connected by explicit transitions. Each action reads from and writes to a shared `State` object, creating a fully deterministic, replayable execution path.

The core API consists of three primitives:

1. **`@action`** — A Python decorator that marks a function as a state transition. Actions declare their inputs (`reads`) and outputs (`writes`), making dependencies explicit.

2. **`State`** — An immutable dictionary-like object that captures the full application state at each step. Every action returns a new `State`, enabling time-travel debugging and replay.

3. **`ApplicationBuilder`** — A fluent API for composing actions into an executable application graph with defined transitions, state initialization, and tracking configuration.

### Design Philosophy

Burr's design is explicitly anti-magic and decision-centric. Unlike frameworks that abstract away agent internals, Burr makes state transitions explicit and observable. This supports:

- **[[durable-execution]]**: State is persisted at every step, enabling pause/resume and replay from any point.
- **[[ai-observability|Observability]]**: A built-in Burr UI provides real-time tracing of state transitions and action execution.
- **Deterministic replay**: Debug production issues by replaying exact application states.
- **No DSL, no YAML**: Everything is defined in Python code with decorators and typed APIs.

## Relationship to Hamilton

Burr is the agent layer built on top of **Hamilton**, another DagWorks project. Hamilton is a lightweight framework for defining data transformations as typed Python functions with explicit dependencies — conceptually similar to a DAG (Directed Acyclic Graph) of computations.

Burr extends this model by adding:
- A **state machine execution model** (beyond Hamilton's pure functional DAGs)
- **Cyclic transitions** (agents loop, they don't just compute once)
- **Persistence and tracking** infrastructure
- **A UI for debugging and monitoring** agent behavior

This two-layer architecture (Hamilton for data, Burr for decision flow) positions Burr differently from monolithic agent frameworks that bundle everything together.

## Comparison to Other Agent Frameworks

Burr enters a crowded landscape of agent frameworks, including [[langgraph|LangGraph]], CrewAI, AutoGen, and Microsoft's Agent Framework. Key differentiators:

| Dimension | Burr | LangGraph | CrewAI/AutoGen |
|---|---|---|---|
| **Execution Model** | State machine (action → transition) | Event-driven graph | Role-based multi-agent |
| **State Philosophy** | Immutable, persisted at every step | Mutable, checkpoint-based | Varies |
| **Observability** | Built-in Burr UI | LangSmith integration | Limited built-in |
| **Language** | Python only | Python, JS | Python |
| **Governance** | Apache Incubator | VC-backed (LangChain) | Community/Startup |
| **Learning Curve** | Low (decorators + builder) | Medium (graph concepts) | Low-Medium |

### User Testimonials

> "I have been using Burr over the past few months, and compared to many agentic LLM platforms out there (e.g. LangChain, CrewAi, AutoGen, Agency Swarm, etc), Burr provides a more robust framework for designing complex behaviors." — **Hadi Nayebi**, Co-founder, CognitiveGraphs

> "Moving from LangChain to Burr was a game-changer! It took me just a few hours to get started with Burr, compared to the days and weeks I spent trying to navigate LangChain." — **Aditya K.**, DS Architect, TaskHuman

## Community & Adoption

Despite being relatively new (first GitHub commit: January 2024), Burr has attracted a growing community:

- **2,256 GitHub stars** and 163 forks
- Active Discord community
- Companies using in production: Peanut Robotics, Watto.ai, Paxton.ai, Provectus, TaskHuman
- Part of the Apache Incubator, which provides governance, legal protection (Apache 2.0 license), and community-building infrastructure

The Apache incubation pathway has sparked curiosity in the community, as it's an unusual route for an AI agent framework — most competitors are VC-backed startups or community-run [[open-source]] projects.

## HN Community Reaction

When featured on Hacker News (June 10, 2026, 227 points), the discussion revealed a healthy tension in the AI engineering community:

**The "frameworks aren't necessary" camp**: Several developers argued that an agent is fundamentally "context building, making an LLM call, executing requested tool calls" — simple enough to write from scratch. One commenter noted they built an MVP chatbot for a client using Claude/Codex to generate the agent loop directly, bypassing frameworks entirely.

**The "frameworks provide reliability" counter-argument**: Burr's emphasis on state management, persistence, and observability addresses pain points that hand-rolled solutions often rediscover — particularly around debugging, replay, and production monitoring.

**Comparison discourse**: Commenters compared Burr to StrandsAgents, AWS Bedrock + Serverless Agent Core, and debated whether the Apache governance model is an advantage or liability for a fast-moving AI framework.

This mirrors a broader debate in the [[agent-framework]] ecosystem: whether frameworks add necessary structure for production reliability or just add abstraction overhead to fundamentally simple agent loops.

## See Also

- [[langgraph]] — LangChain's event-driven agent orchestration framework
- [[multi-agents/multi-agent-systems]] — Patterns and architectures for multi-agent coordination
- [[durable-execution]] — Long-running, fault-tolerant agent execution
- [[ai-observability]] — Monitoring and debugging AI systems in production
