---
title: "Generative Recursive Reasoning (GRAM)"
source: https://arxiv.org/html/2605.19376
date: 2026-05-19
authors: Junyeob Baek, Mingyu Jo, Minsu Kim, Mengye Ren, Yoshua Bengio, Sungjin Ahn (KAIST, Mila, NYU, UdeM)
---

# Generative Recursive Reasoning Models (GRAM)

GRAM turns recursive latent reasoning into probabilistic multi-trajectory computation. Unlike deterministic Recursive Reasoning Models that follow a single latent trajectory, GRAM samples stochastic trajectories enabling multiple hypotheses and alternative solution strategies.

## Architecture
- Two-level hierarchical latent state: high-level h (abstract reasoning, stochastic) and low-level l (fine-grained, deterministic)
- Learnable stochastic guidance around deterministic proposal at high level
- Inference scales with both recursive depth AND parallel trajectory sampling (width-based scaling)
- Supports conditional reasoning p(y|x) and unconditional generation p(x)

## Results
- 10M params GRAM outperforms 27M param deterministic baselines on Sudoku-Extreme, ARC-AGI, N-Queens, Graph Coloring
- Direct prediction baselines score 0% on Sudoku and ARC-AGI-2 — recursive computation essential
- Unconditional generation capability demonstrated on binarized MNIST and Sudoku
