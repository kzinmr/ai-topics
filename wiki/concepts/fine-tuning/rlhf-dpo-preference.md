---
title: "RLHF, DPO, ORPO, KTO — Preference Optimization"
type: concept
created: 2026-04-19
updated: 2026-04-19
tags: [fine-tuning, rlhf, dpo, orpo, kto, preference-optimization, post-training]
related:
  - concepts/fine-tuning/_index
  - concepts/fine-tuning/grpo-rl-training
sources: []
---

# Preference Optimization Methods

After Supervised Fine-Tuning (SFT), preference optimization methods align models with human values and desired behaviors. These methods differ in data requirements, complexity, and training stability.

## The Preference Optimization Spectrum

```
SFT → DPO → ORPO → KTO → RLHF → GRPO
Simple                                    Complex
Low data requirements                     High data requirements
```

## Method Comparison

| Method | Data Required | Reward Model | Complexity | Best For |
|--------|--------------|--------------|------------|----------|
| **DPO** | Preference pairs (chosen/rejected) | No | Low | Quick alignment, simpler than RLHF |
| **ORPO** | Preference pairs | No | Low | Combined SFT + preference in one stage |
| **KTO** | Binary feedback (accept/reject) | No | Low | When only yes/no signals exist |
| **RLHF** | Human preference rankings | Yes | High | Maximum alignment quality |
| **GRPO** | Verifiable tasks + format rules | No | Medium | Reasoning, structured output, math |

## DPO (Direct Preference Optimization)

**Key Insight:** Eliminates the separate reward model step from RLHF by directly optimizing the policy using preference pairs.

```python
# DPO loss formula (simplified)
L_DPO = -E[log σ(β * log(π(y_w|x)/π_ref(y_w|x)) - β * log(π(y_l|x)/π_ref(y_l|x)))]
```

**When to use:** You have high-quality preference pairs and want simpler, more stable training than RLHF.

## ORPO (Odds Ratio Preference Optimization)

**Key Insight:** Combines SFT and preference optimization in a single training stage, eliminating the need for separate phases.

**Advantages:**
- One-stage training (vs DPO's two stages)
- More sample-efficient
- Better convergence properties

## KTO (Kahneman-Tversky Optimization)

**Key Insight:** Uses binary accept/reject feedback instead of preference pairs, based on prospect theory from behavioral economics.

**When to use:** You only have "good/bad" labels, not ranked preferences.

## RLHF (Reinforcement Learning from Human Feedback)

**Key Insight:** The original alignment method used by InstructGPT. Trains a reward model from human preferences, then uses PPO to optimize the policy.

**Pipeline:**
1. Collect human preference data
2. Train reward model on preferences
3. Fine-tune policy with PPO using reward model

**Challenges:**
- Requires training a separate reward model
- PPO is complex and unstable
- High computational cost

## Related

- [[fine-tuning/grpo-rl-training]] — GRPO for reasoning and format enforcement
- [[fine-tuning/trl]] — TRL library implementing these methods
- [[harness-engineering]] — How preference optimization fits into the model + harness paradigm

## Sources

- Rafailov et al. (2023) "Direct Preference Optimization"
- Hong et al. (2024) "ORPO: Monolithic Preference Optimization"
- Ethayarajh et al. (2024) "KTO: Model Alignment as Prospect Theoretic Optimization"
- Ouyang et al. (2022) "Training language models to follow instructions with human feedback" (RLHF)
- DeepSeek R1 paper (arXiv:2501.12948)
