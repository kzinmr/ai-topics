---
title: "Benchmarking QLoRA + FSDP: Training Performance Analysis"
source: "Answer.AI (fsdp_qlora repo)"
url: "https://raw.githubusercontent.com/AnswerDotAI/fsdp_qlora/refs/heads/main/benchmarks_03_2024.md"
author: "Answer.AI"
date: 2024-03
tags:
  - fine-tuning
  - fsdp
  - qlora
  - benchmarking
  - distributed-training
  - memory-efficiency
  - answer-ai
  - performance
---

# Benchmarking QLoRA + FSDP: Training Performance Analysis

This report analyzes the performance of combining **Fully Sharded Data Parallel (FSDP)** with **QLoRA** to enable training of large models (up to 70B) on consumer-grade and professional hardware.

## 1. Key Technical Insights & Excerpts

### The Core Value Proposition
The primary breakthrough is the ability to shard quantized weights across multiple GPUs, significantly lowering the VRAM entry barrier for massive models.

> "QLoRA enables a larger max batch size, giving it an extra speed advantage over the standard LoRA version... by using less memory for model weights."

### Hardware Bottlenecks
- **Interconnect Speed:** On machines with slow PCIe lanes (e.g., older motherboards), data transfer between GPUs can outweigh the benefits of avoiding quantization.
- **CPU RAM:** Training a 70B model can saturate 128GB of CPU RAM during initialization. A swapfile (e.g., 10GB) may be necessary to prevent crashes.
- **PCIe vs. NVLink:** For dual 3090 setups, NVLink is highly recommended. For dual 4090s, a workstation motherboard with **full x16 PCIe v4 lanes** is essential to minimize FSDP overhead.

### Baseline Command Template
```bash
python train.py --model_name meta-llama/Llama-2-7b-hf \
  --batch_size 1 --context_length 512 \
  --train_type qlora --use_gradient_checkpointing True \
  --reentrant_checkpointing True --use_cpu_offload False \
  --log_to wandb --dataset dummy --dataset_samples 1024
```

## 2. Case Study: Dual GPU Performance

### Llama-2 7B (Consumer Hardware)
- **Memory Efficiency:** QLoRA (4-bit) uses significantly less VRAM than LoRA (16-bit), allowing for higher batch sizes which improves overall throughput.
- **DDP vs. FSDP:** If a model fits entirely on a single GPU's VRAM, using **Distributed Data Parallel (DDP)** is often faster than FSDP because it avoids weight sharding communication overhead.

### Yi 34B & Llama-2 70B
- **CPU Offloading:** Storing weights in CPU RAM (`--use_cpu_offload true`) allows for larger batch sizes. On a dual 3090 rig, the higher batch size enabled by offloading actually made training *faster* than keeping weights on-GPU with a smaller batch size.
- **70B Feasibility:** Training a 70B model on dual 3090s is possible but slow (~50s per batch). With **activation offloading**, it is theoretically possible to train on a single 16GB GPU.

## 3. Hardware Recommendations & Cost Analysis (70B Model)

Benchmarks for training 1,024 samples of Llama-2 70B (Context Length 2048, Effective Batch Size 32):

| Accelerator | GPUs | CPU Offload | Time (s) | Ballpark Cost |
| :--- | :---: | :---: | :---: | :--- |
| **A5000 24GB** | 2 | True | 9,688 | $2.37 - $4.14 |
| **A5000 24GB** | 8 | False | 2,613 | $2.55 - $4.47 |
| **A6000 Ada 48GB** | 2 | False | 5,867 | $3.72 - $5.22 |
| **A100 40GB SXM** | 4 | False | 1,266 | $2.53 - $2.90 |
| **H100 80GB SXM** | 4 | False | 667 | $3.48 - $3.53 |

**Key Finding:** While high-end GPUs (H100) are much faster, the **total cost to train** remains relatively consistent across tiers. Lower-end hardware is more cost-effective if you already own it, despite longer wait times.

## 4. Practical Guide for Optimal Configuration

To find the fastest training setup without Out-of-Memory (OOM) errors, follow these steps in order:

1. **Vanilla Start:** Use DDP, Batch Size 1, and no memory-saving options.
2. **Gradient Checkpointing:** Enable to save memory by recomputing activations during the backward pass.
3. **SHARD_GRAD_OP:** Shard only gradients and optimizer states (FSDP ZeRO-2 style).
4. **FULL_SHARD:** Shard parameters, gradients, and optimizer states (FSDP ZeRO-3 style).
5. **CPU Offloading:** Move parameters and gradients to CPU RAM when not in use.
6. **Activation Offloading:** Move intermediate activations to CPU RAM.

**Optimization Tip:** Once you find a stable configuration at Batch Size 1, try to increase the batch size. If you hit an OOM, it may be faster to move to the next "heavier" memory-saving step (e.g., moving from DDP to FULL_SHARD) if it allows a significantly larger batch size.
