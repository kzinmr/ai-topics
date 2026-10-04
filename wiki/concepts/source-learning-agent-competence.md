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

## The third axis (source- vs episode- vs time-scoped)

Mem++ (arXiv:2610.02002, see [[concepts/mempp-non-destructive-memory]]) attacks the *same*
write-time-compression default from the opposite side. Both papers refuse to let the memory layer
decide the answer in advance, and both re-ground retrieval in the **authoritative document**. They
differ on what is *learned*:

| Axis | Source Learning (SourceLearn) | Mem++ |
|------|------------------------------|-------|
| Unit | one durable **source** | a **time-scoped** slice of many documents |
| Persistent artifact | a source model of how knowledge is structured | every document **whole**, nothing distilled |
| When intelligence moves | *pre*-query — reuse accumulates competence | *post*-query — answering model selects the version |
| Trigger | repeated use of the same source | a question that specifies *when* |
| Failure avoided | repeated access ≠ understanding the source | write-time distillation destroys the version/time dimension |

Mem++ relocates the hard reasoning to **read** time; SourceLearn builds durable competence *before*
any question. A third lineage — the [[concepts/ai-agent-memory-two-camps]] "Camp 1" fact-graph camp —
sits at neither: it compresses at write time and thus pre-commits what can be answered, which is
exactly what both 2610 papers reject. Read together, the three stances are a coordinate system, not
a ranking: **what is persistent (source model vs raw record), when selection happens (pre- vs
post-query), and what scope it is keyed to (source vs time).**

## Related

- [[concepts/mempp-non-destructive-memory]] — same anti-write-distillation stance, read-time selection instead of a persistent source model
- [[concepts/agentic-rag]] — the "improve access" lineage this contrasts with
- [[concepts/ai-agent-memory-two-camps]] — experience-based memory as the other baseline
- [[concepts/memory-integrity]] — re-grounding updates in the authoritative source
- [[concepts/contextual-retrieval]] — organizing source knowledge for retrieval
