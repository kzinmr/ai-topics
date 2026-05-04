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
  - raw/articles/2024-06_justine-tunney-llama-cpu-matmul.md
  - raw/articles/2024-03_answerai-fsdp-qlora-benchmarks.md
  - raw/articles/2026-05-04_phil-schmid-fsdp-qlora-llama3.md
  - https://github.com/AnswerDotAI/fsdp_qlora
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

### Answer.AI Official Benchmarks (70B Model)

Answer.AI's fsdp_qlora repo provides real benchmarks for Llama-2 70B training (1,024 samples, context length 2048, effective batch size 32):

| Accelerator | GPUs | CPU Offload | Time (s) | Ballpark Cost |
| :--- | :---: | :---: | :---: | :--- |
| **A5000 24GB** | 2 | True | 9,688 | $2.37 – $4.14 |
| **A5000 24GB** | 8 | False | 2,613 | $2.55 – $4.47 |
| **A6000 Ada 48GB** | 2 | False | 5,867 | $3.72 – $5.22 |
| **A100 40GB SXM** | 4 | False | 1,266 | $2.53 – $2.90 |
| **H100 80GB SXM** | 4 | False | 667 | $3.48 – $3.53 |

**Key Finding:** Total cost to train 70B remains surprisingly consistent ($2–5) across all hardware tiers. Upper hardware (H100) is 14.5× faster but costs about the same per-run. The real ROI comes from existing hardware — using what you already own is more cost-effective despite longer wall time.

### Hardware Bottlenecks

- **Interconnect Speed:** On machines with slow PCIe lanes (older motherboards), GPU ↔ GPU data transfer overhead can outweigh the benefits of quantization-based sharding.
- **CPU RAM Saturation:** Training a 70B model can saturate 128GB of CPU RAM during initialization. A swapfile (e.g., 10GB) may be necessary to prevent crashes.
- **PCIe vs. NVLink:** Dual 3090 setups benefit greatly from NVLink. Dual 4090 setups require a workstation motherboard with **full x16 PCIe v4 lanes** to minimize FSDP overhead.

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

## Practical Optimization Guide

Answer.AI recommends a progressive memory-savings approach — start simple and escalate only when needed:

| Step | Configuration | Method | When to Use |
|:-----|:-------------|:-------|:------------|
| 1 | **Vanilla** | DDP, batch size 1, no memory options | Starting point (model fits single GPU) |
| 2 | **Gradient Checkpointing** | Recompute activations during backward pass | First memory bottleneck |
| 3 | **SHARD_GRAD_OP** | FSDP ZeRO-2: shard gradients + optimizer only | Parameters still fit in GPU but optim states OOM |
| 4 | **FULL_SHARD** | FSDP ZeRO-3: shard params + gradients + optim | Model doesn't fit in single-GPU memory |
| 5 | **CPU Offloading** | Move shards to CPU RAM when inactive | Extreme VRAM constraints (e.g., 24GB cards for 70B) |
| 6 | **Activation Offloading** | Move intermediate activations to CPU RAM | Last resort (single 16GB GPU) |

> **Key strategy:** Once stable at batch size 1, try increasing batch size. Moving to a heavier memory-saving step may be faster overall if it enables a significantly larger batch size.

### CPU Performance & Offloading Viability

Offloading to CPU during training depends critically on CPU math throughput. Justine Tunney's 84 new matmul kernels (llamafile/llama.cpp) demonstrated **30–500% faster CPU matrix multiplication**, with some configurations exceeding Intel MKL by 2× for L2-cache fits.

This is directly relevant to [[concepts/pytorch-fsdp#DDP vs FSDP: When to Use Which|CPU offloading in FSDP/DeepSpeed]]: when offloaded parameters require CPU computation before being sent back to GPU, faster CPU matmul reduces the PCIe transfer bottleneck. The more efficient CPU becomes, the less penalty offloading incurs — making CPU-offloaded FSDP+Q-LoRA training on 24GB cards more viable.

### DDP vs FSDP Decision Rule

> **If model fits on a single GPU, use DDP (not FSDP).** FSDP's all-gather communication overhead exceeds its benefits when the model already fits in GPU memory. QLoRA's 4-bit quantization already reduces memory footprint enough that many models that previously required FSDP (e.g., 7B) now fit on single GPUs with DDP.

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
