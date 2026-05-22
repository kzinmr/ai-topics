---
title: Attractor Models
created: 2026-05-22
updated: 2026-05-22
type: concept
tags: [concept, transformer-architecture, training, optimization, reasoning, llm, benchmark]
sources: [raw/articles/2026-05-12_attractor-models-language-reasoning.md, https://arxiv.org/html/2605.12466]
---

# Attractor Models

A two-stage neural architecture where a backbone Transformer proposes output embeddings and an **attractor module** refines them to a **fixed-point equilibrium** via implicit differentiation. Published by USC researchers (Fein-Ashley & Rashidinejad), May 12, 2026.

## Architecture

1. **Backbone** (large Transformer `T_θb`): Produces meaningful initial output embedding `ỹ₀` in the output space
2. **Attractor** (smaller weight-tied block `T_θa`): Refines via `ỹ_{t+1} = T_θa(ỹ_t, ỹ₀)` with persistent injection of the backbone proposal
3. **Fixed-Point Solver**: Anderson acceleration with adaptive convergence-based step count (not prescribed)

## Key Innovation: Equilibrium Internalization

A novel phenomenon discovered during training: the backbone learns to place its initial guess `ỹ₀` near the fixed point `ỹ*`, reducing needed refinement steps. **The solver can often be removed at inference** with minimal degradation — recurrence acts as a moving teacher that the model internalizes.

## Key Results

| Metric | Value |
|---|---|
| Perplexity reduction | Up to 46.6% (Lambada) |
| CORE accuracy gain | Up to 19.7% |
| 770M Attractor vs 1.3B Transformer | Outperforms with 2× fewer tokens |
| Training FLOPs reduction | 25-31% |
| Training memory | O(1) in recurrence depth |
| Sudoku-Extreme (27M params) | 91.4% |
| Maze-Hard (27M params) | 93.1% |

## vs. Looped/Recurrent Architectures

Traditional looped models suffer from:
- Linearly growing memory (backprop-through-time)
- Fixed recurrence depth causing train-test mismatch
- Training instability

Attractor Models solve these by:
- Implicit differentiation with **one-step approximation** (u≈v) → constant memory
- Adaptive step count via convergence → no train-test mismatch
- Stable training via fixed-point formulation

## Training

- Standard next-token prediction cross-entropy on fixed-point output `ỹ*`
- Gradients via implicit differentiation (not backprop-through-time)
- One-step approximation avoids differentiating through every solver iteration
- Tied embedding/unembedding throughout

## Reasoning at Tiny Scale

A 27M-parameter Attractor Model achieves 91.4% on Sudoku-Extreme and 93.1% on Maze-Hard — tasks where frontier models ([[entities/claude|Claude]], [[entities/gpt-o3|o3]], [[entities/deepseek-r1|DeepSeek-R1]]) fail completely, and specialized recursive reasoners collapse at larger scales.

## Related

- [[concepts/transformer-architecture|Transformer Architecture]]
- [[concepts/reasoning|Reasoning]]
- [[concepts/training|LLM Training]]
- [[concepts/chain-of-thought|Chain of Thought]]
- [[concepts/mechanistic-interpretability|Mechanistic Interpretability]]
- [[concepts/test-time-scaling|Test-Time Scaling]]
