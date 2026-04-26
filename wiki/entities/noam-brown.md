---
title: Noam Brown
type: entity
created: 2026-04-14
updated: 2026-04-14
depth_tracking: {'L1_basic_profile': True, 'L2_timeline_works': True, 'L3_thought_analysis': True, 'L4_ongoing_monitoring': False}
tags:
  - person
  - openai
  - meta-fair
  - cmu
  - poker-ai
  - reasoning
  - multi-agent
  - diplomacy
sources: []
---


# Noam Brown

| | |
|---|---|
| **Role** | Research Scientist, OpenAI |
| **Education** | BA Mathematics & CS, Rutgers (2008, summa cum laude); MS Robotics & PhD CS, CMU (2014–2020) |
| **Known for** | Libratus (poker AI); Pluribus (6-player poker AI); CICERO (Diplomacy AI); o1/o3 reasoning models |
| **Bio** | Rutgers (math/CS) → MJM Trading (algorithmic trading) → Federal Reserve Board (research) → CMU PhD under Tuomas Sandholm → Meta FAIR → OpenAI. Pioneer of imperfect-information game AI (Libratus, Pluribus, CICERO). Key architect of OpenAI's o1/o3 reasoning models. Marvin Minsky Medal winner. Uniquely positioned at the intersection of game theory, multi-agent systems, and deliberative AI reasoning. |

## Overview

Noam Brown is the **most influential AI researcher that most people haven't heard of** — his work powers three of the most significant game-playing AIs in history (Libratus, Pluribus, CICERO), and he is now a key architect of OpenAI's **o1 and o3 reasoning models**. His trajectory is unique among AI leaders:

1. **Algorithmic trader** (MJM Trading, 2006–2010)
2. **Federal Reserve researcher** (2010–2012)
3. **CMU PhD student** under Tuomas Sandholm — built Libratus and Pluribus
4. **Meta FAIR** — created CICERO (Diplomacy AI)
5. **OpenAI** — leading reasoning model development (o1, o3, Project Strawberry)

Brown's entire career has focused on **decision-making under uncertainty** — from poker tables to diplomatic negotiations to mathematical reasoning. His insight is that **the same principles that govern strategic games also govern real-world problem-solving**: imperfect information, multi-agent dynamics, and the need for deliberative planning.

## Early Life and Education

### High School and Early Interests
- Developed an early fascination with **poker during high school** — not for gambling, but for the **strategic and intellectual challenges**
- Described getting "really into poker when [he] was a kid" — drawn to its **decision-making under uncertainty**
- This early interest directly shaped his entire research career

### Rutgers University (2005–2008)
- **BA in Mathematics and Computer Science**, graduated **summa cum laude** (2008)
- Undergraduate foundation in quantitative reasoning that propelled him toward advanced studies

## Algorithmic Trading and Federal Reserve (2006–2012)

### MJM Trading Group (2006–2010)
- **Algorithmic Trading Engineer** in New York
- Built foundational skills in **probabilistic modeling** and **real-time decision-making under uncertainty**
- The adversarial nature of trading markets — where participants must anticipate opponents' moves with limited knowledge — paralleled concepts in **game theory**

### Federal Reserve Board (2010–2012)
- **Research Assistant** at the Board of Governors, Washington DC
- Worked in the **International Financial Markets** section of the International Finance division
- Researched algorithmic trading, including in **foreign exchange markets**
- This public-sector research experience ignited his interest in **game theory** and its applications to strategic decision-making

> Brown's transition from finance to AI research was driven by recognizing the intersection between **financial decision-making and computational strategies for imperfect-information environments**.

## CMU PhD: Libratus and Pluribus (2012–2020)

### Graduate Studies
- **MS Robotics** (2012–2014) and **PhD Computer Science** (2014–2020) at Carnegie Mellon University
- Advisor: **Tuomas Sandholm** — a leading game theorist and AI researcher
- Dissertation: *"Equilibrium Finding for Large Adversarial Imperfect-Information Games"*
- **2020**: Awarded CMU School of Computer Science **Distinguished Dissertation Award**

### Libratus (2017) — First AI to Beat Humans at No-Limit Poker

**Heads-up No-Limit Texas Hold'em** — a game with approximately **10^161 possible decision points**, making it vastly more complex than chess.

| Component | Innovation |
|-----------|-----------|
| **Abstraction** | Reduced billions of bet sizes to manageable set; grouped similar hands into buckets |
| **Pre-computation** | Blueprint strategy via Monte Carlo CFR with regret-based pruning |
| **Real-time solving** | Subgame solving during play — adapting to opponents' actual actions |
| **Self-improvement** | Algorithm learned from its own mistakes during matches |

**Results:** Libratus defeated **four top professional poker players** (Dong Kim, Jimmy Chou, Daniel McAulay, Jason Les) over **120,000 hands** with statistically significant margins.

> This was a breakthrough not just in poker, but in **decision-making under imperfect information** — applicable to negotiation, cybersecurity, and financial trading.

### Pluribus (2019) — Multiplayer Poker Superintelligence

Building on Libratus, Pluribus tackled **six-player no-limit Texas Hold'em** — an even harder problem because:
- Multiple agents with hidden information
- No clear zero-sum structure (coalitions, implicit cooperation)
- Strategy space grows **exponentially** with number of players

**Key innovation: Single Deep CFR**
- Efficient computation of near-optimal strategies **without opponent modeling**
- Limited real-time depth-limited search for strategy refinement
- Training: just **12,400 CPU core-hours** — far less than many contemporary AIs

**Results:** Pluribus defeated **five top human professionals** (including two-time World Series of Poker champion Chris Ferguson) over 10,000 hands, achieving an average win rate of **~5 big blinds per game** — considered decisive in poker.

- Published on the **cover of Science magazine** (2019)
- Named **runner-up for Science's Breakthrough of the Year**

> Pluribus demonstrated that **multi-agent imperfect-information games** could be solved efficiently — a result with implications for economics, political science, and any domain involving strategic interaction.

## Meta FAIR: CICERO (2018–2022)

Brown joined **Meta's Fundamental AI Research (FAIR)** lab in 2018.

### CICERO — Human-Level Diplomacy AI (2022)

**Diplomacy** is arguably the hardest strategic game for AI:
- 7 players negotiating simultaneously
- Requires **natural language communication** to form alliances
- Involves **trust, betrayal, and long-term planning**
- No hidden information on the board — but hidden **intentions** in players' minds

**CICERO's architecture:**
| Component | Function |
|-----------|----------|
| **Language model** | Generates human-like diplomatic messages |
| **Strategic planner** | Combines Monte Carlo tree search with dialogue generation |
| **Partner modeling** | Infers opponents' intentions from messages and actions |
| **Commitment devices** | Proposes verifiable plans to build trust |

**Results:**
- Ranked in the **top 10% of human competitors** in anonymous online games
- Generated messages preferred by human experts over alternatives in **62% of pairwise comparisons**
- First AI to achieve human-level performance in a game requiring **social negotiation**

> CICERO demonstrated that AI systems could **combine strategic reasoning with natural language understanding** — a capability essential for real-world applications involving human-AI collaboration.

### ReBeL Framework
- **Recursive Belief-based Learning** — integrates deep RL with search for imperfect-information games
- Provably converges to **Nash equilibrium** through self-play
- Achieved superhuman performance in heads-up no-limit Texas hold'em

## OpenAI: Reasoning Models (2022–Present)

Brown joined OpenAI after 2022 and has become a **key architect of the o1 model series**.

### o1 Reasoning Model (September 2024)

Part of **Project Strawberry** (with Ilge Akkaya and Hunter Lightman):

- Models that **"think longer"** before responding — extended deliberation
- Trained using **large-scale reinforcement learning** to optimize chain-of-thought processes
- Enables **backtracking and self-correction** — model recognizes errors during deliberation and adjusts
- *"We saw that once it's able to think for longer, it develops these abilities almost emergently."* — Brown

**Performance:**
- Near **gold-medal level** on International Mathematical Olympiad problems
- **93.9%** on competitive programming benchmarks (Codeforces)
- **96.7%** on AIME 2024 math problems

### o3 Model (December 2024)

- Announced just 3 months after o1
- Further advances in reasoning paradigms
- *"We announced @OpenAI o1 just 3 months ago. Today, we announced o3. We have every reason to believe this trajectory will continue."* — Brown on X/Twitter

### Connection to Game AI

Brown's work on reasoning models directly extends his game AI research:

| Game AI | Reasoning Model | Shared Principle |
|---------|----------------|-----------------|
| Libratus subgame solving | o1 chain-of-thought | **Deliberative search** before acting |
| Pluribus multi-agent dynamics | o3 multi-step reasoning | **Planning ahead** in complex environments |
| CICERO language + strategy | GPT-4 + o1 integration | **Combining communication with planning** |

> Brown has stated that the principles underlying **strategic game-playing** — imperfect information, multi-step planning, self-correction — are the same principles needed for **general AI reasoning**. His career is a continuous exploration of this insight.

## Awards and Recognition

| Year | Award | For |
|------|-------|-----|
| 2018 | **Marvin Minsky Medal** (IJCAI) | Libratus development |
| 2019 | **MIT Technology Review 35 Innovators Under 35** | AI for strategic games |
| 2019 | **Science Breakthrough of the Year** (runner-up) | Pluribus |
| 2020 | **CMU Distinguished Dissertation Award** | PhD thesis on equilibrium finding |

## Publications (Selected)

| Paper | Venue | Year | Significance |
|-------|-------|------|-------------|
| "Safe and Nested Subgame Solving for Imperfect-Information Games" | NIPS | 2017 | Libratus algorithm |
| "Superhuman AI for Multiplayer Poker" | Science | 2019 | Pluribus (cover article) |
| "Human-Level Play in the Game of Diplomacy by Combining Language Models with Strategic Reasoning" | Science | 2022 | CICERO |
| "ReBeL: Combining Deep Reinforcement Learning with Search for Imperfect-Information Games" | FAIR | 2021 | ReBeL framework |
| GPT-4 Technical Report | OpenAI | 2023 | Co-author |
| o1 System Card | OpenAI | 2024 | Co-author |

## Personal Life and Communication Style

- **Active on X/Twitter** — frequently shares insights about AI reasoning and game theory
- Known for **clear, accessible explanations** of complex technical concepts
- Often draws parallels between **game-playing AI and real-world applications**
- Maintains connections to the **competitive programming community** through IOI coaching

## Related

- [[concepts/tuomas-sandholm]] — PhD advisor; co-developer of Libratus and Pluribus
- [[mark-chen]] — OpenAI colleague; o1 reasoning model
- [[concepts/hunter-lightman]] — OpenAI colleague; Project Strawberry
- [[ilya-sutskever]] — OpenAI co-founder; Q* project (related to reasoning)
- [[sam-altman]] — OpenAI CEO
-  — Brown's theoretical foundation
-  — o1/o3 models represent this paradigm
-  — CICERO and Pluribus

## Sources

- Grokipedia: Noam Brown
- "Safe and Nested Subgame Solving for Imperfect-Information Games" (NIPS 2017)
- "Superhuman AI for Multiplayer Poker" (Science 2019)
- "Human-Level Play in the Game of Diplomacy" (Science 2022)
- o1 System Card (OpenAI 2024)
- MIT Technology Review "35 Innovators Under 35" (2019)
- IJCAI Marvin Minsky Medal (2018)
