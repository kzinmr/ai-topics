---
title: "Claude Code /goal — Goal-Driven Autonomous Workflow"
type: concept
slug: claude-code-goal
status: complete
tags:
  - claude-code
  - coding-agents
  - agent-loop
  - ai-agents
  - anthropic
  - prompt-caching
  - tool
created: 2026-05-13
updated: 2026-05-13
aliases: [/goal, claude-goal, claude-code-autonomous-loop]
sources:
  - raw/articles/2026-05-13_anthropic_claude-code-goal.md
  - https://code.claude.com/docs/en/goal
---

# Claude Code /goal — Goal-Driven Autonomous Workflow

> **Definition:** `/goal` is a slash command in Claude Code that sets a **completion condition** and keeps Claude working autonomously across turns until the condition is met. After each turn, a small fast evaluator model (Haiku by default) checks whether the condition holds. If not, Claude starts another turn without requiring user input.

## Architecture: Prompt-Based Stop Hook

`/goal` is built on Claude Code's **hook system** — specifically, a **session-scoped prompt-based Stop hook**. This is the fundamental architectural difference from Codex `/goal`:

| Layer | Claude Code `/goal` | Codex `/goal` |
|-------|-------------------|---------------|
| **Underlying mechanism** | Prompt-based Stop hook | App-server state + `update_goal` tool |
| **Completion check** | Evaluator model (Haiku) judges condition from transcript | Agent calls `update_goal` tool to mark status |
| **Persistence** | Session-scoped (survives `--resume`) | App-server persistent state |
| **Condition format** | Natural language, max 4,000 chars | Structured objective |
| **Goal states** | Active / Achieved / Cleared | pursuing / paused / achieved / unmet / budget-limited |
| **TUI controls** | `/goal clear` only | `/goal pause`, `/goal resume`, `/goal clear` |

The evaluator model receives the condition + full conversation transcript and returns a binary yes/no decision with a short reason. It does **not** call tools — it can only judge what Claude has already surfaced in the transcript.

## The Goal Loop Lifecycle

```
┌─────────────┐     condition not met     ┌──────────────┐
│  User sets  │ ─────────────────────────→ │  Claude works │
│  /goal      │                            │  (one turn)   │
└─────────────┘                            └──────┬────────┘
                                                  │
                                          turn completes
                                                  │
                                                  ▼
                                    ┌──────────────────────┐
                                    │  Evaluator (Haiku)   │
                                    │  checks condition    │
                                    └──────┬───────────────┘
                                           │
                              ┌────────────┴────────────┐
                              ▼                         ▼
                         "Yes"                       "No"
                    condition met              reason + retry
                              │                         │
                              ▼                         │
                    ┌──────────────┐                   │
                    │  Goal achieved│                   │
                    │  cleared      │                   │
                    └──────────────┘                   │
                                                       │
                                          ┌────────────┘
                                          │
                                          ▼
                                    Claude gets reason
                                    as guidance for
                                    next turn ──────→ loop back
```

A goal keeps running until:
- The evaluator returns "Yes" → goal achieved, auto-clears
- User runs `/goal clear` (or aliases: `stop`, `off`, `reset`, `cancel`)
- User runs `/clear` to start a new conversation

## Comparison: Claude Code Autonomous Approaches

Three approaches keep the current session running between turns. Choose based on **what should trigger the next turn**:

| Approach | Trigger | Stops when | Best for |
|----------|---------|------------|----------|
| **`/goal`** | Previous turn finishes | Evaluator model confirms condition met | Goal-driven work (migrations, backlogs, multi-file refactors) |
| **`/loop`** | Time interval elapses | User stops it, or Claude decides done | Periodic checks, polling workflows |
| **Stop hook** | Previous turn finishes | Your script or prompt decides | Custom evaluation logic, deterministic checks |

### `/goal` vs `/loop`

- **`/goal`**: Condition-driven. "Work until X is true." Turns fire back-to-back as fast as Claude can work.
- **`/loop`**: Time-driven. "Check every N minutes." Turns fire on a schedule regardless of progress.

### `/goal` + Auto Mode

Auto mode (`--dangerously-skip-permissions` alternative) and `/goal` are **complementary**:
- **Auto mode** removes per-tool approval prompts within a turn
- **`/goal`** removes per-turn prompts between turns
- Together: fully unattended autonomous execution

The evaluator provides a critical safety layer — a **fresh model** (not the one doing the work) judges completion, reducing the risk of an agent incorrectly declaring itself "done."

## Effective Conditions

The evaluator cannot run commands or read files. Write conditions as something Claude's own output can demonstrate in the transcript:

| ❌ Avoid | ✅ Prefer |
|----------|----------|
| "The database is migrated" | "`rake db:migrate:status` shows all migrations as up" |
| "Everything is clean" | "`git status` is clean and `npm test` exits 0" |
| "The module is split" | "All files in `src/auth/` are under 200 lines and `npm test` passes" |

### Three Components of a Good Condition

1. **Measurable end state**: A test result, a build exit code, a file count, an empty queue
2. **Stated check**: How Claude should prove it — "`npm test` exits 0", "`git status` is clean"
3. **Constraints**: What must NOT change — "no other test file is modified", "don't touch `schema.rb`"

### Bounding Goal Duration

Include a turn or time clause to prevent infinite loops:
```
/goal all tests pass or stop after 20 turns
/goal the migration is complete, check with rake db:migrate:status, or stop after 30 minutes
```

Claude reports progress against the bound each turn, and the evaluator judges it from the conversation.

## Non-Interactive Mode

`/goal` works with `-p` for headless execution:

```bash
claude -p "/goal CHANGELOG.md has an entry for every PR merged this week"
```

This runs the entire goal loop to completion in a single CLI invocation. Interrupt with Ctrl+C.

## Requirements

- Must accept the **trust dialog** in the workspace (evaluator is part of hooks system)
- Unavailable when `disableAllHooks` is set at any settings level
- Unavailable when `allowManagedHooksOnly` is set in managed settings

Evaluation tokens are billed on the small fast model (Haiku) and are typically negligible compared to main-turn spend.

## Cross-Reference: Claude Code vs Codex /goal

Both products converged on goal-driven autonomous loops within weeks of each other (April–May 2026), reflecting the [[concepts/agentic-loop|agentic loop]] pattern's maturation:

| Dimension | Claude Code `/goal` | Codex `/goal` |
|-----------|-------------------|---------------|
| **Ship date** | ~April 2026 | April 30, 2026 (v0.128.0) |
| **Completion model** | External evaluator (Haiku) | Agent self-reports via `update_goal` |
| **Pause/Resume** | Not supported (clear + restart) | Full TUI controls |
| **External API** | Exposed via hook system | App-server REST API |
| **Budget mechanism** | Turn/time clauses in condition | Configurable token budget in `config.toml` |
| **Architecture philosophy** | "Evaluator judges agent" | "Agent knows its own state" |

→ See [[concepts/codex-goal]] for Codex `/goal` details and [[concepts/codex-goal-meta-prompting]] for meta-prompting workflows.

## Related Concepts

- [[concepts/agentic-loop]] — The canonical agent execution pattern all goal loops implement
- [[concepts/codex-goal]] — OpenAI Codex's `/goal` (Ralph loop++)
- [[concepts/codex-goal-meta-prompting]] — Using AI to generate better goal prompts
- [[concepts/karpathy-loop]] — Karpathy's fixed-budget autonomous ML research loop
- [[concepts/pi-autoresearch]] — Shopify's generalized metric optimization loop
- [[concepts/harness-engineering]] — Runtime infrastructure that makes goal loops reliable
- [[entities/claude-code--capabilities]] — Full Claude Code feature catalog

## References

- [Claude Code Docs — Goals](https://code.claude.com/docs/en/goal) — Official documentation
- [[raw/articles/2026-05-13_anthropic_claude-code-goal.md]] — Full doc page extraction
