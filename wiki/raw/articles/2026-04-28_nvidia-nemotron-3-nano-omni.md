---
title: "NVIDIA Nemotron 3 Nano Omni Powers Multimodal Agent Reasoning in a Single Efficient Open Model"
source: https://developer.nvidia.com/blog/nvidia-nemotron-3-nano-omni-powers-multimodal-agent-reasoning-in-a-single-efficient-open-model/
date: 2026-04-28
author: Anjali Shah, Isabel Hulseman, Padmavathy Subramanian
publisher: NVIDIA Technical Blog
---

Agentic systems often reason across screens, documents, audio, video, and text within a single perception-to-action loop. However, they still rely on fragmented model chains—separate stacks for vision, audio, and text. NVIDIA Nemotron 3 Nano Omni brings unified multimodal reasoning into a single, highly efficient open model.

## Key Specifications
- Architecture: 30B-A3B hybrid Mixture-of-Experts (MoE)
- Total parameters: 30B, Active: 3B
- Modalities: video, audio, image, text — unified
- License: Fully open weights, datasets, and recipes
- Optimized for: NVIDIA Ampere, Hopper, Blackwell GPUs
- Supported engines: vLLM, NVIDIA TensorRT-LLM
- Quantization: FP8 and NVFP4 support

## Performance Highlights
- Best-in-class accuracy on MMlongbench-Doc and OCRBenchV2 (document intelligence)
- Leading video/audio understanding: WorldSense, DailyOmni, VoiceBench
- MediaPerf benchmark: highest throughput across every task, lowest inference cost for video-level tagging
- Designed to function as the multimodal perception and context sub-agent within agentic systems

## Architecture Details
Built on hybrid MoE architecture that activates only the expert required for each task and modality. Supports convolutional 3D-based temporal-spatial processing. Enables sustained multimodal perception with lower compute costs across GPU tiers — from workstations to data center and cloud deployments.

Available on Oracle Cloud Infrastructure (OCI) Enterprise AI as of May 2026.
