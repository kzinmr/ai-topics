---
title: StateWise — Repairing Persistent Operational State Before Agent Actions
created: 2026-10-06
updated: 2026-10-06
type: concept
tags: [agent-memory, context-engineering, self-correction, ai-agents, agent-runtime, agent-safety]
sources: [raw/articles/arxiv-2610.05241-statewise-persistent-operational-state-repair.md]
confidence: medium
related: [concepts/overact-proactive-over-authorization, concepts/agent-trace-integrity, concepts/harness-engineering, concepts/pace-provenance-aware-capability-enforcement]
---

# StateWise — Repairing Persistent Operational State Before Agent Actions

Long-lived agents reuse stored operational records (memory, prior state, workspace facts) as
premises for later actions. When the environment or requirements change, those records go
stale — but existing action review, provenance tracking, and clarification mechanisms leave the
*underlying persistent state uncorrected*. StateWise diagnoses and repairs that state *before*
an action runs.

## Problem

An audit of coding-agent trajectories found failure chains where an invalid stored record was
reused as a premise, producing task failures and unsafe modifications. Reviewing the *action*
doesn't help when the *premise* is corrupted.

## Method

1. **Record-level counterfactual replanning** to identify decision-critical records (which
   stored facts actually drive the action).
2. Establish each record's **current validity**: reliability checks + read-only verification of
   machine-observable facts + targeted clarification of developer-owned intent.
3. **Typed evidence grounding** binds evidence to specific records/scopes, enabling persistent
   corrections with **repair lineage**.
4. Agent **replans from the repaired state**, then an independent state-action check gates execution.

## Results

On 150 executable coding-agent cases (diverse runtimes/workspaces/repos) under **corrupted
persistent state**: **93.3% overall correctness** vs. **38.7%** for the baseline agent, with
**no unsafe actions**. Ablations and transfer evals show recovery and corrections persist across
repositories and tool interfaces.

## Implication

This is a *premise-integrity* layer, distinct from execution-boundary enforcement. Where
[[concepts/pace-provenance-aware-capability-enforcement]] gates the tool call and
[[concepts/overact-proactive-over-authorization]] constrains authority, StateWise fixes the
corrupted *memory-as-premise* that makes an otherwise-correct action wrong — the
statefulness dimension of [[concepts/harness-engineering]] and record trust in
[[concepts/agent-trace-integrity]].

## Related

- [[concepts/overact-proactive-over-authorization]] — action-boundary vs premise-boundary
- [[concepts/agent-trace-integrity]] — trust in stored/generated records
- [[concepts/harness-engineering]] — the statefulness substrate StateWise repairs
- [[concepts/pace-provenance-aware-capability-enforcement]] — complementary enforcement point
- [[queries/2026-10-09-crash-consistent-agent-synthesis]] — places premise repair alongside Retire, durable execution, and UndoBench as one effect-integrity family
