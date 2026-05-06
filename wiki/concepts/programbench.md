---
title: "ProgramBench"
created: 2026-05-06
updated: 2026-05-06
type: concept
tags:
  - concept
  - benchmark
  - evaluation
  - coding-agents
  - meta
aliases:
  - "ProgramBench (Meta)"
related:
  - [[concepts/swe-bench]]
  - [[concepts/coding-benchmarks]]
  - [[entities/meta]]
sources:
  - raw/newsletters/2026-05-06-ainews-silicon-valley-gets-serious-about-services.md
  - https://open.substack.com/pub/swyx/p/ainews-silicon-valley-gets-serious
---

# ProgramBench

**ProgramBench** is a benchmark released by **Meta** (May 2026) that evaluates AI models on **full-repository software generation from scratch** — building real-world software like SQLite and FFmpeg without internet access. It represents the hardest frontier for LLM code generation, with a current top accuracy of **0%** (though models pass >50% of individual subtasks).

## Summary

Unlike existing coding benchmarks (HumanEval, SWE-bench, Terminal-Bench) that test isolated function writing, bug fixing, or single-file generation, ProgramBench requires models to architect and implement **complete software systems** from specifications alone. The benchmark includes ~200 tasks spanning database engines, media codecs, and other real-world software.

## Key Results

| Metric | Value |
|--------|-------|
| **Tasks** | ~200 full-repo generation tasks |
| **Top Accuracy** | 0% (no model successfully builds a complete system) |
| **Partial Progress** | Models pass >50% of individual tests per task |
| **Scope** | SQLite, FFmpeg, and similar real-world software |

## Significance

### What This Reveals

1. **The "Whole-Repo Gap"**: Current models can write functions and fix bugs, but cannot architect a complete software system from scratch
2. **Specification-to-Implementation**: The hardest part is not code generation but translating high-level requirements into a coherent architecture
3. **Integration Complexity**: Real software has interacting components, edge cases, and design tradeoffs that benchmark-style tasks don't capture

### Comparison to Other Benchmarks

| Benchmark | Scope | Top Score | Difficulty |
|-----------|-------|-----------|------------|
| **HumanEval** | Single function | ~95% (GPT-5) | Low |
| **SWE-bench Verified** | Bug fixes in existing repos | ~72% (Claude 4.5) | Medium |
| **Terminal-Bench 2.0** | Multi-step system tasks | ~82.7% (GPT-5.5) | High |
| **ProgramBench** | Full-repo from scratch | **0%** | Extreme |

### Industry Context

ProgramBench arrives alongside:
- **Cursor CI-fix agents** — automatically fixing CI failures in existing repos (higher success rate because the repo structure already exists)
- **Devin for Security** — automated vulnerability remediation with pre-existing codebase
- **Harness quality debate** — experts arguing Model–Harness–Task fit matters more than raw benchmarks

The 0% accuracy suggests that while AI can assist developers within established projects, **autonomous greenfield software development** remains unsolved.

## Related Concepts

- [[concepts/swe-bench]] — Standard benchmark for bug-fixing in existing codebases
- [[concepts/coding-benchmarks]] — Overview of LLM coding evaluation
- [[entities/meta]] — Publisher of ProgramBench
- [[entities/cursor-ai]] — Cursor CI-fix agents (complementary capability)

## Sources

- [AINews: Silicon Valley gets Serious about Services](https://open.substack.com/pub/swyx/p/ainews-silicon-valley-gets-serious) — May 6, 2026
