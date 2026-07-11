---
title: SambaNova
created: 2026-07-11
updated: 2026-07-11
type: entity
tags:
  - sambanova
  - ai-hardware
  - inference
  - llm-inference
  - company
  - asic
  - data-center
  - startup
  - valuation
sources:
  - raw/articles/2026-07-11_sambanova-about.md
---

# SambaNova

**SambaNova Systems** is an AI infrastructure company that designs and builds custom **RDU (Reconfigurable Dataflow Unit)** chips and integrated systems for the fastest AI inference and fine-tuning. Founded in 2017 by a team of Stanford researchers and industry veterans, SambaNova offers a complete AI platform spanning custom silicon (SN40L RDU), cloud inference APIs (SambaNova Cloud), and enterprise-grade integrated systems (DataScale). The company competes directly with GPU-based providers ([[entities/nvidia|NVIDIA]]) and other custom-silicon inference specialists such as [[entities/cerebras-systems|Cerebras]] and [[entities/groq|Groq]], and is known for delivering the highest tokens-per-second benchmarks on open-source models including Llama, DeepSeek, Mistral, and Qwen.

## Technology: RDU Architecture

### What is an RDU?

The **Reconfigurable Dataflow Unit (RDU)** is SambaNova's custom processor designed specifically for AI workloads. Unlike GPUs, TPUs, and LPUs — each of which uses a fixed hardware execution model — the RDU employs a **reconfigurable dataflow architecture** that adapts its on-chip compute pipeline to the specific dataflow graph of each AI model.

### How RDUs Differ from Other AI Chips

| Architecture | Vendor | Execution Model | Key Characteristic |
|---|---|---|---|
| **GPU** | NVIDIA, AMD | SIMT (Single Instruction, Multiple Threads) | General-purpose parallel compute; high FLOPS but memory-bandwidth bottlenecked for inference |
| **TPU** | Google | Systolic array (matrix multiply focused) | Optimized for dense matmul; less flexible for sparse or irregular workloads |
| **LPU** | Groq | Deterministic single-core TSP | Ultra-low latency via on-chip SRAM; limited model capacity per chip |
| **CS-3 (Wafer-Scale)** | Cerebras | Massive many-core on-wafer | Enormous single-chip throughput; niche physical form factor |
| **RDU** | SambaNova | Reconfigurable dataflow pipeline | Adapts hardware data paths to model graph; balances throughput, flexibility, and efficiency |

### SN40L RDU — Current Generation

The **SN40L** is SambaNova's latest production RDU:

- **Reconfigurable fabric**: On-chip interconnects re-map per-model to match the exact dataflow graph (attention patterns, FFN shapes, routing decisions), eliminating wasteful data movement that occurs on fixed-function hardware
- **Large on-chip memory**: Reduces reliance on off-chip HBM, lowering latency and power consumption
- **Native multi-model support**: A single RDU can be reconfigured for different model architectures without hardware changes — Llama, DeepSeek, Mistral, Qwen, and custom enterprise models all run natively
- **Dataflow compilation**: Models are compiled into hardware dataflow graphs via SambaFlow, SambaNova's software stack, rather than running through a general-purpose instruction set

### Performance Advantage

SambaNova's RDU architecture achieves its speed advantage through **spatial computing**: instead of scheduling operations sequentially through a fixed pipeline (as GPUs do), the RDU spatially maps the entire model graph onto the chip fabric, allowing thousands of operations to execute concurrently in a true dataflow manner. This yields:

- **Higher throughput**: Industry-leading tokens/second on Llama, DeepSeek, Mistral, Qwen open-source models
- **Lower latency per token**: Reduced data movement and on-chip orchestration minimize per-token generation time
- **Better power efficiency**: Less energy wasted on data shuttling and control overhead vs GPU-based inference

## Products

### SambaNova Cloud

SambaNova Cloud is a managed inference API platform offering RDU-powered inference as a service:

- **REST API** compatible with OpenAI SDK for drop-in replacement
- **Model library**: Pre-optimized open-source models including Llama (various sizes), DeepSeek-V3 and R1, Mistral, Qwen, and more
- **High-throughput serving**: Optimized for production workloads requiring sustained high tokens/second under concurrent load
- **Pay-per-token pricing** competitive with GPU cloud providers
- **Agentic AI support**: Low-latency inference suitable for multi-turn agentic workloads where total response time matters

### SambaNova Suite

An enterprise AI platform providing a full-stack solution for organizations building and deploying AI applications:

- End-to-end workflow from data preparation through training/fine-tuning to production inference
- Pre-built AI models and templates for common enterprise use cases
- Integrated MLOps tooling for model lifecycle management
- On-premise, cloud, or hybrid deployment options

### DataScale

SambaNova's integrated systems offering for data center deployment:

- **Rack-scale RDU clusters**: Pre-integrated compute, networking, and storage for enterprise AI infrastructure
- **Turnkey deployment**: Purpose-built appliances that don't require GPU supply chain dependencies
- **Sovereign/private cloud**: Enables organizations to run AI inference entirely within their own infrastructure
- Deployed at **Argonne National Laboratory**, U.S. Department of Energy, and multiple enterprise customers

## Company & Funding

| Detail | Value |
|---|---|
| **Founded** | 2017 |
| **Founders** | Rodrigo Liang (CEO), Kunle Olukotun (Stanford Professor), Chris Ré (Stanford Professor) |
| **Headquarters** | Palo Alto, California |
| **Total Funding** | $1.1B+ |
| **Latest Round** | Series D (2021) at **$5B+ valuation** |
| **Key Investors** | SoftBank Vision Fund 2, Intel Capital, GV (Google Ventures), Walden International, BlackRock, Temasek |
| **Notable Customers** | Argonne National Lab, U.S. Department of Energy, various enterprise accounts |

### Founding Story

SambaNova was founded by a team combining academic research depth with semiconductor industry experience:

- **Kunle Olukotun**: Stanford professor and pioneer in multicore processor architecture; led the Stanford Hydra chip multiprocessor project; his research on domain-specific architectures directly informed the RDU concept
- **Chris Ré**: Stanford professor in machine learning and data systems; MacArthur "Genius Grant" recipient; research on efficient ML systems and weak supervision
- **Rodrigo Liang**: CEO with prior leadership roles at Oracle and Sun Microsystems; semiconductor and enterprise systems background

## Competitive Positioning

SambaNova operates at the intersection of three competitive forces reshaping the AI inference market:

### vs. Cerebras (Wafer-Scale)

Both SambaNova and [[entities/cerebras-systems|Cerebras]] challenge NVIDIA's GPU dominance with custom silicon, but take fundamentally different approaches:

- **SambaNova (RDU)**: Reconfigurable dataflow — moderate chip size, adapts fabric per-model
- **Cerebras (CS-3)**: Wafer-scale integration — enormous single chip (entire silicon wafer), massive parallelism
- **Trade-off**: Cerebras offers raw throughput for the largest models; SambaNova emphasizes efficiency, flexibility, and deployment practicality across more model architectures

### vs. Groq (LPU)

[[entities/groq|Groq]] is SambaNova's closest architectural comparator:

- Both use custom ASICs designed specifically for inference (not repurposed GPUs)
- Both emphasize deterministic, low-latency execution
- **Key difference**: Groq's LPU is a fixed, deterministic single-core architecture focused on minimal latency; SambaNova's RDU is reconfigurable, adapting to each model's optimal dataflow
- **Ecosystem**: Groq has a larger developer cloud presence (GroqCloud); SambaNova targets enterprise and national lab deployments with integrated systems

### vs. NVIDIA (GPU)

[[entities/nvidia|NVIDIA]] dominates the AI compute market with general-purpose GPUs:

- NVIDIA's strength is ecosystem breadth — training, inference, CUDA software stack, and massive installed base
- SambaNova competes on **inference efficiency**: purpose-built silicon that delivers more tokens/second/watt than GPUs
- Enterprise customers seeking independence from GPU supply constraints and lower inference TCO are the primary SambaNova target

### Market Position Summary

| Dimension | SambaNova (RDU) | Cerebras (CS-3) | Groq (LPU) | NVIDIA (GPU) |
|---|---|---|---|---|
| **Architecture** | Reconfigurable dataflow | Wafer-scale many-core | Deterministic TSP | SIMT GPU |
| **Inference speed** | Very high | Very high | Ultra-low latency | Moderate-high |
| **Model flexibility** | High (reconfigurable) | Moderate | Moderate | Highest (general-purpose) |
| **Training capability** | Fine-tuning only | Limited | Minimal | Full training |
| **Deployment model** | Cloud + on-prem | Cloud + on-prem | Cloud + on-prem | Universal |
| **Ecosystem maturity** | Growing | Growing | Growing | Dominant |

## Related Pages

- [[entities/cerebras-systems]] — Wafer-scale AI compute (primary competitor)
- [[entities/groq]] — LPU-based inference (architecture competitor)
- [[entities/nvidia]] — GPU-based AI infrastructure (dominant incumbent)
- [[concepts/inference-hardware]] — Landscape of AI accelerator hardware
- [[concepts/llm-inference]] — Overview of LLM inference techniques and infrastructure
- [[entities/groq]] — Language Processing Unit architecture (Groq's approach, for comparison)
- [[concepts/inference-hardware]] — Inference-specific hardware design patterns
- [[concepts/inference]] — Landscape of LLM inference runtimes
