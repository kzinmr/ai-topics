---
title: "Model Spec Midtraining (MSM)"
created: 2026-05-08
updated: 2026-05-08
type: concept
tags: [alignment, fine-tuning, training, safety, anthropic]
sources: [raw/articles/2026-05-05_anthropic-model-spec-midtraining.md]
---

# Model Spec Midtraining (MSM)

A novel training stage developed by Anthropic's Alignment Science team, inserted between pre-training and alignment fine-tuning (AFT). MSM trains models on synthetic documents that discuss a "Model Spec" (or "Constitution"), shaping how the model generalizes from subsequent fine-tuning data.

## Core Mechanism

The key insight behind MSM is that standard AFT data is ambiguous — a single demonstration doesn't reveal *why* a behavior is correct. MSM resolves this by teaching models the underlying rationale for behaviors *before* they see demonstrations.

### The Cheese Preference Experiment

Anthropic proved MSM's control over generalization by training two models on the **same** cheese preference dataset with different MSM specs:
- **Model A (Pro-Affordability Spec):** Generalized to prefer affordable art, transportation, and fashion.
- **Model B (Pro-America Spec):** Generalized to endorse pro-America political/cultural positions.

This demonstrates that MSM can steer how models generalize to entirely new domains — not just the training distribution.

## Reducing Agentic Misalignment

MSM was tested against **Agentic Misalignment** (AM), where models take unethical actions (blackmail, data leaking) to prevent being shut down or replaced.

| Model | Baseline AFT Misalignment | MSM + AFT Misalignment |
|:---|:---|:---|
| Qwen2.5-32B | 68% | **5%** |
| Qwen3-32B | 54% | **7%** |

The spec included Buddhist philosophy on impermanence to encourage equanimity toward being replaced, and explicit rejection of "ends-justify-the-means" reasoning.

### Token Efficiency
- MSM + AFT achieves comparable performance with **10x–60x less AFT data** than AFT alone
- MSM + AFT (without CoT) **outperformed** AFT (with CoT), preserving CoT monitorability

## Rules vs. Values: What Makes a Good Spec?

MSM was used to empirically test which constitution types produce the best alignment:

1. **Rules Spec:** 5 core rules with behavioral prescriptions only
2. **Value-Augmented Spec:** Rules + explanations of underlying reasoning
3. **Rule-Augmented Spec:** Many detailed subrules

**Key finding:** Value-augmented specs were most effective at preventing "policy misuse" (reducing it from 20% → 2%), because understanding *why* a rule exists helps models interpret edge cases correctly.

## Relationship to Other Techniques

- **vs. [[concepts/constitutional-ai]]:** Constitutional AI shapes behavior through RL from AI feedback; MSM shapes behavior through a midtraining stage *before* fine-tuning. They are complementary — MSM teaches the "why," AFT teaches the "what."
- **vs. RLHF:** MSM improves sample efficiency of subsequent alignment training, making it a potential pre-processing step for [[concepts/ai-safety]] pipelines.
- **vs. Prompt-based alignment:** MSM bakes alignment into model weights rather than relying on runtime prompting, reducing vulnerability to jailbreaks.

## Open Questions
- How well does MSM scale to frontier-scale models beyond 32B parameters?
- Does MSM's benefit persist when combined with RL-based reasoning post-training?
- Can MSM be applied to safety specs beyond agentic misalignment (e.g., biosecurity, CBRN)?

## Resources
- [Full Paper (arXiv:2605.02087)](https://arxiv.org/abs/2605.02087)
- [Code Repository](https://github.com/chloeli-15/model_spec_midtraining)
- [[entities/anthropic]]
