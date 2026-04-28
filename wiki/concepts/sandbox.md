---
title: "Sandbox (Agent Sandboxing)"
type: concept
tags: [sandbox, agent-security, isolation, mcp]
status: L3
created: 2026-04-27
updated: 2026-04-28
aliases: [Agent Sandboxing, AI Sandbox, Code Sandbox]
related: [[concepts/agent-sandboxing]], [[concepts/agentic-security]], [[concepts/capability-based-security]], [[concepts/excessive-agency]]
sources: [https://firecracker-microvm.github.io/, https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/security]
---

# Sandbox (Agent Sandboxing)

## Summary

Sandboxing for AI agents is the practice of executing untrusted agent code in isolated, resource-constrained environments to prevent malicious or erroneous actions from affecting the host system. The 2025-2026 era has seen a shift from Docker-based isolation toward hardware-enforced isolation using microVMs (Firecracker, gVisor) and the adoption of the Model Context Protocol (MCP) as the standard interface between agents and external resources, providing protocol-level security boundaries alongside runtime isolation.

## Key Ideas

- **Defense in Depth**: Agent sandboxing should layer multiple isolation mechanisms — runtime sandbox (Firecracker/gVisor), filesystem restrictions (read-only root, bind mounts), network controls (no egress by default), and permission systems (capability-based security)
- **MicroVM Isolation**: Firecracker (AWS) and gVisor (Google) provide lightweight virtual machine isolation that combines the security of VMs with the efficiency of containers — each agent runs in its own microVM with no shared kernel
- **MCP as Security Boundary**: The Model Context Protocol (MCP) defines a standardized interface between agents and tools/servers. This creates a natural security boundary — agents can only access resources exposed through MCP servers, and server operators can enforce access controls, rate limits, and audit logging
- **Capability-Based Security**: Moving from identity-based access control (who the agent is) to capability-based (what tokens the agent holds) — an agent can only perform actions for which it possesses an unforgeable capability token
- **Code Execution Sandbox**: For coding agents (Claude Code, Codex, Devin), code execution happens in isolated containers with no network access, limited filesystem, and automatic cleanup after execution

## Terminology

- **Firecracker**: AWS-built microVM hypervisor using KVM, designed for running lightweight VMs (~5ms startup, ~5MB memory overhead per VM)
- **gVisor**: Google's application kernel that provides a security boundary between the host OS and sandboxed processes, intercepting system calls
- **MCP (Model Context Protocol)**: Anthropic-originated protocol standardizing how AI agents connect to external tools and data sources, creating a natural security boundary
- **Excessive Agency**: OWASP Top 10 for LLMs vulnerability where an agent has more permissions than needed — sandboxing is a key mitigation
- **No Egress Default**: Network isolation principle — agents can't initiate outbound connections unless explicitly permitted

## Examples/Applications

- **Coding Agents**: Claude Code and Codex execute generated code in disposable Docker containers with no network access, preventing data exfiltration or system modification
- **Browser Automation**: browser-use and Playwright MCP run browser instances in isolated containers, preventing access to the user's actual browser data or credentials
- **Multi-Tenant Agent Platforms**: Claude Managed Agents and OpenAI Responses API run each customer's agents in separate microVMs with Firecracker
- **Plugin/MCP Server Isolation**: Each MCP server runs in its own sandboxed process, preventing a compromised server from affecting other servers or the agent runtime

## Related Concepts

- [[agent-sandboxing]]
- [[agentic-security]]
- [[capability-based-security]]
- [[excessive-agency]]
- [[defense-in-depth]]

## Sources

- [Firecracker MicroVM | AWS](https://firecracker-microvm.github.io/)
- [Claude Code Security | Anthropic Docs](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/security)
- [gVisor: Application Kernel for Containers | Google](https://gvisor.dev/)
