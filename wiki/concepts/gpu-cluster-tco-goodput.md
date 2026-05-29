---
title: "GPU Cluster TCO & Goodput Framework"
type: concept
created: 2026-05-29
updated: 2026-05-29
tags:
  - gpu
  - cloud
  - ai-infrastructure
  - economics
  - reliability
  - training
related:
  - [[concepts/gpu-cloud-rankings]]
  - [[entities/semianalysis]]
  - [[entities/dylan-patel]]
  - [[concepts/compute-scaling-bottlenecks]]
sources:
  - raw/articles/substack.com--app-link-post--1509e963.md
  - raw/articles/substack.com--app-link-post--dc1fa8f9.md
  - https://semianalysis.com/
  - https://www.clustermax.ai/
---

# GPU Cluster TCO & Goodput Framework

A methodology for calculating the **Total Cost of Ownership (TCO)** of GPU clusters that goes beyond raw $/GPU-hr pricing. Introduced by SemiAnalysis in their ClusterMAX research series (April 2026), it demonstrates that two cloud offerings with identical GPU pricing can have very different TCO once indirect costs are factored in.

## Core Thesis

> "Focusing solely on the price per GPU-hour a provider offers can be misleading. What appears to be a cheaper cluster can in many cases end up being more expensive." — SemiAnalysis

The TCO framework decomposes GPU cluster costs into **8 line items**:

| # | Cost Category | Unit | Description |
|---|--------------|------|-------------|
| 1 | **GPUs** | $/GPU-hr | Headline rental price, factoring in volume discounts, spot/preemptible instances, and orchestration premiums (e.g., SageMaker Hyperpod vs standard EC2) |
| 2 | **Storage** | $/GB-mo | Hot storage (NVMe parallel filesystems), warm/object storage, cold archival. Includes API call costs and data egress charges. |
| 3 | **Networking** | $/hr or $/GB-mo | Frontend/N-S: public IPs, firewalls, load balancers, data egress/transfer. Backend/E-W: InfiniBand, RoCE, EFA interconnects. |
| 4 | **Control Plane** | $/hr | Orchestration software management: login nodes, code development, job submission, CPU nodes for data processing and RL rollouts. |
| 5 | **Support** | % uplift | Tiered support charges (e.g., AWS: 10% → 3% of monthly bill as spend increases). Affects response time during outages. |
| 6 | **Goodput Expense** | % uplift | **Implicit cost** — downtime from failures/interruptions expressed as wasted rental time. Captures MTBF, time-to-identify, time-to-repair, checkpoint frequency, blast radius. |
| 7 | **Setup Expense** | $/hr | Engineering time to configure cluster and tune performance (e.g., NCCL + EFA tuning on AWS can take weeks to months). |
| 8 | **Debugging Expense** | $/hr | Ongoing engineering time spent debugging cluster issues (e.g., NCCL + EFA debugging involves 4-5 layers from PyTorch code through driver stack to NIC firmware). |

## TCO Formula

$$\text{TCO}_{\$/\text{cluster-mo}} = \text{GPU} + \text{Storage} + \text{Network} + \text{Control Plane} + \text{Support} + \text{Goodput} + \text{Setup} + \text{Debugging}$$

Where setup costs are amortized over the contract term (3 months to 3 years). Spending weeks setting up a 3-month cluster is devastating; the same effort on a 3-year contract is negligible.

## Goodput: The Hidden Cost Multiplier

**Goodput** = the amount of *useful* work performed on a cluster, as opposed to raw throughput. Not all throughput is "good" — GPU failures, NCCL stalls, and OOM errors during checkpoint saves waste compute without productive output.

### Why Goodput Matters More at Scale

| Cluster Size | Single GPU Failure Impact |
|--------------|--------------------------|
| 8 GPUs (1 job) | Job restarts from checkpoint; ~10-15 min lost |
| 4,096 GPUs (1 big job) | Entire job restarts; **hours** of wasted compute + re-initialization |
| 8,192 GPUs | Even worse — blast radius grows with cluster size |

As SemiAnalysis notes: *"If 80% of your cluster is running one job, and that job has to restart (10-15 minutes for job initialization), this costs you all of those minutes plus all the wasted compute from the last checkpoint to the time of failure."*

### Goodput Expense Formulae

SemiAnalysis defines three scenarios with distinct formulae:

**1. Checkpoint-Restart, Hot Spare ($G_{\text{chkpt-hot}}$)**
$$G_{\text{chkpt-hot}} = \left[\max\left(t_{\text{id}}, \frac{t_{\text{chkpt}}}{2}\right) + t_{\text{init}} + t_{\text{repair}}\right] \cdot j_{\text{size}} \cdot \#_{\text{failures}} \cdot \$_{\text{GPU-hr}}$$

**2. Checkpoint-Restart, Cold Spare ($G_{\text{chkpt-cold}}$)**
$$G_{\text{chkpt-cold}} = \left\{\left[\max\left(t_{\text{id}}, \frac{t_{\text{chkpt}}}{2}\right) + t_{\text{init}}\right] \cdot j_{\text{size}} + t_{\text{repair}} \cdot b_{\text{radius}}\right\} \cdot \#_{\text{failures}} \cdot \$_{\text{GPU-hr}}$$

**3. Fault-Tolerant Training ($G_{\text{tolerant}}$)**
$$G_{\text{tolerant}} = \left[(t_{\text{id}} + t_{\text{failover}}) \cdot j_{\text{size}} + t_{\text{repair}} \cdot b_{\text{radius}}\right] \cdot \#_{\text{failures}} \cdot \$_{\text{GPU-hr}}$$

| Variable | Meaning |
|----------|---------|
| $t_{\text{id}}$ | Time to identify failure (provider monitoring or customer report) |
| $t_{\text{chkpt}}$ | Checkpoint frequency (customer-configured) |
| $t_{\text{init}}$ | Time to initialize training job |
| $t_{\text{repair}}$ | Time to repair/replace failed node (MTTR) |
| $t_{\text{failover}}$ | Time to failover to hot spare node |
| $b_{\text{radius}}$ | Blast radius (e.g., 8-way HGX or 64-way NVL72) |
| $j_{\text{size}}$ | Average job size (GPUs per job) |
| $\#_{\text{failures}}$ | Number of failures (inverse of MTBF) |
| $\$_{\text{GPU-hr}}$ | Price per GPU hour |

### Blast Radius at Scale (Node MTBF)

As node failures become more common and cluster size increases, time between failures (MTBF) shrinks dramatically. This is why **provider operational quality** matters more than raw GPU pricing at scale.

## Fault-Tolerant Training Frameworks Compared

### 1. TorchFT (Meta — Open Source)

- **Approach**: Replica-group-level fault tolerance integrated with torchtitan
- **Mechanism**: When a GPU/node fails, the entire replica group crashes. Surviving groups serialize state via `state_dict()`, serve over HTTP to recovering group, which calls `load_state_dict()` and rejoins quorum. Orchestrated by TorchFT lighthouse server.
- **Blast Radius**: Entire replica group (e.g., FSDP shard=16 → 16 GPUs lost per failure; shard=32 → 32 GPUs lost)
- **Tradeoff**: Requires GLOO (not NCCL) for cross-replica communication → **10%+ per-iteration overhead** (allreduce through CPU via TCP instead of RDMA)
- **Scheduler**: Agnostic — supports Kubernetes and Slurm
- **Adoption**: Open source, but not widely adopted for production training yet

**FSDP-specific detail**: Because parameters are all-gathered before computation and gradients are reduce-scattered in backward, a single failed or hung rank can stall the entire participating group. HSDP makes this explicit: blast radius is a topology decision at the replica-group level.

**Checkpointing interaction**: On FSDP2, converting a DTensor state dict back to a full tensor for saving issues an all-gather across ranks. Checkpoint frequency is itself a reliability parameter — more frequent checkpointing = more communication surface for failures.

**Not all failures look the same**: A meaningful share of large-scale incidents first appear as **stuck collectives or watchdog timeouts** (symptoms, not root causes). Goodput loss includes not just repair time but also the time to detect, attribute, and unwind a hung collective across participating ranks.

### 2. AWS SageMaker HyperPod Checkpointless Training (AWS — Proprietary)

- **Approach**: Model redundancy — each GPU maintains redundant copies of its model shards on peer GPUs
- **Mechanism**: Cross-group sync allows recovery without interrupting running job. Failing node loads state via RDMA over EFA. Managed by CheckpointManager.
- **Blast Radius**: Proportional to replica group size relative to total job
- **Requirements**: Kubernetes-only, NeMo Megatron-only (as of Dec 2025 launch)
- **Recovery Time**: **1 min 45 sec** (vs 15 min for checkpoint restart)
- **Tradeoff**: **~5% GPU memory overhead** from redundant model replicas → reduced batch size or different parallelism strategies → performance impact
- **Integration**: Deep health checks identify hardware failures in <2 min, replace nodes in <20 min
- **Proven at**: 1,000+ GPU scale (used internally for training Amazon Nova models)

### 3. TorchPass (Clockwork.io — Licensed)

- **Approach**: Scheduler-level plugin with "just-in-time" checkpoint via `get_state()`
- **Mechanism**: Failing node transfers state via RDMA to idle spare node. Minimal code changes to training scripts (few lines via Manager class).
- **Blast Radius**: Single node (hard failures handled via unplanned migration from healthy replica group)
- **Performance Overhead**: **Zero** — maintains same training performance as non-fault-tolerant jobs
- **Cost Model**: Idle spare nodes in cluster or pre-empting lower-priority jobs
- **Tested On**: 8-node GKE cluster with torchtitan via PyTorchJob (KubeFlow)
- **Failure Types Supported**: Planned migrations (upgrades/maintenance) + unplanned migrations (ECC errors, GPU off-bus, power failures, link flaps, kernel panics)
- **Recovery Times**: Similar to TorchFT for planned migrations, but without performance overhead

### Framework Comparison Summary

| Dimension | TorchFT | AWS Checkpointless | TorchPass |
|-----------|---------|-------------------|-----------|
| **License** | Open Source | AWS Proprietary | Commercial (Licensed) |
| **Performance Overhead** | 10%+ (GLOO vs NCCL) | 5% (memory) | ~0% |
| **Blast Radius** | Entire replica group | Replica group | Single node |
| **Recovery Time** | Minutes (state transfer) | 1 min 45 sec | Similar (JIT checkpoint) |
| **Infrastructure Cost** | Lighthouse server | Redundant model copies | Idle spare nodes |
| **Code Changes** | Moderate (lighthouse integration) | Minimal (CheckpointManager) | Minimal (few lines) |
| **Platform Support** | K8s + Slurm | K8s only (HyperPod EKS) | K8s (GKE tested) |
| **Maturity** | Emerging | Proven at 1k+ GPUs | Early production |

**Key insight**: *"Fault tolerant training remains secret sauce available to frontier labs or those willing to pay for a software license."* Meanwhile, **fault tolerant inference** is already standard for single 8-way systems via frameworks like [[entities/nvidia|NVIDIA Dynamo]], [[concepts/mooncake]], and LMCache.

## Scenario Analysis: TCO by Workload Type

### Scenario 1: Large LLM Pretrain (5,184 GB300 NVL72 GPUs)

- **Assumptions**: Equal GPU pricing ($4/GPU-hr), 80% single job, 2TB/GPU storage, long EFA tuning setup
- **Results (3-year TCO multiplier vs Gold-tier)**:

| Provider Tier | TCO Multiplier | Key Cost Drivers |
|--------------|---------------|-----------------|
| **Gold-tier** (Nebius/Fluidstack/Crusoe) | **1.00x** | Baseline — included support, strong storage, quick setup |
| **Hyperscaler** (AWS/Azure/GCP/Oracle) | **1.10x** | Support costs (10% uplift), EFA tuning (1 month POC + ongoing debugging) |
| **Silver-tier** (Together/Lambda/Vultr/etc.) | **1.15x** | Goodput loss (60% worse MTBF), longer failure ID/repair, weaker storage |

**Goodput expense as % of TCO**: Gold (TorchPass) = 6.14%, Hyperscaler (Checkpointless) = 10.53%, Silver (checkpoint restart) = 20.91%

### Scenario 2: Multimodal RL Research (2,048 B200 GPUs)

- **Assumptions**: Real-world pricing (Gold 25th percentile vs Hyperscaler 50th), 12TB/GPU storage, no fault tolerance in code, 1-hour async checkpoints
- **Results (3-year TCO multiplier)**:

| Provider Tier | TCO Multiplier | Key Cost Drivers |
|--------------|---------------|-----------------|
| **Gold-tier** | **1.00x** | Baseline |
| **Hyperscaler** | **1.61x** | GPU pricing premium, orchestration software surcharge, storage, setup/debugging |
| **Silver-tier** | **1.15x** | Storage performance, small goodput impact |

**Goodput expense** (no fault tolerance, provider-managed spares): 0.23% – 0.96% — negligible because small jobs (64 GPUs = 3% of cluster) mean individual failures have limited blast radius.

### Scenario 3: Inference Endpoints (512 H200 GPUs)

- **Assumptions**: Single-node jobs (8 GPUs = 1.5% of cluster), modern LLM serving framework with load balancing, no checkpointing needed
- **Results (3-year TCO multiplier)**:

| Provider Tier | TCO Multiplier | Key Cost Drivers |
|--------------|---------------|-----------------|
| **Gold-tier** | **1.00x** | Baseline |
| **Hyperscaler** | **1.59x** | GPU pricing premium, support, orchestration surcharge |
| **Silver-tier** | **~1.00x** | Virtually equal — inference workloads tolerate silver-tier downtime |

**Key insight**: *"Inference providers can find unused capacity from lower tier providers all around the world and use it effectively to serve single-node inference workloads for happy customers."* For inference, **GPU price is the only thing that matters** — cluster reliability differences contribute <0.5% to TCO.

## Provider Tier Characteristics (from SemiAnalysis Testing)

### Gold-Tier (Nebius, Fluidstack, Crusoe)
- Aggressive discounts approaching 25th percentile for large/long-term contracts
- Strong storage performance with volume discounts
- InfiniBand/RoCE performance out-of-the-box, minimal setup
- Free POCs, included 24/7 support with direct-to-engineer access
- Monitoring dashboards + health checks configured by default
- Hot-spare node pools with capacity guarantees

### Hyperscalers (Oracle, Azure, AWS, GCP)
- Volume discounts at 50th-75th percentile (higher for MSA enterprises)
- Poor default storage performance, extra charges for improvements
- Networking requires significant setup and debugging time
- POCs generally not free
- Tiered support with escalating charges (10% → 3% of bill)
- Well-run datacenters, good health checks, capacity guarantees exist

### Silver-Tier Neoclouds (Together, Lambda, Vultr, Voltage Park, Cirrascale, Gcore, Firmus, GMO, Tensorwave)
- Pricing ranges from 25th percentile (low end) to 50th percentile (high end)
- Aggressive discounts can signal low quality
- Storage performance depends on provider's VAST/Weka experience
- InfiniBand/RoCEv2 good out-of-the-box but setup/debugging time lost
- POCs not always free, support included but rarely 24/7
- Monitoring dashboards and health checks usually not configured
- Hot spares available but no capacity guarantees; cold spares typical (rely on OEM for repairs)

## ClusterMAX 2.1 Update (April 2026)

New provider assessments from this article:

| Provider | Status | Key Finding |
|----------|--------|------------|
| **Core42** (UAE/G42) | Pre-Silver | Strong hands-on support, Broadcom Thor-II NICs battle-tested, compliance restrictions limit testing |
| **BitDeer** (Malaysia) | Pre-Silver | Initial GB200 NVL72 testing, IMEX domain configuration challenges, large capacity pipeline |
| **FPT Smart Cloud** (Vietnam) | Blocked → Silver | Strong monitoring (custom DCGM + Loki), but PKey/SAKey security failures exposed other tenants' endpoints |
| **Radiant** (ex-Ori/Brookfield) | Pre-Silver | Similar security issues (PKey/SAKey), NetworkOperator misconfiguration, no automated health checks, targeting Q2 2026 monitoring release |
| **Tatra Supercompute** | Tracked | Slovakia-based |
| **QumulusAI** | Tracked | Texas/Oklahoma |
| **Boostrun** | Tracked | Seattle/Texas/NC |
| **Moonlite** | Tracked | Reseller/operator |
| **Vessl** | Tracked | Korean marketplace |
| **SK Telecom** | Tracked | Korea |
| **BytePlus** | Tracked | ByteDance division |

## Key Takeaways

1. **GPU $/hr is the wrong metric** — TCO depends on 8 cost categories, with goodput being the most invisible but impactful at scale
2. **Training vs Inference have fundamentally different reliability economics** — Training jobs (big, long-running, collective-bound) suffer massively from failures; inference (small, stateless, load-balanced) barely notices
3. **Fault tolerance is still unsolved for training** — All three frameworks have significant tradeoffs (performance overhead, memory overhead, or idle node costs)
4. **Provider quality gap is real and quantified** — Gold-tier vs Silver-tier can differ by 6.14% vs 20.91% in goodput expense alone for large training jobs
5. **The alpha is in operational excellence, not raw hardware** — As SemiAnalysis demonstrates, two providers with the same GPUs at the same price can have 15%+ TCO difference based purely on reliability and support

## Related Concepts
- [[concepts/gpu-cloud-rankings]] — ClusterMAX rating system
- [[entities/semianalysis]] — Research firm behind this framework
- [[concepts/compute-scaling-bottlenecks]] — Physical constraints on AI compute
- [[entities/nvidia]] — GPU manufacturer, DGX Cloud, Dynamo fault-tolerant inference
- [[concepts/mooncake]] — KV cache offloading for fault-tolerant inference
- [[concepts/elastic-ep]] — Fault-tolerant expert parallelism for MoE deployments

## Sources
- SemiAnalysis — "How Much Do GPU Clusters Really Cost?" (April 2026)
- SemiAnalysis ClusterMAX 2.1 Rankings (April 2026) — https://www.clustermax.ai/
- SemiAnalysis GPU Cluster TCO Calculator (free)
- SemiAnalysis Goodput Calculator (free)
- SemiAnalysis GPU Rental Pricing Data Series
- Meta — arXiv:2410.21680v2 (TorchFT paper)
- PyTorch blog on TorchFT
- AWS Checkpointless Training Documentation (December 2025)
- TorchPass Blog from Clockwork.io
