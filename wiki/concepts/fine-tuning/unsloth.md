---
title: "Unsloth — Fast Fine-Tuning"
type: concept
created: 2026-04-19
updated: 2026-04-19
tags:
  - fine-tuning
  - unsloth
  - optimization
  - speed
related:
  - concepts/fine-tuning/_index
  - concepts/fine-tuning/axolotl
  - concepts/fine-tuning/trl
sources: []
---

# Unsloth

Unsloth is a fine-tuning optimization library providing 2-5x faster training with 50-80% less memory usage through custom Triton kernels and LoRA/QLoRA optimization.

## Key Benefits

- **2-5x faster training** — Custom Triton kernels replace standard PyTorch operations
- **50-80% less memory** — Optimized memory layout and kernel fusion
- **LoRA/QLoRA native** — Built-in parameter-efficient fine-tuning
- **Wide model support** — Llama, Mistral, Gemma, Qwen, and more
- **Seamless TRL integration** — Works with GRPOTrainer, SFTTrainer, DPOTrainer

## Quick Setup

```python
from unsloth import FastLanguageModel

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="google/gemma-3-1b-it",
    max_seq_length=1024,
    load_in_4bit=True,         # QLoRA
    fast_inference=True,       # vLLM backend
    max_lora_rank=32,
)

model = FastLanguageModel.get_peft_model(
    model,
    r=32,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
                    "gate_proj", "up_proj", "down_proj"],
    lora_alpha=32,
    use_gradient_checkpointing="unsloth",  # Memory optimization
)
```

## GRPO Training with Unsloth

```python
from trl import GRPOTrainer

trainer = GRPOTrainer(
    model=model,
    reward_funcs=[format_reward, correctness_reward],
    args=training_args,
    train_dataset=dataset,
)
trainer.train()
```

## Memory Optimization Techniques

1. **4-bit quantization** (`load_in_4bit=True`) — NF4 format with minimal accuracy loss
2. **Gradient checkpointing** (`use_gradient_checkpointing="unsloth"`) — Trade compute for memory
3. **Triton kernels** — Custom GPU kernels replace standard operations
4. **LoRA merging** — Adapters merge into base model with no inference latency

## Supported Models

| Model Family | 4-bit Support | LoRA Support |
|-------------|--------------|--------------|
| Llama 3.x | ✅ | ✅ |
| Mistral | ✅ | ✅ |
| Gemma 3 | ✅ | ✅ |
| Qwen 2.5 | ✅ | ✅ |
| Phi-4 | ✅ | ✅ |

## Comparison to Standard Fine-Tuning

| Metric | Standard PyTorch | Unsloth |
|--------|-----------------|---------|
| Training speed | 1x | 2-5x |
| Memory usage | 100% | 20-50% |
| Setup complexity | High | Low |
| Model compatibility | All | Select models |

## Related

- [[concepts/fine-tuning/axolotl]] — Alternative framework with YAML configuration
- [[concepts/fine-tuning/trl]] — TRL library integration
- [[concepts/fine-tuning/peft-lora-qlora]] — LoRA/QLoRA fundamentals

## Sources

- [Unsloth Documentation](https://docs.unsloth.ai/)
- [Unsloth GitHub](https://github.com/unslothai/unsloth)
