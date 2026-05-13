---
title: "Codex /goal — OpenAI's Built-in Ralph Loop"
type: concept
slug: codex-goal
status: complete
tags: [coding-agents, codex, openai, cli, agent-loop, ralph-loop, autonomous-agents, self-improving]
created: 2026-05-13
updated: 2026-05-13
aliases: [/goal, codex-goal-command, openai-goal-loop]
sources:
  - raw/articles/2026-05-11_chrishayduk-using-codex-goals-effectively.md
  - https://ralphable.com/blog/codex-goal-command-ralph-loop-openai-built-in-autonomous-coding-agent-2026
  - https://x.com/ChrisHayduk/status/2053807198870880743
---

# Codex /goal — OpenAI's Built-in Ralph Loop

> **Definition:** `/goal` is a slash command in Codex CLI (shipped in v0.128.0, April 30, 2026) that turns Codex into a **long-horizon autonomous agent**. It runs the canonical [[concepts/agentic-loop|agentic loop]] — plan → act → verify → correct — for **hours** of continuous work in a single invocation.

Greg Brockman summarized it: *"codex now has a built in Ralph loop++."*

## What It Ships

| Feature | Description |
|---------|-------------|
| **Persisted goals** | First-class objects in Codex app-server state, survive across turns, compactions, and `/clear` |
| **Runtime continuation** | After each turn, if goal isn't `achieved` and budget remains, runtime injects `continuation.md` and re-invokes the model |
| **Model tools** | `update_goal` tool the agent calls to mark status (structured, not text) |
| **TUI controls** | `/goal pause`, `/goal resume`, `/goal clear` |
| **App-server APIs** | External tooling can create, query, pause, resume goals |

## Enabling

```toml
# ~/.codex/config.toml
[features]
goals = true
```

## Goal Lifecycle States

| State | Meaning |
|-------|---------|
| `pursuing` | Agent actively working. Continuation prompt injected each turn. |
| `paused` | Agent stopped mid-work. `/goal resume` to continue. |
| `achieved` | Agent marked the goal as complete. Loop stops. |
| `unmet` | Agent determined the goal cannot be met. Loop stops. |
| `budget-limited` | Token budget exhausted. Loop stops with partial results. |

## The Two Prompts That Power It

### `continuation.md` (injected each turn)
The runtime injects a system prompt telling the agent: "You are in a goal loop. The objective is still being pursued. Continue making progress. Use `update_goal` to mark your status."

### `budget_limit.md` (injected when budget runs low)
Warns the agent that token budget is nearing its limit. The agent should wrap up work, commit partial progress, and call `update_goal` with `budget-limited`.

## `/goal` vs Hand-Rolled Bash Ralph Loop

| Aspect | Hand-Rolled Bash | `/goal` Built-in |
|--------|-----------------|-----------------|
| **Setup** | Write bash script with `DONE`/`BLOCKED` files, iteration counters | `codex features enable goals` + `/goal <objective>` |
| **Persistence** | File-based state, fragile | App-server state, survives `/clear` |
| **Token budget** | Manual iteration counter | Configurable in `config.toml` |
| **Audit** | Manual log parsing | Structured `update_goal` tool calls |
| **TUI integration** | None | Full slash-command surface |
| **Model awareness** | None (model doesn't know it's in a loop) | System prompts tell the model about its goal state |

## When to Use `/goal`

✅ **Use `/goal` when:**
- Long-horizon autonomous work (hours+)
- Clear, measurable objectives
- You trust the agent to self-correct
- You want structured audit trail of goal states

❌ **Skip `/goal` when:**
- Short, interactive tasks (single prompt is faster)
- High-uncertainty work where human judgment is needed frequently
- You need fine-grained control over each iteration
- You're already in an AI-assisted IDE (Cursor, Copilot chat)

## Effective Goal Prompting (Chris Hayduk's Tips)

[[entities/chris-hayduk|Chris Hayduk]] (FDE @ OpenAI) — who uses goal mode internally at OpenAI and in side projects — shares practical advice for getting the most out of `/goal`. The key insight: **goal mode requires different prompting than normal Codex usage**.

### 1. Specify a Clear, Quantitative Goal

Models have gotten so good that many of us have gotten lazy as prompters. Vague prompts like "make the app faster" work in interactive mode because you'll course-correct. In autonomous goal mode:

| ❌ Bad | ✅ Good |
|--------|---------|
| "Make the app faster" | "Reduce TTI from 3.2s to under 1.5s, maintain Lighthouse > 90" |
| "Improve the codebase" | "Reduce build time by 40% without changing any test expectations" |
| "Fix the bugs" | "Close all 12 open issues in the `auth` module, verify with existing tests" |

### 2. Be Explicit About Constraints

- What NOT to change (e.g., "don't touch the database schema")
- What architectural patterns to follow
- Files/directories the agent can modify

### 3. Define Done with Verification Steps

Without a clear definition of done, the agent will either stop early or loop forever. Include:
- Specific test criteria ("all 342 existing tests must pass")
- Acceptance tests or verification scripts
- Quantitative thresholds

### 4. Meta-Prompting for Better Goals

Use AI to write better `/goal` prompts:
1. Open a fresh Codex session with full project context
2. Ask it to research how `/goal` actually works
3. Have it inspect your codebase for high-leverage missions
4. Ask it to produce complete goal prompts with scope, constraints, and definitions of done

→ See [[concepts/codex-goal-meta-prompting|Codex /goal Meta-Prompting]] (Aditya Bawankule's workflow)

### 5. Practical Guardrails

- **Start small** — don't jump to "rebuild the entire frontend"
- **Define file scope** — which files/directories can be modified
- **Test suites as guardrails** — instruct agent to keep all tests passing
- **Set clear budget limits** — configure token budgets in `~/.codex/config.toml`
- **Review agent commits** — valid optimizations often mix with hacks that need reverting

> *Source:* [[raw/articles/2026-05-11_chrishayduk-using-codex-goals-effectively.md]] — Chris Hayduk, "Using Codex Goals Effectively" (May 11, 2026)

## Token Budget Design

The Ralphable blog recommends **token budget over iteration count**:
- Iteration limit → agent rushes near the limit
- Token budget → agent allocates tokens naturally across thinking and action
- Default: configure in `~/.codex/config.toml`

## Related Concepts

- [[concepts/agentic-loop]] — The canonical agent execution pattern
- [[concepts/karpathy-loop]] — Autonomous ML research variant
- [[concepts/pi-autoresearch]] — Generalized metric optimization (Shopify)
- [[concepts/codex-goal-meta-prompting]] — Using AI to generate better /goal prompts
- [[concepts/ralph-loop]] — The Ralph Wiggum loop pattern (if exists)
- [[concepts/self-improving-agents]] — Agents that improve over multiple runs

## References

- [Codex /goal Command: Deep Dive](https://ralphable.com/blog/codex-goal-command-ralph-loop-openai-built-in-autonomous-coding-agent-2026) — Ralphable Blog, May 2026
- [Codex CLI v0.128.0 Release Notes](https://github.com/openai/codex/releases)
- [Greg Brockman's X post](https://x.com/gdb/status/1915497181795295268) — "codex now has a built in Ralph loop++"
- [[raw/articles/2026-05-04_adityabawankule-codex-goal-meta-prompting.md]]
