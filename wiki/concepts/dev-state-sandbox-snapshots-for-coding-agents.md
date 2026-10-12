---
title: "Returning to Development States — Sandbox Snapshots for Coding Agents"
created: 2026-10-12
updated: 2026-10-12
type: concept
tags: [coding-agents, sandbox, durable-execution, ai-agents, agent-runtime]
sources: [raw/papers/2026-10-09_2610.13841_dev-state-sandbox-snapshots-coding-agents.md]
confidence: medium
related: [concepts/security-and-governance/agent-sandboxing, concepts/durable-execution, concepts/agent-runtime-and-sandboxes]
---

# Returning to Development States — Sandbox Snapshots for Coding Agents

Coding agents often make real progress before they fail — but `retry-from-scratch` throws away
the *machine state* built along the way. Graviet & Shah (arXiv:2610.13841, Oct 2026) reframe
failure recovery as a **search problem over environment states**, and find the value of that
search lives mostly *outside the repository*.

## Method

They implement **Go-Explore-style search over full Daytona snapshots**: instead of restarting
from the initial state, the agent restores and branches from intermediate machine states that
preserved useful progress. The archive of "interesting" states is what Go-Explore contributes —
keep diverse frontier states and return to them rather than greedily continuing one trajectory.

## Key finding

Higher and more *efficient* solve rates depend mainly on progress that sits **outside the
repository**: databases, running services, and other runtime state. The implication:

- When a task's real progress is captured by a git diff, snapshots add little — a diff already
  reconstructs the state.
- Full-snapshot search pays off when long-horizon coding work **spans multiple services whose
  state cannot be reconstructed from a single diff** (migrations applied to a DB, a service left
  in a warm state, external side effects).

## Why it matters

This makes the *environment* — not just the transcript — a first-class object in agent
[[concepts/durable-execution]]. It sits at the intersection of two wiki themes: the
[[concepts/security-and-governance/agent-sandboxing]] literature (which treats snapshots mostly
as an isolation/isomorphism boundary) and the long-horizon harness work. If progress is
recoverable only from machine state, then snapshot/branch infrastructure becomes part of the
agent's problem-solving capability, not just its safety envelope.

## Caveats

Abstract-only; exact solve-rate deltas, model, and task suite are not disclosed. Marked
`confidence: medium`. The Go-Explore framing and the "state outside the repo" conclusion are the
durable claims.

## Related

- [[concepts/security-and-governance/agent-sandboxing]]
- [[concepts/durable-execution]]
- [[concepts/sandbox]]
