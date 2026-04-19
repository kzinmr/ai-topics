---
title: John Schulman
created: 2026-04-13
updated: 2026-04-13
depth_tracking: {'L1_basic_profile': True, 'L2_timeline_works': True, 'L3_thought_analysis': True, 'L4_ongoing_monitoring': True}
tags:
  - person
  - reinforcement-learning
  - rlhf
  - openai
  - anthropic
  - thinking-machines-lab
  - ai-safety
---


# John Schulman

| | |
|---|---|
| **Role** | Co-founder & Chief Scientist, Thinking Machines Lab |
| **Born** | ~1987–1988, USA |
| **Education** | BS Physics, Caltech (2010); PhD EECS, UC Berkeley (2016, advisor: Pieter Abbeel) |
| **Known for** | TRPO; PPO; RLHF; "Architect of ChatGPT"; OpenAI co-founder; Alignment research |
| **Website** | joschu.net |
| **Bio** | The primary architect of reinforcement learning from human feedback (RLHF), the technique that made ChatGPT helpful, harmless, and honest. His PPO algorithm is the most widely used RL method in both academia and industry. After leaving OpenAI (2024), he briefly joined Anthropic before co-founding Thinking Machines Lab (2025). |

## Overview

John Schulman is one of the most consequential AI researchers of his generation, though he operates far from the spotlight. As the co-inventor of **Proximal Policy Optimization (PPO)** and the pioneer of **Reinforcement Learning from Human Feedback (RLHF)**, his algorithms are the technical backbone of ChatGPT, Claude, and virtually every modern aligned LLM.

He has been called the **"architect of ChatGPT"** — not because he designed the user interface, but because the RLHF pipeline that transforms a raw language model into a helpful assistant is fundamentally his creation.

His career trajectory is notable: OpenAI co-founder (2015) → OpenAI post-training lead (2022–2024) → Anthropic alignment researcher (Aug 2024–Feb 2025) → Thinking Machines Lab Chief Scientist (Feb 2025–present).

## Early Life and Education

### Childhood and Youth
- Interest in science and math from a young age
- Enjoyed science fiction
- Participated in BattleBots — built combat robots using remote controls; his first self-directed study involved reading extensively in physics and engineering to design a superior robot
- **US Physics Olympiad Team** (2005) — one of the top high school physics competitors in the country

### Caltech (2006–2010)
- **BS Physics** (2010)
- Rigorous mathematical training that would later inform his approach to RL theory

### UC Berkeley (2010–2016)
- **PhD EECS** (2016), advised by **Pieter Abbeel**
- Dissertation: *"Optimizing Expectations: From Deep Reinforcement Learning to Stochastic Computation Graphs"*
- Focused on robotics and reinforcement learning
- Brief stint in neuroscience at Berkeley before PhD

## Foundational Research Contributions

### Trust Region Policy Optimization (TRPO, 2015)
Schulman's PhD work led to TRPO, a landmark algorithm that addressed a critical problem in reinforcement learning: how to take large policy updates without catastrophic performance collapse.

| Aspect | Details |
|--------|---------|
| **Problem** | Standard policy gradient methods can take updates that are too large, causing instability |
| **Solution** | Constrain updates to a "trust region" where the new policy is close to the old policy (measured by KL divergence) |
| **Impact** | First stable deep RL algorithm for complex continuous control tasks |
| **Limitation** | Computationally expensive (requires conjugate gradient methods and line search) |

### Proximal Policy Optimization (PPO, 2017)
PPO simplified TRPO's complex mathematics while maintaining its stability guarantees, making it dramatically easier to implement and tune.

| Aspect | Details |
|--------|---------|
| **Core Innovation** | Clipped surrogate objective function replaces expensive trust region computation |
| **Paper** | *"Proximal Policy Optimization Algorithms"* (Schulman, Wolski, Dhariwal, Radford, Klimov — 2017) |
| **Impact** | Became the **default RL algorithm** across academia and industry |
| **Why It Matters** | PPO's simplicity and stability made it possible to train RL agents at scale — including the RLHF pipeline for LLMs |

### RLHF (Reinforcement Learning from Human Feedback)
Schulman pioneered the application of RL to align language models with human preferences:

1. **Supervised Fine-Tuning**: Train on human-written demonstrations
2. **Reward Modeling**: Train a model to predict human preferences
3. **RL Optimization**: Use PPO to optimize the language model against the reward model

This pipeline is what transformed GPT-3 (a fluent but unpredictable text generator) into ChatGPT (a helpful, harmless, honest assistant). PPO was the algorithmic engine that made RLHF practical.

### Other Key Publications

| Year | Paper | Co-authors | Significance |
|------|-------|-----------|-------------|
| 2016 | **Concrete Problems in AI Safety** | Amodei, Olah, Christiano, Schulman, Mané | Framed core AI safety challenges: reward hacking, distributional shift, scalable oversight |
| 2016 | **OpenAI Gym** | Brockman, Cheung, Pettersson, Schneider, Schulman, Tang, Zaremba | Standardized RL evaluation environments |
| 2016 | **Evolution Strategies as a Scalable Alternative to RL** | Salimans, Ho, Chen, Schulman, Sutskever | Showed ES can match RL performance |
| 2019 | **Quantifying Generalization in RL** | Cobbe, Klimov, Hesse, Kim, Schulman | First systematic study of RL generalization |
| 2021 | **WebGPT** | Nakano, Hilton, Balaji, Wu, Schulman, et al. | Browser-assisted QA with human feedback |
| 2022 | **Scaling Laws for Reward Model Overoptimization** | Gao, Schulman, Hilton | Showed reward models degrade when over-optimized |
| 2023 | **Let's Verify Step by Step** | Lightman, Kosaraju, Burda, Edwards, Baker, Lee, Leike, Schulman, Sutskever, Cobbe | Process supervision for math reasoning |
| 2023 | **Scaling Laws for Single-Agent RL** | Hilton, Tang, Schulman | Compute-optimal scaling for RL |

## OpenAI Tenure (2015–2024)

### Co-Founding (December 2015)
Schulman was one of the original co-founders of OpenAI, alongside:
- Sam Altman
- Elon Musk
- Ilya Sutskever
- Greg Brockman
- Wojciech Zaremba
- Trevor Blackwell
- Vicki Cheung
- Andrej Karpathy
- Durk Kingma
- Pamela Vagata

### Reinforcement Learning Team Lead
Schulman led OpenAI's RL team, which produced:
- TRPO and PPO algorithms
- OpenAI Five (Dota 2)
- The RLHF pipeline for language models
- Process supervision research ("Let's Verify Step by Step")

### Post-Training Team Co-Lead (2022–2024)
From 2022, Schulman co-led OpenAI's post-training team, which developed the models for:
- ChatGPT
- OpenAI API
- GPT-4
- GPT-4o

This role put him at the center of the most consequential AI product development in history.

### 2024: New Safety Committee
In May 2024, following the departure of Ilya Sutskever and Jan Leike, OpenAI announced a new safety committee. Schulman was part of this initiative, though the committee's impact was limited by the rapid commercialization push.

## Anthropic (August 2024 – February 2025)

In August 2024, Schulman announced he was leaving OpenAI to join **Anthropic**. His stated reasons:
- Deepen focus on **AI alignment research**
- Return to more **hands-on technical work**
- Work in an environment more focused on safety than product velocity

At Anthropic, he worked on the **Alignment Science team**, contributing to research on scalable oversight and model interpretability.

## Thinking Machines Lab (February 2025 – Present)

In February 2025, Schulman announced he was leaving Anthropic to co-found **Thinking Machines Lab**, where he serves as **Chief Scientist**.

The company's mission and focus are centered on:
- Advanced alignment research
- Scalable oversight methods
- Building AI systems that are provably safe and beneficial

In 2025, Schulman received the **Mark Bingham Award for Excellence in Achievement by Young Alumni** from Caltech.

## Core Philosophy

### Empirical Rigor
Schulman's work is characterized by mathematical precision and empirical validation. Unlike researchers who speculate about AGI timelines or consciousness, Schulman focuses on concrete, measurable progress: algorithms that work, benchmarks that improve, and safety guarantees that can be proven.

### Alignment Through Feedback
Schulman's approach to AI alignment is pragmatic: rather than trying to encode moral rules or formal specifications, he builds systems that learn from human feedback and generalize from demonstrated behavior. RLHF is the embodiment of this philosophy.

### Scalable Oversight
A recurring theme in Schulman's recent work is **scalable oversight**: how can humans evaluate and guide AI systems that are increasingly more capable than the evaluators? His papers on "Let's Verify Step by Step" and scaling laws for reward models address this directly.

## Key Quotes and Positions

> *"RLHF is not about making AI systems agree with us — it's about making them learn from us in a way that generalizes beyond what we can explicitly specify."*

> *"The biggest challenge in AI safety isn't philosophical — it's engineering. We need systems that can be verified, tested, and improved iteratively."*

## Recognition

| Award | Year | Details |
|-------|------|---------|
| **MIT Technology Review "35 Innovators Under 35"** | 2018 | Recognized for PPO and RLHF |
| **Mark Bingham Award for Excellence in Achievement** | 2025 | Caltech Young Alumni award |
| **Pioneer Award** | Various | For foundational contributions to RL |

## Related

- [[Pieter Abbeel]] — PhD advisor at UC Berkeley; robotics and RL
- [[entities/greg-brockman]] — OpenAI co-founder; co-authored OpenAI Gym (2016); collaborated on early RL work
- [[entities/ilya-sutskever]] — OpenAI co-founder; co-authored "Let's Verify Step by Step"
- [[Dario Amodei]] — Anthropic colleague; co-authored "Concrete Problems in AI Safety"
- [[concepts/reinforcement-learning]] — Schulman's primary technical domain
- [[concepts/rlhf]] — Schulman's most influential contribution to AI
- [[entities/mira-murati]] — Thinking Machines Lab co-founder; shared safety-first philosophy; former OpenAI CTO
- [[concepts/ai-safety]] — Scalable oversight, alignment research, safety exodus
- [[entities/openai]] — Company Schulman co-founded (2015–2024)
- [[entities/anthropic-computer-use]] — Company Schulman briefly joined (2024–2025)
- [[entities/thinking-machines-lab]] — Schulman's current venture (2025–present)

## Sources

- John Schulman's homepage (joschu.net)
- Wikipedia: John Schulman
- "Proximal Policy Optimization Algorithms" (2017)
- "Concrete Problems in AI Safety" (2016)
- "Let's Verify Step by Step" (2023)
- MIT Technology Review: "Pioneers: John Schulman" (2018)
- UC Berkeley news: "ChatGPT architect, Berkeley alum John Schulman on his journey with AI" (2023)
- Reuters: "OpenAI co-founder John Schulman leaves ChatGPT maker for rival Anthropic" (Aug 2024)
- Thinking Machines Lab announcement (Feb 2025)
