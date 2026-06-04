# Structural Duality Analysis Pattern

A reusable three-layer analytical framework for technical essays about AI architecture. Emerged from the 2026-05-20 session analyzing Anthropic's multi-agent system, RLM, and information retrieval.

## When to Use

When the essay involves two or more seemingly unrelated technologies that, on deeper inspection, share structural commonality. Especially effective for AI architecture topics where constraints (context windows, token budgets, capacity limits) drive convergent solutions.

## The Three-Layer Unfolding

### Layer 1: Divide-and-Conquer Commonality

Start by identifying the shared constraint (e.g., limited context window) and show how two different systems solve it via different splitting axes. Establish that they're variants of the same fundamental pattern, not just superficially similar.

### Layer 2: Query-Document Duality

Go deeper. Show that within one of the systems, there's a hidden structural correspondence to a well-known dual relationship from another field (e.g., information retrieval's query-document duality). Map concrete operations to dual counterparts, show the feedback loop is identical.

### Layer 3: Identify the Naive Model's Limit

The most powerful move: find where the duality model breaks down. State the naive assumption explicitly, show that in open-ended scenarios there's always a residual, reformulate with a condition: `compress(context | goal)` not `compress(context)`. Connect to known concepts from other fields (residual learning, advantage functions, active learning). Surface the open design questions.

## Narrative Arc Integration

- **出発点**: Ground in concrete phenomenon — the specific article, the surprising numbers
- **中間展開**: Layer 1 → Layer 2 → Layer 3 (progressive deepening)
- **着地点**: Identify the **next frontier** — the open design problem the analysis reveals. Forward-looking, not retrospective.

## Voice Guidelines

- Reader discovers the pattern with you, not lectured
- Each layer reads as "but if you look more carefully..." — progressive deepening
- Third layer (finding the limit) is most important — distinguishes from mere "X is like Y"
- End by naming the open problem, not declaring victory

## Example: 2026-05-20 Session

Anthropic Multi-Agent Research × RLM × IR duality:
- Layer 1: Both use divide-and-conquer to break context window limits (horizontal vs depth)
- Layer 2: Subagent objective↔query, subagent results↔document, interleaved thinking↔relevance feedback
- Layer 3: Naive model assumes context = complete satisfaction. Real systems need `compress(context | goal)` — shifted conditional compression. Opens three design questions: satisfaction measurement, residual query-ification, displacement granularity
