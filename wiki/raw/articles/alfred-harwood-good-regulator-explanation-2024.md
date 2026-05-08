---
title: "A Straightforward Explanation of the Good Regulator Theorem"
author: Alfred Harwood
source_url: https://www.lesswrong.com/posts/JQefBJDHG6Wgffw6T/a-straightforward-explanation-of-the-good-regulator-theorem
date: 2024-11-18
platform: LessWrong
points: 91
curated: true
tags: [Good Regulator Theorems, Agent Foundations, AI, World Modeling]
ingested: 2026-05-08
---

# A Straightforward Explanation of the Good Regulator Theorem
**Author:** Alfred Harwood | **Date:** 2024-11-18 | **Platform:** LessWrong | **Points:** 91 (Curated)

## Purpose
Aimed at filling the gap for a medium-length, entry-level explainer of the original Good Regulator Theorem. Written during the agent foundations fellowship with Alex Altair (funded by LTFF).

## The Setup
Visualized as a causal Bayes net with three variables:
- **System (S)**: The thing being controlled — has various possible states
- **Regulator (R)**: The controller — observes S and takes actions
- **Outcome (Z)**: Determined by both S and R together

The regulator chooses policy P(R|S) to minimize entropy of Z.

## The Theorem
"What makes a regulator 'good'?"
1. It minimizes the entropy of outcome Z
2. It is not unnecessarily complex (no randomness that doesn't affect Z)

Under these conditions, for any optimal regulator: **R is a deterministic function of S**. That is, all R-values with nonzero probability for a given S must produce the same Z.

## Relationship to the 'Gooder Regulator'
Harwood notes that Wentworth's 'Gooder Regulator' theorem adds the crucial constraint: **limited internal state forces actual model-building**. The original theorem only shows equivalence, not that the regulator internally reconstructs S.

## "What counts as a model?"
The post deliberately brackets this philosophical question to focus on the math. The key mathematical result: R becomes a deterministic function of S under optimality + minimal noise conditions.
