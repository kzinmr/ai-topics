---
title: "How Coding Agents Work"
type: concept
created: 2026-04-25
updated: 2026-11-19
tags:
  - concept
  - coding-agents
  - agent-loop
  - tool-use
  - agent-architecture
aliases:
  - coding agent internals
  - agent loop
sources:
  - raw/articles/2025-08-29_humanlayer-advanced-context-engineering-coding-agents.md
  - wiki/concepts/coding-agent-harness-design-study.md
related:
  - "[[concepts/agent-loop-orchestration]]"
  - "[[concepts/harness-engineering]]"
  - "[[concepts/harness-engineering/system-architecture/context-engineering]]"
status: active
---

# How Coding Agents Work

A **coding agent** is an LLM running inside a *harness* that gives it tools (shell, file edit, search), a loop that feeds tool results back as new context, and guardrails (sandbox, permissions, checkpoints). The model itself only produces text; the harness turns that text into actions and turns the results of those actions back into prompts. This page is the canonical end-to-end explanation of that loop.

## The Core Loop

```
┌──────────────────────────────────────────────────────┐
│                      Harness                          │
│                                                      │
│  System prompt + tool schemas + AGENTS.md/CLAUDE.md  │
│           │                                          │
│           ▼                                          │
│       ┌───────┐   tool call    ┌──────────────────┐  │
│       │  LLM  │ ─────────────► │ Tool executor    │  │
│       └───────┘                │ (bash, edit, grep)│  │
│           ▲                    └────────┬─────────┘  │
│           │   tool results appended     │            │
│           └─────────────────────────────┘            │
│                      (loop until stop / approval)    │
└──────────────────────────────────────────────────────┘
```

1. **Prompt assembly** — the harness builds context: system prompt, tool definitions, project instructions (`AGENTS.md` / `CLAUDE.md`), conversation history, and recent tool outputs.
2. **Model turn** — the LLM either emits a tool call (JSON matching a declared schema) or a final answer. Reasoning models may emit an internal chain of thought first.
3. **Tool execution** — the harness parses the call, enforces permissions/approvals, runs it (often in a sandbox or container), and captures stdout/stderr/diffs.
4. **Feedback** — results are appended to the transcript and the loop repeats. Termination is triggered by the model's stop token, a user message, or harness policy (max turns, token budget).

See [[concepts/agent-loop-orchestration]] for control-flow variants (sequential, parallel subagents, plan-then-execute) and [[concepts/harness-engineering]] for the umbrella "Agent = Model + Harness" thesis.

## The Tool Surface

Modern coding agents converge on a small, orthogonal tool set:

| Tool | Purpose | Design note |
|------|---------|-------------|
| `read` / `view` | File contents with line numbers | Pagination + "did you mean" fuzzy suggestions |
| `edit` / `apply_patch` | Targeted find-and-replace | Fuzzy matching tolerates whitespace drift |
| `write` | Whole-file creation | Paired with syntax checks after write |
| `search` (ripgrep/glob) | Content + filename search | Replaces grep/find/ls; ranked, bounded output |
| `terminal` / `bash` | Arbitrary shell | Persistent sessions, background jobs, PTY mode |
| `task` / `subagent` | Spawn a scoped child agent | Fresh context window per subtask |

Key insight from harness design studies: **tool descriptions are prompts**. A model that misuses a tool is usually being misdescribed by it — see [[concepts/harness-engineering/system-architecture/writing-tools-for-agents]].

## Context Management (the hard part)

- **Context rot**: long transcripts degrade accuracy; naive history append eventually poisons the window ([[concepts/context-engineering/context-rot]]).
- **Compaction**: harnesses summarize old turns or drop stale tool outputs when the window fills ([[concepts/harness-engineering/system-architecture/context-compaction]]).
- **Retrieval on demand**: agents pull files/tokens via search tools instead of pre-loading everything — "agentic search beats embedding search" is a recurring finding ([[concepts/agentic-retrieval]], [[concepts/search-as-code]]).
- **Instructions files**: `AGENTS.md` / `CLAUDE.md` act as durable, project-scoped memory injected every turn ([[concepts/agents-md-evaluation]]).

## Verification & Reliability Loops

Reliable agents interleave **execution with verification**: run tests after edits (first-run-the-tests), lint/typecheck after writes, request subagent review, and treat failing output as new context rather than giving up. Cost/complexity budgets cap how long a loop may run (Lee Rob's complexity-budgets pattern). See [[concepts/harness-engineering/agentic-workflows/first-run-the-tests]] and [[concepts/coding-agents/ai-coding-reliability]].

## Failure Modes

- **Looping**: repeating a failing command without changing strategy (mitigate with turn budgets and reflection).
- **Premature stopping**: declaring victory without verification (mitigate with explicit done-criteria).
- **Context poisoning**: one bad tool dump skews all later turns (mitigate with truncation + structured tool output).
- **Permission theater vs. real sandboxing**: approval prompts are UX; containers/network egress control are security ([[concepts/harness-engineering/system-architecture/agent-security-patterns]]).
- **Model drift across harness migrations** ([[concepts/agent-model-drift]]).

## Where to go next

- Conceptual framework: [[concepts/harness-engineering]] — "Agent = Model + Harness".
- Workflow patterns humans use around agents: [[concepts/harness-engineering/agentic-workflows/how-agents-work]], [[concepts/harness-engineering/agentic-workflows/prompt-driven-development]].
- Security view: [[concepts/ai-agent-security]], [[concepts/prompt-injection]].
- Comparison of concrete harnesses: [[concepts/coding-agent-harness-design-study]].

## Sources

- Anthropic, "Building effective agents" — via [[concepts/harness-engineering/system-architecture/building-effective-agents]]
- HumanLayer, "Advanced context engineering for coding agents" (raw article above)
- Simon Willison, Agentic Engineering Patterns — https://simonwillison.net/guides/agentic-engineering-patterns/
