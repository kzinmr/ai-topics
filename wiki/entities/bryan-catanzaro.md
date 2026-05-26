---
title: Bryan Catanzaro
type: entity
created: 2026-05-26
updated: 2026-05-26
tags:
  - person
  - nvidia
  - researcher
  - open-source
  - ai-infrastructure
  - ml-engineering
aliases:
  - @ctnzr
sources:
  - raw/articles/substack.com--redirect-fc937db9-1f9f-4d17-8d14-568f58e27526--f7737c4f.md
  - https://www.linkedin.com/in/bryan-catanzaro/
  - https://scholar.google.com/citations?user=ctnzr
---

# Bryan Catanzaro

**Bryan Catanzaro** (X: [@ctnzr](https://x.com/ctnzr)) is Vice President of Applied Deep Learning Research (ADLR) at NVIDIA, where he leads the Nemotron open model development effort. He oversees a team of ~500 technical staff working on models, datasets, training recipes, and inference optimization.

## Overview

Catanzaro has been at NVIDIA since 2008 (with a 2014–2016 departure to Baidu's Silicon Valley AI Lab). He holds a PhD from UC Berkeley in electrical engineering and computer science. He is a key architect of NVIDIA's open model strategy, arguing that "AI is a form of infrastructure" that should be openly developed so organizations across every sector can customize it for their specific needs.

## Career Timeline

### UC Berkeley PhD (2006–2008)
- Worked on machine learning on FPGAs before discovering CUDA
- David Kirk (NVIDIA Chief Scientist) visited Berkeley and encouraged CUDA experimentation
- Catanzaro rewrote SVM training code in CUDA and achieved 200× speedup over single-threaded CPU
- Published first paper at ICML 2008 on GPU-based SVM training

### NVIDIA — Early Years (2008–2014)
- Joined NVIDIA research organization
- Helped build cuDNN and other deep learning libraries
- Advocated for GPU-based ML when it was an unpopular position in the academic community
- "I was a little bit caught in between different fields — the systems people didn't think I was systems enough, and the machine learning people didn't think I was machine learning enough"

### Baidu Silicon Valley AI Lab (2014–2016)
- Worked under Andrew Ng alongside Dario Amodei and Awni Hannun
- Learned large-scale applied ML for business problems
- Returned to NVIDIA after hitting limits of what could be done at a Chinese company in California

### NVIDIA — Applied Deep Learning Research (2016–present)
- Recruited by Jensen Huang to build an applied research lab
- Led development of **Megatron-LM** (2019+) — model parallelism framework for training large transformers
- Led **NeMo Framework** — end-to-end LLM stack for training, evaluation, deployment
- **DLSS** — AI-powered graphics rendering (15 of every 16 pixels gamers see are now rendered by AI models from his team)
- **Nemotron** — open model family (2023–present), leading the 500+ person effort

## Nemotron Open Model Strategy (2025–2026)

Catanzaro articulated NVIDIA's rationale for open models in the January 2026 Interconnects podcast interview with Nathan Lambert:

### "AI as Infrastructure" Thesis
> "NVIDIA believes that AI is a form of infrastructure. It's a very useful technology when it's applied, but on its own it's kind of a foundation and infrastructure. We think that technology generally works better when there's openness to the infrastructure so that people can build things in different ways."

He compares this to the internet's transformation of the economy: different sectors incorporated it in different ways because the internet was built on open technologies. AI will evolve similarly.

### Two Jobs of Nemotron
1. **Systems R&D** — Understanding AI workloads to design better NVIDIA hardware (GPUs, interconnects, memory). "We can't just go to our customers and do a survey... the information that influences the design of these systems is very expensive to derive, and so therefore it's very closely held."
2. **Ecosystem support** — Enabling the broader AI ecosystem to grow, which drives NVIDIA's business. "Whenever AI is able to grow in any sort of direction, in any capability, then that's an opportunity for us to grow our business."

### Open Datasets Strategy
NVIDIA began releasing pretraining datasets in 2025 (CC-v2, CC-Math-v1, etc.), taking on legal risk that few other companies accept. Catanzaro: "Nemotron is not just a model... what we're trying to do is support openly developed AI... we do a lot of expensive experiments in order to figure out how to do blending for our datasets or to optimize our settings. We're very happy for other people to pick that up and run with it."

### "Invitation, Not Control" Organizational Philosophy
Managing 500+ full-time contributors (2,000+ interested) at NVIDIA requires a decentralized, volunteer-based culture:
- **"Pilot in Command"** structure: 20 area leaders, each responsible for a specific Nemotron component
- **Integration studies** over ablations: "Rather than isolating the particular contribution of one idea, integration studies are about putting a hundred ideas together and seeing if they're better than what we had before"
- Open internal idea submission with unique identifiers
- "Nemotron is better together" — coordination over independent publication

### "Potential Energy" Analogy for Open Models
> "Intelligence is kind of like a potential energy — it's not a kinetic energy. In order to transform intelligence into kinetic energy, it needs to have a platform. It needs to be applied in the proper way... I believe every company, every organization, has secrets that only they know. They have special data, they have special ways of thinking about their problems, their customers, their solutions, and they're gonna know how to apply AI better than anyone else."

### Intelligence-per-Second Thesis
Catanzaro's prediction for AI's future direction: "The way to think about AI is not just in terms of absolute intelligence, but rather intelligence per second... models that incorporate this compute acceleration characteristic, where they're thinking about intelligence per unit time, those are gonna end up winning because they end up being trained on more data, they end up being post-trained with more cycles."

## Megatron-LM Evolution

- **2019**: First public release, focused on demonstrating NVIDIA systems for transformers
- **2020s**: Evolved from "hard to use" research tool to industry standard
- **Current**: Software engineering shared across ~4 NVIDIA teams; Megatron Core is the "especially protected" subset
- Catanzaro named it: "I came up with the name Megatron. One of my proudest moments, I suppose. I was thinking about it — this is a really big transformer. What's the biggest and baddest transformer? Oh, it's Megatron."
- Nemotron 3 Super and Ultra models trained using FP4 precision on Megatron + Transformer Engine

## Key Publications & Projects

| Year | Project | Description |
|------|---------|-------------|
| 2008 | GPU SVM Training | ICML paper on parallel SVM training |
| 2019 | Megatron-LM | Model parallelism framework for large transformers |
| 2020s | NeMo Framework | End-to-end LLM training/evaluation/deployment stack |
| 2023 | DLSS 3.x | AI rendering for gaming (15/16 pixels AI-generated) |
| 2023–2026 | Nemotron Family | Open model series (Nano, Super, Ultra, Cascade, Labs-Diffusion) |
| 2025 | Nemotron Datasets | Pretraining datasets (CC-v2, CC-Math-v1, etc.) |

## Career Philosophy

- **Follow your convictions**: "I've done a lot of unpopular things during my career because I believed in them"
- **Choose your tribe**: "The people that you work with, the community that you work with has a big impact on the problems you think about and then the impact that your work has"
- **Stay ahead of trends**: "If you want to change the world, you need to be ahead of the trends... trends in computing are not just fashion. There's truth that drives those trends"
- **Against AGI eventism**: "I believe AI is more like infrastructure than the singularity... I don't believe in AI as an event that one day makes everyone obsolete"

## Cross-References

- [[entities/nvidia]] — Employer; Catanzaro leads Nemotron open model effort
- [[entities/megatron-lm]] — Training framework he named and helped develop
- [[concepts/nemotron-family]] — Open model series under his leadership
- [[entities/nathan-lambert]] — Interviewed Catanzaro on Interconnects podcast (Jan 2026)

## Sources

- [Interconnects Podcast — "Why Nvidia builds open models with Bryan Catanzaro"](https://substack.com/redirect/fc937db9-1f9f-4d17-8d14-568f58e27526) (Jan 2026) — Full transcript interview with Nathan Lambert
- [LinkedIn](https://www.linkedin.com/in/bryan-catanzaro/)
- [Google Scholar](https://scholar.google.com/citations?user=ctnzr)
