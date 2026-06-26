---
title: "CORE-Bench"
type: concept
created: 2026-06-26
updated: 2026-06-26
tags: [benchmark, evaluation, ai-agents, ai-research]
sources:
  - title: "CORE-Bench: Fostering the Credibility of Published Research Through a Computational Reproducibility Agent Benchmark"
    arxiv: "2409.11363"
    year: 2024
related_concepts:
  - "[[paperbench]]"
  - "[[scienceagentbench]]"
  - "[[re-bench]]"
  - "[[gaia-benchmark]]"
---

# CORE-Bench

CORE-Bench (Computational Reproducibility Agent Benchmark) evaluates AI agents on their ability to reproduce computational results from published research papers. The benchmark addresses a fundamental challenge in modern science — the reproducibility crisis — by testing whether AI agents can verify that published computational claims are reproducible.

## What It Measures

CORE-Bench assesses an agent's ability to:

- **Reproduce computational results**: Execute code and workflows described in papers to verify that reported results can be obtained
- **Navigate research artifacts**: Understand and work with code repositories, datasets, and computational environments associated with published papers
- **Resolve dependency and environment issues**: Handle missing dependencies, version conflicts, and environment setup challenges common in research code
- **Verify claims against results**: Compare reproduced outputs against values reported in the paper to assess reproducibility
- **Report reproducibility status**: Produce clear assessments of whether and to what extent results are reproducible

The benchmark is designed around the practical challenges that make computational reproducibility difficult even for human researchers.

## Data/Methodology

CORE-Bench is built from real research papers and their associated computational artifacts:

- **Paper-repository pairs**: Each task includes a published paper and its associated code repository, providing all materials needed for reproduction
- **Multi-domain coverage**: Tasks span multiple scientific disciplines, testing generalizable reproduction skills
- **Tiered difficulty**: Tasks range from papers with well-structured, documented code to papers with minimal documentation and complex dependency chains
- **Binary and graded evaluation**: Some tasks have clear pass/fail reproducibility criteria; others allow for partial reproduction with graded scoring
- **Environment management**: Agents must navigate real challenges like setting up Docker containers, installing specific package versions, and handling deprecated dependencies
- **Automated verification**: Reproduced outputs are automatically compared against reference values to determine reproducibility

## Key Results

- Current agents achieve moderate success rates on well-documented papers with clean codebases, but performance drops sharply on papers with complex or poorly documented code
- Environment setup and dependency management remain the primary failure modes — many agents fail before even beginning the actual reproduction
- Agents perform better on papers from fields with standardized computational tooling (e.g., Python-based ML papers) compared to those using less common languages or tools
- The time and compute required for reproduction varies enormously across tasks, highlighting the heterogeneous nature of computational reproducibility
- Agent performance improves significantly with access to better tooling for environment management and dependency resolution

## Related Benchmarks

- **[[paperbench]]**: Tests reproduction from paper descriptions alone (building code from scratch); CORE-Bench tests reproduction from existing code repositories
- **[[scienceagentbench]]**: Covers broader scientific analysis tasks; CORE-Bench focuses specifically on verifying published results
- **[[re-bench]]**: Evaluates research capabilities in ML specifically; CORE-Bench spans multiple scientific domains
- **[[gaia-benchmark]]**: Tests general assistant capabilities including some reproducibility-adjacent tasks

## Connections to Other Wiki Concepts

CORE-Bench directly addresses the [[replication-crisis]] and [[research-reproducibility]] challenges in modern science. The benchmark connects to discussions of [[open-science]] and [[research-integrity]], as automated reproducibility checking could become a standard part of the publication process. It also relates to [[ci-cd-for-science]] — the idea that computational experiments should be continuously verified. CORE-Bench has implications for [[peer-review]] processes, where AI agents could serve as automated reproducibility reviewers, and connects to broader discussions of [[trustworthy-ai]] in scientific applications.
