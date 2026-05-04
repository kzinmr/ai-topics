---
title: "LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale"
source: timdettmers.com
author: Tim Dettmers
url: https://timdettmers.com/2022/08/17/llm-int8-and-emergent-features/
date: 2022-08-17
tags: [quantization, llm, inference, llm-int8, emergent-features]
---

# LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale

Tim Dettmers' foundational blog post explaining the LLM.int8() quantization method and the discovery of emergent features in large language models — features that only appear above ~6.7B parameters and require mixed-precision handling.

## Key Insights

- Standard quantization (absmax, zeropoint) fails at scale due to **emergent outlier features**
- Above 6.7B parameters, certain attention features have magnitudes 10-100× larger than others
- **Mixed-precision decomposition**: vector-wise quantization for most weights, 16-bit for outlier columns
- No degradation in model quality (perplexity) while reducing memory by 2×
- This work paved the way for QLoRA and other practical quantization methods

## Impact

This blog post is the canonical reference for understanding **why** quantization is non-trivial for large models. Cited as a 🟢 top-tier resource in the [[concepts/genai-handbook|GenAI Handbook]] (Section VI: Performance Optimization).
