---
title: "AscendGYM"
created: 2026-11-24
updated: 2026-11-24
type: concept
tags:
  - benchmark
  - evaluation
  - chip-design
  - us-china-ai-race
  - china
  - agentic-coding
sources:
  - raw/newsletters/2026-11-23-import-ai-482-huawei-kernel-benchmarks-airborne-drone-detection-and-a-national-l.md
  - https://arxiv.org/abs/2611.17621
---

# AscendGYM

**AscendGYM** is a kernel optimization benchmark for **Huawei Ascend NPUs**, built and released by the **Shenzhen Loop Area Institute**, a Chinese research organization. Covered in Import AI 482 (Jack Clark, Nov 23 2026). It is the first benchmark that measures whether coding agents can improve the performance of *already-correct* kernels on non-NVIDIA Chinese silicon.

## Core Evaluation Question

Unlike kernel-generation benchmarks, AscendGYM asks:

> Given a correct kernel implementation, can an agent further improve performance on the target workload **while preserving correctness** and staying within a compute budget?

This mirrors real production kernel-optimization work, where a working baseline already exists and the task is performance engineering rather than from-scratch generation.

## Evaluation Environment: AscendForge

The benchmark ships with **AscendForge**, a unified interface that handles:

- **Compilation** of candidate kernels for Ascend NPUs
- **Correctness verification** against reference outputs
- **Performance measurement** on target workloads
- **Feedback loop** back to the agent

## Model Results (as reported in Import AI 482)

| Finding | Detail |
|---------|--------|
| Best single model | **Claude Opus 5** |
| Runner-up | **GPT-5.6** |
| Best open-weight | **GLM-5.3** |
| Best harness | **Claude Code** achieved the highest absolute scores |
| Token efficiency | GPT-5.6 was token-efficient; Opus 5 consumed notably more tokens |

## Jack Clark's Framing: "China's Own Form of RSI"

Clark reads AscendGYM as material for a **Chinese version of recursive self-improvement (RSI)**: because export controls prevent China from buying Western semiconductors, Chinese labs are pushed to extract maximum performance from domestic Huawei silicon — and kernel-optimizing agents are a direct lever for that. See [[concepts/recursive-self-improvement]] and [[concepts/us-china-ai-race]] context.

## Related

- [[concepts/nvidia-blackwell-architecture]] — Ascend 950 as the geopolitically significant Blackwell competitor
- [[concepts/deepinfer]] — DeepSeek's Ascend 950 NPU inference path (same domestic-silicon optimization pressure)
- [[concepts/deepseek-v4]] — frontier inference running entirely on Ascend 950DT
- [[concepts/ai-benchmarks]] — benchmark hub

## Sources

- Import AI 482 (Jack Clark, Nov 23 2026): `raw/newsletters/2026-11-23-import-ai-482-huawei-kernel-benchmarks-airborne-drone-detection-and-a-national-l.md`
- arXiv: [2611.17621](https://arxiv.org/abs/2611.17621)
