---
title: ZAYA1-VL-8B
type: concept
category: model
tags:
  - vlm
  - model
  - open-source
  - multimodal
  - amd
  - zyphra
aliases: [ZAYA1-VL]
sources:
  - https://www.zyphra.com/post/zaya1-vl-8b
  - https://huggingface.co/Zyphra/ZAYA1-VL-8B
  - https://www.zyphra.com/zaya1-vl-8b-technical-report
related:
  - entities/zyphra
  - concepts/zaya1-8b
  - concepts/zaya1-74b-preview
  - concepts/mixture-of-experts
  - concepts/vision-language-models
created: 2026-05-09
updated: 2026-05-09
---

# ZAYA1-VL-8B

**ZAYA1-VL-8B** is Zyphra's first vision-language model (VLM), released May 2026 under Apache 2.0 license. It's a Mixture of Experts (MoE) model with **700M active and 8B total parameters**, built atop the [[concepts/zaya1-8b|ZAYA1-8B]] base LLM. Despite being trained on only ~140B vision-language tokens (far fewer than competing models trained on trillions), it achieves state-of-the-art performance for its size class.

## Key Innovations

### 1. Vision-Specific LoRA Parameters
Specialized LoRA parameters on MLPs and CCA (Cross-Correlation Attention) weights, activated **only on vision tokens**. This gives the model dedicated capacity for visual processing without affecting language capabilities. Trained alongside main parameters.

### 2. Bidirectional Attention for Image Tokens
Unlike standard VLMs that force causal (left-to-right) attention on all tokens, ZAYA1-VL-8B processes image tokens with **bidirectional attention**. Images have no natural causal order — this improves performance by removing an arbitrary ordering constraint.

## Architecture

- **Base LLM**: ZAYA1-8B (MoE, 700M active / 8B total)
- **Vision Encoder**: Qwen2.5-VL ViT
- **Training Data**: Open data only (~140B vision-language tokens)
- **Training Hardware**: AMD GPUs (end-to-end)

## Performance Highlights

Strongest in:
- **Document understanding & OCR** (DocVQA: 92.5, AI2D: 87.5)
- **Spatial perception & grounding** (RefCOCO avg: 84.3, Point-Bench avg: 58.0)
- **GUI and computer use tasks**

Outperforms comparable models (MolmoE 1.2B/8B, Qwen3.5-2B, Molmo2-4B) on multiple benchmarks while having fewer active parameters.

## Usage

```python
from transformers import Zaya1VLForConditionalGeneration, Zaya1VLProcessor

# Requires Zyphra's transformers fork
# pip install "transformers @ git+https://github.com/Zyphra/transformers.git@zaya1-vl"
processor = Zaya1VLProcessor.from_pretrained("Zyphra/ZAYA1-VL-8B")
model = Zaya1VLForConditionalGeneration.from_pretrained("Zyphra/ZAYA1-VL-8B")
```

## Significance

ZAYA1-VL-8B demonstrates that compact MoE vision-language models can compete with much larger dense models when architectural innovations (vision-specific parameters, bidirectional image attention) are applied. The model also validates AMD as a viable training platform for frontier VLMs.

## See Also

- [[entities/zyphra]] — Company behind ZAYA1
- [[concepts/zaya1-74b-preview]] — Larger ZAYA1 reasoning model
- [[concepts/mixture-of-experts]] — MoE architecture
- [[concepts/vision-language-models]] — VLM landscape
