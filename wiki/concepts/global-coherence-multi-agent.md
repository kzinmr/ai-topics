---
title: "Global Coherence Problem (Multi-Agent Collaboration)"
created: 2026-10-03
updated: 2026-10-03
type: concept
tags: [concept, multi-agent, agent-orchestration, agent-architecture, agent-coordination, agentic-rl, state-management, ai-agents]
aliases: [global coherence, observation-aliasing, local-to-global semantics]
confidence: medium
sources: ["raw/articles/arxiv-2610.02036-global-coherence-local-to-global-multi-agent.md"]
---

# Global Coherence Problem (Multi-Agent Collaboration)

The **global coherence problem**: AI agents can each make locally valid decisions yet *jointly*
produce an invalid result. Heng (arXiv:2610.02036, Oct 2026) reframes this as **a failure of
shared state, not of model intelligence** — the counter-intuitive core claim being that *local
intelligence cannot substitute for missing global state*.

This is a harness-side diagnosis that complements the better-known "smarter model" reflex: when a
multi-agent team fails, the instinct is to upgrade the model. This paper argues the failure can be
*unfixable by more intelligence* if the missing information simply isn't in any agent's context.

## The impossibility boundary

The **Observation-Aliasing Impossibility Theorem** gives an exact boundary:

> A policy can guarantee a valid action **exactly when** all worlds producing the same observation
> share an admissible action. If *k* indistinguishable worlds require pairwise-disjoint actions,
> the best *randomized* worst-case success is **1/k**; more reasoning, roles, messages, or samples
> cannot recover the missing distinction.

The intuition: a stronger model reasons better *within its context*, but it cannot see *beyond* it.
If the deciding fact was never delivered into the agent's observation, no amount of added
reasoning/budget/roles recovers it — the ceiling is information-theoretic, not computational.

## Local-to-global runtime semantics

The paper proposes a formal runtime `X = (H, C, G, F; D)` where **models propose and the harness
owns shared state and governs commit**:

| Symbol | Role |
|--------|------|
| `H` topology | records overlapping scopes |
| `C` category | governs state-changing actions |
| `G` groupoid | retains reversible translations |
| `F` sheaf | tests whether local views *glue* into one world |
| `D` minimal history | keeps only distinctions that alter legal futures |

This positions the [[concepts/harness-engineering]] layer (not the model) as the owner of the
"one world" property — an explicit *sheaf/gluing* framing for whether independently-correct agent
views compose into a single consistent state.

## Evidence (9 studies)

- **Controlled revision benchmark:** the same frontier model scores **40/40** when the deciding
  event is *visible*; when *hidden*, arms score **12–17/40**, consistent with chance (1/3).
  Restoring **one** authoritative fact returns **40/40** — proof the deficit was a single missing
  fact, not capability.
- **TeamBench shared budget:** ordinary teams exceed a shared budget in **5/5** runs; a *visible
  live count* reduces violations to **4/5**; *commit enforcement* by the harness leaves **0/5**.
- **tau2-bench Telecom:** after *silent reverts*, current-state checks score **0.07**, while the
  harness (which owns true state) scores **1.00**.
- **Boundary check:** where a conventional solver already owns the complete relevant state, it
  ties the harness — as the theorem predicts.

## Why it matters

- Reframes a whole class of multi-agent failures as **observability/state-ownership gaps**, aligning
  with the harness-owns-state thesis in [[concepts/harness-engineering]].
- Provides a *negative* result worth heeding before buying scale: adding agents, roles, or
  reasoning tokens does not help when the bound is 1/k aliasing.
- The "restore one authoritative fact → 40/40" result is a cheap intervention: **authoritative
  shared state + commit enforcement**, not model upgrades.

## Open questions

- The theorem's *k* (number of indistinguishable worlds) is a modeling choice — real systems rarely
  expose a clean discrete set of aliased worlds.
- Single-author, single-source paper (`confidence: medium`); the sheaf/groupoid formalism has not
  yet been reproduced or adopted elsewhere.
- Relationship to distributed-systems consensus (which also bounds what local views can agree on)
  is asserted but not formally connected.

## Related

- [[concepts/multi-agents/multi-agent-systems]] — the collaboration substrate this diagnoses
- [[concepts/harness-engineering]] — the "harness owns shared state, governs commit" thesis
- [[concepts/agent-orchestration-runtime]] — where the commit/state boundary is enforced
