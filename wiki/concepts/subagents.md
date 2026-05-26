---
title: "Subagents — Parallel AI Agent Delegation"
type: concept
aliases:
  - subagents
  - sub-agent
  - multi-agent-delegation
tags:
  - concept
  - agentic-engineering
  - multi-agent
  - orchestration
status: complete
description: "Pattern where a main agent spawns independent sub-agents in parallel to delegate tasks."
created: 2026-04-12
updated: 2026-04-24
sources:
  - "https://simonwillison.net/guides/agentic-engineering-patterns/subagents/"
related:
  - "[[concepts/harness-engineering/agentic-workflows/subagents]]"
  - "[[concepts/agentic-engineering]]"
  - "[[concepts/cognitive-debt]]"
  - "[[concepts/multi-agent-consensus-patterns]]"
  - "[[concepts/harness-engineering]]"
---

# Subagents

A pattern where the main AI agent **spawns independent sub-agents in parallel**, each executing tasks in isolated context and terminal sessions.

## Three Design Principles

1. **Independence** — Sub-agents don't share the main conversation context. Instructions must be fully self-contained.
2. **Parallelism** — Execute multiple independent tasks concurrently (batch mode). Dramatically reduces wait time.
3. **Self-containment** — Explicitly pass necessary file paths, error messages, and constraints via the `context` field.

## When to Use

| ✅ Suitable | ❌ Not Suitable |
|-------------|---------------|
| Reasoning-heavy subtasks (debugging, code review, research) | Simple tasks not needing reasoning (`execute_code` is enough) |
| Large-scale data processing where context overflows | Single tool calls |
| Parallel independent workstreams | Tasks requiring user interaction |

## Important Constraints

- **Lossy Summary Problem**: Sub-agent return values (summaries) lack detailed information. For precision-sensitive decisions, make the main agent read the files directly.
- **Iteration Limit**: Sub-agents have a maximum iteration count (~50). Complex tasks may hit the limit.
- **No Context Sharing**: Main agent memory is not automatically shared.

## Implementation Pattern (Hermes)

```yaml
delegate_task:
  goal: "Research the latest developments in agentic engineering"
  context: "Focus on Simon Willison's blog posts from 2025-2026"
  toolsets: ["terminal", "web"]
  max_iterations: 50
```

Details: [[concepts/harness-engineering/agentic-workflows/subagents]]

## Related Concepts

- [[concepts/harness-engineering/agentic-workflows/subagents]] — Detailed implementation guide
- [[concepts/agentic-engineering]] — Parent concept
- [[concepts/cognitive-debt]] — Sub-agent self-containment reduces cognitive debt
- [[concepts/harness-engineering]] — Positioning as environment design philosophy

## Claude Code Sub-agent Implementation Details (2026-04)

### Built-in Sub-agents: Explore and Plan
Claude Code ships with sub-agents for common cases:
- **Explore**: Search the codebase without polluting main context. Runs `grep`, `find` calls in its own window, returns only relevant results
- **Plan**: Reads files, understands architecture, creates step-by-step implementation plans. Intermediate `read` calls don't appear in main context

### Context Forking (`CLAUDE_CODE_FORK_SUBAGENT=1`)
By default sub-agents start with blank context, but after spending 100K+ tokens building codebase understanding, you may want to inherit that understanding:
- `export CLAUDE_CODE_FORK_SUBAGENT=1` makes all sub-agent spawns inherit the parent's full context
- `/fork` slash command also enables on-demand forking
- Forked sub-agents:
  - Inherit parent's full conversation at fork time
  - Share prompt cache prefix with parent (child 2-N gets ~1/10th the input token cost)
  - Isolated execution so tool calls don't pollute the parent
  - Only return final summary

### Context-Timeline Hook
Tracking the main agent's context alongside parallel sub-agents is difficult. The `context-timeline` hook (https://www.aitmpl.com/component/hook/monitoring/context-timeline) displays a timeline from session start, tracking sub-agent spawning, completion, and result return in real time.

### Sub-agent Storage Locations
Stored in different locations by scope:
- `.claude/agents/` — committed to version control, shared with team
- `~/.claude/agents/` — personal, available everywhere
When sub-agents share a name, the higher-priority location wins.

## Skills and Subagents Interrelationship

Practical insight from @ankrgyl (2026-04-27):

Was spawning subagents in Claude Code to isolate main session context. Complex tasks were polluting the conversation window, consuming tokens, degrading reasoning ability. Just having subagents do heavy processing and return summaries fixed it.

Then Skills appeared, and started building a library of context, conventions, patterns, and domain knowledge, injected on-demand into Claude's tasks.

> "Now both exist at the same time, and they can compose in both directions. A skill can spawn a subagent, and a subagent can use skills."

This means Skills and Subagents are bidirectionally composable:
- **Skill → Subagent**: Spawn sub-agent from within a skill to delegate tasks
- **Subagent → Skill**: Sub-agents use skills to access domain knowledge

Reference: [Skills can use subagents, Subagents can use skills](../raw/articles/2041185537172607014_skills-can-use-subagents_-subagents-can-use-skills.md)

## Claude Agent SDK — Hub-and-Spoke Orchestration (Exam Knowledge)

From Claude Certified Architect exam Domain 1 (27%). Details: [[concepts/claude-certified-architect-domains]]

### Hub-and-Spoke Architecture

The coordinator is the Hub, sub-agents are Spokes. **All communication goes through the coordinator.** Sub-agents never communicate directly with each other.

### Isolation Principle (Most Tested on Exam)

- Sub-agents **do not automatically inherit** the coordinator's conversation history
- Sub-agents **do not share memory** across spawns
- All necessary information **must be explicitly passed in the prompt**
- This is the **#1 misconception** among exam takers. If not included in the prompt, the sub-agent doesn't know it.

### Task Tool

Mechanism for spawning sub-agents from the coordinator. `allowedTools` must include `"Task"`. Each sub-agent has an `AgentDefinition` (description, system prompt, tool restrictions). **Parallel spawning**: Issue multiple Task calls in a single response to simultaneously spawn multiple sub-agents.

### fork_session

Creates an independent branch. Used for divergent exploration from a shared baseline (e.g., comparing two different test strategies from the same codebase analysis).

### Narrow Decomposition Failure (Exam-Specific)

If the coordinator insufficiently decomposes a task, the failure is the **coordinator's responsibility**, not the downstream sub-agent's. The exam tests the ability to trace failure back to its source.

### Related

- [[concepts/claude-certified-architect-domains]] — Comprehensive knowledge of all 5 domains
- [[concepts/claude-code-best-practices]] — CLAUDE.md configuration patterns
- [[concepts/claude-agent-sdk-sre-patterns]] — Agent SDK + MCP SRE patterns
