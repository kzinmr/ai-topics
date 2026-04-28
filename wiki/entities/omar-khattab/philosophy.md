---
title: "Omar Khattab — Decomposition Philosophy"
tags: [philosophy, research-philosophy]
created: 2026-04-24
updated: 2026-04-24
type: sub-entity
---

# Philosophy: Decomposition at the Right Joints

In 2026, [[entities/omar-khattab]] articulated the unifying philosophy across all four of his major research contributions — a direct response to "bitter lesson maximalists" who believe only scale and compute matter:

> *"A subtle thing that's worth observing is how all four are actually riffs on the same fundamental concept: decomposing something that the mainstream paradigm insists as treating as a monolith."*
> — Omar Khattab (@lateinteraction), 2026

## The Four "Riffs" on Decomposition

| Framework | What it Decomposes | Monolith it Replaces | Longevity |
|-----------|-------------------|---------------------|-----------|
| **Late Interaction ([[entities/omar-khattab/colbert|ColBERT]])** | Document representations → sets of objects; similarity → compositional operations | Single-vector dense embeddings | 6.5+ years (2020–present) |
| **[[entities/omar-khattab/dspy|DSPy]]** | Specification vs optimization; AI programs → symbolic modules with NL specs | Monolithic prompt debt | 3.5+ years (2023–present) |
| **[[entities/omar-khattab/gepa|GEPA]]** | Learning signals → actual tokens + feedback (not scalar rewards) | Policy gradient RL rewards | Emerging (2025) |
| **[[entities/omar-khattab/rlm|RLMs]]** | Hard problems → symbolic programs that invoke models; context → recursive access | Monolithic attention over massive contexts | Emerging (2025) |

## Against Bitter Lesson Maximalism

Khattab explicitly argues that decomposition, when done correctly, is **compatible with scaling** — not opposed to it:

> *"I guess I failed to make that clear, but this is a post against the naive bitter lesson maximalists. You *can* and in fact *need* to win with decomposition. It's not against scale and does not need to expire with time. It's what enables scaling to go beyond brute force."*
> — Omar Khattab, X post (2026)

The key insight: **decomposition done poorly runs foul of the bitter lesson** (Sutton, 2019), but decomposition done at the *right fundamental joints* enables scaling to transcend brute force.

## Connection to Harness Engineering

Khattab's decomposition philosophy aligns with Anthropic's Harness Engineering principle: **design the right scaffolding, don't just scale the model**.
