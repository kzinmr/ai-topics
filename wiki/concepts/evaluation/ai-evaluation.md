---
title: "AI Evaluation"
type: concept
aliases:
  - ai-evaluation
  - llm-evaluation
  - evaluation-methods
created: 2026-04-25
updated: 2026-07-18
tags:
  - concept
  - evaluation
  - infrastructure
  - testing
related:
  - [[concepts/evaluation/llm-as-judge]]
  - [[concepts/evaluation/evaluation-flywheel]]
  - [[concepts/evaluation/offline-evaluation]]
  - [[concepts/evaluation/ai-benchmarks-and-evals]]
sources:
  - raw/articles/benchflow-awesome-evals-2025.md
  - https://github.com/benchflow-ai/awesome-agent-evals
  - raw/articles/2026-05-19_langfuse-academy-evals-explained.md
  - raw/articles/2026-06-15_langchain_building-100x-cheaper-trace-judge-fireworks.md
  - https://langfuse.com/academy/evaluate
---

# AI Evaluation

AI evaluation is the systematic process of judging whether an AI system's outputs are good, forming the critical feedback loop between experimentation and shipping in the **AI Engineering Loop**.

## The AI Engineering Loop

The AI Engineering Loop connects production behavior (tracing, monitoring) to structured iteration (datasets, experiments, evaluation). Each shipped improvement produces new data, and teams loop through this process continuously.

Evaluation sits between running an experiment and shipping a change: you have a dataset, you've run your application against it, and now you need to judge whether the outputs are good.

## Evaluation Methods

### Manual Evaluation

The foundational step: manually reviewing outputs to build intuition for what "good" and "bad" look like in your specific application. This produces human labels that serve as ground truth for validating automated evaluators later.

Teams that skip manual review and jump to automated evaluation often measure things that don't matter.

### Code-Based Evaluation

Deterministic checks that are fast, cheap, and produce the same result every time. Ideal for:
- Valid JSON / schema compliance
- Keyword or pattern presence/absence
- Length limits
- Executable SQL without errors

**Limitation**: Cannot assess meaning. Can check that "refund" appears but not whether the refund policy is correctly explained.

### LLM-as-a-Judge

Uses a language model to score outputs, required for qualities that require understanding language: relevance, tone appropriateness, summary accuracy.

**Critical considerations**:
- LLMs don't automatically grade as human experts would — they lack expert context
- Need calibration against human preferences to verify they measure what's intended
- Can share blind spots with the application's LLM, especially when same model family is used for both

When calibrated against human labels and backed by code-based checks, LLM judges are reliable evaluators.

### LLM Trace Judge

Trace judges extend the LLM-as-judge paradigm from single-turn evaluation to multi-turn production trace analysis. Instead of scoring isolated outputs against reference examples, trace judges infer quality signals — such as perceived errors — from real user interaction patterns: user corrections, rejection of agent actions, repeated requests, and assistant acknowledgements of mistakes.

In June 2026, LangChain and Fireworks published a study showing that a fine-tuned Qwen model, trained on perceived error detection across multiple trace datasets, matched or exceeded frontier model performance at roughly 100× lower cost. Labels were created through a cascade of model-assisted judgments plus human review for disagreements. The perceived error signal showed strong cross-domain transfer, confirming its generality beyond a single application.

See [[concepts/llm-trace-judge]] for the detailed methodology and [[raw/articles/2026-06-15_langchain_building-100x-cheaper-trace-judge-fireworks.md]] for the full article.

## Reference-Based vs Reference-Free

| Type | Description | Advantage |
|------|-------------|-----------|
| **Reference-Based** | Compares output against a predefined expected output | Precise, verifiable |
| **Reference-Free** | Assesses output on its own, without ground truth | Can be applied to unseen production data |

## Practical Guidelines

### When to Set Up Automated Evaluators

Start with manual review. Ask: is this a one-time fix or a generalization problem? If a simple prompt change resolves it, just make the change. If you can clearly identify a failure mode to test repeatedly across different inputs, set up an evaluator.

### What to Evaluate

Prefer **binary scores (pass/fail)** over graded scales (1–5). Binary scores force a clear definition of what separates acceptable from unacceptable. Graded scales introduce ambiguity about what a 3 means vs. a 4.

### Combining Methods

Mature setups use all three methods together. Each quality gets its own evaluator, and together they provide a view on overall application quality.

## Langfuse Academy Framework

Langfuse Academy, launched May 2026, provides an open educational resource walking through the full AI engineering lifecycle: **Trace → Monitor → Build Datasets → Experiment → Evaluate**. The evaluation page covers all three methods and their integration into the broader AI Engineering Loop.

See [[raw/articles/2026-05-19_langfuse-academy-evals-explained.md]] for the full Langfuse Academy evaluation guide.

## Related Concepts

- [[concepts/evaluation/llm-as-judge]] — Detailed methodology for LLM-based evaluation
- [[concepts/llm-trace-judge]] — Extending LLM-as-judge to multi-turn production trace analysis
- [[concepts/evaluation/evaluation-flywheel]] — Evaluation as a continuous improvement loop
- [[concepts/evaluation/offline-evaluation]] — Offline evaluation techniques
- [[concepts/evaluation/ai-benchmarks-and-evals]] — AI Benchmarks & Evals MOC (systematic navigation of all benchmark/eval pages)

## Sources

- [Evals, explained — Langfuse Academy](https://langfuse.com/academy/evaluate) — May 2026
- [[raw/articles/2026-05-19_langfuse-academy-evals-explained.md]]
- [Building a 100× Cheaper Trace Judge with Fireworks — LangChain Blog](https://www.langchain.com/blog/building-a-100x-cheaper-trace-judge-with-fireworks) — June 2026
- [[raw/articles/2026-06-15_langchain_building-100x-cheaper-trace-judge-fireworks.md]]
