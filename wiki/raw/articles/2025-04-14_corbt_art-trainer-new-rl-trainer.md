---
title: "ART Trainer: A New RL Trainer for Agents"
author: Kyle Corbitt
date: 2025-04-14
source_url: https://corbt.com/posts/art-trainer-a-new-rl-trainer-for-agents
type: article
tags:
  - reinforcement-learning
  - agents
  - grpo
  - openpipe
  - art
  - training
  - fine-tuning
---

# ART Trainer: A New RL Trainer for Agents

**Author:** Kyle Corbitt
**Date:** April 14, 2025
**Source:** https://corbt.com/posts/art-trainer-a-new-rl-trainer-for-agents

---

The article announces **Agent Reinforcement Trainer (ART)**, a reinforcement learning framework by OpenPipe for training LLM-based agents using GRPO (and PPO in the future). It's an early alpha focused on best-in-class training efficiency and agentic multi-turn support.

## Motivation — Three Limitations of Existing Frameworks

1. **Multi-turn roll-outs**: Existing trainers focus on single-turn interactions, insufficient for agentic flows.
2. **GPU efficiency**: GPUs are often idle during rollout when agents take real-world actions (web navigation, form submission, etc.).
3. **Integration with existing codebases**: Existing RL pipelines require significant refactoring; agents are embedded in complex codebases using frameworks like CrewAI, Mastra, or OpenAI Agents SDK.

## Architecture Innovations

1. **Separate backend and frontend** — Frontend (user-defined rollouts/rewards) and backend (LLM inference/training) can run on separate machines. Frontend lives locally; backend runs on cloud GPU.
2. **OpenAI-compatible inference endpoints** — Uses vLLM for inference, TRL + Unsloth for training. Offloads vLLM's KV cache to CPU memory during training, saving ~4GB VRAM for 7B models, enabling training on Google Colab's free tier.

## Early Results

- HN title generation (SOTA model for upvotes)
- 2048 game (multi-turn rollouts, Qwen 7B)
- Tic-tac-toe (7B model surpasses GPT-4o)
- Temporal Clue (14B model surpasses most frontier models)

## FAQs

Cover: how it works (GRPO-based), why separate frontend/backend, requirements for using ART (30%+ success rate baseline, verifiable rewards, runnable without real-world side effects), open-source commitment, cost ($15–$200 per training run), production feedback training (reward model recommended), and non-agentic use cases.
