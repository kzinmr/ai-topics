---
title: "FSDP + Q-LoRA"
type: concept
created: 2026-05-04
updated: 2026-05-04
tags:
  - concept
  - fine-tuning
  - distributed-training
  - memory-efficiency
  - peft
  - quantization
aliases:
  - FSDP+Q-LoRA
  - FSDP with Q-LoRA
related:
  - concepts/pytorch-fsdp
  - concepts/qlora
  - concepts/peft-fine-tuning
  - entities/phil-schmid
sources:
  - raw/articles/2026-05-04_phil-schmid-fsdp-qlora-llama3.md
  - https://www.philschmid.de/fsdp-qlora-llama3
---

# FSDP + Q-LoRA

**FSDP + Q-LoRA** is a combined training technique that integrates PyTorch's **Fully Sharded Data Parallel (FSDP)** with **Quantized Low-Rank Adaptation (Q-LoRA)**, developed through a collaboration between Answer.AI, Tim Dettmers, and Hugging Face. It enables fine-tuning of massive language models (e.g., Llama 3 70B) on as few as 2× 40GB GPUs by sharding quantized model states across devices.

## Overview

The core innovation is making FSDP (which normally requires full-precision parameters for sharding) compatible with 4-bit quantized weights. Previous approaches required base models in FP16/FP32 for FSDP sharding; this breakthrough allows FSDP to operate on NF4-quantized model states, drastically reducing the memory floor per GPU.

> "FSDP + Q-LoRA allows sharding quantized model states across multiple GPUs."
> — Phil Schmid

## Hardware Requirements & Memory Scaling

The technique offers multiple tiers of hardware accessibility:

| Method | Hardware Required | Relative Cost |
|:---|:---|---:|
| Full Fine-tuning | ~16 × 80GB GPUs (e.g., H100) | Baseline (most expensive) |
| FSDP + LoRA (FP16) | ~8 × 80GB GPUs | ~50% of full ft |
| **FSDP + Q-LoRA** | **~2 × 40GB GPUs** (e.g., A100) | **~12.5% of full ft** |
| FSDP + Q-LoRA + CPU Offload | 4 × 24GB GPUs (e.g., A10G) | Most accessible tier |

### Real-World Cost Example

For Llama 3 70B, 3-epoch training:
- **4× A10G (g5.12xlarge):** ~$5.67/h × 45h = **~$255**
- **4× H100:** ~$1.25h (p95) = **~$25–50**

## Technical Architecture

### How It Works

1. **Model Loading:** Base model is loaded in 4-bit NF4 quantization via `bitsandbytes`
2. **LoRA Adapters:** Low-rank adapters (in FP16/FP32) are attached to the quantized model
3. **FSDP Wrapping:** FSDP wraps the combined model, sharding both quantized weights and LoRA adapters across GPUs
4. **Sharded Quantized States:** Each GPU holds only its fraction of the quantized model + its fraction of the LoRA weights
5. **CPU Offloading (optional):** When VRAM is critically constrained, least-recently-used shards are offloaded to CPU RAM

```ascii
                    FSDP Wrapping Layer
┌──────────────────────────────────────────────┐
│                GPU 0   GPU 1   GPU 2   GPU 3 │
│  Quantized (NF4) Weights:  [shard] [shard]  │
│  LoRA Adapters (FP16):     [shard] [shard]  │
│  Optimizer States:         [shard] [shard]  │
│  Gradients:                [shard] [shard]  │
└──────────────────────────────────────────────┘
      ↑ Shard reconstruction on-demand via all-gather
      ↑ CPU RAM acts as overflow (offload mode)
```

### Key Configuration

```yaml
fsdp: "full_shard auto_wrap offload"  # ZeRO-3 + CPU offload
fsdp_config:
  backward_prefetch: "backward_pre"   # Prefetch during backward pass
  forward_prefetch: "false"
  use_orig_params: "false"             # Required for Q-LoRA compatibility
```

```bash
# Launch with CPU-efficient loading
ACCELERATE_USE_FSDP=1 FSDP_CPU_RAM_EFFICIENT_LOADING=1 \
torchrun --nproc_per_node=4 ./scripts/run_fsdp_qlora.py \
  --config llama_3_70b_fsdp_qlora.yaml
```

## Implementation Details

### Required Stack
- **PyTorch 2.2+** — FSDP and SDPA (Flash Attention v2)
- **bitsandbytes 0.43+** — 4-bit NF4 quantization
- **PEFT 0.10+** — LoRA adapter management
- **TRL 0.8+** — SFTTrainer for supervised fine-tuning
- **Accelerate 0.29+** — FSDP configuration and launch

### Critical Implementation Notes

1. **Chat Templates Matter:** Using base Llama 3 special tokens requires updating both embedding layer and `lm_head`, increasing memory. Vicuna-style templates (`User:` / `Assistant:`) avoid this penalty.
2. **Merging Adapters is Memory-Intensive:** After training, merging Q-LoRA adapters back into the base model requires ~192GB CPU RAM for a 70B model.
3. **Adapter-Only Saves:** Q-LoRA saves only the low-rank adapters — not the full model weights. Production deployment via TGI requires a full merge.

### Inference After Training

```python
from peft import AutoPeftModelForCausalLM
from transformers import AutoTokenizer

model = AutoPeftModelForCausalLM.from_pretrained(
    "./llama-3-70b-hf-no-robot",
    torch_dtype=torch.float16,
    quantization_config={"load_in_4bit": True},
    device_map="auto"
)
```

## Comparison with Alternatives

| Aspect | FSDP + Q-LoRA | FSDP + LoRA | Full Fine-Tuning |
|--------|---------------|-------------|------------------|
| **Base precision** | 4-bit NF4 | FP16 | FP16/BF16 |
| **GPU floor (70B)** | 2× 40GB | 8× 80GB | 16× 80GB |
| **Cost (70B, 3 epochs)** | ~$255 | ~$2,000+ | ~$10,000+ |
| **Speed** | Slowest (dequant overhead) | Medium | Fastest |
| **Task quality** | Near-full (~99%) | Full (~99.5%) | Baseline |
| **Production merge** | Required (~192GB RAM) | Required | Not needed |

## Key People & Organizations

- [[entities/phil-schmid]] — Author of the practical guide
- **Tim Dettmers** — Q-LoRA inventor, collaboration lead for FSDP integration
- **Answer.AI** — Co-developed the FSDP sharding mechanism for quantized weights
- **Hugging Face** — Integration into TRL, PEFT, Accelerate, and Transformers

## Related Concepts

- [[concepts/pytorch-fsdp]] — The sharding framework behind the technique
- [[concepts/qlora]] — The quantization + LoRA method that enables 4-bit training
- [[concepts/peft-fine-tuning]] — Umbrella for parameter-efficient fine-tuning methods
