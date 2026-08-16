---
title: vLLM
type: concept
created: 2026-04-25
updated: 2026-07-14
tags:
  - inference
  - vllm
  - infrastructure
  - open-source
sources:
  - raw/newsletters/2026-07-14-ainews-codex-usage-up-10x-in-6-months-to-7m-users-1m-in-the-past-day-did-codex-o.md
  - raw/articles/2026-05-10_mistral-ai_debugging-memory-leak-in-vllm.md
  - https://github.com/vllm-project/vllm
  - https://docs.vllm.ai
---

# vLLM

vLLM is an open-source high-throughput LLM serving engine developed at UC Berkeley and maintained by the vLLM project team. It uses PagedAttention for efficient memory management and supports continuous batching, tensor parallelism, and streaming.

## HuggingFace Transformers Integration (July 2026)

HuggingFace CEO Clement Delangue announced that HuggingFace Transformers models can now run in vLLM at native or exceeding hand-written implementation speed. This eliminates the need to double-implement each architecture for both Transformers and vLLM, significantly reducing maintenance burden.

Key benefits:
- Single implementation path for new model architectures
- Performance matching or exceeding hand-written vLLM implementations
- Reduced ecosystem fragmentation for open-source model deployment

## Disaggregated Serving Memory Leak: UCX mmap Hook Case Study (Jan 2026)

Mistral AI's engineering deep-dive (first post in their Engineering Deep Dive series, by Mathis Felardos) documents a production memory leak in vLLM's Prefill/Decode (P/D) disaggregated serving. The leak appeared only with a frontier model (Mistral Medium 3.1), graph compilation, and NIXL-based KV cache transfer — a steady ~400 MB/min RSS growth leading to OOM after hours.

**Debugging methodology** (a reference path for LLM serving memory investigations):
1. Python-level profilers (Memray, Guppy 3) showed nothing — the heap was stable
2. Heaptrack (LD_PRELOAD malloc/free hooking) showed stable heap but growing peak RSS
3. `pmap` on `/proc/<pid>/maps` revealed anonymous mappings growing with changing base addresses
4. BPFtrace (eBPF) traced `mmap` syscalls originating from glibc's raw `syscall+29` wrapper — but user stack traces were incomplete (frame pointers disabled in optimized Python deps)
5. Targeted GDB conditional breakpoints on the `syscall` instruction (firing only for SYS_mmap) captured full stack traces: Python → UCX UCM memory hooks → `mmap`

**Root cause**: UCX (Unified Communication X, NIXL's transport dependency) hooks **all** `mmap`/`munmap` calls by dynamically patching GOT entries — not just its own InfiniBand allocations — to manage its Registration Cache (RCache) of pinned memory. On `munmap`, UCX moves regions to an invalidation queue instead of freeing; the queue's memory pool grows without bound (default `UCX_RCACHE_MAX_UNRELEASED=inf`), calling `mmap` during `munmap` operations. The hooking auto-disables when Valgrind is detected (why Valgrind appeared usable), and bypasses glibc's wrapper entirely (why LD_PRELOAD hooks missed the calls).

**Fix**: `UCX_MEM_MMAP_HOOK_MODE=none` disables the hooking without performance impact for vLLM — only one large contiguous KVCache region needs registration for NIXL transfers. Alternative: `UCX_RCACHE_MAX_UNRELEASED=1024` forces cleanup at a threshold. Mistral merged a fix in the vLLM repository; the UCX/NIXL teams changed the default for a future NIXL release.

**Key lesson**: performance-critical dependency layers (UCX, PyTorch custom allocators) can silently intercept system calls, defeating standard profiling tools. Cross-layer collaboration (vLLM/Red Hat maintainers, NIXL/UCX/NVIDIA) was required to confirm and fix. Source: [[raw/articles/2026-05-10_mistral-ai_debugging-memory-leak-in-vllm.md]].

## Related Pages

- [[concepts/inference/vllm]] — Detailed vLLM architecture and optimization
- [[concepts/serving-llms-vllm]] — LLM serving patterns with vLLM
- [[concepts/local-llm/vllm]] — vLLM for local inference
- [[concepts/huggingface]] — HuggingFace ecosystem
