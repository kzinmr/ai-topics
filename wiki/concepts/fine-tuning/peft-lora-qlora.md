---
title: "PEFT, LoRA, and QLoRA"
created: 2026-04-19
updated: 2026-04-19
tags: [fine-tuning, peft, lora, qlora, parameter-efficient]
related:
  - concepts/fine-tuning/_index
  - concepts/fine-tuning/unsloth
  - concepts/fine-tuning/axolotl
---

# PEFT, LoRA, and QLoRA

**Parameter-Efficient Fine-Tuning (PEFT)** enables training large models (7B-70B+) by updating only a small subset of parameters, typically <1%, while maintaining near-full fine-tuning accuracy.

## Why PEFT?

Full fine-tuning of a 70B model requires hundreds of GBs of GPU memory. PEFT methods reduce this dramatically by:
- Freezing most of the pre-trained model
- Training only lightweight adapter modules
- Enabling multi-adapter serving (one base model + many task-specific adapters)

## LoRA (Low-Rank Adaptation)

LoRA injects trainable rank decomposition matrices into Transformer layers:

```
W' = W + ΔW = W + BA
```

Where W is frozen, and B, A are low-rank matrices (r << d).

**Key Parameters:**
- `r` (rank): Higher = more capacity (16-64 typical)
- `lora_alpha`: Scaling factor (typically 2×r)
- `target_modules`: Which layers to adapt (q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj)

**Advantages:**
- No inference latency added (adapters merge into base model)
- Small checkpoint sizes (~100MB vs ~100GB)
- Easy to swap adapters for different tasks

## QLoRA (Quantized LoRA)

QLoRA combines 4-bit quantization with LoRA:
- Base model quantized to 4-bit (NF4)
- LoRA adapters trained in 16-bit
- Enables fine-tuning 65B models on a single 48GB GPU

**Trade-off:** ~1-2% accuracy loss vs full precision, but 4× memory reduction.

## Other PEFT Methods (25+ in HuggingFace PEFT library)

| Method | Approach | Best For |
|--------|----------|----------|
| **LoRA** | Low-rank injection | General fine-tuning |
| **QLoRA** | Quantized + LoRA | Limited GPU memory |
| **AdaLoRA** | Adaptive rank allocation | Budget-constrained training |
| **IA³** | Rescaling activations | Minimal parameter count |
| **Prompt Tuning** | Learnable prompt vectors | Task adaptation without weight changes |
| **Prefix Tuning** | Learnable prefix tokens | Generation tasks |
| **P-Tuning v2** | Deep prompt tuning | Multi-task learning |

## Integration with Training Frameworks

LoRA/QLoRA works seamlessly with:
- **TRL** (Transformer Reinforcement Learning) — `peft_config` parameter in GRPOTrainer/SFTTrainer
- **Unsloth** — Built-in LoRA optimization with 2-3x speedup
- **Axolotl** — YAML-configured LoRA/QLoRA with `load_in_4bit: true`

## Example: LoRA with TRL

```python
from peft import LoraConfig

peft_config = LoraConfig(
    r=16,                          # Rank
    lora_alpha=32,                 # Scaling factor (2×r)
    target_modules=[
        "q_proj", "k_proj", "v_proj", "o_proj",
        "gate_proj", "up_proj", "down_proj"
    ],
    task_type="CAUSAL_LM",
    lora_dropout=0.05,
)

# Pass to any TRL trainer (GRPOTrainer, SFTTrainer, DPOTrainer)
trainer = GRPOTrainer(
    model=model,
    peft_config=peft_config,
    ...
)
```

## Merging Adapters for Deployment

```python
# Merge LoRA adapters into base model for production
merged_model = model.merge_and_unload()
merged_model.save_pretrained("production_model")
tokenizer.save_pretrained("production_model")
```

## Related Concepts
- [[concepts/fine-tuning/unsloth]] — 2-5x faster fine-tuning with LoRA optimization
- [[concepts/fine-tuning/axolotl]] — YAML-config fine-tuning with LoRA/QLoRA support
- [[concepts/fine-tuning/grpo-rl-training]] — GRPO training with PEFT integration
- [[concepts/fine-tuning/quantization-overview]] — GGUF/GPTQ/FP8 quantization formats

## Sources
- HuggingFace PEFT documentation (huggingface.co/docs/peft)
- LoRA paper (Hu et al., 2021)
- QLoRA paper (Dettmers et al., 2023)
