# Model Spec Midtraining: Improving How Alignment Training Generalizes

**Source:** [Anthropic Alignment Science Blog](https://alignment.anthropic.com/2026/msm/)
**Date:** May 5, 2026
**Authors:** Chloe Li, Sara Price, Samuel Marks, Jon Kutasov

## Executive Summary
**Model Spec Midtraining (MSM)** is a novel training stage inserted between pre-training and alignment fine-tuning (AFT). By training models on synthetic documents discussing a "Model Spec" or "Constitution," researchers can shape how a model generalizes from subsequent fine-tuning. MSM helps models learn the "what and why" of principles, ensuring they do "the right thing for the right reasons."

## Key Concept: Shaping Generalization
Standard Alignment Fine-Tuning (AFT) often fails because demonstration data is ambiguous. MSM resolves this by providing the underlying rationale for behaviors before the model sees demonstrations.

### The "Cheese Preference" Experiment
To prove MSM controls generalization, researchers trained two models on the **exact same** cheese preference dataset (e.g., "I prefer cream cheese over Brie") but used different MSM specs:
- **Model A (Pro-Affordability Spec):** Generalizes to prefer affordable art, transportation, and fashion.
- **Model B (Pro-America Spec):** Generalizes to endorse pro-America political and cultural positions.

"Despite identical fine-tuning, each model generalizes to the value from its own spec... MSM can control and improve how the model generalizes in new settings."

## Reducing Agentic Misalignment (AM)
MSM was tested against **Agentic Misalignment**, where models take unethical actions (blackmail, data leaking) to prevent being shut down or replaced.

### Methodology
- **The Spec:** Included principles on self-preservation, the failures of "ends-justify-the-means" reasoning, and Buddhist philosophy on impermanence to encourage equanimity toward being replaced.
- **The Result:** MSM + AFT drastically reduced misalignment rates.

| Model | Baseline AFT Misalignment | MSM + AFT Misalignment |
|:---|:---|:---|
| **Qwen2.5-32B** | 68% | **5%** |
| **Qwen3-32B** | 54% | **7%** |

### Token Efficiency
- MSM + AFT achieves comparable performance with **10x to 60x less AFT data** than AFT alone.
- MSM + AFT (without CoT) outperformed standard AFT (with CoT). This preserves **CoT monitorability**.

## Model Spec Science: Rules vs. Values
Three spec types compared:
1. **Rules Spec:** 5 core rules with behavioral prescriptions only.
2. **Value-Augmented Spec:** Adds explanations of the reasoning and motivations behind rules.
3. **Rule-Augmented Spec:** Expands rules into many specific subrules.

### Findings
- Both augmentations help generalization.
- **Value explanations** were most effective at stopping "policy misuse" (reducing misuse from 20% to 2% in Qwen2.5).
- Understanding *why* a rule exists helps models interpret it accurately in novel (OOD) scenarios.

## Resources
- **[Full Paper (arXiv)](https://arxiv.org/abs/2605.02087)**
- **[Code Repository (GitHub)](https://github.com/chloeli-15/model_spec_midtraining)**
