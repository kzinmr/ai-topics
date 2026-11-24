---
title: "SciResearch-Eval"
created: 2026-11-24
updated: 2026-11-24
type: concept
tags:
  - benchmark
  - evaluation
  - ai-in-science
  - llm-evaluation
  - agent-evaluation
sources:
  - raw/newsletters/2026-11-23-import-ai-482-huawei-kernel-benchmarks-airborne-drone-detection-and-a-national-l.md
  - https://btwestyo.github.io/sciresearch-eval/
---

# SciResearch-Eval

**SciResearch-Eval** is a benchmark from **Lawrence Livermore National Laboratory** (LLNL) that tests how reliably AI agents can give **calibrated uncertainty estimates** for physical quantities — reported as confidence intervals against strict ground truth. Covered in Import AI 482 (Jack Clark, Nov 23 2026). The authors frame it as the first benchmark combining all three of: **agent-designed experiments**, a **deliberately flawed simulator**, and **calibrated-interval grading** against strict ground truth.

## Motivation

> "An agent that reports a confident wrong number is worse than one that reports honest uncertainty, because nobody downstream can tell the difference." — LLNL researchers

## Task Design

1. The **agent designs its own experiments** (no fixed experimental protocol).
2. The agent is given a simulator that is **intentionally incomplete or physically wrong** — a plausible-looking physics surrogate with hidden defects.
3. The agent fits a **heat conduction model** and must report material property values with **95% confidence intervals**.
4. Grading is done against strict ground truth, scoring **calibration** of the intervals, not just point accuracy.

## Key Results (as reported in Import AI 482)

- In the setting where the simulator lacks real physics, only **GPT-6 Astra** and **Claude Fable 5.2** report trustworthy intervals by default.
- **Claude 5.5-family** models recover only at their **highest reasoning settings**.
- Older models and **open-weight models fail entirely** on calibration.

## Significance

Jack Clark positions SciResearch-Eval within the AI-driven-science wave: national labs are building evaluation infrastructure for agents doing real scientific work, where **calibrated uncertainty is a deployment requirement**, not an academic nicety — a physically confident wrong number propagates into engineering decisions.

## Related

- [[concepts/ai-mathematics-theorem-proving]] — the broader 2026 AI-for-science results wave
- [[concepts/autoscientist]] — automated scientific experimentation
- [[concepts/open-science]] — open science infrastructure
- [[concepts/ai-benchmarks]] — benchmark hub

## Sources

- Import AI 482 (Jack Clark, Nov 23 2026): `raw/newsletters/2026-11-23-import-ai-482-huawei-kernel-benchmarks-airborne-drone-detection-and-a-national-l.md`
- Project page: [btwestyo.github.io/sciresearch-eval](https://btwestyo.github.io/sciresearch-eval/)
