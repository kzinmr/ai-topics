---
title: "Takuya Akiba (@iwiwi)"
created: 2026-05-28
updated: 2026-05-28
type: entity
tags:
  - person
  - sakana-ai
  - optuna
  - japan
  - kaggle
  - competitive-programming
  - model
  - training
  - evolutionary-algorithms
  - training-efficiency
  - open-source
sources:
  - https://takiba.net/
  - https://www.s.u-tokyo.ac.jp/en/rigakuru/alumni/gc4Ne8rw/
  - https://arxiv.org/abs/2506.14202
  - wiki/raw/papers/2025-06-17_2506.14202_diffusionblocks-block-wise-training.md
---

# Takuya Akiba (@iwiwi)

> **Staff Research Scientist at Sakana AI** (Dec 2023–present). Creator of Optuna, co-creator of ChainerMN. Kaggle Grandmaster, TopCoder legend. PhD from the University of Tokyo.

## Quick Profile

| Attribute | Detail |
|---|---|
| **Name** | Takuya Akiba |
| **Current Role** | Staff Research Scientist, Sakana AI (Dec 2023–present) |
| **Previous Roles** | Stability AI, Preferred Networks (VP of ML Infrastructure), NII Assistant Professor |
| **Education** | PhD Computer Science, University of Tokyo (2015, Dean's Award, completed in 2 years) |
| **GitHub** | [@iwiwi](https://github.com/iwiwi) |
| **Twitter/X** | [@iwiwi](https://twitter.com/iwiwi) |
| **Website** | [takiba.net](https://takiba.net/) |
| **Google Scholar** | [Takuya Akiba](https://scholar.google.com/citations?user=WW-22F8AAAAJ) |
| **Kaggle** | [takuyaakiba](https://www.kaggle.com/takuyaakiba) — Grandmaster (2019) |

## Overview

Takuya Akiba is a Japanese deep learning researcher and engineer with a uniquely broad technical profile spanning competitive programming, distributed systems, hyperparameter optimization, and generative AI. He is best known as the creator of **Optuna** (KDD 2019, ~14K GitHub stars, ~3,900 citations), the define-by-run hyperparameter optimization framework that became an industry standard. He also co-created **ChainerMN**, which scaled ResNet-50 training on ImageNet to 1,024 GPUs — a world record at the time.

His career reflects two deliberate shifts: from classical algorithms research to deep learning (around 2016), and then into generative AI/LLMs (2023 at Sakana AI). Throughout, he has prioritized competing on **ingenuity over data scale**, a philosophy that aligns with Sakana AI's nature-inspired, Scaling Law-defying vision.

## Professional Timeline

| Period | Role | Organization | Key Focus |
|---|---|---|---|
| **Dec 2023–present** | Staff Research Scientist | Sakana AI | Foundation models, nature-inspired AI, evolutionary model merging, DiffusionBlocks |
| **Jun–Nov 2023** | Senior Research Scientist | Stability AI | Japanese StableLM series, LLM training |
| **May 2018–Mar 2022** | VP of ML Infrastructure | Preferred Networks | Led 20+ engineers across 4 teams (DL framework, MN-Core compiler, Optuna, HPC) |
| **Jul 2016–Jul 2018** | Researcher | Preferred Networks | ChainerMN, distributed DL research, Kaggle competitions |
| **Apr 2015–Jun 2016** | Assistant Professor | National Institute of Informatics (NII) | Large-scale graph data structures and algorithms |
| **Earlier** | Internships | Google, Microsoft Research Asia, Microsoft Research SVC | — |

## Major Contributions

### Optuna — Hyperparameter Optimization Framework (KDD 2019)

Akiba proposed, designed, and implemented Optuna at Preferred Networks. It introduced the **define-by-run** API paradigm for hyperparameter optimization, allowing users to construct search spaces dynamically rather than statically declaring them upfront.

- **KDD 2019 paper**: ~3,900 citations
- **GitHub**: ~14K stars, 320+ contributors
- **Key features**: define-by-run search spaces, efficient sampling + pruning (TPE, CMA-ES, etc.), large-scale distributed optimization, interactive visualization dashboard
- **License**: MIT
- **Impact**: Adopted as the primary HPO tool across the ML ecosystem; integrated with PyTorch, TensorFlow, Hugging Face, and MLflow

> *"Optuna offers several unique features that previous frameworks lacked. These features include a flexible define-by-run style search space description and a combination of sampling and pruning for efficient optimization."* — Akiba, takiba.net

### ChainerMN — Scalable Distributed Deep Learning

At Preferred Networks, Akiba established the methodology for large-scale parallel deep learning. He made the prescient decision to prioritize **synchronous SGD over async SGD** for image classification tasks — a choice that proved correct as sync SGD became the dominant approach.

- Designed and implemented ChainerMN, the distributed training extension for the Chainer framework
- Enabled training at 128+ GPU scale with 90% parallel efficiency
- Led to Preferred Networks building MN-1, MN-2, MN-3 supercomputers and the MN-Core ASIC

### ResNet-50 on ImageNet in 15 Minutes (World Record)

Proposed and led the challenge to train ImageNet ResNet-50 in **15 minutes using 1,024 GPUs** — the world's fastest record at the time. This required overcoming hardware failures and middleware bugs to demonstrate ChainerMN's scalability at extreme scale.

### PFDet — 2nd Place Open Images Challenge 2018 (CVPR 2019)

Led a team of 6 to build a large-scale object detection system using **512 GPUs** via ChainerMN. Achieved 2nd place in the Open Images Challenge object detection track. Published at CVPR 2019.

### Evolutionary Model Merging (2024, Nature Machine Intelligence 2025)

At Sakana AI, Akiba co-authored the **Evolutionary Model Merge** method, which uses evolutionary algorithms to automatically discover optimal combinations of open-source models. The approach produced **EvoLLM-JP** (Japanese Math LLM) and **EvoVLM-JP** (culturally-aware Japanese VLM), both achieving state-of-the-art results surpassing models with far more parameters.

- Published in Nature Machine Intelligence (Jan 2025)
- Implemented in mergekit and Optuna Hub
- Spawned follow-up work including CycleQD (ICLR 2025) and Natural Niches

### DiffusionBlocks — Block-wise Training (ICLR 2026)

Co-authored with Makoto Shing and Masanori Koyama. DiffusionBlocks transforms residual networks into genuinely independent trainable blocks by reinterpreting residual connections as Euler discretization of a diffusion process. Reduces memory requirements proportionally to the number of blocks while maintaining competitive performance with end-to-end training.

- Accepted at ICLR 2026
- Source: `[[wiki/raw/papers/2025-06-17_2506.14202_diffusionblocks-block-wise-training]]`

### Japanese StableLM Series (2023)

At Stability AI, Akiba led continued pre-training of Japanese language models. The Japanese StableLM-3B-4E1T model transferred knowledge from an English base model to Japanese via continued pre-training on ~100B Japanese tokens.

## Competitive Programming & Kaggle

### Competitive Programming
One of the world's elite competitive programmers during the 2010s:

| Achievement | Year | Detail |
|---|---|---|
| **TopCoder** | — | Max rating 3,292 (**4th worldwide**) |
| **ACM ICPC World Finals** | 2012 | **Bronze medal** (3rd place) |
| **Google Code Jam** | 2010 | **9th place** worldwide |
| Google Code Jam | 2014 | 15th place |
| ICFP Contest | 2013 | Finalist |

### Kaggle
- **Grandmaster** since 2019
- **6 gold medals**, including **1 solo gold**
- Focused primarily on deep learning competitions
- Started Kaggle in 2016 as part of his transition into deep learning

> *"I started Kaggle in 2016 and became a Kaggle Grandmaster in 2019. I mainly participated in deep learning contests."* — takiba.net

## Books

- **Algorithms for Competitive Programmers** (Japanese) — Co-authored; translated into Korean, Chinese, and Taiwanese
- **Kaggle** book (Japanese, Kodansha) — Co-authored guide to deep learning competitions
- **Optuna** book (Japanese) — Co-authored ML optimization guide

## Research Philosophy

Akiba's career is defined by two deliberate shifts driven by a consistent principle: **compete on ingenuity, not scale**.

1. **Algorithms → Deep Learning (2016)**: After his PhD and NII position, Akiba felt important algorithmic problems were being solved. Deep learning was producing results, and he saw an opportunity for impact. He learned from scratch, emphasizing **reading source code** over textbooks alone.

2. **Deep Learning → Generative AI (2023)**: Joined Sakana AI with zero LLM experience, confident that fundamentals matter more than domain-specific knowledge. His critique of Scaling Laws captures his philosophy:

   > *"The more data we put into generative AI, the better it gets. That is guaranteed in the future. Of course, it is a lot of work because of the scale, but algorithmically it is only an extension of what has been done so far. There is no special creativity; everyone is doing pretty much the same thing."*

   Sakana AI's vision of **nature-inspired AI** that breaks away from Scaling Laws aligns with this ethos:

   > *"We can compete based on people's ingenuity rather than the amount of data we put in. It is putting my own skills to the test."*

**Learning approach**: Beyond textbooks and papers, Akiba emphasizes reading source code as the ultimate blueprint — "computers cannot read between the lines, so there are no such spaces in the source code either."

## Selected Papers

- **Optuna: A Next-generation Hyperparameter Optimization Framework** — KDD 2019. ~3,900 citations.
- **ChainerMN: Scalable Distributed Deep Learning Framework** — arXiv 2017.
- **PFDet: 2nd Place Solution to Open Images Challenge 2018** — CVPR 2019 workshop.
- **Extremely Large Minibatch SGD: Training ResNet-50 on ImageNet in 15 Minutes** — arXiv 2017.
- **A Graph Theoretic Framework of Recomputation Algorithms for Memory-Efficient Backpropagation** — NeurIPS 2019.
- **MN-Core: A Highly Efficient and Scalable Approach to Deep Learning** — VLSI Circuits 2021.
- **Evolutionary Optimization of Model Merging Recipes** — Nature Machine Intelligence, 2025 (arXiv 2024).
- **DiffusionBlocks: Block-wise Neural Network Training via Diffusion Interpretation** — ICLR 2026.

## Related Pages

- [[entities/sakana-ai]] — Sakana AI, Tokyo-based nature-inspired AI lab (to be created)
- [[concepts/diffusionblocks]] — DiffusionBlocks block-wise training method (to be created)
- [[concepts/optuna]] — Optuna hyperparameter optimization framework (to be created)
- [[concepts/evolutionary-algorithms]] — Evolutionary algorithms in AI
- [[concepts/distributed-training]] — Distributed deep learning training
- [[concepts/training-efficiency]] — Training efficiency methods and techniques

## External Links

- Personal website: https://takiba.net/
- GitHub: https://github.com/iwiwi
- Google Scholar: https://scholar.google.com/citations?user=WW-22F8AAAAJ
- Kaggle: https://www.kaggle.com/takuyaakiba
- DiffusionBlocks code: https://github.com/SakanaAI/DiffusionBlocks
- Evolutionary Model Merge code: https://github.com/SakanaAI/evolutionary-model-merge
- UTokyo RIGAKU-RU interview (2024): https://www.s.u-tokyo.ac.jp/en/rigakuru/alumni/gc4Ne8rw/
