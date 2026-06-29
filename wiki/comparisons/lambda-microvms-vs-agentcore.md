---
title: "AWS Lambda MicroVMs vs Amazon Bedrock AgentCore"
type: comparison
created: 2026-06-29
updated: 2026-06-29
tags:
  - comparison
  - aws
  - ai-agents
  - sandbox
  - harness-engineering
  - infrastructure
  - microvm
  - firecracker
  - platform
sources:
  - "https://aws.amazon.com/jp/blogs/aws/run-isolated-sandboxes-with-full-lifecycle-control-aws-lambda-introduces-microvms/"
  - "https://aws.amazon.com/bedrock/agentcore/"
  - raw/articles/2026-06-22_aws-lambda-microvms-announcement.md
  - raw/articles/2026-05-03_amazon-bedrock-agentcore.md
---

# AWS Lambda MicroVMs vs Amazon Bedrock AgentCore

## What Is Being Compared

Both are AWS services targeting the AI agent infrastructure market, but they operate at **fundamentally different layers of the agent stack**:

| | Lambda MicroVMs | AgentCore |
|---|---|---|
| **Layer** | Isolation / sandbox primitive | Managed agent platform |
| **Abstraction** | Low-level (VM lifecycle API) | High-level (composable services) |
| **Analogy** | EC2 for agent sandboxes | Heroku for agent platforms |
| **What you build** | Custom harness on top | Agent using platform services |

## Architectural Position in the Agent Stack

```
┌─────────────────────────────────────────────────────────┐
│  Agent Application (your code)                          │
├─────────────────────────────────────────────────────────┤
│  Harness Layer (orchestration, tools, memory, context)  │
├────────────────────────┬────────────────────────────────┤
│  AgentCore Platform    │  Custom Platform               │
│  ┌─────────────────┐   │  ┌──────────────────────────┐  │
│  │ Memory           │   │  │ Your harness framework   │  │
│  │ Gateway          │   │  │ (LangGraph, Claude SDK,  │  │
│  │ Browser Runtime  │   │  │  custom, etc.)           │  │
│  │ Code Interpreter │   │  └──────────┬───────────────┘  │
│  │ Session Isolation│   │             │                  │
│  │ IAM Integration  │   │             ▼                  │
│  │ CloudWatch/OTel  │   │  ┌──────────────────────────┐  │
│  └─────────────────┘   │  │ Lambda MicroVMs           │  │
│                         │  │ (Firecracker isolation,   │  │
│                         │  │  snapshot-based launch,   │  │
│                         │  │  stateful 8hr sessions)   │  │
│                         │  └──────────────────────────┘  │
├────────────────────────┴────────────────────────────────┤
│  AWS Infrastructure (IAM, VPC, S3, CloudWatch)          │
└─────────────────────────────────────────────────────────┘
```

## Detailed Comparison

| Dimension | Lambda MicroVMs | AgentCore |
|-----------|----------------|-----------|
| **Primary purpose** | Isolated sandbox for untrusted code execution | Full agent lifecycle platform (build/deploy/monitor/scale) |
| **Isolation mechanism** | Firecracker VM (hardware virtualization) | Session isolation (managed, implementation not disclosed) |
| **Startup model** | Snapshot-based near-instant resume | Seconds (managed) |
| **Max session duration** | 8 hours | 8 hours |
| **Statefulness** | Full (memory + disk + process state) | Partial (Memory service for knowledge retention) |
| **Resource control** | Up to 16 vCPU, 32 GB RAM, 32 GB disk | Managed (not user-configurable) |
| **API surface** | `create-microvm-image` → `run-microvm` → token-based HTTPS | AgentCore SDK / API (composable services) |
| **Framework coupling** | None (raw infrastructure primitive) | Framework-agnostic but platform-coupled |
| **Identity/IAM** | Short-lived proxy tokens (`X-aws-proxy-auth`) | Native IAM integration with automated delegation |
| **Observability** | Bring your own | CloudWatch + OpenTelemetry built-in |
| **Memory/knowledge** | None (you manage state yourself) | Persistent Memory service built-in |
| **Tool integration** | None (you build tool layer yourself) | Gateway service for tool connections |
| **Browser automation** | None | Secure Browser Runtime included |
| **Pricing model** | Per-MicroVM compute time | Per-service usage |

## When to Use Which

### Use Lambda MicroVMs When

- You need **maximum control** over the isolation environment
- Building a **custom sandbox platform** (like E2B, Modal, Daytona)
- Running **user-generated or AI-generated code** that requires VM-level security
- You already have a harness (LangGraph, Claude Agent SDK, etc.) and need a **pluggable isolation backend**
- You need **fine-grained resource control** (specific vCPU/RAM/disk allocation)
- Building **multi-tenant SaaS** where each tenant gets an isolated environment
- Cost-sensitive workloads where you want to **optimize idle/suspend behavior**

### Use AgentCore When

- You want a **managed platform** without building infrastructure
- Need **end-to-end agent lifecycle** (build → deploy → monitor → scale)
- Enterprise requirements: **IAM integration, compliance, audit trails**
- Want **built-in observability** (CloudWatch, OpenTelemetry)
- Need **managed memory, tool gateway, browser runtime** out of the box
- Framework-agnostic: works with any agent framework
- Team lacks infrastructure engineering capacity

### Use Both Together

The most powerful pattern combines both layers:

1. Use **AgentCore** for the platform layer (memory, gateway, identity, monitoring)
2. Use **Lambda MicroVMs** as the **isolation backend** for AgentCore's Code Interpreter or custom sandbox needs
3. This gives you managed platform convenience with VM-level isolation guarantees

## Relationship to Agent Harness Concepts

These products map directly to the [[concepts/harness-engineering/agent-harness|harness/runtime distinction]]:

| Concept | Lambda MicroVMs | AgentCore |
|---------|----------------|-----------|
| **Harness layer** | Not provided — you build the harness | Partially provided (orchestration via Gateway) |
| **Runtime layer** | The isolation primitive itself | The managed runtime |
| **Control flow ownership** | Developer owns everything | Platform mediates execution |
| **Harness type** | Infrastructure for any harness | Platform-as-harness |

Lambda MicroVMs is a **runtime primitive** — it answers "where does the agent execute safely?" without answering "how does the agent orchestrate?" AgentCore answers both, but at a higher abstraction with less control.

## Competitive Landscape Context

| Provider | Low-Level Primitive | Managed Platform |
|----------|--------------------|--------------------|
| **AWS** | Lambda MicroVMs | AgentCore |
| **GCP** | GKE Sandbox (gVisor) | Gemini Enterprise Agent Platform |
| **Azure** | ACI / Confidential Containers | Azure AI Agent Service |
| **Independent** | E2B, Modal, Daytona | LangChain Platform, CrewAI Enterprise |

AWS is unique in offering **both layers as separate products**, letting teams choose their abstraction level. Google and Microsoft bundle isolation into their platforms.

## Open Questions (as of June 2026)

- Will AgentCore's Code Interpreter migrate to Lambda MicroVMs as its isolation backend? (Currently unconfirmed)
- Pricing comparison: AgentCore's per-service model vs. Lambda MicroVMs' per-compute model at scale
- Multi-region snapshot replication for Lambda MicroVMs (currently 5 regions at GA)

## Related Pages

- [[concepts/aws-lambda-microvms]] — Lambda MicroVMs detailed page
- [[entities/amazon-bedrock-agentcore]] — AgentCore entity page
- [[concepts/harness-engineering/agent-harness]] — Agent Harness architecture
- [[concepts/harness-engineering/agent-runtime]] — Agent Runtime layer
- [[comparisons/agent-sandboxing]] — Agent sandboxing ecosystem
- [[concepts/firecracker]] — Firecracker MicroVM technology
