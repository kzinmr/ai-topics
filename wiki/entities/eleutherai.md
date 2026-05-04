---
title: EleutherAI
description: Grassroots research collective turned non-profit that started the modern open-source AI movement
url: https://www.eleuther.ai/
type: entity
created: 2026-05-04
updated: 2026-05-04
aliases:
  - EleutherAI
  - EAI
tags:
  - organization
  - open-source
  - evaluation
  - lm-eval
  - research-collective
sources:
  - https://www.eleuther.ai/
  - https://github.com/EleutherAI
  - https://huggingface.co/EleutherAI
  - raw/papers/2024-05-23_2405.14782_lessons-from-the-trenches.md
---

# EleutherAI

**EleutherAI** is a grassroots research collective turned non-profit research institute that started the modern open-source AI movement. Known for releasing foundational open-source models and infrastructure tools, EleutherAI's work has been widely adopted across academia and industry.

## Key Projects

### Models
- **GPT-Neo / GPT-NeoX-20B** — Early open-source LLMs that bridged the gap after GPT-3
- **Pythia** — Suite of 16 LLMs (70M–12B) for studying training dynamics (ICML 2023)
- **BLOOM** — 176B parameter multilingual LLM (BigScience collaboration)
- **Llemma** — Open language model for mathematics

### Infrastructure
- **[[concepts/llm-evaluation-harness|LM Evaluation Harness]]** (lm-eval) — Industry-standard evaluation library for LLMs (200+ tasks)
- **The Pile** — 800GB diverse text dataset for language modeling
- **OpenFold** — Open-source protein folding model

## Governance

- **Executive Director:** [[entities/stella-biderman|Stella Biderman]] — Transitioned the collective from grassroots to non-profit (2023)
- **Research Scientists:** [[entities/hailey-schoelkopf|Hailey Schoelkopf]] (lm-eval maintainer), and others

## Impact

EleutherAI's tools and models have become foundational infrastructure for open-source AI research:
- lm-eval powers the Hugging Face [[concepts/open-llm-leaderboard|Open LLM Leaderboard]]
- The Pile is the most widely used open training corpus
- Pythia enabled systematic study of LLM training dynamics at ICML 2023
- Over 4,500 datasets in the Open LLM Leaderboard ecosystem

## Cross-References

- **[[entities/stella-biderman]]** — Executive Director
- **[[entities/hailey-schoelkopf]]** — Research Scientist
- **[[concepts/llm-evaluation-harness]]** — Flagship tool
- **[[concepts/open-llm-leaderboard]]** — Uses EleutherAI's lm-eval
