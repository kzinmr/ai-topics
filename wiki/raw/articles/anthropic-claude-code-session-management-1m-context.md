---
title: Using Claude Code: Session Management & 1M Context
category: other
status: active
---

# Using Claude Code: Session Management & 1M Context

**Source:** Anthropic (claude.com/blog)
**Author:** Thariq Shihipar
**Date:** April 15, 2026
**URL:** https://claude.com/blog/using-claude-code-session-management-and-1m-context

## Core Concepts & Mechanics

- **Context Window:** 1,000,000 tokens. Contains system prompt, full conversation history, every tool call/output, and all read files.
- **Context Rot:** Performance degradation as context grows. Attention dilutes across tokens, and older/irrelevant content distracts from the current task.
- **Compaction:** Automatic or manual summarization triggered near the context limit. Replaces full history with a condensed summary. *Note: Context windows are a hard cutoff.*
- **New Feature:** `/usage` slash command released to help track consumption and session metrics.

## Session Management Strategies

Every completed turn presents a branching point. Choose based on task continuity and context relevance:

| Strategy | Command / Action | When to Use |
|:---|:---|:---|
| **Continue** | Send next prompt | Context remains fully relevant; avoids rebuilding state. |
| **Rewind** | `/rewind` or `Esc Esc` | Claude took a wrong path. Drops subsequent messages, preserves useful file reads, lets you re-prompt with new constraints. |
| **Compact** | `/compact` | Session is bloated with stale debugging/exploration. Low-effort, AI-summarized history. Can be steered: `/compact focus on auth refactor, drop test debugging`. |
| **Clear** | `/clear` | Starting a genuinely new task. Zero rot. You manually distill what matters into a fresh brief. |
| **Subagents** | Explicit prompt or auto-trigger | Next step will generate heavy intermediate output where only the conclusion matters. Child gets a clean context window. |

## Decision Matrix

| Situation | Consider reaching for | Why |
|:---|:---|:---|
| Same task, context is still relevant | `Continue` | Everything in the window is still load-bearing; don't pay to rebuild it. |
| Claude went down a wrong path | `Rewind` (`Esc Esc`) | Keep the useful file reads, drop the failed attempt, re-prompt with what you learned. |
| Mid-task but session is bloated with stale debugging/exploration | `/compact` | Low effort; Claude decides what mattered. Steer it with instructions if needed. |
| Starting a genuinely new task | `/clear` | Zero rot; you control exactly what carries forward. |
| Next step will generate lots of output you'll only need the conclusion from (codebase search, verification, doc writing) | `Subagent` | Intermediate tool noise stays in the child's context; only the result comes back. |

## Best Practices & Pro Tips

- **Proactive Compaction:** With 1M tokens, you have more runway to `/compact` *manually* before hitting limits. This lets you specify focus areas and prevent lossy summaries.
- **Avoid Bad Autocompacts:** These occur when the model can't predict your next direction (e.g., after a long debugging session, you pivot to a different warning). Manual compaction or `/clear` prevents critical context from being dropped.
- **Subagent Prompting:** Explicitly trigger subagents for isolated, high-output tasks:
  ```text
  "Spin up a subagent to verify the result of this work based on the following spec file"
  "Spin off a subagent to read through this other codebase and summarize how it implemented the auth flow, then implement it yourself in the same way"
  "Spin off a subagent to write the docs on this feature based on my git changes"
  ```
- **Cost/Speed Tradeoff:** Reusing context (`Continue`/`/compact`) avoids re-reading files, saving time and tokens compared to `/clear`. Only clear when the task fundamentally shifts.

## Key Excerpts

> "Context rot is the observation that model performance degrades as context grows because attention gets spread across more tokens, and older, irrelevant content starts to distract from the current task."

> "The mental test we use at Anthropic: will I need this tool output again, or just the conclusion?"

> "Bad compacts can happen when the model can't predict the direction your work is going... With one million context, you have more time to `/compact` proactively with a description of what you want to do."
