---
title: "Subagent Patterns"
created: 2026-05-06
updated: 2026-05-06
type: concept
tags: [agents, orchestration, multi-agent, architecture, design-patterns]
aliases:
  - subagent-architecture
  - agent-orchestration-patterns
  - multi-agent-patterns
related:
  - [[concepts/harness-engineering]]
  - [[concepts/mistral-vibe-remote-agents]]
  - [[concepts/agent-observability-feedback]]
  - [[concepts/agent-patterns]]
sources:
  - raw/articles/2026-05-05-how-agents-manage-other-agents-four-subagent-patterns.md
  - https://www.philschmid.de/subagent-patterns-2026
  - https://spring.io/blog/2026/01/27/spring-ai-agentic-patterns-4-task-subagents/
  - https://nevo.systems/blogs/nevo-journal/ai-subagents
description: "Architectural patterns for how main agents manage and coordinate subagents, ranging from simple inline tool calls to persistent multi-agent teams with direct inter-agent communication."
---

# Subagent Patterns

**Subagent patterns** describe the architectural approaches by which a primary ("main") agent manages, coordinates, and communicates with specialized subordinate agents. As LLMs improve at planning, tool use, and multi-step reasoning, the patterns for agent-to-agent coordination have evolved from simple task delegation to complex, autonomous agent teams.

The concept was systematically categorized by [[entities/philipp-schmid|Philipp Schmid]] in his May 2026 article "How Agents Manage Other Agents: Four Subagent Patterns in 2026."

## The Four Patterns (by Control Level)

### Pattern 1: Inline Tool — Subagent as Function Call

The simplest pattern. The main agent treats a subagent exactly like any other tool (e.g., `read_file`, `run_command`).

- **Mechanism:** Main agent calls a `call_agent` tool → subagent runs with its own context, tools, and instructions → result returns as tool response
- **Sync vs Async:** Can be synchronous (main agent blocks) or asynchronous (returns `agent_id`, result injected later as notification)
- **Best For:** Self-contained tasks — research lookups, code reviews, test generation
- **Limitations:** No follow-up or mid-task course correction possible
- **Model Requirements:** Works with smaller, cheaper models

### Pattern 2: Fan-Out — Spawn and Wait

The main agent dispatches multiple tasks and independently decides when to collect results. Spawning and collecting are decoupled.

- **Mechanism:** Two tools — `spawn_agent` (returns ID immediately) and `wait_agent` (blocks until agents finish)
- **Key Advantage:** Main agent can interleave its own work while subagents run in parallel
- **Best For:** Multiple independent concurrent tasks with no intermediate result dependencies
- **Limitations:** Model must know when to wait; calling `wait_agent` immediately after spawning negates parallelism
- **Model Requirements:** Works with smaller models, but needs good planning capability

### Pattern 3: Agent Pool — Persistent Messaging

Subagents are long-lived, stateful, and interactive. The main agent acts as a coordinator between specialists.

- **Mechanism:** Rich toolset — `spawn_agent`, `send_message`, `wait_agent`, `list_agents`, `kill_agent`
- **Key Advantage:** Subagents retain conversation history. Main agent can send a task → receive draft → send feedback → request revision
- **Best For:** Multi-step workflows requiring iterative refinement (e.g., Researcher → Writer → Fact-checker pipeline)
- **Limitations:** Developer must ensure model understands resource management (calling `kill_agent`, `wait_agent`)
- **Model Requirements:** Needs models capable of tracking multi-agent states across turns

### Pattern 4: Teams — Direct Inter-Agent Communication

The main agent acts as a high-level supervisor. It sets up the team and steps back, allowing subagents to message each other directly.

- **Mechanism:** Subagents have their own `send_message` tools to address teammates by name or path
- **Key Advantage:** Keeps main agent's context clean. Complex coordination logic (Implementer ↔ Reviewer) happens autonomously
- **Best For:** Large-scale tasks where coordination complexity exceeds what a single agent can manage
- **Limitations:** High risk of "agent loops" (A waits for B, B waits for A). Can spiral without proper termination conditions
- **Model Requirements:** Requires frontier-class models (GPT-4o, Claude 3.5 Sonnet) for **every** team member, not just the supervisor

## Comparison Summary

| Pattern | Tools | Main Agent Role | Agent Lifetime | Model Tier |
|---------|-------|-----------------|----------------|------------|
| **Inline Tool** | `call_agent` | Caller | Single task | Small/cheap |
| **Fan-Out** | `spawn`, `wait` | Dispatcher | Single task | Small/cheap |
| **Agent Pool** | `spawn`, `send`, `wait`, `list`, `kill` | Coordinator | Multi-turn | Mid-range |
| **Teams** | All above + cross-agent `send` | Supervisor | Persistent | Frontier |

## Implementation Guidance

1. **Start Simple:** Begin with Pattern 1. Most tasks that feel like they need multi-agent systems work fine with a well-prompted inline tool call.
2. **Escalate Gradually:** Move to Pattern 2 for genuinely parallel independent work, Pattern 3 for multi-step collaboration, Pattern 4 only when coordination logic exceeds single-agent capacity.
3. **Future-Proof Design:** A task requiring four coordinated agents today may be solvable by a single, more capable model tomorrow. Design patterns for flexibility and easy simplification.
4. **Resource Management:** In advanced patterns, the framework provides the tools but the **model controls the orchestration**. Ensure proper lifecycle management (spawn → use → kill).
5. **Coordination Risk:** Pattern 4 requires careful design to prevent agent deadlocks and infinite loops. Implement timeouts and termination conditions.

## Related Concepts

- [[concepts/agent-observability-feedback]] — Observability and feedback loops are critical for managing subagent teams
- [[concepts/harness-engineering]] — The harness surrounds and constrains agents; subagent patterns are part of the harness design
- [[concepts/mistral-vibe-remote-agents]] — Factory/enterprise-level subagent orchestration with cloud execution
- [[concepts/agent-patterns]] — Broader agent architectural patterns beyond subagent coordination

## References

- [Philipp Schmid — "How Agents Manage Other Agents: Four Subagent Patterns in 2026"](https://www.philschmid.de/subagent-patterns-2026)
- [Spring AI — "Agentic Patterns Part 4: Subagent Orchestration"](https://spring.io/blog/2026/01/27/spring-ai-agentic-patterns-4-task-subagents/)
- [Nevo Systems — "AI Subagents: What They Are, How They Work & Why They Matter"](https://nevo.systems/blogs/nevo-journal/ai-subagents)
