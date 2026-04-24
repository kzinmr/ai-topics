---
title: "Axolotl — Fine-Tuning Framework"
type: concept
created: 2026-04-19
updated: 2026-04-19
tags: [fine-tuning, axolotl, framework, yaml, llm-training]
related:
  - concepts/fine-tuning/_index
  - concepts/fine-tuning/trl
sources: []
---

# Axolotl

Axolotl is a YAML-configured fine-tuning framework supporting 100+ models with LoRA/QLoRA, DPO/KTO/ORPO/GRPO, and multimodal capabilities.

## Key Features

- **YAML-based configuration** — declarative, version-controllable training setups
- **100+ model support** — Llama, Mistral, Qwen, Gemma, Phi, and more
- **Multiple training methods** — SFT, DPO, KTO, ORPO, GRPO, PPO
- **PEFT integration** — LoRA, QLoRA, AdaLoRA out of the box
- **Distributed training** — DeepSpeed, FSDP support
- **Multimodal** — vision-language model fine-tuning
- **Cloud integration** — Modal, RunPod, and other cloud platforms

## Configuration Example

```yaml
base_model: Qwen/Qwen2.5-1.5B-Instruct
model_type: AutoModelForCausalLM
tokenizer_type: AutoTokenizer

load_in_8bit: true
load_in_4bit: false
strict: false

datasets:
  - path: your-dataset.jsonl
    type: alpaca

sequence_len: 4096
sample_packing: true
eval_sample_packing: false
pad_to_sequence_len: true

adapter: lora
lora_r: 32
lora_alpha: 64
lora_dropout: 0.05
lora_target_linear: true

gradient_accumulation_steps: 4
micro_batch_size: 2
num_epochs: 3
optimizer: adamw_bnb_8bit
learning_rate: 0.0002

lr_scheduler: cosine
warmup_steps: 100

fsdp:
  - full_shard
  - auto_wrap
fsdp_config:
  fsdp_offload_params: true
  fsdp_state_dict_type: FULL_STATE_DICT
```

## FSDP Configuration

```yaml
fsdp_version: 2
fsdp_config:
  offload_params: true
  state_dict_type: FULL_STATE_DICT
  auto_wrap_policy: TRANSFORMER_BASED_WRAP
  transformer_layer_cls_to_wrap: LlamaDecoderLayer
  reshard_after_forward: true
```

## NCCL Testing

Before distributed training, validate network performance:

```bash
./build/all_reduce_perf -b 8 -e 128M -f 2 -g 3
```

## Compressed Model Saving

```yaml
save_compressed: true
```

Reduces disk space by ~40% while maintaining vLLM and llmcompressor compatibility.

## Context Parallelism

`context_parallel_size` should be a divisor of total GPU count. With 8 GPUs and context_parallel_size=4, only 2 different batches are processed per step (each split across 4 GPUs).

## Related

- [[concepts/fine-tuning/trl.md]] — TRL library (Axolotl uses TRL under the hood)
- [[concepts/fine-tuning/unsloth.md]] — Alternative fast fine-tuning framework
- [[concepts/fine-tuning/pytorch-fsdp.md]] — FSDP distributed training

## Sources

- [Axolotl GitHub](https://github.com/axolotl-ai-cloud/axolotl)
- [Axolotl Documentation](https://axolotl-ai-cloud.github.io/axolotl/)
