---
title: SkyPilot
type: entity
tags:
  - cloud
  - ai-infrastructure
  - developer-tooling
  - open-source
  - kubernetes
created: 2026-06-15
updated: 2026-06-15
sources:
  - "https://skypilot.co"
  - "https://github.com/skypilot-org/skypilot"
  - "https://sky.cs.berkeley.edu"
---

# SkyPilot

**Type:** Open-source multi-cloud AI workload orchestrator
**Origin:** UC Berkeley Sky Computing Lab
**Key people:** Zongheng Yang, Zhanghao Wu, and team
**License:** Apache 2.0
**GitHub:** https://github.com/skypilot-org/skypilot
**Website:** https://skypilot.co
**Status:** Acquired by CoreWeave (2025)

## Overview

SkyPilot is an open-source framework for running AI and data workloads on any cloud. It provides a unified interface to launch jobs across cloud providers (AWS, GCP, Azure, Lambda, CoreWeave, etc.) with automatic cost optimization, instance selection, and data transfer.

Originally developed at UC Berkeley's Sky Computing Lab, SkyPilot addresses the fragmentation problem: ML engineers spend significant time configuring cloud infrastructure instead of working on models. SkyPilot abstracts away cloud-specific details and automatically finds the cheapest available GPUs.

## Core Features

### `sky launch` — One Command to Any Cloud
```yaml
# task.yaml
resources:
  accelerators: A100:8
  cloud: gcp  # or aws, azure, lambda, etc.

run: |
  python train.py --epochs 100
```
```bash
sky launch task.yaml
```
SkyPilot handles instance provisioning, setup, data sync, and job execution.

### Cost Optimization
- **Spot instance support**: Automatic spot/recovery across clouds
- **Price comparison**: Shows costs across all available clouds before launch
- **Auto-failover**: If one cloud is out of capacity, automatically tries another

### Data Management
- **Cloud storage mounting**: Mount S3/GCS/Azure Blob as local filesystems
- **Data transfer**: Automatic upload/download of datasets and artifacts
- **Persistent storage**: Keep data across spot interruptions

### Multi-Node Training
- **Distributed training**: Launch multi-node PyTorch DistributedDataParallel jobs
- **Cluster management**: `sky status` shows running clusters across all clouds
- **Job queue**: Submit multiple jobs to the same cluster

## Architecture

SkyPilot has a layered architecture:
1. **Cloud abstraction**: Unified API across AWS, GCP, Azure, Lambda, CoreWeave, etc.
2. **Optimizer**: Selects the cheapest cloud/instance type that satisfies resource requirements
3. **Provisioner**: Handles instance creation, networking, and SSH setup
4. **Runtime**: Manages job execution, log streaming, and file sync

## Use Cases in ML/AI

- **Training**: Launch distributed training jobs on the cheapest available GPUs
- **Fine-tuning**: Run fine-tuning experiments across multiple cloud providers
- **Inference**: Deploy model serving endpoints with auto-scaling
- **Research**: Berkeley researchers use SkyPilot to access GPUs across multiple clouds

## Acquisition by CoreWeave

SkyPilot was acquired by CoreWeave in 2025 as part of CoreWeave's vertical integration strategy. The acquisition brought:
- **Technology**: Cost-optimized job scheduling and multi-cloud orchestration
- **Team**: Berkeley Sky Computing Lab researchers with deep expertise in cloud systems
- **Open-source community**: Widely used open-source project with active contributors

SkyPilot's multi-cloud scheduling capabilities complement CoreWeave's GPU cloud by making it easier for users to launch workloads on CoreWeave infrastructure while maintaining the flexibility to use other clouds.

## Relationship to CoreWeave Stack

SkyPilot sits at the compute orchestration layer in CoreWeave's vertical stack:
- **Below**: CoreWeave GPU infrastructure (bare-metal H100s, A100s)
- **Above**: W&B Models (experiment tracking) and W&B Weave (LLM tracing)
- **Peer**: OpenPipe ART (RL post-training)

See [[entities/coreweave]] for the full acquisition and integration picture.

## Compared to Alternatives

| Tool | Focus | Cloud support | Key difference |
|------|-------|---------------|----------------|
| **SkyPilot** | Multi-cloud AI jobs | AWS, GCP, Azure, Lambda, etc. | Automatic cost optimization + failover |
| **RunPod** | GPU cloud marketplace | RunPod only | Simplified GPU rental |
| **Modal** | Serverless functions | Modal only | Pay-per-second, no cluster management |
| **Brev** | Dev environments | Multi-cloud | IDE-focused, less batch-job oriented |
| **Kubernetes + Helm** | General orchestration | Any K8s cluster | More control, more setup |

## Related

- [[entities/coreweave]] — Acquirer (2025)
- [[entities/weights-and-biases|Weights & Biases]] — Sister acquisition (platform layer)
- [[entities/openpipe|OpenPipe]] — Sister acquisition (training layer)
