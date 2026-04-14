---
name: Deep Agents
type: concept
tags: [ai-agents, autonomy, planning, file-operations, delegation, sandbox]
related:
  - [[concepts/pydantic-ai]]
  - [[concepts/harness-engineering]]
  - [[concepts/code-mode]]
  - [[entities/samuel-colvin]]
depth: L2
status: complete
created: 2026-04-15
---

# Deep Agents — Autonomous Multi-Step AI Agents

## Definition

Deep agents are autonomous AI agents that combine multiple architectural patterns to handle complex, multi-step tasks with minimal human intervention. They feature:

1. **Planning** — Breaking complex tasks into sub-goals
2. **Progress tracking** — Monitoring completion status
3. **File operations** — Reading, writing, and modifying files
4. **Task delegation** — Spawning sub-agents for specialized work
5. **Sandboxed code execution** — Running generated code safely

## Pydantic AI's Approach

Pydantic AI defines Deep Agents as the highest level (level 6) in its multi-agent complexity hierarchy:

1. Single agent workflows
2. Agent delegation (agents calling other agents via tools)
3. Programmatic agent hand-off
4. Graph-based control flow
5. Deep Agents (autonomous, planning, file ops, delegation, sandbox)

## Implementation Patterns

### Planning and Progress Tracking
Deep agents break complex tasks into steps and track their progress, giving users visibility into the agent's reasoning and current state.

### File Operations
Unlike simple tool-calling agents, deep agents can read and write files, enabling them to:
- Modify codebases
- Create reports and documentation
- Manage configuration files

### Task Delegation
Deep agents can spawn sub-agents for specialized work, similar to how human engineers delegate to specialists.

### Sandboxed Execution
Deep agents require secure code execution environments. Options include:
- **Monty** — Minimal, secure Python interpreter (0.004ms start)
- **Docker** — Full isolation with higher overhead
- **Sandbox services** (Modal, E2B, Daytona) — Remote execution

## Community Implementations

- `pydantic-deep` by Vstorm — Opinionated package bringing deep agent patterns together

## Related

- [[concepts/pydantic-ai]] — Framework supporting deep agents
- [[concepts/harness-engineering]] — Environment design for autonomous agents
- [[concepts/code-mode]] — Code execution for deep agents
- [[concepts/monty-sandbox]] — Secure execution environment
- [[entities/samuel-colvin]] — Pydantic AI creator
