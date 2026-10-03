---
title: "Source Learning (Source-Specific Agent Competence)"
created: 2026-10-03
updated: 2026-10-03
type: concept
tags: [concept, agentic-retrieval, agent-memory, retrieval, knowledge-graph, ai-agents]
aliases: [source learning, SourceLearn, source-specific competence, source model]
confidence: medium
sources: ["raw/articles/arxiv-2610.02150-sourcelearn-source-specific-competence.md"]
---

# Source Learning (Source-Specific Agent Competence)

**Source learning** (Fu et al., arXiv:2610.02150, Oct 2026) reframes how agents use persistent
external corpora. The paper's move: **from knowledge *access* to source *learning*** — treat
repeated use of the same authoritative source not as repeated access, but as an opportunity to
**progressively build reusable, source-specific competence.**

## The gap it attacks

Two dominant lineages stop short:

- **Retrieval/RAG** improves *how* source content is accessed and organized (see
  [[concepts/retrieval-augmented-generation]], [[concepts/agentic-rag]]).
- **Agent memory** preserves reusable knowledge from *prior interactions*.

But in both, hammering the same source over and over is still treated as *repeated access*. The
agent never accumulates a durable understanding of **that specific source** — how its knowledge is
structured, interpreted, and applied.

## Mechanism: a persistent source model

Competence is represented as a **persistent source model** capturing reusable understanding of the
source. It is built and refined by two complementary signals:

- **Self-Directed Source Learning** — identifies what remains *incompletely understood* and
  adaptively *revisits the source* to fill the gap.
- **Task-Guided Source Learning** — uses *downstream task experience* to reveal local
  representational gaps and recurring needs for how source knowledge should be organized.

Key discipline: **learning signals decide *what* to reconsider, but the persistent updates are
reconstructed from the authoritative source itself** — so the source model is grounded, not
hallucinated from memory. This "signals select, source reconstructs" split is the paper's answer to
the drift problem that plagues experience-based memory.

## Results

Across **5 benchmarks × 3 LLM backends**, SourceLearn is best in **13/15 settings**, with gains up
to **+22.6 points over Hybrid RAG**, and substantial wins over static source representations and
experience-based memory baselines.

## Why it matters

- Sits at the intersection of retrieval and agent memory: it is neither pure RAG (it accumulates a
  model of the source) nor pure experiential memory (it re-grounds updates in the source).
- Directly relevant to enterprise agents that live on top of one durable corpus (codebase, wiki,
  legal corpus) — the case where source-specific competence compounds.
- The reconstruction-from-source rule is a concrete anti-hallucination pattern for self-improving
  memory, complementary to [[concepts/memory-integrity]].

## Open questions

- Single source, `confidence: medium`; benchmarks unnamed in the abstract — need to confirm which
  corpora and whether "source model" is text, graph, or embeddings.
- Scaling a persistent per-source model (storage, staleness when the source changes) is unaddressed
  in the abstract.
- Boundary vs. **fine-tuning on the corpus**: what does a "source model" keep that weight updates
  or cached context do not?

## Related

- [[concepts/agentic-rag]] — the "improve access" lineage this contrasts with
- [[concepts/ai-agent-memory-two-camps]] — experience-based memory as the other baseline
- [[concepts/memory-integrity]] — re-grounding updates in the authoritative source
- [[concepts/contextual-retrieval]] — organizing source knowledge for retrieval
