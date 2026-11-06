---
title: "SWE-Marathon (Long-Horizon Engineering Benchmark)"
type: concept
created: 2026-11-06
updated: 2026-11-06
tags:
  - benchmark
  - evaluation
  - coding-agents
  - long-horizon
  - ai-agents
sources:
  - raw/articles/2026-11-06_moonshotai_kimi-k3-github-readme.md
  - "https://github.com/MoonshotAI/Kimi-K3"
related_concepts:
  - "[[concepts/ai-benchmarks/deepswe-benchmark]]"
  - "[[concepts/kimi-k3]]"
  - "[[concepts/dayjob-benchmark]]"
  - "[[concepts/ai-benchmarks/frontier-swe-benchmark]]"
---

# SWE-Marathon (Long-Horizon Engineering Benchmark)

SWE-Marathon is a long-horizon software engineering benchmark in which tasks are marathon-scale engineering sessions rather than single-issue fixes. It entered the wiki's radar as a headline discriminator in Moonshot's official [[concepts/kimi-k3|Kimi K3]] launch materials (July–October 2026), where it produced the largest score gaps of any coding benchmark in the comparison table.

## Known task characteristics

From Moonshot's disclosed evaluation setup (Kimi-K3 README, footnotes):

- Tasks run under the **Claude Code harness** (K3, Claude Opus 4.8, Claude Fable 5) or the **Codex harness** (GPT-5.6 Sol).
- Moonshot evaluated on an **H20-calibrated branch of the official tasks** (as of July 9, 2026, prior to the final v1.1 release): Docker images, **performance gates**, and reference oracles for **GPU tasks** were recalibrated for H20 GPUs, while correctness and anti-cheat validators remained unchanged.
- The existence of **GPU tasks with performance gates** implies tasks require not just correctness but measurable performance improvements — aligning with Moonshot's positioning of K3's long-horizon strengths (GPU kernel optimization, compiler development, chip design).
- Harness sensitivity is material: **Claude Fable 5 hit fallbacks on 35% of tasks** in Moonshot's run, which Moonshot itself flags as possibly depressing its measured score.

## The 2026 leaderboard (Moonshot-reported, max reasoning effort)

| Model | SWE-Marathon |
|---|---|
| **Kimi K3** | **42.0** |
| Claude Opus 4.8 | 40.0 |
| GPT-5.6 Sol | 39.0 |
| Claude Fable 5 | 35.0 (35% fallbacks) |
| GPT-5.5 | 14.0 |
| GLM-5.2 | 13.0 |

Two signals stand out:

1. **No model exceeds ~42%** — unlike Terminal-Bench 2.1 (~88) or BrowseComp (~91), where the frontier clusters near ceiling. SWE-Marathon remains far from saturation, in contrast to the depreciation dynamic of [[concepts/benchmark-ceiling]].
2. **It separates generations sharply**: GPT-5.5 (14.0) and GLM-5.2 (13.0) — strong models on other suites — collapse relative to the Sep/Jul 2026 frontier cohort (35–42). Multi-hour, gate-checked engineering sessions appear to require something beyond issue-resolution ability measured by [[concepts/ai-benchmarks/deepswe-benchmark]] or [[concepts/ai-benchmarks/frontier-swe-benchmark]].

## Positioning

SWE-Marathon complements the hour-scale professional-work suites ([[concepts/dayjob-benchmark]], GDPval-family, [[concepts/ai-benchmarks/alphaeval]]) by specializing in *engineering* marathons: endurance, self-correction against performance gates, and long tool-chain orchestration rather than professional deliverables. It is the benchmark most frontier labs' current coding claims are *not* yet leading with.

## Caveats

- Primary public data at this time comes from **Moonshot's self-reported table** (vendor-reported; H20 recalibration is a nonstandard deviation from official settings, and the official v1.1 leaderboard was not directly cited for most models). Independent multi-model reproductions should be tracked.
- The benchmark's origin/team and full task protocol are not documented on this page yet — the wiki currently records only what the K3 README discloses. Add provenance (authors, task count, official leaderboard URL) on next crawl.

## See Also

- [[concepts/kimi-k3]] — Moonshot's launch table where SWE-Marathon was the biggest separator
- [[concepts/ai-benchmarks/deepswe-benchmark]] — large-repo issue resolution (single-session scale)
- [[concepts/ai-benchmarks/frontier-swe-benchmark]] — frontier SWE suite where K3 leads with 81.2
- [[concepts/dayjob-benchmark]] — hour-scale ground-truth work, premature-commitment failure mode
- [[concepts/long-horizon-agents]] — capability cluster the marathon regime probes
