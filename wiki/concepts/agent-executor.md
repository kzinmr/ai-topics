---
title: Agent Executor
created: 2026-05-24
updated: 2026-05-24
type: concept
tags:
  - ai-agents
  - infrastructure
  - open-source
  - google
  - agent-runtime
  - durable-execution
  - orchestration
  - sandbox
  - developer-tooling
sources: [raw/articles/2026-05-20_google-agent-executor.md]
---

# Agent Executor

Agent Executor is Google's **open-source runtime standard** for AI agent execution, resumption, and distributed deployment, announced at Google I/O 2026 on May 20. It addresses the fragility and management complexity of long-running agent workflows in production, providing durable execution guarantees across arbitrary agent stacks.

## Native Capabilities

### 1. Durable Execution
Automatic backend resilience via **event log + snapshotting**. Agents resume after outages or human-in-the-loop (HITL) interruptions — for any component: agent, harness, skill, tool, or sandbox.

### 2. Secure Isolation
All components run in **secure-by-design sandboxes**, preventing harmful side-effects and containing malicious activity. Critical when agents generate code or handle multi-tenant data concurrently.

### 3. Session Consistency
Built-in **single-writer architecture** ensures only one component updates shared session state at a time, reducing corruption risk in distributed workflows.

### 4. Connection Recovery
Clients can reconnect after disconnections (network outages). Backfills responses from the last known sequence for a smooth user experience.

### 5. Trajectory Branching
**Checkpoints** allow branching an agentic trajectory at any point, enabling testing/evaluation of alternative paths without losing context or state.

## Deployment Model

Agent Executor bridges heterogeneous deployment models:

- **Google Antigravity 2.0** — Gemini's agent harness
- **Managed Agents in Gemini API** — Google-managed custom agents
- **Self-built agents** — LangChain/LangGraph, ADK, or any agent using the A2A protocol

Enterprises maintain full workload sovereignty: deploy on own infrastructure, bring own harness, full control over data residency and policy enforcement.

## Agent Substrate

A companion open-source project built with the GKE team. Introduces a new **agent-first compute layer** for Kubernetes:

- Designed for **millions of sub-second tool calls** — standard Kubernetes control planes would be overwhelmed
- Minimal control plane bypassing Kubernetes limitations without reinventing it
- Combines secure runtime + snapshotting for ultra-dense agent scheduling
- Enables agents to move on and off ready compute capacity in real-time

## Related Pages

- [[entities/google-antigravity]] — Google Antigravity platform
- [[concepts/agent-runtime]] — agent runtime concept
- [[concepts/harness-engineering]] — agent harness engineering
- [[concepts/durable-execution]] — durable execution pattern
- [[concepts/sandbox]] — sandbox isolation
- [[events/google-io-2026]] — Google I/O 2026 event
- [[concepts/agent-sandbox-patterns]] — Sandboxing and scheduling patterns (Agent Substrate GA)
- [[concepts/nvidia-ai-q]] — NVIDIA's competing deep research agent architecture
