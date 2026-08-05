---
title: Ahmed Awadallah
type: entity
created: 2026-05-26
updated: 2026-08-05
tags:
  - person
  - microsoft
  - reinforcement-learning
  - agent-training
  - agentic-rl
  - world-models
  - ml-research
  - research-lab
sources:
  - raw/papers/2026-05-26_2605.24517_echo-terminal-agents-world-models.md
  - https://arxiv.org/abs/2605.24517
  - https://www.microsoft.com/en-us/research/people/anawadal/
related:
  - "[[entities/microsoft-ai-frontiers]]"
  - "[[concepts/post-training/echo-rl]]"
---

# Ahmed Awadallah

**Ahmed Awadallah** is a Principal Researcher / research manager at **Microsoft Research, AI Frontiers** lab. He leads the team that developed [[concepts/post-training/echo-rl|ECHO]], providing space, GPUs, and research infrastructure for pursuing novel ideas in agent reinforcement learning. His research spans agent RL, GUI/terminal agents, world models, and small language models (Phi series).

- **Affiliation**: Microsoft Research AI Frontiers
- **Role**: Principal researcher / research manager
- **Profile**: [microsoft.com/en-us/research/people/anawadal](https://www.microsoft.com/en-us/research/people/anawadal/)

## Research Focus

- Reinforcement learning for AI agents (agentic RL)
- CLI/terminal agent training and environment modeling
- World models and environment prediction
- GUI agents and web trajectory synthesis (OmniParser, Explorer)
- Small language models (Phi series co-development)
- Agent infrastructure and scaling

## Notable Work

### ECHO: Terminal Agents Learn World Models for Free (2026-05)
Research lead on ECHO, co-authored with [[entities/vaishnavi-shrivastava|Vaishnavi Shrivastava]], [[entities/piero-kauffmann|Piero Kauffmann]], and [[entities/dimitris-papailiopoulos|Dimitris Papailiopoulos]]. Paper: [arxiv.org/abs/2605.24517](https://arxiv.org/abs/2605.24517). ECHO combines GRPO-style policy-gradient loss with an auxiliary loss that trains the policy to predict environment observation tokens, turning terminal feedback into dense supervision. It doubles GRPO pass@1 on TerminalBench-2.0 (Qwen3-8B: 2.70% → 5.17%; Qwen3-14B: 5.17% → 10.79%).

As Dimitris put it: "Thanks to... Ahmed Awadallah for giving us space — and GPUs — to chase ideas like this, even when they start as just a research itch."

### Phi-3 Technical Report (April 2024)
Contributor to the Phi-3 report introducing phi-3-mini, a 3.8B parameter model trained on 3.3T tokens whose performance rivals much larger models — part of Microsoft's small language model research program.

### OmniParser (2024)
Co-author of OmniParser for Pure Vision Based GUI Agent — a screen parsing tool that converts GUI screenshots into structured elements for vision-based agents, widely adopted for computer-use agent development.

### Explorer: Scaling Exploration-driven Web Trajectory Synthesis (Feb 2025)
Co-author of a scalable recipe synthesizing the largest trajectory-level dataset to date — 94K+ successful multimodal web trajectories, 49K unique URLs, 720K screenshots, 33M web elements — and training the Explorer multimodal web agent on it.

## See Also

- [[entities/vaishnavi-shrivastava]] — ECHO lead researcher
- [[entities/dimitris-papailiopoulos]] — ECHO co-author
- [[entities/piero-kauffmann]] — ECHO RL infrastructure
- [[concepts/post-training/echo-rl]] — the ECHO training method
- [[concepts/world-models-for-agents]] — broader world-model learning context
- [[entities/microsoft-ai-frontiers]] — research lab
