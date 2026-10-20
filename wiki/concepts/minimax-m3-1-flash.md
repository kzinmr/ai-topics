---
title: "MiniMax M3.1 Flash"
created: 2026-10-20
updated: 2026-10-20
type: concept
tags: [model, agent-employees, computer-use, cost-optimization, benchmark, cybersecurity, token-economics]
aliases:
  - "MiniMax-M3.1-Flash"
  - "M3.1 Flash"
confidence: high
sources:
  - url: https://www.minimax.io/blog/minimax-m31f
    title: "MiniMax M3.1 Flash: Redefining Agent Performance and Cost"
    org: MiniMax
    date: 2026-10-19
  - url: https://news.ycombinator.com/item?id=50154540
    title: "HN discussion — MiniMax M3.1 Flash (481 pts)"
    date: 2026-10-19
  - raw/articles/2026-10-20_minimax-minimax-m31f-m3-1-flash.md
related:
  - concepts/minimax-m3
  - concepts/minimax-m2-7
  - entities/minimax
  - concepts/minimax-sparse-attention
  - concepts/deepinfer
---

# MiniMax M3.1 Flash

**MiniMax M3.1 Flash** is [[entities/minimax|MiniMax]]'s next-generation Flash-tier model, announced **2026-10-19** (HN 481 pts / 206 comments). MiniMax positions it as a generational leap in agentic tasks, coding, Computer Use, and cybersecurity, with ~3× faster online inference and **70% lower usage cost** than its predecessor. Model weights are promised "later" (API first), unlike the open-weights [[concepts/minimax-m3|M3]] line.

## Positioning

Flash is MiniMax's efficiency/capability-balance tier; the company says a capability-pushing "Pro" variant will also arrive later. M3.1 Flash targets "practical problems in sales, marketing, operations, customer service, finance, and HR from end to end."

## Benchmarks (first-party, MiniMax-reported)

| Benchmark | Score | Note |
|-----------|-------|------|
| BankerToolBench | 76.2 | Multi-step planning, document consistency, financial compliance, chained tool calls |
| DeepSWE v1.1 | 73.7% | "Alongside top models" — independent code understanding → feature dev → fix → test validation |
| OSWorld V2 | 61.7 | #1 among Chinese models (computer operation, cross-app tasks) |
| Agents' Last Exam (ALE) | 29.6 | #1 among Chinese models (real professional work with economic value) |
| CyberGym | 82% | Vulnerability discovery/validation; internal expert evals cover code auditing, patching, pentesting, malware analysis, reverse engineering |

## Efficiency & pricing

- Aggressive sparsity optimizations: **200+ TPS** output speeds in everyday use, P50 **170+ TPS**.
- Flat pricing per 1M tokens: **$0.15 input · $0.60 output · $0.015 cached input**.
- MiniMax claims performance on par with top models at very low task cost across Automation-Bench, DeepSWE, and ALE — "setting a highly competitive new standard for performance and cost."

## Caveats

- All benchmark numbers are first-party vendor claims; no third-party verification yet at time of writing.
- API-only at launch ("M Plan", MiniMax Code desktop app, platform.minimax.io); weights "will be released later" — contrast with M3's open-weights release.
- Continues the Chinese-lab Flash-tier price/performance offensive that the [[events/2026-10-17-deepseek-v4.1-flash-1017-release|DeepSeek V4.1-Flash-1017]] release and the concurrent [[concepts/deepinfer|DeepInfer]] open-sourcing intensified days earlier.

## See Also

- [[concepts/minimax-m3]] — predecessor frontier model (MSA architecture, 1M context)
- [[entities/minimax]] — company page
- [[concepts/minimax-sparse-attention]] — MSA architecture underlying the M-line
