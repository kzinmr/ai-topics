---
title: "Inkling (Thinking Machines)"
type: concept
aliases:
  - inkling
  - Thinking Machines Inkling
created: 2026-07-15
updated: 2026-07-15
tags:
  - model
  - multimodal
  - open-source
  - quantization
  - reasoning
sources:
  - raw/articles/2026-07-15_danielhanchen_inkling-1bit-gguf-quants.md
  - raw/articles/2026-07-15_danielhanchen_inkling-unsloth-studio.md
---

# Inkling

**Inkling** is a multimodal AI model developed by [[entities/thinking-machines-lab|Thinking Machines Lab]]. It supports vision, audio, and tool calling natively, and uses a numerical reasoning level system (0.0 to 0.99) for controlling inference depth.

## Overview

Inkling is Thinking Machines Lab's flagship multimodal model, designed for native interaction across modalities. Unlike bolt-on multimodal scaffolding, Inkling handles vision, audio, and text natively as part of its architecture.

## Key Features

- **Native multimodal**: Vision, audio, and text processed in a unified architecture
- **Numerical reasoning levels**: Controllable reasoning depth from 0.0 (fast) to 0.99 (deep)
- **Interleaved tool calling**: Use tools mid-generation without breaking context
- **Web search + code execution**: Built-in capabilities

## Quantization

In July 2026, [[entities/daniel-han|Unsloth]] collaborated with Thinking Machines to produce 1-bit GGUF quants of Inkling:

- **86% smaller**: 270GB vs 1.9TB for the full model
- **74.2% top-1% accuracy retention**: High quality despite aggressive quantization
- **Vision and audio support preserved** in the quantized version
- Available at: [huggingface.co/unsloth/inkling-GGUF](https://huggingface.co/unsloth/inkling-GGUF)

This enables running Inkling on consumer hardware that would otherwise require ~2TB VRAM.

## Integration

- **Unsloth Studio**: Full local integration with tool calling, web search, code execution, vision, and audio support since July 2026
- Documentation: [unsloth.ai/docs/models/inkling](https://unsloth.ai/docs/models/inkling)

## Related Pages

- [[entities/thinking-machines-lab]] — Developer of Inkling
- [[entities/daniel-han]] — Unsloth CEO, led the Inkling GGUF quantization collaboration
- [[concepts/unsloth]] — Unsloth framework
- [[concepts/unsloth-fast-fine-tuning]] — Unsloth's fast fine-tuning approach
