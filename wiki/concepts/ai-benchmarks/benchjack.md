---
title: "BenchJack"
type: concept
created: 2026-06-26
updated: 2026-06-26
tags:
  - benchmark
  - evaluation
  - safety
  - ai-agents
sources:
  - "arXiv:2605.12673"
  - "Dawn Song (UC Berkeley)"
related_concepts:
  - "[[benchmark-evaluation]]"
  - "[[ai-agents]]"
  - "[[evaluation-methodology]]"
  - "[[meta-evaluation]]"
---

# BenchJack

BenchJack is a framework by Dawn Song (UC Berkeley) for **systematically auditing AI agent benchmarks**. Published as arXiv:2605.12673, it provides a structured methodology for identifying flaws and improving the quality of benchmarks used to evaluate AI agents.

## What It Measures

BenchJack evaluates the quality and validity of agent benchmarks themselves:

- **Benchmark flaw identification**: Systematic detection of methodological weaknesses
- **Validity assessment**: Whether benchmarks measure what they claim to measure
- **Robustness**: Susceptibility to gaming and overfitting
- **Coverage gaps**: Missing scenarios or capabilities not captured by the benchmark

## Data/Methodology

BenchJack introduces a structured auditing framework:

- **8-pattern flaw taxonomy**: Eight categories of common benchmark design flaws
  - Includes issues like contamination, leakage, ambiguity, incompleteness, and gaming vulnerability
- **30-question checklist**: Systematic evaluation questions for benchmark auditing
- **Multi-benchmark application**: Framework applicable across diverse agent benchmarks
- **Reproducibility focus**: Emphasis on verifiable and reproducible audit results
- **Community tooling**: Designed for widespread adoption by the research community

## Key Results

- Many widely-used agent benchmarks contain identifiable design flaws
- The 8-pattern taxonomy captures the majority of common benchmark weaknesses
- Systematic auditing reveals issues invisible to ad-hoc evaluation
- Benchmark quality directly impacts the reliability of model comparisons

## Related Benchmarks

- [[agentdojo]] — Agent security benchmark subject to auditing
- [[agentharm]] — Agent harmfulness benchmark
- [[agent-security-bench]] — Comprehensive agent security evaluation
- [[decodingtrust]] — Trustworthiness benchmark

## Connections to Other Wiki Concepts

BenchJack represents **meta-evaluation** — evaluating the evaluators. As the number of **[[ai-agents]]** benchmarks grows rapidly, ensuring their quality becomes critical for reliable model assessment. The framework's **evaluation-methodology** contributions help the research community identify and address flaws in benchmarks like [[agentdojo]], [[agentharm]], and [[agent-security-bench]]. This meta-level quality assurance is essential for the broader **benchmark-evaluation** ecosystem to produce trustworthy and actionable results.
