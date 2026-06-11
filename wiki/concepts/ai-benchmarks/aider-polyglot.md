---
title: "Aider Polyglot Benchmark"
type: concept
created: 2026-05-08
updated: 2026-05-08
status: active
tags:
  - benchmark
  - evaluation
  - coding-agents
  - developer-tooling
aliases:
  - aider-polyglot
  - "Aider Polyglot"
  - "polyglot benchmark"
sources:
  - https://aider.chat/2024/12/21/polyglot.html
  - https://github.com/Aider-AI/polyglot-benchmark
  - https://aider.chat/docs/leaderboards/
  - wiki/raw/articles/2025-04-29_xeophon-ai-benchmark-eval-series.md
related_entities:
  - entities/florian-brand.md
related_concepts:
  - concepts/ai-benchmarks-and-evals.md
  - concepts/llm-evaluation.md
  - concepts/ai-benchmarks/livecodebench.md
  - concepts/ai-benchmarks/swe-bench.md
---

# Aider Polyglot Benchmark

> **Part 3 of @xeophon's 18-part AI Benchmarks & Evals series.** A rare multi-language coding benchmark that tests LLMs on 225 challenging programming exercises across 6 languages — not just Python. Measures both code generation AND the ability to edit/fix code based on error feedback.

**Created by**: Aider-AI (Paul Gauthier) | **Released**: December 2024 | **Repository**: [Aider-AI/polyglot-benchmark](https://github.com/Aider-AI/polyglot-benchmark)

---

## What It Measures

Aider Polyglot evaluates two distinct coding capabilities:

1. **Code Generation (Pass 1)**: Given a natural language problem description in a specific programming language, produce a correct solution that passes all Exercism test cases
2. **Code Editing (Pass 2)**: If Pass 1 fails, the model receives test error feedback and gets a second attempt to fix its code — testing the ability to *edit* code based on execution results

This dual-pass design makes it unique: most coding benchmarks only test generation, but real-world development involves constant editing and debugging. The benchmark runs through the Aider AI pair-programming tool, measuring how well models perform in an agentic coding workflow.

---

## Languages Covered

| Language | Percentage of Exercises |
|----------|------------------------|
| C++ | ~40% |
| Go | ~10% |
| Java | ~10% |
| JavaScript | ~10% |
| Python | ~10% |
| Rust | ~10% |
| Other | ~10% |

The 225 exercises are sourced from **Exercism's language tracks** — curated, community-reviewed programming exercises specifically selected as among the hardest available. Exercises cover algorithms, data structures, language idioms, and problem-solving patterns.

---

## Data Sourcing Method

1. **Curated from Exercism**: Exercises are hand-picked from Exercism's open-source language track repositories, selecting the most challenging problems
2. **Multi-language by design**: Exercises span 6 languages intentionally to test polyglot coding ability, not just Python fluency
3. **Test-driven evaluation**: Each exercise comes with a comprehensive test suite; solutions must pass ALL tests
4. **Automated execution**: The Aider harness automatically runs tests, provides error feedback, and manages the two-attempt workflow
5. **Community-submitted results**: Leaderboard results come from community-submitted evaluations using the Aider CLI tool

---

## Key Numbers

| Metric | Value |
|--------|-------|
| **Total exercises** | 225 |
| **Languages** | C++, Go, Java, JavaScript, Python, Rust |
| **Source** | Exercism language tracks |
| **Attempts per problem** | 2 (initial + retry with error feedback) |
| **Scoring** | Pass rate after 2 attempts |
| **Current top score** | 88.0% (GPT-5, high reasoning) |
| **Models evaluated** | 22+ |

### Aider Polyglot Leaderboard (2025-2026)

| Rank | Model | Pass Rate | Edit Format | Cost |
|------|-------|-----------|-------------|------|
| 1 | GPT-5 (high) | 88.0% | 91.6% | $29.08 |
| 2 | GPT-5 (medium) | 86.7% | 88.4% | $17.69 |
| 3 | o3-pro (high) | 84.9% | 97.8% | $146.32 |
| 4 | Gemini 2.5 Pro (06-05, 32k think) | 83.1% | 99.6% | $49.88 |
| 5 | GPT-5 (low) | 81.3% | 86.7% | $10.37 |
| 6 | o3 (high) | 81.3% | 97.8% | — |
| 7 | Claude 3.7 Sonnet (32k think) | 64.9% | 97.8% | $36.83 |
| 8 | DeepSeek R1 | 56.9% | 96.9% | $5.42 |
| 9 | DeepSeek Chat V3 | 48.4% | 98.7% | $0.34 |

> **Cost efficiency standout**: DeepSeek Chat V3 achieves 48.4% at just $0.34 — by far the best value per dollar. DeepSeek R1 offers strong 56.9% at $5.42.

---

## @xeophon's Key Insights

From the Part 3 analysis (May 1, 2025):

1. **6 languages, not just Python**: Multi-language coding benchmarks are rarer than you'd expect. Most coding evals (HumanEval, MBPP, LiveCodeBench) are Python-only or Python-dominant
2. **Measures code editing, not just generation**: The two-attempt design with error feedback captures a critical real-world skill — fixing your own bugs
3. **Practical Exercism exercises**: Exercises are real programming problems, not synthetic competition tasks
4. **C++ dominance in dataset**: C++ makes up ~40% of exercises — the benchmark particularly tests systems-level language ability
5. **Edit format matters**: The benchmark also tracks "correct edit format" — whether the model can produce properly formatted code diffs, which is essential for agentic coding tools

---

## Strengths

- **True multi-language**: 6 languages, including systems languages (C++, Rust) — much broader than Python-only benchmarks
- **Code editing measured**: Two-attempt design tests the critical skill of fixing code based on error feedback
- **Real-world proxy**: Exercism exercises are practical, not artificial
- **Agentic workflow**: Runs through the Aider pair-programming tool, testing how models perform in a realistic coding assistant context
- **Edit format tracking**: Measures whether models can produce well-formed code edits — crucial for tool use
- **Cost transparency**: Leaderboard includes cost data, enabling price-performance comparisons

---

## Weaknesses

- **Small dataset**: 225 exercises is modest; limited statistical power for close comparisons
- **Only 6 languages**: While broader than most, still missing many important languages (TypeScript, C, Swift, Kotlin, etc.)
- **Exercism-specific biases**: Exercises from a single source may not represent all types of programming tasks
- **No real-world software engineering**: Single-file exercises don't test repo navigation, architecture, or multi-file changes
- **Static dataset**: Unlike LiveCodeBench, problems don't update — risk of eventual saturation
- **Community-submitted results**: Self-reported scores (not independently verified); potential for cherry-picking
- **Aider tool dependency**: Results are specific to the Aider harness; the same model might perform differently with other tools

---

## Relationship to Other Benchmarks

| Benchmark | Languages | Tests Editing? | Update Model |
|-----------|-----------|----------------|--------------|
| **Aider Polyglot** | 6 (C++, Go, Java, JS, Python, Rust) | Yes (2 attempts) | Static |
| **LiveCodeBench** | Python (primary) | Yes (self-repair) | Continuous |
| **HumanEval** | Python only | No | Static |
| **MBPP** | Python only | No | Static |
| **SWE-Bench** | Python (repo-level) | Yes (agentic) | Static |
| **MultiPL-E** | 18+ languages | No | Static |

---

## Related Pages

- [[concepts/evaluation/ai-benchmarks-and-evals]] — Full 18-part benchmark series overview
- [[entities/florian-brand]] — Florian Brand (@xeophon), series author
- [[concepts/ai-benchmarks/livecodebench]] — LiveCodeBench (contamination-free competition coding)
- [[concepts/ai-benchmarks/swe-bench]] — SWE-Bench (real-world software engineering)
- [[concepts/llm-evaluation]] — LLM evaluation landscape

---

## Sources

1. Paul Gauthier / Aider-AI, "Aider Polyglot Benchmark," Dec 2024. https://aider.chat/2024/12/21/polyglot.html
2. Aider Polyglot Benchmark Repository. https://github.com/Aider-AI/polyglot-benchmark
3. Aider LLM Leaderboards. https://aider.chat/docs/leaderboards/
4. LLM Stats, Aider-Polyglot Leaderboard. https://llm-stats.com/benchmarks/aider-polyglot
5. @xeophon (Florian Brand), "AI Benchmarks & Evals Series, Part 3: Aider Polyglot," May 1, 2025.
