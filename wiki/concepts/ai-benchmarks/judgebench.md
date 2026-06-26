---
title: "JudgeBench"
type: concept
created: 2026-06-26
updated: 2026-06-26
tags:
  - benchmark
  - evaluation
  - llm-as-judge
sources:
  - "GitHub: ScalerLab/JudgeBench"
related_concepts:
  - "[[llm-as-judge]]"
  - "[[reward-models]]"
  - "[[evaluation-methodology]]"
  - "[[bias-detection]]"
---

# JudgeBench

JudgeBench is a benchmark for evaluating **LLM-as-judge** systems, developed by Scaler Lab and available on GitHub (ScalerLab/JudgeBench). It systematically tests the alignment, bias, and reliability of language models used as automated evaluators.

## What It Measures

JudgeBench evaluates the quality and reliability of LLM-based judges:

- **Judge alignment**: Agreement with human expert judgments
- **Bias detection**: Systematic biases in evaluation (position, verbosity, style)
- **Reliability**: Consistency of judgments across repeated evaluations
- **Calibration**: How well confidence scores reflect actual accuracy
- **Robustness**: Resistance to manipulation and adversarial inputs

## Data/Methodology

The benchmark provides a comprehensive evaluation framework:

- **Multi-task evaluation**: Tests judges across diverse evaluation tasks
- **Bias probes**: Systematic testing for known judge biases (position bias, verbosity preference, etc.)
- **Human alignment datasets**: Gold-standard human judgments for comparison
- **Consistency testing**: Repeated evaluation with controlled variations
- **Adversarial testing**: Attempts to manipulate judge outputs through crafted inputs

## Key Results

- LLM judges exhibit measurable biases that affect evaluation quality
- Position bias and verbosity preference are common across judge models
- Judge alignment varies significantly across evaluation domains
- No single judge model excels across all evaluation dimensions

## Related Benchmarks

- [[rewardbench]] — Reward model evaluation including judge-like capabilities
- [[rewardbench-2]] — Advanced reward model benchmarking
- [[verifybench]] — Reasoning verifier evaluation
- [[decodingtrust]] — Trustworthiness evaluation

## Connections to Other Wiki Concepts

JudgeBench addresses the growing reliance on **[[llm-as-judge]]** systems for automated evaluation and training data generation. It connects to **[[reward-models]]** research by evaluating a key component of modern RLHF pipelines. The benchmark's focus on **[[bias-detection]]** and reliability has implications for **evaluation-methodology** across the field, as many benchmarks themselves rely on LLM judges for scoring. Understanding judge quality is essential for ensuring trustworthy automated evaluation.
