---
title: "Agent Lightning v1.0: Towards Harnessed Agentic RL (microsoft/agent-lightning)"
url: https://github.com/microsoft/agent-lightning/releases/tag/v1.0.1
date: 2026-08-24
fetched_at: 2026-08-26
source: github.com/microsoft/agent-lightning (official release + README)
secondary_sources:
  - https://arxiv.org/abs/2608.17528
  - https://microsoft.github.io/agent-lightning/stable/
tags: [microsoft, reinforcement-learning, agentic-rl, agent-training, coding-agents, open-source, swebench]
---

# Agent Lightning v1.0.1 (Microsoft, GitHub release)

Agent Lightning was completely refactored in v1.0. Release v1.0.1 (Aug 24, 2026). Legacy pre-v1.0 releases live on the `v0.x` branch.

Tagline: **"3,500-Line Lightweight Agentic RL Framework for Training Agents with Real Harnesses!"**

MIT License. Technical report: arXiv:2608.17528 "Agent Lightning v1.0: Towards Harnessed Agentic RL" (Zhiyuan He, Siwei Zhang, Zhiwen Zhou, Yuqing Yang, Yu Kang, Yuge Zhang, Luna K. Qiu, Tin Yan Tsui, Jiahang Xu, Chong Luo; Aug 19, 2026).

## Key Features

- **~3,500 lines of code** — "We treat simplicity as the first principle."
- **Train with real agent harnesses**: agents interact with the model through the Agent Lightning v1.0 proxy with **ZERO changes**, while keeping tools, context, control flow, and environments in the loop.
- **Native Kubernetes support**: run agents directly as Kubernetes Jobs without relying on external sandbox services.
- **Full coding agent training example**: using only **6K training samples**, an end-to-end **Qwen3.5-9B** workflow improves **SWE-bench Verified from 41.8% to 56.4%** (+14.6 percentage points). The full pipeline is released, including data cleaning, reward-hacking prevention, and training scripts.

## Installation

```bash
cd <this-repo>
uv sync
bash scripts/setup_verl.sh 0.8.0 cu130
```

(Example on a CUDA 13.0 machine; uses `verl` + vLLM GPU stack.)

## Architecture (3 lightweight components)

Agent Lightning v1.0 keeps the training architecture simple:

- **Trainer** — runs `verl` and vLLM, builds training samples, and updates the policy.
- **API Gateway** — proxies model requests and captures training data.
- **Rollout Controller** — runs agents locally or as Kubernetes Jobs.

The Trainer creates rollouts, the Controller launches agents, and the Gateway turns interactions into training data, while agents continue to run with their real harnesses.

## Results

Evaluated across several practical training domains: **Search R1**, **LLM-in-Sandbox**, and **Coding Agent**. Pure RL delivers substantial improvements across all three domains.

## Documentation

| Section | Content |
|---------|---------|
| Installation | Base environment and `verl` GPU stack |
| Quick Start | Local first run and end-to-end flow |
| Basics | Components, rollouts, events, and trajectories |
| Trainer Configuration | `verl` integration and trace aggregation |
| API Gateway Configuration | Gateway and model proxy settings |
| Controller Configuration | Local and Kubernetes runners |
| Asynchronous Training | Collocated async collection and pause/drain |

## Examples

| Example | Description |
|---|---|
| Calc-X | POC math reasoning example with AutoGen and MCP calculator tools, requiring only one GPU |
| GSM8K | POC grade-school math reasoning example |
| ScienceWorld | Interactive science tasks in a text-based environment |
| Search-R1 | Multi-turn retrieval and reasoning agent |
| LLM-in-Sandbox | General agent with computer and code execution tools |
| Coding Agent | Coding agent trained with repository tests |

## Related Articles & History

- 8/19/2026 — Agent Lightning v1.0: Towards Harnessed Agentic RL (arXiv:2608.17528) technical report
- 12/17/2025 — Adopting the Trajectory Level Aggregation for Faster Training (Agent-lightning blog)
- 11/4/2025 — Tuning ANY AI agent with Tinker x Agent-lightning (Medium, 2 parts)
- 10/22/2025 — No More Retokenization Drift: Returning Token IDs via the OpenAI Compatible API Matters in Agent RL (vLLM blog)
- 8/11/2025 — Training AI Agents to Write and Self-correct SQL with RL (Medium)
- 8/5/2025 — Agent Lightning: Train ANY AI Agents with Reinforcement Learning (arXiv:2508.03680, original paper)
- 7/26/2025 — "We discovered an approach to train any AI agent with RL, with (almost) zero code changes" (Reddit r/LocalLLaMA)
- 6/6/2025 — Agent Lightning — Microsoft Research project page

## Community Projects

- **DeepWerewolf** — case study of agent RL training for the Chinese Werewolf game (AgentScope + Agent Lightning)
- **AgentFlow** (Stanford) — modular multi-agent framework combining planner, executor, verifier, and generator agents with the Flow-GRPO algorithm for long-horizon, sparse-reward tasks
- **Youtu-Agent** (Tencent) — built with a modified Agent Lightning branch; verified up to 128-GPU RL training on maths/code and search with steady convergence; blog: "Stop Wrestling with Your Agent RL: How Youtu-Agent Achieved Stable, 128-GPU Scaling Without Breaking a Sweat"

**HN discussion**: https://news.ycombinator.com/item?id=49400810 (55 points, 9 comments, Aug 24 2026)
