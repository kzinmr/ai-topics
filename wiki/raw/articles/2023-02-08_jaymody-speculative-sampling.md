---
title: "Speculative Sampling"
author: "Jay Mody"
url: "https://jaykmody.com/blog/speculative-sampling/"
date: 2023-02-08
tags:
  - llm-inference
  - speculative-sampling
  - optimization
---

# Speculative Sampling: Accelerating LLM Inference

**Source:** Jay Mody
**Key Concept:** A method to speed up LLM decoding by using a small "draft" model to predict future tokens, which are then verified in parallel by a larger "target" model.

## The Problem: Autoregressive Sampling
Standard LLM generation is autoregressive — one token at a time.

**Time Complexity:** O(N · t_target) where N = tokens to decode, t_target = time per forward pass.

## The Solution: Speculative Sampling
Uses two models:
1. **Draft Model (M_draft):** Small, fast (e.g., 7B)
2. **Target Model (M_target):** Large, slow (e.g., 70B)

### Algorithm:
1. Draft model autoregressively predicts K future tokens
2. Target model performs a single forward pass on the full sequence
3. Accept/reject each draft token based on probability ratios
4. Bonus token if all K accepted

### Properties:
- Mathematically equivalent to sampling from target model alone
- Architecture agnostic
- Common phrases are easy for small models → big savings

### Performance (DeepMind Chinchilla 70B/7B):
- HumanEval: 2.46x speedup
- XSum: 1.92x speedup

### Local Reproduction (GPT-2 1.5B / 124M, K=4):
- Greedy (Temp=0): 2.23x speedup, identical output
- Non-greedy: similar speedup, statistically equivalent distribution
