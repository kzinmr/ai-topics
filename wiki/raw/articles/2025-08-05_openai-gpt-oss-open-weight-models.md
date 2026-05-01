# Introducing gpt-oss — OpenAI's First Open-Weight Model

**Source:** https://openai.com/index/introducing-gpt-oss/
**Date:** August 5, 2025
**Models:** gpt-oss-120b, gpt-oss-20b
**License:** Apache 2.0 (Open-weight)

## Model Specifications

| Model | Total Params | Active/Token | Layers | Experts (Total/Active) | Context |
|---|---|---|---|---|---|
| gpt-oss-120b | 117B | 5.1B | 36 | 128/4 | 128k |
| gpt-oss-20b | 21B | 3.6B | 24 | 32/4 | 128k |

## Architecture
- Mixture-of-Experts (MoE) design
- Attention: Alternating dense and locally banded sparse patterns; GQA with group size 8
- Positional Encoding: Rotary Positional Embedding (RoPE)
- Tokenizer: o200k_harmony (open-sourced alongside models)
- Quantization: Native MXFP4 — 120B runs on single 80GB GPU, 20B on 16GB

## Performance
- gpt-oss-120b: Near-parity with o4-mini on reasoning; outperforms o1 and GPT-4o on HealthBench
- gpt-oss-20b: Matches/exceeds o3-mini; optimized for edge devices
- Adjustable reasoning effort: low, medium, high
- Chain-of-thought fully visible to developers (not end-users)

## Safety
- Preparedness Framework evaluation
- Adversarial fine-tuning tests: models could not reach high-risk capability levels
- $500,000 Kaggle red teaming prize for community safety testing
- CoT monitoring recommended — may contain hallucinations or violations

## Availability
- Hugging Face, Azure, AWS, vLLM, Ollama, llama.cpp, Databricks
- Hardware: NVIDIA, AMD, Cerebras, Groq, Apple Metal
- Windows: ONNX Runtime GPU-optimized versions
- Harmony Renderer (Python/Rust), Open Model Playground

## Key Quote
> "Broad access to these capable open-weights models created in the US helps expand democratic AI rails."
