---
title: "Agentic Security"
type: concept
status: incomplete
description: "Agentic security encompasses the security patterns, protocols, and tools for protecting AI agents, MCP servers, and the agent-to-API communication layer."
created: 2026-04-27
updated: 2026-04-28
tags: [concept, security, agents, mcp, api-security]
aliases: [AI agent security, MCP security, agent stack security]
related: [[concepts/model-context-protocol-mcp]], [[entities/salt-security]], [[concepts/sandbox]], [[concepts/ai-agent-traps]]
---

# Agentic Security

## Summary

**Agentic security** is the emerging discipline of securing the AI agent stack: protecting LLM-powered agents, the Model Context Protocol (MCP) servers they interact with, and the agent-to-API communication layer. As agents gain autonomy to execute code, access files, and call APIs, traditional security models are insufficient — new attack surfaces emerge including tool poisoning, indirect prompt injection, and credential theft.

## Key Attack Surfaces

### 1. MCP Server Vulnerabilities
- **CVE-2025-6514**: Critical RCE vulnerability in `mcp-remote` discovered by JFrog Security Research (July 2025)
- Tool poisoning attacks where adversaries compromise MCP server responses to manipulate agent behavior
- CoSAI (Coalition for Secure AI) released an extensive taxonomy for MCP security in January 2026

### 2. Prompt Injection
- **Indirect prompt injection** via web content: agent reads compromised pages that inject malicious instructions
- Microsoft Security published guidance on protecting against indirect prompt injection attacks in MCP (April 2025)
- Google's Project Glasswing / Claude Mythos offers defensive research into agent-secure architectures

### 3. API Security
- Salt Security Research (April 2026): As AI agents outpace security, most organizations face an unsecured API surge
- Salt Security launched "industry's first Agentic Security Platform for the AI Stack" (March 2026)
- Agent-to-API traffic must be monitored, rate-limited, and authenticated differently from human API usage

### 4. Code Execution
- Sandboxed execution environments (Docker, gVisor, Firecracker microVM)
- Tool-use enforcement and credential scoping
- Capabilities-based security model (zero-initial, grant-granted)

### 5. Package Security for AI Agents (Nesbitt.io, April 2026)

[[bradford-morgan-white]] (Nesbitt.io) identified a critical gap: **AI agents install packages without understanding security implications**. Key findings:

- Agents will blindly `pip install` or `npm install` packages that may be malicious
- Package registries lack AI-specific security signals (agents can't evaluate "is this package safe?")
- **Supply chain attacks on agents** are emerging: typosquatting, dependency confusion, and malicious code injection in widely-used packages
- Agents have **wider blast radius** than humans — they install across more packages, faster, with less scrutiny
- Pagination and discovery mechanisms in registries make it hard for agents to verify package authenticity
- **Stages of package installation** (discovery → verification → install → runtime) each have distinct vulnerabilities when performed by agents

Recommended mitigations:
- **Allow-listing** — agents should only install from vetted package sources
- **Sandboxed installs** — run package installation in isolated environments ([[concepts/agent-sandboxing]])
- **Static analysis** — scan packages before installation, not after
- **Human-in-the-loop** — require approval for new package installations
- **Package signature verification** — verify publisher identity before install

## Industry Response

| Organization | Contribution |
|-------------|-------------|
| **Salt Security** | Agentic Security Platform: monitors LLMs, MCP servers, and APIs |
| **CoSAI** | Released MCP Security Taxonomy (January 2026) |
| **OWASP** | LLM AI Security and Governance Checklist |
| **NIST** | AI Risk Management Framework |
| **Invariant Labs** | Tool Poisoning Attacks research |
| **Akto** | Full-stack agentic AI security platform |
| **Prompt Security** | Agent monitoring and guardrails |

## Related Concepts

- [[concepts/model-context-protocol-mcp]] — The protocol that agents use to communicate with tools
- [[concepts/sandbox]] — Isolated execution environments for AI agents
- [[concepts/ai-agent-traps]] — Google DeepMind's framework for adversarial web content targeting agents
- [[concepts/capabilities-based-security]] — Zero-initial, capability-granted security model

## Sources

- [Salt Security: Agentic Security Platform](https://salt.security/newsroom)
- [CoSAI: Securing the AI Agent Revolution — MCP Security Guide](https://www.coalitionforsecureai.org/securing-the-ai-agent-revolution-a-practical-guide-to-mcp-security)
- [The Hidden Dangers of AI Agents: 11 Critical Security Risks in MCP](https://medium.com/@jbalaji.ai/the-hidden-dangers-of-ai-agents-11-critical-security-risks-in-model-context-protocol-mcp-d2f659b57fc5)
- [Akto: AI Security Platform Explained](https://akto.io/blog/ai-security-platform)
