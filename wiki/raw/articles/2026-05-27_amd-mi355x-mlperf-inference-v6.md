# AMD Instinct MI355X MLPerf Inference v6.0 Results

**Source:** AMD ROCm Blogs
**Date:** April 1, 2026
**URL:** https://rocm.blogs.amd.com/artificial-intelligence/mlperf-inference-v6.0/README.html

## Summary

AMD MLPerf Inference v6.0 submission with MI355X:
- Surpassed 1M tok/s at cluster scale (Llama 2 70B, GPT-OSS-120B)
- Single-node vs B200: tied in Offline, 97% in Server, 119% in Interactive (Llama 2 70B)
- Single-node vs B300: 92% Offline, 93% Server, 104% Interactive
- GPT-OSS-120B: 115% of B200 Server, 111% of B200 Offline
- Scale-out efficiency: 92-98% across multi-node configurations
- First MLPerf heterogeneous submission (MI300X + MI325X + MI355X)
- 3.1× performance increase over MI325X (FP4 quantization)
- New workloads: GPT-OSS-120B, Wan-2.2 text-to-video
- ATOM inference engine for modern LLM primitives (MLA, sparse MoE, block-scale GEMMs)

## Additional coverage
- StorageReview: https://www.storagereview.com/news/amd-instinct-mi355x-achieves-mlperf-inference-v6-0-gains-with-over-1-million-tokens-per-second-and-supports-scalable-rocm-stack
- AMD distributed inference analysis: https://www.amd.com/en/developer/resources/technical-articles/2026/distributed-inference-performance-on-instinct-mi355x-gpu.html
