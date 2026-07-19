---
title: "Anyscale"
created: 2026-07-19
updated: 2026-07-19
type: entity
tags:
  - company
  - infrastructure
  - distributed-systems
  - ray
sources:
  - raw/articles/anyscale.com--blog-building-highly-available-and-scalable-online-applicati--7faef8c2.md
  - raw/articles/anyscale.com--blog-online-resource-allocation-with-ray-at-ant-group--487de159.md
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
