---
title: NVIDIA DeepSeek-V4.1-Flash NVFP4 checkpoint
created: 2026-11-01
updated: 2026-11-01
type: event
tags: [announcement, deepseek, nvidia, quantization, inference, open-source]
sources:
  - https://huggingface.co/nvidia/DeepSeek-V4.1-Flash-1017-NVFP4
  - https://x.com/TheZachMueller/status/2116262967167598739
confidence: medium
---

# NVIDIA DeepSeek-V4.1-Flash-1017-NVFP4

On **October 30, 2026**, NVIDIA published
[`nvidia/DeepSeek-V4.1-Flash-1017-NVFP4`](https://huggingface.co/nvidia/DeepSeek-V4.1-Flash-1017-NVFP4)
on the Hugging Face Hub — an **NVFP4-quantized** build of DeepSeek's
**V4.1-Flash-1017** checkpoint (the Oct 17, 2026 release; see
[[events/2026-10-17-deepseek-v4.1-flash-1017-release]]). The Hub page describes it as an
**Image-Text-to-Text model with 665B parameters**, i.e. the multimodal V4.1-Flash variant in
NVIDIA's 4-bit floating-point format targeting Blackwell (SM100) hardware.

## Significance

- **Day-13 vendor quant**: NVIDIA shipped an official NVFP4 build roughly two weeks after the
  1017 checkpoint release, continuing the pattern of third-party (non-DeepSeek) artifacts
  appearing quickly around V4.x releases.
- **NVFP4 vs MXFP4**: this is the NVFP4 (Blackwell-native) path — distinct from DeepSeek's own
  MXFP4 QAT weights. Kernel maturity and serving performance differ between the two formats
  (see [[concepts/deepseek-v4-serving]], [[concepts/nvidia-blackwell-architecture]]).
- **Multimodal framing**: the "Image-Text-to-Text" Hub tag aligns with the 552B–665B-class
  multimodal MoE description in [[entities/deepseek-v4.1-flash]].

## Reception

[[entities/zach-mueller]] (Hugging Face) posted "It's here 😍 Thank you @NVIDIAAI 🫡" with the model
link on 2026-10-30 (96 likes, 29 bookmarks) — the quant was anticipated by the open-model serving
community.

## Caveats

- Page is thin: model card details (benchmark deltas vs BF16/MXFP4, serving recipes) were not
  scraped this run; treat parameter count (665B) as the Hub-listed figure, pending card details.

## Related Pages

- [[concepts/deepseek-v4]]
- [[entities/deepseek-v4.1-flash]]
- [[events/2026-10-17-deepseek-v4.1-flash-1017-release]]
- [[concepts/nvidia-blackwell-architecture]]
