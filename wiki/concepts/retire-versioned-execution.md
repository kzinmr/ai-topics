---
title: "Retire — Versioned Execution for Interruptible Agents"
created: 2026-10-04
updated: 2026-10-04
type: concept
tags:
  - llm-inference
  - kv-cache
  - agent-runtime
  - durable-execution
  - infrastructure
  - token-economics
aliases:
  - Retire
  - versioned execution
  - revision-to-successor
sources:
  - raw/articles/arxiv-2610.01160-retire-versioned-execution-interruptible-agents.md
confidence: medium
related:
  - concepts/vllm
  - concepts/kv-cache
  - concepts/durable-execution
  - concepts/agent-runtime
---

# Retire — Versioned Execution for Interruptible Agents

**Retire** (Zhang et al., arXiv:2610.01160, Oct 1 2026) is a serving **control-plane redesign** that turns the way agents revise running work — "abort the old request, submit a replacement" — into a *coordinated version transition* that stops obsolete output fast while preserving useful computed state for its successor.

## The problem: revision as abort-and-restart wastes work and leaks effects

Agents constantly revise: the user changes instructions, a tool fails, new information changes the plan. Today's servers express a revision as **abort + submit replacement**. That creates two obligations handled separately today:
- the old execution's **buffered output and outstanding work** must stop affecting the application;
- the **completed KV state** may still be useful to its replacement.

Handled separately, you get two failure modes: **obsolete effects stay publishable** (stale output leaks to the app) and the successor is forced to **rebuild valid state** from scratch.

## The mechanism: separate *resources* from *authority*

Retire's key abstraction: **requests own scheduling and memory resources; execution *versions* own authority** — the permission to publish output or install state for the current execution. A revision is then one version transition that:
1. **revokes** obsolete work (authority withdrawn → it can no longer publish/install),
2. **bounds** its remaining execution,
3. **certifies the completed prefix** its successor can inherit.

The successor runs from the inherited state while isolated old resources are reclaimed **asynchronously**. This unifies *fast invalidation* and *selective preservation* into one atomic transition — the same correctness concern (which effects are still "live") that drives [[concepts/agent-trace-integrity]], but pushed down into the inference server.

## Results

Implemented in **vLLM** ([[concepts/vllm]]) across five paths: output publication, GPU execution, **KV handoff** ([[concepts/kv-cache]]), tiered recovery, and distributed/multi-tenant serving.
- Correctness experiments verify current-version output and valid state inheritance across all paths.
- Combining invalidation + inheritance cuts **revision-to-successor time-to-first-token by a median 17.1%** (controlled paired experiments).
- A replay of **recorded coding-agent interruption arrivals** emits **no obsolete output** and keeps every final version progressing through repeated revisions.

## Why it matters

Interactive and coding agents spend a large share of their latency budget on *revisions* (pivots, corrections, retries), not first attempts. Retire reframes that from a cache-invalidation nuisance into a first-class control-plane object ("execution version = authority"). The authority/resource split is conceptually the serving-layer twin of [[concepts/durable-execution]] (deterministic replay of effects) and of the capability "authority" idea in [[concepts/pace-provenance-aware-capability-enforcement]] — both are about *which running work is allowed to have an effect*.

## Open questions
- Median 17.1% TTFT is on paired experiments; real-world gains depend on how *often* revisions inherit a valid prefix vs. needing rebuild.
- Certification of the "valid prefix" is doing the safety work — what is its cost on very long contexts (interaction with [[concepts/attention-bottleneck]])?
- Multi-tenant isolation of reclaimed resources is claimed but the security proof surface (obsolete-but-still-scheduled kernels) deserves scrutiny.

## Related
- [[concepts/vllm]] / [[concepts/kv-cache]] — the substrate Retire modifies
- [[concepts/durable-execution]] — effect-authority at the application layer
- [[concepts/agent-trace-integrity]] — "which effects are legitimate/live," same question, different layer
- [[concepts/pace-provenance-aware-capability-enforcement]] — authority-to-act, enforced at the tool boundary instead
