---
title: "Model Quantization"
type: concept
created: 2026-04-25
updated: 2026-05-26
tags:
  - concept
  - quantization
  - inference
  - optimization
status: L1
sources:
  - https://timdettmers.com/2022/08/17/llm-int8-and-emergent-features/
  - https://www.maartengrootendorst.com/blog/quantization/
  - https://arxiv.org/abs/2208.07339
  - https://arxiv.org/abs/2310.11453
  - https://arxiv.org/abs/2402.17764
related:
  - "[[concepts/gguf-quantization]]"
  - "[[concepts/local-llm/model-quantization]]"
  - "[[concepts/fine-tuning/quantization-overview]]"
  - "[[concepts/ai-infrastructure-engineering/gpu-vram-fundamentals]]"
  - "[[concepts/inference/vllm]]"
  - "[[concepts/tensorrt-llm]]"
  - "[[concepts/emergent-features-llm]]"
  - "[[concepts/ai-infrastructure-engineering/_index]]"
  - "[[entities/tim-dettmers]]"
  - "[[entities/maarten-grootendorst]]"
---

# Model Quantization

> Model quantization is a technique that reduces memory usage and improves inference speed by representing neural network parameters at lower precision. It is an essential foundational technology for the practical deployment of LLMs.

## Why This Matters

Without quantization, running modern LLMs (70B to 500B parameters) on practical hardware would be impossible. For example, a 70B model at FP16 (2 bytes/parameter) requires 140GB of VRAM — it won't fit even on an H100 (80GB). At INT4 (0.5 bytes/parameter), this drops to 35GB, making it feasible even on a single consumer GPU (RTX 4090: 24GB).

## 1. Numerical Representation Fundamentals (IEEE-754)

Floating-point numbers consist of three components (IEEE-754 standard):

| Component | Role | Example: FP32 |
|-----------|------|---------------|
| **Sign** | Positive/negative | 1 bit |
| **Exponent** | Determines the **range** of values | 8 bits |
| **Fraction/Mantissa** | Determines the **precision** (distance between adjacent values) | 23 bits |

**Key Distinction:**
- **Dynamic Range** → Determined by Exponent (interval of representable values)
- **Precision** → Determined by Fraction (gap between two adjacent values)

### Common Data Types

| Type | Bits | Exponent | Fraction | Characteristics |
|------|------|----------|----------|-----------------|
| FP32 | 32 | 8 | 23 | Baseline precision, trainable |
| FP16 | 16 | 5 | 10 | Narrow range (±65K) |
| BF16 | 16 | 8 | 7 | **Same range** as FP32, lower precision |
| FP8 (E4M3) | 8 | 4 | 3 | ±448, **H100 Transformer Engine** |
| FP8 (E5M2) | 8 | 5 | 2 | ±57344, wider range than E4M3 |
| INT8 | 8 | — | — | Integer mapping with 256 values |
| NF4 | 4 | — | — | Optimized for normal-distributed weights (QLoRA) |

> BF16 is the "golden ratio" of Deep Learning: it maintains the same range as FP32 while halving memory usage.

## 2. Quantization Fundamentals

Quantization maps high-precision values (FP32) to lower-precision values (INT8/INT4, etc.).

### Memory Formula
```
Memory (GB) ≈ (Number of Parameters × Number of Bits) / 8
```

### Linear Mapping Methods

#### Symmetric Quantization (Absmax)
Maps values to a range symmetric around zero:
- **Scale:** $s = \frac{2^{b-1} - 1}{\alpha}$ (α = max absolute value)
- **Quantize:** $x_{quant} = \text{round}(s \cdot x)$
- **Dequantize:** $x_{dequant} = x_{quant} / s$
- Simple but inefficient for asymmetric distributions

#### Asymmetric Quantization (Zero-point)
Maps min/max to the full quantization range, not centered on zero:
- **Scale:** $s = \frac{\beta - \alpha}{2^{b} - 1}$
- **Zero-point:** $z = -\text{round}(s \cdot \alpha) - 2^{b-1}$
- More flexible, but requires zero-point calculation and storage

### Clipping & Calibration

**Clipping:** Artificially limits the dynamic range (e.g., [-5, 5]) to improve precision for the majority of values at the cost of truncating outliers.

**Calibration** (the process of selecting optimal ranges):

| Method | Mechanism | Characteristics |
|--------|-----------|-----------------|
| **MSE** (Mean Squared Error) | Minimizes difference between original and quantized values | Theoretically optimal, moderate compute cost |
| **Percentile** | Sets α/β by percentile | Simple, robust to outliers |
| **KL-divergence** | Maximizes distribution entropy | Most accurate but high cost |
| **Min/Max** | Uses full range as-is | A single outlier can tank precision |

### Accumulation Data Types
To prevent precision loss during computation, each data type has a corresponding **accumulation type**:

| Data Type | Accumulation Type | Reason |
|:----------|:------------------|:-------|
| float16 | float16 | Same type has sufficient range |
| bfloat16 | float32 | Exponent can overflow during accumulation |
| int16 | int32 | e.g., 127+127=254 > int8 range |
| int8 | int32 | Sum of two int8 max values exceeds int8 |

Example: A=127, B=127 (int8 max values), C = A + B = 254 exceeds int8 range (-128 to 127), requiring int32 accumulation.

### Granularity: Per-tensor vs Per-channel
Quantization granularity determines the trade-off between precision and memory:

| Granularity | (S, Z) pairs | Precision | Memory |
|:------------|:-------------|:----------|:-------|
| **Per-tensor** | 1 pair for entire tensor | Low (vulnerable to outliers) | Minimal |
| **Per-channel** | 1 pair per dimension (e.g., channel axis of 4D tensor) | High | Moderate |
| **Vector-wise (LLM.int8)** | 1 pair per row + per column | High (robust to outliers) | Higher |

Per-channel offers higher precision than per-tensor, but incurs more memory overhead due to the increased number of scale factors. LLM.int8() vector-wise quantization is a special case with independent scales for each row and each column.

## 3. Precision Formats Overview

| Format | Bits/Param | 70B Model | Quality | Inference Speed | Primary Use |
|--------|-----------|-----------|---------|-----------------|-------------|
| FP32 | 32 (4 bytes) | 280 GB | Baseline | Slow | Training only |
| FP16/BF16 | 16 (2 bytes) | 140 GB | Nearly lossless | Medium | Training/Inference |
| FP8 (E4M3/E5M2) | 8 (1 byte) | 70 GB | Negligible | Fast | H100/B200 inference |
| INT8 | 8 (1 byte) | 70 GB | Minimal | Fast | General inference |
| INT4 (GPTQ/AWQ) | 4 (0.5 bytes) | 35 GB | Small (1-2%) | Fastest | Local inference |
| NF4 (QLoRA) | 4 (0.5 bytes) | 35 GB | Small | Fastest | LoRA training |
| FP4 (MXFP4) | 4 (0.5 bytes) | 35 GB | Very small | Fastest | Next-gen hardware |
| 2-bit (TSM) | 2 (0.25 bytes) | 17.5 GB | Moderate | — | Research stage |
| **1.58-bit (BitNet)** | ~1.58 (0.2 bytes) | **~14 GB** | Moderate (research) | **Add only** | **Research stage** |

## 4. Main Quantization Methods

### Weight-only Quantization (Inference Only)

#### GPTQ (GPU-focused, Frantar et al. 2023)
- **Method:** Uses inverse Hessian matrix to quantify each weight's "importance"
- **Process:** Quantizes row by row → redistributes quantization error to **remaining unquantized weights**
  - "Passing the debt to neighbors" maintains overall model performance
- Optimized for GPU inference, high throughput with batch inference

#### AWQ (Activation-aware Weight Quantization, 2023)
- **Method:** Identifies important activation channels and protects their weights
- Higher accuracy than GPTQ on smaller models, faster quantization process than GPTQ

#### GGUF (llama.cpp, CPU/GPU Offloading)
- **Method:** Block-wise quantization ("super blocks" + "sub blocks" each with their own scale factor)
- Can offload specific layers to CPU when VRAM is insufficient
- Q2_K to Q8_0 multi-level quality selection

#### RTN (Round-To-Nearest)
- Simplest rounding method. Largest precision degradation.
- Used for baseline comparison

### Weight+Activation Quantization

| Method | Mechanism | Characteristics |
|--------|-----------|-----------------|
| **FP8 Inference** | H100 Transformer Engine + FP8 GEMM | Native hardware support |
| **INT8 SmoothQuant** | Smooths activation outliers | Mitigates outlier problem |
| **KV Cache INT8/FP8** | Reduces KV Cache memory for long contexts | Robust due to sparse attention distribution |

## 5. LLM.int8() and the Outlier Problem (Dettmers, 2022)

### The Challenge
Standard Int8 quantization breaks down for **models with 6.7B+ parameters**. The reason: "emergent outlier features."

### How Quantization Normally Works
1. Find the maximum absolute value in a vector
2. Normalize by that value
3. Scale to the target type's range
4. Round

**Outlier Problem:** In models >6.7B, certain hidden dimensions develop extremely large values (-60 to -95), causing 99.9% of small values (-0.1 to 0.5) to be quantized together and lose information.

### LLM.int8() Solution
Achieves zero degradation through two simultaneous techniques:

#### 1. Vector-wise Quantization
Instead of a single scale constant for the entire tensor, uses **independent scale constants for each row and each column** of the matrix product.

#### 2. Mixed Precision Decomposition
Exploits the fact that outliers are **systematically concentrated in only a few dimensions**:
1. **Separate**: Extract dimensions containing outliers → compute matrix product at high precision (FP16)
2. **Quantize**: Process the remaining 99.9% of values with Int8
3. **Combine**: Merge both outputs to restore full performance

```
Input Hidden States
├── Outlier Dimensions (FP16 matmul) → Few dimensions
└── Normal Dimensions (INT8 matmul)  → 99.9% of values
        ↓
Combined Output (zero degradation)
```

### The 6.7B Phase Shift

Dettmers' definition: *"A phenomenon where a gradual change in one characteristic suddenly causes a phase shift that changes the nature of the substrate."*

| Characteristic | Below 6.7B | Above 6.7B |
|:---------------|:-----------|:-----------|
| **Outlier coordination** | Stochastic/inconsistent | **100% of layers use the same dimensions** |
| **Outlier magnitude** | Small (~15) | Large (60-95+) |
| **Sequences affected** | Some | **75% of sequences affected** |
| **Attention** | Distributed | Highly sparse/discrete |
| **FFN pruning tolerance** | ~30% removable | **<5%** |
| **Quantization** | Standard Int8 works | Mixed precision (LLM.int8) required |

### Two Streams Theory
Dettmers theorizes that outliers manage two processing streams:
1. **Input Explanation** — Learning features that explain the data
2. **Feature Removal** — Using outlier dimensions to "mute" noise or context-irrelevant features

> By maintaining large values (-60 to -95) in specific dimensions, they can be multiplied by small weights to effectively zero out other features after non-linear functions (Softmax/ReLU).

### Research Implications
- **Research on <6.7B models does not generalize to >6.7B models**
- Emergence follows perplexity, not parameter count, exponentially
- The perplexity curve of small models (125M-1.3B) can predict behavior of 175B+ models

> "There are two types of transformers and you should not generalize from one to the other." — Tim Dettmers

## 6. Post-Training Quantization (PTQ)

Quantization performed after training is complete.

### Weights vs Activations

| | Weights | Activations |
|--|---------|-------------|
| **Nature** | Static, known | Varies with input |
| **Quantization** | Easy (stable distribution) | Difficult (dynamic distribution) |
| **Calibration** | Not required | Requires calibration dataset |

#### Dynamic Quantization
- Computes scale factors for each layer at inference time
- Higher accuracy but **slower** (significant overhead)

#### Static Quantization
- Pre-computes scale factors using a calibration dataset
- **Faster** but requires a dataset representative of training data distribution

### GPTQ (GPU-focused)
- Uses inverse Hessian matrix to quantify weight "importance"
- Quantizes row by row, redistributes error to unquantized weights
- High batch throughput, optimized for GPU inference

### GGUF (CPU/GPU Offloading)
- Block-wise quantization (super blocks + sub blocks)
- Supports CPU offloading, flexible for VRAM-constrained environments

## 7. Quantization-Aware Training (QAT)

A technique that integrates quantization into the training process.

### How It Works
**"Fake Quants"** — During forward pass, quantizes to lower bits then immediately restores to FP32. Backward pass stays at FP32 (using STE — Straight-Through Estimator — since quantization is non-differentiable).

### Wide Minima Theory
- **PTQ**: May have low loss at FP32 but high loss at low precision (INT4)
- **QAT**: Finds **"wide minima"** in the low-precision loss landscape
  - Wide minima = robust to quantization error

> QAT is like training with weighted clothes — when you remove them (quantize), you still perform well because you trained under those constraints.

### QAT vs PTQ

| Criterion | PTQ | QAT |
|-----------|-----|-----|
| **Cost** | Minutes to hours (calibration only) | 2-3x increase over training time |
| **INT4 accuracy** | Good | **Superior** (especially small models) |
| **BI4 accuracy** | Not possible | Required |
| **Training data** | Hundreds of samples | Full training set |

## 8. The Frontier: 1-bit and 1.58-bit LLMs

### BitNet (1-bit, Wang et al. 2023)
Replaces standard Linear layers with **BitLinear**:
- **Weights:** Quantized to {-1, +1} using `Signum` function
- **Activations:** Matrix product computed at INT8
- **Scaling:** Restored using mean absolute weight value (β) + max absolute activation value (α)

### BitNet b1.58 (Ternary Weights, 2024)
Adds **0** to the weights → **{-1, 0, +1}**:
- **Feature Filtering:** Weights=0 can ignore specific features
- **Computational revolution:** Matrix products **only use addition and subtraction** (no multiplication)
- **Quantization method:** `absmean` quantization (ternarizes based on mean absolute value)

```
Traditional FP16 matmul: y = w₁x₁ + w₂x₂ + ... + wₙxₙ  (multiply + add)
BitNet b1.58 matmul:     y = ±x₁ ± x₂ ... ± xₙ           (add/subtract only)
```

### Potential Impact
- Could reduce inference **power consumption by 90%+**
- With dedicated hardware, high-speed inference on CPU becomes feasible
- Brings LLMs to small devices (mobile, IoT)

### Current Limitations
- Currently at research stage (limited large-scale validation)
- Quality gap compared to equivalent FP4/INT4 models
- Training instability (especially at 50B+ scale)

## 9. Practical Tradeoff Analysis

### Accuracy vs Memory Tradeoff (LLaMA-3 70B, MMLU benchmark)
```
Format         | MMLU | VRAM
FP16           | 82.0% | 140 GB
FP8            | 81.8% | 70 GB
INT8           | 81.7% | 70 GB
INT4 AWQ       | 81.2% | 35 GB
NF4            | 80.9% | 35 GB
```
(Approximate values, vary by actual model and evaluation method)

### When to Use What

| Requirement | Recommended Method |
|-------------|-------------------|
| Highest quality | FP16/BF16 (sufficient VRAM) |
| Production server efficiency | FP8 (H100/B200) |
| Cost-conscious server | INT8 + KV Cache INT8 |
| Local inference (24GB GPU) | INT4 AWQ / GGUF Q4_K_M |
| VRAM extreme (with CPU) | GGUF + CPU Offloading |
| Post-training quantization | GPTQ (GPU) / GGUF (general) |
| Best quantization accuracy | QAT (though costly) |
| Long context (128K+) | FP16/INT8 + KV Cache FP8 |

### PTQ Method Selection

| Environment | Recommended Method | Reason |
|-------------|-------------------|--------|
| GPU only (sufficient VRAM) | GPTQ / AWQ | High throughput, batch inference |
| VRAM constrained (CPU assist) | GGUF | Block-wise quantization + offloading |
| No GPU (CPU/Apple Silicon) | GGUF Q4_K_M or higher | llama.cpp optimized |

## 10. KV Cache Quantization

- vLLM TurboQuant: 2-bit KV Cache → 4x capacity, < 1% quality loss
- KV Cache is more tolerant to quantization than weights (attention distribution is sparse)
- FP8 KV Cache: Nearly lossless, 2x KV Cache capacity

## 11. Energy Efficiency & Practical Workflow

### Energy Efficiency: Counterintuitive Findings
Quantization does not always save energy. Optimum's empirical data:

| Condition | Energy Variation | Cause |
|:----------|:-----------------|:------|
| Large models (>=5B) + NF4 | **Memory savings + efficiency maintained** | Quantization gains outweigh overhead |
| Small models (<3B) + NF4 | **25-56% increase** | Dequantization overhead dominates |
| Mixed INT8 (threshold=6.0) vs FP16 | **17-33% increase** | Mixed precision branching cost |
| Batch size 1→64 | **96% reduction** (across all quantization methods) | Improved memory bandwidth utilization |

**Practical implication:** For small models, batch size optimization is more effective than NF4 quantization. The primary option for energy reduction should be "batch processing optimization," followed by quantization format selection.

### Practical Implementation Workflow (Optimum)
HF Optimum's recommended 6-step implementation flow:

1. **Identify operators**: Identify compute-intensive operations (Linear projections, MatMul)
2. **Try Dynamic Quantization**: Runtime range computation. Easy to set up, done if accuracy is sufficient
3. **Try Static Quantization**: Apply Observers to model. Requires calibration data
4. **Calibration**: Choose method, determine range with representative data (~200 samples)
5. **Conversion**: Replace float32 operators with int8 versions
6. **Evaluate**: If accuracy insufficient, move to QAT (Quantization Aware Training)

```python
# Tools available in Optimum
from optimum.onnxruntime import ORTQuantizer  # ONNX models
from optimum.intel import (                   # Intel HW optimization
    IntelQuantizer, IntelModelForQuantization
)
from optimum.gptq import GPTQQuantizer         # GPTQ quantization for LLMs
from optimum.fx import FxQuantizer             # PyTorch graph-mode quantization
```

## Related Pages

- [[concepts/bitsandbytes]] — bitsandbytes: NF4/FP4 quantization library, QLoRA backend
- [[concepts/gguf-quantization]] — GGUF format deep-dive
- [[concepts/local-llm/model-quantization]] — Local LLM quantization specifics
- [[concepts/fine-tuning/quantization-overview]] — Fine-tuning quantization
- [[concepts/ai-infrastructure-engineering/gpu-vram-fundamentals]] — VRAM requirements by quantization
- [[concepts/inference/vllm]]#TurboQuant — vLLM 2-bit KV cache
- [[concepts/tensorrt-llm]] — NVIDIA FP8/FP4 inference
- [[concepts/ai-infrastructure-engineering/_index]] — Parent page
- [[entities/tim-dettmers]] — bitsandbytes, LLM.int8(), QLoRA
- [[entities/maarten-grootendorst]] — Visual quantization guide

## Skills Reference

- `gguf-quantization` — GGUF format & quantization workflow
- `llama-cpp` — Local inference with quantized models

## Sources

- [LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale (Dettmers et al., 2022)](https://arxiv.org/abs/2208.07339)
- [A Visual Guide to Quantization (Grootendorst, 2024)](https://www.maartengrootendorst.com/blog/quantization/)
- [QLoRA: Efficient Finetuning of Quantized LLMs (Dettmers et al., 2023)](https://arxiv.org/abs/2305.14314)
- [BitNet: Scaling 1-bit Transformers for Large Language Models (Wang et al., 2023)](https://arxiv.org/abs/2310.11453)
- [The Era of 1-bit LLMs: All Large Language Models are in 1.58 Bits (Ma et al., 2024)](https://arxiv.org/abs/2402.17764)
- [GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers (Frantar et al., 2023)](https://arxiv.org/abs/2210.17323)
- [AWQ: Activation-aware Weight Quantization for LLM (Lin et al., 2023)](https://arxiv.org/abs/2306.00978)
- [HF Optimum Quantization Concept Guide](https://huggingface.co/docs/optimum/concept_guides/quantization)

## TODO

- [x] Add LLM.int8() and emergent features section (Dettmers)
- [x] Add IEEE-754 representation fundamentals
- [x] Add symmetric/asymmetric quantization mapping
- [x] Add calibration deep-dive (MSE, KL, Percentile)
- [x] Add BitNet / 1.58-bit frontier section
- [x] Update sources with Dettmers and BitNet papers
- [x] Add accumulation types & granularity (per-tensor vs per-channel)
- [x] Add energy efficiency counterintuitive findings (Optimum)
- [ ] Add per-method benchmark comparisons (GPTQ vs AWQ vs GGUF vs vanilla)
- [ ] Add calibration dataset requirements for GPTQ/AWQ
- [ ] Add hardware-specific quantization guide per GPU generation
- [ ] Add FP4 (MXFP4) architecture details
