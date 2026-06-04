# Cross-Concept Analogy Tables

When a user draws an analogy between two wiki concepts (especially during or after article ingestion), capture it as a structured comparison table. This turns a conversational insight into durable wiki content.

## When to Create

The user makes a connection like:
- "X is like Y in that both…" (structural analogy)
- "This reminds me of Z in information retrieval…" (cross-domain analogy)
- "X and Y both solve the same constraint through different means" (isomorphic pattern)

## Table Structure

Use a **7-dimension comparison** as the default template:

| 次元 | Concept A | Concept B |
|---|---|---|
| **分割対象** | what does A split? | what does B split? |
| **分割方向** | horizontal / depth / time | horizontal / depth / time |
| **パターン** | named pattern (MapReduce, Recursive, etc.) | named pattern |
| **制約突破** | what constraint does it overcome? | same question |
| **スケーリング** | quantitative claim if available | quantitative claim |
| **集約方法** | how results are combined | how results are combined |
| **本質** | one-line essence | one-line essence |

Add a closing quote that crystallizes the common insight beneath both.

## Real Examples from This Wiki

### Multi-Agent (MapReduce) × RLM (Recursive) — 2026-05-20

Both split to overcome single-context-window limits. Multi-Agent splits the task space horizontally; RLM splits the input space recursively. Same divide-and-conquer pattern, different axes.

### Agent-Context × Query-Document Duality — 2026-05-20

Agent task (objective) mirrors an IR query; subagent results (context) mirror retrieved documents. Interleaved thinking mirrors relevance feedback. Both are projections of the same information need at different granularities in the same token space.

## Where to Place

- **Primary**: On the page that was the subject of the original ingestion/conversation (the page being enriched)
- **Secondary**: Add a reciprocal cross-reference on the other concept's page in its "Related Concepts" or equivalent section

## Related Skills

- `wiki-entity-enrichment-from-article` — the parent ingestion workflow
- `cross-leader-synthesis` — synthesizing perspectives across multiple thought leaders
