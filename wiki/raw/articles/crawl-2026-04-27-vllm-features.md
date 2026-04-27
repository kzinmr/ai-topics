# vLLM April 2026 Update: v0.18.0–v0.19.1

Source: GitHub releases (vllm-project/vllm), Q2 2026 Roadmap
Date: 2026-04-27
Topic: local-llm deepdive

## Overview

vLLM continues as the leading high-throughput LLM serving engine. The v0.19.0 release (April 3, 2026) with 448 commits from 197 contributors represents a major step forward.

## Key New Features (v0.18.0–v0.19.1)

### 1. Gemma 4 Full Support (v0.19.0)
- Complete support for Gemma 4 architecture: MoE, multimodal, reasoning, tool-use
- Requires `transformers>=5.5.0`
- Pre-built Docker image: `vllm/vllm-openai:gemma4`
- v0.19.1 fixes: streaming tool calls, HTML duplication, tool call corruption, BOS injection, quantized MoE, Eagle3 support, LoRA adapter loading

### 2. Zero-Bubble Async Scheduling + Speculative Decoding
- Significantly improves throughput by overlapping scheduling and execution
- Eliminates idle bubbles in the pipeline
- Integrates with speculative decoding for combined gains

### 3. Model Runner V2
- Piecewise CUDA graphs for pipeline parallelism (PP)
- Speculative decode rejection sampler (greedy + logprobs)
- Multimodal embeddings and streaming inputs support
- Configurable acceptance rate and FP32 draft logits
- EPLB (Expert Parallel Load Balancing) support

### 4. Performance Mode Flag
- New `--performance-mode {balanced, interactivity, throughput}` flag (v0.17.0)
- Simplifies performance tuning for common deployment scenarios

### 5. Anthropic API Compatibility
- Anthropic thinking blocks support
- `count_tokens` API
- `tool_choice=none`
- Streaming and image handling fixes

### 6. Qwen3.5 GDN (Gated Delta Networks) Support
- Full support for Qwen3.5 model family with FP8 quantization
- MTP speculative decoding
- Reasoning parser support

### 7. CPU KV Cache Offloading (V1 Engine)
- Pluggable cache policy with block-level preemption
- Multiple KV groups and hybrid model support
- Enables running larger models on limited GPU memory

### 8. DBO (Dual-Batch Overlap) Generalization
- Previously limited to specific architectures, now works with all models
- Improves throughput for all supported model types

### 9. NVIDIA B300/GB300 (SM 10.3) Support
- Allreduce fusion enabled by default
- Optimized for next-generation NVIDIA hardware

### 10. ViT Full CUDA Graphs
- Reduced overhead for vision encoder processing
- Benefits multimodal model serving

### 11. Q2 2026 Roadmap Highlights
- torch.compile: 1.3x cold compile speedup, ≤2s warm compile (5x improvement)
- Full vLLM IR migration
- Improved performance dashboard
- torch.compile x CUDA streams
- Custom helion kernel by default

## Model Support Expansion
- New architectures: Gemma 4, Cohere ASR, Cohere Transcribe, ColQwen3.5 4.5B, LFM2-ColBERT-350M, Granite 4.0 1B Speech, Qwen3-ForcedAligner
- Speculative decoding: Eagle3 for Pixtral, EagleMistralLarge3 fix
- LoRA expansion: H2OVL tower/connector, `--lora-target-modules`

## Hardware Support
- NVIDIA: Blackwell (SM120 FP8 GEMM), B300/GB300, H200 tuning
- AMD ROCm 7.2.1: DeepEP all2all backend, FP8×FP8 attention, AWQ Marlin, RDNA4 support
- Intel XPU: MLA model support, CompressedTensor W4A8
- TPU: Async scheduling interface
- CPU: tcmalloc by default (48.9% throughput improvement for pooling models)
