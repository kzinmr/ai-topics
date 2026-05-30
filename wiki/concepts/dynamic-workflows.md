---
title: "Dynamic Workflows"
type: concept
created: 2026-05-30
updated: 2026-05-30
tags:
  - concept
  - agent-orchestration
  - coding-agents
  - multi-agent
  - claude-code
sources:
  - https://www.anthropic.com/news/claude-opus-4-8
---

# Dynamic Workflows

**Dynamic Workflows** is a feature introduced with [[concepts/claude-opus-4-8|Claude Opus 4.8]] in Claude Code (May 28, 2026, research preview). It enables a single Claude Code session to plan work, spawn **hundreds of parallel subagents**, execute them, verify outputs, and report back — all without user intervention between subagent runs.

## How It Works

1. **Planning phase**: Claude analyzes the task and creates a work plan
2. **Parallel execution**: Spawns hundreds of subagents that run concurrently
3. **Verification**: Claude checks the outputs of all subagents before returning
4. **Reporting**: Results are presented to the user as a completed unit of work

This enables **codebase-scale migrations** — operations spanning hundreds of thousands of lines of code — to be completed "from kickoff to merge" using the project's existing test suite as the verification bar.

## Availability

- Claude Code for **Enterprise, Team, and Max plans**
- Requires `claude-opus-4-8` model
- Research preview status (May 2026)

## Architectural Significance

Dynamic Workflows represents a shift from **single-agent interaction** to **multi-agent orchestration within a single session**. This is distinct from:

- **[[entities/cognition|Cognition's Devin]]**: Async agents running in separate VM sandboxes with brain-machine separation
- **[[concepts/subagents]]**: OpenAI's delegate_task pattern where the parent agent spawns independent child agents

Dynamic Workflows keeps the orchestration **within the Claude Code process** — the parent Claude instance manages the subagent lifecycle, verification, and synthesis without the user needing to explicitly manage individual agents.

## Related

- [[concepts/claude-opus-4-8]] — the model that introduced this feature
- [[concepts/multi-agent]] — broader category of multi-agent systems
- [[entities/cognition]] — alternative async agents architecture
- [[concepts/agent-orchestration]] — patterns for coordinating multiple agents
