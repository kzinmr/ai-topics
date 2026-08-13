---
title: "AI Timelines & ESNI Tasks"
created: 2026-08-13
updated: 2026-08-13
type: concept
tags: [concept, forecasting, prediction, timeline, automation, agi, ai-safety, coding-agents]
aliases: [esni-tasks, ai-timelines]
related:
  - [[concepts/scaffold-vs-rl-debate]]
  - [[concepts/agentic-scaffolding]]
  - [[concepts/ai-coding-effectiveness-debate]]
  - [[entities/epoch-ai]]
sources:
  - raw/articles/substack.com--redirect-83a03e0e-24ff-40d0-8d66-d76a255c3ac2--89f6ff53.md
---

# AI Timelines & ESNI Tasks

## Summary

A March 2026 forecasting update (captured via Substack redirect, author not identified in the raw file) argued that AI capability timelines had shortened substantially: AIs can now often complete massive, easy-and-cheap-to-verify software engineering tasks, and this observation propagates directly into AI R&D automation forecasts. The post introduced a task taxonomy (ES / ESNI), reported superexponential progress on the 50%-reliability time horizon for those tasks, and revised the probability of full AI R&D automation by end-2028 to ~30% (up from ~15%).

## ES / ESNI Task Taxonomy

- **ES tasks** ("easy-and-cheap-to-verify"): tasks whose correctness can be checked cheaply, so the AI can build a test suite / benchmark set and iterate against it. Examples: fully-CLI software tasks, straightforward metric-optimization tasks.
- **ESNI tasks**: ES tasks that do not require much ideation (no "new" ideas beyond what is already on the internet).
- Task hierarchy: (1) ES tasks -> (2) tasks checkable for training/evaluation but not easily self-checkable by the AI -> (3) harder-to-check tasks. The gap between (1) and (2) appears much larger than the gap between (2) and (3).
- A separate axis is ideation: tasks requiring clever ideas resist iterative attack; distributed/concurrent and algorithms-heavy software is substantially harder to build iteratively, while schlep-heavy software (many small well-defined pieces) is ideal for incremental progress.

## Why Easy-to-Verify Tasks Accelerate Progress

The core mechanism: the AI develops its own test suite, then spends unbounded time optimizing its solution against that evaluation set. Mistakes become non-critical because there is a correcting loop; multiple AIs can write test sets, and the test suite itself can be improved incrementally. Easy verification helps at two levels: it is easier for AI companies to optimize (directly in RL and as an outer-loop metric) AND easier for the AI to keep applying labor at runtime.

## Superexponential Progress

Beyond a threshold, each successive doubling of the 50%-reliability time horizon becomes easier, because sufficient generality and error recovery allow effectively infinite time horizons (the AI keeps noticing and recovering from its mistakes). ESNI tasks entered this superexponential regime earlier than the author's prior median, because mistakes are easier to spot and recover from when verification is cheap.

## Evidence (as of March 2026)

- Opus 4.5 and Codex 5.2 were significantly above expectations; Opus 4.6 (and probably Codex 5.3/5.4) came in above expectations again. 2025 showed ~3.5-month doubling times on the METR 50%-reliability time horizon, with a big (though unreliable) jump at the start of 2026.
- Demonstrations: the author's own scaffold completing tasks that would take humans months-to-years; a C compiler almost entirely autonomously written by Claude; cyber results; forthcoming METR and Epoch AI results on software replication.
- Well-elicited 50%-reliability time horizon on ESNI tasks (public models, as of March 1): between a month and several years. The 90%-reliability horizon is much lower (hours to days).
- EOY 2026 expectation: 50%-reliability time horizon of years-to-decades on reasonably difficult ESNI tasks.
- Prior error identified: the 50%-reliability horizon on ESNI tasks is ~20x longer than on METR's task suite (previously expected ~4x; >100x plausible). Most of the gap is task distribution (checkability, iterability), not underelicitation of METR tasks.

## Scaffolding Overhang

Scaffolding overhang on very large tasks is larger than previously thought. Relatively basic scaffolds do not suffice, but a moderately sophisticated scaffold mostly unlocks the capability; better general-purpose prompting and scaffolding could greatly improve ES performance. Scaffolding matters most when a task would naturally consume a large fraction (at least ~1/3) of the model's context window.

## Updated Timelines (Cotra parity framing)

| Milestone | EOY 2026 | EOY 2027 | EOY 2028 | EOY 2029 | EOY 2030 | EOY 2031 | EOY 2032 | EOY 2033 | EOY 2034 | EOY 2038 |
|---|---|---|---|---|---|---|---|---|---|---|
| AI R&D parity | 7% | 19% | 30% | 40% | 48% | 54% | 58% | 61% | 63% | 70% |
| AI stack + conflict parity | 3% | 9% | 17% | 25% | 32% | 37% | 42% | 47% | 51% | 61% |
| Automated Coder (AC) | 11% | 27% | 39% | 48% | 56% | 62% | 66% | 69% | 71% | 77% |
| Top-Expert-Dominating AI (TEDAI) | 4% | 12% | 19% | 26% | 32% | 37% | 42% | 46% | 50% | 58% |

- "Parity" = the point at which you would be better off firing all humans working in a domain than reverting to 2020-era AI (Cotra's Six Milestones for AI Automation framing).
- Comparison: Cotra's median for AI Research Parity is early 2030 (this author: early 2031); AI Production Parity mid 2032 (this author: late 2034). The author estimates median time from AI R&D parity to TEDAI (conditioning on before 2035) at ~1.75 years.
- The author flags the numbers as reflectively unstable; most of the update happened in February 2026.

## AI R&D Automation Implications

- Only part of current AI R&D is ESNI-like: implementing optimized versions of experiments/architectures given precise specs, building well-specified internal tools/infrastructure, some cheap-to-verify ML experiments, and optimizing AI applications.
- Naive expectation: very high ESNI performance yields only a moderate speed-up; labs quickly bottleneck on ideation, taste, and expensive verification.
- Wildly superhuman ES performance could massively accelerate AI R&D — but using expensive resources more sample-efficiently than top human experts effectively requires research taste matching top humans, which looks several years away at current progress rates.
- Full AI R&D automation by EOY 2028: ~30% (previously ~15%). Progress in 2026 is expected to be faster than 2025, partly because AIs that are more useful for AI R&D accelerate the rate of progress itself.

## Bottlenecks: Taste & Judgment

- AIs have poor "taste"/"judgment" in many domains (more so in things that are harder to RL on), and this improves substantially slower than general agentic capability. It is the main observed bottleneck on less well-specified SWE tasks and on code quality even for well-specified tasks.
- Taste appears mostly driven by pretraining progress or RL on the specific domain (it does not generalize well across domains); pretraining progress is perhaps 2-3x slower than overall AI progress, though 2026 pretraining might be unusually fast.
- Empirical safety-automation experience: an agent orchestrator could complete reasonably large chunks (roughly a day to a few weeks of unaccelerated human work) of well-specified projects, but required prompting/scaffolding patches around Opus 4.5 instruction-following issues and mundane misalignment; the author flagged a forthcoming post on misalignment in current models.

## Empirical Results Reported

- 2 massive easy-to-verify SWE tasks (estimated 3-30 person-years of human work): AIs completed what looks like many months (3-12) of useful work; one project close to beating a large, moderately complex closed-source product on some dimensions; code quality low but improvable with later-developed approaches.
- 1 hard easy-to-verify AI R&D task: a few days to a bit over a week of progress vs a strong human professional; limited by idea-finding, prioritization, and resource inefficiency.
- Cyber exploitation on relatively hardened targets: quite good with moderate scaffolding, aided by domain-specific knowledge (relevant talk: Nicholas Carlini).

## Related Concepts

- [[concepts/scaffold-vs-rl-debate]] — the relative contribution of scaffolding vs RL to measured capability; this article argues scaffolding overhang is larger than previously assumed
- [[concepts/agentic-scaffolding]] — production scaffolding patterns; "scaffolding overhang" is the capability-side complement
- [[concepts/ai-coding-effectiveness-debate]] — coding agent capability vs software quality; ESNI success coexists with low code quality and poor taste
- [[entities/epoch-ai]] — METR's MirrorCode co-developer; forthcoming replication-task results cited in the article
- METR (no entity page yet) — origin of the 50%-reliability time horizon metric used throughout the post

## Sources

- raw/articles/substack.com--redirect-83a03e0e-24ff-40d0-8d66-d76a255c3ac2--89f6ff53.md — "AIs can now often do massive easy-to-verify SWE tasks and I've updated towards shorter timelines" (Substack redirect capture, auto-ingested 2026-04-18; author not identified in capture)
