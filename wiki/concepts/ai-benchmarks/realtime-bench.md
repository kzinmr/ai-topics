---
title: "Realtime-Bench"
type: concept
created: 2026-11-03
updated: 2026-11-03
tags:
  - benchmark
  - evaluation
  - ai-agents
  - agent-evaluation
  - real-time
  - arxiv
sources:
  - https://arxiv.org/abs/2610.22155
  - raw/newsletters/2026-11-02-import-ai-479-spacewar-low-latency-tasks-versus-llms-genie-4.md
related:
  - concepts/ai-benchmarks/androidworld
  - concepts/ai-benchmarks/agentdojo
  - concepts/ai-benchmarks/webarena
  - concepts/inference-speed-development
confidence: medium
---

# Realtime-Bench

**Realtime-Bench** is a benchmark for evaluating whether general-purpose AI systems can act
under **strict temporal constraints** — tasks where a delayed action directly changes the
outcome. Introduced in arXiv 2610.22155 (submitted 2026-10-15) by researchers at UT Austin,
Ohio State, UIUC, NVIDIA, Northwestern, and Steadyworks, its headline finding is that
frontier models are still bad at low-latency work: **best success rate ~44% and best Pass^3
only 36% under Wall Clock**, versus ~70–80% for the same high-reasoning models when the clock
is paused.

**Paper**: [Realtime-Bench: Can Frontier Models Solve Real-time Interactive Problems?](https://arxiv.org/abs/2610.22155)
**Leaderboard**: [realtimeagents.org](https://realtimeagents.org)
**First surfaced here via**: Import AI 479 (Jack Clark, 2026-11-02)

## The gap it fills

Existing "real-time" evaluations of streaming models measure *conversational quality* and
*streaming perception* — but never whether an agent can **act** in time. Realtime-Bench
targets the missing axis: effective action under temporal pressure. Jack Clark's framing in
Import AI 479: it is "an effective proxy for where AI agents will break — the low scores here
point to tasks where AI agents cannot yet be expected to perform well."

## Task suite (50 tasks)

| Group | Count | Categories |
|---|---|---|
| Web tasks | 30 | travel, e-commerce, service, security |
| Game tasks | 20 | arcade, puzzle, strategy, simulation |

## Three measured capabilities

1. **RT-Perceive** — *temporal state awareness*: using observations to track how the world is
   changing (e.g. is this ticket still actually available?).
2. **RT-Deliberate** — *adaptive deliberation*: altering reasoning length/depth according to
   the time budget remaining (stop thinking when the purchase window is closing).
3. **RT-Act** — *time-aware action selection*: timing the action itself appropriately (wait
   for the sale vs. buy now while stock lasts).

## Three clock conditions

| Condition | What it does | Purpose |
|---|---|---|
| **Wall Clock** | Environment advances with actual inference latency | Real-world performance |
| **Paused Clock** | Inference delay removed entirely | Idealized baseline capability |
| **Token Clock** | Advances simulated time at a fixed rate per generated token; the action applies at the simulated time reached when committed | Isolates temporal awareness from physical serving speed — burning tokens delays execution regardless of hardware |

The Wall-Clock-vs-Paused-Clock gap (36% → ~70–80%) is the paper's core evidence: **the
capability is largely there, the timing discipline is not**. Higher reasoning effort has
*mixed* effects under time pressure — more thinking can mean a missed window, a direct
quality-vs-timeliness trade-off.

## Models evaluated

OpenAI (GPT-6-Astra, GPT-5.6 Sol, GPT-Realtime-2, OpenAI Decisions), Anthropic (Claude Fable 5.1,
Claude Opus 5), Google (Gemini 3.8 Flash, Gemini 3.1 Flash Live, Gemini 3.8 Live), Jev 1.13, plus
Chinese models DeepSeek V4.1 and Moonshot Kimi-K3. Per Import AI 479, **GPT-6 Astra (high)**
topped the Wall Clock pass-rate table at **36%** (the paper abstract reports best success 44% /
best Pass^3 36%, so the "36%" headline is the Pass^3 figure).

## Why it matters

- **Deployment boundary map**: low scores localize the class of agent work — auctions, flash
  sales, live games, any first-come-first-served action — where current agents should *not* be
  trusted unattended.
- **Token Clock is a novel control**: by charging simulated time per token, it separates
  "the model doesn't understand time" from "the model thinks too long." This makes verbose
  chain-of-thought itself a *temporal cost*, a distinct failure mode from accuracy errors.
- **Latency is a first-class capability axis**, alongside the speed-is-usability argument made
  from the practitioner side in [[concepts/duet-style-hierarchical-assistant]] (Claude Duet's
  consistent last-place speed in Claire Vo's nine-task personal-agent benchmark) and
  [[concepts/inference-speed-development]].

## Caveats

- Single paper, single leaderboard; no independent replication yet (`confidence: medium`).
- Game/web task curation is subjective ("carefully curated dynamic tasks") — coverage of real
  economic time-pressure scenarios is unproven.
- Model naming follows Import AI 479's text (e.g. "GPT-6-Astra", "Jev 1.13"); verify exact
  model strings against the paper's tables before quoting scores.

## Related pages

- [[concepts/ai-benchmarks/androidworld]] — GUI agent benchmark without temporal pressure
- [[concepts/ai-benchmarks/agentdojo]] — agent benchmark comparison
- [[concepts/inference-speed-development]] — latency as a capability driver
- [[concepts/duet-style-hierarchical-assistant]] — practitioner-side speed findings
- [[entities/nvidia]] — co-author institution
