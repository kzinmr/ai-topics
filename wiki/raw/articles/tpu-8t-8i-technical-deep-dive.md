# TPU 8t & TPU 8i Technical Deep Dive Summary

## 🎯 Core Philosophy & Architectural Shift
- **Design Pillars:** Scalability, reliability, and efficiency.
- **Workload Evolution:** Hardware now targets **agentic AI, world models, Mixture-of-Experts (MoEs), and reasoning-heavy architectures** rather than raw FLOPS alone.
- **Dual-System Approach:** Replaces a monolithic design with two specialized chips:
  - `TPU 8t`: Optimized for massive-scale pre-training
  - `TPU 8i`: Optimized for post-training, sampling, serving, and reasoning
- **AI Hypercomputer Integration:** Both systems are core components of Google's integrated supercomputing architecture (hardware + software + networking).
- **Arm Axion CPU Headers:** Eliminates host bottlenecks by handling complex data preprocessing and orchestration, ensuring TPUs remain continuously fed without stalling.

---

## ⚡ TPU 8t: Pre-Training Powerhouse

| Innovation | Technical Impact |
|---|---|
| **SparseCore** | Specialized accelerator for irregular embedding lookups. Offloads data-dependent all-gather/collectives, preventing zero-op bottlenecks common in general-purpose chips. |
| **VPU/MXU Overlap** | Balanced scaling minimizes exposed vector time. Overlaps quantization, softmax, and layernorms with MXU matrix multiplications to keep compute saturated. |
| **Native FP4** | 4-bit floating point doubles MXU throughput, reduces memory bandwidth bottlenecks, and fits larger model layers into local hardware buffers. |
| **Virgo Network** | Flat, two-layer non-blocking fabric with high-radix switches. Delivers **up to 4x DCN bandwidth increase**, deterministic low latency, and connects to Jupiter north-south fabric. |
| **TPUDirect RDMA & Storage** | Bypasses host CPU/DRAM for direct HBM-to-NIC and TPU-to-storage transfers. Integrates with **Managed 10T Lustre** for **10x faster storage access** vs. 7th-gen Ironwood. |
| **Scale & Bandwidth** | Scales to **>1 million chips** in a single cluster (JAX/Pathways). Virgo links **134,000 chips** with **47 Pbps** non-blocking bandwidth, delivering **>1.6M ExaFlops** with near-linear scaling. |

---

## 🧠 TPU 8i: Sampling & Serving Specialist

| Innovation | Technical Impact |
|---|---|
| **Large On-Chip SRAM** | **384 MB** (3x previous gen) hosts larger KV caches entirely on silicon, drastically reducing core idle time during long-context decoding. |
| **Collectives Acceleration Engine (CAE)** | Replaces 4 SparseCores with 2 Tensor Cores + 1 CAE per chip. Accelerates reduction/sync steps for auto-regressive decoding & chain-of-thought. **5x lower on-chip collective latency**. |
| **Boardfly ICI Topology** | Hierarchical high-radix design (Building Block → Group → Pod). Reduces network diameter from **16 hops (torus) to 7 hops** (56% reduction), slashing all-to-all latency critical for MoE/reasoning models. |
| **Scale & Structure** | Up to 1,152 chips per board, 36 groups per pod (1,024 active chips), linked via Optical Circuit Switches (OCS) with a maximum 7-hop latency. |

---

## 📊 Technical Comparison: TPU 8t vs. TPU 8i

| Feature | TPU 8t | TPU 8i |
|---|---|---|
| **Primary Workload** | Large-scale pre-training | Sampling, serving, reasoning |
| **Network Topology** | 3D torus | Boardfly |
| **Specialized Chip Features** | SparseCore & LLM Decoder Engine | CAE (Collectives Acceleration Engine) |
| **HBM Capacity** | 216 GB | 288 GB |
| **On-Chip SRAM (Vmem)** | 128 MB | 384 MB |
| **Peak FP4 PFLOPs** | 12.6 | 10.1 |
| **HBM Bandwidth** | 6,528 GB/s | 8,601 GB/s (~1.3x of TPU 8t) |
| **CPU Header** | Arm Axion | Arm Axion |

---

## 💻 Software & Ecosystem Enablement
- **Pallas & Mosaic:** First-class support for hardware-aware custom kernels in Python. Enables developers to maximize TPU 8i CAE and TPU 8t SparseCore performance.
- **Native PyTorch Preview:** Full support for existing PyTorch models, including Eager Mode, enabling seamless migration to TPUs without code rewrites.
- **Portability:** JAX, PyTorch, and Keras code scales across generations. XLA abstracts topology and CAE synchronization behind the scenes.
- **Full Stack Integration:** Compatible with JAX, PyTorch, vLLM, XLA, and Pathways.

---

## 📈 Performance Leap vs. 7th Gen (Ironwood)
- **Training Price-Performance:** Up to **2.7x improvement** for large-scale training.
- **Inference Price-Performance:** Up to **80% improvement**, particularly for low-latency MoE models.
- **Energy Efficiency:** Up to **2x better performance-per-watt**, critical for sustainable AI scaling.

---

## 📜 Key Quotes & Important Facts

> *"At Google, our TPU design philosophy has always been centered on three pillars: scalability, reliability, and efficiency."*

> *"The rise of agentic AI requires infrastructure that can handle long context windows and complex sequential logic... newer agents are simulating future scenarios, anticipating consequences, and learning through 'imagination' rather than risky trial-and-error."*

---

## Boardfly vs. Torus Network Math

Boardfly topology reduces network diameter from 16 hops (3D torus) to 7 hops — a 56% reduction in all-to-all latency, critical for MoE routing and autoregressive decoding patterns.

---

## Sources
- Google Cloud Blog — TPU 8t & TPU 8i Technical Deep Dive
- Cloud Next 2026 — Google Cloud infrastructure announcements
