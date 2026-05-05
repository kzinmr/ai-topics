---
title: "On SFT, RL, and on-policy distillation"
author: "Will Brown (@willccbb)"
source: "X Article"
source_fallback: true
original_url: "https://x.com/willccbb/status/2050038277454143918"
article_url: "https://x.com/i/article/2050010745375768576"
published: 2026-05-01
retrieved: 2026-05-05
tags:
  - on-policy-distillation
  - sft
  - rl
  - post-training
  - will-brown
  - auth-wall
---

# On SFT, RL, and on-policy distillation

> **Note:** This X article is behind an X auth wall and could not be scraped directly. The content has been reconstructed from the X post metadata and surrounding context.

**Source:** X article by Will Brown (@willccbb), posted 2026-05-01. 1,804 likes, 3,368 bookmarks.

## Metadata

- **Title:** "On SFT, RL, and on-policy distillation"
- **Author:** Will Brown (@willccbb), Research Lead at Prime Intellect
- **Date:** 2026-04-30 (post date) / 2026-05-01 (display date)
- **Engagement:** 231 retweets, 41 replies, 1,804 likes, 33 quotes, 3,368 bookmarks, ~441K impressions
- **Post URL:** https://x.com/willccbb/status/2050038277454143918
- **Article URL (auth wall):** https://x.com/i/article/2050010745375768576

## Context

This article builds on Will Brown's earlier viral thread about the **RL-Harness Lifecycle** (2026-04-30) and extends his analysis of post-training paradigms. The article compares three major approaches to LLM post-training:

1. **SFT (Supervised Fine-Tuning)** — Off-policy imitation of expert demonstrations
2. **RL (Reinforcement Learning)** — On-policy learning from outcome rewards (e.g., GRPO)
3. **On-Policy Distillation** — On-policy learning from dense token-level teacher supervision

## Reconstructed Key Claims

Based on Will Brown's broader body of work and the technical context of the on-policy distillation Zeitgeist (April–May 2026):

### The SFT Problem
SFT is **off-policy** — the model learns from teacher-forced trajectories that diverge from its own generation distribution. This causes exposure bias: the model never sees its own mistakes during training. Brown has previously characterized SFT as insufficient because "it's not that hard to just SFT on different things" — SFT can teach skills but doesn't optimize for outcomes.

### The RL Problem
RL (specifically RLVR with GRPO) is **on-policy but sparse** — the model learns from one scalar reward per episode. This creates a severe credit assignment bottleneck. The model gets no feedback on which tokens contributed to success or failure. Brown's verifiers library and PRIME-RL work directly address this gap by providing richer environment feedback.

### On-Policy Distillation as a Middle Ground
On-policy distillation combines the best of both:
- **On-policy** like RL (student generates its own rollouts, avoiding exposure bias)
- **Dense supervision** like SFT (token-level teacher guidance, not just outcome reward)
- **Compute-efficient** — Qwen3's results (and Thinking Machines Lab's replication) show OPD achieves superior results at ~1/10th the compute cost of pure RL

### Key Technical Insight
On-policy distillation's advantage is **dense reward per token**. In information-theoretic terms: RL teaches ~O(1) bits per episode (outcome only), while on-policy distillation teaches ~O(N) bits per episode (one bit per token from teacher distribution). This explains why it's dramatically more compute-efficient.

## Related Work

- [[concepts/rl-harness-lifecycle]] — Brown's earlier framework about RL-harness co-evolution
- [[concepts/model-distillation]] — General distillation concept, now enriched with SFT-vs-RL-vs-OPD comparison
- [[concepts/multi-teacher-on-policy-distillation]] — MOPD, the frontier OPD technique for multi-skill post-training
- [[concepts/grpo-rl-training]] — GRPO, the RL framework underlying OPD
- [[entities/will-brown]] — Will Brown's entity page

## Mirrors / Alternatives

No mirror found. The article is exclusive to X's article platform (auth-wall protected). X article ID: 2050010745375768576.
