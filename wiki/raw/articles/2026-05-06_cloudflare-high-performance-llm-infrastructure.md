# Building the Foundation for Running Extra-Large LLMs at Cloudflare

**Source**: https://blog.cloudflare.com/high-performance-llms/
**Date**: 2026-05-06

## Key Points

- PD (Prefill-Decode) Disaggregation: 3x intertoken latency improvement (100ms → 20-30ms)
- Prompt caching with x-session-affinity: 60% → 80% cache hit ratio
- Mooncake Transfer Engine for KV-cache offload to NVMe
- Speculative decoding with NVIDIA EAGLE-3 for Kimi K2.5
- Infire Rust engine: Llama 4 Scout on 2 H200s (1.2M+ token context), Kimi K2.5 on 8 H100s
- Cold start under 20 seconds, 20% higher tokens/sec than vLLM

## Full Article

[Read original](https://blog.cloudflare.com/high-performance-llms/)
