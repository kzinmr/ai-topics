---
title: "Practical multi-agent orchestration in Codex"
author: eric provencher (@pvncher)
date: 2026-07-24
type: x_article
source_url: https://x.com/pvncher/status/2080707291603407077
article_url: https://x.com/i/article/2080691655238107136
ingested: 2026-07-25
tags:
  - codex
  - multi-agent
  - orchestration
  - gpt-5.6-sol
  - openai
  - agent-coordination
  - reasoning-effort
  - agent-harnesses
---

# Practical multi-agent orchestration in Codex

*By Eric Provencher ([@pvncher](https://x.com/pvncher)), Codex DX @ OpenAI*

GPT-5.6 Sol gets especially interesting when it has a team to work with. Codex's new Multi-Agent V2 tools give Sol and Terra a natural way to delegate tasks, share updates, and coordinate through complex tasks.

Ultra makes agent coordination the default and is best reserved for high-stakes work, where ambiguity or scattered context justify the added depth.

For other tasks, a short prompt or skill can encourage the same collaborative behavior from Sol Medium, as it stays in conversation with you while organizing the work behind the scenes. With the right nudge, Sol can turn broad requests into focused assignments, bringing in other agents, and deciding when a problem calls for deeper reasoning.

## Match reasoning to the work

While it's possible to have Sol delegate to another model like Terra, the simplest setup keeps one model family and adjusts only the reasoning effort, with dedicated roles like so:

- **Scout** — GPT-5.6 Sol Light. Answer narrow, read-only questions: locate files, trace a code path, or find relevant tests.
- **Worker** — GPT-5.6 Sol Medium. Implement scoped changes, run checks, or handle supporting work.
- **Smart worker** — GPT-5.6 Sol High. Take on difficult implementation, resolve ambiguity, or coordinate help when useful.

Treat these roles as useful defaults. Sol Light retains the judgment to find useful context without spending as much reasoning on discovery.

## Let the team coordinate

The coordinator acts as the primary delegator: it assigns substantive work, avoids duplicate investigations, and tracks what each agent is doing. Scouts can investigate in parallel, while workers can share implementation when responsibilities are clear.

Agents can also message one another directly through a common messaging system with separate inboxes. When a scout discovers something a worker needs, it can recognize the dependency and pass along its findings without waiting for the coordinator to relay them.

Concurrency is configurable per thread and defaults to four agents, including the coordinator. Within that budget, a smart worker might coordinate a scout and another worker, or the coordinator could send three scouts to investigate separate questions.

## Choose what context agents inherit

Forking conversation history helps agents understand the broader goal and earlier decisions. Starting with fork_turns: "none" gives an agent a fresh, focused assignment instead. Fresh-context agents can still recognize when a teammate needs information and contact them independently.

Agents that inherit their parent's context may also see its orchestration instructions. When an agent should remain a leaf, give it a short boundary:

> Complete this assignment directly. Do not spawn other agents; your parent's delegation instructions apply only to your parent.

Fresh-context agents won't inherit task-specific tool or safety boundaries, so include any essential restrictions directly in their assignments.

## Capture the pattern in a skill

A practical skill can give the coordinator a few standing instructions:

> Stay available to the user while delegating substantive work. Send focused, read-only scouts out in parallel with reasoning_effort: "low" and fork_turns: "none". Use reasoning_effort: "medium" for routine implementation and reasoning_effort: "high" for harder problems. Give each agent clear ownership, avoid overlapping assignments, and tell leaf workers not to delegate. Bring the results together and keep approvals with the user.

## Experiment with the knobs

Start with these defaults, then experiment with reasoning effort, context inheritance, delegation authority, and how agents collaborate. The goal is to understand which settings help a team move the work forward without spending more reasoning than the task requires.
