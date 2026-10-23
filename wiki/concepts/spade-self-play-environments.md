---
title: SPADE — Self-Play in Adaptive Synthetic Executable Environments
type: concept
created: 2026-08-25
updated: 2026-10-23
tags:
  - agentic-rl
  - self-play
  - synthetic-data
  - reinforcement-learning
  - self-improving
  - agent-training
sources:
  - raw/articles/2026-08-19_2608.19197_spade-self-play-adaptive-synthetic-environments.md
  - https://arxiv.org/abs/2608.19197
---

# SPADE — Self-Play in Adaptive Synthetic Executable Environments

**SPADE** (Self-Play in Adaptive Synthetic Executable Environments), arXiv:2608.19197 (v1 2026-08-19, v2 2026-08-24; Bo Liu et al.), is a **self-play RL framework for language agents** in which a single LLM plays two roles:

- **Environment Designer** — writes complete, long-horizon training environments as *executable code* (OpenAI Gym-style `reset()`/`step()` interface).
- **Reasoning Agent** — learns to act inside those environments.

## The problem it solves
Existing training-environment pools for language agents (hand-curated, statically synthesized, or frozen-verifier) keep the **goal distribution fixed as the learner scales** — a bottleneck for continuous self-improvement. SPADE generates the environment *by* a model, so the goal pool adapts and expands.

## How it works
- Each environment is a **stateful, multi-turn** Gym-style program.
- **Privileged-hint reward**: the reasoning agent's reward is estimated from the gap between its reward *with* and *without* a "privileged hint" (h) — task-relevant information (e.g. a partial solution) the Environment Designer attaches.
- **Scale**: validated at the 30B scale. The authors tune three Qwen3 backbones — Qwen3-4B-Instruct-2507, Qwen3-8B, Qwen3-30B-A3B-Instruct-2507 — via **GRPO** for 400 rollouts of 25 environments each; Qwen3-30B performs best.

## Why it matters
- A concrete route to **continuous self-improvement / self-play** for agents: the training signal (environments) is itself model-generated and adaptive rather than a static benchmark.
- Ties directly to [[concepts/recursive-self-improvement]] and [[concepts/agent-training]] — environment generation is a new optimization surface alongside reward design.
- Distinct from the **2024 "SPADE" paper** (Shreya Shankar et al. — synthesizing data-quality assertions for LLM pipelines; see [[entities/shreya-shankar]]). Same name, different field.

## Related Pages
- [[concepts/recursive-self-improvement]] — continuous self-improvement
- [[concepts/agent-training]] — training agents
- [[concepts/ai-agent-engineering]] — agent execution environments / harness
- [[concepts/evaluation/ai-evals]] — synthetic data & evals
- [[entities/shreya-shankar]] — (the other "SPADE")

## Sources
- [SPADE: Self-Play in Adaptive Synthetic Executable Environments (arXiv:2608.19197)](https://arxiv.org/abs/2608.19197)
- Code: https://github.com/spade-rl/spade
- Raw article: `raw/articles/2026-08-19_2608.19197_spade-self-play-adaptive-synthetic-environments.md`
- Discussed in Import AI 470 (Jack Clark, 2026-08-24)

## WarcraftSim — self-play RL on a single desktop (Warlock AI / Robin Kahlow, Oct 2026)

A concrete, *low-resource* counterpart to SPADE's "self-play to get good at hard sequential decision-making" thesis. **WarcraftSim** (Warlock AI, by **Robin Kahlow**; curated via True Positive Weekly #183) trains an agent that plays the **full real game of Warcraft III** (2002 RTS, classic ladder map Echo Isles) under the game's own rules against the strongest shipped opponent — the built-in AI on **insane**, the hardest of its three levels. ^[raw/newsletters/2026-10-22-true-positive-weekly-183.md]

**Headline result**: in **three weeks**, the agent went from losing to the *easy* AI to winning **~9 games in 10 (~89% win rate)** against *insane* — trained by **self-play on a single desktop**.

**Key numbers:**
- **89% win rate** vs the insane built-in AI
- **13 ms per step** — small enough to play on an ordinary CPU
- **~840,000 games** in training ≈ **11 years of Warcraft III** played
- Hardware: **1 GPU (RTX 3090) + 16 CPU cores**
- Methods: **reinforcement learning, self-play, behavioral cloning, curriculum learning**
- Code: github.com/RobinKa/warcraftsim

**Why it matters for the self-play-scaling debate**: it is a pointed contrast to datacenter-scale game-playing RL. DeepMind's **AlphaStar** (StarCraft II) trained 12 agents for **44 days on 32 TPUs each**, and **OpenAI Five** (Dota 2) used a datacenter with the game makers' help — both in 2019. Kahlow achieved a strong agent on the *real* game with **one desktop**, on a game "never built for any of this" (fog of war, four races, thousands of simultaneous unit decisions, sparse win/loss reward at the very end). Together with Modal's GPU-scale RL rollouts ([[entities/modal-labs]]), it frames the live question of **how far agent capability can go on small compute** when the environment, reward, and curriculum are well designed — the same design-lever theme as the GRPO reward-design claim in [[concepts/agentic-search]].

### Sources
- [WarcraftSim: Beating Warcraft III's hardest AI with self-play RL on one desktop](https://warlock.ai/blog/warcraftsim-1/) — Robin Kahlow / Warlock AI (Oct 2026). Discovered via True Positive Weekly #183.
