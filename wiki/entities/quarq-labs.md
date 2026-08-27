---
title: "Quarq Labs"
type: entity
created: 2026-04-30
updated: 2026-08-26
tags:
  - lab
  - research-lab
  - open-source
  - context-management
sources:
  - raw/articles/2026-04-29_quarqlabs-longcot.md
  - https://x.com/quarqlabs/status/2049392959616143809
related:
  - entities/raw-works
  - entities/alex-zhang
  - concepts/harness-engineering
  - concepts/agentic-scaffolding
---

# Quarq Labs

Quarq Labs (@quarqlabs) is an AI research lab focused on **long-context reasoning** and **scaffold-based agent performance**.

## Key Achievement (April 2026)
- Published announcement about hitting state-of-the-art on **LongCoT** (Long Chain-of-Thought)
- **Qwen3.5-9B** (relatively small model) beat **GPT-5.2** on a long-horizon reasoning benchmark by over 60%
- Key insight: "using the right scaffold" — not just model size, but the orchestration pattern matters

## The Scaffold-Over-Size Thesis

Quarq Labs' result sits in the same April 2026 cluster of evidence that **scaffold quality can exceed raw model size** on long-reasoning benchmarks:

| Lab / Researcher | Result (Apr 2026) | Scaffold |
|------------------|-------------------|----------|
| [[entities/quarq-labs\|Quarq Labs]] | Qwen3.5-9B beat GPT-5.2 by 60%+ on long-horizon reasoning | Unspecified ("the right scaffold") |
| [[entities/raw-works\|Raymond Weitekamp]] | Qwen3.5-9B + dspy.RLM: 15.69% LongCoT-Full SOTA vs GPT-5.2's 9.83% | DSPy.RLM (recursive prompting) |
| [[entities/alex-zhang\|Alex Zhang]] | GPT-5.2 + RLM + tips: 65.6% LongCoT-mini (baseline 38.7%) | RLM + trajectory-analysis tips |

All three cases converge on the [[concepts/harness-engineering|harness engineering]] thesis: the orchestration layer around a model matters as much as — or more than — the model's parameter count.

## Philosophy
Quarq Labs explores whether **true intelligence** emerges from the right scaffolding around smaller models, rather than sheer parameter count. This aligns with the broader [[concepts/harness-engineering]] thesis that the infrastructure around the model matters as much as the model itself.

## Ecosystem Position

- Announced via X (@quarqlabs) — a video/image post (metadata-only content, no written blog yet)
- Closest public-voice analogue: [[entities/raw-works|Raymond Weitekamp]], who documented the RLM approach in detail on raw.works
- Benchmark: [LongCoT](https://longcot.ai/) — long-horizon chain-of-thought reasoning

## Related
- [[entities/raw-works]] — Quarq Labs published the announcement 2 weeks ago on this profile
- [[concepts/agentic-scaffolding]] — Quarq Labs demonstrates the power of proper scaffolding
- [[concepts/harness-engineering]] — The umbrella thesis: scaffold quality ≈ model quality
