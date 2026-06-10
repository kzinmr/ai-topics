---
title: "Infrastructure Noise in Agentic Coding Evals"
type: concept
created: 2026-05-08
updated: 2026-05-08
tags:
  - evaluation
  - infrastructure
  - benchmark
  - coding-agents
aliases:
  - infra noise evals
  - resource allocation variance
status: active
sources:
  - raw/articles/2026-05-08_anthropic-engineering_infrastructure-noise.md
  - https://www.anthropic.com/engineering/infrastructure-noise
related:
  - swe-bench
  - frontier-swe-benchmark
  - ai-resistant-evaluations
---

# Infrastructure Noise in Agentic Coding Evals

Quantitative analysis of how **infrastructure configuration differences alone can cause significant score variation** in agentic coding benchmarks. "Hidden variables" like resource allocation, time limits, and cluster state distort the measurement of model capability.

## Key Findings

> On Terminal-Bench 2.0, a **6pp difference** (p < 0.01) between the most resource-constrained and unconstrained settings.

Leaderboard gaps at the top are often 2-3pp, meaning infrastructure configuration differences can exceed them.

## Experimental Setup

Terminal-Bench 2.0 run across 6 resource configurations:
- **1x**: Task-specified value = guaranteed allocation = hard cap (strict enforcement)
- **3x**: 3x headroom
- **Uncapped**: No limits

Comparison with identical model (Claude), same harness, same task set.

## Results

| Config | Infra Error Rate | Success Rate | Significance |
|------|---------------|--------|--------|
| 1x (strict) | 5.8% | baseline | — |
| 3x | 2.1% | within noise (+1.5pp) | p=0.40 |
| Uncapped | 0.5% | **+6pp** | p<0.01 |

### Two Phases

**Phase 1 (1x to 3x)**: Infrastructure reliability improvement
- Prevents false OOM-Kills from temporary resource spikes
- Score within noise range (p=0.40) → does not make eval "easier"

**Phase 2 (3x to unlimited)**: Change in evaluation nature
- 1.6pp reduction in infrastructure errors vs 4pp increase in success rate
- Enables large dependency pulls, high-load subprocesses, memory-intensive tests
- Looser constraints favor "resource-utilizing strategies" over "efficient strategies"

## SWE-bench Reproduction

227 tasks × 10 samples with RAM 1x to 5x:
- Same direction effect, smaller magnitude (+1.54pp at 5x)
- Because SWE-bench tasks are less resource-intensive

## Other Hidden Variables

- **Time of day**: API latency varies with traffic patterns → pass rates also vary (unquantified)
- **Concurrency**: Simultaneous execution count
- **Egress bandwidth**: Network speed
- **Hardware specs**: CPU, disk I/O

> "Agentic evaluation is structurally an end-to-end system test, and any component of the system can be a confounding factor"

## Recommendations

### For evaluation runners
- Specify **both** guaranteed allocation and hard cap per task (not a single value)
- Calibrate the cap within the floor's noise range (3x recommended for Terminal-Bench 2.0)
- Average out noise by running across multiple times and days

### For benchmark consumers
- **Be skeptical of leaderboard gaps under 3pp** (especially if configuration is unpublished)
- Simple binomial confidence interval (1-2pp) + infrastructure confounding (~6pp) = effective uncertainty exceeds what's shown

## See Also

- [[concepts/ai-benchmarks/swe-bench]] — SWE-bench benchmark
- [[concepts/frontier-swe-benchmark]] — Frontier SWE benchmark
- [[concepts/ai-resistant-evaluations]] — AI-resistant evaluation design
- [[concepts/eval-awareness-browsecomp]] — Eval awareness and contamination
- [[swe-bench-agent-scaffolding]] — Agent scaffolding for SWE-bench
