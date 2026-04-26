---
title: Richard Sutton
type: entity
created: 2026-04-13
updated: 2026-04-13
depth_tracking: {'L1_basic_profile': True, 'L2_timeline_works': True, 'L3_thought_analysis': True, 'L4_ongoing_monitoring': True}
tags:
  - person
  - reinforcement-learning
  - agi
  - keen-technologies
  - bitter-lesson
sources: []
---


# Richard S. Sutton

| | |
|---|---|
| **Role** | Professor, University of Alberta; Research Scientist, Keen Technologies; Former Distinguished Research Scientist, Google DeepMind |
| **Education** | BA Psychology, Stanford (1978); MS & PhD CS, UMass Amherst (1980, 1984, advisor: Andrew G. Barto) |
| **Known for** | Founding reinforcement learning; Temporal-difference learning; Policy-gradient algorithms; "The Bitter Lesson"; 2024 ACM Turing Award |
| **Bio** | The "father of reinforcement learning" whose 40+ year career established the mathematical foundations of trial-and-error learning. His 2019 essay "The Bitter Lesson" argues that general methods leveraging computation ultimately outperform hand-engineered approaches — a thesis that directly influences John Carmack's AGI strategy at Keen Technologies. |

## Overview

Richard Sutton is the most consequential figure in the history of reinforcement learning (RL). Along with his doctoral advisor **Andrew G. Barto**, Sutton established the conceptual and algorithmic foundations of RL as a distinct field of AI research. His textbook *Reinforcement Learning: An Introduction* (1st ed. 1998, 2nd ed. 2018) is the definitive reference for the field.

In 2024, Sutton and Barto were jointly awarded the **ACM A.M. Turing Award** — the highest honor in computer science — for their foundational contributions to RL. Sutton's influence extends far beyond academia: his **"Bitter Lesson"** thesis (2019) has become a rallying cry for researchers who believe that scaling computation, not hand-crafted knowledge, is the path to AGI.

## Education and Early Career

- **BA Psychology**, Stanford University (1978) — His psychology background gave him a unique perspective on learning as a behavioral phenomenon
- **MS Computer Science**, University of Massachusetts Amherst (1980)
- **PhD Computer Science**, UMass Amherst (1984) — Doctoral research under **Andrew G. Barto** established foundational RL concepts
- **Postdoc/Early Positions**: Worked at GTE Laboratories and the University of Massachusetts before joining faculty positions

## Foundational Research Contributions

### Temporal-Difference (TD) Learning
Sutton's most fundamental algorithmic contribution. TD learning bridges the gap between Monte Carlo methods (which learn from complete episodes) and dynamic programming (which requires a model of the environment).

- **Key Paper**: *"Learning to Predict by the Methods of Temporal Differences"* (1988)
- **Core Insight**: Learning from the difference between successive predictions is more efficient than waiting for final outcomes
- **Impact**: Foundation for modern RL algorithms including Q-learning, SARSA, and all deep RL methods

### Policy Gradient Algorithms
Sutton pioneered the direct optimization of policies (rather than value functions), enabling RL to work with function approximation and continuous action spaces.

- **REINFORCE** (1992): The canonical policy gradient algorithm
- **Actor-Critic** methods: Combining policy gradients with value function estimation
- **Impact**: Enabled RL in high-dimensional spaces, directly leading to modern deep RL

### The Textbook: *Reinforcement Learning: An Introduction*
Co-authored with Andrew G. Barto:
- **1st Edition** (1998): Established RL as a coherent field
- **2nd Edition** (2018): Integrated deep RL, added modern algorithms (DQN, policy gradients, Monte Carlo tree search)
- **Open Access**: Freely available online, widely used in university courses
- **Code Examples**: Official implementations in Lisp, C, Python; community re-implementations in Python and Julia
- **Standard Exercises**: Multi-armed bandits, gridworld policy evaluation, Blackjack Monte Carlo methods, Random Walk TD learning, Cliff Walking Q-learning, Jack's Car Rental (Dynamic Programming), Windy Gridworld (Sarsa)

## Career Timeline

| Period | Position | Key Activities |
|--------|----------|---------------|
| 1984–1998 | Faculty, UMass Amherst / GTE Labs | Developed TD learning, policy gradients, RL textbook |
| 1998–2002 | Principal Technical Staff Member, AT&T Shannon Laboratory | Applied RL to telecommunications |
| 2002–2017 | Professor, University of Alberta | Founded the RLAI Lab (one of world's largest academic RL research groups); AITF Chair in RL & AI |
| 2017–2023 | Distinguished Research Scientist, Google DeepMind | Contributed to AlphaGo/AlphaZero research; bridged academic RL with industrial-scale applications |
| 2023–Present | Professor, University of Alberta + Research Scientist, Keen Technologies | Returned to academia; partnering with John Carmack on AGI research |

## "The Bitter Lesson" (2019)

Sutton's most influential essay argues a simple but controversial thesis:

> *"The biggest lesson that can be read from 70 years of AI research is that general methods that leverage computation are ultimately the most effective, and by a large margin."*

### Key Arguments

1. **Historical Pattern**: Every major AI breakthrough has come from leveraging more computation, not from encoding more human knowledge
2. **Failed Approaches**: Hand-crafted expert systems, human-knowledge-intensive approaches, and symbolic reasoning all ultimately lost to scalable, data-driven methods
3. **Successful Approaches**: Search (chess), learning (vision), and RL — all methods that scale with compute
4. **The Lesson is Bitter**: It's uncomfortable for researchers who spend their careers encoding human knowledge into AI systems

### Impact on the Field
- Widely cited in debates about AI strategy
- Directly influences **John Carmack's** AGI approach at Keen Technologies
- Used to argue against symbolic AI and for scaling-based approaches
- Referenced in discussions about whether LLMs represent a "general method" or a dead end

## Keen Technologies Partnership

Sutton joined **Keen Technologies** (founded 2022 by John Carmack) as a research partner. The collaboration represents a bet that:

1. RL-first approaches will ultimately outperform LLM-based approaches for AGI
2. Hardware-software co-design (including Carmack's fiber-optic L2 cache proposal) will be essential
3. The "Bitter Lesson" applies to the current generation of AI as much as to previous ones

This partnership has significant implications for the AGI debate: if Sutton and Carmack are right, the current LLM-centric approach may be a dead end, and RL-based methods will eventually dominate.

## Major Recognition

| Award | Year | Details |
|-------|------|---------|
| **ACM A.M. Turing Award** | 2024 | Joint with Andrew G. Barto for conceptual and algorithmic foundations of RL |
| **Fellow of the Royal Society** | 2021 | Recognition of fundamental contributions to science |
| **IJCAI Award for Research Excellence** | Earlier | For sustained contributions to AI research |

## Personal Life

- Libertarian political philosophy
- Avid chess player — this likely influenced his interest in game-playing AI and search algorithms
- Cancer survivor
- Known for his quiet, principled approach to research — focused on fundamentals rather than hype

## Core Philosophy

### Computation > Knowledge
Sutton's "Bitter Lesson" thesis is the cornerstone of his philosophy: general methods that scale with computation will always beat hand-crafted approaches. This is fundamentally different from the neuro-symbolic approach advocated by researchers like Gary Marcus.

### RL as the Path to AGI
Sutton believes reinforcement learning — learning from interaction with the environment through trial and error — is the essential ingredient for general intelligence. This contrasts with the language-first approach of LLM researchers.

### Empirical Rigor
Sutton emphasizes mathematical foundations and empirical validation over theoretical speculation. His work is characterized by clean algorithms, clear proofs, and practical implementations.

## Related

- [[john-carmack]] — Keen Technologies partner; advocate of Sutton's "Bitter Lesson"
-  — PhD advisor; co-author of RL textbook; Turing Award co-recipient
- [[reinforcement-learning]] — Sutton's foundational field
- [[chatgpt-memory-bitter-lesson]] — Sutton's most influential essay
-  — Sutton's long-term research goal
-  — Sutton's current industry affiliation

## Sources

- Grokipedia: Richard Sutton
- *Reinforcement Learning: An Introduction* (Sutton & Barto, 2nd ed. 2018)
- *"The Bitter Lesson"* (2019, http://www.incompleteideas.net/IncIdeas/BitterLesson.html)
- ACM Turing Award announcement (2024)
- Keen Technologies partnership announcements
- Royal Society fellowship citation (2021)
