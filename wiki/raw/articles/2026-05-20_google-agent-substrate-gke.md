# Google Announces Agent Sandbox GA on GKE and Agent Substrate

**Source:** [Google Cloud Blog](https://cloud.google.com/blog/products/containers-kubernetes/bringing-you-agent-sandbox-on-gke-and-agent-substrate)
**Date:** May 20, 2026
**Authors:** Brandon Royal (Product Manager, GKE) and Tim Hockin (Software Engineer, GKE)

## Agent Sandbox on GKE — General Availability

Since its preview at KubeCon NA (November 2025), adoption has surged with 16x growth in sandboxes in less than 5 months. Key customers like Langchain and Lovable are deploying millions of agents.

Core features:
- **Pod Snapshots**: Suspend idle agents, resume in seconds
- **Ultra-low latency provisioning**: 300 sandboxes/sec per cluster at sub-second latency, 90% in 200ms
- **Warm pool with standby capacity buffers**: Suspended VMs at fraction of running cost
- **Ironclad security**: gVisor, default-deny network policies, Kata Containers pluggable
- **Axion processors**: Up to 30% better price-performance

## Agent Substrate — New Open-Source Project

Targets the next frontier: 10s-100s of millions of agents that are increasingly idle, waiting for human input.

> "While standard Kubernetes is optimized to handle thousands of long-running services, Agent Substrate is designed for the chatter of millions of sub-second tool calls."

Key design goals:
- **Minimal control plane**: Bypass k8s control plane limits for high-chatter tool calls
- **Real-time agent movement**: Move agents on/off compute in real-time with specialized scheduler
- **Extreme density**: Data locality integrated into scheduler
- **Foundation for agent-native tools**: Agent Executor project, harnesses, runtimes

Developed in the open, community-driven like early Kubernetes.
