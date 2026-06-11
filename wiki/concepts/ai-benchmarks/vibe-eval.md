---
title: "Vibe-Eval"
type: concept
created: 2026-06-10
updated: 2026-06-10
tags:
  - benchmark
  - evaluation
  - methodology
  - ai-agents
aliases:
  - vibe-eval
  - vibeeval
status: active
sources:
  - https://arxiv.org/abs/2405.02716
  - wiki/raw/articles/2025-04-29_xeophon-ai-benchmark-eval-series.md
related:
  - "[[concepts/ai-benchmarks-and-evals]]"
  - "[[concepts/evaluation/ai-evaluation]]"
---

# Vibe-Eval

> **Part 8 of @xeophon's 18-part AI Benchmarks & Evals series.** A personalized evaluation benchmark built on the idea that everyone should have their own eval — using custom prompt sets based on personal interests and use cases.

## Overview

Vibe-Eval introduces the concept of **personalized evaluation**: instead of a universal benchmark, users create custom prompt sets that reflect their actual use cases and preferences. The name captures the idea of testing whether a model matches your "vibe" — your specific needs, style, and quality expectations.

**Paper**: [arXiv 2405.02716](https://arxiv.org/abs/2405.02716) (May 2024)

## What It Measures

| Aspect | Detail |
|--------|--------|
| **Domain** | Personalized model suitability |
| **Task type** | Custom prompts reflecting user-specific use cases |
| **Key innovation** | User-defined evaluation criteria, not universal benchmarks |
| **Evaluation** | User judgment (manual or customized LLM-as-judge) |
| **Philosophy** | "Everyone should have their own eval" |

## Core Concept

Traditional benchmarks ask: "Which model is best on average?"
Vibe-Eval asks: "Which model is best **for me**?"

This shift recognizes that:
1. **Use cases vary wildly**: A novelist, a programmer, and a customer support agent need very different things from a model
2. **Quality is subjective**: What counts as "good" depends on context, audience, and purpose
3. **Average performance is misleading**: A model that's 2nd-best at everything might be best for your specific combination of needs

## @xeophon's Key Insight

> "Custom prompts. Everyone should have their own." — @xeophon, Part 8

Xeophon frames Vibe-Eval as a philosophical statement as much as a benchmark. The idea that evaluation should be personal challenges the entire model-card-leaderboard paradigm.

## Strengths

- **User-centric**: Tests what actually matters to the individual user
- **Flexible**: Adapts to any domain, language, or use case
- **Practical**: Directly measures production-relevant performance
- **Anti-leaderboard**: Encourages users to think beyond aggregate scores

## Weaknesses

- **Not standardized**: Results are personal and not comparable across users
- **Requires effort**: Users must design and maintain their own prompt sets
- **No community benchmarks**: Difficult to share or aggregate results
- **Subjective evaluation**: Relies on user judgment, which may be inconsistent

## Related Pages

- [[concepts/ai-benchmarks-and-evals]] — Full benchmarks & evals MOC
- [[concepts/evaluation/ai-evaluation]] — AI evaluation methods (Langfuse Academy)
- [[concepts/evaluation/evals-vs-monitoring-debate]] — Evals vs monitoring debate
- [[concepts/evaluation/evaluation-flywheel]] — Evaluation as continuous improvement

## Sources

1. arXiv 2405.02716. https://arxiv.org/abs/2405.02716
2. @xeophon, "AI Benchmarks & Evals Series, Part 8: Vibe-Eval," May 8, 2025.
