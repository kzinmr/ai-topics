---
title: "StarSkirmish Bench"
type: concept
created: 2026-10-19
updated: 2026-10-19
tags:
  - benchmark
  - ai-agents
  - coding-agents
  - agentic-rl
  - self-play
confidence: medium
sources:
  - url: https://starskirmish.com/bench/v0-2/
    title: "StarSkirmish Bench v0.2"
    author: Kai McPheeters
    date: 2026-10-15
  - raw/articles/2026-10-19_active-crawl-mlx-starskirmish-web-access.md
related:
  - concepts/ai-benchmarks/index
  - concepts/coding-agents/_index
  - concepts/post-training/sdar-self-distilled-agentic-rl
  - events/2026-10-01-gemini-4-argon-release
  - concepts/frontier-models-comparison-april-2026
  - concepts/code-review-bottleneck
---

# StarSkirmish Bench

> An agentic coding benchmark where each frontier LLM gets **one hour** to write a competitive StarCraft: Brood War Protoss bot in C++, tested against established human-written bots. Created by Kai McPheeters. HN 249p (Oct 16, 2026).

## Design

- **Task**: Each LLM writes a Protoss bot in C++ against BWAPI 4.4.0, played on OpenBW. One hour of wall-clock time.
- **Starting state**: Skeleton bot that only mines. Source code of three demo bots is provided as reference.
- **Evaluation**: Average win rate (0–100) over 5 runs against a roster of competitive human-written bots and demo bots.
- **Maps**: Protoss vs Protoss on three ladder maps — Heartbreak Ridge, Benzene, Destination. Game ends when one side's buildings are destroyed; 60-minute cap (86,400 frames) decided by BASIL ladder scoring (kills + razings).
- **Harness**: Each model runs in its lab's first-party CLI harness (Codex for OpenAI, Claude Code for Anthropic, etc.).
- **Reasoning effort**: Gemini 4 Argon runs at "high" (its maximum); every other model runs at "max."

## What It Tests

StarSkirmish is distinctive as a **dual-capability** benchmark:

1. **Long-horizon agentic coding**: Writing competitive real-time-strategy game AI in C++ under time pressure — a complex, multi-file software engineering task with no reference implementation.
2. **Self-improving practice loop**: LLMs must incorporate learnings from practice games to iteratively improve their bot within the hour. The bot starts weak; the model must observe losses, diagnose weaknesses, and rewrite strategy. This makes self-directed experimentation a core measured skill, not an add-on.

The strongest predictor of a model's score is **how many practice games it plays against the 7 strongest roster bots** during the hour — a behavioral signal about self-directed learning.

## v0.2 Results (Oct 15, 2026)

v0.2 updates v0.1 with flagship models from OpenAI, Anthropic, Google, and Meta.

| Rank | Model | Score (avg win rate) | Notes |
|------|-------|---------------------|-------|
| 1 | GPT-6 Astra | clear leader | Starts playing strong bots early; runs cost ~10x GPT-6.1 Sol |
| 2 | GPT-6.1 Sol | ~10 points behind | Best cost/value — only model in "most attractive quadrant" |
| 3–5 | Gemini 4 Argon | ~37–39 | Highest variance (best/worst runs 18 pts apart) |
| 3–5 | Claude Opus 5.5 | ~37–39 | Consistent across runs (±8 pt spread) |
| 3–5 | Claude Fable 5.1 | ~37–39 | **Outlier**: scores 37 while practicing almost entirely vs weaker bots |
| 7 | Muse Wonder Full | behind leaders | Rarely/never practices vs strong roster bots |

### Key observations

- **No sign of saturation**: The best model (GPT-6 Astra) wins only **7%** against top human-written bots (Stardust, PurpleWave, BananaBrain). Human bots remain dominant.
- **Cost/value**: GPT-6.1 Sol is uniquely positioned — second-highest score at just over 1/10th of GPT-6 Astra's per-run API cost.
- **Variance**: Gemini 4 Argon's run-to-run spread (18 pts) is double that of GPT-6 Astra (9 pts) or Claude Opus 5.5 (8 pts).
- **Self-play behavior predicts success**: GPT-6 Astra, GPT-6.1 Sol, and Gemini 4 Argon begin playing the strongest bots early in the hour even while losing. Muse Wonder Full, Claude Haiku 5.5, and GPT-6 Luna rarely or never practice against them.
- **Fable 5.1 anomaly**: Tied at 37 while practicing almost exclusively against weaker bots — suggests strong code-writing ability without self-directed learning pressure.

## Context

- **v0.1 predecessors**: Gemini 3.8 Flash and Muse Spark 1.3 (now replaced by Gemini 4 Argon and Muse Wonder Full). GPT-6 Astra and Claude Opus 5.5 were introduced in v0.1.
- **Human bot lineage**: Stardust, PurpleWave, and BananaBrain are established, expert-crafted bots from the BWAPI community with years of iteration — the benchmark measures the LLM against real competitive programming.
- **Comparison to other agentic benchmarks**: Unlike [[concepts/ai-benchmarks/tau-bench]] or [[concepts/agents-last-exam]], StarSkirmish measures code quality through **adversarial gameplay outcomes** rather than task-completion metrics. Unlike [[concepts/coding-agents/_index|SWE-bench]]-style benchmarks (single-repo diffs), it requires building an entire real-time strategy program from scratch with no fixed specification.

## Limitations

- **Single game**: Protoss vs Protoss only; no race diversity or matchup strategy variance.
- **Time-bound**: The 1-hour cap may not reflect performance given longer development cycles.
- **Small roster**: ~10 models in v0.2; statistical power on individual rank differences is limited.
- **Cost reporting**: Based on API pricing at time of evaluation; subject to change.

## Related

- [[concepts/ai-benchmarks/index]] — benchmark directory
- [[concepts/coding-agents/_index]] — agentic coding capabilities
- [[concepts/post-training/sdar-self-distilled-agentic-rl]] — self-improvement via practice loops
- [[events/2026-10-01-gemini-4-argon-release]] — Gemini 4 Argon release context
- [[concepts/frontier-models-comparison-april-2026]] — frontier model landscape
- [[concepts/code-review-bottleneck]] — complementary measurement of coding-agent productivity
