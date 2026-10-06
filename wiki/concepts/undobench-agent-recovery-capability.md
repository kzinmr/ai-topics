---
title: UndoBench — Task Competence vs. Recovery Capability in Tool-Using Agents
created: 2026-10-06
updated: 2026-10-06
type: concept
tags: [agent-evaluation, benchmark, durable-execution, agent-tooling, ai-agents, tool-use]
sources: [raw/articles/arxiv-2610.05622-undobench-recovery-capability-tool-agents.md]
confidence: medium
related: [concepts/durable-execution, concepts/retire-versioned-execution, concepts/overact-proactive-over-authorization, concepts/agent-loop-orchestration]
---

# UndoBench — Task Competence vs. Recovery Capability in Tool-Using Agents

Most agent benchmarks score *nominal task completion*, which conflates baseline planning
skill with the ability to recover when an operation fails halfway. UndoBench separates the
two: it measures whether an agent can safely recover from faults without duplicating
external side effects — the property that actually matters once agents act on enterprise
systems.

## Setup

- 36 base workflows + 36 fault scenarios across 8 enterprise domains.
- Counterfactual **paired trials** under identical seeds, plus **wire-level effect-history**
  and **environment-state oracles** (ground truth on what effects actually fired).
- Evaluated on 12 held-out workflows: 2 open-weight models × 2 frameworks × 3 recovery
  paradigms = 5,760 executions / 2,880 paired trials.

## Headline result: the competence–recovery gap

In a frozen "lost-acknowledgment" study:
- Nominal competence: **83.54%**
- Conditional Recovery Success Rate (CRSR): **46.72%**
- Naive retry produced **duplicate external effects in 53.33%** of trials.

Commercial API models reproduced the same separation, so it is not a weak-model artifact.

## Recovery is phase-dependent

The right recovery strategy depends on *where* in the transaction the fault lands:
- **Before mutation**: methods perform similarly; capable trials avoid duplicate effects.
- **During partial mutation**: naive retry, per-call idempotency, and zero-privilege
  journaling all collapse on the composite workflows.
- **After commit but before acknowledgment**: verification and server-side idempotency
  substantially improve safety.

## Implication

Scoring completion alone masks critical, phase-dependent recovery vulnerabilities. This is
the eval-side complement to the execution-substrate work in [[concepts/durable-execution]]
and versioned/interruptible execution in [[concepts/retire-versioned-execution]] — durable
execution is the mechanism; UndoBench is the instrument that proves agents don't have it.

## Related

- [[concepts/durable-execution]] — checkpoint-resume as the recovery substrate
- [[concepts/retire-versioned-execution]] — authority/resource split for interruption
- [[concepts/overact-proactive-over-authorization]] — irreversible-action failure family
- [[concepts/agent-loop-orchestration]] — the loop in which faults occur
