---
title: "SimpleQA"
type: concept
created: 2026-06-10
updated: 2026-06-10
tags:
  - benchmark
  - evaluation
  - reasoning
  - model
aliases:
  - simpleqa
  - simple-qa
status: active
sources:
  - https://openai.com/index/simpleqa/
  - wiki/raw/articles/2025-04-29_xeophon-ai-benchmark-eval-series.md
related:
  - "[[concepts/ai-benchmarks-and-evals]]"
  - "[[concepts/gpqa]]"
  - "[[concepts/hle]]"
---

# SimpleQA

> **Part 7 of @xeophon's 18-part AI Benchmarks & Evals series.** A factual accuracy benchmark from OpenAI designed as a "sanity check" — testing whether models can answer short, unambiguous factual questions without hallucinating.

## Overview

SimpleQA is a benchmark of **short, fact-seeking questions** with unambiguous answers, created by OpenAI to measure factual accuracy. It serves as a baseline check: can the model answer straightforward factual questions correctly, or does it hallucinate?

**Announced**: OpenAI blog, 2024 | **Purpose**: Factual accuracy sanity check

## What It Measures

| Aspect | Detail |
|--------|--------|
| **Domain** | Factual knowledge retrieval |
| **Task type** | Short-answer factual questions |
| **Key property** | Unambiguous, verifiable answers |
| **Difficulty** | Ranges from easy to niche — designed to catch hallucination, not to be maximally hard |
| **Evaluation** | Exact match or LLM-judged equivalence against reference answers |

## Design Philosophy

SimpleQA is intentionally **not** the hardest benchmark. Its value lies in:

1. **Hallucination detection**: Models that confidently produce wrong answers on simple factual questions reveal fundamental reliability issues
2. **RL training validation**: After RL training (which can cause knowledge loss), SimpleQA checks whether the model retains basic factual knowledge
3. **Sanity check**: A model scoring well on GPQA but poorly on SimpleQA has a problem

## @xeophon's Key Insight

> "Sanity check. Important for RL-trained models." — @xeophon, Part 7

Xeophon emphasizes SimpleQA's role as a **regression detector** for RL-trained models. Reinforcement learning can cause models to lose factual knowledge while gaining reasoning ability. SimpleQA catches this trade-off.

## Strengths

- **Simple and interpretable**: Easy to understand what's being tested and why a model failed
- **Hallucination detector**: Directly measures whether models fabricate answers to simple questions
- **RL regression check**: Critical for validating that RL training doesn't destroy factual knowledge
- **Unambiguous answers**: Clear ground truth reduces evaluation ambiguity

## Weaknesses

- **Limited scope**: Only tests factual recall — not reasoning, creativity, or safety
- **Not a discriminator**: Most frontier models score well, limiting differentiation
- **Static**: Fixed question set — contamination risk
- **English-only**: No multilingual coverage

## Related Pages

- [[concepts/ai-benchmarks-and-evals]] — Full benchmarks & evals MOC
- [[concepts/gpqa]] — GPQA (harder, graduate-level science)
- [[concepts/hle]] — HLE (hardest knowledge benchmark)
- [[concepts/mmlu-pro]] — MMLU Pro (broader multi-domain knowledge)

## Sources

1. OpenAI, "SimpleQA." https://openai.com/index/simpleqa/
2. @xeophon, "AI Benchmarks & Evals Series, Part 7: SimpleQA," May 7, 2025.
