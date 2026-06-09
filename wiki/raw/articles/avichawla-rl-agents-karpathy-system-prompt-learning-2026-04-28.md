---
title: "How top AI labs are building RL agents in 2026 (using Karpathy's system prompt learning idea)"
author: Avi Chawla (@_avichawla)
source_url: https://x.com/_avichawla/status/2049037299334472015
article_url: https://x.com/i/article/2048280670825496576
date: 2026-04-28
type: x_article
topics: [RL, RLHF, GRPO, RULER, system-prompt-learning, reward-function, agent-training, OpenPipe-ART]
metrics:
  likes: 396
  bookmarks: 1025
  retweets: 77
  impressions: 512662
---

# How top AI labs are building RL agents in 2026 (using Karpathy's system prompt learning idea)

**Author:** Avi Chawla (@_avichawla)
**Date:** 2026-04-28
**Engagement:** 1,025 bookmarks, 396 likes, 512K impressions

## Summary

This X Article traces the evolution of reinforcement learning for LLMs — from RLHF to DeepSeek R1's RLVR (Reinforcement Learning with Verifiable Rewards) to RULER (OpenPipe's ART framework) — arguing that Anthropic, OpenAI, and DeepSeek are converging on a single idea: **using the system prompt as the reward function**.

## Key Concepts

### 1. RLHF → RLVR → RULER Evolution

- **RLHF (2022, OpenAI InstructGPT):** Human rankings → reward model → PPO fine-tuning. Required 4 full-size models in memory (policy, reference, critic, reward model).
- **RLVR (Jan 2025, DeepSeek R1):** Rule-based verification (math answers, code compilers). GRPO removed critic model entirely, collapsing 4 models to 2. R1-Zero went from 15.6% to 77.9% on AIME 2024.
- **RULER (2026, OpenPipe ART):** LLM-as-judge scores trajectories relative to each other using the system prompt as implicit evaluation criteria.

### 2. The Problem: Non-Verifiable Tasks

RLVR works for math/code (deterministic verification), but most agent workflows (RAG, customer support, summarization) have no deterministic verifier. Custom reward functions are brittle, hard to debug, and need rewriting when the system prompt changes.

### 3. Karpathy's "System Prompt Learning" Idea

The article states:

> "He argued in 2025 that we're missing a major learning paradigm for LLMs, something he tentatively called 'system prompt learning.' The core idea is that the system prompt carries a richer signal than a scalar reward, and RL training should be finding ways to leverage that signal rather than relying solely on hand-crafted reward functions."

**Note on sourcing:** The article references this as Karpathy's 2025 idea but does not provide a specific tweet URL or blog post link. Karpathy's RSS feed (via fxtwitter.com) does not contain a tweet explicitly using the term "system prompt learning." This framing appears to be Avi Chawla's interpretation/summary of Karpathy's broader arguments about RL and LLM training, possibly drawing from:
- Karpathy's Sequoia Ascent 2026 fireside chat (2026-04-30): discusses verifiability as the key property enabling RL for coding/math, and the gap for non-verifiable domains
- Karpathy's April 2026 tweet on AI capability gap: "these domains offer explicit reward functions that are verifiable meaning they are easily amenable to reinforcement learning training"
- Karpathy's general advocacy for system prompts as rich instructional specifications (seen in his LLM Wiki work and "install .md skills" concept)

The term "system prompt learning" as a named concept does not appear to originate from a specific Karpathy tweet or blog post — it may be Avi Chawla's coinage to describe the convergence he observes.

### 4. RULER (OpenPipe ART Framework)

- **Repo:** https://github.com/OpenPipe/ART (9k+ stars)
- **How it works:**
  1. Generate N trajectories per scenario (4-8)
  2. LLM judge reads system prompt + all trajectories
  3. Judge scores each trajectory 0-1 relative to others
  4. GRPO normalizes within groups for training signal
- **Key insight:** Relative scoring is easier than absolute scoring for LLMs; GRPO only needs relative ordering anyway
- **Practical details:** Works with cheaper models (Qwen3 32B), deduplicates common prefixes, caches judge responses

### 5. Lab Convergence

- **Anthropic:** Constitutional AI — principles document replaces human evaluators
- **OpenAI:** "Universal Verifiers" — extending RL beyond math/code into biology, medicine, general knowledge
- **DeepSeek:** RLVR + GRPO as the foundation

## Code Examples (from article)

The article includes 12 Python code snippets demonstrating:
- Trajectory/TrajectoryGroup construction
- `ruler()` low-level scoring API
- `ruler_score_group()` high-level API
- Custom rubrics in natural language
- Full training loop with `art.gather_trajectory_groups`

## Sources Referenced

- OpenPipe ART: https://github.com/OpenPipe/ART
- DeepSeek R1 (Jan 2025)
- OpenAI InstructGPT / RLHF (2022)
- Anthropic Constitutional AI
