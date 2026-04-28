---
title: "Instruction Fine-Tuning (IFT)"
type: concept
created: 2026-04-28
updated: 2026-04-28
tags: [fine-tuning, training, evaluation, instruction-tuning]
sources:
  - https://www.gilesthomas.com/2026/04/llm-from-scratch-32l-interventions-instruction-fine-tuning-tests
  - https://crfm.stanford.edu/2023/03/13/alpaca.html
---

# Instruction Fine-Tuning (IFT)

## Overview

Instruction fine-tuning adapts pre-trained language models to follow user instructions effectively. Unlike raw pre-training which optimizes for next-token prediction on internet text, IFT explicitly trains models to respond to prompts in a structured, useful manner.

## Evaluation Challenge: Test Loss vs Real-World Utility

A key insight from Giles Thomas's LLM-from-scratch experiments (Part 32l, April 2026) demonstrates that **test set loss does not necessarily correlate with real-world instruction-following ability**.

### The Problem with Single-Model Evaluation

When evaluating a single model's instruction responses using an LLM judge, the judge's inherent randomness produces inconsistent scores — even for identical inputs run at different times. This means isolated quality scores are not reliable for comparing models that are close in quality.

### Paired Evaluation Solution

The fix is **paired evaluation**: present responses from multiple models side-by-side to the judge simultaneously, forcing relative rather than absolute scoring. This reduces variance and produces more meaningful comparisons.

### Key Findings

| Model | Test Loss | IFT Score | Notes |
|-------|-----------|-----------|-------|
| OpenAI GPT-2 medium | 3.231 | 39.64 | Baseline |
| OpenAI GPT-2 small | 3.500 | 16.66 | Expected lower |
| Cloud FineWeb 8×A100 40GB | 3.674 | 16.5 | Similar to GPT-2 small despite lower loss |
| FineWeb-Edu local train | 4.135–4.167 | 15.77–16.41 | Higher IFT scores than loss suggests |

**Critical Insight**: The FineWeb-Edu models scored much higher on IFT than their test loss would predict, suggesting that **training data quality matters more for instruction-following than raw model size or loss**.

## Implications for Model Development

1. **Don't rely solely on test loss** for model selection if instruction-following is the target use case
2. **Data curation matters**: Educational/high-quality datasets produce better instruction-following behavior
3. **Evaluation methodology matters**: Paired evaluation is more reliable than single-model scoring
4. **The "smart but ignorant" hypothesis**: Models can have low loss (be "smart" at next-token prediction) but lack the knowledge density needed for good instruction following

## Related Concepts

- [[concepts/fine-tuning]] — General fine-tuning overview
- [[concepts/llm-training-coherence-evolution]] — Training methodology evolution
- [[entities/gpjt]] — Giles Thomas's LLM training experiments
- [[concepts/evaluation-benchmarks]] — Model evaluation approaches

## Sources

- [Giles Thomas: LLM from Scratch Part 32l](https://www.gilesthomas.com/2026/04/llm-from-scratch-32l-interventions-instruction-fine-tuning-tests) — Instruction fine-tuning evaluation methodology
- [Stanford Alpaca Dataset](https://crfm.stanford.edu/2023/03/13/alpaca.html) — Common instruction-tuning dataset
