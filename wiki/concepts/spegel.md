---
title: "Spegel"
type: concept
aliases:
  - Spegel
  - spegel
created: 2026-04-25
updated: 2026-11-24
tags:
  - open-source
  - infrastructure
  - kubernetes
  - developer-tooling
  - self-hosted
sources:
  - https://github.com/spegel-org/spegel
  - https://spegel.dev
status: active
---

# Spegel

**Spegel** (Swedish for "mirror") is a **stateless, distributed OCI registry
mirror** for Kubernetes clusters. Rather than relying on a centralized,
stateful registry mirror, Spegel turns every cluster node into a peer in a
distributed, peer-to-peer image cache. When a node needs a container image, it
first tries to pull the layers from other nodes already running that image,
falling back to the upstream registry only if no peer has it.

## How It Works

- Deployed as a **DaemonSet** — one Spegel pod per node.
- Each node acts as both a **client and a stateless mirror** of OCI image
  registry functionality, backed by the container images already present locally.
- Uses a **DHT (distributed hash table)** — via libp2p Kademlia — for nodes to
  discover which peers hold a given image digest.
- Pulls are resolved peer-first via the `registry.k8s.io`-style mirror endpoint,
  reducing external registry egress and improving pull latency and resilience.

Its "stateless" property is the key design point: there is no cache to provision,
back up, or scale centrally. The cluster's own running images *are* the cache.

## Origin & Status

Spegel was originally created by **Avito** (a large Russian marketplace) and is now
maintained under the **`spegel-org`** GitHub organization. It is a CNCF-adjacent /
Kubernetes-ecosystem tool commonly discussed alongside **containerd** mirror
configuration and **image-pull optimization** for large clusters and air-gapped
environments.

| Attribute | Value |
|-----------|-------|
| Repo | `spegel-org/spegel` |
| Site | spegel.dev |
| Stars | ~3.8k |
| Category | Kubernetes OCI registry mirror / P2P image distribution |

## Relevance to AI / LLM Infrastructure

Spegel is part of the **GPU cluster infrastructure** layer: large AI training and
inference fleets pull huge container images (CUDA, PyTorch, vLLM images often
multiple GB) across many nodes. P2P image distribution materially cuts cold-start
time and registry egress when scaling out a fleet of identically-imaged GPU nodes —
a common pattern in self-hosted inference platforms.

## Related Pages

- [[concepts/kubernetes]] — deployment substrate
- [[concepts/docker-sandbox-microvm-api]] — adjacent container/runtime infrastructure

## See Also

Spegel sits in the self-hosted inference / GPU-fleet operations layer alongside
[[concepts/vllm]] and [[concepts/llm-inference]].

## Sources

- [spegel-org/spegel — GitHub](https://github.com/spegel-org/spegel) — "Stateless cluster local OCI registry mirror." ~3.8k stars (scraped 2026-11-24)
- [spegel.dev](https://spegel.dev)
