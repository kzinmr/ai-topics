---
title: "BFCL V3 (Berkeley Function Calling Leaderboard)"
type: concept
created: 2026-06-10
updated: 2026-06-10
tags:
  - benchmark
  - evaluation
  - tool-calling
  - ai-agents
aliases:
  - bfcl-v3
  - berkeley-function-calling-leaderboard
  - bfcl
status: active
sources:
  - https://gorilla.cs.berkeley.edu/leaderboard.html
  - wiki/raw/articles/2025-04-29_xeophon-ai-benchmark-eval-series.md
related:
  - "[[concepts/ai-benchmarks-and-evals]]"
  - "[[concepts/tau-bench]]"
  - "[[concepts/ifeval]]"
---

# BFCL V3 (Berkeley Function Calling Leaderboard)

> **Part 9 of @xeophon's 18-part AI Benchmarks & Evals series.** The industry-standard leaderboard for evaluating LLM function calling (tool use) capabilities — with multi-turn, multi-step interactions and human-validated test cases.

## Overview

The Berkeley Function Calling Leaderboard (BFCL) evaluates how well LLMs can **call functions and use tools** — a critical capability for AI agents. BFCL V3, the latest version, moved beyond single-turn function calls to test **multi-turn, multi-step** tool use interactions with human validation.

**Website**: [gorilla.cs.berkeley.edu/leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html) | **Maintained by**: UC Berkeley (Gorilla project)

## What It Measures

| Aspect | Detail |
|--------|--------|
| **Domain** | Function calling / tool use |
| **Task type** | Generate correct function calls given a task description and available tools |
| **V3 innovation** | Multi-turn, multi-step interactions (not just single-shot calls) |
| **Evaluation** | Human-validated test cases comparing expected vs actual function calls |
| **Format** | Given a natural language task + function/tool definitions → produce correct API calls |

### Evaluation Categories

| Category | What It Tests |
|----------|--------------|
| **Simple function** | Single function call with straightforward parameters |
| **Multiple function** | Choosing the right function from several options |
| **Parallel function** | Calling multiple functions simultaneously |
| **Parallel multiple** | Multiple functions + multiple choices |
| **Multi-turn** | Sequential function calls across conversation turns |
| **Multi-step** | Chained function calls where output of one feeds into another |

## @xeophon's Key Insight

> "Multi-turn, multi-step. Human-validated." — @xeophon, Part 9

Xeophon highlights BFCL V3's shift from single-turn to multi-turn evaluation. Real-world agent workflows involve chains of tool calls with dependencies — a single function call is rarely sufficient. The human validation of test cases adds reliability.

## Strengths

- **Industry standard**: Widely cited and used by model providers for tool-use benchmarking
- **Multi-turn, multi-step**: Tests realistic agent workflows, not just individual function calls
- **Human-validated**: Test cases verified by human annotators
- **Comprehensive**: Covers simple to complex function calling scenarios
- **Open**: Public leaderboard with community submissions

## Weaknesses

- **Synthetic tasks**: Function calling scenarios are crafted, not from real production systems
- **No real-world side effects**: Tests whether calls are correct, not whether they achieve the desired outcome
- **API-specific**: Evaluation depends on specific API formats and documentation styles
- **English-centric**: Primarily English-language task descriptions

## Related Pages

- [[concepts/ai-benchmarks-and-evals]] — Full benchmarks & evals MOC
- [[concepts/tau-bench]] — Tau-Bench (function calling with LLM-simulated users)
- [[concepts/ifeval]] — IFEval (instruction following)
- [[concepts/tool-calling]] — Tool calling concepts

## Sources

1. BFCL Leaderboard. https://gorilla.cs.berkeley.edu/leaderboard.html
2. @xeophon, "AI Benchmarks & Evals Series, Part 9: BFCL V3," May 9, 2025.
