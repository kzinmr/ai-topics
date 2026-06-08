---
title: "AlphaProof Nexus"
created: 2026-05-31
updated: 2026-05-31
type: concept
tags:
  - google
  - formal-verification
  - education
  - architecture
  - neurosymbolic
sources:
  - https://wpnews.pro/news/how-deepmind-alphaproof-nexus-cracks-56-year-old-math-agentic-llm-loops-and-lean
---

# AlphaProof Nexus

**AlphaProof Nexus** is a framework by [[entities/deepmind|Google DeepMind]] for building agents that interleave LLM calls with Lean compiler calls for formal mathematical proof generation. Paper: arXiv:2605.22763 (Tsoukalas et al., May 21, 2026).

## Architecture

- **Pool of parallel subagents**, each independently searching for a proof
- LLM generates proof steps → Lean compiler provides deterministic feedback → iterate
- Agent D combines Ralph loop, sub-tool integration, and evolutionary population database
- **EVOLVE-VALUE** mechanism: simultaneous search over proofs AND algorithm parameters

## Results

| Achievement | Details |
|---|---|
| **Erdős Problems** | 9 open problems resolved autonomously (out of 353 formalized in Lean) |
| **OEIS Conjectures** | 44 proofs passed human expert review (out of 492 autoformalized) |
| **Algebraic Geometry** | 15-year open question settled |
| **Convex Optimization** | Novel algorithm discovered with better O(1/t) convergence rate |

## Key Insights

1. **Neuro-symbolic paradigm**: Neural networks for creativity + symbolic systems for rigorous verification
2. **Compiler feedback as force multiplier**: Replacing "does this look right?" with "the Lean compiler tells you exactly what went wrong"
3. **Shift from specialized to simple loops**: "Ongoing shift from specialized trained systems toward simple agentic loops as LLMs become more capable"
4. **LLM + deterministic verifier beats specialized systems**: The simple loop is more capable than expected

## Cost

- Inference cost: "a few hundred dollars" per overnight autonomous proof run
- 56-year-old Erdős problem resolved with minimal compute vs. decades of human effort

## Related Pages
- [[entities/deepmind]] — Google DeepMind, developer
- [[concepts/neurosymbolic]] — Neuro-symbolic AI paradigm
- [[concepts/recursive-self-improvement]] — RSI and proof search
- [[concepts/agent-architecture]] — Agentic system design
