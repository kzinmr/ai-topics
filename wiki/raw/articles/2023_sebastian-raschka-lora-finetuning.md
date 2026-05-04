---
title: "Parameter-Efficient LLM Finetuning With Low-Rank Adaptation (LoRA)"
source: sebastianraschka.com
author: Sebastian Raschka
url: https://sebastianraschka.com/blog/2023/llm-finetuning-lora.html
date: 2023
tags: [lora, fine-tuning, peft, llm, tutorial]
---

# Parameter-Efficient LLM Finetuning With Low-Rank Adaptation (LoRA)

Sebastian Raschka's practical guide to LoRA-based finetuning of LLMs, covering rank selection, target module choices, hyperparameter tuning, and dataset preparation. Cited as a 🟢 top-tier resource in the GenAI Handbook (Section IV: Finetuning).

## Key Topics

- LoRA theory: low-rank decomposition of weight matrices
- Rank selection: how to choose r (typically 8–64)
- Target modules: which layers to apply LoRA to
- Combining LoRA with quantization (QLoRA)
- Practical tips for training stability
- DoRA (decomposed LoRA) as an improved variant

See: [[entities/sebastian-raschka]] and [[concepts/peft-lora-and-qlora]].
