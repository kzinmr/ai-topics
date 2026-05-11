---
title: "NVIDIA Nemotron 3 Nano Omni Powers Multimodal Agent Reasoning in a Single Efficient Open Model"
source: "https://developer.nvidia.com/blog/nvidia-nemotron-3-nano-omni-powers-multimodal-agent-reasoning-in-a-single-efficient-open-model/"
date: 2026-04-28
author: "Anjali Shah, Isabel Hulseman, Padmavathy Subramanian (NVIDIA)"
tags: [nvidia, model, multimodal, open-source, inference]
---

# NVIDIA Nemotron 3 Nano Omni

NVIDIA announced Nemotron 3 Nano Omni, a unified multimodal model that reasons across video, audio, image, and text in a single architecture. Built on a 30B-A3B hybrid MoE architecture.

Key specs:
- 30B total parameters, 3B active (MoE)
- Unified video/audio/image/text reasoning
- Fully open weights, datasets, and recipes
- Supports FP8 and NVFP4 quantization
- Optimized for NVIDIA Ampere, Hopper, Blackwell GPUs
- Compatible with vLLM and TensorRT-LLM

Benchmarks: Best-in-class on MMLongbench-Doc, OCRBenchV2, WorldSense, DailyOmni, VoiceBench. Highest throughput on MediaPerf benchmark.

Available on HuggingFace and OCI Enterprise AI.
