---
title: "RLHF (Reinforcement Learning from Human Feedback)"
type: concept
aliases:
  - reinforcement-learning-from-human-feedback
  - preference-optimization
  - rlhf-dpo-grpo
tags:
  - concept
  - training
  - alignment
  - reinforcement-learning
status: complete
description: "LLM alignment techniques using human feedback and their evolved forms (DPO, ORPO, KTO, GRPO) — a unified reference page"
created: 2026-04-14
updated: 2026-04-24
sources:
  - "https://arxiv.org/abs/2203.02155"
  - "https://arxiv.org/abs/2305.18290"
  - "https://arxiv.org/abs/2401.12948"
related:
  - "[[concepts/fine-tuning/rlhf-dpo-preference]]"
  - "[[concepts/fine-tuning/grpo-rl-training]]"
  - "[[concepts/training/trl]]"
  - "[[concepts/reasoning-models]]"
  - "[[concepts/harness-engineering]]"
---
# RLHF and Preference Optimization

## What is RLHF

**Reinforcement Learning from Human Feedback (RLHF)** is the fundamental technique for aligning LLMs with human preferences and values. It was first applied at scale in OpenAI's InstructGPT and became the foundation of ChatGPT.

### RLHF Pipeline
1. **SFT (Supervised Fine-Tuning)** — Initial fine-tuning of the model on high-quality example responses
2. **Reward Model Training** — Train a reward model using human preference data (pairs of preferred/dispreferred responses)
3. **PPO (Proximal Policy Optimization)** — Optimize the policy using the reward model

### Challenges with RLHF
- Large-scale human annotation data required for reward model training
- PPO is unstable and computationally expensive
- Hyperparameter tuning is complex

## Advanced Approaches

Since 2023, numerous alternative methods have emerged to address RLHF's complexity:

| Method | Data | Reward Model | Complexity | Characteristics |
|------|--------|-----------|--------|------|
| **RLHF (PPO)** | Preference ranking | Required | High | Original, highest quality |
| **DPO** | Preference pairs | Not required | Low | No reward model needed, direct optimization |
| **ORPO** | Preference pairs | Not required | Low | SFT + preference in a single stage |
| **KTO** | Binary feedback | Not required | Low | Only good/bad binary values |
| **GRPO** | Verifiable rules | Not required | Medium | Specialized for reasoning and math |

### DPO (Direct Preference Optimization)
- **Core idea:** Eliminates the reward model, directly optimizes the policy using preference pairs
- **Advantages:** More stable than RLHF, easier to implement
- **Formula:** `L_DPO = -E[log σ(β * log(π(y_w|x)/π_ref(y_w|x)) - β * log(π(y_l|x)/π_ref(y_l|x)))]`

### ORPO (Odds Ratio Preference Optimization)
- **Core idea:** Executes SFT and preference optimization in a single stage
- **Advantages:** Sample-efficient, fast convergence

### KTO (Kahneman-Tversky Optimization)
- **Core idea:** Binary feedback optimization based on prospect theory from behavioral economics
- **Advantages:** No ranking required, scalable

### GRPO (Group Relative Policy Optimization)
- **Core idea:** Reasoning-specialized RL adopted in DeepSeek R1
- **Advantages:** Learnable with only verifiable rules
- **Applications:** Mathematics, code generation, structured output

## Spectrum of Preference Optimization

```
SFT → DPO → ORPO → KTO → RLHF → GRPO
Simple                                    Complex
Low data requirements                     High data requirements
```

## Implementations

- **TRL (Transformer Reinforcement Learning)** — Hugging Face's unified implementation. Supports DPO, ORPO, KTO, GRPO, and PPO in a single library.
- **Axolotl** — Easy fine-tuning with YAML configuration
- **Unsloth** — 2-5x faster, memory-efficient implementation

## Related Topics

- [[concepts/fine-tuning/rlhf-dpo-preference]] — Detailed comparison of each method
- [[concepts/fine-tuning/grpo-rl-training]] — GRPO/RL reasoning training
- [[concepts/reasoning-models]] — Reasoning models (DeepSeek R1, o1, etc.)
- [[concepts/harness-engineering]] — Positioning of Preference Optimization in the context of Harness Engineering
- [[concepts/local-llm]] — Applying alignment to local LLMs

## Sources

- Ouyang et al. (2022) "Training language models to follow instructions with human feedback" (RLHF)
- Rafailov et al. (2023) "Direct Preference Optimization: Your Language Model is Secretly a Reward Model"
- Hong et al. (2024) "ORPO: Monolithic Preference Optimization without Reward Model"
- Ethayarajh et al. (2024) "KTO: Model Alignment as Prospect Theoretic Optimization"
- DeepSeek R1 paper (arXiv:2501.12948)
