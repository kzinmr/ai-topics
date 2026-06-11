---
title: "RULER: Easy Mode for RL Rewards"
author: Kyle Corbitt
date: 2025-07-11
source_url: https://corbt.com/posts/ruler
type: article
tags:
  - reinforcement-learning
  - reward-function
  - llm-as-judge
  - grpo
  - openpipe
  - art
  - evaluation
---

# RULER: Easy Mode for RL Rewards

**Author:** Kyle Corbitt
**Date:** July 11, 2025
**Source:** https://corbt.com/posts/ruler

---

Introduces RULER (Relative Universal LLM-Elicited Rewards), a general-purpose reward function for GRPO that requires no labeled data, no hand-crafted reward functions, and no human feedback.

## Core Insight

1. **Ranking multiple solutions side-by-side is easier than scoring them in isolation** — LLMs struggle with absolute scoring (no shared calibration), but excel at comparison tasks
2. **GRPO only needs relative scores within each group, not absolute calibration** — whether the best trajectory scored 0.9 or 0.3 doesn't matter; GRPO only needs the relative ordering

## Benchmarks

Benchmarks on 4 tasks (ART-E, Reasoning Classifier, Voice Ordering, Customer Support Agent) show RULER-trained Qwen 2.5 models outperform OpenAI o3 on 4/4 tasks and outperform hand-crafted reward functions on 3/4.

## Key Findings

- RULER often converges faster than hand-tuned baselines
- Cheaper judge models (Qwen3 32B) often work well
- Group size of 4-8 trajectories recommended
- Common prefix deduplication is automatic
- Judge responses cached to disk for debugging

## Open Source

RULER is open-sourced in the ART framework. Available as `art.rewards.ruler()` (low-level) and `art.rewards.ruler_score_group()` (high-level).
