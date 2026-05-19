---
title: Dimitris Papailiopoulos
type: person
created: 2026-05-19
updated: 2026-05-19
tags: [person, researcher, microsoft, reinforcement-learning, agent-training]
sources:
  - raw/articles/2026-05-18_dimitris-papailiopoulos_echo-terminal-agents-world-models.md
  - https://x.com/DimitrisPapail
aliases:
  - "@DimitrisPapail"
---

# Dimitris Papailiopoulos

Researcher at **Microsoft Research, AI Frontiers** lab. Professor at **UW-Madison** (on leave). Works on reinforcement learning for AI agents, with a focus on CLI/terminal agents and self-improvement.

- **X/Twitter**: [@DimitrisPapail](https://x.com/DimitrisPapail)
- **Affiliation**: Microsoft Research AI Frontiers
- **Academic**: Professor, UW-Madison (on leave)

## Research Focus

- Agent RL training (GRPO, ECHO)
- CLI/terminal agents and environment interaction
- Self-improvement and continual learning for agents
- World models for LLM agents

## Notable Work

### ECHO: Terminal Agents Learn World Models for Free (2026-05)
Co-authored with Vaishnavi Shrivastava. Introduced **[[echo-rl|ECHO]]**, a hybrid training objective that adds environment cross-entropy loss on terminal-output tokens alongside standard GRPO loss on action tokens. Key findings:
- Nearly doubles TerminalBench-2.0 pass@1 at no extra cost
- 2.3× faster training to same performance
- Can substitute for expert SFT and enables verifier-free self-improvement

Published at Microsoft Research AI Frontiers. Code: [github.com/microsoft/echo-rl](https://github.com/microsoft/echo-rl).

### Other Contributions
- Known for advocating small-scale "microcosm" experiments to validate ideas before scaling (the "silly maze experiment" — testing ECHO on a 10M-param transformer navigating 2D mazes on a laptop)
- Frequent collaborator with Ahmed Awadallah at MSR AI Frontiers

## Philosophy

Believes most clean ideas have a microcosm — a scaled-down version you can run on a laptop in an evening that tells you whether the idea is worth scaling up. "Most of my ideas are wrong and the laptop experiment tells me which ones to drop before they cost anyone else time."

## See Also

- [[entities/vaishnavi-shrivastava]] — co-author of ECHO
- [[echo-rl]] — the ECHO training method
- [[world-models-for-agents]] — world models in agent training
- [[entities/will-brown]] — discussed continual learning for agents
