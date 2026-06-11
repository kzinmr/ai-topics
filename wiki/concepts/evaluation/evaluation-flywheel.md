---
title: "Evaluation Flywheel"
tags: [evaluation]
created: 2026-04-13
updated: 2026-05-27
type: concept
---

# Evaluation Flywheel

A development pattern from OpenAI's cookbook that cycles evaluation and improvement.

## Core Concept

Frames model and agent improvement as a **continuous feedback loop**:

```
Data Collection → Evaluation → Analysis → Improvement → Data Collection → ...
```

This is a platform-agnostic methodology composed of the following elements.

## Key Components

### 1. Building a Golden Dataset

- A collection of representative input cases
- Correct answer labels for expected outputs
- Stratified by difficulty (easy, normal, edge cases)
- Regularly updated and expanded

### 2. Multi-Metric Evaluation

Rather than a single score, evaluate across multiple dimensions:

| Metric | Purpose |
|--------|---------|
| Accuracy | Correctness rate |
| Latency | Response speed |
| Cost | Token cost |
| Consistency | Reproducibility |
| Safety | Safety |

### 3. Regression Detection

- Monitor whether new changes break existing test cases
- Version control for evaluation results
- Automatic alerts when thresholds are breached

### 4. Continuous Improvement Loop

1. Identify bottlenecks from evaluation results
2. Form hypotheses about prompts, tools, and architecture
3. Validate with A/B testing
4. Deploy successful changes to production
5. Add new cases to the Golden Dataset

## Anti-Patterns

- **Evaluating only once**: Models are updated and use cases evolve
- **Relying on subjective evaluation**: Combine with quantitative metrics
- **Biased test cases**: Cover a representative distribution

## Related

- [[concepts/evaluation/ai-evals]] — AI Evals (Hamel Husain & Shreya Shankar)
- [[concepts/evaluation/llm-evaluation-harness]] — LLM Evaluation Harness
- [[comparisons/eval-tools-comparison]] — AI Eval Tools Comparison
- [[concepts/harness-engineering/system-architecture/infrastructure-noise]] — Infrastructure Noise in Agentic Evals
