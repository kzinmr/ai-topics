---
source_url: https://arxiv.org/abs/2609.34649
ingested: 2026-09-30
sha256: 851279d0ba7295e777cf7fdfc6418f6670da9eb96419b0a026eeca6d7f3fab78
---

# Beyond Skill Evolution: Self-Evolving Context Management Policies for Long-Horizon Agent Harnesses

**arXiv:** 2609.34649v1  
**Published:** 2026-09-28  
**Primary category:** cs.AI  
**Authors:** Weiyuan Li, Jinghan Xu, Aili Chen, Xintao Wang, Shuang Liang, Jiaqing Liang, Deqing Yang

## Abstract

Harness evolution improves LLM agents by learning from execution trajectories, but existing experience- and skill-based methods are less effective on long-horizon tasks. As interactions grow, useful evidence can be buried by redundant or outdated context, making context management itself a key bottleneck. We introduce ContextEvo, a framework that learns a context policy from long-horizon trajectories. ContextEvo reconstructs the model-visible context at key decision points, identifies context-related failures, and applies targeted policy updates. Starting from the open-source Pi-agent harness, ContextEvo improves performance across three long-horizon task benchmarks, achieving results comparable to or better than several prominent agent harnesses, including Codex, OpenCode, and OpenClaw. Additional analyses show that fixed or locally evolved context strategies can fall short under long-horizon information pressure, while our methods adapt to the information demands of each environment.
