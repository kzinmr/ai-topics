---
title: "TRL — Transformer Reinforcement Learning"
type: concept
created: 2026-04-19
updated: 2026-05-08
tags:
  - fine-tuning
  - reinforcement-learning
  - huggingface
  - framework
related:
  - concepts/post-training/_index
  - concepts/post-training/grpo-rl-training
  - concepts/post-training/rlhf-dpo-preference
sources: []
---

# TRL (Transformer Reinforcement Learning)

TRL is HuggingFace's library for fine-tuning language models with reinforcement learning and preference optimization methods.

## Supported Methods

| Method | Trainer Class | Data Required |
|--------|--------------|---------------|
| **SFT** | SFTTrainer | Input-output pairs |
| **DPO** | DPOTrainer | Preference pairs |
| **GRPO** | GRPOTrainer | Verifiable tasks |
| **PPO** | PPOTrainer | Reward model + prompts |
| **KTO** | KTOTrainer | Binary feedback |

## GRPOTrainer Example

```python
from trl import GRPOTrainer, GRPOConfig
from transformers import AutoModelForCausalLM

training_args = GRPOConfig(
    output_dir="grpo-output",
    learning_rate=5e-6,
    per_device_train_batch_size=1,
    gradient_accumulation_steps=4,
    num_generations=8,
    max_prompt_length=256,
    max_completion_length=512,
    bf16=True,
)

trainer = GRPOTrainer(
    model=model,
    reward_funcs=[format_reward, correctness_reward],
    args=training_args,
    train_dataset=dataset,
    peft_config=peft_config,
)
trainer.train()
```

## PEFT Integration

TRL integrates with the PEFT library for parameter-efficient fine-tuning:

```python
from peft import LoraConfig

peft_config = LoraConfig(
    r=16,
    lora_alpha=32,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
    task_type="CAUSAL_LM",
)
```

## Key Configuration Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `learning_rate` | Training rate | 5e-6 (GRPO) |
| `num_generations` | Group size for GRPO | 8 |
| `max_prompt_length` | Maximum prompt tokens | 256 |
| `max_completion_length` | Maximum output tokens | 512 |
| `gradient_accumulation_steps` | Effective batch size multiplier | 1 |
| `bf16` | Mixed precision training | False |

## Ecosystem Position

TRL's greatest strength is its integration with the HuggingFace ecosystem (datasets, transformers, accelerate, PEFT). With 15.3k ⭐ and 391 contributors, it has the largest community among RL libraries.

| Aspect | TRL | Comparison with Other Libraries |
|------|-----|-------------------|
| Design Philosophy | Simplicity, HF integration | Verl: Performance-focused, Verifiers: Environment expansion built on TRL |
| Target | RLHF, reasoning models (single-turn) | Verifiers, RAGEN: Multi-turn agent RL |
| Environment Support | ❌ | SkyRL, RAGEN: ✅ Custom environments |
| Scalability | Limited by HF Trainer | Verl: FSDP+Megatron, slime: Megatron-specific |
| Async Training | ❌ | AReaL, slime, OpenRLHF: ✅ |

TRL is best suited for text-based RL (RLHF, reasoning model training). For multi-turn RL and agent training, [[concepts/post-training/verifiers-rl|Verifiers]] (a TRL-based extension), [[concepts/hybrid-flow|Verl]], and [[concepts/post-training/skyrl|SkyRL]] are more appropriate.

→ Full RL library comparison: [[comparisons/open-source-rl-libraries-comparison]]

## Related

- [[concepts/post-training/grpo-rl-training]] — GRPO implementation details
- [[concepts/post-training/rlhf-dpo-preference]] — Preference optimization methods
- [[concepts/post-training/peft-lora-qlora]] — Parameter-efficient fine-tuning
- [[comparisons/open-source-rl-libraries-comparison]] — 10 RL library comparison portal
- [[concepts/post-training/verifiers-rl]] — TRL-based multi-turn RL extension

## Sources

- [TRL Documentation](https://huggingface.co/docs/trl)
- [TRL GitHub](https://github.com/huggingface/trl)
- [Anyscale: Open Source RL Libraries for LLMs](https://www.anyscale.com/blog/open-source-rl-libraries-for-llms)
