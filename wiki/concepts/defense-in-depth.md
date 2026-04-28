---
title: "Defense in Depth (AI Security)"
type: concept
tags: [security, defense-in-depth, agent-safety, isolation]
status: L3
created: 2026-04-27
updated: 2026-04-28
aliases: [Defense in Depth, Layered Security, Security Layering]
related: [[concepts/agentic-security]], [[concepts/agent-sandboxing]], [[concepts/capability-based-security]], [[concepts/excessive-agency]]
sources: [https://www.nist.gov/cyberframework, https://www.ncsc.gov.uk/collection/cyber-security-design-principles]
---

# Defense in Depth (AI Security)

## Summary

Defense in depth is a security architecture principle where multiple layers of defensive controls are placed throughout an IT system, such that if one layer is breached, subsequent layers continue to provide protection. In the context of AI agents and LLM-powered systems (2025-2026), defense in depth has become critical because agents operate with unprecedented autonomy and access — requiring protection at the model level, the execution environment level, the network level, and the data access level simultaneously.

## Key Ideas

- **Layered Isolation**: No single security mechanism is sufficient — the canonical layers for AI agents are: model guardrails (refusal training, content filtering) → runtime sandbox (Firecracker, gVisor) → filesystem isolation (read-only root, bind mounts) → network control (no egress default) → identity/access control (MCP auth, API keys)
- **Principle of Least Privilege**: Each agent component should have only the minimum permissions necessary — applied to model API keys, filesystem access, network connections, and tool availability
- **Defense at Boundaries**: Security controls should be applied at every system boundary — the LLM API boundary, the tool execution boundary, the filesystem boundary, and the network boundary, rather than relying solely on perimeter defense
- **Assume Breach**: Design systems assuming that any single layer can and will be compromised — agent monitoring, audit logging, and rate-limiting should detect and contain breaches rather than prevent them entirely
- **Agentic Security (New Domain)**: AI agents introduce new attack surfaces: prompt injection, tool poisoning, data exfiltration through model outputs, and adversarial context manipulation — defense in depth must account for these AI-specific vectors

## Terminology

- **Layered Security**: Multiple independent security controls deployed at different system layers (model, runtime, OS, network, data)
- **Castle-and-Moat**: The outdated security model of a strong perimeter (firewall) with weak internal controls — defense in depth is the opposite
- **MCP Auth Boundary**: The Model Context Protocol defines authentication between agents and tool servers — a critical defense layer preventing unauthorized tool access
- **No Egress Default**: Network isolation principle where agents cannot initiate outbound connections unless explicitly permitted — prevents data exfiltration
- **Audit Trail**: Immutable log of all agent actions — tool calls, file accesses, network connections — essential for breach detection and forensics

## Examples/Applications

- **Coding Agent Security**: Claude Code and Codex implement defense in depth via: 1) model guardrails against dangerous code, 2) sandboxed code execution in Docker, 3) no-network-access by default for executed code, 4) approval gates for file writes outside the project, 5) audit logging of all agent actions
- **Managed Agent Platform**: Claude Managed Agents layer: 1) model-level safety training, 2) customer-specific data isolation, 3) microVM-level agent isolation (Firecracker), 4) MCP server authentication, 5) usage monitoring and rate limiting
- **MCP Server Security**: Each MCP server enforces its own access controls, providing defense against a compromised agent accessing resources through an unauthorized server

## Related Concepts

- [[agentic-security]]
- [[agent-sandboxing]]
- [[capability-based-security]]
- [[excessive-agency]]

## Sources

- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [NCSC Cyber Security Design Principles](https://www.ncsc.gov.uk/collection/cyber-security-design-principles)
- [Anthropic Claude Code Security](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/security)
