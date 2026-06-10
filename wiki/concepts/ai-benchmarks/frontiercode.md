---
title: "FrontierCode"
type: concept
created: 2026-06-09
updated: 2026-06-09
tags:
  - concept
  - benchmark
  - coding-agents
  - code-quality
  - evaluation
  - software-engineering
sources:
  - https://www.latent.space/p/ainews-frontiercode-benchmarking
  - https://twitter.com/cognition
  - raw/newsletters/2026-06-09-ainews-frontiercode-benchmarking-for-code-quality-over-slop.md
related:
  - concepts/ai-code-quality
  - concepts/ai-benchmarks/swe-bench
  - concepts/ai-benchmarks/frontier-swe-benchmark
  - concepts/ai-benchmarks/deepswe-benchmark
  - concepts/ai-benchmarks/agent-arena
  - concepts/metr-swe-bench-analysis
---

# FrontierCode

**FrontierCode** is a coding evaluation benchmark introduced by **Cognition** (creators of Devin) in June 2026. Unlike prior benchmarks that measure whether agents can pass tests, FrontierCode explicitly measures **whether generated code would actually be merged into a production codebase**.

## Core Innovation

The benchmark shifts evaluation from "does the code work?" to **"would you merge this code?"** — a fundamentally harder standard that captures code quality, maintainability, and regression safety.

### Task Construction

- Each task required **40+ hours of work by leading open-source maintainers** to create
- Evaluation dimensions include: **regression safety, cleanliness, scope, test correctness, and maintainability**
- Inspired by **FrontierMath** (hardest-tier problems for frontier models), FrontierCode focuses on extremely difficult coding tasks

### Headline Results

| Model | Success Rate | Notes |
|-------|-------------|-------|
| **Opus 4.8** | ~13% (hardest subset) | Best performing model, but far below 50%+ regime of SWE-Bench-style evals |
| Claude 3.5 Sonnet | <2% | With extended thinking (10K tokens), Python access, and experimentation |
| GPT-4o | <2% | Same conditions |
| Gemini 1.5 Pro | <2% | Same conditions |

The headline finding: even the best model scores only ~13% on the hardest subset — dramatically lower than the 50%+ scores common on SWE-Bench-style evaluations. This suggests **coding is much less "solved" than popular benchmarks imply**.

## Connection to the SWE-Bench Critique

FrontierCode directly addresses the problem identified in METR's analysis: **"Many SWE-bench-Passing PRs Would Not Be Merged into Main."** The false positive trajectories (not quite reward hacks, but spiritually similar — exploiting benchmark unreliability rather than model capability) measured in the FrontierCode report validate concerns that SWE-Bench-style evaluations have been systematically overstating agent coding ability.

### SWE-Bench Pro Limitations Exposed

The AINews commentary notes that even after the switch to SWE-Bench Pro, there was **"insufficient articulation around WTF Happened in 2025"** — the rapid capability gains shown on benchmarks didn't translate to genuinely mergeable code. FrontierCode was designed to close this gap.

## Broader Context: Benchmarks as Training Pipelines

Ofir Press (Princeton, SWE-Bench co-author) argued that the best benchmarks are **scalable and rooted in real-world crawled data sources**, making them useful for both measurement and data generation. FrontierCode exemplifies this principle:
1. Tasks sourced from real open-source maintainer workflows
2. Evaluation criteria derived from actual merge decisions
3. Results feed back into training pipelines (Cognition uses FrontierCode to improve Devin)

This contrasts with earlier benchmarks where the evaluation was static and disconnected from training loops.

## Relationship to Other Coding Benchmarks

| Benchmark | Focus | Key Differentiator |
|-----------|-------|-------------------|
| **SWE-Bench** | Issue resolution via test passing | First agentic coding benchmark |
| **SWE-Bench Pro** | Harder tasks, verified correctness | Addressed contamination |
| **FrontierSWE** | 20-hour limit, ultra-difficult | Time-bounded performance |
| **DeepSWE** | 113 tasks, 91 repos, 5 languages | Exposed 32% verifier error rate |
| **FrontierCode** | **Mergeability** | "Would you merge this?" criterion |
| **Agent Arena** | Real-world causal tracing | 1M+ sessions, treatment effects |

## Significance

FrontierCode represents a maturation of coding agent evaluation:
1. **Quality > Quantity**: Moving from "how many issues can you close?" to "how good is the code you produce?"
2. **Production-readiness focus**: Code that passes tests but isn't maintainable is still slop
3. **Harder problems**: 40+ hour maintainer tasks vs. typical 1-2 hour GitHub issues
4. **Realistic performance gap**: The dramatic drop from 50%+ (SWE-Bench) to 13% (FrontierCode hardest) reveals how much capability gap remains

## Related Concepts

- [[concepts/ai-code-quality]] — The broader "quality vs slop" debate in AI coding
- [[concepts/ai-benchmarks/swe-bench]] — The benchmark FrontierCode builds upon and critiques
- [[concepts/ai-benchmarks/frontier-swe-benchmark]] — Another "hardest tasks" benchmark for coding agents
- [[concepts/ai-benchmarks/deepswe-benchmark]] — Datacurve's benchmark exposing SWE-Bench Pro verifier errors
- [[concepts/ai-benchmarks/agent-arena]] — Arena AI's causal evaluation methodology
- [[concepts/ai-evals]] — Broader evaluation landscape

## Sources

- [AINews: FrontierCode coverage](https://www.latent.space/p/ainews-frontiercode-benchmarking) (swyx, June 9, 2026)
- [Cognition announcement](https://twitter.com/cognition) (June 8, 2026)
- [METR: Many SWE-bench-Passing PRs Would Not Be Merged](https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/)
