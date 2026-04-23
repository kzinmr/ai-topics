---
name: abacaj
updated: 2026-04-10
tags:
- ml-engineer
- open-source
- llm
- post-training
- ai2
- olmo
---

# abacaj

## Info

| Field | Value |
|-------|-------|
| **Name** | Anton Bacaj |
| **X** | [@abacaj](https://x.com/abacaj) (48K followers) |
| **GitHub** | [abacaj](https://github.com/abacaj) (393 followers, 38 public repos, 507 contributions) |
| **YouTube** | [Anton Bacaj](https://youtube.com/@AntonBacaj) |
| **LinkedIn** | [anton-bacaj](https://linkedin.com/in/anton-bacaj-8699a148) (1,182 followers) |
| **Website** | [arlanrakh.com](https://www.arlanrakh.com/) |
| **Role** | ML Engineer, Post-Training Specialist, Open-Source Contributor |
| **Languages** | English, Albanian |
| **Education** | BBA Business Management (Iona University, 2008–2012), MS Computer Science (CUNY Herbert H. Lehman College, 2014–2016) |

## Overview

Anton Bacaj is a software engineer and ML practitioner known for his open-source contributions in large language model fine-tuning, evaluation, and inference optimization. He has worked at Jet.com (2015–2021), Nines (2021–2023), and is currently at Something New AI, a stealth startup focused on LLM applications.

Bacaj's GitHub repositories — including `fine-tune-mistral` (724 stars), `awesome-transformers` (680 stars), and `code-eval` (430 stars) — are widely used by the open-source ML community for practical LLM development work. He is particularly active in the post-training and fine-tuning space, having contributed to and advocated for the OLMo model flow at AI2.

## Timeline

| Date | Event |
|------|-------|
| 2008–2012 | BBA Business Management, Iona University |
| 2012–2013 | Software engineering internship at PolicyGenius |
| 2014–2016 | MS Computer Science, CUNY Herbert H. Lehman College |
| 2015 | Joined Jet.com as Software Engineer |
| 2015–2018 | Software Engineer, Jet.com (Walmart-owned) |
| 2018–2020 | Senior Software Engineer, Jet.com |
| 2020–2021 | Staff Software Engineer, Jet.com |
| Sep 2021 | Joined Nines as Engineer |
| Sep 2021 – Sep 2023 | Engineering, Nines (consumer services startup) |
| 2022-01 | Published Flan-T5 fine-tuning guidance widely cited by community |
| Sep 2023 | Co-founded Something New AI (stealth startup) |
| Sep 2023 – Present | LLMs at Something New AI |
| 2023-04 | Created `awesome-transformers` (680 stars) |
| 2023-06 | Released `mpt-30B-inference` (576 stars) — CPU inference for MPT-30B |
| 2023-07 | Released `replit-3B-inference` (160 stars) — CPU inference for Replit Code 3B |
| 2023-09 | Released `code-eval` (430 stars) — HumanEval benchmark for LLMs |
| 2023-10 | Released `fine-tune-mistral` (724 stars) — Full fine-tuning of Mistral-7B |
| 2023-10 | Published `abacaj/mistral-7b-sft` on HuggingFace |
| 2023-12 | Released `unofficial-chatgpt-api` (68 stars) — Node.js ChatGPT client |
| 2024-07 | Updated `chatgpt-backup` (275 stars) — Client-side ChatGPT history backup |
| 2025–2026 | Active contributor and advocate for AI2's OLMo 3 project |

## Core Ideas

### Open-Source Model Fine-Tuning

Bacaj is a vocal advocate for full fine-tuning over parameter-efficient methods like QLoRA. His `fine-tune-mistral` repository provides a clean, production-ready pipeline for full fine-tuning of Mistral-7B on consumer and datacenter GPUs (RTX 3090s, A100s, H100s). His approach emphasizes:

- Using sufficient data (>1k samples, ideally 40k+ for quality results)
- Running multiple epochs with held-out evaluation data
- Lowering learning rate when batch size is constrained
- Avoiding overfitting through proper validation

> "If running with a small batch size, lower the learning rate. Use enough data — I recommend >1k samples. I ran this for 3 epochs on 40k samples, will need to experiment more on epochs because the model was still improving."

### Model Flow Transparency

Bacaj has been an active participant in the AI2 OLMo ecosystem, advocating for complete transparency in model development. The OLMo "Model Flow" concept — which exposes every stage from pretraining through post-training with full checkpoints, datasets, and recipes — aligns with his philosophy that the ML community needs visibility into the entire training pipeline, not just final weights.

### CPU Inference Democratization

Two of his repositories (`mpt-30B-inference` and `replit-3B-inference`) focus on running large models on CPU hardware, lowering the barrier to experimentation for developers without access to expensive GPUs. This reflects a broader philosophy of making AI accessible to individual practitioners.

### Specialized Small Models Over General Large Models

Bacaj has consistently advocated for fine-tuning smaller models for specific tasks rather than relying on massive general-purpose models:

> "More I use flan-t5, more I realize Google has given us something very powerful. Best to think of it as a smaller model that can be specialized, won't do everything out of the box. Training multiple flan-t5s and coordinating them for a larger task is the way."

### Practical ML Engineering

His body of work reflects a pragmatic approach to ML: building tools that solve real problems for real developers. From ChatGPT backup utilities to LLM evaluation benchmarks, his contributions are characterized by minimalism and immediate utility.

## Key Quotes

> "Make the models cheap to use. Great, they all forgot how to code. Now 10x the price." — @abacaj on X, April 2026

> "More I use flan-t5, more I realize Google has given us something very powerful. Best to think of it as a smaller model that can be specialized, won't do everything out of the box. Training multiple flan-t5s and coordinating them for a larger task is the way." — January 2023

> "Opus 4.1 is still really good. I don't think any new model has replaced it yet for me." — December 2025

> "I've had very little success fine tuning over gpt-oss models and very much success with qwen3 models (even the instruction versions). Not sure if this is a case of skill issue or what, but they are not as friendly." — December 2025

## Projects

| Project | Description | Stars |
|---------|-------------|-------|
| [fine-tune-mistral](https://github.com/abacaj/fine-tune-mistral) | Full fine-tuning of Mistral-7B on 3090s, A100s, H100s | 724 |
| [awesome-transformers](https://github.com/abacaj/awesome-transformers) | Curated list of transformer models | 680 |
| [mpt-30B-inference](https://github.com/abacaj/mpt-30B-inference) | CPU inference for MPT-30B | 576 |
| [code-eval](https://github.com/abacaj/code-eval) | HumanEval benchmark for LLMs | 430 |
| [chatgpt-backup](https://github.com/abacaj/chatgpt-backup) | Client-side ChatGPT conversation backup | 275 |
| [replit-3B-inference](https://github.com/abacaj/replit-3B-inference) | CPU inference for Replit Code 3B | 160 |
| [unofficial-chatgpt-api](https://github.com/abacaj/unofficial-chatgpt-api) | Node.js ChatGPT API client | 68 |

## Related

- [[ai2]] — Creator of OLMo, where Bacaj contributes post-training expertise
- [[olmo]] — Open language model with transparent training pipeline
- [[mistral-ai]] — Fine-tuning target for his most popular repository
- [[anthropic]] — Preferred model provider (Opus 4.1)
- [[entities/qwen3-6-plus.md]] — High-quality open model for fine-tuning

## Sources

- [GitHub Profile](https://github.com/abacaj)
- [LinkedIn Profile](https://linkedin.com/in/anton-bacaj-8699a148)
- [HuggingFace Profile](https://huggingface.co/abacaj)
- [X/Twitter Profile](https://x.com/abacaj)
- [fine-tune-mistral Repository](https://github.com/abacaj/fine-tune-mistral)
- [Ai2 OLMo Documentation](https://allenai.org/olmo)
