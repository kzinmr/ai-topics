---
title: "Vision-Language-Action Models (VLA)"
created: 2026-05-31
updated: 2026-05-31
type: concept
tags:
  - robotics
  - multimodal
  - model
  - reinforcement-learning
sources:
  - https://openvla.github.io/
  - https://arxiv.org/html/2604.19728v1
  - https://arxiv.org/html/2601.02456v1
  - https://www.marktechpost.com/2026/04/28/top-10-physical-ai-models-powering-real-world-robots-in-2026/
---

# Vision-Language-Action Models (VLA)

**Vision-Language-Action (VLA)** models are a class of foundation models that map multimodal observations (vision + language) directly to robot action commands, enabling general-purpose robotic manipulation through end-to-end learning.

## Architecture

VLA models typically consist of:
1. **Visual encoder**: Processes image/video inputs into embeddings (e.g., SigLIP, DINOv2)
2. **Language backbone**: LLM that interprets instructions and generates reasoning
3. **Action head**: Maps the fused representations to continuous motor control commands

## Key Models (2024-2026)

| Model | Developer | Parameters | Key Innovation |
|---|---|---|---|
| OpenVLA | Stanford/Berkeley | 7B | Open-source, beats 55B RT-2-X by 16.5pp |
| π0 / π0.5 / π0.7 | [[entities/physical-intelligence|Physical Intelligence]] | — | Flow-matching, compositional generalization |
| GR00T N1.7 | [[entities/nvidia|NVIDIA]] Isaac | 3B | EgoScale: 20K+ hrs human egocentric video |
| Helix | [[entities/figure-ai|Figure AI]] | 7B+80M | Dual-system: System 2 (7-9Hz) + System 1 (200Hz) |
| InternVLA-A1 | Shanghai AI Lab | 2B-3B | Mixture-of-Transformers for understanding + action |
| Gemini Robotics | [[entities/deepmind|Google DeepMind]] | — | Agentic capabilities, transparent reasoning |
| SmolVLA | [[entities/huggingface|HuggingFace]] LeRobot | 450M | Community data, runs on consumer hardware |
| LaRA-VLA | Research | — | Latent reasoning, 90% inference latency reduction |

## OpenVLA Highlights

- Trained on 970K robot episodes from Open X-Embodiment dataset
- Controls multiple robot platforms out-of-the-box
- LoRA fine-tuning matches full fine-tuning with only 1.4% of parameters
- 7x smaller than RT-2-X (55B) but outperforms it

## VLA Foundry

Unified open-source framework (arXiv:2604.19728v1) that spans the entire LLM → VLM → VLA training pipeline in a single codebase. Supports from-scratch training and pretrained backbones from HuggingFace. Released Foundry-VLA-1.7B (from scratch) and Foundry-Qwen3VLA-2.1B-MT (on Qwen3-VL backbone).

## Current State (May 2026)

VLA models have crossed a genuine technical threshold:
- Can generalize to novel situations rather than failing on first contact with the unexpected
- Early production deployments generating real returns in logistics, manufacturing, healthcare
- Training data scarcity remains a bottleneck relative to language/vision models
- Physical AI has crossed from research to deployment phase

## Related Pages
- [[concepts/physical-ai]] — Physical AI and robotics
- [[concepts/world-models]] — World models for simulation
- [[entities/nvidia]] — NVIDIA Isaac GR00T
- [[entities/physical-intelligence]] — Physical Intelligence, π0 developer
- [[entities/figure-ai]] — Figure AI, Helix developer
- [[entities/deepmind]] — Google DeepMind, Gemini Robotics
