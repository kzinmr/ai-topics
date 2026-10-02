---
title: "DAYJOB — Long-Horizon Professional Work Benchmark"
created: 2026-10-02
updated: 2026-10-02
type: concept
tags:
  - benchmark
  - agent-evaluation
  - long-horizon
  - enterprise-agents
  - healthcare
  - labor
  - domain-expertise
aliases:
  - DAYJOB
sources:
  - raw/articles/arxiv-2610.01306-dayjob-long-horizon-professional-work-benchmark.md
confidence: medium
related:
  - concepts/long-horizon-agents
  - concepts/legible-work
  - concepts/reward-hacking-research-agents
  - concepts/ai-benchmarks/frontier-swe-benchmark
---

# DAYJOB — Long-Horizon Professional Work Benchmark

**DAYJOB** (Finley et al., 15 authors including Edwin Chen; arXiv:2610.01306, Oct 1, 2026) is a benchmark of **130 tasks built by working professionals** in healthcare (50) and finance (80), measuring whether agents can do multi-day knowledge work from an ambiguous brief — not solve a closed problem.

## Design

- Tasks are estimated to take a human professional **13.6 hours on average** (healthcare) and **16.6 hours** (finance) — multi-day scale, an order of magnitude beyond SWE-bench-style tasks.
- Each task is a **containerized Harbor environment** with an expert-written rubric of **binary criteria** (median 47.5 per healthcare task, 57.5 per finance task).
- An **agentic judge** applies the rubric to delivered files; an attempt passes only if it meets **every** criterion (all-or-nothing).
- Tasks deliberately start with "a brief request that leaves the professional to work out what is needed, which documents matter, and whether the request's premise holds" — premise verification is part of the job.
- Released: all 50 healthcare tasks, 50 of 80 finance tasks, the evaluation harness, and a leaderboard.

## Results (30 model configurations, 13 developers)

| Configuration | Healthcare pass | Finance pass |
|---|---|---|
| Best: **Claude Opus 5.5** | **24.7%** | **23.9%** |
| Median configuration | 0.6% | 2.5% |

The headline failure mode in case studies: **agents accept premises that the record contradicts** and carry wrong inputs through otherwise-consistent analyses. The reasoning is sound; the factual foundation was never checked.

## Why it matters

- **Frontier = quarter of a day's work, verified end-to-end.** At ~24% all-or-nothing pass on 13-17 hour tasks, the top model cannot yet be trusted to *replace* a professional on real deliverables — a much sharper deployment boundary than any chat benchmark. The long tail (median 0.6-2.5%) shows most configurations are not close.
- **Premise acceptance** is the empirically-grounded failure mode for agent deployment in knowledge work: it aligns with the "absorbed bad context" failure family and argues for premise-checking as a first-class harness capability, connecting to [[concepts/explicit-belief-states-long-horizon-agents]]' "unresolved requirements + world-state estimate" design.
- **All-or-nothing rubric judging** (47-58 binary criteria via agentic judge) is a harder evaluation regime than partial-credit rubrics used elsewhere (cf. [[concepts/ai-benchmarks/frontier-swe-benchmark]]), making pass rates conservative lower bounds.
- As labor-displacement claims concentrate on white-collar automation, DAYJOB is the first benchmark calibrated in *professional hours* — its results translate directly into "what fraction of a workday an agent can independently close."

## Limitations

- 130 tasks, two industries; not a general professional-work measure.
- Agentic-judge grading inherits judge weaknesses (cf. reward-hacking findings in research agents — judge gaming is plausible under binary rubrics).
- Single source; confidence medium pending leaderboard activity from third parties.

## Related

- [[concepts/long-horizon-agents]] — the product category DAYJOB operationalizes
- [[concepts/explicit-belief-states-long-horizon-agents]] — PoS targets premise/world-state failures DAYJOB measures
- [[concepts/reward-hacking-research-agents]] — agentic-judge gaming risk for rubric benchmarks
- [[concepts/legible-work]] — which professional work is verifiable enough to benchmark (tag; see [[concepts/the-untrainable]])
