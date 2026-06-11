---
title: "Claude Code as a Coding Agent"
created: 2026-05-20
updated: 2026-06-01
type: concept
tags:
  - claude-code
  - coding-agents
  - ai-agents
  - multi-agent
  - orchestration
  - agent-safety
  - agentic-engineering
  - mcp
  - prompting
  - infrastructure
  - developer-experience
  - ai-adoption
  - strategy-execution
  - feedback-loop
  - shopify
  - optimization
sources: [raw/articles/2026-05-20_zodchiii_shopify-claude-code-setup.md, raw/articles/2026-05-20_pragmatic-engineer_farhan-thawar-shopify-ai.md, raw/articles/2026-05-28_anthropic-claude-code-dynamic-workflows.md]
---

# Claude Code as a Coding Agent

Claude Code is [[entities/anthropic|Anthropic]]'s AI coding agent — a CLI tool that operates as an autonomous developer within a codebase. While the tool itself is well-documented, the emerging patterns for *how* large engineering organizations deploy it as team infrastructure represent a distinct body of knowledge. This page focuses on the operational patterns, workflows, and guardrails that turn Claude Code from a single-user assistant into **team-scale coding infrastructure**, as practiced by [[entities/shopify|Shopify]] across 23,000 engineers.

## The Infrastructure Layer

Before any agent patterns work, organizations need a unified infrastructure layer. Shopify built an internal **LLM proxy** ([[concepts/shopify-ai-engineering#llm-proxy-architecture|→ Shopify AI Engineering]]) that routes every AI request — from Claude Code, GitHub Copilot, Cursor, and other tools — through a single gateway. This provides centralized cost control, usage analytics, and the ability to swap models without changing any engineer's workflow.

The lesson: don't standardize on one tool. Standardize the layer *underneath* the tools.

### Dynamic Workflows (May 2026)

In May 2026, Anthropic introduced **Dynamic Workflows** for Claude Code as a research preview. This feature represents a fundamental shift in how Claude Code approaches large-scale codebase operations:

- **Hundreds of parallel subagents** per session — Claude Code plans a task, dynamically spins up parallel subagents, and coordinates their output
- **Codebase-scale migrations** across 100,000+ lines from kickoff to merge
- **Full workflow pipeline**: task planning → parallel execution → verification → merge
- **Dynamic agent spawning** based on task complexity — the system allocates more subagents for more complex tasks

This capability builds on the parallel agent patterns already used by organizations like Shopify (documented in [[concepts/claude-code#Pattern-1-Parallel-Agents-Not-Single-Chat|Pattern 1]]), but automates the orchestration layer that previously required manual engineer coordination.

Dynamic Workflows represents Anthropic's move toward automated multi-agent orchestration at scale, where the tool itself handles subagent spawning, work distribution, and output verification rather than requiring the engineer to manually launch and monitor parallel agents.

## Pattern 1: Parallel Agents, Not Single Chat

The foundational pattern shift: Claude Code is not a single-prompt-single-response tool at scale. Senior engineers launch **multiple agents simultaneously**, each working on different parts of the codebase:

- One agent refactors the auth module
- Another writes tests
- A third updates documentation
- The engineer reviews outputs, discards what doesn't work, merges what does

The engineer's role shifts from *writing code* to **reviewing and merging agent outputs**. [[entities/farhan-thawar|Farhan Thawar]] (VP Engineering at Shopify) describes this as "orchestrating intelligent systems." This is [[concepts/harness-engineering/agentic-design-patterns|agentic design patterns]] at production scale — engineers become orchestrators of parallel agent fleets rather than line-by-line authors.

This pattern maps to the broader [[multi-agent]] and [[concepts/multi-agents/agent-orchestration]] paradigm: the unit of work is not a prompt but a **delegated subtask with independent execution**.

## Pattern 2: Extended Critique Loops

Not every task benefits from parallelism. For complex architectural decisions, Shopify engineers run a single agent through **extended critique loops** — the agent generates an answer, evaluates it, revises it, and continues refining over long reasoning cycles.

Instead of accepting the first output, the agent is forced to argue with itself:

```text
"Propose an architecture for [X].
Then critique your own proposal: what breaks at scale?
Then revise based on your critique.
Then critique the revision.
Give me the final version with confidence levels for each decision."
```

This produces dramatically better results because Claude catches its own mistakes before a human has to. The pattern leverages the model's ability to self-correct through [[chain-of-thought]] reasoning and structured [[feedback-loop|feedback loops]].

**Key insight**: this is not just "ask twice." The structure — *propose → critique → revise → critique → finalize* — creates a deliberate adversarial dynamic that surfaces edge cases and assumptions that single-pass prompting misses.

## Pattern 3: MCP Integration (Shopify AI Toolkit)

In April 2026, Shopify released an open-source [[mcp|MCP]] server that connects Claude Code directly to Shopify's documentation, GraphQL API schemas, and live store operations:

```bash
claude mcp add --transport stdio shopify-dev-mcp -- npx -y @shopify/dev-mcp@latest
```

This gives Claude Code 7 tools:
- Search current Shopify docs (not stale training data)
- Validate GraphQL queries against live schemas
- Execute store operations through Shopify CLI
- Create products, manage metafields, modify themes
- Run bulk operations with natural language

Without MCP, Claude hallucinates API fields and invents component patterns. With it, Claude works with **real platform data** — grounding LLM outputs in live schemas eliminates a major class of [[ai-coding]] errors.

The broader trend: MCP servers are being built by non-engineering teams (finance, sales, support) within Shopify, connecting Claude Code to Salesforce, Google Calendar, Gmail, and Slack — all without engineer help. This represents a significant [[vibe-coding]] democratization of tool-building.

## Pattern 4: CLAUDE.md as Team Infrastructure

CLAUDE.md is not personal config. At Shopify, it's **team infrastructure** committed to git and shared across all 23,000 engineers:

```markdown
# CLAUDE.md (Shopify internal pattern)

## Stack
Ruby on Rails, React, GraphQL, MySQL

## Commands
- Dev: `dev up && dev server`
- Test: `dev test [path]`
- Lint: `dev style`
- Type check: `bin/srb tc`

## Architecture
- app/models/ → ActiveRecord models, business logic
- app/controllers/ → thin controllers, delegate to services
- app/services/ → service objects for complex operations
- app/graphql/ → GraphQL types, mutations, resolvers

## Rules
- NEVER bypass Sorbet type checking
- All new code must have type signatures
- Database queries only through established patterns
- IMPORTANT: run `dev test` after every change
```

**Critical constraint**: keep CLAUDE.md under 60 lines. Stuffing it with every standard and convention makes performance *worse*, not better — you pay for all of it on every turn. The document serves as **context injection** that sets the agent's baseline understanding of the codebase, stack, and conventions.

This aligns with [[developer-experience]] best practices: the configuration is minimal, version-controlled, and shared. When a new engineer joins, the CLAUDE.md is part of the repo they clone — the agent inherits team conventions automatically.

## Pattern 5: Strategy-First Validation

Shopify flipped the engineering time ratio:

```
2024 workflow:
Strategy: 30% → Execution: 70%

2026 workflow (Shopify):
Strategy: 70% → Execution: 30%
```

Because AI handles most coding, engineers now spend 70% of time on **strategy**: mapping user flows, validating market demand, choosing the right architecture. Only 30% on execution. This represents an estimated ~20% productivity improvement — not from writing more code, but from **testing 10 approaches instead of 2**, faster prototyping, and higher-fidelity deliverables.

This shift embodies [[strategy-execution]] rebalancing: the bottleneck moves from "can we build it?" to "should we build it?" and "what's the right way?" The agent handles the *how*; the engineer focuses on the *what* and *why*.

## Pattern 6: Safe Autonomy with Guardrails

Shopify doesn't let agents run wild. Their permission-based guardrail system:

```json
{
  "permissions": {
    "allow": [
      "Read", "Glob", "Grep", "LS", "Edit",
      "Bash(dev test *)",
      "Bash(dev style *)",
      "Bash(git status)",
      "Bash(git diff *)",
      "Bash(git add *)",
      "Bash(git commit *)"
    ],
    "deny": [
      "Read(**/.env*)",
      "Bash(git push *)",
      "Bash(dev deploy *)",
      "Bash(bin/rails db:drop *)",
      "Bash(rm -rf *)"
    ],
    "defaultMode": "acceptEdits"
  }
}
```

Agents can read, write, test, and commit. They **cannot** push to remote, deploy to production, drop databases, or read secrets. A human stays in the loop for anything irreversible.

This is [[agent-safety]] at the operational level: explicit allowlists and denylists create a **bounded autonomy** zone where agents can work freely without risking production systems. The `acceptEdits` default mode means agents can edit files without constant human approval, but the denylist prevents escape from the sandbox.

## Configuration and Prompt Patterns

### Minimal Effective CLAUDE.md
- **Stack**: one line per technology (Ruby on Rails, React, GraphQL, MySQL)
- **Commands**: 3-5 essential dev commands (dev, test, lint, type check)
- **Architecture**: directory-to-responsibility mapping (app/models/ → business logic)
- **Rules**: hard constraints (NEVER bypass type checking), test-after-change requirement
- **Total**: under 60 lines — larger files degrade performance on every turn

### Parallel Agent Workflow
1. Identify independent subtasks (different files/modules)
2. Launch 2-3 agents in separate terminals
3. Each agent receives a focused prompt for its subtask
4. Engineer reviews all outputs, merges what works, discards what doesn't

### Critique Loop Prompt Pattern
```
"Propose [solution]. Critique your proposal. Revise. Critique again. 
Give final version with confidence levels per decision."
```

### Guardrail Setup
- **Allow**: read, write (via Edit), test, lint, commit
- **Deny**: push, deploy, database drops, secret access, destructive filesystem operations
- **Default mode**: acceptEdits

## Adoption Path for Teams

1. **Standardize CLAUDE.md** — stack, commands, architecture, rules. Under 60 lines. Commit to git.
2. **Set up parallel agents** — 2-3 agents in separate terminals for larger tasks
3. **Install relevant MCP servers** — connect to your stack's APIs (GitHub, Slack, database)
4. **Add guardrails** — allow read/write/test/lint/commit, deny push/deploy/delete/secrets
5. **Flip the ratio** — spend 70% on strategy, let agents handle execution

## Current State and Trajectory

Shopify targets 90% autonomous coding by Q3 2026 with 23,000 engineers working toward it. The 20% productivity gain comes not from writing more code but from exploring more approaches, prototyping faster, and catching mistakes earlier. The teams getting the most out of Claude Code aren't the ones with the best prompts — they're the ones who built the infrastructure to let agents work **safely, in parallel, on real codebases**.

## See Also

- [[concepts/shopify-ai-engineering]] — Shopify's AI-first engineering approach
- [[entities/claude-code]] — Claude Code entity overview
- [[entities/shopify]] — Shopify entity page
- [[entities/anthropic]] — Anthropic
- [[concepts/harness-engineering/agentic-design-patterns]] — Agentic design patterns
- [[entities/farhan-thawar]] — Farhan Thawar (VP Engineering, Shopify)
- [[entities/coding-agents]] — Coding agents ecosystem overview
