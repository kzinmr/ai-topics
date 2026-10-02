---
title: "Just-In-Time Agent Memory"
created: 2026-09-30
updated: 2026-09-30
type: concept
tags: [agent-memory, memory-systems, ai-agents, agentic-retrieval, reinforcement-learning, arxiv]
confidence: medium
sources:
  - raw/articles/arxiv-2609.34385-just-in-time-agent-memory-with-runtime-agentic-research.md
related:
  - "[[concepts/ai-agent-memory]]"
  - "[[concepts/lifelong-agent-memory]]"
  - "[[concepts/ai-agent-memory-middleware]]"
---

# Just-In-Time Agent Memory

**Just-In-Time (JIT) agent memory** inverts the dominant memory design. Most agent-memory systems are **Ahead-of-Time (AOT)**: memory is constructed *before* a specific request arrives. AOT reduces online serving cost, but request-agnostic construction silently discards fine-grained information that only becomes important once the (unknown-future) query lands. JAM instead constructs the relevant context *at runtime, conditioned on the query*.

> "Just-In-Time Agent Memory with Runtime Agentic Research" (arXiv:2609.34385, cs.CL, Sept 2026) — Yan, Li, Qian, Lu, Li. Framework: **JAM**; training environment: **Memory-Gym**; code released at VectorSpaceLab/general-agentic-memory.

## Two-Role Architecture

| Role | Responsibility |
|------|----------------|
| **Memorizer** | Preserves *complete raw histories* in a hierarchical page-store, with compact navigational summaries — the summaries are for navigation, never a lossy substitute for the raw record |
| **Researcher** | For each request, *iteratively retrieves, inspects, and integrates* evidence — effectively an agent doing research over the agent's own history |

The load-bearing decision: keep the raw store lossless and pay compute at read time, rather than pre-crushing history into a fixed schema. This is the compiler analogy made explicit — AOT vs JIT — and the JIT side trades latency for fidelity.

## Training the Behavior

Memory *use* is trained, not prompted:

- **Memory-Gym** — an evidence-grounded data-synthesis pipeline covering **nine task types across six domains**.
- **Two-stage optimization of the Researcher**: supervised fine-tuning on **verified trajectories**, then **Hint-guided Group Relative Policy Optimization** (GRPO variant).

## Reported Position

JAM claims stronger task performance than AOT-style memory systems across agent-memory and long-context processing benchmarks, while remaining **substantially more efficient than prior trained agentic-memory approaches** — the efficiency claim matters because "just run a research agent over the history" is otherwise prohibitively expensive.

*Single paper, self-reported benchmarks; treat numbers as `confidence: medium` until replicated.*

## Why It Matters

This wiki's memory literature has largely argued over *storage substrates* (vector DB vs filesystem vs knowledge graph — see [[concepts/ai-agent-memory-two-camps]], [[concepts/filesystem-memory]]). JAM shifts the axis to *when* the memory is compiled, which is orthogonal to all of them: a JIT system could sit on top of any substrate. It also converges agent memory and [[concepts/deep-research]] — the mechanism for answering "what did we decide last month?" becomes the same as for "research this topic," differing only in corpus.

## Open Questions

- Does the runtime-research cost stay bounded for genuinely long histories (months of sessions), or does the Researcher's own context become the bottleneck?
- Verified-trajectory SFT presumes ground-truth evidence paths; how well does the recipe survive domains where "verified" is unavailable?
- Security: an always-searchable raw store is a large attack surface — see [[concepts/memory-integrity]].

## Related

- [[concepts/ai-agent-memory]] — the umbrella the AOT/JIT split extends
- [[concepts/ai-agent-memory-two-camps]] — storage-substrate debate, orthogonal axis
- [[concepts/lifelong-agent-memory]] — reuse without forgetting, complementary goal
- [[concepts/context-policy-evolution]] — JIT at the context level vs. at the memory level
- [[concepts/memory-integrity]] — risk surface of keeping complete raw histories
