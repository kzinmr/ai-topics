# Introducing the Agent Governance Toolkit: Open-source runtime security for AI agents

**Source:** [Microsoft Open Source Blog](https://opensource.microsoft.com/blog/2026/04/02/introducing-the-agent-governance-toolkit-open-source-runtime-security-for-ai-agents/)
**Date:** April 2, 2026
**License:** MIT

## Summary
Microsoft released the **Agent Governance Toolkit**, an open-source project (MIT license) designed to provide runtime security and governance for autonomous AI agents. It is the first toolkit to address all 10 risks identified in the **OWASP Top 10 for Agentic Applications (2026)** with sub-millisecond policy enforcement.

## Core Components (7 packages, 5 languages)
1. **Agent OS:** Stateless policy engine acting as a "kernel" for agents. Intercepts actions at <0.1ms p99 latency. Supports YAML, OPA Rego, and Cedar.
2. **Agent Mesh:** Cryptographic identity (DIDs with Ed25519) and the Inter-Agent Trust Protocol (IATP). Dynamic trust scoring (0–1000 scale).
3. **Agent Runtime:** Dynamic execution rings (CPU-style privilege levels), saga orchestration for transactions, and emergency kill switch.
4. **Agent SRE:** SRE practices (SLOs, error budgets, circuit breakers, chaos engineering) applied to agent systems.
5. **Agent Compliance:** Maps agent behavior to regulatory frameworks (EU AI Act, HIPAA, SOC2) and collects evidence for OWASP risk categories.
6. **Agent Marketplace:** Manages plugin lifecycles with Ed25519 signing and supply-chain security.
7. **Agent Lightning:** Governs Reinforcement Learning (RL) training to ensure zero policy violations during reward shaping.

## OWASP Risk Mitigation Mapping
- **Goal hijacking:** Semantic intent classifier
- **Tool misuse:** Capability sandboxing and MCP security gateway
- **Identity abuse:** DID-based identity and behavioral trust scoring
- **Memory poisoning:** Cross-Model Verification Kernel (CMVK) with majority voting
- **Cascading failures:** Circuit breakers and SLO enforcement
- **Rogue agents:** Ring isolation and automated kill switches

## Supported Frameworks
LangChain, CrewAI, AutoGen, Microsoft Agent Framework, OpenAI Agents SDK, Haystack, LangGraph, PydanticAI, LlamaIndex.

## Deployment
- Azure Kubernetes Service (AKS) as sidecar container
- Microsoft Foundry Agent Service (built-in middleware)
- Azure Container Apps (serverless)
- Python: `pip install agent-governance-toolkit[full]`
- TypeScript: `@microsoft/agentmesh-sdk` (npm)
- .NET: `Microsoft.AgentGovernance` (NuGet)

## Design Philosophy
- **Statelessness:** Enables horizontal scaling and auditability
- **Security by Default:** Governance built into execution path
- **Dynamic Trust:** Behavioral decay and privilege assignment instead of binary trusted/untrusted

## Project Maturity
- 9,500+ tests with continuous fuzzing (ClusterFuzzLite)
- SLSA-compatible build provenance, OpenSSF Scorecard tracking
- Planned move to a foundation home for community stewardship
