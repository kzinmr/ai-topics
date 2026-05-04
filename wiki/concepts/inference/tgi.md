---
title: "Text Generation Inference (TGI)"
type: concept
created: 2026-05-04
updated: 2026-05-04
tags:
  - concept
  - inference
  - serving
  - huggingface
  - lora
  - multi-lora
  - tgi
aliases:
  - TGI
  - Text Generation Inference
  - Hugging Face TGI
related:
  - concepts/inference/vllm
  - concepts/inference/sglang
  - concepts/inference/llama-cpp
  - concepts/qlora
  - concepts/fine-tuning/peft-lora-qlora
  - concepts/fine-tuning/pytorch-fsdp
sources:
  - raw/articles/2024-07-18_tgi-multi-lora-serving.md
  - https://huggingface.co/blog/multi-lora-serving
  - https://huggingface.co/docs/text-generation-inference
---

# Text Generation Inference (TGI)

**Text Generation Inference (TGI)** is Hugging Face's production-grade inference server for large language models, developed and maintained by the Hugging Face team. Its standout capability is **Multi-LoRA serving** — deploying a single base model with multiple LoRA adapters, dynamically selecting the right adapter per request.

## Overview

TGI is optimized for Hugging Face ecosystem integration (Transformers, PEFT, Hub) and provides a drop-in OpenAI-compatible API. Like [[concepts/inference/vllm|vLLM]] and [[concepts/inference/sglang|SGLang]], it supports continuous batching, PagedAttention, and quantization. However, TGI's key differentiator is its **first-class Multi-LoRA support**, making it the most practical choice for organizations running many fine-tuned adapter variants.

## Multi-LoRA Serving

The core innovation: deploy one base model, load dozens of LoRA adapters into the same VRAM, and route requests to the correct adapter via a simple `adapter_id` parameter.

### How It Works

1. Base model (e.g., Mistral-7B) is loaded once into GPU memory
2. Multiple LoRA adapters are loaded alongside, each adding ~1% memory overhead
3. Each inference request specifies an `adapter_id` (HF Hub ID)
4. TGI dynamically selects the correct adapter weights, enabling **heterogeneous batches** with different adapters in one batch

```bash
# Launch with 30+ adapters
docker run --gpus all ghcr.io/huggingface/text-generation-inference:2.1.1 \
    --model-id mistralai/Mistral-7B-v0.1 \
    --lora-adapters=predibase/customer_support,predibase/magicoder,...
```

```bash
# Each request picks its adapter
curl 127.0.0.1:3000/generate \
    -d '{"inputs": "Hello", "parameters": {"adapter_id": "predibase/customer_support"}}'
```

### Economics

| Metric | Single Model Deployment | Multi-LoRA (30 adapters) |
|:-------|:----------------------|:-------------------------|
| VRAM per deployment | ~14.5 GB (Mistral-7B) | ~14.9 GB (+3%) |
| Cost | Scales linearly per model | Flat (one base model) |
| Training cost | Full fine-tune per model | ~$8 per adapter |
| Maintenance | Update each deployment | Update adapter only |

> "Loading 30 adapters into RAM results in only a 3% increase in VRAM... effectively equivalent to having multiple fine-tuned models in one single deployment."

### Performance

- **75 requests/s** on Nvidia L4 (Mistral-7B base)
- Adapter size: ~13.6MB (vs 14.48GB base model)
- Optimized kernels from **Punica** and **LoRAX** for multi-adapter efficiency

## Comparison with Alternatives

| Aspect | TGI | vLLM | SGLang |
|:-------|:----|:-----|:-------|
| **Target** | HF ecosystem serving | General production | Research + production |
| **Multi-LoRA** | **First-class** (native) | Via separate deployment | Limited |
| **PagedAttention** | Yes | Yes (native) | Yes (RadixAttention) |
| **Continuous batching** | Yes | Yes | Yes |
| **HF Hub integration** | Deep (native) | Via transformers | Via transformers |
| **OpenAI API** | Yes | Yes | Yes |
| **Quantization** | GPTQ, AWQ, bitsandbytes | GPTQ, AWQ, FP8 | FP8, INT8 |
| **Kernel optimization** | Punica, LoRAX | FlashAttention, CUDA kernels | RadixAttention, Triton |

## Relationship to LoRA / PEFT

TGI Multi-LoRA is the **production serving counterpart** to PEFT training workflows:

1. **Train:** Fine-tune multiple LoRA adapters using [[concepts/fine-tuning/peft-lora-qlora]] with tools like TRL SFTTrainer
2. **Serve:** Deploy all adapters as a single TGI endpoint
3. **Route:** Each request selects its adapter dynamically

## Key Advantages

- **Cost efficiency:** ~30× cheaper than per-adapter deployments
- **Operational simplicity:** Manage one endpoint instead of 30
- **Usage smoothing:** Bursty/low-usage adapters "fill in" gaps, reducing idle GPU
- **Independent iteration:** Teams update their adapter without redeploying the base
- **Privacy:** Adapter-level data segregation

## Related Concepts

- [[concepts/inference/vllm]] — Alternative serving engine with different optimization focus
- [[concepts/inference/sglang]] — Research-oriented serving with RadixAttention
- [[concepts/inference/llama-cpp]] — Local inference engine
- [[concepts/qlora]] — Quantized LoRA training approach
- [[concepts/fine-tuning/peft-lora-qlora]] — Parameter-efficient fine-tuning methods
