---
title: "Multi-SWE-bench"
type: concept
created: 2026-06-26
updated: 2026-06-26
tags:
  - benchmark
  - evaluation
  - coding-agents
  - software-engineering
sources:
  - title: "Multi-SWE-bench: A Multilingual Software Engineering Benchmark"
    arxiv: "2504.02605"
    year: 2025
related_concepts:
  - concepts/ai-benchmarks/swe-bench
  - concepts/ai-benchmarks/aider-polyglot
  - concepts/ai-benchmarks/livecodebench
  - concepts/evaluation/ai-benchmarks-and-evals
---

# Multi-SWE-bench

Multi-SWE-bench extends the [[concepts/ai-benchmarks/swe-bench|SWE-bench]] paradigm **beyond Python** to cover multiple programming languages. It evaluates coding agents on real-world software engineering tasks across **Java, JavaScript, TypeScript, Go, Rust, and C++**.

## What It Measures

Multi-SWE-bench measures:

- **Cross-language SWE agent capability** — can agents resolve issues in languages beyond Python?
- **Language-specific challenges** — each language has unique build systems, type systems, and tooling
- **Generalization of SWE skills** — whether agents trained or optimized for Python transfer to other ecosystems
- **Polyglot software engineering** — real-world engineering often requires multi-language competence

## Data/Methodology

- **Languages**: Java, JavaScript, TypeScript, Go, Rust, C++ (in addition to Python baselines)
- **Source**: Real open-source repositories in each target language
- **Task format**: SWE-bench-compatible — issue descriptions with corresponding pull requests and test suites
- **Evaluation**: Automated test-based verification, adapted for each language's testing ecosystem
- **Scale**: Multi-language task collection covering diverse project sizes and domains
- **Infrastructure**: Language-specific build and test environments

## Key Results

- Agent performance varies significantly across programming languages
- Python-optimized agents do not necessarily transfer well to statically-typed languages (Java, Go, Rust, C++)
- Languages with complex build systems (Java, C++) present additional challenges beyond code generation
- TypeScript/JavaScript performance often falls between Python and systems languages
- Results suggest that language-specific training and tooling is important for SWE agent effectiveness

## Related Benchmarks

| Benchmark | Relationship |
|-----------|-------------|
| [[concepts/ai-benchmarks/swe-bench\|SWE-bench]] | Multi-SWE-bench extends SWE-bench to multiple languages |
| [[concepts/ai-benchmarks/aider-polyglot\|Aider Polyglot]] | Both evaluate multi-language coding capabilities |
| [[concepts/ai-benchmarks/livecodebench\|LiveCodeBench]] | Both provide diverse-language coding evaluation |
| [[concepts/ai-benchmarks/swe-rebench\|SWE-rebench]] | Both improve upon the SWE-bench foundation |

## Connections to Other Wiki Concepts

- **[[concepts/ai-benchmarks/swe-bench]]**: Multi-SWE-bench is a direct multilingual extension of SWE-bench, addressing its Python-only limitation
- **[[concepts/ai-benchmarks/aider-polyglot]]**: Both evaluate polyglot coding ability, but Multi-SWE-bench focuses on real-world SWE tasks while Aider Polyglot targets code editing
- **[[concepts/evaluation/ai-benchmarks-and-evals]]**: Highlights the need for language-diverse evaluation in an increasingly polyglot software ecosystem
- **[[concepts/ai-benchmarks/livecodebench]]**: Both recognize that coding agent evaluation should span multiple programming languages
