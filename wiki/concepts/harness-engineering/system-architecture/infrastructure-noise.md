---
title: "Quantifying Infrastructure Noise in Agentic Coding Evals"
type: concept
aliases:
  - infrastructure-noise
  - agentic-eval-noise
  - benchmark-infrastructure
created: 2026-04-12
updated: 2026-05-26
tags:
  - concept
  - architecture
  - harness-engineering
  - anthropic
  - evaluation
status: draft
sources:
  - "https://www.anthropic.com/engineering/infrastructure-noise"
---

# Quantifying Infrastructure Noise in Agentic Coding Evals

A study quantifying the impact of infrastructure configuration alone on agentic coding benchmark scores.

## Core Insight

> "Infrastructure configuration alone can swing agentic coding benchmark scores by up to 6 percentage points—often exceeding the narrow margins separating top models on public leaderboards."

> "An agent that writes lean, efficient code very fast will do well under tight constraints. An agent that brute-forces solutions with heavyweight tools will do well under generous ones. Both are legitimate things to test, but collapsing them into a single score without specifying the configuration makes the differences—and real-world generalizability—hard to interpret."

**Infrastructure configuration alone can swing benchmark scores by up to 6 points — exceeding the margin between top models.**

## Experimental Results

### Terminal-Bench 2.0 (6 settings: `1x` strict → uncapped)

| Metric | 1x | 3x | uncapped |
|-----------|-----|-----|----------|
| Infra error rate | 5.8% | 2.1% | 0.5% |
| Success rate change | - | p=0.40 (not significant) | +6pp (p<0.01) |

- `1x → 3x`: Merely absorbs transient OOM kills without making tasks easier
- `3x → uncapped`: Success rate jumps ~4pp. Infra errors drop only 1.6pp. **Infrastructure enables new solution pathways**

### SWE-bench Crossover (RAM up to `5x` baseline)

- Same monotonic increase, but smaller magnitude: **`5x` yields +1.54pp over `1x`**
- Expected, since SWE-bench tasks are generally less resource-intensive

## How Infrastructure Changes What Is Measured

| Resource Band | Impact on Evaluation | What Is Being Measured |
|:---|:---|:---|
| **≤ `3x` headroom** | Fixes infra reliability (transient spikes) | Stabilizes eval without artificially inflating scores |
| **> `3x` headroom** | Actively enables new solution pathways | Rewards agents that exploit generous resources |

### Strategy Bias Example (`bn-fit-modify`)
- **Generous limits**: Agent installs `pandas`, `networkx`, `scikit-learn` → success
- **Tight limits**: Pod OOMs during installation. Only lightweight strategies (stdlib math) succeed

> Different models default to different approaches. Resource settings determine which defaults succeed, conflating `model capability` with `infrastructure tolerance`.

## Other Hidden Variables

- Time limits, cluster health, hardware specs, concurrency level, outbound bandwidth
- **API latency/time-of-day**: Pass rates fluctuate with traffic patterns and incidents
- **Important**: The boundary between model capability and infrastructure behavior is blurrier than any single benchmark score suggests

## Implications for Benchmark Interpretation

> "A few-point lead might signal a real capability gap—or it might just be a bigger VM."

- **Leaderboard skepticism**: Differences of `<3pp` should be treated cautiously unless evaluation settings are documented and consistent
- Simple binomial confidence intervals already cover `1-2pp`. Infra confounders add on top
- For labs: Resource allocation directly impacts measured capability. Standardization is critical for reproducibility

## Practical Recommendations

1. **Specify dual parameters**: Evaluation settings should define both guaranteed allocation and hard kill limits
2. **Calibrate bands**: Set ceilings so floor/ceiling scores fall within statistical noise
3. **Report methodology**: Publish exact resource multipliers and enforcement strategies
4. **Treat infrastructure as a first-class variable**: Document and control resource settings with the same rigor as prompt format and sampling temperature

## Related Concepts

- [[concepts/harness-engineering]] — Parent index
- [[comparisons/evals-skills]] — Evaluation skills
- [[concepts/harness-design-long-running-apps]] — Harness design
- [[concepts/ai-evals]] — AI evaluation concepts

