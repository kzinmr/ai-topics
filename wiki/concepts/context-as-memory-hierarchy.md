---
title: Context as Memory Hierarchy (L1/L2/L3)
created: 2026-06-12
updated: 2026-06-12
type: concept
tags: [context-engineering, context-management, agent-architecture, agent-harness, ai-agents, vertical-agent, prompt-caching, token-economics, design-patterns]
sources:
  - raw/articles/2026-06-11_peterwang_building-good-vertical-agent.md
---

# Context as Memory Hierarchy

A framework for organizing AI agent context inspired by CPU memory hierarchy (L1/L2/L3 cache). Proposed by [[entities/peter-wang|Peter Wang]] of [[entities/shortcut|Shortcut]] based on a year of building a production vertical agent for hedge funds.

## Core Thesis

With the model fixed, agent accuracy is a function of context quality. Bloated context buries signal; missing context forces guessing. The objective: **minimize context spent per task, averaged over the task distribution**. This is the same problem CPUs solve — long-tailed access patterns, tiny fast storage next to the processor, bigger slower tiers below.

> "A good agent is a faithful compression of its task distribution."

## The Three Tiers

| Tier | Analogy | Agent Design | Frequency | Token Cost |
|------|---------|-------------|-----------|------------|
| **L1** | CPU L1 cache (tiny, instant) | System prompt — core operations, contract, safety guidelines | ~80% of tasks | Paid every call |
| **L2** | L2/L3 cache (bigger, slower) | On-demand curated English specs + deferred tool schemas | ~15% of tasks | One discovery call |
| **L3** | Main memory/disk | Raw complete API reference + grep skill | Long tail | 3-6 tool calls |

### L1 — Always Resident

The bread-and-butter operations on the steep part of the frequency curve. Key principle: **spend disproportionate effort here** because the agent pays this cost on every task. Design for:
- Token efficiency (formula aliasing, style compression)
- Consequence reporting (write diffs with built-in linting)
- Free context injection (row/column labels attached automatically)

### L2 — On Demand

Important-but-occasional capabilities written as curated prose specs (not raw API dumps). Must include the canonical recipe and gotchas learned by failing. Two applications:
- **Documentation**: `console.log(getPivotTableInfo())` fetches a ~few hundred line spec
- **Deferred tools**: Tool schemas not in prompt; loaded via meta-tool wall as session-scoped cache

### L3 — Escape Hatch

The complete raw substrate (e.g., 70k-line API reference) on disk, made navigable by a ~100-line skill that teaches grep recipes. The system prompt makes the path explicit: "If the wrapped API can't do it, use the raw API — don't compromise."

## Key Insight: The Hierarchy Moves But Never Disappears

As models improve, yesterday's L3 becomes tomorrow's L2, yesterday's L2 collapses into L1. But the hierarchy itself persists — context will always be scarce relative to everything you could put in it.

> Bigger context windows tempt people to paste in more. The better instinct is the one CPUs settled on decades ago: summaries in cache, details on demand, the raw substrate as the last resort.

## Design Questions for Any Domain

1. **What goes in L1?** The 80% case. Make it brutally token-efficient and consequence-reporting.
2. **What goes to L2?** Important-but-occasional. Curated, gotcha-aware specs.
3. **What is your L3?** Raw complete substrate + a skill to mine it. Must be reachable and findable in bounded steps.

## Prompt Budget Pattern

- L1: ~few hundred lines (the bulk)
- L2: ~50 lines (allowlist + pointers)
- L3: ~5 lines (skill name + references)

## Related Concepts

- [[concepts/context-engineering|Context Engineering]] — broader discipline of designing agent context
- [[concepts/context-compression|Context Compression]] — techniques for reducing token usage
- [[concepts/progressive-disclosure|Progressive Disclosure]] — UX pattern of revealing complexity on demand
- [[concepts/prompt-caching|Prompt Caching]] — infrastructure-level caching of prompt prefixes
- [[concepts/agent-architecture|Agent Architecture]] — structural patterns for AI agents

## Contrast With Other Approaches

| Approach | Philosophy | Trade-off |
|----------|-----------|-----------|
| **L1/L2/L3 hierarchy** | Place each capability at the tier that minimizes total cost across the distribution | Requires domain knowledge + upfront effort |
| **Everything in prompt** | Maximize capability availability | Token bloat, signal buried in noise |
| **Everything deferred** | Minimize prompt cost | Too many discovery steps, slow common case |
| **RAG-only** | Retrieve relevant context dynamically | Retrieval quality bottleneck, unpredictable |

## Sources

- [[raw/articles/2026-06-11_peterwang_building-good-vertical-agent|Building a Good Vertical Agent]] by Peter Wang (X Article, Jun 2026, 972 bookmarks)
