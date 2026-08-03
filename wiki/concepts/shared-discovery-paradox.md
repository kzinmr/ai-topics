---
title: "Shared Discovery Paradox"
created: 2026-08-03
updated: 2026-08-03
type: concept
tags:
  - concept
  - game-theory
  - coordination
  - multi-agent
  - collective-intelligence
  - information-theory
  - agent-coordination
  - ai-economics
related:
  - concepts/caid-coordination
  - entities/yohei-nakajima
sources:
  - "raw/articles/2026-07-21_yoheinakajima_shared-discovery-paradox.md"
  - "https://arxiv.org/abs/2607.18045"
  - "https://yoheinakajima.github.io/shared-discovery-paradox/"
aliases:
  - Shared Discovery Paradox
  - information sharing paradox
---

# Shared Discovery Paradox

The **Shared Discovery Paradox** is a game-theoretic concept formulated by [[entities/yohei-nakajima|Yohei Nakajima]] (July 2026) demonstrating that **information sharing without action coordination can improve individual decision-making while simultaneously degrading group outcomes**. It provides a formal, inspectable model separating the effects of information pooling from action allocation in collective discovery problems.

## Summary

The paradox challenges the intuition that more shared information always improves collective outcomes. Using a simple 16-box, 8-player game with imperfect clues (20% accuracy), Nakajima shows that:

- **Without information sharing**: Each player follows their own clue → 20% individual accuracy, **83.2% collective success**
- **With information sharing but no coordination**: All players converge on the same most-likely box → 38.4% individual accuracy, **38.4% collective success**
- **With information sharing + coordination**: Players choose the 8 most likely distinct boxes → **85.9% collective success**

Sharing information **nearly doubles individual accuracy** while **halving the collective probability of success** when actions are uncoordinated. This cleanly demonstrates that the bottleneck in collective discovery is action allocation, not information quality.

## The Model

### Setup
- 16 boxes, 8 players, 1 jackpot
- Each player receives an independent imperfect clue (20% accuracy; otherwise uniform random)
- Players independently choose one box
- Goal: maximize the probability that **at least one** player selects the jackpot

### Scenarios

| # | Scenario | Individual Accuracy | Collective Success | Key Dynamic |
|---|----------|-------------------|-------------------|-------------|
| 1 | Random (no info, no coord) | 6.25% | 40.3% | Baseline randomness |
| 2 | Coordinated random | 6.25% | 50.0% | Mutual exclusion works even without info |
| 3 | Clues, no sharing | 20.0% | 83.2% | Independent signals → diverse choices |
| 4 | Clues shared, no coord | **38.4%** | **38.4%** | Convergence kills diversity |
| 5 | Clues shared, jackpot split equilibrium | — | ~60% | Incentives partially restore diversity |
| 6 | Clues shared, coordinated | 10.74% (avg) | **85.9%** | Optimal: assign lower-probability boxes |

### Core Tension

The paradox arises from a **misalignment between individual and collective objectives**:

- **Individual objective**: maximize P(I choose the jackpot) → pick the single box with highest posterior probability
- **Collective objective**: maximize P(someone chooses the jackpot) → distribute choices across multiple high-probability boxes

When information is shared and every player independently maximizes their own accuracy, **all players converge on the same box** — the one with the highest posterior probability. The collective success probability collapses to that single box's probability (38.4%), down from 83.2% when players followed their independent clues without sharing.

## Academic Foundations

The paradox synthesizes several established literatures in economics and game theory:

| Literature | Key Contributors | Relevance |
|-----------|-----------------|-----------|
| **Information cascades** | Banerjee (1992); Bikhchandani, Hirshleifer & Welch (1992) | How sequential decision-makers ignore private signals and follow predecessors |
| **Observational learning** | Smith & Sørensen (2000) | Pathological learning when agents observe others' actions but not signals |
| **Organizational learning** | March (1991) | Exploration vs exploitation in organizational contexts |
| **Optimal search** | Koopman (1956) | Mathematical theory of search allocation |
| **Division of cognitive labor** | Kitcher (1990); Zollman (2007) | How scientific communities benefit from diverse approaches |
| **Price of anarchy / congestion** | Roughgarden (2005) | Inefficiency of selfish routing in networks |
| **Informational Braess' paradox** | Acemoglu et al. (2016) | How additional information can worsen outcomes in network games |

The novelty of Nakajima's contribution is a **minimal, fully inspectable game** that cleanly separates information sharing from action allocation — showing that the latter, not the former, determines whether group outcomes improve.

## Relevance to AI Multi-Agent Systems

The Shared Discovery Paradox has direct implications for multi-agent AI systems:

### Shared Memory as Shared Information

When multiple AI agents share a common knowledge base or memory (e.g., vector DB, ActiveGraph), they effectively "share clues." If each agent independently maximizes its own task success without coordination, the system may exhibit the paradox:

- **Agents converge on the same solution paths** — reducing collective exploration
- **Diverse approaches collapse** — the system loses the benefit of parallel exploration
- **Collective problem-solving degrades** — even as individual agent performance metrics improve

### Mitigation Strategies

The paradox suggests several design principles for multi-agent systems:

1. **Action coordination layer**: Beyond shared memory, agents need explicit mechanisms to avoid duplicating effort (e.g., task queues with mutual exclusion, role assignment)
2. **Diversity-preserving incentives**: Reward agents for finding novel solutions, not just accurate ones
3. **Exploration budgets**: Allocate some agents to lower-probability paths despite shared information suggesting a single best approach
4. **Pooled outcomes**: Align incentives so agents benefit from collective success, not just individual performance (analogous to the jackpot-pooling equilibrium)

### Connection to Known Patterns

- **[[concepts/caid-coordination]] (CAID)**: Centralized Asynchronous Isolated Delegation — one solution to the coordination problem where a central orchestrator assigns distinct work items
- **[[concepts/harness-engineering/agent-statefulness]]**: ActiveGraph's event-sourced model tracks which agent did what, enabling post-hoc detection of duplicated effort
- **[[entities/yohei-nakajima]]**: The paradox extends Nakajima's consistent thesis — the bottleneck is control and coordination, not model capability

## Broader Implications

Beyond AI agents, the paradox applies to:

- **Corporate innovation**: Competing internal teams may all pursue the same "obvious" opportunity after sharing market research, reducing collective innovation yield
- **Venture capital**: When VCs share deal flow and market analysis, capital concentrates on consensus picks, potentially missing higher-return opportunities requiring coordinated diversification
- **Scientific discovery**: Open sharing of preliminary results may cause researchers to converge on the most promising direction, reducing the diversity of approaches (counterpoint to the "division of cognitive labor" argument)

## Key Insight

> **"Improving the group outcome depends on action allocation, not just information sharing."**

The paradox reframes the debate about information sharing in multi-agent systems: the question is not whether agents should share information, but **how they coordinate actions after sharing it**.

## Graph Structure Query

```
[shared-discovery-paradox] ──author──→ [entities/yohei-nakajima]
[shared-discovery-paradox] ──contrasts──→ [concepts/caid-coordination] (solves the coordination problem the paradox identifies)
[shared-discovery-paradox] ──extends──→ [game-theory literature: information cascades, division of cognitive labor]
[shared-discovery-paradox] ──relates-to──→ [concepts/harness-engineering/agent-statefulness]
[shared-discovery-paradox] ──embodies──→ [philosophy: exploration-exploitation tradeoff in collective settings]
```

This structure informs graph traversal queries: authored by [[entities/yohei-nakajima]], the paradox identifies a coordination failure that [[concepts/caid-coordination|CAID]] directly addresses, and extends March's exploration-exploitation framework to multi-agent information-sharing contexts.

## Sources

- [The Shared Discovery Paradox — X Article](https://x.com/i/article/2079412885021970432) (July 21, 2026)
- [arXiv:2607.18045](https://arxiv.org/abs/2607.18045) — Full preprint
- [Interactive Site](https://yoheinakajima.github.io/shared-discovery-paradox/)
- [GitHub Repository](https://github.com/yoheinakajima/shared-discovery-paradox)
