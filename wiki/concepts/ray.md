---
title: "Ray (distributed computing framework)"
created: 2026-07-19
updated: 2026-07-19
type: concept
tags:
  - distributed-systems
  - infrastructure
  - python
sources:
  - raw/articles/anyscale.com--blog-building-highly-available-and-scalable-online-applicati--7faef8c2.md
  - raw/articles/anyscale.com--blog-online-resource-allocation-with-ray-at-ant-group--487de159.md
related:
  - entities/anyscale
  - concepts/ml-training-infrastructure
---

# Ray

Ray is an open-source distributed computing framework for Python, originally developed at UC Berkeley's RISELab. It provides a simple API for scaling Python applications from a laptop to a cluster.

## Core Abstractions

### Tasks (Stateless)
```python
@ray.remote
def compute(x):
    return x * x

futures = [compute.remote(i) for i in range(100)]
results = ray.get(futures)
```

### Actors (Stateful)
```python
@ray.remote
class Counter:
    def __init__(self):
        self.value = 0
    def increment(self):
        self.value += 1
        return self.value
```

### Placement Groups
Resource-aware scheduling for co-locating related tasks on specific node types (e.g., GPU machines for LP solvers).

## Key Components

| Component | Purpose |
|-----------|---------|
| **Ray Core** | Task/actor API, distributed scheduler |
| **Ray Serve** | Model serving with batching, composition |
| **Ray Train** | Distributed training (PyTorch, TensorFlow) |
| **Ray Tune** | Hyperparameter optimization |
| **Ray Data** | Distributed data processing |
| **RLlib** | Reinforcement learning at scale |

## Production Scale: Ant Group

[[entities/anyscale|Anyscale]] and Ant Group demonstrated Ray at massive scale:
- **Ant Ray Serving**: 60,000 cores, 5,000 nodes
- **Online resource allocation**: 6,000+ cores for LP-based optimization
- **SLA**: 99.99% availability
- **Event**: Double Eleven (11.11) — world's largest online shopping event

### Architecture Pattern
The Ant Group deployment uses a three-tier computation model:
1. **Online**: Synchronous RPC, ms-level latency (user-facing)
2. **Nearline**: Real-time planning, seconds-level (LP solving)
3. **Offline**: Flow estimation, minutes-level (historical data)

This pattern enables real-time decision-making with LP duality — dual variables computed offline/nearline serve as fast parameters for online reranking.

## Why Ray for ML Infrastructure

- **Unified API**: Same framework for training, serving, and data processing
- **Python-native**: No need to learn new languages or DSLs
- **Heterogeneous**: CPU, GPU, mixed workloads on same cluster
- **Fault tolerance**: Automatic task retry, actor reconstruction
- **Ecosystem**: Deep integration with PyTorch, HuggingFace, scikit-learn

## Sources

- "Building Highly Available and Scalable Online Applications on Ray at Ant Group" — [[raw/articles/anyscale.com--blog-building-highly-available-and-scalable-online-applicati--7faef8c2.md]]
- "Online Resource Allocation with Ray at Ant Group" — [[raw/articles/anyscale.com--blog-online-resource-allocation-with-ray-at-ant-group--487de159.md]]
