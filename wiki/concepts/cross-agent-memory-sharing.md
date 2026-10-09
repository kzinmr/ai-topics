---
title: "Cross-Agent Memory Sharing"
created: 2026-10-09
updated: 2026-10-09
type: concept
tags: [agent-memory, memory-systems, multi-agent, knowledge-graph, tool-use]
sources:
  - raw/papers/2026-09-11_2609.09192_memcollab-cross-memory-collaboration-via.md
related: [memory-integrity, knowledge-graph-memory-agents, vector-db-agent-memory, ai-memory-systems, ai-control]
confidence: medium
aliases: ["cross-memory collaboration", "MemCollab", "test-time memory evolution", "CrossMemKG", "shared agent memory"]
---

# Cross-Agent Memory Sharing

**Cross-agent memory sharing** is the practice of letting multiple LLM agents read,
negotiate over, and refine a *common pool of memories* rather than each agent keeping an
isolated, private experience store. It promises faster knowledge transfer (one agent's
hard-won lesson becomes available to all) but creates a shared, mutable attack surface and a
new "whose memory wins" conflict problem.

## The Isolation Problem

Memory has become a standard module for LLM agents — they learn from past episodes instead of
re-solving each task. But in most deployments memory is **confined to a single agent**, which
causes two failures:

1. **Inefficient knowledge transfer** — a fleet of agents each rediscovers the same lessons.
2. **Homogenized experience** — identical base models + independent memory drift toward
   correlated blind spots, because no agent ever sees a genuinely different experience.

## MemCollab: Cross-Memory Collaboration (Wu et al., 2026)

arXiv:2609.09192 (MemCollab) is the first framework for **test-time** cross-memory
collaboration — sharing happens at inference, not training.

- **Memories as living artifacts.** When an agent meets a new task it retrieves relevant
  memories *from peers* and **evolves** them through collaborative reasoning, rather than
  replaying them frozen.
- **CrossMemKG (Cross-Memory Knowledge Graph).** A graph that links episodes, entities, and
  strategies across agents so relevant experiences from other agents can be located and merged.
- **Test-Time Memory Evolution (TTME).** A mechanism that reconciles **conflicts between
  heterogeneous agent memories** — two agents may hold contradictory "lessons" from different
  contexts; TTME negotiates which generalizes to the current task.

## Why This Matters for the Wiki

Cross-agent memory is the *optimistic* half of a story whose *pessimistic* half is
[[memory-integrity]] and the persistent-memory attack surface. The moment you let agents
share memory you gain compounding but also let a single poisoned or wrong memory propagate
across an entire fleet — the shared-memory equivalent of a supply-chain attack. The
conflict-resolution machinery (TTME) is also, unknowingly, a first version of a
**consensus-over-memory** problem that security has to co-design with.

## Open Questions

- How do you authenticate the *provenance* of a shared memory so a compromised agent can't
  poison the pool? (Directly the [[memory-integrity]] question.)
- Does cross-memory homogenize agents *more* (echo chamber) or *less* (diverse experiences
  merged)?
- Can CrossMemKG support access control — some agents see a memory, others shouldn't?

## Related

- [[memory-integrity]] — the poisoning risk that sharing amplifies
- [[knowledge-graph-memory-agents]] — graph-structured memory (CrossMemKG's nearest neighbor)
- [[vector-db-agent-memory]] — retrieval substrate most shared-memory pools sit on
- [[ai-memory-systems]] — the cost side of accumulating shared experience
- [[ai-control]] — attack/defense framing for shared state
