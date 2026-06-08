---
title: Agent Substrate
created: 2026-05-26
updated: 2026-05-26
type: concept
tags:
  - concept
  - ai-agents
  - developer-tooling
  - google
  - open-source
  - sandbox
  - agent-runtime
  - infrastructure
sources: [raw/articles/2026-05-20_google-agent-substrate-gke.md]
---

# Agent Substrate

Google Cloud's open-source project for ultra-scale AI agent infrastructure, announced May 20, 2026 alongside the general availability of Agent Sandbox on GKE. Designed for the next frontier: 10s-100s of millions of agent instances running simultaneously, often idle, awaiting human input or triggers.

## Core Design

Agent Substrate introduces a minimal control plane layered above Kubernetes, purpose-built for short-lived, high-chatter agent tool calls:

> "While standard Kubernetes is optimized to handle thousands of long-running services, Agent Substrate is designed for the chatter of millions of sub-second tool calls that would otherwise overwhelm a standard control plane."

### Key Capabilities
- **Real-time agent movement**: Moves agents onto/off ready compute capacity in real-time, pairing secure runtimes and snapshotting from Agent Sandbox with a specialized scheduler
- **Extreme density**: Integrates data locality into the core scheduler to minimize overhead
- **Suspend-and-resume**: Enables rapid context switching for millions of idle agents
- **Open development**: Community-driven like early [[concepts/kubernetes]]

## Relationship to Agent Sandbox

Agent Sandbox on GKE (now GA) provides the secure, scalable execution layer. Since KubeCon NA November 2025, adoption grew 16× in <5 months, with LangChain and Lovable deploying millions of agents. Key GA features:

- 300 sandboxes/sec per cluster at sub-second latency (90% in 200ms)
- Pod snapshots for reduced idle compute
- gVisor + Kata Containers isolation
- 30% better price-performance on Axion processors

Agent Substrate builds on these primitives, targeting the next order of magnitude in scale.

## Significance

This represents Google's bet that agent infrastructure is at a Kubernetes-like inflection point. By developing Agent Substrate in the open from day one, Google aims to recreate "the magic of radically open and collaborative innovation" that defined Kubernetes' early success.

## Related Pages
- [[entities/google]] — Google's AI infrastructure strategy
- [[concepts/kubernetes]] — Foundation for Agent Sandbox
- [[concepts/nvidia-ai-q]] — NVIDIA's open-source deep research agent blueprint
