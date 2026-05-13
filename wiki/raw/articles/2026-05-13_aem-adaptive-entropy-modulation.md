---
title: "AEM: Adaptive Entropy Modulation for Multi-Turn Agentic Reinforcement Learning"
source_url: https://arxiv.org/abs/2605.00425
date: 2026-05-13
type: paper
arxiv_id: "2605.00425"
authors: [Haotian Zhao, Songlin Zhou, Yuxin Zhang, Stephen S.-T. Yau, Wenyu Zhang, Lun Tian, Tianshu Zhu, Yifeng Huang, Yucheng Zeng, Jingnan Gu, Daxiang Dong, Jianmin Wu]
affiliations: [Baidu, Tsinghua University]
submitted: 2026-05-01
revised: 2026-05-08
tags: [reinforcement-learning, agent-training, optimization, training]
---

# AEM: Adaptive Entropy Modulation for Multi-Turn Agentic Reinforcement Learning

**Authors**: Haotian Zhao, Songlin Zhou, Yuxin Zhang, Stephen S.-T. Yau, Wenyu Zhang, Lun Tian, Tianshu Zhu, Yifeng Huang, Yucheng Zeng, Jingnan Gu, Daxiang Dong, Jianmin Wu (Baidu & Tsinghua University)

**30 pages, v3 (May 8, 2026)**

## Abstract

Reinforcement learning (RL) has substantially improved the ability of large language model (LLM) agents to interact with environments and solve multi-turn tasks. However, effective agentic RL remains challenging: sparse outcome-only rewards provide limited guidance for assigning credit to individual steps within long interaction trajectories.

Existing approaches often introduce dense intermediate supervision, such as process reward models or auxiliary self-supervised signals, which increases supervision and tuning complexity and may limit generalization across tasks and domains.

AEM is a **supervision-free credit assignment method** that adaptively modulates entropy dynamics during RL training to improve the exploration-exploitation trade-off.

### Key Innovation: Response-Level Entropy

Since in agentic RL the environment is typically affected by a complete response (not individual tokens), AEM lifts entropy dynamics from the token level to the **response level**, aligning uncertainty estimation with the effective action granularity of LLM agents and reducing sensitivity to token-level sampling noise.

### How It Works

Entropy drift under natural-gradient updates is governed by the interaction between the sampled-response advantage and its relative surprisal. AEM derives a practical response-level uncertainty proxy and uses it to rescale advantages, leveraging the evolving balance between positive and negative samples to naturally transition from exploration to exploitation.

## Results

Extensive experiments on ALFWorld, WebShop, and SWE-bench-Verified with models ranging from 1.5B to 32B demonstrate that AEM consistently improves strong RL baselines:

- **+1.4%** gain when integrated into a state-of-the-art software-engineering RL training framework
- Consistent improvements across environments from 1.5B to 32B models

## Significance

AEM is a supervision-free method — no process reward models, no auxiliary supervision signals needed. This makes it simpler to deploy and more generalizable across tasks and domains compared to existing credit assignment approaches.

Source: arXiv:2605.00425
