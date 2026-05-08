---
title: "Detecting when LLMs are Uncertain — Entropix Explained"
url: https://www.thariq.io/blog/entropix/
date: 2024-10-11
author: Thariq Shihipar (@trq212)
source: thariq.io
type: article
tags: [entropix, inference, sampling, entropy, varentropy, llm, reasoning, chain-of-thought]
---

# Detecting when LLMs are Uncertain — Entropix Explained

Thariq Shihipar - 11 October 2024 · 7 min read

This post explains the reasoning techniques developed by XJDR (@_xjdr) in the Entropix project.

## Core Idea

Entropix attempts to improve reasoning in models through being smarter at sampling during moments of uncertainty. It uses **entropy** and **varentropy** of the logit distribution to guide **adaptive sampling** strategies.

## Entropy and Varentropy

- **Entropy**: Measures how uniform the logit distribution is. High entropy = uncertain, low entropy = confident.
- **Varentropy**: The "shape" of uncertainty. High varentropy = disparate peaks (some tokens much more likely), low varentropy = even spread.

## The Entropy Quadrant (4 States)

### 1. Low Entropy, Low Varentropy
- A very peaked distribution (one highly probable outcome)
- **Strategy**: Standard argmax sampling — choose the token with highest probability

### 2. Low Entropy, High Varentropy
- Distribution with a few disparate peaks
- Could represent branching paths (e.g., Java vs C) or synonyms
- **Strategy**: Branch by predicting multiple logits, compare paths, possibly ask the user

### 3. High Entropy, Low Varentropy
- Uniform or near-uniform distribution
- Model genuinely doesn't recognize what it's seeing (out of distribution)
- **Strategy**: Insert a "thinking token" (e.g., "Wait...") to push the model toward higher confidence through additional compute

### 4. High Entropy, High Varentropy
- Spread-out but uneven distribution
- Model has no clear favorite but prefers some outputs
- **Strategy**: Higher temperature resampling, or branching + thinking tokens. Any of the top options may be solid choices.

## Implementation Details

From the entropix codebase (torch_sampler.py):

- **High Entropy, Low Varentropy** (ent > 3.0, vent < 0.1): Insert clarification token [2564]
- **High Entropy, High Varentropy** (ent > 5.0, vent > 5.0): Resample with temp_adj = 2.0 + 0.5 * attn_vent, top_p_adj = max(0.5, top_p - 0.2 * attn_ent)
- **Intermediate cases**: Adaptive sampling — take 5 samples, score by entropy/varentropy/attention, pick best

## Caveats

- No large-scale evals yet at time of writing (Oct 2024)
- Unclear how much this helps in practice
- Promising techniques and mental models for reasoning

## Sources

- [Entropix GitHub](https://github.com/xjdr-alt/entropix)
- [@_xjdr on X](https://x.com/_xjdr)
- [DEV Community deep dive](https://dev.to/m_sea_bass/entropix-sampling-techniques-for-maximizing-inference-performance-2hgc)
