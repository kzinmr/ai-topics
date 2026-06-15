---
title: "bitsandbytes"
type: concept
created: 2026-05-04
updated: 2026-05-04
tags:
  - concept
  - quantization
  - inference
  - fine-tuning
status: L2
sources:
  - https://huggingface.co/docs/bitsandbytes/en/reference/nn/linear4bit
  - https://huggingface.co/blog/4bit-transformers-bitsandbytes
  - https://arxiv.org/abs/2305.14314
  - https://github.com/bitsandbytes-foundation/bitsandbytes
related:
  - "[[concepts/model-quantization]]"
  - "[[concepts/qlora]]"
  - "[[concepts/post-training/fsdp-qlora]]"
  - "[[entities/tim-dettmers]]"
  - "[[concepts/post-training/peft-lora-qlora]]"
  - "[[concepts/llm-int8]]"
  - "[[entities/artidoro-pagnoni]]"
---

# bitsandbytes

> The de facto standard 4-bit / 8-bit quantization library. As the backend for LLM quantization in the Hugging Face Transformers ecosystem, it enables 4-bit fine-tuning via QLoRA. Developed by Tim Dettmers, now maintained by **bitsandbytes-foundation**.

## Why This Matters

Without bitsandbytes, fine-tuning 70B-class LLMs on consumer GPUs (24GB-48GB VRAM) is practically impossible. The combination of NF4 quantization + double quantization + paged optimizer enables 65B models to be trained on a single 48GB GPU (Guanaco model, achieving 99.3% of ChatGPT performance).

## Architecture

### Core Modules

#### `Linear4bit` — Base Class
The base for 4-bit quantized linear layers. Quantization is triggered **at device transfer time** (`.to("cuda")`). This design is important: weights are not quantized upon loading — they are converted to 4-bit only when copied to the GPU.

```python
import torch
import bitsandbytes as bnb
from bnb.nn import Linear4bit

layer = Linear4bit(4096, 4096)
layer.load_state_dict(torch.load("weights.pt"))
layer = layer.to("cuda")  # ← Quantization happens here
```

| Parameter | Type | Default | Description |
|-----------|-----|-----------|------|
| `input_features` | int | Required | Input dimension |
| `output_features` | int | Required | Output dimension |
| `bias` | bool | True | Whether to use bias |
| `compute_dtype` | torch.dtype | None | Computation precision (bf16 recommended) |
| `compress_statistics` | bool | True | Compress quantization statistics |
| `quant_type` | str | 'fp4' | 'fp4' or 'nf4' |
| `quant_storage` | torch.dtype | uint8 | Storage format for 4-bit weights (packed 2 values/byte) |

#### `LinearFP4` / `LinearNF4`
Subclasses of `Linear4bit`. Specialized layers with fixed `quant_type`:
- **LinearFP4**: Standard 4-bit floating point
- **LinearNF4**: NormalFloat 4 — optimized for normally distributed weights

#### `Params4bit`
A special parameter class for holding 4-bit weights. Internally packs two 4-bit values into `quant_storage` (uint8). On-the-fly decompression to the precision specified by `compute_dtype`.

### NF4 (NormalFloat 4) — Details

NF4 is a **4-bit data type optimized for normally distributed weights**, introduced in the QLoRA paper.

#### Design Principle
Utilizes the cumulative distribution function (CDF) of the standard normal distribution N(0, 1):
1. Divide N(0, 1) into 16 equal-area bins
2. Each bin's CDF value corresponds to a quantization level
3. Map to the normalized range [-1, 1]

```
Implementation: create_normal_map() function
α = 929/960 ≈ 0.9677083  # Coefficient to clip the tails of the normal distribution
```

#### Why It Outperforms FP4
- **FP4**: Fixed exponent/mantissa bit allocation. Uniform spacing regardless of value distribution.
- **NF4**: High precision in dense regions (near the mean), lower precision in sparse regions (tails)
  - LLM weights follow a normal distribution → most weights cluster near the mean
  - NF4 allocates "resolution" to match this distribution

Not perfectly symmetrical — cannot represent 0 exactly (due to asymmetric tails). Per John D. Cook's analysis: `α = 929/960` is an empirical value approximating the best distribution of 2^4=16 values.

### Double Quantization
bitsandbytes applies another stage of quantization to the quantization constants themselves:
- First quantization: FP16 weights → NF4 (block-wise, block size 64)
- Second quantization: FP32 quantization constants → FP8 (block-wise, block size 256)
- Savings: approximately **0.4 bits** additional reduction per parameter

## Integration with Hugging Face

### Transformers Integration
Configured via `BitsAndBytesConfig`:

```python
from transformers import BitsAndBytesConfig
import torch

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",        # NF4 vs FP4
    bnb_4bit_use_double_quant=True,   # Double quantization
    bnb_4bit_compute_dtype=torch.bfloat16,
)

model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-2-70b-hf",
    quantization_config=bnb_config,
    device_map="auto",
)
```

### PEFT + TRL Integration (QLoRA Fine-Tuning)
4-bit quantized models cannot be trained directly → add PEFT LoRA adapters:

```python
from peft import LoraConfig, get_peft_model
from trl import SFTTrainer

peft_config = LoraConfig(
    r=16, lora_alpha=32,
    target_modules=["q_proj", "v_proj"],
    bias="none", task_type="CAUSAL_LM",
)

trainer = SFTTrainer(
    model=model,      # 4-bit quantized base
    peft_config=peft_config,
    ...
)
```

## Ecosystem Position

```
Hugging Face Transformers
  └── BitsAndBytesConfig (Config)
       └── bitsandbytes (CUDA Kernels)
            ├── Linear4bit → NF4/FP4 Quantization
            ├── LLM.int8() → 8-bit Mixed Precision
            └── Params4bit → 4-bit Parameter Management
                 └── PEFT/TRL (LoRA Training)
```

- **Differences from competitors**: GPTQ/AWQ are post-training quantization (PTQ) specialized for inference; bitsandbytes enables training-time quantization (QAT-like) for QLoRA training
- **vLLM / SGLang**: Inference on bitsandbytes-quantized models is possible via HF Transformers, but vLLM uses its own GPTQ/AWQ kernels

## Hardware & Constraints

| Requirement | Details |
|------|------|
| **GPU** | NVIDIA CUDA 11.2+, Compute Capability 7.0+ |
| **CPU** | Not supported (CUDA only) |
| **Supported Models** | All models compatible with Accelerate loading |
| **Training Method** | Pure 4-bit training not possible → PEFT (LoRA) adapters required |
| **Storage** | 2 values packed per uint8 (memory savings with slight decompression overhead) |

## Performance

Benchmark on T4 16GB GPU:

| Model | FP16 Size | Method | Result |
|-------|-----------|------|------|
| Llama-7B | 14GB | 4-bit NF4 + bf16 | **No OOM** |
| Llama-13B | 27GB | 4-bit NF4 + fp16 + GC + DQ | **No OOM** (seq=1024) |
| Llama-13B | 27GB | 8-bit + GC | OOM |

## Key Takeaways

- **At Training Time**: QLoRA + bitsandbytes is the only practical 4-bit training path
- **At Inference**: GPTQ/AWQ/GGUF are faster (optimized dedicated kernels)
- **NF4 vs FP4**: NF4 is always more accurate for normally distributed weights
- **quant_storage=uint8**: Memory savings from packing 2 values; decompressed to bf16 at compute time
- **bitsandbytes is CUDA Only**: Use GGUF for CPU/Apple Silicon

## Related Pages

- [[concepts/model-quantization]] — Comprehensive quantization guide
- [[concepts/qlora]] — QLoRA fine-tuning (bitsandbytes-based)
- [[concepts/post-training/fsdp-qlora]] — FSDP + QLoRA distributed training
- [[concepts/llm-int8]] — LLM.int8() 8-bit inference
- [[entities/tim-dettmers]] — bitsandbytes creator
- [[concepts/post-training/peft-lora-qlora]] — PEFT integration
- [[concepts/gguf-quantization]] — CPU/Apple Silicon alternative

## Sources

- [bitsandbytes Linear4bit API Docs](https://huggingface.co/docs/bitsandbytes/en/reference/nn/linear4bit)
- [Making LLMs even more accessible with bitsandbytes (HF Blog, 2023)](https://huggingface.co/blog/4bit-transformers-bitsandbytes)
- [QLoRA: Efficient Finetuning of Quantized LLMs (Dettmers et al., 2023)](https://arxiv.org/abs/2305.14314)
- [bitsandbytes GitHub Repository](https://github.com/bitsandbytes-foundation/bitsandbytes)
- [Gaussian distributed weights for LLMs: NF4 and QLoRA (John D. Cook, 2026)](https://www.johndcook.com/blog/2026/04/18/qlora/)
