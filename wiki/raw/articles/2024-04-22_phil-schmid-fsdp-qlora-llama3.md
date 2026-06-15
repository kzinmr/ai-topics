---
title: "Efficiently fine-tune Llama 3 with PyTorch FSDP and Q-Lora"
source: "Phil Schmid Blog"
url: "https://www.philschmid.de/fsdp-qlora-llama3"
author: "Phil Schmid"
date: 2026-05-04
tags:
  - fine-tuning
  - fsdp
  - qlora
  - llama3
  - distributed-training
  - memory-efficiency
  - pytorch
  - peft
---

# Efficiently fine-tune Llama 3 with PyTorch FSDP and Q-Lora

This guide details how to fine-tune large language models like **Llama 3 70B** using a combination of **PyTorch FSDP (Fully Sharded Data Parallel)** and **Q-LoRA**. This approach makes training massive models accessible on consumer-grade or mid-tier GPU setups (e.g., 4x A10G 24GB).

## 🚀 Key Technologies & Breakthroughs
*   **FSDP + Q-LoRA:** A collaboration between Answer.AI, Tim Dettmers, and Hugging Face that allows sharding quantized model states across multiple GPUs.
*   **Memory Efficiency:** Enables training a 70B model on as little as 2x 40GB GPUs (or 4x 24GB GPUs with CPU offloading).
*   **SDPA:** Uses PyTorch's Scaled Dot Product Attention (Flash Attention v2) for faster processing.

## 1. Environment Setup
Required libraries include `trl` (for SFTTrainer), `peft` (for LoRA), and `bitsandbytes` (for quantization).

```bash
pip install "torch==2.2.2" tensorboard
pip install --upgrade "transformers==4.40.0" "datasets==2.18.0" \
"accelerate==0.29.3" "evaluate==0.4.1" "bitsandbytes==0.43.1" \
"trl==0.8.6" "peft==0.10.0"
```

## 2. Dataset Preparation
The guide uses the **HuggingFaceH4/no_robots** dataset (10,000 human-annotated instructions).
*   **Format:** OpenAI-style messages (System, User, Assistant).
*   **Customization:** A custom system message is added to ensure the model follows a specific persona.
*   **Filtering:** Conversations are filtered to ensure an even number of turns (User/Assistant pairs).

## 3. Training Configuration
The training uses `SFTTrainer` with a YAML configuration.

### Hardware Requirements & Memory Trade-offs
| Method | Hardware Requirement |
| :--- | :--- |
| **Full Fine-tuning** | ~16 x 80GB GPUs |
| **FSDP + LoRA** | ~8 x 80GB GPUs |
| **FSDP + Q-LoRA** | ~2 x 40GB GPUs |
| **FSDP + Q-LoRA + CPU Offload** | **4 x 24GB GPUs** (e.g., NVIDIA A10G) |

### Key Configuration (`llama_3_70b_fsdp_qlora.yaml`)
```yaml
model_id: "meta-llama/Meta-Llama-3-70b"
max_seq_len: 3072
learning_rate: 0.0002
num_train_epochs: 3
per_device_train_batch_size: 1
gradient_accumulation_steps: 2
bf16: true
# FSDP Settings
fsdp: "full_shard auto_wrap offload" # Use 'offload' for low VRAM
fsdp_config:
  backward_prefetch: "backward_pre"
  forward_prefetch: "false"
  use_orig_params: "false"
```

### Launching the Training
Use `torchrun` with specific environment variables to trigger memory-efficient loading:
```bash
ACCELERATE_USE_FSDP=1 FSDP_CPU_RAM_EFFICIENT_LOADING=1 \
torchrun --nproc_per_node=4 ./scripts/run_fsdp_qlora.py \
--config llama_3_70b_fsdp_qlora.yaml
```

## 4. Important Implementation Notes
*   **Chat Templates:** The guide uses a Vicuna-style template (`User:` / `Assistant:`) rather than the native Llama 3 special tokens. This is because the base Llama 3 special tokens are untrained; using them would require updating the embedding layer and `lm_head`, which significantly increases memory consumption.
*   **Cost Analysis:**
    *   **Low-cost:** 4x A10G GPUs (g5.12xlarge) cost ~$5.67/h. Total 3-epoch training: ~$255 (45 hours).
    *   **High-performance:** 4x H100 GPUs can finish the same task in ~1.25 hours for ~$25-$50.
*   **Merging Adapters:** Q-LoRA saves only the adapters. To use the model in production (e.g., with TGI), you must merge the weights. *Note: This requires ~192GB of CPU RAM.*

## 5. Inference and Testing
After training, load the model using `AutoPeftModelForCausalLM` to combine the base model with the new adapters.

```python
from peft import AutoPeftModelForCausalLM
from transformers import AutoTokenizer

# Load Model with PEFT adapter
model = AutoPeftModelForCausalLM.from_pretrained(
    "./llama-3-70b-hf-no-robot",
    torch_dtype=torch.float16,
    quantization_config={"load_in_4bit": True},
    device_map="auto"
)
```

**Result Example:**
*   **Query:** "How long was the Revolutionary War?"
*   **Generated Answer:** "The Revolutionary War... lasted from 1775 to 1783." (Accurate and concise).
