---
title: "niplav"
created: 2026-05-09
updated: 2026-05-09
type: entity
status: l2
tags:
  - person
  - alignment
  - agent-safety
  - writing
  - blog
aliases: ["niplav LessWrong"]
sources: [raw/articles/2026-03-17_lesswrong_giant-lookup-tables-of-shallow-circuits.md]
related: [concepts/glut-of-circuits, concepts/rlhf, concepts/constitutional-ai, concepts/chain-of-thought]
---

# niplav

LessWrong contributor and AI alignment researcher. Author of the "GLUT-of-circuits" model of LLMs.

## Key Contributions

### GLUT-of-Circuits Model (2026-03-17)
[[concepts/glut-of-circuits]] — Proposed that LLMs are superlinear-in-network-width lookup-table-like collections of depth-limited, composeable, error-correcting circuits computed in superposition. This model explains how LLMs can be capable without being agentic optimizers. 95 points, 35 comments on LessWrong.

**Core claims**:
- Frontier models have <20,000 serial computation steps per forward pass
- Circuits in superposition can be individually aligned via RLHF
- The token bottleneck (~8-10 bits) limits optimization pressure
- Alignment reduces from Category I to Category II problem

### Research Interests
- Agent structure problem — what makes an AI system an "agent" vs. a collection of shallow circuits
- Computation in superposition — how neural networks use high-dimensional spaces to run many computations in parallel
- AI alignment — reframing alignment as circuit-level selection rather than agent-level control
- Singular learning theory and its connection to error-correcting circuits

### Writing
- LessWrong: Primary platform for technical posts
- Contributed to discourse on agent foundations, shard theory, and AI safety
- Engages with both technical (Hänni et al. 2024) and philosophical (Garrabrant 2019, Altair 2024) literature

## Style & Approach
- Technical rigor grounded in theoretical computer science (circuit complexity, Johnson-Lindenstrauss lemma)
- Probabilistic forecasting (explicit confidence levels: 50%, 65%, 85%)
- Bridge-building between mechanistic interpretability and agent foundations communities
- Willing to stake concrete predictions ("LLMs will plateau")
