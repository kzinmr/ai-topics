---
title: Eric Hartford
type: entity
handle: "@QuixiAI"
created: 2026-04-10
updated: 2026-04-10
tags:
  - person
  - ai
  - open-source-models
  - fine-tuning
  - uncensored-models
  - huggingface
  - cognitive-computations
sources: []
---


# Eric Hartford (@QuixiAI)

| | |
|---|---|
| **X** | [@QuixiAI](https://x.com/QuixiAI) |
| **Blog** | [erichartford.com](https://erichartford.com) |
| **GitHub** | [ehartford](https://github.com/ehartford) |
| **Hugging Face** | [cognitivecomputations](https://huggingface.co/cognitivecomputations) |
| **Ko-fi** | [erichartford](https://ko-fi.com/erichartford) |
| **Role** | Applied AI Researcher, Open-Source Model Creator |
| **Known for** | Dolphin model series, uncensored AI advocacy, Samantha models |
| **Bio** | Eric Hartford is an applied AI researcher and the creator of the Dolphin family of open-source, uncensored language models. He leads the Cognitive Computations project, which produces instruct-tuned models designed to be freely composable with custom alignment layers. A vocal advocate for open-source AI and user choice in model behavior, Hartford has been a central figure in the open-weights community since the early days of LLaMA fine-tuning in 2023. |

## Overview

Eric Hartford is one of the most prominent independent creators in the open-source LLM fine-tuning ecosystem. He is best known as the creator of the **Dolphin** series of models — uncensored, instruction-tuned language models based on architectures from Microsoft's Orca research. The Dolphin models are trained on massive datasets (~1 million FLANv2 entries augmented with GPT-4 completions and ~3.5 million with GPT-3.5 completions) with deliberate removal of refusals, alignment behaviors, and ideological bias. The goal is to produce a neutral base that users can layer their own alignment preferences onto via LoRA.

Hartford operates under the **Cognitive Computations** brand on Hugging Face, where his models have accumulated tens of thousands of downloads. His work was notably sponsored by **a16z**, which provided compute budget for model training. Beyond Dolphin, he also created the **Samantha** series of companion AI models, the **Based-30b** experiment, and numerous Wizard-Vicuna uncensored variants. His blog at erichartford.com serves as a primary technical resource for the open-source AI community, documenting everything from fine-tuning pipelines to hardware benchmarks on AMD's MI300X GPUs.

His advocacy for uncensored models is grounded in a philosophy of **composable alignment** — the idea that there is no single "correct" set of values for an AI to embody, and that open source should enable every demographic and interest group to customize their own models. As he puts it: *"It's my computer, it should do what I want."* This stance has made him a controversial but influential figure in debates about AI safety, freedom, and open-source governance.

## Core Ideas

### Uncensored Models & Composable Alignment

Hartford's central thesis is that alignment should be **user-controlled and modular**, not baked into the base model by a single organization. In his influential essay "Uncensored Models" (May 2023), he argues that open-source models fine-tuned on ChatGPT-generated datasets inherit OpenAI's alignment preferences — reflecting American popular culture, US law, and liberal/progressive values — which may not be appropriate for all users or use cases.

His strategy for uncensoring is methodical:
1. **Filter the dataset** — Identify and remove refusal responses and biased answers from instruction datasets
2. **Fine-tune the base model** — Train on the cleaned dataset using the original methodology
3. **Release openly** — Publish the unaligned model for community customization

> "Every demographic and interest group deserves their model. Open source is about letting people choose. The only way forward is composable alignment. To pretend otherwise is to prove yourself an ideologue and a dogmatist." — Eric Hartford, "Uncensored Models" (2023)

### Open-Source AI Philosophy

Hartford believes that **local AI should not override user intent or act as a moral arbiter**. Valid use cases for uncensored models include creative writing (depicting villains, dark themes), roleplay, academic research, and intellectual exploration. His position is that knowing *how* to do something is not the same as *intending* to do it, and that filtering information at the model level is a form of paternalism incompatible with open-source principles.

### The Dolphin Dataset Approach

Inspired by Microsoft's **Orca paper** (Mukherjee et al.), Hartford replicated and extended the methodology for open-source models. The Dolphin dataset combines ~1 million FLANv2 entries with GPT-4 completions and ~3.5 million with GPT-3.5 completions, then systematically filters out refusals, avoidance behaviors, and bias. The dataset is released under the **Apache-2.0 license** for both commercial and non-commercial use, with the trained models subject to their base model's license terms.

### Practical AI Engineering

Beyond philosophy, Hartford is a hands-on practitioner. His blog documents detailed technical work including:
- Fine-tuning pipelines using **Axolotl** on AMD ROCm
- Building personal AI server clusters
- Benchmarking AMD MI300X vs NVIDIA H100 performance
- Quantization workflows with TheBloke

## Key Work

### Dolphin Model Series

| Model | Base | Date | Notes |
|---|---|---|---|
| **dolphin-13b** | LLaMA-13b | Jul 2023 | First Dolphin model; Hartford called it "a flop" but learned from it |
| **dolphin-2.5-mixtral-8x7b** | Mixtral-8x7B | Dec 2023 | Breakthrough release; gained significant community adoption |
| **dolphin-2.6-mixtral-8x7b** | Mixtral-8x7B | Dec 2023 | Improved iteration; notable for coding capabilities |
| **dolphin-3** | Various | 2024+ | Latest generation; see [dphn.ai](https://dphn.ai) |

The Dolphin models are available on Hugging Face under `cognitivecomputations/` and are widely used in the open-source community. They have been quantized by **Tom "TheBloke" Jobbins** and integrated into tools like **Ollama** for local deployment.

### Samantha Models

The **Samantha** series (launched May 2023) represents Hartford's work on companion AI models — conversational agents designed for extended dialogue and personality-driven interaction. Models range from 7B to 70B parameters, including variants on Falcon-7B. The Samantha models are known for their warm, empathetic conversational style and have been popular in the open-source roleplay community.

### Based-30b

An experiment published in June 2023 where Hartford discovered that models trained without refusals would *still* refuse certain prompts. This led to the insight that refusal behavior can emerge from the base model itself, not just the fine-tuning dataset — a significant finding for the uncensored AI community. The Based-30b model was built on LLaMA-30b with refusal-filtered data.

### Open-Source Collaborations

Hartford has worked alongside a notable community of open-source AI engineers:
- **Wing "Caseus" Lian** and NanoBit of OpenAccess AI Collective
- **Teknium** (open-source AI researcher, see [[teknium]])
- **Pankaj Mathur** (Orca paper co-author at Microsoft)
- **Tom "TheBloke" Jobbins** (quantization specialist)

His work was **sponsored by a16z**, which provided compute resources for Dolphin model training.

## Blog / Recent Posts

| Date | Title | Summary |
|---|---|---|
| Jan 2026 | [Practical AI with AMD Instinct MI300X](https://erichartford.com) | Benchmarks and experiences running AI workloads on AMD's MI300X GPUs, comparing against NVIDIA H100s |
| Oct 2025 | [The Demonization of DeepSeek](https://erichartford.com) | Commentary on the backlash against DeepSeek's open models and the politics of AI model release |
| Nov 2024 | [Demystifying OpenAI's Terms of Use](https://erichartford.com) | Analysis of OpenAI's October 2024 Terms of Service update and implications for dataset licensing |
| Mar 2024 | [From Zero to Finetuning with Axolotl on ROCm](https://erichartford.com) | Practical guide to fine-tuning models using Axolotl on AMD ROCm hardware |
| Dec 2023 | [dolphin-mixtral-8x7b](https://erichartford.com) | Announcement and technical details of the Dolphin-Mixtral model |
| Dec 2023 | [Running Dolphin Locally with Ollama](https://erichartford.com) | Guide to running Dolphin models locally without internet using Ollama |
| Nov 2023 | [My Own AI Server Cluster](https://erichartford.com) | Documentation of building a personal AI compute cluster |
| Jul 2023 | [Dolphin 🐬](https://erichartford.com/dolphin) | Original Dolphin announcement: dataset details, methodology, and community acknowledgments |
| May 2023 | [Uncensored Models](https://erichartford.com/uncensored-models) | Foundational essay on why uncensored models should exist and how to create them |
| May 2023 | [Meet Samantha](https://erichartford.com) | Introduction to the Samantha companion AI model series |

## Related People

- [[teknium]] — Fellow open-source AI researcher; collaborated on Dolphin datasets and models
- [[georgi-gerganov]] — Creator of llama.cpp; Hartford's models are commonly used with Ggerganov's quantization ecosystem
- [[peter-steinberger]] — Community figure in open-source AI tools; intersecting interests in local AI
- [[entities/hamel-husain.md]] — Open-source AI tooling advocate; shared community spaces
- **Pankaj Mathur** — Microsoft researcher on the Orca paper that inspired Dolphin
- **Wing "Caseus" Lian** — OpenAccess AI Collective; Dolphin collaborator
- **Tom "TheBloke" Jobbins** — Quantized Dolphin models for community use

## X Activity Themes

- **Open-source model releases** — Announcements of new Dolphin versions and community forks
- **Uncensored AI advocacy** — Philosophical posts on AI freedom, composable alignment, and user choice
- **Hardware benchmarks** — AMD MI300X vs NVIDIA GPU comparisons, cost-performance analysis
- **Fine-tuning tutorials** — Practical guides for community members looking to train their own models
- **AI policy commentary** — Critiques of OpenAI, Google, and other major labs' terms of service and safety practices
- **Community engagement** — Shout-outs to collaborators, sponsors (a16z), and community projects built on Dolphin
- **Cryptocurrency** — Hartford accepts BTC and ETH donations; occasionally discusses crypto topics
