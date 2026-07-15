---
title: "Unsloth + Thinking Machines: 1-bit GGUF quants for Inkling"
type: raw_article
date: 2026-07-15
source_handle: danielhanchen
source_url: https://x.com/danielhanchen/status/2077468775478423601
external_urls:
  - https://huggingface.co/unsloth/inkling-GGUF
tags:
  - model
  - quantization
  - open-source
  - inference
  - multimodal
  - unsloth
---

# Unsloth + Thinking Machines: 1-bit GGUF quants for Inkling

Daniel Han (@danielhanchen) announced a collaboration between Unsloth and Thinking Machines to bring dynamic Unsloth 1-bit GGUF quants for the Inkling model.

## Key Points

- **86% smaller**: Inkling quantized from 1.9TB down to 270GB
- **74.2% top-1% accuracy retention**: High quality preserved despite aggressive quantization
- **Vision and audio support**: Multimodal capabilities maintained in the quantized version
- **GGUF format**: Available at huggingface.co/unsloth/inkling-GGUF

## Impact

This enables running the Inkling model on consumer hardware that would otherwise require enterprise-grade infrastructure (~2TB VRAM for the full model). The 1-bit quantization approach pioneered by Unsloth makes frontier multimodal models accessible to individual developers and researchers.
