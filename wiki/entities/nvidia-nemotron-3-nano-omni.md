---
title: NVIDIA Nemotron 3 Nano Omni
created: 2026-05-09
updated: 2026-05-09
type: entity
tags: [model, multimodal, open-source, nvidia, mixture-of-experts, ai-agents, inference]
sources: [raw/articles/2026-04-28_nvidia-nemotron-3-nano-omni.md]
---

# NVIDIA Nemotron 3 Nano Omni

A fully open-source multimodal model from NVIDIA that unifies video, audio, image, and text reasoning in a single efficient architecture. Part of the [[entities/nvidia|NVIDIA Nemotron 3 family]].

## Overview

Nemotron 3 Nano Omni is designed to replace fragmented vision-language-audio stacks in agentic systems. It functions as the multimodal perception and context sub-agent within agentic workflows, enabling agents to perceive and reason across all modalities in a single shared perception-to-action loop.

Released April 28, 2026. Available on [[entities/oracle|Oracle Cloud Infrastructure]] Enterprise AI as of May 2026.

## Specifications

| Property | Value |
|----------|-------|
| Architecture | Hybrid Mixture-of-Experts (MoE) |
| Total parameters | 30B |
| Active parameters | 3B |
| Modalities | Video, audio, image, text (unified) |
| License | Fully open weights, datasets, recipes |
| GPU support | Ampere, Hopper, Blackwell |
| Inference engines | vLLM, TensorRT-LLM |
| Quantization | FP8, NVFP4 |

## Performance

- **Document intelligence**: Best-in-class on MMlongbench-Doc and OCRBenchV2
- **Video/audio**: Leads on WorldSense, DailyOmni, VoiceBench
- **MediaPerf**: Highest throughput across all tasks, lowest inference cost for video-level tagging
- **Efficiency**: Convolutional 3D-based temporal-spatial processing enables sustained multimodal perception with lower compute costs

## Architecture

Uses a hybrid MoE design that activates only the expert required for each task and modality. Combined with convolutional 3D temporal-spatial processing, this delivers predictable low-latency inference across GPU tiers — from workstations to data centers.

## Role in Agentic Systems

Nemotron 3 Nano Omni is positioned as the perception sub-agent within larger agentic architectures. By handling all multimodal perception in a single model, it reduces orchestration complexity, inference hops, and cross-modal context inconsistency compared to fragmented multi-model pipelines.

## Related Pages
- [[entities/nvidia]] — Parent company and Nemotron family
- [[concepts/multimodal]] — Multimodal models
- [[concepts/mixture-of-experts]] — MoE architecture
- [[concepts/ai-agents]] — Agentic AI systems
- [[concepts/open-source]] — Open-source AI
- [[concepts/inference]] — Model inference optimization
