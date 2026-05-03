---
title: Amazon Bedrock AgentCore
created: 2026-05-03
updated: 2026-05-03
type: entity
tags: [platform, aws, enterprise, ai-agents, agent-harness, infrastructure, serverless]
sources: [raw/articles/2026-05-03_amazon-bedrock-agentcore.md]
---

# Amazon Bedrock AgentCore

> **Type:** Fully-managed agentic AI platform | **Vendor:** AWS | **Key Differentiator:** Framework-agnostic

Amazon Bedrock AgentCore is AWS's fully-managed platform for building, deploying, and operating AI agents securely at scale. It provides composable services that function independently of specific frameworks or models — a deliberate contrast with Google's vertically-integrated Gemini Enterprise Agent Platform.

## Platform Architecture

AgentCore splits agent infrastructure into four composable layers:

### Build
- **Persistent Memory:** Agent knowledge retention; learns from user interactions
- **Gateway:** Minimal-code connection of agents to existing tools/services
- **Secure Browser Runtime:** Complex web-based workflow execution
- **Code Interpreter:** Secure code execution for data tasks

### Deploy
- **Session Isolation:** Complete security/privacy per user session
- **Long-Running Workloads:** Multi-step tasks up to **8 hours**
- **Identity Integration:** Native IAM, automated auth/permission delegation
- **Fine-Grained Access:** Policy enforcement for tools and data

### Monitor
- **Real-time Metrics:** Via Amazon CloudWatch (tokens, latency, errors)
- **Quality Evaluation:** Continuous correctness, helpfulness, safety scoring
- **OpenTelemetry Integration:** Third-party observability tool compatibility

### Scale
- **VPC Connectivity:** Private network isolation
- **AWS PrivateLink:** Secure service-to-service communication
- **Pay-for-what-you-use pricing**

## Customer Impact

| Customer | Outcome |
|----------|---------|
| **Epsilon** | 30% faster campaign setup; 8 hrs/week saved |
| **Amazon Devices** | Fine-tuning from days → under 1 hour |
| **Ericsson** | Double-digit R&D efficiency gains |
| **Thomson Reuters** | Development timelines: months → weeks |
| **Cox Automotive** | Agentic vehicle discovery marketplace |

## Competitive Positioning

AWS holds **31% cloud market share** — the largest infrastructure base. AgentCore is their bid to translate that dominance into the agentic era. Key strategic contrast:

| Dimension | AWS AgentCore | Google Gemini Enterprise | Microsoft Foundry |
|-----------|---------------|--------------------------|-------------------|
| **Philosophy** | Framework-agnostic | Full-stack vertical | Distribution-led |
| **Models** | Any model (200+ on Bedrock) | Gemini-first + select third-party | OpenAI-centric + open |
| **Lock-in** | Low (interoperable) | High (optimized stack) | Medium (Office integration) |
| **Strength** | Infrastructure scale | Custom silicon (TPU Ironwood) | Enterprise distribution |

## Related

- [[entities/gemini-enterprise-agent-platform]] — Google's full-stack competitor
- [[concepts/microsoft-agent-365]] — Microsoft's governance layer
- [[concepts/agent-harness]] — The infrastructure layer for LLM agents
- [[concepts/agent-governance]] — Enterprise agent governance
- [[entities/anthropic]] — Claude Managed Agents competitor
