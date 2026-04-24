---
title: "Zero Trust for Agentic AI"
created: 2026-04-24
updated: 2026-04-24
type: concept
tags: [agent-security, zero-trust, excessive-agency, governance, identity]
sources:
  - raw/articles/crawl-2026-04-24-zero-trust-agent-security-auth0.md
  - raw/articles/crawl-2026-04-24-cisco-zero-trust-agentic-ai.md
---

# Zero Trust for Agentic AI

Zero Trust security model applied to AI agents: assume no request is safe by default, verify every action, and enforce least privilege. **The LLM should not be the one making security decisions.**

## Core Threat: Excessive Agency

**Excessive Agency** (OWASP LLM Top 10) occurs when an AI agent is granted overly broad permissions, allowing unintended, harmful, or unauthorized actions. Like giving an intern admin keys to production.

### Three Risk Dimensions

| Dimension | Challenge | Zero Trust Solution |
|-----------|-----------|-------------------|
| **Identity** | Agents as Non-Human Identities (NHIs) | Agent discovery, governance, lifecycle management |
| **Access** | Unscoped tool/API permissions | Role-Based Access Control (RBAC), OAuth2 with least privilege |
| **Behavior** | Machine-speed autonomous actions | Continuous verification, real-time policy enforcement |

## The Three Key Controls

### 1. Tool Access Authorization
- **Default:** No tool access
- **Grant:** Based on logged-in end user's permissions
- **Mechanism:** RBAC + ABAC (Attribute-Based Access Control)
- **Critical:** The LLM does NOT decide access — a separate authorization layer does

### 2. Secure API Authentication
- Agents authenticate with other services on behalf of users
- Use OAuth2 access tokens scoped to specific actions
- Never store credentials with broad permissions
- Implement token rotation and short-lived sessions

### 3. Human Oversight
- Critical/irreversible actions require explicit human consent
- "Human-on-the-loop" monitoring for autonomous operations
- Audit trails for all agent decisions
- Escalation paths for anomalous behavior

## Cisco Zero Trust Framework for Agentic AI

1. **Discover** — Catalog all agents (first-party, third-party, embedded)
2. **Identify** — Assign persistent agent identities with accountable owners
3. **Authorize** — Least-privilege access per agent role and task context
4. **Enforce** — Inline policy checks on every agent action
5. **Monitor** — Continuous behavioral analysis and anomaly detection

## Implementation Patterns

### The "Hotel Key Card" Model
- Agents get temporary, scoped access (like a hotel room key)
- Access expires automatically
- Different rooms (tools) require different keys
- Master keys are never issued

### Egress Proxy Pattern
- All agent tool calls route through a policy enforcement proxy
- Proxy validates: Is this agent authorized? Is this user permitted? Is this action allowed?
- Blocks unauthorized requests before they reach the tool/API

## Related Concepts

- [[agent-sandboxing]] — Isolation as a complementary security layer
- [[sandbox]] — Execution environment security
- [[agentic-conflict-resolution]] — Governance patterns for multi-agent systems
- [[agent-communication-protocols]] — Secure protocol design
- [[excessive-agency]] — The core vulnerability this addresses
