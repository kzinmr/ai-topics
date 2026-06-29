---
title: "AA-Briefcase"
created: 2026-06-29
updated: 2026-06-29
type: concept
tags: [benchmark, agent-evaluation, evals, agentic-engineering, llm-as-judge]
sources: [raw/articles/2026-06-29_artificial-analysis_aa-briefcase-benchmark.md]
---

# AA-Briefcase

**AA-Briefcase** is an agentic knowledge work benchmark developed by **Artificial Analysis** to evaluate frontier models on long-horizon, multi-week professional workflows.

## Structure

- **4 scenarios**: Data Science, Product Management, Banking Operations, Heavy Industry Strategy
- **91 tasks** across multiple weeks per scenario
- **Thousands of input files** — realistic professional deliverables
- Agents complete tasks in independent runs (no carryover of prior submissions between tasks)

## Grading Dimensions

Each task is graded across three dimensions:

| Dimension | Method | Description |
|-----------|--------|-------------|
| **Rubric** | Binary pass/fail | Did the agent follow instructions, identify hidden requirements, use correct evidence? |
| **Analytical Quality** | Pairwise comparison | Which submission is more thorough, analytically rigorous, and well-supported? |
| **Presentation Quality** | Pairwise comparison | Which submission is more professionally presented? |

The combined **AA-Briefcase Elo** aggregates rubric pass rate, analytical quality Elo, and presentation Elo into a single metric.

## Key Findings (via Ethan Mollick)

Ethan Mollick graphed the frontier curve from AA-Briefcase scores and reported:
1. **Rapid frontier gains** — models are improving quickly on complex knowledge work
2. **Open-weights gap** — clear performance gap between open-weight and closed frontier models

## Public Scenario

A fifth demonstrative scenario is available on HuggingFace as `ArtificialAnalysis/AA-Briefcase-Lite`, illustrating structure, submission format, and grading without counting toward official results.

## Related
- [[concepts/agent-evaluation]] — Agent evaluation methodologies
- [[concepts/evals]] — AI model evaluation
- [[concepts/benchmark]] — Benchmarking in AI
- [[entities/artificial-analysis]] — Artificial Analysis platform
