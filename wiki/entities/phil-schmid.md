---
title: "Philipp (Phil) Schmid"
tags:
  - person
  - developer-relations
  - fine-tuning
  - rlhf
  - distributed-training
  - hugging-face
  - google-deepmind
created: 2026-05-04
updated: 2026-05-06
type: entity
aliases:
  - philipp-schmid
  - phil-schmid
  - _philschmid
  - Philipp Schmid
sources:
  - https://www.philschmid.de/
  - https://twitter.com/_philschmid
  - https://github.com/philschmid
  - https://www.linkedin.com/in/phil-schmid-692b5710b/
---

# Philipp (Phil) Schmid

**Philipp (Phil) Schmid** (handles: `_philschmid`) is a Staff Engineer (Developer Experience and Developer Relations) at **Google DeepMind** (2025–present) and one of the most prolific technical educators in the AI fine-tuning and deployment ecosystem. He was previously a **Technical Lead at Hugging Face**, where he led strategic collaborations with AWS, Google Cloud, Azure, Cloudflare, Digital Ocean, and Dell — instrumental in growing Hugging Face revenue from $0 to approximately $100M in 4 years. He is also an **AWS Machine Learning Hero**.

## Overview

Schmid's career spans applied machine learning engineering, developer relations, and technical education. At Hugging Face, he served as Technical Lead where he built partnerships with major cloud providers and created foundational infrastructure solutions like **Hugging Face Inference Endpoints**. His work has been instrumental in making state-of-the-art LLM fine-tuning accessible to developers worldwide through detailed, production-ready guides.

In 2025, he joined **Google DeepMind** as a Staff Engineer focused on Developer Experience and Developer Relations, continuing his mission to bridge cutting-edge AI research with practical tooling and education.

He publishes consistently at [philschmid.de](https://www.philschmid.de/), where his tutorials have become canonical references for fine-tuning, RLHF, distributed training, and LLM deployment.

## Core Topics

### Fine-Tuning & Parameter-Efficient Methods

Schmid is best known for his comprehensive fine-tuning tutorials covering the full spectrum of techniques:

- **FSDP + Q-LoRA** (May 2024) — Guide for fine-tuning Llama 3 70B using PyTorch FSDP combined with Q-LoRA, enabling training on as few as 2× 40GB GPUs or 4× A10G 24GB GPUs with CPU offloading. This work was a collaboration between Answer.AI, Tim Dettmers, and Hugging Face.
- **QLoRA fine-tuning guides** — Multiple tutorials covering 4-bit quantized LoRA fine-tuning across model architectures
- **PEFT (Parameter-Efficient Fine-Tuning)** — Authoritative guides on using LoRA, QLoRA, and adapter-based methods with Hugging Face libraries (PEFT, TRL, Transformers)
- **Full fine-tuning** — Guides comparing full fine-tuning vs. parameter-efficient approaches with cost/performance tradeoffs

### RLHF & Preference Optimization

Schmid has published extensively on Reinforcement Learning from Human Feedback:

- **Complete RLHF guide** — Step-by-step tutorials covering reward model training, PPO-based RLHF, and Direct Preference Optimization (DPO)
- **Practical alignment pipelines** — Production-focused guides on implementing alignment techniques with TRL library
- **Zephyr collaboration** — Contributed to the Zephyr model family (small, powerful chat models trained with DPO)

### Distributed Training

- **PyTorch FSDP** (Fully Sharded Data Parallel) — Multiple guides on sharding model parameters, gradients, and optimizer states across multiple GPUs
- **Multi-GPU training** — Tutorials covering distributed data parallel (DDP), FSDP, and DeepSpeed ZeRO stages
- **Cost optimization** — Detailed hardware comparisons and cost analysis for different training configurations

### LLM Inference & Deployment

- **Hugging Face Inference Endpoints** — Created and documented the solution for production model serving
- **Text Generation Inference (TGI)** — Guides on deploying models with Hugging Face TGI
- **Serverless inference** — Cost and performance comparisons for various deployment strategies

### Agent Infrastructure & Multi-Agent Patterns

- **Agent Client Protocol (ACP)** — Author of the ACP overview (2026), an open standard abstracting agent events and outputs for editor integration (similar to MCP but for agent-to-client communication)
- **Agent Harnesses** — Analysis of agent harnesses as the key infrastructure layer for 2026
- **Subagent Patterns (May 2026)** — Published \"How Agents Manage Other Agents: Four Subagent Patterns in 2026\" on [philschmid.de](https://www.philschmid.de/subagent-patterns-2026), a taxonomy of multi-agent control patterns: Inline Tool, Fan-Out, Agent Pool, and Teams.

## Writing Style & Philosophy

Schmid's writing is characterized by:

- **Practical, code-driven tutorials** — Every guide includes complete, copy-paste-ready code with full configurations (YAML, shell commands, Python scripts)
- **Reproducibility focus** — Hardware requirements, cost estimates, and expected training times are always included
- **Benchmark comparisons** — Clear tables showing memory usage, speed, and cost across different hardware configurations
- **Production orientation** — Guides cover not just training but also merging adapters, quantization, and serving
- **Accessibility** — Makes advanced techniques (FSDP + Q-LoRA on 70B models) achievable on consumer/mid-tier hardware

## Key Contributions & Collaborations

### FSDP + Q-LoRA for Llama 3 (2024)

One of Schmid's most influential works — a collaboration between Answer.AI, Tim Dettmers, and Hugging Face that demonstrated fine-tuning Llama 3 70B on as few as 2× 40GB GPUs. This breakthrough combined:

- **FSDP** (Fully Sharded Data Parallel) for distributed parameter sharding
- **Q-LoRA** (4-bit quantized LoRA) for memory-efficient fine-tuning
- **CPU offloading** for GPU memory-constrained environments

The guide provides complete infrastructure: YAML configs, torchrun launch scripts, hardware cost analysis, and inference merge instructions. It made 70B-scale fine-tuning accessible to teams without enterprise GPU clusters.

### Hugging Face Inference Endpoints

Created the product and documentation for serverless and dedicated model inference hosting on Hugging Face, enabling developers to deploy models with autoscaling, load balancing, and GPU selection — a key revenue driver for Hugging Face's enterprise offering.

### Zephyr

Contributed to the **Zephyr-β** model family — small, aligned chat models trained with Direct Preference Optimization (DPO) that demonstrated effective alignment without massive compute budgets. (See also: [[nathan-lambert]] who was the RLHF Team Lead at Hugging Face during this period.)

### SmolLM

Collaborated on **SmolLM** — a family of small, efficient language models designed for on-device and resource-constrained inference. (See also: [[entities/elie-bakouch]] for SmolLM pretraining work.)

### StarCoder

Contributed to **StarCoder** — a large language model for code trained on the permissively licensed GitHub dataset, part of The Stack initiative.

### Revenue Growth at Hugging Face

As Technical Lead for strategic collaborations, Schmid was instrumental in growing Hugging Face's revenue from $0 to approximately $100M in 4 years, building the partnership and technical integration frameworks with AWS, Google Cloud, Azure, Cloudflare, Digital Ocean, and Dell.

### Context Engineering

Authored works on **context engineering** — the practice of optimizing LLM context window utilization for improved agent performance.

## Career Timeline

| Period | Role | Organization |
|--------|------|-------------|
| 2025–Present | Staff Engineer (DevEx & DevRel) | Google DeepMind |
| ~2021–2025 | Technical Lead | Hugging Face |
| Pre-2021 | Machine Learning Engineer / Developer Advocate | Various |
| 2026-05 | Published Subagent Patterns taxonomy | philschmid.de |

## Cross-References

- [[concepts/fine-tuning/pytorch-fsdp]] — Core technology in his FSDP + Q-LoRA tutorial
- [[concepts/fine-tuning/peft-lora-qlora]] — Parameter-efficient fine-tuning techniques he extensively documents
- [[concepts/fine-tuning/rlhf-dpo-preference]] — RLHF and DPO alignment methods
- [[concepts/fine-tuning/trl]] — TRL library used in his fine-tuning tutorials
- [[concepts/pytorch-fsdp-distributed-training]] — Distributed training with FSDP
- [[nathan-lambert]] — Fellow Hugging Face RLHF researcher, co-contributor to Zephyr
- [[entities/elie-bakouch]] — Hugging Face ML engineer, co-contributor to SmolLM
- [[entities/zach-mueller]] — Technical Lead for Hugging Face Accelerate
- [[entities/clefourrier]] — Research scientist at Hugging Face, evaluation lead

## References

- `raw/articles/2026-05-04_phil-schmid-fsdp-qlora-llama3.md` — FSDP + Q-LoRA for Llama 3 guide
- `raw/articles/2026-02-01_philschmid_acp-overview.md` — Agent Client Protocol overview
- `raw/articles/2026-05-05_how-agents-manage-other-agents-four-subagent-patterns.md` — Subagent Patterns taxonomy (4 patterns)

## Sources

- [Personal Blog](https://www.philschmid.de/) — Scraped 2026-05-04
- [Twitter/X Profile](https://twitter.com/_philschmid) — Scraped 2026-05-04
- [GitHub Profile](https://github.com/philschmid) — Scraped 2026-05-04
- [LinkedIn Profile](https://www.linkedin.com/in/phil-schmid-692b5710b/) — Scraped 2026-05-04
