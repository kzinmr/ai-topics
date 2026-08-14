---
title: DataBench
type: concept
created: 2026-08-14
updated: 2026-08-14
tags:
  - benchmark
  - evaluation
  - agent-evaluation
  - text-to-sql
  - data-science
  - llm-as-judge
sources:
  - https://hex.tech/blog/databench-agentic-analytics-benchmark/
  - raw/articles/2026-08-14_hex-technologies_databench-agentic-analytics-benchmark.md
related_concepts:
  - agent-evaluation
  - llm-as-judge
  - cursorbench
---

# DataBench

DataBench is an agentic analytics benchmark from [[entities/hex-technologies]] that evaluates how frontier LLMs perform on realistic, under-specified analytical tasks in a messy enterprise data warehouse. It targets the gap between existing analytics benchmarks (which the authors call "overspecified pub trivia") and the vague, directional prompts real users send to agentic analytics tools.

## What It Measures

DataBench v1 covers **100 realistic analytical tasks** split into Q&A and Open-Ended prompts, all executed in the **Shorelane Commerce** synthetic environment (a fake B2B2C office-supplies platform doing ~$129M/year). Ten tasks are deliberately constructed "signature traps."

- **Q&A tasks**: Straightforward but not over-specified analytical queries ("What was conversion by device and browser for our campaigns?"). Correctly answering requires discovering hidden context — which timestamp clock to use, which population to track (canceled orders stay in booked volume by convention), which labels (channel renames without backfill), and which revenue column (five plausible candidates, each meaning something different).
- **Open-ended tasks**: Require the agent to create an artifact or make a judgment call ("Should we keep giving two months free on annual plans?"), synthesizing multiple data points with judgment — "cleverly" working around a correct simple answer to produce a convoluted wrong one is a common failure.
- **Signature traps**: Tasks with an obvious, plausible-but-wrong answer where success requires going deeper (e.g., a collections call list where the "obvious" delinquent accounts are stale sync artifacts — only Opus 5 passed).

## Methodology

- **Environment**: Shorelane Commerce — migrated platforms in 2021 (dropped customer IDs), acquired a competitor without merging data, renamed sales channel in 2022 without backfill, three ad platforms with different conversion totals, five "revenue" columns, six years of data, 30,000 handcrafted lines of generators/dbt models/docs. Workspace ships with "golden" semantic models but some task-critical data sits unmodeled.
- **Judge**: Every task is evaluated by an LLM judge (GPT-5.6 Sol) with a plain-language rubric brief (right answer + evidence, why the case is hard, traps, common failure modes). Each verdict is the majority of three judge runs (judges agreed 96% of the time).
- **Execution**: Runs in the Hex workspace using Hex's native Evals functionality.

## Key Results

- **High floor**: No model/effort pair scores below 50%; the performance floor is much higher than expected — models are innately good at noticing analytical details across 250K-token query results.
- **Early Pareto frontier is steep**: GPT-5.6 Luna forms the entire pre-elbow of the Pareto frontier — near-Sol performance at xHigh effort for ~1/14th the cost, and the only model that increases accuracy with effort without significant cost increases.
- **Effort can backfire**: Unlike coding benchmarks (CursorBench shows clean test-time-compute curves), DataBench shows **regressions at high effort** — models talk themselves past correct simple answers (Opus 5 "devastated" at xhigh/max; e.g., correctly stating access runs through the paid term at medium effort, then hedging at max effort after triple work).
- **Claude Fable 5 is the exception**: The only model where scaling test-time compute/effort consistently buys better outcomes without regressions (85/100 top score).
- **GPT-5.6 Luna is absurd bang-for-buck**; GPT-5.6 Sol is "good enough" at half the cost; Sonnet 5 is "a bit confusing and probably rarely the right choice."
- **Task-type breakdown**: Best at evidence gathering (75% Q&A), worse at open-ended delegated decisions (66%), worst at traps (54%) — the gap is *judgment*, with smaller models hanging close on Q&A but falling behind on traps.
- **Failure mode — manufacturing certainty**: Opus 5 at max effort produced eleven minutes of correct arithmetic then promoted correlation into a causal law ("each extra parcel is an independent opportunity for a complaint") and wrote a confident recommendation — on an intentional trap where the data cannot distinguish the two stories.

## Connections to Other Wiki Concepts

DataBench exemplifies the trend toward domain-specific [[agent-evaluation]] for knowledge-work agents, parallel to [[cursorbench]] for coding agents. Its LLM-judge rubric methodology connects to [[llm-as-judge]]; its findings on test-time-scaling regressions are relevant to the broader [[test-time-scaling]] discussion. The benchmark complements [[entities/hex-technologies]]' Shoebox evaluation lab and Shorelane environment (the same synthetic business DataBench runs in). Hex plans to open-source the Shorelane analytical environment so other agentic-analytics builders can use a realistic public eval environment; DataBench itself remains private to avoid training contamination.

## Related
- [[entities/hex-technologies]] — benchmark creator; Shoebox eval lab, Shorelane environment
- [[concepts/ai-benchmarks/cursorbench]] — coding-agent benchmark with clean test-time-compute curves (contrast case)
- [[concepts/evaluation/llm-as-judge]] — rubric-judge methodology
- [[concepts/evaluation/agent-evaluation-methodology]] — agent eval design
