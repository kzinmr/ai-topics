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
  - concepts/fine-tuning/_index
  - concepts/fine-tuning/grpo-rl-training
  - concepts/fine-tuning/rlhf-dpo-preference
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

TRLはHuggingFaceエコシステム（datasets, transformers, accelerate, PEFT）との統合を最大の強みとする。15.3k ⭐、391 contributorsとRLライブラリ中最大のコミュニティ。

| 側面 | TRL | 他ライブラリとの比較 |
|------|-----|-------------------|
| 設計哲学 | シンプルさ、HF統合 | Verl: パフォーマンス重視、Verifiers: TRLベースで環境拡張 |
| ターゲット | RLHF、推論モデル（シングルターン） | Verifiers, RAGEN: マルチターンエージェントRL |
| 環境サポート | ❌ | SkyRL, RAGEN: ✅ カスタム環境 |
| 拡張性 | HF Trainerで制限 | Verl: FSDP+Megatron、slime: Megatron特化 |
| Async訓練 | ❌ | AReaL, slime, OpenRLHF: ✅ |

TRLはテキストベースRL（RLHF、推論モデル訓練）に最適。マルチターンRLやエージェント訓練には [[concepts/verifiers-rl|Verifiers]]（TRLベースの拡張）や [[concepts/hybrid-flow|Verl]]、[[concepts/skyrl|SkyRL]] が適する。

→ 全RLライブラリ比較: [[comparisons/open-source-rl-libraries-comparison]]

## Related

- [[concepts/fine-tuning/grpo-rl-training]] — GRPO implementation details
- [[concepts/fine-tuning/rlhf-dpo-preference]] — Preference optimization methods
- [[concepts/fine-tuning/peft-lora-qlora]] — Parameter-efficient fine-tuning
- [[comparisons/open-source-rl-libraries-comparison]] — 10 RLライブラリ比較ポータル
- [[concepts/verifiers-rl]] — TRLベースのマルチターンRL拡張

## Sources

- [TRL Documentation](https://huggingface.co/docs/trl)
- [TRL GitHub](https://github.com/huggingface/trl)
- [Anyscale: Open Source RL Libraries for LLMs](https://www.anyscale.com/blog/open-source-rl-libraries-for-llms)
