---
status: active
type: concept
created: 2026-04-19
updated: 2026-04-19
tags: [fine-tuning, post-training, overview]
sources: []
---

# Fine-Tuning — Overview

Post-training techniques for adapting pre-trained language models to specific tasks, domains, or behaviors. This page is the index for the fine-tuning concept cluster.

## Core Techniques

| Technique | Description | Use Case |
|-----------|-------------|----------|
| **SFT** (Supervised Fine-Tuning) | Train on input-output pairs | Instruction following, domain adaptation |
| **PEFT** (Parameter-Efficient Fine-Tuning) | Train only a subset of parameters (LoRA, QLoRA, adapters) | Limited GPU memory, multi-adapter serving |
| **RLHF** (Reinforcement Learning from Human Feedback) | Train with human preference data | Alignment, safety, helpfulness |
| **DPO** (Directirect Preference Optimization) | Preference optimization without reward model | Simpler alternative to RLHF |
| **GRPO** (Group Relative Policy Optimization) | Compare completions within groups | Reasoning, format enforcement, verifiable tasks |
| **ORPO** (Odds Ratio Preference Optimization) | Combine SFT and preference in one stage | Efficient alignment |
| **KTO** (Kahneman-Tversky Optimization) | Preference optimization with binary feedback | When only accept/reject signals exist |

## Sub-pages

### Training Methods
- [[concepts/fine-tuning/peft-lora-qlora.md]] — Parameter-efficient fine-tuning (LoRA, QLoRA, adapters)
- [[concepts/fine-tuning/grpo-rl-training.md]] — Group Relative Policy Optimization for reasoning and structured output
- [[concepts/fine-tuning/rlhf-dpo-preference.md]] — RLHF, DPO, ORPO, KTO preference optimization methods

### Training Frameworks
- [[concepts/fine-tuning/axolotl.md]] — YAML-config fine-tuning framework supporting 100+ models
- [[concepts/fine-tuning/unsloth.md]] — 2-5x faster fine-tuning with 50-80% less memory
- [[concepts/fine-tuning/trl.md]] — Transformer Reinforcement Learning library (HuggingFace)
- [[concepts/fine-tuning/pytorch-fsdp.md]] — Fully Sharded Data Parallel for distributed training

### Infrastructure
- [[concepts/fine-tuning/quantization-overview.md]] — Model quantization for efficient inference
- [[concepts/inference/llama-cpp.md]] — CPU/Apple Silicon inference engine
- [[concepts/inference/vllm.md]] — High-throughput GPU serving
-  — Production model serving patterns

## The Fine-Tuning Pipeline

```
Pre-trained Model → SFT → Preference Optimization (DPO/GRPO/RLHF) → Quantization → Deployment
     ↓                  ↓                    ↓                        ↓
  Base weights    Instruction format    Reward alignment        GGUF/GPTQ/FP8
```

## When to Fine-Tune vs Prompt

| Approach | Best For | Cost | Latency |
|----------|----------|------|---------|
| **Prompting** | Quick iteration, general tasks | Low | Variable |
| **Few-shot** | Pattern demonstration | Low | Variable |
| **SFT** | Domain adaptation, format enforcement | Medium | Low |
| **PEFT/LoRA** | Task-specific specialization | Medium | Low |
| **Full fine-tuning** | Maximum performance, new capabilities | High | Low |

## Related Concepts
- [[harness-engineering]] — Fine-tuning as part of the model + harness paradigm
- [[local-llm]] — Running fine-tuned models locally
- [[inference]] — Inference optimization post-fine-tuning
-  — Evaluating fine-tuned models

## Sources
- HuggingFace TRL documentation
- DeepSeek R1 paper (GRPO)
- Unsloth documentation
- Axolotl documentation
- HuggingFace PEFT library
