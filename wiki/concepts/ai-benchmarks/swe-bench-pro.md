---
title: "SWE-bench Pro"
type: concept
created: 2026-06-26
updated: 2026-06-26
tags:
  - benchmark
  - evaluation
  - coding-agents
  - software-engineering
sources:
  - title: "SWE-bench Pro: Professional-Grade Software Engineering Evaluation"
    arxiv: "2509.16941"
    year: 2025
related_concepts:
  - concepts/ai-benchmarks/swe-bench
  - concepts/ai-benchmarks/swe-rebench
  - concepts/ai-benchmarks/frontier-swe-benchmark
  - concepts/evaluation/ai-benchmarks-and-evals
---

# SWE-bench Pro

SWE-bench Pro is a **professional-grade evaluation benchmark** for AI coding agents, featuring harder and more realistic software engineering tasks than the original [[concepts/ai-benchmarks/swe-bench|SWE-bench]]. It targets the gap between current benchmark performance and real-world professional SWE capability.

## What It Measures

SWE-bench Pro measures an agent's ability to:

- **Resolve complex, professional-level software issues** that require deep codebase understanding
- **Handle multi-file changes** and architectural decisions
- **Perform at the level expected of professional software engineers**
- **Navigate large, complex codebases** with realistic project structures

The benchmark specifically targets tasks that are harder than typical SWE-bench instances.

## Data/Methodology

- **Source**: Curated from professional open-source projects with higher complexity standards
- **Task difficulty**: Significantly harder than vanilla SWE-bench — requiring deeper reasoning and broader codebase understanding
- **Scope**: Multi-file patches, architectural understanding, and complex dependency chains
- **Evaluation**: Automated test-based verification with comprehensive test suites
- **Quality control**: Professional-grade task specifications with clear success criteria

## Key Results

- Performance on SWE-bench Pro is substantially lower than on vanilla SWE-bench, indicating a meaningful difficulty gap
- Highlights that current agents struggle with professional-level software engineering complexity
- Provides a more realistic assessment of agent capabilities for production SWE tasks
- Reveals specific failure modes not visible in easier benchmarks (e.g., architectural reasoning failures)

## Related Benchmarks

| Benchmark | Relationship |
|-----------|-------------|
| [[concepts/ai-benchmarks/swe-bench\|SWE-bench]] | SWE-bench Pro is a harder, professional-grade extension |
| [[concepts/ai-benchmarks/swe-rebench\|SWE-rebench]] | Both improve upon vanilla SWE-bench — Pro for difficulty, rebench for quality |
| [[concepts/ai-benchmarks/frontier-swe-benchmark\|Frontier SWE Benchmark]] | Both target high-difficulty SWE evaluation |
| [[concepts/ai-benchmarks/swe-lancer\|SWE-Lancer]] | Both evaluate professional-grade SWE capability |

## Connections to Other Wiki Concepts

- **[[concepts/ai-benchmarks/swe-bench]]**: Extends SWE-bench's evaluation paradigm to professional difficulty levels, pushing beyond what current agents can reliably solve
- **[[concepts/evaluation/ai-benchmarks-and-evals]]**: Represents the trend toward harder benchmarks as agents improve on existing ones — the "benchmark saturation" cycle
- **[[concepts/ai-benchmarks/frontier-swe-benchmark]]**: SWE-bench Pro and Frontier SWE Benchmark both aim to keep evaluation ahead of agent capabilities
- **[[concepts/ai-benchmarks/deepswe-benchmark]]**: Both provide high-difficulty alternatives to vanilla SWE-bench for measuring cutting-edge agent performance
