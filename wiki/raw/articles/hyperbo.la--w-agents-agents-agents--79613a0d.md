---
title: "Agent Utilization Is the New Performance Ceiling"
url: "https://hyperbo.la/w/agents-agents-agents/"
fetched_at: 2026-04-29T07:02:15.003642+00:00
source: "hyperbola :: blog"
tags: [blog, raw]
---

# Agent Utilization Is the New Performance Ceiling

Source: https://hyperbo.la/w/agents-agents-agents/

Intelligence from the models is directly related to token consumption — that is
the core insight behind reasoning models and chain-of-thought. Every engineer,
and eventually every human, should be running at high token utilization.
A billion tokens per engineer per day is a utilization target. It asks how much
of the software lifecycle the agents are actually allowed to do.
Writing patches is a small slice of the job. Most of the software lifecycle is
reading logs, checking traces, diffing behavior across releases, chasing down
performance regressions, inspecting crash dumps, following analytics, tightening
invariants, and proving that a fix actually worked.
As of March 2026, the numbers I have are 3-5 PRs per engineer per day on GPT-5.2
without Symphony and about 75 PRs per engineer per week with Symphony. The
difference is utilization. Symphony keeps the agent busy.
Utilization drops anywhere the agent cannot see or act. Datadog, Grafana, and
Statsig matter. Slack and Google Drive matter when the context lives there.
Deploy tooling, Linear, local dev environments, and web search matter too. If
the agent cannot inspect the traces, launch the app, check the analytics, or
land the fix, it sits idle.
Most software work is the long middle: opening the dashboard, checking the
trace, reproducing the bug, diffing the release, finding the bad assumption, and
proving the fix in a real system.
Utilization is what turns model intelligence into engineering output. Idle
agents usually mean missing access, missing context, or a human gate.
