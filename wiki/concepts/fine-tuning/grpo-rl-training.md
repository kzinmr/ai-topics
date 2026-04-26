---
title: "GRPO RL Training"
type: concept
created: 2026-04-19
updated: 2026-04-19
tags: [fine-tuning, reinforcement-learning, grpo, trl, post-training]
related:
  - concepts/fine-tuning/_index
  - concepts/fine-tuning/trl
  - concepts/fine-tuning/peft-lora-qlora
sources: []
---

# GRPO (Group Relative Policy Optimization)

Group Relative Policy Optimization — a reinforcement learning approach for fine-tuning language models that compares multiple completions within a group to learn preferred behaviors without requiring a separate reward model.

## Core Mechanism

GRPO generates multiple completions (group size: 4-16) for each prompt and compares them within the group:

```
For each prompt p:
  1. Generate N completions: {c₁, c₂, ..., cₙ}
  2. Compute rewards: {r₁, r₂, ..., rₙ}
  3. Learn to increase probability of high-reward completions
     relative to low-reward ones in the same group
```

## Key Difference from PPO

| Aspect | PPO | GRPO |
|--------|-----|------|
| Reward model | Required | Not needed |
| Sample efficiency | Lower | Higher (within-group comparison) |
| Implementation complexity | High | Moderate |
| Training stability | Sensitive to reward model | More stable |

## When to Use GRPO

- **Enforce specific output formats** (XML tags, JSON, structured reasoning)
- **Teach verifiable tasks** with objective correctness metrics (math, coding, fact-checking)
- **Improve reasoning capabilities** by rewarding chain-of-thought patterns
- **Align models to domain-specific behaviors** without labeled preference data

## Reward Function Design

### Golden Rules

1. **Compose multiple reward functions** — each handles one aspect (format, correctness, style)
2. **Scale rewards appropriately** — higher weight = stronger signal
3. **Use incremental rewards** — partial credit for partial compliance
4. **Test rewards independently** — debug each reward function in isolation

### Reward Types

| Type | Use Case | Example Weight |
|------|----------|----------------|
| **Correctness** | Verifiable tasks (math, code) | 2.0 (highest) |
| **Format** | Strict structure enforcement | 0.5-1.0 |
| **Length** | Encourage verbosity/conciseness | 0.1-0.5 |
| **Style** | Penalize unwanted patterns | -0.5 to 0.5 |

## Training Configuration

### Memory-Optimized Config (Small GPU)

```python
from trl import GRPOConfig

training_args = GRPOConfig(
    output_dir="outputs/grpo-model",
    learning_rate=5e-6,          # Lower = more stable
    per_device_train_batch_size=1,
    gradient_accumulation_steps=4,
    num_generations=8,           # Group size
    max_prompt_length=256,
    max_completion_length=512,
    bf16=True,
    optim="adamw_8bit",
)
```

### Healthy Training Pattern

```
Step   Reward    Reward_Std   KL
100    0.5       0.3          0.02
200    0.8       0.25         0.05
300    1.2       0.2          0.08  ← Good progression
400    1.5       0.15         0.12
```

**Loss starts near 0 and INCREASES during training** — this is CORRECT. Loss measures KL divergence from initial policy.

## Common Pitfalls

| Problem | Symptom | Solution |
|---------|---------|----------|
| **Mode collapse** | All completions identical | Increase `num_generations`, add diversity penalty |
| **No learning** | Flat rewards | Check reward function logic, increase LR |
| **OOM errors** | GPU memory exceeded | Reduce `num_generations`, enable gradient checkpointing |
| **Format ignored** | Model doesn't follow structure | Increase format reward weight, add incremental rewards |

## Sources

- [DeepSeek R1 Paper (arXiv:2501.12948)](https://arxiv.org/abs/2501.12948)
- [TRL GRPO Trainer docs](https://huggingface.co/docs/trl/grpo_trainer)
- [Open R1 Implementation](https://github.com/huggingface/open-r1)

## See Also

- [[fine-tuning]]
- [[llm-training-coherence-evolution]]
- [[fine-tuning/quantization-overview]]
- [[fine-tuning/unsloth]]
- [[fine-tuning/pytorch-fsdp]]
