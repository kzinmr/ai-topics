# DFlash: Block Diffusion for Flash Speculative Decoding
Source: arXiv
URL: https://arxiv.org/abs/2602.06036
Date: 2026-02-05

## Problem
Autoregressive LLMs decode token-by-token, causing high inference latency and poor GPU utilization. Current speculative decoding relies on sequential autoregressive drafting, limiting speedup gains.

## Innovation
DFlash replaces autoregressive drafting with a lightweight **block diffusion model** for parallel token generation:
- **Single forward pass** drafting — eliminates sequential drafting overhead
- **Context-aware conditioning** using features extracted from the target LLM
- **Seamless integration** with existing speculative decoding verification pipelines

## Performance
- **>6x lossless speedup** across diverse models and tasks
- **Up to 2.5x higher speedup** than SOTA speculative decoding (EAGLE-3)
- Maintains lossless generation quality while drastically reducing latency

## Supported Models
Qwen3.5-122B-A10B, Qwen3.6-35B-A3B, Kimi-K2.5, gpt-oss-120b, LLaMA-3.1-8B-Instruct, and more. DFlash draft models available on HuggingFace.

## Integration
- vLLM: `--speculative-config '{"method": "dflash", "model": "..."}'`
- SGLang: `--speculative-algorithm DFLASH`
- Transformers: Qwen3 and LLaMA-3.1 support

## Authors
Jian Chen, Yesheng Liang, Zhijian (z-lab)

## GitHub
https://github.com/z-lab/dflash (2.3k stars)

## HuggingFace
https://huggingface.co/collections/z-lab/dflash
