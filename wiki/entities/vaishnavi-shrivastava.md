---
title: Vaishnavi Shrivastava
type: person
created: 2026-05-19
updated: 2026-05-26
tags:
  - person
  - microsoft
  - reinforcement-learning
  - agent-training
  - world-models
sources:
  - raw/articles/2026-05-18_dimitris-papailiopoulos_echo-terminal-agents-world-models.md
  - raw/papers/2026-05-26_2605.24517_echo-terminal-agents-world-models.md
  - https://arxiv.org/abs/2605.24517
  - https://x.com/VaishShrivas
aliases:
  - "@VaishShrivas"
---

# Vaishnavi Shrivastava

Researcher at **Microsoft Research, AI Frontiers**. Primary author of [[echo-rl|ECHO]], a method for training CLI agents that learns world models from terminal environment responses during RL.

- **X/Twitter**: [@VaishShrivas](https://x.com/VaishShrivas)
- **Affiliation**: Microsoft Research AI Frontiers

## Research Focus

- Reinforcement learning for CLI/terminal agents
- World models and environment prediction
- GRPO and hybrid training objectives
- Self-improving agents

## Notable Work

### ECHO: Terminal Agents Learn World Models for Free (2026-05)
Lead researcher and primary implementer of ECHO, co-authored with [[entities/dimitris-papailiopoulos|Dimitris Papailiopoulos]], [[entities/piero-kauffmann|Piero Kauffmann]], and [[entities/ahmed-awadallah|Ahmed Awadallah]]. ECHO introduces a hybrid GRPO + environment cross-entropy loss that trains CLI agents on terminal responses — essentially learning a world model "for free" from tokens already in the rollout.

Paper: [arxiv.org/abs/2605.24517](https://arxiv.org/abs/2605.24517) (May 2026). Code: [github.com/microsoft/echo-rl](https://github.com/microsoft/echo-rl). Built on [[entities/nova-sky|NovaSky-AI]]'s SkyRL.

Key contributions:
- Designed and ran the full ECHO experiments (first cluster run launched March 29, 2026)
- Demonstrated near-doubling of TerminalBench-2.0 pass@1 (2.7 → 5.2 at 8B, 5.2 → 10.8 at 14B)
- Showed ECHO can substitute for expert SFT and enables verifier-free self-improvement

As Dimitris put it: "Vaish did all the work to figure it out. I contributed a silly maze experiment, a strong opinion on the title, and saying 'holy shit' when she showed me the first result."

Work done at **AI Frontiers**, a boutique research lab inside Microsoft Research, under Ahmed Awadallah.

## See Also

- [[entities/dimitris-papailiopoulos]] — co-author
- [[entities/piero-kauffmann]] — RL infrastructure co-author
- [[entities/ahmed-awadallah]] — MSR AI Frontiers research lead
- [[echo-rl]] — the ECHO training method
- [[entities/microsoft-ai-frontiers]] — research lab
- [[concepts/world-models-for-agents]] — world models in agent training
