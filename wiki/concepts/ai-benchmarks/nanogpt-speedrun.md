---
title: "NanoGPT Speedrun Frontier"
type: concept
aliases:
  - nanogpt-speedrun
created: 2026-08-23
updated: 2026-08-23
tags:
  - benchmark
  - evaluation
  - agentic-engineering
  - harness-engineering
  - agentic-rl
sources:
  - raw/articles/2026-08-23_primeintellect_nanoGPT-speedrun-frontier.md
  - https://www.primeintellect.ai/research/nanogpt-speedrun
  - https://news.ycombinator.com/item?id=49404380
---

# NanoGPT Speedrun Frontier

**NanoGPT Speedrun Frontier** is a public leaderboard published by [[entities/prime-intellect|Prime Intellect]] (research page, ~Aug 22, 2026; HN [item 49404380](https://news.ycombinator.com/item?id=49404380)) that ranks frontier models on a continuous-time agentic optimization task: autonomously optimize a nanoGPT training run until it beats a human baseline ("human record"), measured as **share of the human record gap closed** per run.

**Setup (from the research page):** 153 autonomous agent runs across **18 frontier models**, each model wrapped in its native harness (claude-code, codex, prime-agent, grok-cli, qwen-code, kimi-code, pi, muse-code) at various effort settings. All agent traces are published. The leaderboard is live and values move as runs finish — treat any snapshot as point-in-time.

## Snapshot (captured 2026-08-23)

| Model | Harness | Gap closed | Tokens | Days |
|---|---|---|---|---|
| Fable 5 | claude-code · high | **81.7%** | 800M | 8.7 |
| Opus 5 | claude-code · max | 53.6% | 183M | 2.9 |
| Kimi K3 | prime-agent · max | 52.2% | 112M | 3.6 |
| GPT-5.6 Sol | codex · xhigh | 35.9% | 2.9B | 6.1 |
| GPT-5.6 Luna | codex · xhigh | 26.1% | 894M | 1.9 |
| Qwen3.8 Max | qwen-code · max | 24.6% | 216M | 1.9 |
| DeepSeek V4 Pro | claude-code · max | 12.3% | 26M | 1.1 |
| GPT-5.5 | codex · xhigh | 8.1% | 70M | 1.1 |

(Full 19-row table in the raw article. "note / serial era / running" mark run modes on the live page.)

## What makes it structurally different

- **Continuous-time, non-boolean outcome.** SWE-Bench-family benchmarks report pass@k on discrete tasks; here the score is a graded, unbounded quantity (gap closed %), so harness/effort differences can't be papered over by a single lucky pass.
- **Harness × model, not model-only.** Every row names its harness and effort level. Kimi K3 scores 52.2% under prime-agent vs 45.8% under kimi-code; within claude-code, Fable 5 (81.7%) vs Opus 5 (53.6%) vs DeepSeek V4 Pro (12.3%) is a ~70pp spread — the model dominates the ranking, but harness and effort settings are first-class variables, not noise.
- **Token-cost dimension is exposed.** Opus 5 reaches 53.6% gap closure on 183M tokens vs Fable 5's 800M (4.4× cheaper for ~half the progress); GPT-5.6 Sol burns 2.9B tokens for 35.9%. "Best model" is not answerable without a cost/time axis.
- **Published trajectories.** All runs link to full traces — this is a bench for studying *how agents explore optimization landscapes*, not just who wins.

## Relation to the eval-noise debate

This leaderboard is a constructive datapoint for [[concepts/quantifying-infrastructure-noise-in-agentic-coding-evals|infrastructure noise in agentic coding evals]] and the **benchmaxxing** discussion: on a task with a fixed, public, continuous metric, harness choice and effort settings produce order-of-magnitude differences in token efficiency and large gaps in outcome. It also sits adjacent to [[concepts/ai-benchmarks/swe-bench|SWE-Bench]]-style coding evals and to Prime Intellect's own [[concepts/gepa|GEPA]]/RL post-training workline — the speedrun is both an eval artifact and a research environment for self-improving agents.

## Related Pages

- [[entities/prime-intellect]] — publisher; open stack for self-improving agents
- [[concepts/quantifying-infrastructure-noise-in-agentic-coding-evals]] — OpenAI's harness-variance analysis; consumer-side corroboration
- [[concepts/ai-benchmarks/swe-bench]] — boolean-task coding benchmark family
- [[concepts/ai-benchmarks/terminal-bench]] — same harness×model leaderboard lineage, now extended to science workflows (Terminal-Bench-Science 0.1)
- [[concepts/self-evolving-agents]] — agents that improve their own toolchains
- [[concepts/ai-evals]] — evaluation methodology overview
