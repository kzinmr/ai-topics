---
title: "RAO: Recursive Agent Optimization — X Thread by Apurva Gandhi"
source: "X/Twitter"
source_url: "https://x.com/apurvasgandhi/status/2052831719263461722"
author: "Apurva Gandhi (@apurvasgandhi)"
date: "2026-05-08"
scraped: "2026-05-11"
tags: [ai-agents, reinforcement-learning, inference-time-scaling, recursive-agents, rao]
type: raw-article
---

# RAO: Recursive Agent Optimization — X Thread Summary

Thread by [@apurvasgandhi](https://x.com/apurvasgandhi) on May 8, 2026.

## 1/10 — Introduction
Sub-agents are a promising inference-time scaling primitive:
- Expand an agent's working memory
- Divide-and-conquer hard problems
- Solve problems faster with parallel execution

But how do we train a model to best take advantage of sub-agents and make sure we get these benefits?

Very excited to release **RAO: Recursive Agent Optimization**. RAO is an end-to-end reinforcement learning approach for training LLM agents to spawn, delegate to, and coordinate with recursive copies of themselves (that can themselves spawn other agents) — turning recursive inference into a learned capability.

## 2/10 — Credit Assignment
RAO leverages the recursive rollout structure to provide **structured, dense credit assignment** per sub-task trajectory (via environment feedback when available or an LLM-judge proxy). Agents at each node in the tree are rewarded locally for their own sub-task success and globally for contributions to the root task.

## 3/10 — Multi-Task Objective
RAO's training objective can be thought of as a **multi-task objective** with tasks sampled from different levels on the recursive rollout execution trees. Tasks at deeper levels tend to be easier sub-problems than parent tasks higher up the tree. In this way, RAO provides a natural curriculum.

## 8/10 — Results
In just **75 steps** of training Qwen3-4B-Instruct on deep research, recursive agents beat the trained single agent baseline by **16% SR** (success rate).

## 9/10 — Adaptive Compute
Recursive agents trained with RAO adapt inference-time compute based on the difficulty of the problem; e.g., the max recursive depth reached by trajectories goes higher as problems become more difficult.

## 10/10 — Release
Project Webpage (code will be released soon!): https://apga.github.io/RAO
Paper: https://arxiv.org/abs/2605.06639

Huge thanks to collaborators Satyaki Chakraborty, XJ Wang and advisors Aviral Kumar, Graham Neubig.

## Notable Replies
- **@rosinality** (RT'd): "Recursively delegating subtasks to subagents by spawning themselves. And generalization across the recursion depth was possible."
- **@williamjurayj**: Asked about incentivizing parallelism. Apurva: "we found prompting was enough with the Qwen-Instruct models on the domains we experimented on"
- **@trydotworks**: Apurva: "You could use RAO to train agents that are better at using this :)"
