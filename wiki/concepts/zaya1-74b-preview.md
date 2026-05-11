---
title: ZAYA1-74B-Preview
type: concept
category: model
tags:
  - model
  - open-source
  - amd
  - reasoning
  - zyphra
aliases: [ZAYA1-74B]
sources:
  - https://huggingface.co/Zyphra/ZAYA1-74B-preview
  - https://www.zyphra.com/post/zaya1-74b
related:
  - entities/zyphra
  - concepts/zaya1-vl-8b
  - concepts/zaya1-8b
  - concepts/mixture-of-experts
created: 2026-05-09
updated: 2026-05-09
---

# ZAYA1-74B-Preview

**ZAYA1-74B-Preview** is a Mixture of Experts (MoE) language model with **4B active and 74B total parameters**, released by [[entities/zyphra|Zyphra]] as a research preview in May 2026 under Apache 2.0 license.

## Characteristics

- **Type**: Reasoning-base checkpoint — **not chat-tuned**, no RL post-training
- **Architecture**: MoE with Mamba/CCA hybrid attention
- **Training**: End-to-end on AMD GPUs
- **Context**: Uses Qwen3 reasoning parser format
- **Tool calling**: Supports tool calling via `zaya_xml` parser

## Deployment

Requires Zyphra's vLLM fork:

```bash
pip install "vllm @ git+https://github.com/Zyphra/vllm.git@zaya1-pr"

vllm serve Zyphra/ZAYA1-74B-Preview --port 8010 \
  --mamba-cache-dtype float32 --dtype bfloat16 \
  --reasoning-parser qwen3 --enable-auto-tool-choice \
  --tool-call-parser zaya_xml
```

For multi-GPU: recommended DP=EP (Data Parallel = Expert Parallel), not TP (Tensor Parallel), as TP is unsupported for CCA in the current fork.

Also runnable via Zyphra's transformers fork:
```bash
pip install "transformers @ git+https://github.com/Zyphra/transformers.git@zaya1"
```

## Status

This is a **preview** release — the model has not undergone RLHF/DPO alignment and is intended for research. A chat-tuned version is expected in future releases.

## Significance

ZAYA1-74B demonstrates Zyphra's scaling trajectory from 8B to 74B total parameters (4B active), all trained on AMD hardware. The 4B active parameter count makes inference relatively efficient compared to equivalently-capable dense models.

## See Also

- [[entities/zyphra]] — Company behind ZAYA1
- [[concepts/zaya1-vl-8b]] — Zyphra's vision-language model
- [[concepts/mixture-of-experts]] — MoE architecture
