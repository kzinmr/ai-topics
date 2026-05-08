---
title: "Fixing The Good Regulator Theorem"
author: johnswentworth
source_url: https://www.lesswrong.com/posts/Dx9LoqsEh3gHNJMDk/fixing-the-good-regulator-theorem
date: 2021-02-09
platform: LessWrong
points: 158
comments: 39
tags: [Good Regulator Theorems, Selection Theorems, World Modeling]
ingested: 2026-05-08
---

# Fixing The Good Regulator Theorem
**Author:** johnswentworth | **Date:** 2021-02-09 | **Platform:** LessWrong | **Points:** 158

## Key Claims

### The Original Theorem (Conant & Ashby, 1970)
Conant & Ashby claimed: "every good regulator of a system must be a model of that system." Their proof showed that an optimal, noise-free regulator is *equivalent to* one that reconstructs system state then acts on it — but this does NOT mean the regulator *actually* builds an internal model.

### The "Gooder" Fix (johnswentworth)
Wentworth identifies three problems with the original theorem:
1. **Perfect information assumption**: The original proof implicitly assumes the regulator has perfect information about system state S
2. **Equivalence ≠ internal modeling**: Being equivalent to a model-based regulator doesn't mean the regulator IS one internally
3. **No uniqueness**: Multiple optimal policies may exist, only some of which use models

The fix: **an information bottleneck forces the use of a model**. When the regulator must act through a constrained channel (limited internal state), it MUST reconstruct system state internally — similar to how an information bottleneck forces mesa-optimizer emergence in Risks From Learned Optimization.

### Causal Setup
System S → Regulator input X (noisy observation of S). Regulator produces R → Outcome Z determined by (R, S). Goal: minimize entropy of Z.

### Key Result
Under an information bottleneck constraint, any optimal minimal regulator MUST actually construct a model of the controlled system internally — not just be "equivalent to" one.
