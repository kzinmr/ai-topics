---
title: "Agent Standup"
created: 2026-10-16
updated: 2026-10-16
type: entity
tags: [tool, developer-tooling, ai-agents, open-source, agent-observability]
aliases: [agent-standup]
sources:
  - raw/articles/2026-10-16_active-crawl-on-device-moe-and-review-bottleneck.md
confidence: medium
related:
  - "[[concepts/multi-agent-session-observability]]"
  - "[[concepts/coding-agents/async-coding-agents]]"
  - "[[concepts/agent-harnesses]]"
---

# Agent Standup

## Overview

**Agent Standup** is a free, open-source tool that turns concurrent AI coding-agent
sessions (Claude Code, Codex, Mistral Vibe) into a **live team-call view** — showing
which agent is working, which is blocked waiting on another, and which needs the human
developer. It gained attention on Hacker News (217 points, Oct 11 2026) as an early,
concrete instance of [[concepts/multi-agent-session-observability]].

## How it works

- **Reads existing session files.** It parses the transcript files that Claude Code,
  Codex, and Mistral Vibe already write to disk, so it works wherever those tools run:
  VS Code (extension, panel + sidebar), Cursor, a plain terminal, or a desktop app.
- **Zero token cost.** It makes no LLM calls and sends nothing anywhere — it is pure
  local parsing. Install via VS Code Marketplace or `npx @double_geste/agent-standup`.
- **Who-waits-on-whom tree.** It renders a dependency graph of agent requests and a
  shared-screen view of each agent's real commands, output, and pending change.

## Why it matters

Agent Standup operationalizes supervision of parallel agents — the practical companion
to [[concepts/coding-agents/async-coding-agents]]. Its notable design bet is that
agent *visibility* is a filesystem + UI problem solvable at zero token cost, rather
than an inference problem requiring the model to summarize itself. It is one data
point for where agent [[concepts/agent-harnesses|harness]] tooling goes as developers
juggle fleets of agents rather than a single assistant.

## Sources

- Project page: `https://atoll92.github.io/agent-standup/`
- Raw note: `raw/articles/2026-10-16_active-crawl-on-device-moe-and-review-bottleneck.md`
