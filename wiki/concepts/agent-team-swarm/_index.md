---
title: "Agent Team / Swarm"
tags:
  - concept
  - ai-agents
  - model
  - evaluation
  - rag
created: 2026-04-24
updated: 2026-04-24
---

# Agent Team / Swarm

**Agent Team (Swarm)** is an architectural pattern where multiple agents collaborate and divide tasks to autonomously execute complex workflows, rather than a single AI agent performing tasks alone.

An extension of traditional **Harness Engineering** (single Agent + tool environment) scaled to multiple Brains and Hands.

## Taxonomy: Agent Team Concepts

| Concept | Proponent/Implementation | Focus | Level |
|---|---|---|---|
| **Agentic Engineering** | Simon Willison et al. | Software development methodology using AI agents | Level 1: Individual developer workflow |
| **Harness Engineering** | Anthropic, Ryan Lopopolo | Agent execution environment, tool integration, guardrails | Level 2: Single-agent infrastructure |
| **Managed Agents** | Anthropic | Platform separating Agent Brain/Hands/Session | Level 3: Enterprise foundation |
| **Agent Team / Swarm** | OpenAI Symphony et al. | Multi-agent coordination and orchestration | Level 4: Team-level autonomy |
| **Dark Factory** | Dan Shapiro, StrongDM | Full autonomy where humans never write or review code | Level 5: Full automation |

## Dan Shapiro"s "5-Level" Model

Dan Shapiro"s classification as introduced by Simon Willison:

1. **Level 1: Spicy Autocomplete** — Early GitHub Copilot, code completion
2. **Level 2: Chat-assisted** — Ask ChatGPT and copy-paste
3. **Level 3: Agent-assisted** — Claude Code/Codex executes tasks
4. **Level 4: The Engineering Team** — Define specs and plans, agents implement. Humans act as managers
5. **Level 5: Dark Factory** — Like Fanuc"s unmanned factories, fully autonomous development requiring no humans

StrongDM practices this Level 5, while Anthropic Managed Agents and OpenAI Symphony serve as bridges from Level 4 to Level 5.

## Key Implementations

### Anthropic Managed Agents
- **Brain (Claude + harness) / Hands (sandbox) / Session (event log)** fully separated
- Multi-Agent Coordination (Research Preview): Agents can spawn other agents
- Self-Evaluation (Research Preview): Define success criteria and autonomously evaluate and improve
- Details: [[concepts/anthropic-managed-agents]]

### OpenAI Symphony
- Monitors task boards (Linear, etc.) and spawns agent teams to execute
- Provide SPEC.md → Implementable in any language (reference implementation in Elixir)
- A paradigm of "managing work" rather than "managing coding agents"
- Developed by Ryan Lopopolo at OpenAI Frontier. Track record: 3-5 PRs/day → 75 PRs/week
- Details: [[concepts/openai-symphony]], [[entities/ryan-lopopolo]]

### StrongDM Attractor / Dark Factory
- Non-interactive development: Spec + scenarios → Agent creates code → Tests → Convergence
- Humans never look at or review the code
- Digital Twin Universe: Clone dependent services with agents
- Details: [[concepts/dark-factory-software-factory]]

## 2026 Production Architecture Patterns

### The Four Proven Patterns
1. **Hierarchical (Orchestrator-Worker)** — Central manager decomposes tasks, delegates to specialized workers
2. **Peer-to-Peer (Collaborative)** — Agents communicate directly, negotiating without a central manager
3. **Pipeline (Sequential)** — Linear sequence where one agent's output is the next's input
4. **Event-Driven (Reactive)** — Agents subscribe to event bus and activate on triggers

### Communication Protocols
Three protocols competing to become the standard:
- **MCP** — Agent-to-tool communication (mature, widely adopted)
- **A2A** — Dynamic discovery + enterprise governance between autonomous agents (Google + IBM/Linux Foundation, 2025 merger)

Decision: MCP for tools, A2A for cross-org and governance.

### Critical Failure Modes
- **Infinite Delegation:** Agent A → B → A loop. Solution: depth limit (3-5)
- **Context Poisoning:** One agent's error amplified downstream. Solution: validation agents at junctions
- **Cost Explosion:** p99 costs 10-20x average. Solution: hard token/dollar limits per task

### The Shared Memory Problem
Centralized state store with **optimistic concurrency control** (e.g., Redis Lua scripts for atomic check-and-set).

## Related Concepts

- [[concepts/harness-engineering]] — Single-agent execution environment design (foundation)
- [[concepts/multi-agent-autonomy-scale]] — Autonomous coordination research at 256-agent scale
- [[concepts/harness-engineering/agentic-engineering-patterns]] — Agentic Engineering pattern collection
- [[entities/ryan-lopopolo]] — Creator of Symphony, Harness Engineering advocate
- [[concepts/agent-communication-protocols]] — MCP/A2A/ACP protocol comparison
- [[concepts/agentic-conflict-resolution]] — Conflict detection and resolution between multiple agents
- [[concepts/zero-trust-agentic-ai]] — Agent security foundation
