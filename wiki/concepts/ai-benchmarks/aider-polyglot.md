---
title: "Aider Polyglot Benchmark"
type: concept
created: 2026-06-10
updated: 2026-06-10
tags:
  - benchmark
  - evaluation
  - coding-agents
  - software-engineering
aliases:
  - aider-polyglot
  - aider-polyglot-benchmark
status: active
sources:
  - https://aider.chat/docs/leaderboards/
  - wiki/raw/articles/2025-04-29_xeophon-ai-benchmark-eval-series.md
related:
  - "[[concepts/ai-benchmarks-and-evals]]"
  - "[[concepts/livecodebench]]"
  - "[[concepts/swe-bench]]"
---

# Aider Polyglot Benchmark

> **Part 3 of @xeophon's 18-part AI Benchmarks & Evals series.** A multi-language code editing benchmark that tests LLMs across 6 programming languages using real Exercism exercises — rare in a landscape dominated by Python-only evaluations.

## Overview

Aider Polyglot evaluates how well LLMs can **edit existing code** (not just generate from scratch) across 6 programming languages. Built by Paul Gauthier as part of the [Aider](https://aider.chat/) AI pair-programming tool's benchmark suite, it uses 225 exercises from the [Exercism](https://exercism.org/) platform.

## What It Measures

| Aspect | Detail |
|--------|--------|
| **Domain** | Multi-language code editing |
| **Task type** | Code modification and bug fixing (not generation from scratch) |
| **Languages** | Python, JavaScript, TypeScript, Java, C#, Go (6 languages) |
| **Dataset** | 225 Exercism exercises (roughly 25 per language with variations) |
| **Evaluation** | Automated test suite execution — each exercise comes with tests |
| **Interaction** | Multi-turn: LLM receives exercise description + existing code + test failures → edits code |

## Key Design Choices

1. **Editing, not generation**: Unlike HumanEval (generate from scratch), Aider Polyglot tests whether models can understand existing code and make targeted modifications — closer to real developer workflows
2. **6 languages**: Python-only benchmarks dominate the landscape. Aider Polyglot is rare in testing JavaScript, TypeScript, Java, C#, and Go alongside Python
3. **Real exercises**: Exercism exercises are community-designed, pedagogically structured, and come with test suites — not synthetic
4. **Test-driven**: Success is determined by running the exercise's test suite, not by human judgment or LLM-as-judge

## @xeophon's Key Insight

> "6 languages, not just Python. Rarer than expected." — @xeophon, Part 3

Xeophon highlights that despite Python's dominance in AI/ML, real-world software engineering spans many languages. Aider Polyglot fills a gap that most benchmarks ignore. The multi-language design also reveals model-specific language biases — a model may excel at Python but struggle with Go or C#.

## Strengths

- **Multi-language coverage**: Tests breadth of programming language understanding, not just Python proficiency
- **Editing paradigm**: Closer to real developer work than generate-from-scratch benchmarks
- **Test-driven evaluation**: Objective, reproducible, no human judgment needed
- **Real exercises**: Community-designed pedagogical problems, not synthetic
- **Aider integration**: Directly measures performance in a real AI coding tool

## Weaknesses

- **Relatively easy**: Exercism exercises are pedagogical (beginner-to-intermediate), not production-level complexity
- **Small dataset**: 225 exercises limits statistical power
- **Static**: Fixed exercise set — risk of contamination over time
- **No agentic capability**: Tests single-file code editing, not codebase navigation or multi-file refactoring
- **Aider-specific**: Optimized for Aider's edit format; may not generalize to other coding tools

## Related Pages

- [[concepts/ai-benchmarks-and-evals]] — Full benchmarks & evals MOC
- [[concepts/livecodebench]] — LiveCodeBench (competition coding, contamination-free)
- [[concepts/swe-bench]] — SWE-Bench (real-world GitHub issue resolution)
- [[concepts/evaluation-coding-agents]] — Coding agent evaluation methodology

## Sources

1. Aider Leaderboard. https://aider.chat/docs/leaderboards/
2. Exercism. https://exercism.org/
3. @xeophon, "AI Benchmarks & Evals Series, Part 3: Aider Polyglot," May 1, 2025.
