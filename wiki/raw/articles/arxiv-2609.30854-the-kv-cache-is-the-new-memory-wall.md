---
source_url: https://arxiv.org/abs/2609.30854
ingested: 2026-09-30
sha256: 50438e6588d90d716cfaa448a3180d2653c0e8702975087e180d867604064b85
---

# The KV Cache Is the New Memory Wall

**arXiv:** 2609.30854v1  
**Published:** 2026-09-25  
**Primary category:** cs.DC  
**Authors:** Tejinder Singh

## Abstract

Autoregressive LLM inference at long context is bounded by memory bandwidth, not arithmetic throughput, and the binding resource shifts from model weights to the Key-Value (KV) cache as sequence length grows. For Llama-3-70B in BF16, the 140 GB weight footprint exceeds the 80 GB HBM of a single accelerator, and one 128k-token sequence adds 42 GB of KV cache. Techniques that compress, evict, page, share, or offload KV state have proliferated, but reported gains use inconsistent workloads, hardware, and quality metrics, preventing cross-paper comparison. This SoK paper unifies the field analytically, with a protocol that strictly separates derived and reported claims. We derive closed-form arithmetic intensity as a decaying function of context length, parameterized by hardware topology for NVIDIA H100, NVIDIA B200, and AMD MI300X, including per-die bandwidth partitioning and the crossover lengths where KV traffic overtakes weight traffic. We classify the literature into five domains, quantization, token eviction, KV paging, prefix caching, and heterogeneous tiering, evaluating one method per domain at 128k context under a single protocol. The central finding is a three-regime structure: below a hardware-specific crossover, weight traffic dominates and KV compression yields negligible speedup; beyond it, KV traffic dominates and each domain trades quality for bandwidth savings approaching the roofline bound. Paging and prefix sharing are lossless but address capacity, not bandwidth. Quantization and eviction cut bandwidth directly, with degradation that accelerates below 4-bit precision and turns discontinuous for eviction on position-sensitive tasks. Tiering converts the bandwidth wall into an interconnect problem bounded by PCIe or NVLink rather than HBM. We close with design rules for selecting a compression domain given hardware, context length, and quality budget.
