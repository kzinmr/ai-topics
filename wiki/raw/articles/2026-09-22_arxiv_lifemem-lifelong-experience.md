---
source_url: https://arxiv.org/abs/2609.12655
ingested: 2026-09-22
sha256: e4687a2fff55a1c3e4083a6955915c0022249041ab1ece72de02e8df880edb0b
---

# LifeMem: Enabling Lifelong Experience Reuse for LLM Agents

**arXiv:** 2609.12655v1 (cs.CL) — submitted 2026-09-11
**Authors:** Yuli Qiu, Yutong Li, Wei Su, Zeming Liu, Wanxiang Che, Heyan Huang, Haifeng Wang, Yuang Guo
**Abstract URL:** https://arxiv.org/abs/2609.12655

## Abstract

Large language model agents are expected to continuously adapt to new tasks and environments over their lifetime by reusing past experience. However, existing memory-based agents struggle to transfer reusable experience across environments and suffer from catastrophic forgetting as experience accumulated. To address these challenges, we propose LifeMem, a lifelong learning framework that enables agents to transfer knowledge across multiple environments. During learning, LifeMem clusters accumulated interaction trajectories based on underlying workflows to extract reusable skills. When solving a new task at inference time, the agent recalls relevant skills and trajectories to guide actions. To validate our method, we conduct experiments across 10 environments and over 13k tasks with 2k newly annotated interaction trajectories. Results show that LifeMem enables effective experience reuse in lifelong learning, achieving both reduced forgetting on learned tasks and superior cross-task transfer. Further analysis reveals that task streaming impacts learning, while consolidating structurally similar trajectories within memory boosts performance.
