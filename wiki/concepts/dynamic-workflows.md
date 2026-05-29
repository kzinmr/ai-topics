---
title: Dynamic Workflows (Claude Code)
created: 2026-05-29
updated: 2026-05-29
type: concept
tags: [claude-code, anthropic, coding-agents, subagents, orchestration, agent-orchestration, workflow, ai-agents, multi-agent, verification, test-time-scaling]
aliases: [ultracode, dynamic-workflows]
related: [rlm-recursive-language-models, agent-orchestration-frameworks, agent-loop-orchestration, dspy-rlm, subagents]
sources: [raw/articles/2026-05-28_anthropic_dynamic-workflows-claude-code.md]
---

# Dynamic Workflows (Claude Code)

**Dynamic Workflows** is a Claude Code feature (research preview, May 2026) that enables Claude to dynamically write orchestration scripts that spawn tens to hundreds of parallel subagents in a single session, with built-in verification and convergence loops. It represents a shift from single-agent loops to **model-coordinated multi-agent orchestration at scale**.

## Architecture

A dynamic workflow is a **JavaScript orchestration script** that coordinates subagents at scale. Unlike traditional agent loops where Claude is the orchestrator deciding turn-by-turn, the workflow script holds the loop, branching, and intermediate results **outside Claude's conversation context**. Key architectural properties:

| Component | Description |
|---|---|
| **Orchestration script** | JavaScript; Claude writes it dynamically based on the task; can be read, rerun, and modified |
| **Subagents** | Up to 16 concurrent, 1,000 total per run; each independent with its own context |
| **Execution environment** | Isolated from conversation; intermediate results stay in script variables, not Claude's context |
| **Verification** | Adversarial agents attempt to refute findings; results checked before integration |
| **Convergence loop** | Iterates until answers converge — achieves results a single pass cannot |
| **Resilience** | Progress saved continuously; interrupted jobs resume from where they left off |

## How It Works

1. **Planning & Decomposition** — Claude plans dynamically based on the prompt, breaking the task into subtasks
2. **Parallel Execution** — Subagents run independently in parallel, with the script managing coordination
3. **Verification** — Results are checked before integration; other agents try to refute what was found
4. **Convergence Loop** — Run iterates until answers converge, reaching results a single pass cannot
5. **Conversation Independence** — Coordination happens outside the conversation context; plan stays on track regardless of task size

## Ultracode Mode

**Ultracode** (`/effort ultracode`) combines `xhigh` reasoning effort with automatic workflow orchestration. With ultracode on, Claude decides when a task warrants a workflow — a single request can spawn multiple workflows in sequence (understand → change → verify). This marks the transition from human-initiated workflows to **model-determined orchestration strategy**.

## Relationship to Recursive Language Models (RLM)

Dynamic Workflows have sparked significant discussion about their relationship to [[concepts/rlm-recursive-language-models]]. Alex Zhang (@a1zhang), creator of the RLM framework, claims Opus 4.8 + Dynamic Workflows constitutes "perhaps the first instance of a frontier model seriously trained to be an RLM."

Zhang's broader observation: "The last few releases in Claude Code have moved away from standard ReAct-style loops with JSON tool-calling to more of this abstraction." Dynamic Workflows represent the culmination of a directional shift — from turn-by-turn human-in-the-loop tool calls toward model-determined orchestration with programmatic sub-agent invocation. Each incremental Claude Code release has moved closer to RLM-like abstractions; DW is the point where the convergence became undeniable.

In a May 28, 2026 clarification, Zhang explicitly defined what RLM does and does not claim, emphasizing that the novelty is in **composition + sufficiency** — which specific components are assembled, and the argument that no additional components are needed. See the [[concepts/rlm-recursive-language-models#what-rlm-is-and-is-not-author-clarifications|RLM page: Author Clarifications]] for the full scope definition.

See [[concepts/rlm-recursive-language-models#from-2-axis-to-3-axis-programmatic-sub-agent-calling-psac|RLM page: 3-Axis Framework]] for the full structural comparison between Task Decomposition (multi-agent), Context Decomposition (RLM), and Programmatic Sub-Agent Calling (Dynamic Workflows).

### The 3-Axis Structural Framework

Dynamic Workflows complete a structural triad with RLM and PTC:

| Axis | Paradigm | Operation | Direction |
|------|----------|-----------|-----------|
| **Data Axis** | RLM | Split 1 huge context → N pieces | Disaggregate (read) |
| **Function Axis** | PTC | Merge N tool calls → 1 code block | Aggregate (write) |
| **Agent Axis** | DW / PSAC | Spawn 1 script → N sub-agents | Delegate (orchestrate) |

Where RLM decomposes **data** and PTC composes **functions**, Dynamic Workflows (as Programmatic Sub-Agent Calling) delegates **execution** — the model generates its own agent harness infrastructure. This is captured by @nickadobos's formulation: "RLM on agent harnesses" — the model vibecodes a custom sub-agent fleet harness for each task.

## Case Study: Bun Zig → Rust Migration

Jarred Sumner used Dynamic Workflows to port Bun from Zig to Rust:

| Metric | Result |
|---|---|
| Lines of Rust | ~750,000 |
| Test suite pass rate | 99.8% |
| Time from first commit to merge | 11 days |
| Reviewers per file | 2 (adversarial verification) |
| Workflow stages | Lifetime mapping → file-by-file port → fix loop → optimization pass |

## Use Cases

- **Codebase-wide audits**: Bug hunts, profiler-guided optimization, security audits across entire services
- **Large migrations**: Framework swaps, API deprecations, language ports spanning thousands of files
- **High-stakes verification**: Adversarial agents attempt to break solutions before delivery; independent angles cross-checked
- **Multi-angle planning**: Plans stress-tested from different perspectives before commitment

## Constraints

| Constraint | Details |
|---|---|
| Concurrent agents | Up to 16 (fewer on limited CPU cores) |
| Total agents per run | 1,000 |
| Mid-run user input | Not supported (only agent permission prompts) |
| Filesystem access | Through subagents only; script itself has no direct access |
| Token consumption | Significantly more than typical sessions |

## Availability

- Claude Code CLI, Desktop, VS Code extension
- Max, Team plans (on by default); Enterprise (admin-enabled)
- Claude API, Amazon Bedrock, Vertex AI, Microsoft Foundry

## See Also

- [[concepts/rlm-recursive-language-models]] — The theoretical framework that Dynamic Workflows partially instantiate
- [[concepts/agent-orchestration-frameworks]] — Broader comparison of multi-agent orchestration approaches
- [[concepts/subagents]] — The subagent spawning primitive that Dynamic Workflows scale to hundreds
- [[concepts/agent-loop-orchestration]] — Traditional single-agent loop vs. workflow orchestration
