---
title: "Continual Harness: Online Adaptation for Self-Improving Foundation Agents"
source: "https://x.com/i/article/2054438223846264832"
author: "Seth Karten (@sethkarten)"
date: "2026-05-13"
scraped: "2026-05-14"
type: x_article
x_article_id: "2054438223846264832"
bookmark_tweet_id: "2054579536612966480"
paper: "arXiv:2605.09998"
tags: [ai-agents, agent-harness, self-improving, agent-loop, embodied]
---

# Continual Harness: Online Adaptation for Self-Improving Foundation Agents

**Author**: Seth Karten (@sethkarten), CS PhD at Princeton, ex-CMU/Waymo
**Published**: May 13, 2026
**Retrieved via**: x.com/i/status/2054579536612966480
**Paper**: [arXiv:2605.09998](https://arxiv.org/abs/2605.09998) (submitted May 11, 2026)

## Core Argument

Long-horizon embodied agency is a **harness problem** rather than a model-scale problem. Coding agents already work this way. Claude Code and OpenHands are scaffolding around the model (prompt, skills, memory, sub-agents), and that scaffolding is most of what makes them useful. Embodied agents have not had an equivalent, which is why a frontier vision-language model playing Pokémon Red through a raw screenshot-and-buttons interface barely makes it past the first town.

## Gemini Plays Pokémon (GPP)

Gemini Plays Pokémon, led by co-author Joel Zhang, was the first AI system to complete Pokémon Blue, Yellow Legacy on hard mode, and Crystal without losing a battle. The key insight: **iterative harness development**.

The agent plays, the trajectory exposes failure modes, and the harness is refined to address them. This is the same pattern that makes coding agents effective — the harness improves faster than the model. Over time, the agent itself began iterating on its strategy through long-context memory, surfacing emergent self-improvement signals.

## Continual Harness

**Continual Harness** removes the human fully from the harness refinement loop. It formalizes and automates what was observed with GPP's human-in-the-loop harness development.

Starting from only a minimal environment interface, the agent alternates between:
1. **Acting** — using the current harness (prompt, sub-agents, skills, memory)
2. **Refining** — improving its own harness based on trajectory data

Unlike prompt-optimization methods that require episode resets, Continual Harness adapts **online within a single run**.

## Results

On Pokémon Red and Emerald across frontier models, Continual Harness starting from scratch:
- Substantially reduces button-press cost relative to the minimalist baseline
- Recovers a majority of the gap to a hand-engineered expert harness
- Shows capability-dependent gains

The paper also demonstrates a **process-reward co-learning loop**: an open-source agent's rollouts through the refining harness are relabeled by a frontier teacher and used to update the model, driving sustained in-game milestone progress without resetting the environment.

## Authors

- Seth Karten — CS PhD @ Princeton, PokeChamp, PokeAgent
- Joel Zhang — co-author of GPP
- Tersoo Upaa Jr, Ruirong Feng, Wenzhe Li, Chengshuai Shi
- Chi Jin — Princeton professor
- Kiran Vodrahalli

---

*Note: Content extracted from x.com/i/status page preview and arXiv abstract. Full article behind X auth wall.*
