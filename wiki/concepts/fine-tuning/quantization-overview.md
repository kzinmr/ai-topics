---
title: "Model Quantization"
type: concept
created: 2026-04-19
updated: 2026-04-19
tags: [fine-tuning, quantization, inference, gguf, gptq, fp8]
related:
  - concepts/fine-tuning/_index
  - concepts/fine-tuning/peft-lora-qlora
  - concepts/inference/llama-cpp
sources: []
---

# Model Quantization

Quantization reduces model precision (FP32 → FP16 → INT8 → INT4) to decrease memory requirements and improve inference speed with minimal accuracy loss.

## Quantization Formats

| Format | Precision | Memory vs FP32 | Use Case |
|--------|-----------|----------------|----------|
| **FP32** | 32-bit float | 1x | Training, maximum accuracy |
| **FP16/BF16** | 16-bit float | 2x smaller | Training, inference on modern GPUs |
| **FP8** | 8-bit float | 4x smaller | Inference on H100/Ada GPUs |
| **INT8** | 8-bit integer | 4x smaller | CPU inference, edge devices |
| **INT4/GGUF** | 4-bit integer | 8x smaller | Consumer hardware, local LLM |
| **GPTQ** | 4-bit (per-channel) | 8x smaller | GPU inference with accuracy |
| **AWQ** | 4-bit (activation-aware) | 8x smaller | Better accuracy than GPTQ |
| **NF4** | 4-bit (normal float) | 8x smaller | QLoRA fine-tuning |

## QLoRA Quantization

QLoRA enables fine-tuning 65B models on a single 48GB GPU:

```python
from transformers import BitsAndBytesConfig

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_use_double_quant=True,
)
```

**Trade-off:** ~1-2% accuracy loss vs full precision, but 4× memory reduction.

## GGUF (llama.cpp format)

GGUF is the standard format for CPU/Apple Silicon inference:

```bash
# Convert HF model to GGUF
python convert-hf-to-gguf.py --outfile model.gguf

# Quantize to 4-bit
./llama-quantize model.gguf model-Q4_K_M.gguf Q4_K_M
```

## Quantization Methods

| Method | Description | Best For |
|--------|-------------|----------|
| **PTQ (Post-Training Quantization)** | Quantize after training | Quick deployment, no retraining |
| **QAT (Quantization-Aware Training)** | Train with quantization in loop | Maximum accuracy after quantization |
| **GPTQ** | Per-channel 4-bit quantization | GPU inference |
| **AWQ** | Activation-aware quantization | Better accuracy on small models |
| **SmoothQuant** | Smooth activation outliers | INT8 inference |

## Axolotl Compressed Saving

```yaml
save_compressed: true
```

Reduces disk space by ~40% while maintaining vLLM and llmcompressor compatibility.

## Related

- [[fine-tuning/peft-lora-qlora]] — QLoRA fine-tuning
- [[inference/llama-cpp]] — GGUF inference engine
- [[inference/vllm]] — vLLM serving with quantized models

## Sources

- [GGUF Format Specification](https://github.com/ggerganov/ggml/blob/master/docs/gguf.md)
- [GPTQ Paper](https://arxiv.org/abs/2210.17323)
- [AWQ Paper](https://arxiv.org/abs/2306.00978)
- [QLoRA Paper (Dettmers et al., 2023)](https://arxiv.org/abs/2305.14314)
