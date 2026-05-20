---
title: "Cloudflare Sandbox (Claude Managed Agents)"
created: 2026-05-19
updated: 2026-05-19
type: entity
tags:
  - entity
  - cloudflare
  - sandbox
  - managed-agents
  - ai-agents
  - agent-architecture
  - agent-security
  - infrastructure
  - ai-infrastructure
  - browser-automation
  - serverless
  - virtualization
  - agent-sdk
  - security
  - orchestration
sources:
  - raw/articles/2026-05-19_cloudflare_claude-managed-agents-sandbox.md
---

# Cloudflare Sandbox (Claude Managed Agents)

**Cloudflare Sandbox** is Cloudflare's self-hosted sandbox environment for [[concepts/claude-managed-agents|Claude Managed Agents]] (CMA), launched May 19, 2026 in collaboration with [[entities/anthropic|Anthropic]]. It provides a Workers-based control plane that decouples the agent loop (running on Anthropic's platform) from code execution (running on Cloudflare's infrastructure), giving developers full control over sandbox security, observability, and tooling.

Note: this page covers Cloudflare's **external-facing CMA sandbox product**. For Cloudflare's internal AI engineering stack (iMARS), see [[concepts/cloudflare-agents]].

## Architecture

The integration uses a **Workers-based control plane** that receives messages from the Claude agent loop and provisions sandboxed environments per session. The control plane ships with a built-in dashboard UI, sandbox metrics and logs (shippable to Datadog or Splunk), and SSH access into running machines. State is automatically persisted across session sleeps.

Cloudflare uniquely offers **two sandbox primitives**:

1. **microVM sandboxes** (Cloudflare Containers) — full Linux environments for agent-as-developer workloads requiring CLI tools, package managers, and full application builds. Custom container images are supported.

2. **V8 isolate sandboxes** (AgentsSDK + Dynamic Workers via Codemode) — lightweight JavaScript isolates that boot in milliseconds, provide a filesystem, and can execute arbitrary code. Positioned as "a faster, cheaper, and more scalable alternative" for workloads that don't need a full Linux toolchain. These enable "bursts of tens of thousands of concurrent agents or more" at a scale no VM-based solution allows.

## Key CMA Integration Features

### Security: Proxy-Based Zero-Trust Credential Brokering

The standout security feature is **outbound proxy-based credential injection**. Secrets are injected into requests at the proxy layer, so the agent sandbox never has access to raw credentials. This protects against exfiltration attacks — even a compromised sandbox cannot extract secrets. Egress policies are definable per tenant, per agent, or per arbitrary metadata with endpoint allowlisting.

### Private Service Connectivity

Agents can connect to private internal services via **Cloudflare Mesh** and **Workers VPC** — post-quantum encrypted tunnels that require no VPN or bastion host. This allows agents to reach services running on AWS, on-premises, or behind NAT without exposing them to the public internet.

### Built-in Tool Suite

Cloudflare ships the richest out-of-the-box tool set among all [[comparisons/claude-managed-agents-sandbox-providers|CMA sandbox providers]]:

- **Browser Run** — Full browser automation with `browser_search`, `browser_execute`, `screenshot`, `browse`, `fetch_to_markdown`, and `web_fetch`. Includes session recording, allowlists/denylists, and audit trails.
- **Email tools** — `send_email`, `email_read`, `email_list`. Each agent gets its own email inbox; sessions can be kicked off via email.
- **Workers AI** — `image_generate` tool for on-platform image generation, complementing Claude's text-based inference.
- **Custom tools** — `defineTool()` with zod schemas for defining custom tools. Extensible with Cloudflare R2 (object storage), Artifacts (git-backed repos), and Dynamic Workers (deploy applications on the fly).
- **Private service calls** — `call_service` tool using Cloudflare Mesh or Workers VPC.

### Sandbox Observability

The control plane includes a built-in UI for tracking sandbox states, querying logs, and SSH-ing into specific machines. Logs can be shipped to external providers like Datadog or Splunk.

### Scale

Isolates enable running at "Internet scale" — booting sandbox backends in milliseconds without paying for full VM resources. MicroVMs are available when full Linux environments are needed. Instance sizes are configurable.

## Relationship to Cloudflare Developer Platform

The CMA sandbox integration leverages Cloudflare's broader Developer Platform: Workers (control plane), Durable Objects (stateful sessions), Agents SDK (agent framework), Browser Run (browser automation), Workers AI (edge inference), Cloudflare Mesh/VPC (private networking), and R2 (object storage).

## Related Pages

- [[concepts/claude-managed-agents|Claude Managed Agents]] — The Anthropic platform this integrates with
- [[comparisons/claude-managed-agents-sandbox-providers|CMA Sandbox Providers Comparison]] — Side-by-side comparison of all four providers
- [[concepts/cloudflare-agents|Cloudflare Agents (iMARS)]] — Cloudflare's internal AI engineering stack
- [[entities/cloudflare|Cloudflare]] — Parent organization
- [[entities/anthropic|Anthropic]] — Platform partner
- [[concepts/agent-sandboxing|Agent Sandboxing]] — Broader sandboxing patterns
