---
title: "Mesh LLM"
created: 2026-07-14
updated: 2026-07-14
type: concept
tags: [distributed-systems, inference, p2p, edge-computing, model, llm-inference, distributed-training, local-first]
sources:
  - raw/articles/2026-07-11_iroh_mesh-llm-distributed-inference.md
  - https://www.iroh.computer/blog/mesh-llm
  - https://hn.algolia.com/api/v1/items/48876505
---

## What It Is

Mesh LLM is a distributed P2P inference system that pools GPU resources across machines into a single OpenAI-compatible API, built on the iroh peer-to-peer networking protocol. It enables running large language models without centralized servers — users contribute their own GPU hardware to a mesh, and inference requests are automatically routed to the best available node or split across multiple machines via layer-wise pipeline parallelism.

The project is open source (https://github.com/Mesh-LLM/mesh-llm) and provides a lightweight ~18 MB binary that exposes `localhost:9337/v1` as an OpenAI-compatible endpoint. The catalog ships with 40+ pre-configured models ranging from 0.5B to 235B parameters.

## How It Works

### iroh Protocol Foundation

Every Mesh LLM node boots an iroh endpoint identified by a public key. iroh handles NAT traversal, hole-punching, and relay fallback to establish direct authenticated QUIC connections between any two nodes — no central coordination server required. Two iroh relays in different regions provide fallback paths when direct connections are impossible.

The protocol uses three ALPN-negotiated QUIC connections:

| ALPN | Purpose |
|------|---------|
| `mesh-llm/1` | Main mesh: gossip, routing, HTTP tunnels, plugin channels |
| `mesh-llm-control/1` | Owner control plane (config sync, ownership attestation) |
| `skippy-stage/2` | Latency-sensitive activation transport for split models |

Within `mesh-llm/1`, a single byte-prefixed multiplexing scheme carries all mesh traffic: gossip announcements (models, GPU, RTT), inference requests tunneled to peers, route queries, and peer lifecycle events (join, graceful leave, failure notification).

### Model Serving Modes

A request can be served in three ways:

1. **Local**: Run entirely on the local machine's GPU.
2. **Routed**: Forwarded to a peer that already has the model loaded in VRAM.
3. **Split (Skippy)**: Partition a model by layer ranges across multiple machines in a pipeline. Each node hosts a contiguous range of layers (e.g., layers 0-15 on node A, 16-31 on node B). Activations flow sequentially through the pipeline.

The Skippy engine is built as a patch queue on top of llama.cpp, providing access to internal activations and tensor filtering at model load time. Model splits are pre-computed and published to the MeshLLM HuggingFace organization. During split serving, each node maintains its own KV cache for the layers it hosts, and if a node fails mid-inference, the topology is recalculated and the request automatically retried.

### Peer Discovery and Routing

Peer discovery uses a gossip protocol over the `mesh-llm/1` connection. Nodes announce their capabilities (available models, GPU specs, RTT estimates) via GOSSIP streams (byte `0x01`). When a request arrives at any node, the mesh decides whether to serve locally, route to a peer, or initiate a split pipeline. The gossip layer controls mesh admission, version compatibility, and trust — iroh provides only the secure transport.

Plugins declare capabilities in a manifest; the runtime starts them, routes calls, and exposes functionality over MCP, HTTP, inference, and mesh events.

## Performance Characteristics

- **Qwen 235B A22B (MoE)**: 16 tok/s across 2 nodes in split mode
- **GLM 5.2**: ~10 tok/s on home lab hardware (2 Mac Studios, simulated 5ms latency)
- **Bottleneck**: Network latency, not bandwidth. Only activation vectors (kilobytes) cross the network per token; model weights stay in each node's VRAM, benefiting from GPU memory bandwidth.
- **Theoretical ceiling**: With 1ms latency per hop and a 4-node split, max ~30 tok/s for autoregressive decoding
- **Prefill advantage**: Prompt processing is not latency-bound since it can be parallelized across stages

This makes split mode practical for LAN and metro-latency WAN deployments but slow over global internet connections.

## Use Cases

- **Edge deployment**: Run models on hardware you already own — office GPUs, workstations under desks, mini PCs in closets
- **Privacy-sensitive inference**: Keep data within a trusted private mesh of owned hardware, avoiding third-party API providers
- **Community compute sharing**: Pool resources among trusted peers (friends, family, small teams) to run models larger than any single machine can hold
- **Model aggregation**: Combine disparate GPU resources behind one endpoint without separate inference providers on each host

## Comparison with Existing Approaches

### vs. HuggingFace TGI (Text Generation Inference)

TGI is a centralized server solution optimized for production serving with continuous batching, quantization, and watermarks. It assumes a single machine or cluster under unified control with fast interconnects. Mesh LLM targets the opposite scenario: distributed, heterogeneous hardware without centralized infrastructure.

### vs. vLLM distributed

vLLM supports tensor parallelism across GPUs within a single machine or tightly-coupled cluster (NCCL, NVLink, InfiniBand). It achieves high throughput through PagedAttention and continuous batching. Mesh LLM operates at a coarser granularity — pipeline parallelism across machines connected by consumer networks — and trades raw throughput for deployment flexibility and hardware sovereignty.

### vs. Petals

Petals (https://petals.dev) pioneered P2P inference for large models, using a similar layer-wise pipeline approach over distributed volunteer hardware. Key differences: Petals uses libp2p and a DHT for peer discovery, supports the BLOOM family, and has a blockchain-based incentive system. Mesh LLM uses iroh/QUIC instead of libp2p, supports a broader model catalog (40+ models via llama.cpp backend), and focuses on private/deployment meshes rather than a global volunteer network. Both share the fundamental challenge of network latency limiting token generation speed.

### vs. exo

exo (Mac-only) also does distributed inference but targets Apple Silicon specifically. Mesh LLM is cross-platform (Linux, macOS, Windows) with broader hardware support. Detailed comparison at meshllm.cloud/docs/pages/exo-comparison/.

## Current Limitations

- **Latency-bound token generation**: Split mode over WAN is too slow for interactive use
- **No E2E encryption for prompts**: Payloads are visible to each node performing computation; transport encryption (QUIC) protects network transit only
- **No incentive mechanism**: Public mesh has no rewards for contributors; primary use case remains private trusted meshes
- **Privacy concerns**: Malicious node operators in a mesh could inspect prompts and responses
- **Limited performance data**: Real-world benchmarks across varied network conditions and hardware configurations are still sparse
- **Security**: As a layer on llama.cpp, needs careful sandboxing when accepting inputs from untrusted peers

## Related Pages

- distributed inference
- edge inference
- peer-to-peer networking
- iroh
- [[concepts/training-infra/distributed-training]]

## External Resources

- Website: https://meshllm.cloud
- GitHub: https://github.com/Mesh-LLM/mesh-llm
- Public mesh dashboard: https://public.meshllm.cloud
- Iroh blog post: https://www.iroh.computer/blog/mesh-llm
