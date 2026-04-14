---
title: Corbett (Kyle Corbitt)
created: 2026-04-10
updated: 2026-04-10
tags:
- x-account
- ai
- startups
- fine-tuning
- rl
- openpipe
- coreweave
aliases:
- '@corbtt'
- kcorbitt
- Kyle Corbitt
source: x-account
---

# Corbett (Kyle Corbitt)

| | |
|---|---|
| **X/Twitter** | [@corbtt](https://x.com/corbtt) |
| **Blog** | [corbt.com](https://corbt.com) |
| **GitHub** | [github.com/kcorbitt](https://github.com/kcorbitt) |
| **Role** | Head of OpenPipe Team at CoreWeave; former YC Director, Google engineer |
| **Location** | Bellevue, WA |
| **Notable for** | OpenPipe founder, Serverless RL, ART library, Startup School at YC |

## Overview

Kyle Corbitt (known as "Corbett" on X/Twitter, handle @corbtt) is a serial entrepreneur and engineer focused on making AI model fine-tuning and reinforcement learning accessible to developers. He is currently **Head of the OpenPipe Team at CoreWeave** (following CoreWeave's acquisition of OpenPipe in September 2025). Previously, he was **Director of Startup School at Y Combinator**, where he led the team that increased YC applications by over 40%.

Corbitt's career spans Google (software engineer, 2016-2017), Y Combinator (2017-2021), founding GenerationalStory (2022-2023), and most notably **OpenPipe** (2023-2025) — a platform for converting expensive LLM prompts into cheap, fast fine-tuned models using supervised fine-tuning (SFT) and reinforcement learning (RL).

## Timeline

| Date | Event |
|------|-------|
| 2010-2014 | Studied at Brigham Young University |
| 2016 | Interned at Google |
| Nov 2016 – Aug 2017 | Software Engineer at Google |
| Aug 2017 – Mar 2020 | Senior Engineer at Y Combinator |
| Mar 2020 – Dec 2021 | Director of Startup School at YC; built Startupschool.org |
| 2021 | Co-founded Taxy.AI (one of the first web agents on GPT-4) |
| Jul 2022 – Jul 2023 | Co-founded GenerationalStory |
| Jun 2023 | Founded **OpenPipe** (YC S23 batch) |
| Mar 2024 | OpenPipe raised $6.2M seed from CRV |
| 2024 | Released **ART** (Agent Reinforcement Trainer) library for RL-based agent training |
| 2024 | Presented at TechCrunch on OpenPipe's vision |
| Sep 2025 | OpenPipe acquired by CoreWeave; Corbitt became Head of OpenPipe Team |
| 2025 | Launched **Serverless RL** — making reinforcement learning for agents faster and cheaper |

## Core Ideas

### Fine-Tuning as the Bridge Between Prototyping and Production

Corbitt's core thesis at OpenPipe is that fine-tuning is the missing link between expensive prototype models and production-ready systems. OpenPipe's platform captures prompt-completion pairs from existing LLM providers (OpenAI, Anthropic, etc.) and uses them to fine-tune smaller, cheaper open-weight models (Mistral 7B, Llama 3, etc.) to match or exceed the original model's performance on specific tasks.

> "OpenPipe lets you capture your existing provider's prompt-completion pairs, pick a base model, and OpenPipe does the rest — at the click of a button."

### Reinforcement Learning for AI Agents

With the **ART (Agent Reinforcement Trainer)** library, Corbitt pioneered accessible RL training for autonomous agents. ART enables developers to:
- Train agents using reinforcement learning without specialized ML expertise
- Improve agent reliability, reduce latency, and lower costs
- Use serverless infrastructure so there's no GPU management overhead

His 2025 launch of **Serverless RL** was a significant milestone — making RL accessible to teams without dedicated ML infrastructure.

### The "Bitter Lesson" Applied to AI Engineering

Corbitt is a vocal advocate of Rich Sutton's "Bitter Lesson" — the idea that general methods leveraging computation scale better than hand-crafted approaches. At OpenPipe, this manifests as:
- Using large, expensive models to generate training data
- Fine-tuning smaller models on that data
- Iterating rapidly with RL to improve performance

### Open Source as a Competitive Advantage

Unlike many AI startups that keep their technology proprietary, OpenPipe has consistently released open-source libraries (ART, SDK wrappers) and contributes to the broader ML engineering community. Corbitt believes that open-source tools accelerate adoption and create network effects that benefit the entire ecosystem.

## Key Projects

| Project | Description |
|---------|-------------|
| **OpenPipe** | Platform for fine-tuning LLMs using prompt-completion pairs; acquired by CoreWeave |
| **ART (Agent Reinforcement Trainer)** | Open-source RL library for training AI agents |
| **Serverless RL** | Cloud-based RL training with zero infrastructure management |
| **Taxy.AI** | Early web agent built on GPT-4 (2021) |
| **Startupschool.org** | YC's largest founder community platform (increased applications 40%) |

## Key Quotes

> "We've barely scratched the surface of what RL can do, and in the coming months we'll be moving even faster." — On OpenPipe joining CoreWeave (September 2025)

> "OpenPipe is an SDK that abstracts away fine-tuning custom models. We capture your existing provider's prompt-completion pairs and use them to train smaller, cheaper models." — On OpenPipe's core value proposition

## Related

- [[concepts/fine-tuning]] — Model customization via supervised fine-tuning
- [[concepts/reinforcement-learning]] — RL training for AI agents
- [[entities/coreweave]] — Acquired OpenPipe in 2025
- [[entities/y-combinator]] — Corbitt's former employer (Startup School Director)
- [[concepts/bitter-lesson]] — Philosophy underlying OpenPipe's approach

## Sources

- [OpenPipe website](https://openpipe.ai)
- [OpenPipe at Y Combinator](https://www.ycombinator.com/companies/openpipe)
- [OpenPipe is Joining CoreWeave — Kyle Corbitt's blog post](https://corbt.com/posts/openpipe-coreweave)
- [Kyle Corbitt on LinkedIn](https://linkedin.com/in/kcorbitt)
- [Tejas Kumar podcast with Kyle Corbitt](https://www.youtube.com/watch?v=KsG-8xyM9A8)
- [OpenPipe raises $6.2M — GeekWire](https://www.geekwire.com/2024/seattle-startup-openpipe-raises-6-2m/)
- [ART library on GitHub](https://github.com/openpipe/art)
