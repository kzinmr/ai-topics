# Multi-Axis Structural Analysis for Concept Pages

## When to Use

Use this pattern when:
- Two or more related paradigms/frameworks share structural similarities that can be decomposed into orthogonal axes
- A new technology/feature completes an existing 2-axis comparison by introducing a third dimension
- An existing wiki page already has a 2-axis comparison (like RLM × PTC) and a new development warrants extension to 3+ axes
- The user asks for "構造的対比" (structural comparison) between related concepts

## Pattern: N-Axis Decomposition

### Step 1: Identify the Axes

Each axis represents a distinct *operation* the model performs. Axes should be:
- **Orthogonal** — they address fundamentally different problems (data, functions, agents)
- **Complementary** — together they form a complete framework
- **Named by operation** — Disaggregate, Aggregate, Delegate — not by technology

### Step 2: Define the Core Operations

| Axis property | Example: Data Axis | Example: Function Axis | Example: Agent Axis |
|---|---|---|---|
| **Paradigm** | RLM | PTC | PSAC (DW) |
| **Core operation** | Split 1 context → N pieces | Merge N tool calls → 1 code block | Spawn 1 script → N sub-agents |
| **Direction** | Disaggregate (read) | Aggregate (write) | Delegate (orchestrate) |
| **Concrete form** | `context[start:end]`, `llm_query(subset)` | `await tool_a()`, `asyncio.gather()` | `spawn_subagent(task)`, workflow script |

### Step 3: Build the Multi-Dimensional Comparison Table

Template columns:

| Dimension | Paradigm A | Paradigm B | Paradigm C |
|---|---|---|---|
| What is decomposed | ... | ... | ... |
| Who decides | ... | ... | ... |
| Topology | ... | ... | ... |
| Invocation | ... | ... | ... |
| State location | ... | ... | ... |
| Output coupling | ... | ... | ... |
| Context isolation | ... | ... | ... |
| Verification | ... | ... | ... |
| Scaling axis | ... | ... | ... |
| Failure mode | ... | ... | ... |

Dimensions should reveal *structural differences*, not just surface-level features. The table should make non-obvious contrasts visible — e.g., "task decomposition is explicit for DW but implicit/emergent for RLM."

### Step 4: Add the ASCII Diagram

A simple 3-axis diagram helps orient the reader:

```
              Paradigm B (operation)
              N inputs → 1 output
                   ↑
                   │  axis 2
                   │
Paradigm A ←────────┼──────────→ Paradigm C
(operation)         │           (operation)
1 input → N outputs │           1 input → N outputs
                   │
              axis 1          axis 3
```

### Step 5: Cross-Reference Both Ways

When adding the analysis to Page A, also add a summary table + cross-reference to Page C (and vice versa). The analysis lives primarily on one page (the one whose existing 2-axis framework is being extended) with a summary on the related page pointing back.

## Real Example: RLM × PTC × PSAC (2026-05-29)

See `concepts/rlm-recursive-language-models.md` for the canonical 3-axis framework extending the existing RLM×PTC 2-axis analysis to include Dynamic Workflows as the Agent Axis (PSAC).

### Key Pitfall: Paper Framing ≠ Actual Behavior

When decomposing paradigms into structural axes, **do not take paper authors' framings at face value.** Example: the RLM paper frames itself as purely "context-centric" ("the choice of decomposition should purely be the choice of an LM"), but in practice, the model's context decomposition decisions *are* task decomposition decisions. Writing `llm_query(subset_a)` vs `llm_query(subset_b)` is implicitly assigning different sub-tasks to different recursive calls.

Always examine **what the system actually does** (operational behavior), not just **what the authors say it does** (framing). The framing is a design philosophy; the operational behavior is the ground truth. The comparison table should reflect the latter.

This also applies to:
- Company blog posts framing features as novel when they implement existing academic concepts
- Papers claiming "we don't do X" when X emerges implicitly from their design
- Marketing language that obscures structural similarities with prior art

### Scaling Insight: Third-Axis Multiplicative Effects

When a new paradigm introduces a genuinely new axis, the relationship may be **multiplicative** rather than additive. Example: Nickadobos's observation that Dynamic Workflows enable `Base Model × Thinking Time × Generated Harness Compute`, where the third factor is a new scaling dimension. Look for cases where case study results (e.g., 750K LOC migration in 11 days) cannot be explained by scaling the first two axes alone — this signals a genuinely new multiplicative factor.
