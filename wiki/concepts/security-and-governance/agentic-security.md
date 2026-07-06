---
title: "Agentic Security"
type: concept
status: incomplete
description: "Agentic security encompasses the security patterns, protocols, and tools for protecting AI agents, MCP servers, and the agent-to-API communication layer."
created: 2026-04-27
updated: 2026-05-22
tags:
sources: []
  - concept
  - security
  - ai-agents
  - mcp
aliases: [AI agent security, MCP security, agent stack security]
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
| **Indirect prompt injection** via web content: agent reads compromised pages that inject malicious instructions
| **The Camel Paper approach**: A theoretical defense using two LLMs — one for policy decisions and one for data retrieval. However, this often breaks the agent's utility because it can no longer make decisions based on the data it reads. As discussed in the Pi podcast (Syntax #976): "there is no foolproof way to differentiate between a user's instruction and malicious data within the same context window."
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

### 7. Credential Management in Agent Sandboxes (Auth Proxy Pattern)

LangChain's LangSmith Sandboxes introduced an **Auth Proxy** pattern (May 2026) that moves credential handling out of the agent runtime entirely:

**Core principle**: Agents need the *effect* of a credential (the ability to call an API) — not *possession* of the credential itself.

**How it works**:
1. Agent/sandboxed code makes an outbound request
2. Auth Proxy intercepts it at the network layer (infrastructure-level, not HTTP_PROXY)
3. Proxy checks configured policy for the destination → blocks, allows, or injects headers
4. Request continues with injected credentials — agent never sees the API key

**Credential types**:
- `workspace_secret`: References platform-stored secrets
- `plaintext`: For non-sensitive headers
- `opaque`: Write-only, encrypted at rest, never retrievable
- `dynamic callbacks`: For OAuth tokens, per-user-scoped tokens, tokens needing refresh

**Key design decisions**:
- **Fail-closed**: If callback fails, reject the sandbox request (don't send without credentials)
- **Per-destination rules**: e.g., only allow `api.openai.com` + `api.github.com/repos/*`
- **Control plane outside runtime**: The proxy is infrastructure, not exposed to agent instructions

This pattern is critical because agents with credentials in the runtime have a wide exposure surface: every tool call, package install, log line, and file write is a possible credential leak path. Header injection moves credentials out of that blast radius.

Source: [[entities/langchain|LangChain]] — [Auth Proxy for LangSmith Sandboxes](https://x.com/i/article/2057309362889326593), May 2026

### 5. Package Security for AI Agents (Nesbitt.io, April 2026)

[[entities/bradford-morgan-white]] (Nesbitt.io) identified a critical gap: **AI agents install packages without understanding security implications**. Key findings:

- Agents will blindly `pip install` or `npm install` packages that may be malicious
- Package registries lack AI-specific security signals (agents can't evaluate "is this package safe?")
- **Supply chain attacks on agents** are emerging: typosquatting, dependency confusion, and malicious code injection in widely-used packages
- Agents have **wider blast radius** than humans — they install across more packages, faster, with less scrutiny
- Pagination and discovery mechanisms in registries make it hard for agents to verify package authenticity
- **Stages of package installation** (discovery → verification → install → runtime) each have distinct vulnerabilities when performed by agents

Recommended mitigations:
- **Allow-listing** — agents should only install from vetted package sources
- **Sandboxed installs** — run package installation in isolated environments ([[concepts/security-and-governance/agent-sandboxing]])
- **Static analysis** — scan packages before installation, not after
- **Human-in-the-loop** — require approval for new package installations
- **Package signature verification** — verify publisher identity before install

### 6. "Not a Security Issue" Policy Failures (Nesbitt.io, May 2026)

[[entities/bradford-morgan-white]] published a follow-up analysis identifying a critical organizational failure pattern: **"Not a Security Issue" as a threat model blind spot**.

The core argument: **the most dangerous vulnerabilities are the ones your threat model tells you to ignore**. Key points:

- Organizations routinely classify certain attack vectors as "not a security issue" — often because they fall outside traditional security boundaries
- This creates **systematic blind spots** where attackers exploit exactly the things defenders decided weren't worth protecting
- Example: supply chain attacks, social engineering of AI agents, and infrastructure misconfigurations are often dismissed because they don't fit neat CVE categories
- The "not a security issue" label becomes self-fulfilling: no budget, no monitoring, no response plan
- **AI agents amplify this risk**: they operate across traditional security boundaries (code, data, APIs, infrastructure) and can trigger cascading failures from a single misclassified vector

This is particularly relevant for agentic security because **agents routinely perform actions that span multiple security domains** — reading files, making API calls, executing code, accessing databases. A vulnerability in any one of these is trivially exploitable if the agent's threat model treats them as separate concerns rather than a unified attack surface.

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
