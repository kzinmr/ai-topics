# Optimum Quantization Concept Guide — HF Docs

**Source:** https://huggingface.co/docs/optimum/concept_guides/quantization
**Date:** 2026-05-04

## Unique Content

### Accumulation Data Types
| Data Type | Accumulation Type |
|:----------|:-----------------|
| float16 | float16 |
| bfloat16 | float32 |
| int16 | int32 |
| int8 | int32 |

### Energy Efficiency (Counterintuitive)
- **Large models (>=5B):** NF4 saves memory + maintains energy efficiency
- **Small models (<3B):** NF4 can INCREASE energy consumption 25-56% (dequantization overhead)
- **Mixed-precision INT8 (llm_int8_threshold=6.0):** +17-33% energy overhead vs FP16
- **Batching (1→64):** Reduces per-token energy by up to 96% — often more impactful than precision choice

### Affine Quantization Formula
x = S * (x_q - Z)
- S (Scale): positive float32
- Z (Zero-point): int8 value corresponding to float32 0

### Granularity: Per-tensor vs Per-channel
- Per-tensor: one (S, Z) pair for entire tensor
- Per-channel: one (S, Z) pair per element along a dimension

### Practical 6-Step Workflow
1. Identify operators (Linear, MatMul)
2. Try Dynamic Quantization
3. Try Static Quantization + Observers
4. Calibrate (choose technique, run representative data)
5. Convert (float32 → int8 operators)
6. Evaluate → If insufficient, move to QAT

### Optimum Tools
- optimum.onnxruntime — ONNX models
- optimum.intel — Intel hardware
- optimum.fx — PyTorch graph-mode quantization
- optimum.gptq — LLM quantization with GPTQ
