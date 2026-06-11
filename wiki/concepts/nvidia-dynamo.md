---
title: NVIDIA Dynamo
created: 2026-04-26
updated: 2026-05-10
type: concept
tags:
  - inference
  - optimization
  - agentic-engineering
  - platform
  - streaming
  - tool
  - reasoning
  - kv-cache
sources:
  - raw/articles/2026-04-25-nvidia-dynamo-agentic-inference.md
  - raw/articles/2026-05-08_nvidia-dynamo-streaming-tokens-tools.md
---

# NVIDIA Dynamo

NVIDIA Dynamo is an inference architecture and platform designed specifically for agentic coding workloads, addressing the limitations of traditional inference stacks when handling multi-step agent interactions.

## Problem Statement

Traditional inference wasn't built for agentic coding. Agentic tools make hundreds of API calls per coding session, often with recomputed context, creating bottlenecks that drive up cost per token. Key challenges:

- **KV Recomputation:** Wastes compute when routing ignores cache overlap
- **Memory Pressure:** Long contexts exceed HBM capacity without multi-tier cache management
- **Dynamic Demand:** Bursty traffic breaks static provisioning assumptions
- **Prompt Instability:** Session-specific headers poison KV cache reuse

## Architecture

### Three-Plane Design

1. **Request Plane** (critical data path)
   - **Frontend:** Accepts and normalizes requests
   - **Router:** Selects workers based on load and KV overlap awareness
   - **Prefill workers:** Compute prompt KV state
   - **Decode workers:** Generate output tokens

2. **Control Plane** (adaptation and orchestration)
   - **Planner:** Computes scaling targets from live metrics
   - **Dynamo Operator:** Reconciles Kubernetes resources
   - **Grove/KAI Scheduler:** Topology-aware placement

3. **Storage & Events Plane** (state propagation)
   - **KV Events:** Publish cache lifecycle transitions
   - **KVBM (Key-Value Block Manager):** Manages block reuse, eviction, and offload/recall
   - **NIXL (NVIDIA Inference eXecution Layer):** High-speed KV/data transfer across workers

## Design Goals

- Latency stability under bursty traffic
- GPU efficiency via disaggregated prefill/decode
- Compute reuse via KV-aware routing
- Operational resilience for worker crashes
- Deployment portability (Kubernetes and non-K8s)
- Correct multi-turn agentic exchange with interleaved reasoning and tool calls

## Agentic Harness Support

### Streaming Tokens and Tools

Dynamo supports multi-turn agentic harnesses (Claude Code, Codex, OpenClaw) with several key capabilities:

#### Reasoning Parsing and Tool Call Interleaving

- Models produce interleaved reasoning and tool calls: `<think>reasoning_0</think> tool_call_0 <think>reasoning_1</think> tool_call_1`
- Dynamo ensures reasoning spans stay attached to their corresponding tool calls across turns
- Prevents the bug where reasoning gets grouped: `<think>reasoning_0 reasoning_1</think> tool_call_0 tool_call_1`

#### Streaming Tool Dispatch

- Tool calls are emitted as typed SSE events (`event: tool_call_dispatch`) rather than buffered until turn completion
- Enables immediate tool execution without harness-side delta assembly
- Improves responsiveness in agent workflows

#### Per-Request Thinking Controls

- Dynamo changes behavior based on whether reasoning is in play:
  - When reasoning parser is configured and client hasn't disabled thinking: `enable_thinking=true` and `truncate_history_thinking=false`
  - Preserves next-turn context agents need without changing defaults for non-thinking requests

### Harness-Facing Dynamo Settings

Key configuration flags for agentic workloads:

```bash
python -m dynamo.frontend \
  --http-port 8000 \
  --enable-anthropic-api \
  --strip-anthropic-preamble \
  --enable-streaming-tool-dispatch
```

Worker-side settings:
- `--dyn-tool-call-parser <parser>` - reconstructs tool calls in harness-expected format
- `--dyn-reasoning-parser <parser>` - handles reasoning blocks per model requirements

### Prompt Stability for KV Cache Reuse

- Claude Code sends session-specific billing headers that poison KV cache:
  ```
  x-anthropic-billing-header: cc_version=0.2.93; cch=abc123def456==;
  ```
- The `--strip-anthropic-preamble` flag removes these headers before tokenization
- **Impact**: On B200 deployment with 52K-token prompt:
  - Stable prefix: 168ms TTFT
  - With varying header: 912ms TTFT (5x degradation)
  - After stripping: 169ms TTFT

### Anthropic API Fidelity

Claude Code and OpenClaw require:
- Model metadata at `GET /v1/models` and `GET /v1/models/{model_id}`
- Correct handling of slashed model IDs
- Useful `input_tokens` in `message_start`
- Acceptance of `cache_control`

### Codex/Responses API Fidelity

Codex requires:
- `v1/responses` endpoint support
- Request compression
- Model catalog metadata that shapes agent behavior
- Tool-output truncation policies (tokens vs bytes limits matter differently)

## Significance

Dynamo represents a fundamental rethinking of inference architecture for agentic workloads, where context reuse (KV cache awareness) becomes the primary optimization target rather than raw throughput. This connects directly to [[concepts/context-engineering|Context Engineering]] and [[concepts/kv-aware-routing]] as core principles.

The streaming tokens and tools capabilities enable Dynamo to serve as a production-grade backend for coding agents that require:
- Interleaved reasoning and tool call handling
- Low-latency streaming responses
- KV cache optimization across multi-turn conversations
- API fidelity with major harness providers (Anthropic, OpenAI)

## Related

- [[concepts/agentic-engineering]]
- [[concepts/inference]]
- [[concepts/context-engineering|Context Engineering]]
- [[concepts/kv-aware-routing]]
- [[nvidia]]
- [First Dynamo post: Full-Stack Optimizations for Agentic Inference](https://developer.nvidia.com/blog/full-stack-optimizations-for-agentic-inference-with-nvidia-dynamo/)
- [Streaming Tokens and Tools article](https://developer.nvidia.com/blog/streaming-tokens-and-tools-multi-turn-agentic-harness-support-in-nvidia-dynamo/)

## Sources

- [@NVIDIAAI tweet (2026-04-25)](https://x.com/NVIDIAAI/status/2048069526000934986) — 454 bookmarks
- [NVIDIA Dynamo Architecture Docs](https://docs.dynamo.nvidia.com/dynamo/design-docs/overall-architecture)
- [Streaming Tokens and Tools: Multi-Turn Agentic Harness Support in NVIDIA Dynamo](https://developer.nvidia.com/blog/streaming-tokens-and-tools-multi-turn-agentic-harness-support-in-nvidia-dynamo/) (May 08, 2026)
