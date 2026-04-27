# SGLang

| Field | Value |
|-------|-------|
| **Type** | LLM Inference Engine / Serving Framework |
| **Organization** | [[lmsys-org]] |
| **Repository** | https://github.com/sgl-project/sglang |
| **Documentation** | https://docs.sglang.io |
| **Language** | Python, CUDA, Triton |
| **License** | Apache 2.0 |
| **Authored By** | Lianmin Zheng, Liangsheng Yin, Ying Sheng, et al. (UC Berkeley) |

## Overview

**SGLang** is a high-performance inference engine for large language models (LLMs) and vision-language models (VLMs), developed by [[LMSYS Org]]. It was introduced in January 2024 with the novel **RadixAttention** mechanism for efficient prefix caching across multiple generation calls.

SGLang has become one of the most widely deployed open-source LLM inference engines, alongside vLLM and TensorRT-LLM. It provides Day-0 support for major model releases and has deep hardware partnerships with NVIDIA, AMD, and Intel.

## Core Technical Innovations

### RadixAttention
A prefix caching mechanism using radix tree data structure to automatically reuse KV cache across prompts with shared prefixes. Eliminates redundant computation for chat sessions, few-shot examples, and multi-turn interactions.

### Prefill-Decode (PD) Disaggregation
Separates the prompt processing (prefill) and token generation (decode) phases across different GPU instances, enabling independent scaling and optimized resource allocation.

### Expert Parallelism (EP)
Specialized support for Mixture-of-Experts (MoE) models like DeepSeek-V3/V4, Qwen3, and Nemotron 3. Features include DeepEP backend, mega-MoE fused kernels, Elastic EP for fault tolerance.

### Pipeline Parallelism (PP)
Chunked Pipeline Parallelism for ultra-long context inference. Achieves 3.31× prefill throughput for DeepSeek-V3.1 with dynamic chunking, enabling million-token contexts.

## Key Features (2026)

### Inference Optimizations
- **FlashMLA**: Fused multi-head latent attention kernel for Hopper/Blackwell GPUs
- **FlashInfer TRTLLM-Gen MoE**: MXFP8 × MXFP4 weight support for Blackwell
- **TileLang mHC**: Manifold-constrained hyper-connections kernel with split-K
- **DeepGEMM Mega MoE**: Fused EP dispatch, GEMM, SwiGLU pipeline
- **Flash Compressor**: Fused 5-stage compression in single kernel pass (up to 80% peak bandwidth)
- **Lightning TopK**: Cluster-of-8 radix-select reduction for top-k (15µs latency)

### Memory Management
- **HiSparse**: Hierarchical memory for sparse attention — offloads inactive KV to CPU, up to 5× throughput gain
- **HiCache**: Hierarchical KV caching with storage backend integration
- **ShadowRadix**: Native prefix caching for hybrid attention (SWA + compressed) in DeepSeek-V4

### Speculative Decoding
- **MTP** (Multiple Token Prediction): DeepSeek-V4 native MTP support
- **SpecForge**: Training framework for speculative decoding
- **SpecBundle**: Configuration toolkit for speculative bundling
- **EAGLE-3**: Speculative decoding integration

### Diffusion Model Support
- **SGLang-Diffusion**: Video generation model serving for models like Wan2.2
- Token-level sequence sharding (SP-Sharding)
- Distributed Parallel VAE for high-resolution encoding
- Fused JIT kernels (CuTeDSL) for WanVideo

### Reinforcement Learning
- **Miles** integration for RL post-training
- INT4 Quantization-Aware Training (QAT) pipeline
- FP8 end-to-end training support
- GRPO/PPO training with Megatron-LM backend

## Hardware Support

| Platform | Status |
|----------|--------|
| NVIDIA Hopper (H100, H200) | Full support |
| NVIDIA Blackwell (B200, GB200 NVL72) | Full support |
| NVIDIA Blackwell Ultra (GB300 NVL72) | Full support — 25× improvement |
| NVIDIA DGX Spark | Verified |
| AMD Instinct MI300X/MI350X | Full support (ROCm) |
| Intel Xeon 6 (Granite Rapids) | Verified — cost-effective CPU deployment |
| Huawei NPU | Experimental support |

## Key Integration Partners
- [[NVIDIA]]: Dynamo, NIXL, TensorRT-LLM kernels
- [[AMD]]: ROCm for both inference and RL training
- [[Alibaba Cloud]]: EPD Disaggregation, Mooncake
- [[Ant Group]]: Production MoE serving, Elastic EP
- [[Intel]]: Xeon optimization
- [[Meituan]]: LongCat-Flash deployment

## Recent Model Support Timeline
- **Apr 2026**: DeepSeek-V4 (Pro 1.6T, Flash 284B)
- **Mar 2026**: NVIDIA Nemotron 3 Super (120B/12B active)
- **Feb 2026**: Qwen3 & Qwen3-VL on AMD MI300X
- **Jan 2026**: GLM-4.5
- **Aug 2025**: OpenAI gpt-oss-120b
- **Jul 2025**: Kimi K2 (1T parameters)
- **May 2025**: DeepSeek V3/R1 large-scale deployment

## Links
- [GitHub Repository](https://github.com/sgl-project/sglang)
- [Documentation](https://docs.sglang.io)
- [Cookbook](https://cookbook.sglang.io)
- [LMSYS Blog Posts](https://lmsys.org/blog/)
