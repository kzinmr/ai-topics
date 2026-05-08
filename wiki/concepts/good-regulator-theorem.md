---
title: "Good Regulator Theorem (Gooder Regulator)"
created: 2026-05-08
updated: 2026-05-08
type: concept
tags:
  - selection-theorem
  - agent-foundations
  - information-theory
  - world-models
  - alignment
aliases:
  - "Gooder Regulator Theorem"
  - "Good Regulator Theorem"
  - "Conant-Ashby Theorem"
sources:
  - https://www.lesswrong.com/posts/Dx9LoqsEh3gHNJMDk/fixing-the-good-regulator-theorem
  - https://www.lesswrong.com/posts/JQefBJDHG6Wgffw6T/a-straightforward-explanation-of-the-good-regulator-theorem
  - https://www.lesswrong.com/posts/xgJuyvi3jGsmNAmg9/do-model-evaluations-fall-prey-to-the-good-er-regulator
  - raw/articles/johnswentworth-fixing-good-regulator-theorem-2021.md
  - raw/articles/alfred-harwood-good-regulator-explanation-2024.md
  - raw/articles/testingthewaters-model-evals-good-regulator-2025.md
related:
  - concepts/causal-backbone-conjecture
  - concepts/world-models-science
  - concepts/karpathy-loop
---

# Good Regulator Theorem (Gooder Regulator)

**Original:** Conant & Ashby, 1970 | **"Gooder" Fix:** John Wentworth, 2021 | **Type:** Selection theorem for control systems

## Original Theorem (Conant & Ashby, 1970)

> "Every good regulator of a system must be a model of that system."

The original claim: under very broad conditions, any regulator that is maximally both **successful** (minimizes outcome entropy) and **simple** (no unnecessary noise) must be isomorphic with the system being regulated. Making a model is thus necessary.

**Setup**: System S → Regulator observes X → Regulator produces R → Outcome Z is determined by both S and R. Goal: choose regulator policy P(R|S) to minimize entropy of Z.

**Main mathematical result**: Under optimality + minimal noise, R becomes a deterministic function of S. That is, all R-values with nonzero probability for a given S must produce the same Z.

### Problems with the Original (Wentworth's Critique)

1. **Perfect information assumption**: The proof implicitly assumes the regulator has perfect information about system state S (`P[R|S]` not `P[R|X]`) — a bait-and-switch from the stated setup
2. **Equivalence ≠ internal modeling**: Being equivalent to a model-based regulator does NOT mean the regulator actually constructs a model internally. The regulator could just be a lookup table.
3. **Misleading framing**: The paper's title/summary claims "making a model is necessary" when the actual proof shows something much weaker

## The "Gooder Regulator" Theorem (Wentworth, 2021)

> **Key addition**: An **information bottleneck** forces the actual internal construction of a model.

Wentworth's improvement: when the regulator must act through a **constrained information channel** (limited internal state, communication bandwidth, or computational capacity), it MUST actually reconstruct a model of the system internally — not just be "equivalent to" one.

### Three sub-theorems in Wentworth's fix

| Component | What it fixes | Key insight |
|-----------|---------------|-------------|
| **Imperfect observation** | Original's perfect-info cheat | Regulator sees noisy X, not perfect S |
| **Deterministic-Z uniqueness** | Original's non-uniqueness of optimal policies | When Z is deterministic in (R,S), optimal policies converge |
| **Information bottleneck** | Original's equivalence-vs-actual-model gap | Limited internal state forces genuine model construction |

### Information Bottleneck → Model Building

The bottleneck argument is conceptually similar to **mesa-optimization** (Risks From Learned Optimization): when an optimization process is itself constrained by an information bottleneck, it must build an internal model of the optimization target. Here, the regulator's internal state is the bottleneck — to be optimal under that constraint, it must reconstruct S internally.

## Why This Matters for AI Agents

### For Agent Architecture
The Gooder Regulator Theorem provides a **formal justification for world models** in agent design:
- Agents operating under compute/attention constraints naturally develop internal representations of their environment
- This is NOT optional overhead — it's a mathematical consequence of optimality under constraints
- The richer the task set, the more detailed the required internal model

### For AI Safety / Model Evaluation
Applied to **evaluation** (testingthewaters, 2025):
- Evaluators are regulators: they produce "pass/fail" outcomes based on observing system behavior
- As systems become more complex, evaluators must build increasingly detailed internal models of the system
- An evaluator checking for "dishonesty" must partially model the agent's internal decision process
- This connects to **scalable oversight**: evaluation difficulty scales with system complexity

### For Harness Design
Agent harnesses (like Claude Code, OpenCode, Pi) are regulators of the LLM → task-completion system. The Gooder Regulator Theorem suggests:
- **Better harnesses literally model the LLM better** — they track the LLM's strengths, failure modes, and context limitations
- **Limited context windows act as information bottlenecks** → they force the agent to build concise internal task-models
- **The Harness Effect** (5-40pp performance difference across harnesses for same model) may be explained by differences in internal system-modeling quality

## Relationship to Selection Theorems

The Good(er) Regulator Theorem is a **selection theorem** — it identifies properties that any optimal controller MUST have, regardless of implementation. Selection theorems form a spectrum:

| Selection Theorem | What it selects for | Key constraint |
|-------------------|---------------------|----------------|
| **Good Regulator** (Conant-Ashby) | Equivalence to model-based regulator | Optimality + simplicity |
| **Gooder Regulator** (Wentworth) | Actual internal model construction | + Information bottleneck |
| **Causal Backbone** (tailcalled) | Sparse, resource-weighted modeling | + Finite resources in environment |

## Contrast with Causal Backbone Conjecture

The shift from Gooder Regulator to Causal Backbone is the shift from **task-driven** to **resource-driven** modeling:

| Dimension | Gooder Regulator | Causal Backbone |
|-----------|-----------------|-----------------|
| **What forces modeling?** | Task diversity + information bottleneck | Resource distribution shifts |
| **What gets modeled?** | The controlled system | High-leverage nodes in resource flow |
| **Failure mode** | Information overload (modeling too much) | Missing backbone shifts (modeling too little) |
| **Scope** | A single regulator-system pair | The entire competitive ecosystem |
| **Key mathematical tool** | Shannon entropy minimization | Log-normal resource distributions |

The Causal Backbone Conjecture argues that the Gooder Regulator's "sufficiently rich set of tasks" assumption is **disastrously wrong** — it leads to modeling everything and collapsing under information overload. Instead, the environment's resource constraints naturally filter what matters.

## Open Questions

1. **Formal bottleneck quantification**: How do we measure "information bottleneck tightness" in practical agent systems?
2. **Bottleneck vs task diversity trade-off**: Is there a formal relationship between bottleneck tightness and required task diversity?
3. **Empirical validation in LLM agents**: Can we measure whether better harnesses build better internal models of their LLM?
4. **Connection to scaling laws**: Does the Gooder Regulator Theorem predict anything about how internal model quality scales with compute?

## Sources

- [Fixing The Good Regulator Theorem](https://www.lesswrong.com/posts/Dx9LoqsEh3gHNJMDk/fixing-the-good-regulator-theorem) by johnswentworth, LessWrong (2021-02-09) — the "Gooder Regulator" post
- [A Straightforward Explanation of the Good Regulator Theorem](https://www.lesswrong.com/posts/JQefBJDHG6Wgffw6T) by Alfred Harwood, LessWrong (2024-11-18) — curated, entry-level explainer
- [Do model evaluations fall prey to the Good(er) Regulator Theorem?](https://www.lesswrong.com/posts/xgJuyvi3jGsmNAmg9) by testingthewaters, LessWrong (2025-08-19) — applies theorem to AI eval
- [Every Good Regulator of a System Must Be a Model of That System](http://pespmc1.vub.ac.be/books/Conant_Ashby.pdf) — Conant & Ashby, 1970 (original paper)
