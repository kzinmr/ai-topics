---
title: "Loop Engineering"
created: 2026-06-21
updated: 2026-06-21
type: concept
tags:
  - concept
  - ai-agents
  - coding-agents
  - agentic-engineering
  - harness-engineering
  - agent-loop
  - orchestration
  - claude-code
  - prompting
  - self-correction
  - loops
aliases:
  - loop-engineering
  - designing-loops
related:
  - "[[concepts/agent-loop-orchestration]]"
  - "[[concepts/harness-engineering/agentic-loop]]"
  - "[[entities/peter-steinberger]]"
  - "[[entities/boris-cherny]]"
  - "[[entities/elvis-saravia]]"
sources:
  - raw/articles/2026-06-19_omarsar0_from-prompting-agents-to-loop-engineering.md
---

# Loop Engineering

**Loop Engineering** is the discipline of designing autonomous loop systems that prompt, verify, and iterate with coding agents — moving the developer's role from writing prompts to writing the system that writes the code. Articulated as a paradigm shift by Peter Steinberger (@steipete) and Boris Cherny (@bcherny) in mid-2026, it represents the maturation of agentic coding from one-shot prompting to durable, self-correcting infrastructure.

> "You shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents." — Peter Steinberger, June 2026

> "I don't prompt Claude anymore. I have loops that are running. They're the ones that are prompting Claude and figuring out what to do. My job is to write loops." — Boris Cherny

## The Loop Paradigm

A loop is a small program that does four things:

1. **Prompts** the coding agent
2. **Reads** what it produced
3. **Decides** whether it is done
4. **Re-prompts** with the error or next step if not

The developer stops sitting inside the loop typing prompts; instead, the model becomes a subroutine the loop calls. The shape is always the same: set a goal → act → check → feed back → repeat until the check passes or the loop stops itself.

## Five Meanings of "Loop"

The term "loop" in AI coding carries at least five distinct meanings, in chronological order:

| # | Name | Era | Description |
|---|------|-----|-------------|
| 1 | **ReAct** | 2022 | Original research pattern: reason → act → observe → repeat |
| 2 | **AutoGPT** | 2023 | Self-prompting goal loop, notorious for not knowing when to stop |
| 3 | **ralph loop** | 2024–25 | Deliberate context reset between iterations to prevent history drowning |
| 4 | **/loop and /goal** | 2025–26 | Cadence and completion conditions built into the agent, carrying state across turns |
| 5 | **orchestration** | 2026 | One author fans out many agents that read GitHub, Slack, and chat, and decide what to build next |

## Six Building Blocks

Every production loop assembles six components, most of which now ship as built-in features of coding tools:

| # | Component | Description |
|---|-----------|-------------|
| 1 | **Trigger** | Schedule, webhook, file change, or PR label that starts the loop without manual intervention |
| 2 | **Isolation** | Private checkout per agent (git worktree) to prevent file conflicts between concurrent agents |
| 3 | **Written-down context** | Conventions, build steps, and rules in files the agent reads on every run (CLAUDE.md, AGENTS.md) |
| 4 | **Tool reach** | Connectors to issue tracker, CI, database, and chat for autonomous PR creation and notification |
| 5 | **Independent verifier** | A separate agent grades output — the producing agent cannot judge its own work |
| 6 | **State on disk** | Markdown file, board, or queue outside the conversation that survives between runs |

## The PR Babysitter Pattern

A canonical loop example that can be built today:

| Dimension | Setting |
|-----------|---------|
| Trigger | Every 15 minutes |
| Scope | Open PRs labeled `agent-watch` |
| Action | If CI red (deterministic), attempt one fix. If main moved, rebase once |
| Budget | One fix per PR, 5 minutes, 10 files |
| Stop | CI green or budget exhausted → ping human |

The same shape covers CI health monitoring, deploy verification, and feedback clustering.

## Claude Code /goal Loop

The `/goal` command in Claude Code is the smallest complete loop shipped inside an agent. It defines a verifiable end state and keeps taking turns until that state is true. A strong `/goal` specifies four things:

1. **End state** — what you want achieved
2. **Evidence** — how to prove it was reached (test result, exit code, file count)
3. **Constraints** — what the agent must not break
4. **Budget** — max turns, time, files, or cost

The evaluator step uses a fast model distinct from the coder, enabling role-based model selection: some models plan better, some execute cheaper, some judge more accurately.

## Unattended Multi-Agent Loops (Cherny's Five Steps)

Boris Cherny's setup for running Opus autonomously for hours:

```
claude --permission-mode auto                          # 1 · no approval prompts
ultracode  orchestrate sub-agents to ship the feature  # 2 · fan out
/goal all tests pass and the demo loads clean          # 3 · keep going
→ cloud / desktop app                                  # 4 · close the laptop
→ chrome ext · sim MCP · live server                   # 5 · self-verify, then halt
```

## crabfleet: Loop Infrastructure as Product

Peter Steinberger's **crabfleet** (an [[entities/openclaw|OpenClaw]] project) packages loop engineering as product infrastructure:

- **Kanban board as loop queue** — tasks move through todo → running → human review → done
- **Durable execution** — heartbeats and state survive closed laptops
- **Agent fan-out** — child sessions spawn from within sandboxes with on-disk memory
- **Disposable cloud sandboxes** — browser-based terminals for safe unattended runs

## Economics of Loop Engineering

Loop engineering shifts the cost model from per-call to per-task:

- **Iterations are the budget line, not tokens.** A cheaper model that loops twice as often is not cheaper. Track cost per finished task.
- **A weak verifier is the most expensive bug.** If the "done" check is loose, the loop stops early on broken work or grinds indefinitely.
- **Failing fast is cost control.** A loop with no cap on consecutive failures eventually drains the account, not succeeds.

## When NOT to Loop

Loops only pay off when a task repeats and a machine can tell when it's done:

| Anti-pattern | Why |
|-------------|-----|
| One-shot edits | Pure overhead if a single pass suffices |
| Unscoped/exploratory work | No pass condition → never converges |
| No automated check | If the only verifier is human eyes, you are still inside the loop |

## Failure Modes

- **Human verification debt** — the loop writes faster than you can review; not reviewing defers work, doesn't remove it
- **Comprehension gaps** — shipping unread code erodes system understanding, surfacing during incidents
- **Silent drift** — a weak verifier lets wrong-but-passing work through, making the loop look productive while digging a hole

## Relationship to Adjacent Concepts

- [[concepts/agent-loop-orchestration]] — The technical architecture of the think-act-evaluate cycle. Loop engineering is the engineering discipline that designs, budgets, and productionizes those cycles.
- [[concepts/harness-engineering/agentic-loop]] — The ralph loop pattern of deliberate context resets between iterations. Loop engineering's six building blocks extend this into full infrastructure.
- [[concepts/compound-engineering-every]] — Matt Van Horn's related framework for compound engineering loops.
- [[concepts/codex/codex-agent-loop]] — Codex CLI's specific loop implementation (user→model→tool→repeat).

## Sources

- [[raw/articles/2026-06-19_omarsar0_from-prompting-agents-to-loop-engineering]] — Elvis Saravia, "From Prompting Agents to Loop Engineering" (Jun 19, 2026). DAIR.AI Academy.
- Peter Steinberger (@steipete), "Design Loops, Don't Prompt Agents" (Jun 7, 2026). Original tweet: 2.2M views.
- Boris Cherny (@bcherny), on running agents autonomously and loop authoring.
