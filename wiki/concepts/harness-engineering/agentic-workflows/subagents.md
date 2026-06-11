---
title: "Subagents — Parallel AI Agent Delegation"
type: concept
aliases:
  - subagents
  - sub-agent
  - multi-agent-delegation
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - agentic-engineering
  - multi-agent
status: draft
sources:
  - "https://simonwillison.net/guides/agentic-engineering-patterns/subagents/"
---

# Subagents

A pattern where the main AI agent spawns **independent sub-agents in parallel**, each executing tasks in an isolated context and terminal session.

## Design Principles

### 1. Independence
> "Each subagent gets its own conversation, terminal session, and toolset. Only the final summary is returned."

- Sub-agents **do not share context** with each other
- The main agent's conversation is not passed to sub-agents
- Each sub-agent operates in an independent environment

### 2. Parallelism
> "Batch mode: up to 3 tasks to run in parallel. All run concurrently and results are returned together."

- Multiple independent tasks run **simultaneously**
- Results are returned as an array
- Significantly reduced wait times

### 3. Self-Containment
> "Subagents have NO memory of your conversation. Pass all relevant info via the 'context' field."

- Instructions to sub-agents must be **fully self-contained**
- The main conversation history is not automatically passed
- Explicitly pass required file paths, error messages, and constraints

## When to Use

| ✅ Appropriate For | ❌ Not Appropriate For |
|-------------|---------------|
| Reasoning-heavy subtasks (debugging, code review, research) | Simple mechanical tasks (use `execute_code` instead) |
| Large data processing that would overflow context | Single tool calls (invoke directly) |
| Parallel independent workstreams (research A and B simultaneously) | Tasks requiring user interaction (sub-agents cannot ask questions) |

## Implementation Patterns

### Basic: Single Sub-agent
```yaml
delegate_task:
  goal: "Research the latest developments in agentic engineering"
  context: "Focus on Simon Willison's blog posts from 2025-2026"
  toolsets: ["terminal", "web"]
  max_iterations: 50
```

### Parallel: Batch Mode
```yaml
delegate_task:
  tasks:
    - goal: "Research tool A"
      toolsets: ["web"]
    - goal: "Research tool B"
      toolsets: ["web"]
    - goal: "Analyze codebase structure"
      toolsets: ["terminal", "file"]
  max_iterations: 50
```

### ACP Mode: External Agent Integration
```yaml
delegate_task:
  goal: "Run Claude Code for deep analysis"
  acp_command: "claude --acp --stdio"
  acp_args: ["--acp", "--stdio", "--model", "claude-sonnet-4"]
```

## Hermes Implementation Example

Hermes uses the `delegate_task` tool to launch sub-agents **strategically**:

```
1. Main agent analyzes the task
2. Determines if reasoning is needed → if so, delegate_task
3. Passes self-contained instructions to sub-agent
4. Continues other work while waiting for results
5. Integrates results and reports to user
```

### Example: X Account Enrichment
```
delegate_task:
  goal: "Research this person's X activity, blog, projects, and contributions"
  context: "Create an L3 thought analysis entity page. Match the depth of antirez-com.md or simon-willison.md."
  toolsets: ["terminal", "web", "file"]
  max_iterations: 50
```

## Caveats

### Iteration Limits
> "Sub-agents of delegate_task can hit iteration limits (around 50) when processing more than 5 entities, which can prevent file writing from completing."

- Sub-agents have **maximum iteration limits**
- Complex tasks may hit these limits
- Processing 5+ entities requires **batch splitting**

### Context Compression
Since sub-agents have **their own context**:
- The main agent's memory is not shared
- Required information must be explicitly passed via the `context` field
- "That thing we discussed earlier" does not apply

### Sub-Agent Summaries Are Lossy

> *"Always have the main agent read relevant files itself. Sub-agent summaries are lossy; cross-attention in the main context window improves pairwise reasoning."*
> — Sankalp (Claude Code 2.0 Guide)

Sub-agent return values (summaries) are missing important details. For decisions requiring precision, **have the main agent read the files directly**.

**Guidance**:
| Task | Recommended | Reason |
|--------|------|------|
| Deep file understanding | Main agent | Accurate reasoning via cross-attention |
| Independent research | Sub-agent | Fast parallel execution |
| Bug finding, code review | Sub-agent (Codex, etc.) | Different model perspectives improve detection |
| Complex refactoring | Main agent | Context understanding is essential |

### Error Handling
- If a sub-agent fails, the main agent can continue
- Results are returned as arrays, so partial success can be handled
- Error information can be passed as `context` to the next sub-agent

## Related Concepts

- [[concepts/agentic-engineering]] — Higher-level concept
- [[concepts/context-engineering/window-management|Context Window Management]] — Sub-agents circumvent context window problems
- [[concepts/harness-engineering/agentic-workflows/cognitive-debt]] — Sub-agent self-containment reduces cognitive debt
- [[concepts/multi-agent-autonomy-scale]] — Sub-agents represent a middle level of autonomy

## References

- [[entities/simon-willison]] — Concept originator, Hermes implementer
- [Subagents guide](https://simonwillison.net/guides/agentic-engineering-patterns/subagents/)
- [Hermes delegate_task documentation](~/wiki/concepts/harness-engineering/)