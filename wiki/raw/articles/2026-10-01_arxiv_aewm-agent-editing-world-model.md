---
source_url: https://arxiv.org/abs/2609.28416
arxiv_id: 2609.28416
ingested: 2026-10-01
sha256: 1eaaaf65c0d9f9bf2abf45adcd93a5a3e1329585c0a55b79e08f2c97e7a65f87
---

# Agent-Editing World Model: Rethinking World Modeling for LLM Agents

arXiv:2609.28416v1 (cs.CL, cs.AI, cs.LG), submitted 2026-09-23.
Authors: Shuang Sun, Guoxin Chen, Fanzhe Meng, Jia Deng, Huatong Song, Jinhao Jiang, Wayne Xin Zhao, Hongteng Xu, Ji-Rong Wen.

## Abstract

Recent advances in large language models (LLMs) have enabled agents to tackle long-horizon tasks across diverse environments. To further improve agent performance, existing language world models typically predict environment observations, yet reconstructing high-entropy, execution-dependent tool responses offers limited value when real feedback is available. Meanwhile, agents suffer from task-state contamination, where unsupported assumptions and outdated plans persist in history and distort subsequent decisions.

We propose the Agent-Editing World Model (AEWM), which models how reasoning and actions shape future task progress rather than simulating tool responses. AEWM combines Action Judge to distinguish Critical, Exploratory, and Noisy decisions with State Revision to edit noisy reasoning-action continuations from the same observed history. EditAct integrates these capabilities with real execution, directly changing the state underlying subsequent decisions rather than merely providing critiques.

We train AEWM across Search, Terminal, and Software Engineering through mid-training and supervised fine-tuning. AEWM achieves 70.5% macro-F1 on our Action Judge benchmark, exceeding the strongest frontier baseline by 10.6 points. Across six benchmarks and three agent backbones, EditAct improves average scores by 3.2-6.7 points over the strongest baseline. Furthermore, rejection sampling fine-tuning on verified EditAct trajectories, termed AEWM-RFT, improves over Self-RFT by 2.2-2.6 points across three domains without online AEWM guidance.
