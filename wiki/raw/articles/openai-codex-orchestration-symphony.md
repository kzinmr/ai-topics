---
title: "Symphony: An Open-Source Spec for Codex Orchestration"
source: "OpenAI Blog"
url: "https://openai.com/index/open-source-codex-orchestration-symphony/"
date: "2026-04-27"
tags: [codex, agent-orchestration, symphony, openai, linear, coding-agents]
---

# An Open-Source Spec for Codex Orchestration: Symphony

**Authors:** Alex Kotliarskyi, Victor Zhu, Zach Brock
**Repository:** [github.com/openai/symphony](https://github.com/openai/symphony)

## Problem: Human Attention Bottleneck

Engineers could only manage 3–5 interactive Codex sessions before productivity collapsed. Instead of supervising agents session-by-session, Symphony lets them **pull work from the issue tracker** (Linear) automatically.

## Results
- **500% increase** in landed PRs on some teams within first 3 weeks
- Linear workspaces spike upon release

## Architecture

1. **Issue tracker (Linear)** → source of truth
2. **Symphony orchestrator** (poll loop, state machine, workspace manager)
3. **Coding agent (Codex app-server)** per issue in isolated workspace
4. **`WORKFLOW.md`** codifies team process

### State Machine
- **Todo/In Progress** → agent starts working
- **In Review** → agent finishes, attaches PRs
- **Done/Closed** → workspace cleaned up

### Key Design
- Agents have **objectives, not rigid transitions**
- **Workspace isolation** per issue
- `WORKFLOW.md` defines workflow (checkout → set In Progress → attach PR → review video)

## SPEC.md (Core Specification)

Language-agnostic spec. Reference in Elixir.

### Key Config
```yaml
tracker:
  kind: linear
  active_states: ["Todo", "In Progress"]
  terminal_states: ["Closed", "Cancelled", "Done"]

agent:
  max_concurrent_agents: 10
  max_retry_backoff_ms: 300000

codex:
  command: codex app-server
  turn_timeout_ms: 3600000
  stall_timeout_ms: 300000
```

### Agent Runner Protocol (JSON-RPC)
```json
{"id":1,"method":"initialize","params":{"clientInfo":{"name":"symphony"}}}
{"method":"initialized","params":{}}
{"id":2,"method":"thread/start","params":{...}}
```

### Safety Invariants
1. Agent only runs in per-issue workspace path
2. Path must be under workspace root
3. Key sanitized: only `[A-Za-z0-9._-]`

### Retry & Backoff
Normal: 1s. Failure: `delay = min(10000 * 2^(attempt-1), max_retry_backoff_ms)`

## Why Elixir?
"When code is effectively free, you can optimize for correctness/elegance over CPU efficiency."
