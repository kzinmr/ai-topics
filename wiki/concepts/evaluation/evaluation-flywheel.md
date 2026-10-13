---
title: "Evaluation Flywheel"
tags: [evaluation]
sources:
  - https://learning.oreilly.com/library/view/ai-engineering/9781098166298/ch04.html
  - https://learning.oreilly.com/library/view/evals-for-ai/9798341660717/ch03.html
  - https://learning.oreilly.com/library/view/evals-for-ai/9798341660717/ch05.html
created: 2026-04-13
updated: 2026-10-14
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

## Ground the loop in observed failures

The 2026-10-14 outer-loop reading adds a concrete route from cases to reusable evaluation. Shankar and Husain's *Evals for AI Engineers*, Chapter 3, begins with trace inspection and free-form observations before organizing a failure taxonomy. Chapter 5 keeps judge-prompt examples, development cases and a final held-out set separate. Huyen's *AI Engineering*, Chapter 4, combines component/intermediate checks with end-to-end task evaluation and data slices.

[[concepts/modernization-evaluation-corpus]] applies this to changing recipes, prompts, tools and recovery procedures. Version cases, expected outcomes, rubric, evaluator configuration and evaluated system together. A targeted failure set can reveal weaknesses without estimating normal production prevalence; a raw judge pass rate is not automatically a business success rate.

Accountable domain judgement can supply the intended expectation. Quantification alone cannot correct an expectation inferred from the same mistaken generated implementation. Carry ambiguity and ownership through [[concepts/modernization-traceability]].

## Anti-Patterns

- **Evaluating only once**: Models are updated and use cases evolve
- **Relying on subjective evaluation**: Combine with quantitative metrics
- **Biased test cases**: Cover a representative distribution

## Related

- [[concepts/evaluation/ai-evals]] — AI Evals (Hamel Husain & Shreya Shankar)
- [[concepts/evaluation/llm-evaluation-harness]] — LLM Evaluation Harness
- [[comparisons/eval-tools-comparison]] — AI Eval Tools Comparison
- [[concepts/harness-engineering/system-architecture/infrastructure-noise]] — Infrastructure Noise in Agentic Evals
