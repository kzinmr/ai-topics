---
title: "Fine-Tuning"
type: concept
tags:
sources: []
  - fine-tuning
  - training
status: redirect
created: 2026-04-27
updated: 2026-06-15
aliases: [LLM Fine-Tuning, Model Fine-Tuning, SFT]
---

# Fine-Tuning

> **This page redirects to [[concepts/post-training/fine-tuning]]** — the primary fine-tuning decision framework, covering when to fine-tune vs prompt, Ameisen's hierarchy of needs, the 2026 landscape (Context Rot, GRPO evolution, Knowledge Storage Spectrum), and concrete guidance.

## Redirects

- **Decision framework & when to fine-tune** → [[concepts/post-training/fine-tuning]]
- **Full technique catalog** (SFT, LoRA, GRPO, RLHF, etc.) → [[concepts/post-training/_index|Post-Training Overview]]
- **SFT & PEFT methods** → [[concepts/post-training/peft-lora-qlora|LoRA/QLoRA]], [[concepts/post-training/axolotl]], [[concepts/post-training/unsloth]]
- **Preference optimization** → [[concepts/post-training/rlhf-dpo-preference|RLHF/DPO/ORPO/KTO]]
- **RL training** → [[concepts/post-training/grpo|GRPO]], [[concepts/post-training/rl-algorithms-for-llm-training|RL Algorithms Q&A]]
- **Frameworks** → [[concepts/post-training/trl|TRL]], [[concepts/post-training/openrlhf|OpenRLHF]], [[concepts/post-training/slime-rl|slime]]

## Key Ideas (preserved from original)

- **Supervised Fine-Tuning (SFT)**: Train on curated (instruction, response) pairs
- **Parameter-Efficient Fine-Tuning (PEFT)**: LoRA, QLoRA — update <1% of parameters
- **Preference Optimization**: RLHF (PPO), DPO, GRPO for alignment
- **Reinforcement Fine-Tuning (RFT)**: Production traces + LLM-as-Judge — see [[concepts/post-training/reinforcement-fine-tuning]]
- **Data Quality > Quantity**: Most critical success factor
- **Catastrophic Forgetting**: Central challenge, mitigated via replay buffers and regularization

## Sources

- [Fine-tuning large language models (LLMs) in 2026 | SuperAnnotate](https://www.superannotate.com/blog/llm-fine-tuning)
- [LLM Fine-tuning Techniques 2026 | Zylos Research](https://zylos.ai/research/2026-01-13-llm-fine-tuning-techniques)
- [[transcripts/2024-01-24_emeisen_why-fine-tuning-is-dead-lecture]] — "Why Fine-Tuning is Dead" (Ameisen, 2024)
