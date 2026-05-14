---
title: Seth Karten
created: 2026-05-14
updated: 2026-05-14
type: entity
status: active
tags: [person, researcher, ai-agents, agent-harness]
sources: [raw/articles/2026-05-13_sethkarten_continual-harness.md]
aliases: ["@sethkarten"]
related: [concepts/continual-harness, entities/ryan-lopopolo, entities/princeton-university]
---

# Seth Karten

**Seth Karten** (@sethkarten) is a CS PhD student at **Princeton University** working on AI agents, with prior experience at **CMU** and **Waymo**. He is the creator of **PokeChamp** and **PokeAgent**, and lead author of the **Continual Harness** framework.

## Bio

- **Current**: CS PhD @ Princeton University
- **Previous**: CMU, Waymo
- **X/Twitter**: [@sethkarten](https://x.com/sethkarten)
- **Website**: [sethkarten.ai](https://sethkarten.ai)
- **Focus areas**: AI agents, agent harnesses, Pokémon as agent benchmarks, LLM economics

## Key Work

### Continual Harness (2026)
Lead author of "Continual Harness: Online Adaptation for Self-Improving Foundation Agents" (arXiv:2605.09998). The framework removes the human from the harness refinement loop, enabling agents to improve their own prompts, sub-agents, skills, and memory online within a single run — without episode resets. Co-authors include Joel Zhang, Chi Jin (Princeton professor), and Kiran Vodrahalli.

> *"Long-horizon embodied agency is a harness problem rather than a model-scale problem."*

### Gemini Plays Pokémon (GPP)
Co-author of GPP — the first AI system to complete Pokémon Blue, Yellow Legacy on hard mode, and Crystal without losing a battle. The project demonstrated that agent harness quality matters more than model scale for long-horizon tasks.

### Pokémon Agent Benchmarking
Creator of **PokeChamp** and **PokeAgent** — open benchmarks for AI agents playing Pokémon. Organized "the largest AI Pokémon tournament ever" (2025), which became an open benchmark for comparing agent architectures across different models and games.

### LLM Economics
Research interest in the economics of LLM deployment, including token costs, inference optimization, and the trade-offs between model scale and harness sophistication.

## Agent Philosophy

Karten's work embodies the "harness engineering" perspective: that the scaffolding around a model (prompts, memory, sub-agents, skills) is more important for agent capability than raw model performance. His research advances the idea that agents should **improve their own harnesses** over time, converging with [[entities/ryan-lopopolo]]'s Harness Engineering framework.

## Related Pages

- [[concepts/continual-harness]] — The framework
- [[entities/ryan-lopopolo]] — Harness Engineering originator
- [[entities/shunyu-yao]] — Reflexion (verbal self-improvement for agents)
- [[entities/lester-solbakken]] — Verifiable feedback loops
