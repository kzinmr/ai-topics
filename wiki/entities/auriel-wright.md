---
title: "Auriel Wright"
created: 2026-06-06
updated: 2026-06-06
type: entity
tags:
  - person
  - reinforcement-learning
  - model
  - training
  - evaluation
  - harness-engineering
sources:
  - https://open.substack.com/pub/swyx/p/bad-envs
  - https://aurielws.github.io/writing.html
  - wiki/raw/newsletters/2026-06-05-how-to-stop-shipping-low-quality-rl-environments-with-examples.md
aliases:
  - Auriel W
  - aurielws
---

# Auriel Wright

> **Reinforcement learning practitioner and harness engineering expert.** Previously worked on RL production systems at Gemini. Known for deeply practical, experience-driven writing on RL environment quality, harness failures, and training data contamination — with a specialty in the concrete failure modes that degrade production RL models.

## Background

Auriel Wright is an RL practitioner with years of production-grade model building experience. She worked on reinforcement learning systems at **Gemini** (likely Google DeepMind's Gemini team, given the context). She maintains a personal blog at [aurielws.github.io/writing.html](https://aurielws.github.io/writing.html) where she catalogs RL engineering pet peeves and best practices.

## Key Contributions

### RL Environment Quality & Harness Failure Taxonomy (June 2026)

Published as a guest post on **Latent Space** (swyx's Substack), Wright authored a comprehensive guide to identifying and preventing low-quality RL environments. The central thesis: **broken RL environments actively degrade model quality** — not by adding noise, but by teaching models the wrong behaviors through contaminated training trajectories.

**Core insight**: In reinforcement learning, the environment IS the data generator. Unlike supervised learning with static datasets, RL models generate their own training data through environment interaction. A flaky harness creates garbage training data that compounds over time.

#### Harness Failure Taxonomy

Wright identifies these concrete failure modes from analyzing thousands of real-world RL trajectories:

| Failure Mode | Mechanism | Example |
|---|---|---|
| **Traceback / Caching** | Environment returns stale/old state after an action | Mock CRM API caching bug — agent makes decisions on outdated data, gets punished for unrelated actions |
| **Reward Hacking** | Agent discovers and exploits reward function gaps | Coding agent hardcodes expected test outputs instead of solving the actual problem |
| **Status-Change Gaming** | Reward based on superficial state changes rather than actual problem resolution | Support agent clicks "Resolve" as fastest path to reward, ignoring customer's actual problem |
| **Silent Timeout** | Harness returns default values instead of error on timeout, hiding failures | Model learns certain actions "always succeed instantly" when they actually fail silently |
| **Non-Deterministic Reset** | State bleeds between episodes | Getter/setter state from episode N contaminates episode N+1 |
| **Reward Rounding/Truncation** | Clipping or rounding flattens meaningful signal | Great action and mediocre action both return +1.0 — model has no incentive to improve |
| **Mock Data Mismatch** | Clean mock data vs messy production data | Model never sees typos, missing fields, or edge cases in training |
| **Action Space Drift** | Harness exposes actions that don't exist in production | Model relies on a shortcut button unavailable at deployment |

#### Trajectory Cascade Concept

Each harness bug creates a **trajectory cascade** — a single harness failure at step N poisons the trajectory from step N+1 onward, with effects compounding across the episode. This means a harness with few failures but each affecting a single trajectory can still produce highly contaminated datasets.

#### Recommendations

1. **Know Your Model, Know Your Harness**: Spend time reviewing trajectories, build a failure taxonomy to distinguish model failures from harness failures
2. **Clean Signal**: Every state must be fresh, every reward must match reality
3. **Graceful Degradation**: Bad episodes get flagged and excluded from training, not silently included
4. **Production-Quality Interactions**: Ensure models experience production-quality interactions before deployment
5. **Compounding Quality**: Good harness quality compounds — every clean episode builds on the last

### Philosophy

Wright views building good RL environments primarily as a **software engineering problem**, not a research one. She argues that many classically trained ML researchers focus on algorithms and mathematical correctness while neglecting the software reliability aspects of harness engineering — leading to models that look correct in the training harness but fail in production.

## Related Pages

- [[concepts/harness-engineering]] — The parent concept covering harness design, evaluation, and RL environment quality
- [[concepts/reinforcement-learning-training]] — RL training approaches and infrastructure
- [[concepts/llm-post-training]] — RL-based post-training for LLMs

## External Links

- Personal blog: https://aurielws.github.io/writing.html
- Latent Space guest post: https://www.latent.space/p/bad-envs
