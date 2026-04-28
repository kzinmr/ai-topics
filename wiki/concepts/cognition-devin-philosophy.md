---
title: "Cognition/Devin Philosophy"
tags: [agentic-engineering-cognition-devin-multi-agents-orchestration]
created: 2026-04-23
updated: 2026-04-24
type: concept
---

# Cognition/Devin Philosophy — Agentic Coding at Scale

Cognition Labs（CEO: Scott Wu @ScottWu46）の Devin チームが発信する、AI coding agent に関する一貫した哲学。

> "I think the most important insight from Cognition is that **context continuity beats parallelism**." — Walden Yan

## Core Thesis: Don't Build Multi-Agents (Walden Yan)

Cognition's fundamental position on multi-agent systems:

- **Single-threaded agents with context continuity outperform parallel multi-agent systems**
- Handoffs between agents lose critical context — "the devil is in the details"
- A single agent with a long context window that can maintain its own thread of thought is more reliable than multiple specialized agents
- **Context continuity** > **parallelism** for most coding tasks

### Key Insight

> "Eventually, the future comes." — Scott Wu

Cognition believes that as context windows grow and models improve, a single Devin instance with persistent memory will handle tasks that currently require multi-agent orchestration.

## 100x Capability Growth

### "Eventually, the Future comes" — Devin Major Update (Apr 2026)

Scott Wu (@scottwu46) and Cognition announced one of the biggest updates to Devin since launch. Key metrics:

| Metric | 2024 | 2026 (current) | Growth |
|--------|------|----------------|--------|
| METR: autonomous task complexity | <5 min human-equivalent tasks | 6+ hour human-equivalent tasks | ~100x capability |
| Internal PRs/week (Cognition) | ~154 (best week 2025) | ~659 (Apr 2026) | 4.3x |
| Enterprise customer sessions/week | Baseline | Doubling every ~6 weeks | ~65x in 13 months |

> "Most folks in code were still focused on tab-complete, but we wanted to build for the future instead." — Scott Wu
> "When you build for the future... eventually the future comes." — Scott Wu

### The "Devin, but good" Philosophy

Cognition explicitly doubled down on the original Devin form-factor rather than pivoting:

- **Same core**: async workflow, cloud VM, browser use, Slack/Linear/GitHub integrations
- **Not a pivot**: "The core form-factor is just good old Devin... Devin, but good"
- **Key improvements shipped**:
  1. Startup time improved 3x
  2. Slack & Linear integrations smoothed
  3. End-to-end testing with computer use
  4. Devin Review → Autofix + GitHub comments (closing the loop)
  5. Hundreds of UX/design/functionality fixes

### SWE-bench Scores (from Devin Review blog)

SWE-bench Verified scores are from the separate Devin Review blog post, not this update announcement:
- SWE-bench Verified: 66.1%
- SWE-bench Verified (METR-evaluated): 71.7%

### The "Closing the Agent Loop" Philosophy

Devin's approach to the full development cycle:

1. **Write code** → 2. **Catch issues** (CI/linters/review) → 3. **Autofix** → 4. **Merge**

Key: The agent doesn't just write code and stop — it handles the entire loop including responding to PR review comments.

> "Devin can now close the loop — writing code, catching CI failures, and fixing review comments autonomously."

## Context Anxiety (Sonnet 4.5 Lessons)

With Claude Sonnet 4.5 integration, Cognition discovered:

- **Context anxiety** — agents become unreliable when context windows exceed model-specific thresholds
- **Single-tasked agents** are more reliable than multi-purpose agents
- **Explicit context management** is critical for long-running agent sessions
- Model-specific limits exist and must be respected (different for each model/provider)

## Managed Devins (Devin 2.2)

Cognition's evolved approach to multi-agent coordination:

- **NOT** the traditional multi-agent pattern (many agents working in parallel on the same task)
- **Instead**: A single Devin instance that can conditionally spawn managed sub-Devins for specific subtasks
- The manager Devin maintains context continuity while delegating discrete, well-bounded tasks
- This is Cognition's answer to "don't build multi-agents" — **build a managed Devin fleet instead**

### Architecture

```
┌─────────────────────────────────────────┐
│           Manager Devin                 │
│  (maintains full context + thread)      │
│                                         │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐ │
│  │Sub-Devin│  │Sub-Devin│  │Sub-Devin│ │
│  │(scoped) │  │(scoped) │  │(scoped) │ │
│  └─────────┘  └─────────┘  └─────────┘ │
└─────────────────────────────────────────┘
```

## Nader Dabit: Agentic Slack & Agents From Anywhere

Cognition Growth Engineer Nader Dabit (@dabit3) extends the philosophy:

### Agentic Slack

- **Slack as an agent interface** — agents operate asynchronously in team communication channels
- Agents don't need to live in terminals or IDEs
- **Fire-and-forget** task delegation via Slack threads
- Human-AI collaboration happens in the same space as human-human collaboration

### Agents From Anywhere

- **Mobile-first agent orchestration** — manage agents from anywhere, not just at your desk
- The future of agent interaction is not tied to a specific workspace
- **Cross-platform agent access** — terminal, IDE, Slack, mobile
- Democratizes access to AI-powered development

> "Engineering for agents that never sleep" — agents operate 24/7, humans review and direct

## Comparison: Cognition vs Anthropic vs OpenAI

| Dimension | Cognition/Devin | Anthropic | OpenAI |
|-----------|-----------------|-----------|--------|
| Multi-agent | Conditional/managed sub-agents | Brain/Hands/Session separation | Symphony workflows |
| Context | Single-threaded continuity | Context engineering | Dynamic token curation |
| Agent interface | IDE + Slack + Mobile | Terminal (Claude Code) | Terminal + API |
| Philosophy | "Context continuity beats parallelism" | "Evaluation-first engineering" | "Workflow orchestration" |
| Key metric | 100x capability growth | Vibe coding → Agentic engineering | Workflows > Agents |

## See Also

- [[concepts/closing-agent-loop]] — Full development loop (Write→Catch→Fix→Merge)
- [[concepts/agent-team-swarm/managed-devins]] — Conditional multi-agent architecture
- [[concepts/harness-engineering/system-architecture/context-anxiety]] — Context window limits
- [[concepts/multi-agent-autonomy-scale]] — 5 levels of multi-agent autonomy
- [[scott-wu]] — Cognition CEO
- [[nader-dabit]] — Cognition Growth Engineer
- [[walden-yan]] — Cognition engineer ("Don't Build Multi-Agents")
