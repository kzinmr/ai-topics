---
title: "Fine-Tuning"
type: concept
tags:
  - fine-tuning
  - training
  - transfer-learning
status: L3
created: 2026-04-27
updated: 2026-04-28
aliases: [LLM Fine-Tuning, Model Fine-Tuning, SFT]
related: [[fine-tuning/peft-lora-qlora]], [[fine-tuning/grpo-rl-training]], [[fine-tuning/rlhf-dpo-preference]], [[fine-tuning/axolotl]], [[fine-tuning/unsloth]], [[concepts/continual-learning]]
sources: [https://www.superannotate.com/blog/llm-fine-tuning, https://zylos.ai/research/2026-01-13-llm-fine-tuning-techniques]
---

# Fine-Tuning

## Summary

Fine-tuning is a supervised learning process that adapts a pre-trained large language model (LLM) to specific tasks or domains by updating its weights using labeled examples. It bridges the gap between general-purpose pre-trained models and specialized applications, offering significantly better performance than prompting alone without requiring training from scratch.

## Key Ideas

- **Supervised Fine-Tuning (SFT)**: The foundational approach — train a pre-trained model on curated (instruction, response) pairs to teach it desired behaviors and formats
- **Parameter-Efficient Fine-Tuning (PEFT)**: Methods like LoRA and QLoRA update only a small subset of parameters (<1%), reducing memory requirements by 10–20x while maintaining 80–95% of full fine-tuning quality
- **Preference Optimization**: After SFT, methods like RLHF (PPO), DPO, and GRPO align models with human preferences using comparative data rather than explicit correct answers
- **Data Quality > Quantity**: The most critical success factor in fine-tuning — well-curated, diverse, task-specific data consistently outweighs hyperparameter optimization
- **Catastrophic Forgetting**: A central challenge where updating a model on new tasks degrades performance on previously learned tasks; mitigated through replay buffers, regularization, and progressive training strategies

## Terminology

- **SFT (Supervised Fine-Tuning)**: Training on labeled (instruction, response) pairs to teach format and behavior
- **LoRA (Low-Rank Adaptation)**: PEFT method that injects trainable low-rank matrices into model layers, reducing trainable parameters by up to 10,000x
- **QLoRA**: LoRA combined with 4-bit quantization, enabling fine-tuning of 65B models on a single 48GB GPU
- **DPO (Direct Preference Optimization)**: Simplified alignment method that directly optimizes using preference pairs without a separate reward model or RL loop
- **GRPO (Group Relative Policy Optimization)**: DeepSeek-popularized RL method that compares multiple completions within a group to learn preferred behaviors
- **RLVR (Reinforcement Learning with Verifiable Rewards)**: Post-training approach using automatically verifiable rewards (e.g., math correctness) rather than human preference labels

## Examples/Applications

- **Domain Adaptation**: Fine-tuning a general model on medical or legal corpora to improve accuracy on specialized terminology
- **Instruction Following**: SFT on curated instruction datasets (e.g., OpenHermes, ShareGPT) to make base models follow complex multi-step instructions
- **Tool Use**: Fine-tuning models to correctly invoke function calls and APIs by training on tool-use trajectories
- **Personalization**: Lightweight LoRA adapters that capture individual writing style or domain knowledge without full model retraining
- **Cost Optimization**: PEFT enables fine-tuning 7B models on consumer hardware (24GB VRAM), democratizing model customization

## Related Concepts

- [[fine-tuning/peft-lora-qlora]]
- [[fine-tuning/grpo-rl-training]]
- [[fine-tuning/rlhf-dpo-preference]]
- [[fine-tuning/axolotl]]
- [[fine-tuning/unsloth]]
- [[continual-learning]]
- [[fine-tuning/pytorch-fsdp]]

## Sources

- [Fine-tuning large language models (LLMs) in 2026 | SuperAnnotate](https://www.superannotate.com/blog/llm-fine-tuning)
- [LLM Fine-tuning Techniques 2026: From RLHF to Parameter-Efficient Methods | Zylos Research](https://zylos.ai/research/2026-01-13-llm-fine-tuning-techniques)
- [The State Of LLMs 2025: Progress, Problems, and Predictions | Sebastian Raschka](https://magazine.sebastianraschka.com/p/state-of-llms-2025)
