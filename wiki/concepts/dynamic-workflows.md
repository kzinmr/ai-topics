---
title: "Dynamic Workflows in Claude Code"
created: 2026-06-02
updated: 2026-06-02
type: concept
tags:
  - claude-code
  - harness-engineering
  - coding-agents
  - multi-agent
  - ai-agents
  - workflow
  - orchestration
  - anthropic
sources: [raw/articles/2026-06-02_trq212_dynamic-workflows-claude-code.md]
---

# Dynamic Workflows in Claude Code

Dynamic workflows are a feature in [[concepts/claude-code|Claude Code]] that allow Claude to **dynamically generate its own agent harness** (written in JavaScript) at runtime, tailored to the specific task at hand. Released in early June 2026, this capability represents a shift from static, pre-built orchestration to on-the-fly [[concepts/harness-engineering|harness engineering]] driven by the model itself.

## Core Concept

Instead of relying on a fixed harness for all tasks, Claude can now **write a custom JavaScript workflow file** that spawns and coordinates [[concepts/harness-engineering/agent-harness|subagents]], each with their own context window, model selection, and isolation level. The workflow file uses special functions to spawn agents, wait for results, and synthesize outputs.

Key properties:
- **JavaScript-based**: Workflows execute as JS files with special agent-spawning functions plus standard JS (JSON, Math, Array)
- **Model routing**: The workflow can choose which model each subagent uses (e.g., Sonnet for simple tasks, Opus for complex reasoning)
- **Worktree isolation**: Subagents can run in isolated git worktrees, preventing interference
- **Resumable**: If interrupted (user action, terminal quit), the workflow resumes where it left off
- **Shareable**: Workflows can be saved to `~/.claude/workflows` and distributed via skills

## Motivation: Why Dynamic Harnesses?

When Claude works in a single context window on complex tasks, it becomes susceptible to failure modes that dynamic workflows structurally mitigate:

| Failure Mode | Description | How Workflows Help |
|---|---|---|
| **Agentic laziness** | Declares task done after partial progress (e.g., reviews 20 of 50 items) | Separate agents with focused scope can't skip items |
| **Self-preferential bias** | Prefers its own results when asked to verify them | Adversarial verification agents have no bias toward the original |
| **Goal drift** | Loses fidelity to original objective across many turns, especially after compaction | Each subagent has a clean context window with the original goal |

Dynamic workflows address these by orchestrating **separate Claudes with their own context windows and focused, isolated goals** — a direct application of [[concepts/harness-engineering|harness engineering]] principles.

## Workflow Patterns

Six composable patterns emerge from the dynamic workflows design:

### 1. Classify-and-Act
A classifier agent decides the task type, then routes to different specialized agents or behaviors.

### 2. Fan-Out-and-Synthesize
Split a task into many smaller steps, run an agent on each step in parallel, then synthesize results. The synthesize step acts as a **barrier** — it waits for all fan-out agents before merging structured outputs. Useful when each step benefits from a clean context window.

### 3. Adversarial Verification
For each spawned agent, run a separate agent to adversarially verify its output against a rubric or criteria. Structurally prevents self-preferential bias.

### 4. Generate-and-Filter
Generate many ideas, then filter by rubric or verification, deduplicate, and return only the highest quality results.

### 5. Tournament
Spawn N agents that each attempt the same task using different approaches. A judging agent evaluates results pairwise until a winner emerges. Comparative judgment is more reliable than absolute scoring.

### 6. Loop Until Done
For tasks with unknown workload, loop spawning agents until a stop condition is met (no new findings, no more errors) rather than a fixed number of passes.

## Use Cases

Dynamic workflows extend [[concepts/claude-code|Claude Code]] beyond traditional coding into structured, adversarial, and research-heavy tasks:

- **Migrations and refactors**: Bun was rewritten from Zig to Rust using workflows — spin off a subagent per fix in a worktree, adversarially review, then merge
- **Deep research**: Fan-out web searches, fetch sources, adversarially verify claims, synthesize a cited report (available as `/deep-research` skill)
- **Deep verification**: Identify all factual claims in a report, spin off a subagent per claim to verify
- **Sorting/ranking**: Tournament or pairwise-comparison pipeline for qualitative sorting (e.g., 80 resumes)
- **Memory and rule adherence**: Verifier agents check each rule, skeptic persona prevents false positives; mine sessions for recurring corrections
- **Root-cause investigation**: Generate hypotheses from disjoint evidence (separate agents for logs, files, data), then verify/refute
- **Triaging at scale**: Classify, dedupe, and act on support queues with quarantine pattern for untrusted content
- **Exploration and taste**: Generate solutions, evaluate against rubric, tournament selection
- **Lightweight evals**: Spin off agents in worktrees, compare outputs against rubric
- **Model routing**: Classifier agent routes to Sonnet or Opus based on task complexity

## Integration Points

Dynamic workflows integrate with existing Claude Code features:

- **`/goal`**: Set hard completion requirements for workflows
- **`/loop`**: Run repeatable workflows (triage, research, verification) at regular intervals
- **Token budgets**: Set explicit caps via prompting (e.g., "use 10k tokens")
- **Skills**: Save workflows as JavaScript files in skill folders, reference in SKILL.md
- **Trigger word**: "ultracode" ensures Claude Code creates a workflow

## Dynamic vs Static Workflows

| Aspect | Static Workflow | Dynamic Workflow |
|---|---|---|
| Definition | Pre-built (Claude Agent SDK, `claude -p`) | Generated on-the-fly by Claude |
| Generality | Generic, covers all edge cases | Tailor-made for specific use case |
| Intelligence | Fixed orchestration logic | Leverages Claude Opus 4.8 reasoning |
| Token cost | Lower (fixed logic) | Higher (model generates harness) |
| Best for | Known, repeatable workflows | Novel, complex, or creative tasks |

## When NOT to Use

Dynamic workflows are not needed for every task and use significantly more tokens. Regular coding tasks that don't require multi-agent orchestration, adversarial verification, or parallel decomposition do not benefit from workflows. The key question: **does this task really need more compute?**

## Related Concepts

- [[concepts/claude-code|Claude Code as a Coding Agent]]
- [[concepts/harness-engineering|Harness Engineering]]
- [[concepts/harness-engineering/agent-harness|Agent Harness]]
- [[concepts/claude/opus-4-8|Claude Opus 4.8]] — the model that makes dynamic workflows intelligent enough to generate custom harnesses
- [[concepts/claude-code-goal|Claude Code /goal]]
- [[concepts/claude-code-skills|Claude Code Skills]]
- [[concepts/anthropic/multi-agent-research|Anthropic Multi-Agent Research System]]
- [[concepts/claude-code-best-practices|Claude Code Best Practices]]

## Authors

Thariq Shihipar ([@trq212](https://x.com/trq212)) and Sid Bidasaria ([@sidbid](https://x.com/sidbid)) are members of technical staff at [[entities/anthropic|Anthropic]], working on Claude Code.
