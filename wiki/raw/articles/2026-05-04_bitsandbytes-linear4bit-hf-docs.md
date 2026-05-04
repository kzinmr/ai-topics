# bitsandbytes — 4-bit Quantization Library (API Docs)

**Source:** https://huggingface.co/docs/bitsandbytes/en/reference/nn/linear4bit
**Date:** 2026-05-04

## Summary

HF docs for the `Linear4bit` module, which is the core building block for 4-bit quantization in bitsandbytes. Covers LinearFP4, LinearNF4, Params4bit, and the key observation that quantization happens *during device transfer* (`.to("cuda")`), not during weight loading.

## Key API Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `input_features` | int | required | Number of input features |
| `output_features` | int | required | Number of output features |
| `bias` | bool | True | Whether to use bias |
| `compute_dtype` | torch.dtype | None | Computation precision (bf16/fp16) |
| `compress_statistics` | bool | True | Compress quantization statistics |
| `quant_type` | str | 'fp4' | 'fp4' or 'nf4' |
| `quant_storage` | torch.dtype | uint8 | Storage type for quantized weights |

## Key Insight

Quantization is triggered on `.to("cuda")`, not during `load_state_dict()`. This means:
1. Load fp16/bf16 weights into Linear4bit module
2. Call `.to("cuda")` → quantization happens during device transfer

## Data Types

- **FP4 (LinearFP4)**: Standard 4-bit float (sign + exponent + mantissa)
- **NF4 (LinearNF4)**: NormalFloat 4 — equal-area bins under N(0,1), normalized to [-1, 1]. Better for normally distributed weights.
- **compute_dtype**: Usually bf16 for stable training
- **quant_storage**: uint8 (stores two 4-bit values per byte)
