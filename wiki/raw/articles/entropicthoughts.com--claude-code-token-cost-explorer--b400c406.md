---
title: "Claude Code token cost explorer"
url: "https://entropicthoughts.com/claude-code-token-cost-explorer"
fetched_at: 2026-11-11T10:01:31.209263+00:00
source: "entropicthoughts.com"
tags: [blog, raw]
---

# Claude Code token cost explorer

Source: https://entropicthoughts.com/claude-code-token-cost-explorer

I should say that the context cost explorer also lets us see a cumulative
picture of what the most expensive types of tokens are across all agents in a
session. In my example, that list mirrors the per-agent case:
Bash
calls most
expensive, followed by reasoning tokens, then the
Read
tool.
However, if we look at the most expensive individual items across all agents, we
find the initial instruction block at the top, contributing 7 % to the cost of
the session.
The reason instructions ended up most expensive, when each
individual agent has a
Bash
call as its most expensive token type, is that all
agents share the same initial instruction block, but they issue slightly
different expensive
Bash
calls. Thus, we need both the cross-agent view and
the per-agent view to optimise this rationally. The cross-agent view tells us of
the items that may be individually small, but which contribute a lot of cost due
to their wide inclusion in many subagents. The per-agent view tells us which
task-dependent items drive the usage of each agent.
