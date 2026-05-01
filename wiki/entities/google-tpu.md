---
title: Google TPU — Tensor Processing Units
type: entity
aliases: [tpu, google-tpu, tpu-v8, tpu-8t, tpu-8i, tpu-ironwood]
created: 2026-04-23
updated: 2026-04-28
tags: [entity, hardware, google, training, inference]
sources:
  - https://cloud.google.com/blog/products/compute/tpu-v8-tensor-processing-unit-cloud-next-2026
  - https://substack.com/redirect/394ee21a-c362-4fb3-adf3-c39eb79ee333
---

# Google TPU — Tensor Processing Units

Google's custom ASIC for ML workloads, now split into specialized **TPU 8t** (training) and **TPU 8i** (inference) chips at the 8th generation. Designed for agentic AI, world models, Mixture-of-Experts (MoEs), and reasoning-heavy architectures.

## Architecture Philosophy

Google's TPU design centers on three pillars: **scalability, reliability, and efficiency**. The 8th generation marks a fundamental shift from monolithic design to **dual-system specialization** — separating training and inference workloads into purpose-built chips.

## 8th Generation: TPU 8t & TPU 8i

### TPU 8t — Pre-Training Powerhouse

| Feature | Specification |
|---------|---------------|
| **Primary Workload** | Massive-scale pre-training |
| **SparseCore** | Specialized accelerator for irregular embedding lookups; offloads data-dependent all-gather/collectives |
| **VPU/MXU Overlap** | Balanced scaling; overlaps quantization, softmax, layernorms with MXU matrix multiplications |
| **Native FP4** | 4-bit floating point doubles MXU throughput, reduces memory bandwidth bottlenecks |
| **Virgo Network** | Flat, two-layer non-blocking fabric with high-radix switches; up to 4x DCN bandwidth increase |
| **TPUDirect RDMA** | Bypasses host CPU/DRAM for direct HBM-to-NIC and TPU-to-storage transfers |
| **HBM Capacity** | 216 GB |
| **On-Chip SRAM** | 128 MB |
| **Peak FP4 PFLOPs** | 12.6 |
| **HBM Bandwidth** | 6,528 GB/s |

**Scale**: Links 134,000 chips with 47 Pbps non-blocking bandwidth; scales to **>1 million chips** in a single cluster (JAX/Pathways); delivers >1.6M ExaFlops with near-linear scaling.

### TPU 8i — Sampling & Serving Specialist

| Feature | Specification |
|---------|---------------|
| **Primary Workload** | Post-training, sampling, serving, reasoning |
| **Large On-Chip SRAM** | 384 MB (3x previous gen) — hosts larger KV caches entirely on silicon |
| **CAE** | Collectives Acceleration Engine — replaces 4 SparseCores with 2 Tensor Cores + 1 CAE; 5x lower on-chip collective latency |
| **Boardfly ICI Topology** | Hierarchical high-radix design; reduces network diameter from 16 hops (torus) to 7 hops (56% reduction) |
| **HBM Capacity** | 288 GB |
| **On-Chip SRAM** | 384 MB |
| **Peak FP4 PFLOPs** | 10.1 |
| **HBM Bandwidth** | 8,601 GB/s (~1.3x of TPU 8t) |

**Scale**: Up to 1,152 chips per board, 36 groups per pod (1,024 active chips), linked via Optical Circuit Switches (OCS) with maximum 7-hop latency. Google claims scalability to **1M TPUs in a single cluster**.

## Technical Comparison: TPU 8t vs TPU 8i

| Feature | TPU 8t | TPU 8i |
|---------|--------|--------|
| **Network Topology** | 3D torus (Virgo) | Boardfly |
| **Specialized Chips** | SparseCore & LLM Decoder Engine | CAE (Collectives Acceleration Engine) |
| **CPU Header** | Arm Axion | Arm Axion |
| **Storage** | Managed 10T Lustre (10x faster than Ironwood) | — |
| **Key Innovation** | SparseCore for embedding lookups | CAE for autoregressive decoding |

## Evolution: From Ironwood to TPU v8

| Generation | Codename | Key Characteristic |
|------------|----------|-------------------|
| 7th gen | Ironwood | Monolithic design, last unified TPU |
| 8th gen | — | Split into TPU 8t (training) + TPU 8i (inference) |

### Performance Leap vs. Ironwood (7th Gen)
- **Training price-performance**: Up to **2.7x improvement**
- **Inference price-performance**: Up to **80% improvement** (especially low-latency MoE)
- **Energy efficiency**: Up to **2x better performance-per-watt**

## Software Ecosystem

- **JAX & Pathways**: Primary framework; full support for scaling to million-chip clusters
- **PyTorch**: Native PyTorch preview with Eager Mode support — no code rewrites needed
- **Pallas & Mosaic**: Hardware-aware custom kernels in Python
- **vLLM, XLA**: Compatible with major inference frameworks
- **Portability**: JAX, PyTorch, and Keras code scales across generations; XLA abstracts topology and CAE synchronization

## Agentic AI Alignment

Google's 8th generation explicitly targets agentic AI workloads:

> *"The rise of agentic AI requires infrastructure that can handle long context windows and complex sequential logic... newer agents are simulating future scenarios, anticipating consequences, and learning through 'imagination' rather than risky trial-and-error."*

Key design choices for agentic workloads:
- TPU 8i's large SRAM (384 MB) for long-context KV caching
- CAE for autoregressive decoding (chain-of-thought, multi-turn agents)
- Boardfly topology for MoE routing in reasoning models
- TPU 8i supports 1,152 TPUs/pod for low-latency, high-throughput multi-agent workloads

## Integration with Google Cloud AI Stack

TPU 8t/8i are core components of Google's **AI Hypercomputer** architecture — integrating hardware, software, networking, and enterprise control planes:

- **Vertex AI / Gemini Enterprise Agent Platform**: Agent Studio, 200+ models via Model Garden
- **Gemini 3.1 Pro/Flash Image, Lyria 3, Gemma 4**: Native TPU support
- **Workspace Intelligence**: Semantic layer over Google Workspace, powered by Gemini Embedding 2 GA

## Related

- [[nvidia-dgx-spark]] — NVIDIA's competitor in local AI compute
- [[concepts/inference-hardware]] — GPU and accelerator landscape
- [[google-tpu]] — Google's broader AI infrastructure
- [[concepts/gemini]] — Google's Gemini model family
- [[openai]] — OpenAI's competing infrastructure approaches
- [[concepts/claude-memory]] — Anthropic's approach (competitor context)


## April 2028 Deep Dive Updates

### Architecture Philosophy Evolution
The eighth generation's dual-system specialization (8t for training, 8i for inference) represents a fundamental departure from previous monolithic TPU designs. Key insights from the technical deep dive:

1. **Workload Separation Rationale**: Training workloads benefit from massive parallelism and regular compute patterns, while inference/sampling requires handling long context windows, MoE routing, and low-latency responses.

2. **Network Topology Choice**: TPU 8t uses Virgo (flat 2-layer non-blocking) for scale-out training efficiency, while TPU 8i uses Boardfly (hierarchical high-radix) for inference latency optimization.

3. **CAE Impact**: The Collectives Acceleration Engine reduces on-chip collective latency by 5x, which is critical for autoregressive decoding in reasoning models.

4. **SparseCore Purpose**: Designed specifically for embedding lookup operations common in recommendation systems and MoE architectures.

### Performance Benchmarks
- Training: 2.7x price-performance improvement over 7th gen Ironwood
- Inference: 80% improvement for MoE models at low-latency targets
- Energy: 2x better performance-per-watt across both chips

## Sources

-  — Google Cloud Blog, Cloud Next 2026-  — AINews #21, Latent.Space

## References

- tpu-8t-8i-technical-deep-dive
