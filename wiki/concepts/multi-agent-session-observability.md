---
title: "Multi-Agent Session Observability"
created: 2026-10-16
updated: 2026-10-16
type: concept
tags: [developer-tooling, ai-agents, agent-observability, coding-agents]
aliases: [agent observability, session observability, agent visibility, multi-agent visibility]
sources:
  - raw/articles/2026-10-16_active-crawl-on-device-moe-and-review-bottleneck.md
confidence: medium
related:
  - "[[concepts/coding-agents/async-coding-agents]]"
  - "[[concepts/agent-harnesses]]"
  - "[[concepts/multi-agents/multi-agent-orchestration]]"
  - "[[concepts/evaluation/agent-observability]]"
---

# Multi-Agent Session Observability

## Definition

As developers run several coding agents concurrently (Claude Code, Codex, Mistral
Vibe, etc.), the binding problem shifts from *running* agents to *knowing what all of
them are doing right now*: who is working, who is blocked waiting on whom, and which
agent needs human input. **Multi-agent session observability** is the emerging tooling
layer that surfaces this state — a "control room" view over a fleet of local agents.

## The catalyst: Agent Standup

[[entities/agent-standup|Agent Standup]] (HN 217 points, Oct 11 2026) is the sharpest
early example. It turns running Claude Code / Codex / Mistral Vibe sessions into a
**live team call** — showing each agent's real commands, output, and the exact change
it's about to make, plus a tree of who-asked-whom. Its two design choices are the
interesting part:

- **Zero token cost.** It reads the session files those tools *already write* to disk.
  No LLM calls, nothing sent anywhere — pure parsing of existing transcripts. Works in
  VS Code, Cursor, a plain terminal, or as a desktop app.
- **Human-in-the-loop routing.** Its headline question is "who needs *you*" — it
  optimizes for directing scarce human attention to the agents that are blocked,
  rather than narrating everything.

## Why it matters for an agent wiki

- **It is the human-side answer to the async-agent problem.** [[concepts/coding-agents/async-coding-agents]]
  describes running agents unattended; observability is what keeps a human able to
  supervise several at once without becoming the bottleneck.
- **It reframes observability as a filesystem + UI problem, not an inference problem.**
  Because the session transcripts already exist, visibility can be added at zero token
  cost — a notable contrast to agent-eval approaches that spend tokens to score agents
  ([[concepts/evaluation/agent-observability]]).
- **Coordination state becomes first-class.** A "who waits on whom" tree is a dependency
  graph over agents — the operational cousin of [[concepts/multi-agents/multi-agent-orchestration]].

## Open questions

- As [[concepts/multi-agents/multi-agent-orchestration|orchestrator]] patterns standardize session
  formats, does observability become a built-in feature of the [[concepts/agent-harnesses|harness]], or stay a side tool?
- Zero-token transcript parsing vs. LLM-summarized dashboards — which scales when you
  run dozens of agents in parallel?
- Does visibility actually improve outcomes, or does a "standup of bots" add
  notification load without raising throughput (see the review-capacity limits in
  [[concepts/code-review-bottleneck]])?

## Sources

- Agent Standup — `https://atoll92.github.io/agent-standup/`
- Raw note: `raw/articles/2026-10-16_active-crawl-on-device-moe-and-review-bottleneck.md`
