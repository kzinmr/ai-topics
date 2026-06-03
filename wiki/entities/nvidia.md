---
title: NVIDIA
created: 2026-04-26
updated: 2026-06-03
type: entity
tags: [company, platform]
sources: [raw/articles/2026-05-20_nvidia-nemotron-labs-diffusion.md,
  - raw/newsletters/2026-05-22-nvidia-s-ai-factory-boom-hits-81-6b.md,
  - raw/articles/2026-04-25-nvidia-dynamo-agentic-inference.md
  - raw/articles/2026-01-05_nvidia_vera-rubin-platform.md
  - https://www.tomshardware.com/tech-industry/artificial-intelligence/jensen-says-nvidia-now-has-zero-percent-market-share-in-china
  - raw/articles/2026-05-20_nvidia-nemotron-labs-diffusion.md
  - raw/articles/substack.com--redirect-fc937db9-1f9f-4d17-8d14-568f58e27526--f7737c4f.md
  - https://github.com/nvidia/skillspector
---

# NVIDIA Corporation

NVIDIA is a semiconductor and AI infrastructure company. In the context of this wiki, NVIDIA is significant for:

### Nemotron-Labs-Diffusion: Tri-Mode Language Model (May 2026)

NVIDIA released Nemotron-Labs-Diffusion, a language model family (3B, 8B, 14B) that unifies **autoregressive (AR) decoding, diffusion-based parallel decoding, and self-speculation decoding** in a single set of weights. The same model switches modes at inference time by changing the attention pattern.

- **Training**: Joint AR-diffusion objective on top of pretrained Ministral3 models, 256 H100 GPUs. Stage 1 (1T tokens pure AR) → Stage 2 (300B tokens joint objective)
- **Three decoding modes**:
  1. **AR Decoding**: Standard causal left-to-right, best for high-concurrency cloud serving
  2. **Diffusion Decoding**: Parallel denoising within fixed-length blocks (32 tokens), bidirectional attention inside block
  3. **Self-Speculation**: Diffusion pathway drafts k candidates → AR verifies longest contiguous prefix. 5.99× TPF (8B linear) and 6.38× TPF (quadratic)
- **Performance**: NLD-8B Self-Spec achieves 62.81% avg accuracy at 5.99× tokens/forward vs Qwen3-8B's 62.75% at 1× TPF
- **License**: NVIDIA Nemotron Open Model License
- **Availability**: Hugging Face `nvidia/Nemotron-Labs-Diffusion-{size}` (3B, 8B, 14B Base/Instruct/Vision-Language variants)

This complements [[concepts/nvidia-vera-rubin]] by demonstrating NVIDIA's focus on novel inference-time architectures alongside system-level integration.


## Key Products & Initiatives

### Vera Rubin Platform (2026)
- Rack-scale AI supercomputer: **6 new chips** (GPU, CPU, switch, NIC, DPU, fabric) in one unified system
- **Extreme co-design**: GPUs, CPUs, networking, security, software, power, cooling architected as one system
- Core thesis: the **data center is the unit of compute** — bottlenecks have shifted from FLOPS to bandwidth, interconnect, and system integration
- **Vera CPU**: 88 custom Olympus cores, 1.2 TB/s memory bandwidth, Spatial Multithreading
- **Rubin GPU**: 336B transistors, 288GB HBM4, 22 TB/s bandwidth, 50 PFLOPS NVFP4 inference
- **NVLink 6**: 3.6 TB/s GPU-to-GPU, full all-to-all topology across 72 GPUs
- **BlueField-4 DPU**: 64-core Grace CPU offloads infrastructure (networking, storage, security)
- **ICMS** (Inference Context Memory Storage): Pod-level flash tier for KV-cache → 5× tokens/sec improvement
- **DGX SuperPOD**: 8× NVL72 racks as validated AI factory deployment unit
- Training: 10T MoE model with **¼ the GPUs** vs Blackwell; Inference: **10× lower cost per token**
- See: [[concepts/nvidia-vera-rubin]]

### NVIDIA Dynamo
- Inference architecture designed for agentic coding workloads
- Three-plane architecture: Request, Control, Storage & Events
- Key components: Planner, Router, [[concepts/kv-aware-routing]], KVBM, NIXL
- Addresses KV recomputation waste and memory pressure in agentic contexts

### GPU Hardware
- Foundation for local AI inference and training
- Connects to [[inference-hardware]] and [[dgx-spark-local-llm-server]]

## Recent Activity (April—May 2026)
- Published Dynamo architecture documentation for agentic inference
- Tweet about agentic coding bottlenecks received 454 bookmarks
- **Nemotron 3 Nano Omni** — Released April 2026. 30B parameters, 256K context length. Open multimodal model with leading accuracy and highest efficiency in the Nemotron family. Tweet received 471 bookmarks, 1149 likes, 393K impressions.
- **China market share drops to 0%** — Jensen Huang confirms at Citadel Securities event (May 2026). From 95% to 0% share of China's AI accelerator market. Citing US export policy as "already largely backfired." $4.5B in charges in Q1 FY2026. 10-K filing warns of "material and adverse impact" from effective foreclosure from China. Huawei Ascend, Cambricon, Moore Threads filling the gap.


### Q1 FY2027 Earnings: $81.6B Revenue, AI Infrastructure Era (May 2026)

NVIDIA reported Q1 FY2027 results with record AI infrastructure revenue:

| Metric | Value | Growth |
|--------|-------|--------|
| Revenue | **$81.6B** | +85% YoY, +20% sequential |
| Data Center Revenue | **$75.2B** | +92% YoY |
| Q2 Guidance | **~$91B** | ±2%, assumes zero China DC compute revenue |
| Share Repurchase Authorization | **$80B** added | — |

**Segment Restructuring**: NVIDIA reorganized reporting into:
- **Data Center — Hyperscale**: Large cloud providers
- **Data Center — ACIE** (AI Compute Infrastructure & Edge): Enterprise AI deployments
- **Edge Computing**: IoT, robotics, autonomous systems

**Jensen Huang**: *"The largest infrastructure expansion in human history."*

**China exposure**: Revenue assumed to be $0 on the compute side due to export restrictions, though the 10-K filing warns of "material and adverse impact" from effective foreclosure from the Chinese market. [[concepts/nvidia-vera-rubin]] and [[entities/nvidia]] overall strategy now focuses on AI factory-scale deployments worldwide.

## Nemotron Open Model Strategy

Led by [[entities/bryan-catanzaro|Bryan Catanzaro]] (VP Applied Deep Learning Research), NVIDIA's Nemotron effort represents a unique open model strategy:

### "AI as Infrastructure" Thesis
NVIDIA views AI as foundational infrastructure — like the internet — that should be openly developed so organizations across every sector can customize it for their specific needs.

### Two Jobs of Nemotron
1. **Systems R&D** — Understanding AI workloads to design better NVIDIA hardware (GPUs, interconnects, memory). The expensive experimentation justifies internal investment.
2. **Ecosystem Support** — Enabling broader AI ecosystem growth drives NVIDIA's business. "Whenever AI is able to grow in any sort of direction, that's an opportunity for us to grow our business."

### Organizational Scale
- **~500 full-time** technical staff on Nemotron technologies
- **~2,000 interested** contributors across NVIDIA
- Decentralized "volunteer" culture with "Pilot in Command" structure for 20 project areas

### Open Dataset Releases (2025)
NVIDIA releases pretraining datasets (CC-v2, CC-Math-v1, Code-v2, Specialized-v1) taking on legal risk that few other companies accept. They also release post-training recipes and NeMo Gym RLVR datasets.

### "Intelligence per Second" Philosophy
Catanzaro's prediction: models that optimize for compute acceleration (intelligence per unit time) will win because they train on more data, get more post-training cycles, and iterate faster during deployment.


### NeMo Agent Toolkit v1.7.0 (May 2026)

NVIDIA released **NeMo Agent Toolkit v1.7.0** with notable new features:

| Feature | Description |
|---------|-------------|
| **AI coding agent skills** | New coding agent capabilities integrated into the toolkit |
| **ATOF v0.1** | Agentic Trajectory Observability Format — aligned specification for agent trace data |
| **Arize AX OTLP exporter** | OpenTelemetry protocol exporter for Arize AI observability |
| **Token streaming** | Streaming support for ReAct Agent |
| **Exa Search API** | Internet search tool integration |
| **ATIF trajectory exporter** | Phoenix visualization support for agent trajectories |
| **Consent-gated telemetry** | Runtime telemetry for NAT CLI commands (privacy-first) |

**Breaking changes**: OpenAI dependency migration 1.x→2.x; removed optuna, chain, openinference from core; removed nvidia-nat-vanna package.

Source: raw/articles/2026-05-27_nemo-agent-toolkit-v1-7-0.md

### NVIDIA SkillSpector

NVIDIA released **SkillSpector**, an open-source tool for inspecting AI agent skills:
- Open-source tool for **inspecting, defining, validating, and testing** AI agent skill definitions
- Available at [https://github.com/nvidia/skillspector](https://github.com/nvidia/skillspector) (note: 'skillspector' in the GitHub repo name is intentional)
- Allows developers to define schemas, validate skill implementations, and test agent skill definitions against expected behavior

### RTX Spark (Windows PC AI Agent Platform)

NVIDIA and **Microsoft** announced **RTX Spark**, a Windows PC AI agent platform:
- Enables AI agents to run **locally on Windows PCs** with NVIDIA RTX acceleration
- Essentially a **Windows-based local agent runtime** for AI agents
- Brings local AI agent capabilities to the Windows ecosystem, leveraging RTX GPUs for inference

## Related

- [[entities/bryan-catanzaro]] — VP Applied Deep Learning Research, leads Nemotron open model effort
- [[entities/nvidia-nemotron-3-nano-omni]] — Nemotron 3 Nano Omni multimodal model
- [[entities/nvidia-nemotron-labs-diffusion]] — Nemotron-Labs-Diffusion tri-mode language model
- [[entities/nemotron-cascade-2]] — Nemotron Cascade 2 model
- [[concepts/nvidia-vera-rubin]]
- [[concepts/nvidia-dynamo]]
- [[concepts/kv-aware-routing]]
- [[concepts/inference]]
- [[inference-hardware]]
- [[dgx-spark-local-llm-server]]
