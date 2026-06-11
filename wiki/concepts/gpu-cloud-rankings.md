---
title: "GPU Cloud Infrastructure Rankings (ClusterMAX)"
type: concept
created: 2026-05-20
updated: 2026-05-29
tags:
  - hardware
  - infrastructure
  - nvidia
  - lab
related:
  - [[entities/semianalysis]]
  - [[entities/dylan-patel]]
  - [[entities/coreweave]]
  - [[concepts/compute-scaling-bottlenecks]]
  - [[concepts/gpu-cluster-tco-goodput]]
sources:
  - raw/articles/2026-05-20_semianalysis_clustermax-2-gpu-cloud-ratings.md
  - raw/articles/substack.com--app-link-post--1509e963.md
  - https://semianalysis.com/p/clustermax-2-0-gpu-cloud-ratings
  - https://www.clustermax.ai/
---

# GPU Cloud Infrastructure Rankings (ClusterMAX)

The systematic evaluation and ranking of GPU cloud providers ("Neoclouds") based on hands-on technical testing across multiple criteria. Established by SemiAnalysis as the industry's independent benchmark for GPU cloud quality, beyond raw $/GPU-hr pricing.

## ClusterMAX Rating System

SemiAnalysis's ClusterMAX evaluates GPU cloud providers across **10 primary criteria**:
- **Security** (SOC2/ISO attestation, multi-tenant isolation, container escapes, embargo programs)
- **Lifecycle** (onboarding, cluster creation, expansion, ease of use, support)
- **Orchestration** (SLURM, Kubernetes, RBAC, IAM/SSO, defaults)
- **Storage** (POSIX filesystems, S3-compatible object storage, caching)
- **Networking** (InfiniBand/RoCEv2, NCCL bandwidth, SHARP, straggler detection)
- **Reliability** (hardware SLAs, health checks, link flapping, filesystem stability)
- **Monitoring** (Grafana dashboards, DCGM metrics, alerting, job stats)
- **Pricing** (consumption models, bundled vs itemized, expansion)
- **Partnerships** (NVIDIA/AMD investment, certifications, SchedMD, ecosystem)
- **Availability** (GPU quantity, on-demand capacity, latest models, roadmap)

**Rating tiers**: Platinum (best-in-class, commands premium pricing) → Gold → Silver → Bronze → Not Recommended (Underperforming/Unavailable)

## ClusterMAX 2.0 Rankings (November 2025)

| Tier | Provider | Notes |
|------|----------|-------|
| **Platinum** | CoreWeave | Only Platinum member. Commands 10-15% pricing premium. $22.4B OpenAI commitment. $14.2B Meta deal. Acquired Weights & Biases + OpenPipe. |
| **Gold** | Nebius | KubeVirt virtualized stack. Soperator (open source Slurm-on-K8s). $17.4B Microsoft deal. On-demand/autoscaling strength. |
| **Gold** | Oracle | Only hyperscaler without in-house AGI research. $300B+ OpenAI deal. 60%+ US Stargate. Strong customer support. |
| **Gold** | Azure | OpenAI anchor tenant. Best InfiniBand + SHARP among hyperscalers. CycleCloud needs improvement. |
| **Gold** | Fluidstack | Unique aggregator model. "Forward Deployed Engineering" ethos. Gold-terawulf/Cipher deals backstopped by Google. |
| **Gold** | Crusoe | Crypto-to-AI pivot. Crusoe Spark (Digital Flare Mitigation). 3.4GW datacenter footprint. |
| **Silver** | Google | TPU + Trainium in arena. Strong managed cluster experience. |
| **Silver** | AWS | Massive capacity, improving managed experience. |
| **Silver** | together.ai | Strong clusters, held back by reliability complaints. TKC kernel innovation (Tri Dao). |
| **Silver** | Lambda | Top on-demand GPU provider. Customer complaints about product confusion. |
| **Bronze+** | 37 total clouds | Includes providers worldwide at Bronze and Silver tiers. |

*Market view expanded to 209 total providers (from 169 in v1.0, 124 in original Neocloud Playbook). Based on interviews with 140+ end users.*

## Key Industry Trends (ClusterMAX 2.0)

### Slurm-on-Kubernetes Convergence
Three competing implementations emerged:
- **SUNK (CoreWeave)**: Proprietary, first-to-market. Hybrid scheduler co-locating SLURM + K8s jobs on same cluster. Custom Go rewrite of SLURM REST API. RPC-based login pod controller.
- **Soperator (Nebius)**: Open source. KubeVirt VM-based Slurm-on-K8s. Declarative SlurmCluster CRD. GPU/IB passthrough to VMs for bare-metal-equivalent performance.
- **Slinky (SchedMD)**: Official SLURM creators' K8s operator. Broken out-of-the-box (missing vim, git, python, sudo in login pods). Adoption by Voltage Park, GCORE.

### Bare Metal vs Virtualization
- **CoreWeave/Oracle**: Bare metal first. Use NVIDIA BlueField DPUs for network isolation (VPCs, encryption, NAT offload).
- **Nebius/Crusoe**: Lightweight VMs (KubeVirt/cloud-hypervisor). Rapid provisioning, stateful snapshots, shared storage. Nebius achieved bare-metal-class performance per MLPerf testing.

### GB200 NVL72 Reliability Crisis
- Single faulty component requires draining entire 72-GPU rack
- NVIDIA firmware bug (v1.3, released 6-7 months late) caused NVLink sync loss
- Top providers offering 99% rack-level uptime guarantees with penalties
- Provisioning replacement racks takes 9 hours to multiple days
- Diurnal 1-2% throughput variation based on time-of-day (thermal effects)

### Container Escape Vulnerabilities
- **NVIDIAScape (CVE-2025-23266)**: 3-line script escapes container to root on host. Effective on dozens of providers with outdated nvidia-container-toolkit (<1.17.8).
- AMD ecosystem historically lacked robust container runtime security
- NVIDIA/AMD now running formal security embargo programs for Neocloud partners

### InfiniBand Security Gaps
- PKeys (Partition Keys) alone are insufficient for multi-tenant isolation
- Compromised tenants can send malicious Subnet Management Packets (SMPs)
- Proper setup requires: M_Key, P_Key, SA_Key, VS_Key, C_Key, N2N_Key, AM_Key
- Many providers misconfigure or omit these layers entirely

### Crypto Miners → AI Cloud Pivot
- Terawulf, Cipher Mining, IREN/Iris Energy, Hut 8/Highrise, BitDeer, Applied Digital, Core Scientific (acquired by CoreWeave)
- IREN scored 200MW GB300 deal with Microsoft at Childress, TX campus
- Two models: Powered Shell/Colocation (rent DC space) vs Wholesale Bare-Metal (procure GPUs, offer cloud)

### NVIDIA's $2.1B Acquisition Spree
- run:ai (orchestration, May 2024, $700M)
- deci (inference optimization, May 2024, $300M)
- shoreline.io (hardware remediation, July 2024, $100M)
- brev.dev (cloud dev machines, July 2024, ~$100M)
- Lepton (clusters/orchestration/monitoring, April 2025, ~$900M)

NVIDIA's DGX Cloud Lepton criticized as BYOC-only marketplace with no pre-registered clouds. Most acquisitions bundled but not open-sourced despite community expectations.

### AMD Cloud Quality Gap
Providers offering both AMD and NVIDIA consistently have worse AMD cloud quality:
- Missing monitoring, health checks, working SLURM support
- Crusoe and Oracle both show degraded AMD experiences vs NVIDIA

## CoreWeave Deep Dive (Platinum Standard)

### Security Architecture
- Zero-trust, defense-in-depth with continuous audits
- Host-to-BMC Access disabled (KCS + RNDIS interfaces)
- Dynamic jumpbox with DPU ACL-based tenant isolation
- ChainGuard base images for all customer containers
- SPDM-based firmware attestation, Secure Boot, Measured Boot
- Teleport for privileged access with TPM-backed node joins
- No multi-tenant co-location on same machine; PXE boot to clean state between tenants

### Monitoring & Health Checks (Industry Standard)
- Custom NVML-based exporters (standard DCGM insufficient)
- Interconnect fabric correlation engine for transient physical-layer problems
- Simultaneous thermal expansion testing across GPUs and interconnect
- Automatic root-cause analysis via XID/SXID error correlation

### Storage
- **CAIOS** (CoreWeave AI Object Storage): Native S3-compatible object storage
- **LOTA** (Local Object Transfer Accelerator): Transparent distributed cache on local NVMe per GPU node. 7GB/s sustained throughput per GPU on Blackwell.
- Storage typically <5% of cluster TCO, but rising to 20%+ for data-heavy workloads (video generation, drug discovery, robotics)

### Support Model
- "Direct to expert" — no tiered support escalation
- All datacenter technicians are CoreWeave employees with equity
- ClearFeed Slack notifications for operational status (including company offsites)

## Nebius Deep Dive (Gold — CoreWeave's Direct Competitor)

- KubeVirt layers: customer VMs → internal K8s → management K8s
- 197TB shared root filesystem via virtio-fs (no 197TB physical drives)
- YDB underpins block, shared, and storage offerings
- Container startup: 10 min → 2-3 min
- Soperator roadmap is public on GitHub — unique transparency in Neocloud space
- Pre-emptible/spot instances for inference workloads
- $17.4B Microsoft deal (Vineland, NJ datacenter), expanding to $19.4B
- Russian origins noted as customer perception challenge despite all staff based outside Russia

## Kubernetes Training Tool Ecosystem

| Tool | Type | Description |
|------|------|-------------|
| **Kueue** | CRD | Job queues + user quotas. Works with default K8s scheduler. |
| **Volcano** | Custom Scheduler | Gang scheduling, job dependencies. Works with Kueue. |
| **PyTorchJob** | Operator/CRD | Lifecycle management of PyTorch jobs (KubeFlow). |
| **MPIOperator** | Operator/CRD | MPI job lifecycle management (KubeFlow). |
| **Jobset** | CRD | General-purpose gang-scheduled jobs (Google). Growing adoption. |
| **Trainy** | Platform | Simplifies job submission (paid product). |
| **dstack** | Platform | Simplifies job submission (open source + enterprise). |
| **SkyPilot** | Platform | Simplifies job submission (open source, fast adoption). |

**Expected consolidation**: Jobset + Kueue (OSS), Volcano (large batch/gang scheduling), SkyPilot (multi-cloud).

## ClusterMAX Quick Benchmarks (Proxy Tests)

| Test | What It Reveals | Best (Platinum) | Median | Worst (Bronze) |
|------|----------------|----------------|--------|----------------|
| `pip install torch` | WAN connection + small file I/O | ~3.2s (uv) | ~8.5s | 41.2s |
| NGC container pull (22GB) | Peering + local caching | <10s (CoreWeave mirror) | 45-60s | 4+ min |
| `import torch` cold start | Driver init + lib loading | ~1.8s | ~1.8s | 8-10s |
| Download phi-4 (15B) from HF | Sustained WAN throughput | ~20s (6+ Gbps) | ~35s (3.4 Gbps) | significantly slower |
| Load phi-4 to GPU memory | Local data path (NVMe→GPU) | ~12s | ~12s | slower |

## Industry Quotes on ClusterMAX

> "ClusterMAX has become a valuable tool for making data-driven decisions about where and how we deploy compute." — Peter Hoeschele, GM of OpenAI Stargate

> "ClusterMAX is delivering a comprehensive rating system that the industry can rely on." — Santosh Janardhan, Head of Global Infrastructure at Meta

> "ClusterMAX has become the go-to benchmark for GPU clouds." — Hunter Almgren, Distinguished Technologist, HPE

> "ClusterMAX is the industry standard for evaluating GPU cloud providers." — Gavin Baker, Managing Partner, Atreides Management

## Related Concepts
- [[concepts/compute-scaling-bottlenecks]] — Dylan Patel's framework on physical constraints
- [[concepts/gpu-cluster-tco-goodput]] — TCO framework with Goodput Expense methodology
- [[entities/nvidia]] — GPU manufacturer, DGX Cloud strategy
- [[entities/coreweave]] — Platinum-tier GPU cloud provider
- [[entities/nebius]] — Gold-tier GPU cloud, KubeVirt architecture
- [[concepts/kubernetes]] — Container orchestration for AI workloads
- [[concepts/slurm]] — HPC job scheduler, Slurm-on-K8s trend
- [[concepts/training-infra]] — Broader infrastructure practices

## Sources
- [[entities/semianalysis]] — "ClusterMAX 2.0: The Industry Standard GPU Cloud Rating System" (November 2025, 46,000+ words)
- https://www.clustermax.ai/ — Live ClusterMAX ratings and criteria
- https://www.clustermax.ai/criteria — Itemized testing criteria
- https://www.clustermax.ai/expectations/health-checks — Health check standards
- https://www.clustermax.ai/monitoring — Monitoring criteria
- https://www.clustermax.ai/quotes — Community quotes
- ClusterMAX 2.0 article, SemiAnalysis (November 2025)
