---
title: "Context Policy Evolution (ContextEvo)"
created: 2026-09-30
updated: 2026-09-30
type: concept
tags: [context-engineering, context-management, agent-harness, self-improving, ai-agents, long-horizon, arxiv]
confidence: medium
sources:
  - raw/articles/arxiv-2609.34649-beyond-skill-evolution-self-evolving-context-management.md
related:
  - "[[concepts/context-engineering/index]]"
  - "[[concepts/harness-learning]]"
  - "[[concepts/self-evolving-agents]]"
  - "[[concepts/context-engineering/context-compaction]]"
---

# Context Policy Evolution (ContextEvo)

**Context policy evolution** extends harness self-improvement from *what the agent knows* (skills, experience records) to *how the agent decides what to keep visible*. On long-horizon tasks, the bottleneck stops being the skill library and becomes context management itself: as interactions accumulate, useful evidence gets buried under redundant or outdated context.

> Introduced in "Beyond Skill Evolution: Self-Evolving Context Management Policies for Long-Horizon Agent Harnesses" (arXiv:2609.34649, Sept 2026) — Li, Xu, Chen, Wang, Liang. System name: **ContextEvo**.

## The Argument Against Skill-Only Evolution

Experience- and skill-based harness evolution learns from execution trajectories, but underperforms on long-horizon tasks. The reason: a skill library is an *append* structure, while long-horizon failure is a *pressure* problem — the model-visible context saturates with stale evidence before any missing skill is reached.

## Mechanism

1. **Reconstruct the model-visible context at key decision points** — replay what the model actually saw, not what the transcript claims.
2. **Identify context-related failures** — attribute failures specifically to context handling rather than to reasoning or tool capability.
3. **Apply targeted policy updates** — modify the context-management *policy* (what to keep, compress, drop, re-surface) rather than adding skills.

## Results

- Built on the open-source **Pi-agent** harness; improves performance across **three long-horizon task benchmarks**, reaching results comparable to or better than several prominent harnesses — the paper names **Codex**, **OpenCode**, and **OpenClaw**.
- Analysis shows **fixed or locally-evolved context strategies fall short under long-horizon information pressure**, whereas the evolved policy adapts to each environment's information demands.

## Why It Matters

This is a third axis in the deployment-time-compute family alongside [[concepts/harness-learning]] (learn the harness program) and [[concepts/search-scaling]] (learn the search budget): *learn the retention rule*. It also reframes [[concepts/context-engineering/context-compaction|compaction]] from a hand-tuned heuristic into a *learnable policy object*, connecting to KV-level work like [[concepts/kv-cache-compression]] where the compression *choice* is likewise treated as adaptive rather than fixed.

## Open Questions

- Does an evolved context policy transfer across domains, or must it be re-evolved per environment (the paper's own results suggest per-environment adaptation is the source of the win)?
- How does context-policy failure attribution avoid the confound where "context was too long" is a proxy for "the task was hard"?
- What is the safety profile? An evolved retention policy can systematically drop the very evidence a monitor would need — see [[concepts/endogenous-misalignment-self-evolving-agents]].

## Related

- [[concepts/context-engineering/index]] — the discipline this automates
- [[concepts/harness-learning]] — sibling: learning the harness program itself
- [[concepts/self-evolving-agents]] — the broader pattern
- [[concepts/search-scaling]] — sibling: scaling the search/retrieval budget
- [[concepts/embedding-long-context-degradation]] — the degradation regime fixed policies cannot handle
