---
title: "Senior SWE-Bench"
type: concept
created: 2026-07-05
updated: 2026-07-05
tags:
  - benchmark
  - coding-agents
  - ai-coding
  - code-quality
  - evaluation
  - anthropic
  - model
sources:
  - raw/articles/2026-07-02_snorkel_senior-swe-bench.md
  - https://senior-swe-bench.snorkel.ai/
---

# Senior SWE-Bench

**Senior SWE-Bench** is a coding benchmark created by [[entities/anthropic|Snorkel AI]] designed to evaluate coding agents at the level of **senior engineers**, not junior engineers. It moves beyond simple pass/fail on over-specified requirements and instead evaluates whether agents can handle the ambiguity, investigation, and quality standards expected of senior developers. The benchmark reveals a massive gap: even the top-performing model, [[entities/anthropic|Anthropic]]'s Claude Opus 4.8, achieves only a **24.0% tasteful solve rate**.

## Overview

Unlike existing coding benchmarks such as [[concepts/ai-benchmarks/swe-bench]] and [[concepts/ai-benchmarks/swe-bench-pro]], which focus primarily on whether an agent can produce a functionally correct patch, Senior SWE-Bench raises the bar by demanding **senior-level judgment**: the ability to interpret ambiguous instructions, investigate runtime behavior, and produce solutions that are not merely correct but well-crafted.

The benchmark is part of a broader trend in [[concepts/evaluation/ai-benchmarks-and-evals|AI benchmarking]] toward evaluating [[concepts/coding-agents/coding-agents|coding agents]] on dimensions beyond raw correctness — recognizing that real-world [[concepts/coding-agents/ai-coding-reliability|AI-assisted coding]] requires taste, maintainability, and investigative skill.

## Three Key Innovations

### 1. Realistic, Under-Specified Feature Tasks

Instructions are written as natural language messages rather than over-specified requirements, mimicking how a human manager might delegate to a senior engineer. The median instruction length is only **31%** that of SWE-Bench Pro (466 characters vs ~1,500 characters). 

To reliably evaluate such open-ended tasks, Senior SWE-Bench introduces a **validation agent** that writes behavioral tests adapting to each submitted solution, enabling automated assessment without requiring the task specification to predetermine every detail of the implementation.

### 2. Bug Tasks Requiring Runtime Investigation

Bug tasks are sourced from real-world pull requests that needed significant runtime investigation — including log analysis, profiling, and reproduction steps. These are not simple unit-test-fix bugs where the failure mode is trivially surfaced by an existing test suite. Agents must actively investigate the runtime behavior of the codebase to diagnose and resolve issues.

### 3. "Taste" Scoring

A solution is scored not just on correctness but on **taste** — the quality and craft of the implementation. A **tasteful solve** requires all of the following criteria:

| Criterion | Requirement |
|-----------|-------------|
| Verifiers pass | All automated tests pass |
| Validation pass | Behavioral validation agent approves |
| Rubric | Score > 0.5 on quality rubric |
| Bloat | Less than 2× the lines of the reference solution |
| Practice | Score > 2/5 on following codebase conventions |
| Relative taste | Score > 2/5 on overall craftsmanship |

This multi-dimensional scoring reflects the real-world expectation that senior engineers don't just solve problems — they solve them well.

## Task Composition

- **100 tasks**: 50 public, 50 private (preventing benchmark contamination)
- **Repositories**: PostHog (8), Electric (6), Gitea (6), Better-Auth (4), Harbor (4), plus 7+ more
- **Task types**: feature, bug, performance, migration
- **Technology stacks**: Python service, Elixir, Go, SQL, TypeScript library, Python library, Rust, TypeScript frontend, plus 4+ more
- **Average files touched per feature task**: 11 (compared to 5–7 for SWE-Bench Pro)
- **Task horizon**: Hundreds of steps even for the strongest agents

## Leaderboard

Tasteful solve rate (pass@1) as of July 2026:

| Rank | Model | Effort | Solve Rate |
|------|-------|--------|:----------:|
| 1 | Claude Opus 4.8 | max | 24.0% |
| — | Claude Sonnet 5 | max | 19.4% |
| 2 | GPT-5.5 | xhigh | 16.0% |
| 3 | Claude Opus 4.7 | max | 14.1% |
| 4 | GPT-5.4 | xhigh | 14.0% |
| 5 | GLM-5.2 | max | 12.5% |
| 6 | Kimi K2.6 | default | 8.2% |
| 7 | Claude Sonnet 4.6 | high | 8.2% |
| 8 | Gemini 3.1 Pro | high | 6.1% |
| 9 | Gemini 3.5 Flash | medium | 3.0% |

## Implications

The 24.0% ceiling on tasteful solves signals a substantial gap between current AI coding agents and true senior-engineer-level performance. Key takeaways:

- **Correctness ≠ seniority**: Getting the code to pass tests is far easier than producing maintainable, well-crafted solutions that follow codebase conventions. The gap between raw pass rate and tasteful solve rate is where most models lose points.

- **Ambiguity is the bottleneck**: Under-specified instructions are the norm in real software engineering. Models that excel on precisely defined SWE-bench tasks struggle when they must interpret intent from terse natural language messages.

- **Runtime debugging remains hard**: Bug tasks requiring log analysis, profiling, and reproduction steps expose a weakness in current agents, which are typically optimized for static code analysis rather than dynamic investigation.

- **Benchmark design is evolving**: Senior SWE-Bench represents a shift in [[concepts/evaluation/ai-benchmarks-and-evals|benchmark]] design philosophy — from "can the agent pass the tests?" to "would a senior engineer approve this solution?" This aligns with the broader trajectory of coding benchmarks toward more holistic evaluation of [[concepts/coding-agents/coding-agents|coding agent]] capability.

## Related Pages

- [[concepts/ai-benchmarks/swe-bench]] — The original SWE-bench and SWE-bench Verified
- [[concepts/ai-benchmarks/swe-bench-pro]] — Professional-grade SWE evaluation by Scale AI
- [[concepts/ai-benchmarks/deepswe-benchmark]] — DeepSWE benchmark critiquing SWE-Bench Pro evaluation
- [[concepts/ai-benchmarks/frontier-swe-benchmark]] — Frontier SWE capability evaluation
- [[concepts/coding-agents/coding-agents]] — Coding agent landscape overview

## Sources

- [Senior SWE-Bench Official Website](https://senior-swe-bench.snorkel.ai/) — Snorkel AI (July 2026)
- Raw article: `raw/articles/2026-07-02_snorkel_senior-swe-bench.md`
