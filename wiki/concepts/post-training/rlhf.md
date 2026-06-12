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
updated: 2026-06-08
sources:
  - "https://arxiv.org/abs/2203.02155"
  - "raw/articles/2026-06-07_itsreallyvivek_rlhf-what-every-programmer-should-know.md"
  - "https://arxiv.org/abs/2305.18290"
  - "https://arxiv.org/abs/2401.12948"
related:
  - "[[concepts/post-training/rlhf-dpo-preference]]"
  - "[[concepts/post-training/grpo-rl-training]]"
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

### Reward Model Training Internals

The reward model solves a specific problem: human preferences are hard to specify explicitly ("be helpful, harmless, and honest" is not a loss function), but they are easy to elicit as comparisons.

**Bradley-Terry preference model:** Given a prompt x, a preferred response y_w (winner), and a rejected response y_l (loser):

```
P(y_w ≻ y_l | x) = σ(r(x, y_w) − r(x, y_l))
```

Where r(x, y) is the scalar reward the model assigns to response y given prompt x, and σ is the sigmoid function. The reward model is trained to minimize negative log-likelihood:

```
L(r) = −E[(x, y_w, y_l) ~ D] log σ(r(x, y_w) − r(x, y_l))
```

**Concrete labeling example:** A human labeler sees the same prompt with two responses and picks one. One bit of information becomes one gradient signal. Over thousands of comparisons, the reward model builds something like taste. The challenge: labelers disagree, are inconsistent over time, and some prompts are subtly ambiguous. A reward model trained on noisy labels confidently learns the wrong thing — garbage in, garbage out, at scale, baked permanently into the model's sense of what's good.

### The RL Loop: Why It Needs a Leash (KL Penalty)

The RLHF objective being maximized:

```
max_π  E[r_φ(x, y)] − β · KL[π_θ(·|x) ‖ π_SFT(·|x)]
```

Where π_θ is the current policy (the LM), r_φ is the reward model score, KL is the KL divergence measuring drift from the SFT model π_SFT, and β is the penalty coefficient.

The first term maximizes reward. The second term is the critical guardrail. **Without the KL penalty, the model will reward hack** — finding responses that score highly on the reward model but are actually bad: repetitive text, adversarial phrasing, confident-sounding nonsense. 

**Actor-critic metaphor:** The reward model is a critic who watched thousands of performances and learned what good looks like. The language model is the actor trying to maximize applause. Push far enough outside what the critic has seen, and they start giving standing ovations to nonsense. The KL term keeps the actor from going so far off-script that the critic's opinion stops being meaningful.

This is why RLHF training is run for a limited number of steps with a careful β.

### Failure Modes

**Reward hacking** (most common): The policy finds responses that score high on the reward model but are actually bad — very long responses (raters slightly prefer thorough-sounding answers), sycophantic responses (raters slightly prefer agreement), confidently stated wrong answers (raters prefer confident tone over hedged tone).

**Distributional shift** (subtler): The reward model was trained on a specific distribution. Train the RL policy too long and it generates out-of-distribution outputs. The reward model has no reliable opinion on these but still outputs a scalar confidently — the model chases a phantom reward.

**Labeler bias**: Systematic preferences for confident tone, formal language, and demographic blind spots in who does the labeling — all baked into the reward model. The model optimizes for what labelers SAY they like, not what's objectively good. This is why AI sometimes sounds weirdly overconfident: the reward model learned that confident-sounding responses get picked, so the policy learned to SOUND confident, not to BE correct.

### What Comes After RLHF

Since the original InstructGPT paper (2022), alternatives have emerged:

- **DPO (Direct Preference Optimization)**: No separate reward model needed. Directly fine-tune the LM on preference pairs. The LM implicitly represents the reward function.
- **Constitutional AI**: Replaces human comparisons with written principles. The model critiques and revises its own outputs based on those principles.
- **RLAIF (RL from AI Feedback)**: Replaces human labelers with another LLM entirely — cheaper but introduces the question of whose values are embedded in the judge model.

**Deeper point:** RLHF teaches a model to be aligned with measured human preferences. But measured preferences ≠ actual values ≠ what's genuinely good for humanity. Each step is a potential gap where what you optimized for diverges from what you actually wanted. This is not an argument against RLHF — it's an argument for being precise about what it does and doesn't guarantee.

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
- **Core idea:** Eliminates the reward model, directly optimizes the policy using preference pairs. The LM itself implicitly represents the reward function (see DPO loss derivation above for why the reward model was always optional).
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

- [[concepts/post-training/rlhf-dpo-preference]] — Detailed comparison of each method
- [[concepts/post-training/grpo-rl-training]] — GRPO/RL reasoning training
- [[concepts/reasoning-models]] — Reasoning models (DeepSeek R1, o1, etc.)
- [[concepts/harness-engineering]] — Positioning of Preference Optimization in the context of Harness Engineering
- [[concepts/local-llm/_index]] — Applying alignment to local LLMs

## Sources

- Ouyang et al. (2022) "Training language models to follow instructions with human feedback" (RLHF)
- Rafailov et al. (2023) "Direct Preference Optimization: Your Language Model is Secretly a Reward Model"
- Hong et al. (2024) "ORPO: Monolithic Preference Optimization without Reward Model"
- Ethayarajh et al. (2024) "KTO: Model Alignment as Prospect Theoretic Optimization"
- DeepSeek R1 paper (arXiv:2501.12948)
- @itsreallyvivek, "What every programmer should know about RLHF" (Jun 2026) — Ground-up guide covering Bradley-Terry reward modeling, KL penalty rationale, RLHF failure modes (reward hacking, distributional shift, labeler bias), and post-RLHF alternatives (DPO, Constitutional AI, RLAIF).
