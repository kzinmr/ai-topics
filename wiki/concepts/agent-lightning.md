---
title: "Agent Lightning (Microsoft)"
created: 2026-08-26
updated: 2026-08-26
type: concept
tags: [microsoft, reinforcement-learning, agentic-rl, agent-training, coding-agents, open-source]
sources:
  - raw/articles/2026-08-24_microsoft-agent-lightning-v1.md
  - https://github.com/microsoft/agent-lightning
  - https://arxiv.org/abs/2608.17528
---

# Agent Lightning (Microsoft)

**Agent Lightning** is Microsoft's open-source (MIT) framework for training AI agents with **reinforcement learning while they run inside their real, unmodified harnesses**. v1.0 (complete refactor; v1.0.1 released **Aug 24, 2026**, HN: 55 pts) is pitched as a "**3,500-line lightweight agentic RL framework**" where simplicity is "the first principle." Technical report: arXiv:2608.17528, "Agent Lightning v1.0: Towards Harnessed Agentic RL" (He, Zhang, Zhou et al., Aug 19, 2026). The original paper (arXiv:2508.03680, Aug 2025) established the core idea: train *any* AI agent with RL with almost zero code changes.

## Core idea: harnessed agentic RL

Agents interact with the model through an Agent Lightning **proxy (API Gateway)** with **zero changes** to the agent code — tools, context, control flow, and environments stay in the loop. The agent keeps running in its real harness (CLI agent, AutoGen flow, MCP-based agent, etc.); the framework observes the interaction stream and turns it into RL training data.

## Architecture (3 components)

- **Trainer** — runs `verl` + vLLM, builds training samples, updates the policy
- **API Gateway** — proxies model requests (OpenAI-compatible) and captures training data; returning token IDs through the API avoids retokenization drift (a known agent-RL failure mode, see vLLM blog, Oct 2025)
- **Rollout Controller** — runs agents locally or **as native Kubernetes Jobs** (no external sandbox service required)

Installation is a `uv sync` + `setup_verl.sh` on a CUDA machine.

## Headline result

End-to-end **coding-agent training example**: with only **6K training samples**, a **Qwen3.5-9B** agent improves **SWE-bench Verified from 41.8% → 56.4% (+14.6 pp)**. The full pipeline is released, including data cleaning, **reward-hacking prevention**, and training scripts. Evaluated domains: Search-R1 (multi-turn retrieval + reasoning), LLM-in-Sandbox (computer + code execution), and Coding Agent (repository tests as reward).

## Examples shipped

Calc-X (math POC, 1 GPU, AutoGen + MCP calculator tools), GSM8K, ScienceWorld, Search-R1, LLM-in-Sandbox, Coding Agent.

## Ecosystem

- **Youtu-Agent** (Tencent) — built on a modified Agent Lightning branch; claims stable 128-GPU RL scaling on maths/code/search
- **AgentFlow** (Stanford) — planner/executor/verifier/generator multi-agent system using Flow-GRPO for long-horizon sparse-reward tasks
- **DeepWerewolf** — agent-RL case study for the Werewolf game (AgentScope + Agent Lightning)

## Positioning

Agent Lightning occupies the "**train the agent, not just the model**" niche: rather than distilling SFT data or fine-tuning a base model in isolation, it applies RL to the full agentic loop (tool calls, environment feedback, multi-turn trajectories). The ~3,500-line footprint and Kubernetes-native rollouts make it a lightweight alternative to heavier RL stacks; the proxy design means existing agent codebases (including commercial CLI harnesses) can become trainable without modification.

## Related

- [[concepts/post-training/reinforcement-learning]] — RL fundamentals
- [[concepts/coding-agents/coding-agents]] — coding agents as the primary trained workload here
- [[concepts/agent-harnesses]] — the harnesses Agent Lightning plugs into
- [[concepts/self-evolving-agents]] — adjacent: agents that improve themselves, but via reflection/memory rather than weight updates
- [[concepts/multi-agents/multi-agent-systems]] — multi-agent training context
- [[concepts/sandbox]] — sandboxing alternatives (Agent Lightning uses native K8s Jobs)
- [[entities/microsoft]] — company

Raw source: [[raw/articles/2026-08-24_microsoft-agent-lightning-v1]]
