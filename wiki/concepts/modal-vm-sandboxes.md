---
title: "Modal — VM Sandboxes and Infrastructure Updates"
created: 2026-06-16
updated: 2026-06-16
type: concept
tags:
  - concept
  - infrastructure
  - sandbox
  - serverless
  - modal
  - agent-safety
  - security
  - agent-architecture
  - agent-runtime
sources:
  - https://modal.com/blog/product-updates-vm-sandboxes-domain
  - https://modal.com
---

# Modal VM Sandboxes and Infrastructure Updates

**Modal** is a serverless cloud platform that announced significant infrastructure updates in June 2026, including **VM Sandboxes (Alpha)**, **lower latency routing**, and **RBAC** (Role-Based Access Control) enhancements.

## VM Sandboxes (Alpha)

The most significant development is Modal's new VM runtime for Sandboxes:
- **Real Linux VMs** — VM Sandboxes run actual Linux virtual machines, not containers
- **Full system isolation** — Complete OS-level separation between agent executions
- **Security boundary** — Harder for agents to escape sandbox constraints compared to container-based approaches
- **Alpha stage** — Currently in limited availability, indicating active development

This addresses a critical need in the agent ecosystem: **secure execution environments** for AI agents that can run arbitrary code without compromising the host system.

## Lower Latency Routing

Modal introduced regional routing to improve performance:
- **Multi-region support** — Functions can now run in US West, EU West, or Asia Pacific South
- **Reduced network latency** — Requests are routed closer to their origin
- **Data residency compliance** — Keeps data in-region for regulatory requirements
- **Single configuration setting** — Easy to enable per-function

## RBAC (Role-Based Access Control)

Enhanced security controls:
- **Fine-grained permissions** — Control access to Modal resources by role
- **Team management** — Better support for organizational use
- **Security compliance** — Meets enterprise security requirements

## Significance for AI Agents

These updates position Modal as a **production-ready infrastructure platform** for AI agent deployment:
1. **VM Sandboxes** solve the security problem of running untrusted agent code
2. **Regional routing** addresses latency concerns for real-time agent interactions
3. **RBAC** enables enterprise adoption with proper access controls

## Related Concepts

- [[concepts/agent-safety]] — Agent execution security and sandboxing
- [[concepts/agent-runtime]] — Infrastructure for running AI agents
- [[concepts/serverless]] — Serverless computing patterns
