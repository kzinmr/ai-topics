---
title: "TGI Multi-LoRA: Deploy Once, Serve 30 Models"
source: "Hugging Face Blog"
url: "https://huggingface.co/blog/multi-lora-serving"
author: "Hugging Face / Predibase"
date: 2024-07-18
tags:
  - inference
  - tgi
  - lora
  - multi-lora
  - serving
  - huggingface
  - efficiency
---

# TGI Multi-LoRA: Deploy Once, Serve 30 Models

**TGI Multi-LoRA** enables serving multiple specialized LoRA adapters from a single base model deployment using Text Generation Inference (TGI), reducing costs by ~30x compared to per-adapter deployments.

## The Motivation
Organizations are moving toward a "fine-tuned world" where many small, specialized models outperform large general-purpose models.
- Task-specific LoRAs (e.g., Mistral-7B) can outperform GPT-4 on specialized tasks
- One base model supports vastly different downstream tasks
- Different teams can update/evaluate their own adapters independently
- Enables data segregation and easier on-device deployment
- LoRA adapters add only **~1% storage/memory overhead** compared to base model

> "Loading 30 adapters into RAM results in only a 3% increase in VRAM... equivalent to having multiple fine-tuned models in one single deployment."

## Technical Background
- **LoRA:** Freezes pre-trained weights and adds small trainable matrices
- **Multi-LoRA Serving:** TGI dynamically picks the correct adapter via `adapter_id` in the request, enabling **heterogeneous batches** (different adapters in one batch)

## Deployment

### Requirements
- TGI v2.1.1+
- Base model compatible with adapters
- `LORA_ADAPTERS` env var listing Hub IDs

```bash
docker run --gpus all -p 8080:80 \
    ghcr.io/huggingface/text-generation-inference:2.1.1 \
    --model-id mistralai/Mistral-7B-v0.1 \
    --lora-adapters=predibase/customer_support,predibase/magicoder
```

### Usage
```bash
curl 127.0.0.1:3000/generate -X POST \
    -d '{"inputs": "Hello", "parameters": {"adapter_id": "predibase/customer_support"}}'
```

## Key Facts
| Metric | Value |
|:-------|:------|
| Adapter size | ~13.6MB (vs 14.48GB base) |
| VRAM impact | ~3% increase for 30 adapters |
| Training cost | ~$8.00 per adapter |
| Throughput | 75 req/s on Nvidia L4 (Mistral-7B) |

## Optimization
TGI uses optimized kernels from **Punica** and **LoRAX** for efficient multi-adapter handling.
