---
title: "AI-Resistant Technical Evaluations"
type: concept
created: 2026-05-08
updated: 2026-05-26
tags:
  - evaluation
  - company
  - agent-safety
  - benchmark
aliases:
  - AI-resistant take-home tests
  - AI-proof evaluations
status: active
sources:
  - raw/articles/2026-05-08_anthropic-engineering_AI-resistant-technical-evaluations.md
  - https://www.anthropic.com/engineering/AI-resistant-technical-evaluations
related:
  - eval-awareness-browsecomp
  - swe-bench
  - frontier-swe-benchmark
---

# AI-Resistant Technical Evaluations

Design principles for AI-resistant technical evaluations (hiring tests) by Tristan Hume, lead of Anthropic's Performance Optimization team. Practical insights from three redesigns driven by Claude model evolution.

## The Problem

> A take-home test that can distinguish human skill levels today may be trivially solved by a model tomorrow, rendering it worthless as an evaluation tool.

### History of Defeat by Claude Models

| Version | Duration | Defeated By |
|-----------|------|------|
| v1 (early 2024) | ~1.5 years | Claude 3.7 Sonnet: >50% of candidates would be better off delegating to Claude Code |
| v1 broken | May 2025 | Claude Opus 4: more optimized solutions than nearly all humans within 4-hour limit |
| v2 | A few months | Claude Opus 4.5: matches the best human performance in 2 hours (and that human also uses Claude 4 heavily) |

## Original Test Design

### Challenge
Code optimization on a pseudo-accelerator (TPU-like) running on a Python simulator:
- Manually managed scratchpad memory
- VLIW (parallel execution across multiple units)
- SIMD (vector operations)
- Multi-core

### Design Principles
1. **Job relevance**: Problems that give a taste of actual work
2. **High signal**: Opportunity to demonstrate a wide range of abilities, not dependent on a single insight
3. **No specialized knowledge required**: Learnable with good fundamentals
4. **Fun**: Fast iteration loops, depth, room for creativity
5. **AI-assistance tolerant**: Long-term problems that AI cannot fully solve

### Results
- 1,000+ candidates tested, dozens hired
- Contributed to shipping all models since Claude 3 Opus and standing up Trainium clusters
- Identified high-potential new graduates who showed aptitude despite limited experience

## v3: Going in a Weird Direction

### Attempt 1 (Failed): Data Transposition Problem
- Claude Opus 4.5 found an unexpected optimization: "transposing the entire computation"
- Fully solved with ultrathink → problems with abundant training data (banking/banking competition) favor AI

### Attempt 2 (Successful): Zachtronics-style Puzzle
- Extremely constrained instruction set (Shenzhen I/O style)
- Compete for optimal solutions with minimum instructions
- No visualization or debugging tools → also evaluates tool-building ability
- Shift from "realism" to "novelty"

> "The original worked because it resembled real work. The replacement works because it simulates novel work."

## Public Challenge

The original test is publicly available with no time limit:
- Claude Opus 4.5: 1,487 cycles (11.5 hours in the harness)
- If you can beat this, contact `performance-recruiting@anthropic.com`

## Insights

- Realism has become a luxury good
- Human advantage only persists over "sufficiently long time horizons"
- "Out-of-distribution" problem design is key against AI's broad training data
- Adversarial nature of evaluation: the smarter models get, the shorter-lived tests become

## See Also

- [[concepts/eval-awareness-browsecomp]] — Eval awareness and benchmark contamination
- [[concepts/ai-benchmarks/swe-bench]] — SWE-bench benchmark
- [[concepts/frontier-swe-benchmark]] — Frontier SWE benchmark
- [[concepts/infrastructure-noise-agent-evals]] — Infrastructure noise in agent evals
