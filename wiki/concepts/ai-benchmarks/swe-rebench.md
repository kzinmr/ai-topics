---
title: "SWE-rebench"
type: concept
created: 2026-06-26
updated: 2026-06-26
tags:
  - benchmark
  - evaluation
  - coding-agents
  - software-engineering
sources:
  - title: "SWE-rebench: A Refreshed SWE-bench with Improved Task Quality and Reduced Contamination"
    arxiv: "2505.20411"
    year: 2025
related_concepts:
  - concepts/ai-benchmarks/swe-bench
  - concepts/ai-benchmarks/swe-gym
  - concepts/ai-benchmarks/swe-bench-pro
  - concepts/evaluation/ai-benchmarks-and-evals
---

# SWE-rebench

SWE-rebench is a **refreshed version of [[concepts/ai-benchmarks/swe-bench|SWE-bench]]** designed to address known issues with the original benchmark, including data contamination, task quality inconsistencies, and evaluation reliability.

## What It Measures

SWE-rebench measures the same core capability as SWE-bench — an agent's ability to resolve real software issues — but with improved rigor:

- **Issue resolution accuracy** on carefully curated, high-quality tasks
- **Reduced contamination** — tasks are selected to minimize the chance agents have seen them during pretraining
- **Consistent task quality** — filtering out problematic or ambiguous tasks from the original SWE-bench
- **Reliable evaluation** — improved test suites and evaluation criteria

## Data/Methodology

- **Source**: Derived from [[concepts/ai-benchmarks/swe-bench|SWE-bench]] task pool with systematic quality improvements
- **Curation process**: Manual and automated filtering to remove contaminated, poorly specified, or incorrectly evaluated tasks
- **Quality improvements**: Better issue descriptions, improved test coverage, and more reliable ground-truth patches
- **Contamination mitigation**: Temporal filtering and careful task selection to reduce training data leakage
- **Evaluation**: Standard SWE-bench evaluation protocol — apply patch and run tests

## Key Results

- SWE-rebench provides a more reliable and interpretable evaluation signal than vanilla SWE-bench
- Leaderboard rankings may shift relative to SWE-bench due to reduced contamination effects
- Benchmark reveals that some apparent model improvements on SWE-bench may be partially attributable to contamination
- Maintains sufficient scale for statistically meaningful evaluation

## Related Benchmarks

| Benchmark | Relationship |
|-----------|-------------|
| [[concepts/ai-benchmarks/swe-bench\|SWE-bench]] | SWE-rebench is a direct refresh and improvement of SWE-bench |
| [[concepts/ai-benchmarks/swe-gym\|SWE-Gym]] | Complementary — SWE-Gym provides training while SWE-rebench improves evaluation |
| [[concepts/ai-benchmarks/swe-bench-pro\|SWE-bench Pro]] | Both aim to improve upon vanilla SWE-bench's limitations |
| [[concepts/ai-benchmarks/multi-swe-bench\|Multi-SWE-bench]] | Both extend and improve the SWE-bench paradigm |

## Connections to Other Wiki Concepts

- **[[concepts/ai-benchmarks/swe-bench]]**: SWE-rebench directly addresses contamination and quality issues in the original SWE-bench, which has become the de facto standard for SWE agent evaluation
- **[[concepts/evaluation/ai-benchmarks-and-evals]]**: Highlights the importance of benchmark integrity — contamination is a growing concern across all AI benchmarks
- **[[concepts/ai-benchmarks/deepswe-benchmark]]**: Both represent efforts to create more rigorous SWE evaluation beyond vanilla SWE-bench
- **[[concepts/ai-benchmarks/frontier-swe-benchmark]]**: SWE-rebench's focus on task quality complements Frontier SWE Benchmark's focus on difficulty
