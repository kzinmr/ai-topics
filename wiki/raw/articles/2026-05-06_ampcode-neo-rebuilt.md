---
title: "Amp, Rebuilt (Neo)"
source: https://ampcode.com/news/neo
date: "2026-05-06"
scraped: "2026-05-09"
author: Amp (Thorsten Ball / Sourcegraph)
tags:
  - coding-agents
  - agent-harness
  - amp
  - auto-compaction
  - plugin-api
  - remote-control
---

# Amp, Rebuilt — Codename: Neo

**Source:** https://ampcode.com/news/neo
**Published:** May 6, 2026

Today we're starting to roll out the new Amp. Not all of it, not yet. But the
first piece: a rebuilt Amp CLI. Codename: Neo.

In [The Coding Agent is Dead](https://ampcode.com/news/the-coding-agent-is-dead)
we wrote about where this is going: agents with longer leashes, less
handholding, and many more places to run. Not just one agent in one terminal.
Agents prompted from anywhere, running everywhere.

## Remote Control

When you start a thread in the new Amp CLI, you can now remote control it from
ampcode.com. You'll get live updates and can send messages, queue and dequeue
them, or cancel what the agent is currently doing.

## No More Manual Context Management

Today's leading frontier models are great at handling compaction. So Amp now
manages context for you. When the context window fills up, Amp automatically
compacts the thread: it summarizes the current context, starts a fresh window
with that summary, and keeps going. Compaction runs automatically when the
context window is 90% full.

Handoff is out. Compaction is in.

## Plugins — Amp Plugin API

With this release Amp officially released the Amp Plugin API. Plugins can:

- **Handle events** — `amp.on(...)` for tool calls, tool results, and agent lifecycle events
- **Add tools** — `amp.registerTool(...)` for custom tools the agent can call
- **Add commands** — `amp.registerCommand(...)` for command palette actions
- **Show UI elements** — `ctx.ui.notify(...)`, `ctx.ui.confirm(...)`, `ctx.ui.input(...)`, `ctx.ui.select(...)`
- **Ask AI questions** — `amp.ai.ask(...)` for yes/no classification with confidence and reasoning

A plugin is a single file in `.amp/plugins`. Example: `ask_user_choice` tool
that presents the user with a multiple choice question.

## Queuing & Steering

Queuing messages is now the default. When you send a message while the agent is
busy, it gets added to the queue instead of interrupting. Steering lets you
fast-track a queued message to be sent as soon as the next tool result arrives.

## Permissions

Amp no longer asks for permission before running tools. The old
`--dangerously-allow-all` flag is now the default. Frontier models now write
throwaway scripts and chain shell commands — it's near-impossible to determine
statically whether a tool invocation will be destructive. Permissions now live in
the Plugin API — build the policy that matches your setup.

## Performance & Efficiency (5000 message thread)

| Metric | Old CLI | Neo | Improvement |
|--------|---------|-----|-------------|
| CPU% (mean ± sd) | 84.1% ± 1.6% | 17.4% ± 8.8% | 79% less CPU |
| CPU% (peak) | 86.3% | 25.8% | — |
| Memory (idle) | 1814 MB | 540 MB | 70% less memory |

## What's Gone

- **Handoff** — Made obsolete by auto-compaction
- **Rollback on message edit** — Models are now good enough to undo changes with more finesse
- **Skill management** — Removed
