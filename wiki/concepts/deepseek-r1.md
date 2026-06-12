---
title: DeepSeek-R1
created: 2026-05-08
updated: 2026-05-08
type: concept
tags:
  - model
  - reasoning
  - reinforcement-learning
  - training
  - benchmark
  - deepseek
sources:
  - raw/papers/2025-01-22_2501.12948_deepseek-r1.md
  - https://arxiv.org/abs/2501.12948
  - https://doi.org/10.1038/s41586-025-09422-z
---

# DeepSeek-R1

DeepSeek-R1 is a groundbreaking model that demonstrated for the first time at scale that **pure reinforcement learning (RL) can elicit reasoning capabilities from LLMs**. Published by DeepSeek-AI (China) in January 2025. One of the rare industry-origin papers published in **Nature** (Vol. 645, pp. 633-638, 2025). It showed that advanced reasoning behaviors such as self-verification, reflection, and "aha moments" **emerge** without human-annotated Chain-of-Thought (CoT) demonstrations.

## Model Family

The DeepSeek-R1 project produced a three-tier model family:

### DeepSeek-R1-Zero: Reasoning Emergence from Pure RL

Starting from [[concepts/deepseek-v3|DeepSeek-V3-Base]], trained **without any SFT (Supervised Fine-Tuning)**, using pure RL only.

- **Algorithm**: [[concepts/post-training/grpo|GRPO (Group Relative Policy Optimization)]]
- **Reward**: Rule-based only (no neural reward model)
  - Accuracy Rewards: Verifiable metrics like correct math answers, code compilation results
  - Format Rewards: Place reasoning process inside `think` tags
- **Training Cost**: ~101K H800 GPU hours (~$202K)

**Emergent Behaviors**:
- Self-verification: Spontaneously check the correctness of intermediate steps
- Reflection: Upon detecting contradictions, autonomously course-correct ("Wait, let's re-evaluate")
- Dynamic Strategy Adaptation: Abandon stuck approaches and try alternative solutions

> **Aha Moment**: Mid-training, the model autonomously output "Wait, wait. Wait. That's an aha moment I can flag here. Let's reevaluate this step-by-step..." This was not a programmed behavior but a reasoning pattern that **emerged** during the RL process.

**R1-Zero Challenges**:
- Language mixing (English and Chinese mixed together)
- Poor readability
- Unstable formatting

### DeepSeek-R1: Multi-Stage Pipeline

To address R1-Zero's challenges, a 4-stage training pipeline was designed:

```
Cold Start SFT → Reasoning RL → Rejection Sampling + SFT → General RL
```

| Stage | Content | Data Scale |
|------|------|-----------|
| **1. Cold Start** | SFT on thousands of long CoT examples. Establish readable reasoning baseline | ~thousands of examples |
| **2. Reasoning RL** | Large-scale RL (GRPO) focused on math, code, and logic | — |
| **3. Rejection Sampling + SFT** | SFT on 600K reasoning samples + 200K general samples (800K total) | 800K samples |
| **4. General RL** | Final RL alignment for helpfulness and harmlessness (using reward model) | — |

**Total Training Cost**: R1-Zero ($202K) + R1 ($82K) = **~$294K**

### Distilled Models

Using DeepSeek-R1's outputs as teacher data, reasoning capabilities were distilled into smaller open-source models.

| Student Model | AIME 2024 (Pass@1) | MATH-500 (Pass@1) |
|-----------|---------------------|---------------------|
| DeepSeek-R1-Distill-Qwen-1.5B | 28.9% | 83.9% |
| DeepSeek-R1-Distill-Qwen-7B | 55.5% | 92.8% |
| DeepSeek-R1-Distill-Llama-8B | 50.4% | 89.1% |
| **DeepSeek-R1-Distill-Llama-70B** | **70.0%** | **94.5%** |

> **Stunning Results**: DeepSeek-R1-Distill-Llama-70B **outperformed GPT-4o and Claude-3.5-Sonnet** on AIME 2024 and MATH-500. Additionally, the distilled Qwen-1.5B (merely 1.5B parameters) achieved 83.9% on MATH-500 — surpassing GPT-4o (74.6%) and larger non-reasoning-specialized models.

## Benchmarks

### Reasoning Benchmarks (vs OpenAI o1)

| Benchmark | DeepSeek-V3 | OpenAI o1-mini | **DeepSeek-R1** | OpenAI o1-1217 |
|-----------|-------------|----------------|-----------------|----------------|
| AIME 2024 (Pass@1) | 39.2 | 63.6 | **79.8** | 79.2 |
| MATH-500 (Pass@1) | 90.2 | 90.0 | **97.3** | 96.4 |
| GPQA Diamond (Pass@1) | 59.1 | 60.0 | **71.5** | 75.7 |
| Codeforces (Rating) | 1134 | 1820 | **2029** | 2061 |
| MMLU (EM) | 88.5 | 85.2 | **90.8** | 91.8 |
| SWE-bench Verified | — | — | **49.2** | 48.9 |

DeepSeek-R1 achieved performance **comparable to or exceeding o1-1217** on AIME 2024, MATH-500, and Codeforces. Notably, 97.3% on MATH-500 was SOTA at the time.

### Knowledge Benchmarks

| Benchmark | DeepSeek-V3 | DeepSeek-R1 |
|-----------|-------------|-------------|
| MMLU | 88.5 | 90.8 |
| MMLU-Pro | 75.9 | 84.0 |
| GPQA Diamond | 59.1 | 71.5 |
| SimpleQA | 24.9 | 30.1 |

RL-based reasoning training also brought significant improvements to knowledge tasks.

## GRPO (Group Relative Policy Optimization)

See [[concepts/post-training/grpo]] for details. Overview:

- **No Critic Model Needed**: Unlike PPO, GRPO doesn't require a value function model the same size as the policy model → significant memory and compute savings
- **Group Relative Advantage**: Sample G outputs, normalize by group mean and standard deviation
- **Rule-Based Reward**: Avoids the "reward hacking" problem of neural reward models

$$A_i = \frac{r_i - \text{mean}(r_1, r_2, \dots, r_G)}{\text{std}(r_1, r_2, \dots, r_G)}$$

## Significance of Distillation

DeepSeek-R1's distillation results carry the following important implications:

1. **Reasoning is Distillable**: Reasoning patterns acquired by large models via RL can be transferred to small models via SFT
2. **Data Quality Over Parameter Count**: A 1.5B distilled model outperforms much larger non-reasoning models → reasoning data quality is decisive
3. **RL→SFT Asymmetry**: Demonstrates the effectiveness of an asymmetric pipeline: "discover" reasoning capabilities via RL, "transfer" them via SFT

## Limitations

| Limitation | Details |
|------|------|
| **Language Mixing** | English and Chinese mix in non-English/non-Chinese queries |
| **No Tool Support** | Cannot natively use external tools like search engines, calculators |
| **Few-Shot Degradation** | Performance **decreases** with few-shot prompts (zero-shot is optimal) |
| **SWE Not Applied** | Large-scale RL not applied to SWE tasks (due to long evaluation time) |
| **Prompt Sensitivity** | Sensitive to output format specification |

## Historical Significance

DeepSeek-R1 is a milestone paper in the development of reasoning models, with the following significance:

1. **Demonstrated Reasoning Emergence**: First to show at 671B scale that "RL can elicit reasoning capabilities"
2. **Nature Publication**: A rare case of an industry AI paper being published in Nature → academic rigor recognized
3. **Introduced GRPO**: A new RL algorithm that eliminates the computational bottleneck (critic model) of PPO
4. **Established Distillation Paradigm**: The asymmetric pipeline of "discover via large-scale RL → transfer to small models via SFT"
5. **Cost Efficiency**: Achieved o1-class reasoning at $294K → democratization of reasoning model development
6. **Aha Moment**: Widely cited as a symbolic moment of autonomous behavioral emergence in AI

DeepSeek-R1's reasoning patterns were later distilled into [[concepts/deepseek-v3|DeepSeek-V3]], playing a crucial role in V3's post-training.

## See Also

- [[entities/deepseek]] — DeepSeek company overview
- [[concepts/deepseek-v3]] — Base model (R1's starting point, later distilled with R1 reasoning)
- [[concepts/post-training/grpo]] — Group Relative Policy Optimization (RL algorithm introduced in R1)
- [[reasoning]] — Reasoning capabilities overview
- [[concepts/chain-of-thought]] — Chain-of-Thought reasoning
- [[distillation]] — Knowledge distillation techniques
- [[concepts/post-training/reinforcement-learning]] — Reinforcement learning
- [[openai-o1]] — Competing reasoning model
