---
title: "A Deep Dive on LM Evaluation"
source: "Google Slides presentation"
author: "Hailey Schoelkopf"
date: 2024-06-11
url: https://docs.google.com/presentation/d/1qTaDYqLCgxkUaTfxQkN1it4tx6_jixwv9ZtsbqQgE4U/edit
tags:
  - evaluation
  - lm-eval
  - loglikelihood
  - perplexity
  - generation
  - eleutherai
---

# A Deep Dive on LM Evaluation

**Presenter:** Hailey Schoelkopf (Research Scientist at EleutherAI, Maintainer of LM Evaluation Harness)
**Date:** June 11, 2024

## Overview

Evaluation is a critical but difficult pillar of LM development. The presentation explores why evaluation is challenging, the technical mechanics of how evaluations work under the hood, and best practices for researchers.

## Three Core Evaluation Methodologies

### A. Loglikelihood
- Measures the probability an LM assigns to a specific string, conditioned on an input
- Algorithm: Feed (x + y) into the LM, sum log probabilities of each token in y
- Key insight: LM returns logits of shape [SequenceLength, VocabSize], predicting the "guess" for the next token at every position simultaneously
- Used for multiple-choice evaluation: model compares loglikelihoods of fixed answer strings

**Pros:** Significantly cheaper than generation (prefill only), no parsing failures
**Cons:** No freeform chat performance, prevents Chain-of-Thought, artificially easy
**Recommendation:** Best for base models, especially smaller ones

### B. Perplexity (PPL)
- Measures how well a model "fits" a given data distribution
- Average loglikelihood over tokens in a dataset

**Pros:** Easy to set up, scales smoothly, acts like a validation set
**Cons:** Generally meaningless for instruction-tuned models, distanced from actual generation quality

### C. Text Generation
- Model generates free-form text which is then evaluated
- Evaluation shortcuts: Heuristics/string matching, LLM-as-a-judge, human annotators

## Key Takeaways

- Base models → loglikelihood/multiple-choice for raw capability
- Chat models → generation-based metrics
- Loglikelihood evaluations are much faster (avoid token-by-token generation cost)
- Use standardized libraries like lm-evaluation-harness for comparable results
