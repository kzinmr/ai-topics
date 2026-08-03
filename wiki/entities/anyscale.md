---
title: "Anyscale"
created: 2026-07-19
updated: 2026-08-03
type: entity
tags:
  - company
  - infrastructure
  - architecture
  - ray
  - nscale
  - physical-ai
sources:
  - raw/articles/anyscale.com--blog-building-highly-available-and-scalable-online-applicati--7faef8c2.md
  - raw/articles/anyscale.com--blog-online-resource-allocation-with-ray-at-ant-group--487de159.md
  - raw/articles/anyscale.com--blog-anyscale-signs-definitive-agreement-to-join-nscale--b919a211.md
  - raw/articles/anyscale.com--blog-introducing-the-anyscale-physical-ai-skill--46582823.md
related:
  - concepts/ray
  - entities/ant-group
---

# Anyscale

Anyscale is the company behind [[concepts/ray|Ray]], the open-source distributed computing framework. Founded by the creators of Ray at UC Berkeley's RISELab, Anyscale commercializes Ray for ML infrastructure, offering managed Ray clusters and enterprise tooling.

## Core Product: Ray

Ray provides a simple distributed API for Python workloads:
- `@ray.remote` decorator for task parallelism
- Actor model for stateful distributed computation
- Flexible scheduling across heterogeneous clusters
- Integration with ML ecosystem (training, serving, tuning)

## Enterprise Deployments

### Ant Group — Ray Serving at Scale
Ant Group built **Ant Ray Serving**, an online service framework based on Ray:
- **Scale**: 60,000 cores, 5,000 nodes
- **Use cases**: Payment strategy computation, marketing, order allocation
- **SLA**: 99.99% availability (< 1 hour downtime/year)
- **Events**: Production-tested through Double Eleven, Double Twelve, and Chinese New Year promotions
- **Architecture**: Serverless platform for Java/Python code as online services
  - Deployment, scaling, traffic routing, and monitoring
  - Users focus on business logic; Ray handles distribution

Source: [[raw/articles/anyscale.com--blog-building-highly-available-and-scalable-online-applicati--7faef8c2.md]]

### Ant Group — Online Resource Allocation
A flexible, high-performance online resource allocation system based on Ray:
- **Scale**: 6,000+ CPU cores
- **Applications**: Marketing, search, recommendation, advertising
- **Core problem**: Maximize ROI under resource constraints (LP optimization)
- **Architecture**: Three-tier computation:
  - **Online**: Synchronous RPC, ms-level latency, high availability
  - **Nearline**: Real-time planning, seconds-level latency
  - **Offline**: Flow estimation, minutes-level latency
- **Key innovation**: LP duality for real-time decision-making with dual variables as fast serving parameters
- **Components**: Real-time model calibration, traffic prediction, constraint correction, large-scale LP optimization

Source: [[raw/articles/anyscale.com--blog-online-resource-allocation-with-ray-at-ant-group--487de159.md]]

## Nscale Acquisition (Aug 2026)

Anyscale signed a definitive agreement to join **Nscale**, a neocloud provider focused on physical AI infrastructure. Key points:
- **Ray doubling down**: Expanding investment in Ray + open-source community under PyTorch Foundation governance (Google, NVIDIA, Microsoft contributing)
- **Nscale**: Multi-gigawatt pipeline, vertical integration from land/power to data centers, among first to deploy **GB300 NVL72** at scale
- **GPU capacity**: Anyscale Platform customers gain access to Nscale compute
- **Multi-cloud**: Anyscale Platform continues across all major clouds post-closing
- **Revenue**: 70%+ QoQ revenue growth in the past quarter
- **Nscale plans** to join PyTorch Foundation as Platinum member

The rationale: software must co-optimize with rack/cluster topology, hardware heterogeneity, and disaggregated compute. Joint optimization across the stack is now essential.

Source: [[raw/articles/anyscale.com--blog-anyscale-signs-definitive-agreement-to-join-nscale--b919a211]]

## Physical AI Skill (Aug 2026)

Anyscale introduced the **Physical AI Skill** for robotics and autonomous driving workloads built on Ray. Covers six workload classes:
1. **VLA fine-tuning** (imitation learning/SFT) — π0, SmolVLA, OpenVLA, GR00T-N1.5, Alpamayo-1.5
2. **Offline/open-loop VLA RL post-training** — using logged trajectories with Cosmos-RL (GRPO/RLVR)
3. **Online/closed-loop VLA RL post-training** — with AlpaSim, Isaac Lab simulators
4. **Robot policy serving** — Ray Serve HTTP endpoints with GPU-isolated simulator workers
5. **World-model training** — Cosmos-Predict2, diffusion world models
6. **Simulator-native RL** — Isaac Lab, MuJoCo MJX, Unreal Engine 5.7

The skill scopes workloads, makes systems decisions explicit, and generates code + compute configs. Extends Anyscale Agent Skills into physical AI following the LLM post-training skill.

Source: [[raw/articles/anyscale.com--blog-introducing-the-anyscale-physical-ai-skill--46582823]]

## Why Ray Matters for AI

Ray's significance in the AI ecosystem:
- **Training**: Distributed training at scale (PyTorch, TensorFlow integration)
- **Serving**: [[concepts/ray|Ray Serve]] for model serving with batching, model composition
- **Tuning**: Ray Tune for hyperparameter optimization
- **Data**: Ray Data for distributed data processing
- **RL**: RLlib for reinforcement learning at scale

## Sources

- Anyscale Blog, "Building Highly Available and Scalable Online Applications on Ray at Ant Group"
- Anyscale Blog, "Online Resource Allocation with Ray at Ant Group"
