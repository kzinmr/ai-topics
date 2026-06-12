---
title: Eric Jang
type: entity
created: 2026-05-16
updated: 2026-05-16
tags:
  - person
  - reinforcement-learning
  - robotics
  - lab
sources:
  - raw/articles/dwarkesh.com--p-eric-jang--44c9439c.md
---

# Eric Jang

**Role:** Former VP of AI, 1X Technologies
**Affiliations:** 1X Technologies (former VP of AI); Google Brain (former researcher)
**Themes:** Reinforcement learning, Monte Carlo Tree Search, robotics, automated AI research

## Overview

Eric Jang is an AI researcher known for his work on **reinforcement learning** and **robotics**. He was most recently **VP of AI at 1X Technologies** (formerly Halodi Robotics), a Norwegian humanoid robotics company. Prior to that, he was a researcher at **Google Brain**, where he worked on probabilistic machine learning and generative models.

## AlphaGo Analysis (May 2026)

In a May 2026 appearance on **Dwarkesh Patel's podcast**, Jang walked through how to build **AlphaGo from scratch** using modern AI tools. The discussion yielded several key insights:

### RL and Credit Assignment

Jang contrasted AlphaGo's approach with LLM reinforcement learning:

- **AlphaGo's MCTS** (Monte Carlo Tree Search) provides a strictly better action at every move, giving a clean training target that sidesteps the credit assignment problem
- **LLM policy gradient RL** must figure out which of 100k+ tokens in a trajectory actually produced the right answer — a much noisier signal
- Jang argued that human learning is closer to the MCTS approach than to naive policy gradients

### Why MCTS Doesn't Work for LLMs

A key question discussed was why MCTS — so successful in Go — doesn't directly transfer to language models:
- Go has a discrete, well-defined action space with clear terminal states
- Language generation involves open-ended, high-dimensional output spaces
- The search tree structure doesn't map cleanly to token-by-token generation

### Automated AI Researchers

Jang kickstarted an **Autoresearch loop** on his AlphaGo project:
- **Automatable**: Implementing experiments, running benchmarks, optimizing hyperparameters
- **Still difficult**: Choosing the right research question, escaping research dead ends
- This provides insight into what parts of AI research LLMs can already handle vs. where human judgment remains essential

## 1X Technologies

As VP of AI at 1X, Jang led efforts to develop intelligence systems for humanoid robots. 1X focuses on general-purpose robots for real-world tasks, requiring advances in:
- Embodied AI and physical reasoning
- Real-time perception and control
- Safe deployment in human environments

## Google Brain

At Google Brain, Jang worked on:
- Probabilistic machine learning
- Generative models (VAEs, GANs)
- Scalable reinforcement learning

## Key Quotes

> "AlphaGo is still the cleanest worked example of the primitives of intelligence: search, learning from experience, and self-play."

> "Sometimes you understand the future better by stepping backward."

## Related

- [[entities/dwarkesh-patel]] — Podcast host; interviewed Jang about AlphaGo
- [[concepts/monte-carlo-tree-search]] — Search algorithm central to AlphaGo
- [[concepts/post-training/reinforcement-learning]] — Jang's area of expertise
- [[entities/1x-technologies]] — Company where Jang served as VP of AI
