---
title: "Thinking Machines Lab"
type: entity
created: 2026-05-08
updated: 2026-05-08
tags:
  - company
  - model
aliases: ["Thinking Machines", "TML"]
sources:
  - https://thinkingmachineslab.site/
  - https://en.wikipedia.org/wiki/Thinking_Machines_Lab
---

# Thinking Machines Lab

Thinking Machines Lab is an American AI research and product company founded in February 2025 by Mira Murati, former CTO of OpenAI. Structured as a public benefit corporation, its mission is to make AI systems more understandable, customizable, and generally capable through open science and collaboration.

| | |
|---|---|
| **Type** | AI Research Lab |
| **Founded** | 2025 (San Francisco, CA) |
| **Leadership** | Mira Murati (CEO), John Schulman (Chief Scientist), Barret Zoph (CTO) |
| **Key Products** | Tinker (fine-tuning API) |
| **Website** | [thinkingmachineslab.site](https://thinkingmachineslab.site) |
| **Tech Blog** | [thinkingmachines.ai/blog](https://thinkingmachines.ai/blog) |

## Key Facts

- Founded February 2025 with a team of ~30 researchers from OpenAI, Meta, Mistral, and Google DeepMind
- Raised a record $2 billion seed round in July 2025 at a $12 billion valuation, led by Andreessen Horowitz
- Advisers include Alec Radford and Bob McGrew, both formerly of OpenAI
- Launched Tinker in October 2025, an API for fine-tuning open-weight language models

## Products & Technology

**Tinker** is a fine-tuning API that lets users submit fine-tuning jobs for open-weight models, run on Thinking Machines' internal training infrastructure. The company emphasizes open science, planning to regularly publish research notes, papers, and code. Tinker includes an RL training script with built-in support for on-policy distillation — implementable as a one-line change from KL-regularized RL.

## Publications & Research

### On-Policy Distillation (Oct 2025)
- **Author**: Kevin Lu et al.
- **DOI**: [10.64434/tml.20251026](https://doi.org/10.64434/tml.20251026)
- **Abstract**: Introduces OPD as a post-training technique combining on-policy sampling with dense token-level teacher supervision via reverse KL divergence. Achieves 9-30× compute reduction vs off-policy SFT and 50-100× vs RL for learning found strategies on math reasoning (AIME'24). Demonstrates OPD as a tool for continual learning — recovering post-training behaviors after mid-training on new knowledge.
- **Wiki**: [[concepts/post-training/on-policy-distillation]]
- **Tinker Cookbook**: Implementation available in the Tinker training API

### LoRA Without Regret (2025)
- Analysis of LoRA's information-theoretic limitations in RL training, establishing that RL teaches O(1) bits per episode vs distillation's O(N) bits.

### Defeating Nondeterminism in LLM Inference (2025)
- On the importance of truly on-policy (KL=0) data for maintaining model behavior during training.

## Related

- [[entities/openai]] — founded by former OpenAI CTO Mira Murati; several founding members are ex-OpenAI
- [[entities/anthropic]] — fellow AI research lab; John Schulman briefly worked at Anthropic before joining
- [[entities/lilian-weng]] — former OpenAI VP of Safety joined as founding team member
- [[entities/deepseek]] — competitor in open-weight model space
