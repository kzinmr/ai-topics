2026-05-22 | arXiv:2605.12466 | Attractor Models: Solving the Loop for Language and Reasoning
=========================================================================================
Source: https://arxiv.org/html/2605.12466
Code: https://github.com/jacobfa/Attractor
Authors: Jacob Fein-Ashley, Paria Rashidinejad (USC)
Date: May 12, 2026

# Attractor Models

A two-stage architecture: backbone Transformer proposes output embeddings → attractor module refines to fixed-point equilibrium via implicit differentiation.

## Key Results
- Pareto improvement over standard Transformers and looped models (140M-770M)
- Up to 46.6% perplexity reduction, 19.7% accuracy gain on CORE
- 770M Attractor Model beats 1.3B Transformer trained on twice the tokens
- 27M model: 91.4% Sudoku-Extreme, 93.1% Maze-Hard (frontier models fail)
- 25-31% fewer training FLOPs, O(1) memory in recurrence depth

## Equilibrium Internalization (Novel)
The backbone learns to place its initial guess near the fixed point over training.
Solver can often be removed at inference with minimal degradation.
Recurrence acts as a moving teacher that the model internalizes.

## Training
Implicit differentiation with one-step approximation (u≈v). Avoids backprop-through-time.
Anderson acceleration for fixed-point solver. Adaptive convergence-based step count.
