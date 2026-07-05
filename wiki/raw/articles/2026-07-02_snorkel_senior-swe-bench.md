---
title: "Senior SWE-Bench"
url: "https://senior-swe-bench.snorkel.ai/"
date: 2026-07-02
date_ingested: 2026-07-05
source: "snorkel-ai"
type: article
authors: ["Snorkel AI"]
tags: [article, raw, benchmark, coding-agents, ai-coding, code-quality, evaluation]
---

# Senior SWE-Bench

Source: https://senior-swe-bench.snorkel.ai/

## Overview

Senior SWE-Bench is a benchmark created by Snorkel AI designed to evaluate coding agents like senior engineers, not junior engineers. It moves beyond simple pass/fail on over-specified requirements and instead evaluates whether agents can handle the ambiguity, investigation, and quality standards expected of senior developers.

## Three Key Differences from SWE-bench

1. **Realistic, under-specified feature tasks**: Instructions read like natural language messages rather than over-specified requirements. The median instruction length is only 31% that of SWE-Bench Pro (466 chars vs ~1,500 chars). To reliably evaluate these, they introduce a validation agent that writes behavioral tests adapting to submitted solutions.

2. **Bug tasks requiring runtime investigation**: Bug tasks are sourced from PRs that needed significant runtime investigation (logs, profiling, reproduction steps), not simple unit-test-fix bugs.

3. **"Taste" scoring**: Solutions must not only be correct but also demonstrate good taste. A "tasteful solve" requires: Verifiers pass, Validation pass, Rubric > 0.5, Bloat < 2× reference solution, Practice > 2/5 (follows codebase practices), Relative taste > 2/5.

## Task Composition

- **100 tasks**: 50 public, 50 private
- **Repos**: PostHog (8), Electric (6), Gitea (6), Better-Auth (4), Harbor (4), +7 more
- **Types**: feature, bug, performance, migration
- **Stacks**: Python service, Elixir, Go, SQL, TypeScript library, Python library, Rust, TypeScript frontend, +4 more
- **Avg files touched per feature task**: 11 (vs 5-7 for SWE-Bench Pro)
- **Task horizon**: Hundreds of steps even for the strongest agents

## Leaderboard — Tasteful Solve Rate (pass@1)

| Rank | Model | Effort | Solve Rate |
|------|-------|--------|------------|
| 1 | Claude Opus 4.8 | max | 24.0% |
| - | Claude Sonnet 5 | max | 19.4% |
| 2 | GPT-5.5 | xhigh | 16.0% |
| 3 | Claude Opus 4.7 | max | 14.1% |
| 4 | GPT-5.4 | xhigh | 14.0% |
| 5 | GLM-5.2 | max | 12.5% |
| 6 | Kimi K2.6 | default | 8.2% |
| 7 | Claude Sonnet 4.6 | high | 8.2% |
| 8 | Gemini 3.1 Pro | high | 6.1% |
| 9 | Gemini 3.5 Flash | medium | 3.0% |

## Key Takeaway

The top-performing frontier models fail to complete tasks with senior-level correctness and taste over 75% of the time. Even Claude Opus 4.8, the #1 model, only achieves a 24.0% tasteful solve rate. This benchmark reveals a massive gap between current AI coding agents and true senior-engineer-level performance.
