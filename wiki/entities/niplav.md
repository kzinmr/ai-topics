---
title: "niplav"
created: 2026-05-09
updated: 2026-07-31
type: entity
status: L3
tags:
  - person
  - alignment
  - agent-safety
  - writing
  - blog
  - forecasting
  - quantified-self
  - mechanistic-interpretability
  - pseudonymous
aliases: ["niplav LessWrong", "niplav Yutsun"]
sources:
  - raw/articles/2026-03-17_lesswrong_giant-lookup-tables-of-shallow-circuits.md
  - https://niplav.site/
  - https://niplav.site/about.html
  - https://github.com/niplav
related: [concepts/glut-of-circuits, concepts/post-training/rlhf, concepts/constitutional-ai, concepts/chain-of-thought]
---

# niplav

LessWrong contributor and AI alignment researcher. Author of the "GLUT-of-circuits" model of LLMs.

## Overview

niplav (they/them) is a **pseudonymous independent researcher** who publishes on LessWrong, the Effective Altruism Forum, and their own long-form website (niplav.site, running since March 2019). Their work spans AI alignment, forecasting, existential risk, quantified self-experimentation, and programming. The personal site follows the "Long Content" model — pages are perpetually refined rather than date-published, explicitly inspired by [[entities/gwern|Gwern Branwen]] ("Think Less Wrong, act Long Now and Suck Less").

niplav is heavily AI-assisted: since mid-2024 the site's content has benefited from "many hundreds of conversations with Claude 3/3.5/3.6/3.7/4/4.5/4.6 Sonnet and Claude 3/4/4.1/4.5/4.6 Opus" (credited where they helped), plus Gemini 2.5/3, GPT-5.x, and Kimi K2/K2.5. They are openly hireable "to investigate research questions, write code, design and execute experiments, analyze data and make predictions."

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

## Forecasting Track Record

niplav is a serious, quantified forecaster and publishes detailed track records (as of 2023-08-05):

| Platform | Metric | Score |
|----------|--------|-------|
| Metaculus | Brier score (281 binary questions, uniformly sampled) | **0.116** |
| Metaculus | Continuous log score (204 questions, uniformly sampled) | 1.35 |
| Metaculus | Ranking | 38th baseline accuracy / 130th peer accuracy |
| PredictionBook | Brier score (131 questions, mostly own-research outcomes) | 0.2365 |
| Manifold Markets | Profit / Net worth | M̶5,295 / M̶37,112 |
| Manifold Markets | Calibration | Grade B-, score -2.69 |

The uniform-sampling methodology (rather than cherry-picking easy questions) makes these scores unusually informative. niplav advocates that "track records are great & underrated" and shares them explicitly so readers can calibrate trust.

## AI Alignment Writings

Beyond GLUT-of-circuits, niplav maintains a substantial alignment corpus on niplav.site:

- **"Brain-Computer Interfaces and AI Alignment"** — BCI as an alignment-relevant technology pathway
- **"A TAI Race With China Can Be Better Than Not Racing"** — strategic analysis of takeoff dynamics under US-China competition
- **"On Discontinuous and Fast Takeoff"** — takeoff-speed scenarios and their governance implications
- **"Anti-Superpersuasion Interventions"** — defenses against AI persuasion
- **"Patching ~All Security-Relevant Open-Source Software?"** — feasibility of comprehensive OSS security patching
- **"Resolving von Neumann-Morgenstern Inconsistent Preferences"** — decision theory under inconsistent preferences
- **"Cryonics Cost-Benefit Analysis"** — quantified long-termist life-extension analysis

## Forecasting Methodology

- **"On The Effectiveness Of Question Decomposition"** — whether splitting forecasting questions improves accuracy
- **"Subscripts for Probabilities"** — a notation proposal for probability annotations
- **"Precision of Sets of Forecasts"** — aggregation of multiple forecasters
- **"Iqisa: A Library For Handling Forecasting Datasets"** — open-source tooling for forecasting data
- **"Range and Forecasting Accuracy"** — calibration vs. range tradeoffs

## Quantified Self

niplav runs self-experiments selected via prediction platforms:

- **"Using Prediction Platforms to Select Quantified Self Experiments"** — formalizing self-experiment selection with markets
- **"Nootropics"** — tracked cognitive-enhancement experimentation
- **"Have Attention Spans Been Declining?"** — quantitative investigation of a common claim
- **"High Status Eschews Quantification of Performance"** — status dynamics around measurement

## Programming & Mathematics

- **"K-99: Ninety-Nine Klong Problems"** and **"99 Problems Klong Solution"** — Klong (APL-family) programming exercises
- **"Nothing to See Here, Just An Implementation of HodgeRank"** — HodgeRank implementation
- **"Implementing Commutative Hyperoperations"** — mathematics of hyperoperation sequences
- **"How Often Does ¬Correlation ⇏ ¬Causation?"** and **"Logical Correlation"** — statistical-philosophical investigations
- **"t-SNE and UMAP Don't Produce Clusters on Random Data"** — dimensionality-reduction null results
- **"Mugging-Immune Utility Functions"** — decision theory (Pascal's mugging)
- 22 public GitHub repos (github.com/niplav), plus translations (English→German) and transcriptions/archives of other writers' work

## Style & Approach
- Technical rigor grounded in theoretical computer science (circuit complexity, Johnson-Lindenstrauss lemma)
- Probabilistic forecasting (explicit confidence levels: 50%, 65%, 85%)
- Bridge-building between mechanistic interpretability and agent foundations communities
- Willing to stake concrete predictions ("LLMs will plateau")
- **Literate-programming style**: site texts are often "static computational notebooks" — code-driven, with results computed locally and embedded
- **Crocker's rules**: explicitly requests direct, honest feedback; publishes psychological measurements (Big Five: Openness 79%, Conscientiousness 46%, Neuroticism 19%) and track records for calibration
- **Transparent about AI use**: no LLM-generated text unless explicitly designated; AI credited in co-authored work (the GLUT paper is bylined "niplav, Claude+")

## Cross-References

- [[concepts/glut-of-circuits]] — Author of the GLUT-of-circuits model of LLMs
- [[concepts/post-training/rlhf]] — GLUT argues circuits in superposition can be individually aligned via RLHF
- [[concepts/constitutional-ai]] — Related alignment paradigm referenced in the GLUT thesis
- [[concepts/chain-of-thought]] — Depth-limited serial computation as a constraint on LLM capability
- [[entities/gwern]] — Intellectual model: Long Content website format, archiving, and quantified self-tracking

## Sources

- [niplav.site](https://niplav.site/) — main website (created 2019-03-20)
- [About page](https://niplav.site/about.html) — author details, track records, methodology
- [GitHub profile](https://github.com/niplav)
- [LessWrong profile](https://www.lesswrong.com/users/niplav)
- [LLMs as Giant Lookup-Tables of Shallow Circuits](https://www.lesswrong.com/posts/a9KqqgjN8gc3Mzzkh/llms-as-giant-lookup-tables-of-shallow-circuits) (2026-03-17) — raw: [[raw/articles/2026-03-17_lesswrong_giant-lookup-tables-of-shallow-circuits]]
