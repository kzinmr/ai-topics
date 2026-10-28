---
title: "ProgramBench"
created: 2026-05-06
updated: 2026-10-27
type: concept
tags:
  - concept
  - benchmark
  - evaluation
  - coding-agents
  - methodology
aliases:
  - "ProgramBench (Meta)"
related:
  - "concepts/ai-benchmarks/swe-bench]]"
  - "concepts/coding-benchmarks]]"
  - "entities/meta]]"
sources:
  - raw/newsletters/2026-05-06-ainews-silicon-valley-gets-serious-about-services.md
  - https://open.substack.com/pub/swyx/p/ainews-silicon-valley-gets-serious
  - raw/articles/2026-10-26_import-ai-478_math-for-alignment-programbench-mirendil.md
  - https://importai.substack.com/p/import-ai-478-math-for-alignment
  - https://arxiv.org/abs/2605.03546
---


# ProgramBench

**ProgramBench** is a benchmark released by **Meta** (May 2026) that evaluates AI models on **full-repository software generation from scratch** — building real-world software like SQLite and FFmpeg without internet access. It represents the hardest frontier for LLM code generation, with a current top accuracy of **0%** (though models pass >50% of individual subtasks).

> ⚠️ **Stale figure — see [Score Progression](#score-progression-0-to-185-october-2026) below.** The 0% figure above reflects the May 2026 release state. By October 2026 **Claude Opus 5.5 (xhigh)** reaches **18.5% resolved / 70.5% almost**.

## Task Definition

ProgramBench tests how well AI systems can **rebuild software programs from a compiled binary plus its documentation** (no source code, no internet). Per the paper's framing, the 200 tasks cover:

| Category | Examples |
|----------|----------|
| **Language interpreters** | PHP, Lua, tinycc |
| **Databases** | DuckDB, SQLite |
| **Media & compression utilities** | FFmpeg, zstd, xz |
| **Developer tools** | ripgrep, fzf, jq |

Two scoring metrics are used, both over the 200-task set:
- **resolved** — fraction of tasks where *all* tests pass
- **almost** — fraction of tasks where **>95%** of tests pass

## Score Progression: 0% → 18.5% (October 2026)

The benchmark is the clearest single illustration of the 2026 coding-agent rate of improvement: a benchmark where *every* model scored 0% at release was cracked to near-majority partial success in about five months.

| Model | resolved | almost | When |
|-------|---------:|-------:|------|
| **Claude Opus 4.7** (best at release) | **0%** | 3% | May 2026 release |
| *(all other tested models at release)* | 0% | — | May 2026 |
| **Claude Opus 5.5 (xhigh)** | **18.5%** | **70.5%** | October 2026 |

Jack Clark's framing in **Import AI 478** (Oct 26, 2026): *"In a reminder of the blistering pace of AI progress, Claude Opus 5.5 (xhigh) has got a score of 18.5% on ProgramBench, a very hard benchmark that came out in May of this year — and when it came out, every tested model scored 0%."*

### Clark's saturation prediction

Clark makes an explicit, falsifiable forecast: **he expects ProgramBench to be saturated by the end of 2027** — defining "saturated" as "some very high score on resolved." He attaches the standard benchmark caveat himself: *"as with most benchmarks it's likely there's some kind of noise ceiling here, so it might not strictly be 100%."*

His argument for why the benchmark matters is not the absolute score but the **slope**: *"In 2027, huge amounts of software will be built via AI systems end-to-end autonomously developing whatever they need to do for whatever tasks they're being put to. Evals like ProgramBench give us a sense of how rapid the pace of progress is here, given we went from 0% earlier this year to 20% now."* He labels the underlying trend **"the era of ephemeral software"** — software generated on demand for a single task rather than maintained as a durable artifact.

### Interpretive caution

The `resolved` vs `almost` gap is the important nuance. **18.5% resolved / 70.5% almost** means the dominant failure mode is no longer "cannot build the system" but "builds a system that fails a small tail of tests." Whether the remaining ~81% resolved gap reflects genuine architectural insufficiency or test-suite brittleness / noise ceiling is unresolved — Clark flags the latter possibility without quantifying it. The May 2026 "The Whole-Repo Gap" thesis below should be read as **partially superseded**: greenfield whole-repo development is no longer categorically unsolved, only unreliable.

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
| **ProgramBench** | Full-repo from scratch | **0%** (May 2026) → **18.5%** (Oct 2026, Claude Opus 5.5 xhigh) | Extreme |

### Industry Context

ProgramBench arrives alongside:
- **Cursor CI-fix agents** — automatically fixing CI failures in existing repos (higher success rate because the repo structure already exists)
- **Devin for Security** — automated vulnerability remediation with pre-existing codebase
- **Harness quality debate** — experts arguing Model–Harness–Task fit matters more than raw benchmarks

The 0% accuracy suggests that while AI can assist developers within established projects, **autonomous greenfield software development** remains unsolved.

> **Update (Oct 2026):** This conclusion is now **partially superseded** — see [Score Progression](#score-progression-0-to-185-october-2026). At 18.5% resolved / 70.5% almost, greenfield whole-repo development is no longer categorically unsolved; the bottleneck has shifted from architecture to a residual tail of failing tests.

## Related Concepts

- [[concepts/ai-benchmarks/swe-bench]] — Standard benchmark for bug-fixing in existing codebases
- [[concepts/coding-benchmarks]] — Overview of LLM coding evaluation
- [[entities/meta]] — Publisher of ProgramBench
- [[entities/cursor-ai]] — Cursor CI-fix agents (complementary capability)

## Sources

- [AINews: Silicon Valley gets Serious about Services](https://open.substack.com/pub/swyx/p/ainews-silicon-valley-gets-serious) — May 6, 2026
- [ProgramBench: Can Language Models Rebuild Programs From Scratch?](https://arxiv.org/abs/2605.03546) — arXiv 2605.03546 (original paper)
- [Import AI 478: Math for alignment; ProgramBench; and Mirendil shows what RSI means](https://importai.substack.com/p/import-ai-478-math-for-alignment) — Jack Clark, Oct 26, 2026 (source of the 18.5%/70.5% scores, task taxonomy, and the 2027 saturation prediction)
