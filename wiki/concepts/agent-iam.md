---
title: "Agent IAM — Non-Human Identity Security"
type: concept
description: "Identity and access management for AI agents — treating agents as Non-Human Identities (NHI) with ephemeral credentials, fine-grained authorization, and behavioral monitoring"
category: concepts
sub_category: AI Security
tags: [agent-iam, non-human-identity, security, authorization, SaaS, OAuth]
status: complete
created: 2026-04-30
updated: 2026-04-30
---

# Agent IAM — Non-Human Identity Security

## TL;DR

As AI agents proliferate, they become **Non-Human Identities (NHI)** that require dedicated identity and access management. Traditional IAM systems designed for humans are insufficient for agents that operate at machine speed, create ephemeral credentials, and access multiple SaaS APIs autonomously.

## The Problem

NHIs now **outnumber human identities 25-50x** in modern enterprises (2026), with the ratio accelerating as AI agent deployment scales. Traditional security controls fail because:

- **No MFA**: Agents don't have biometrics or physical tokens
- **24/7 operation**: No "normal" behavior patterns to detect anomalies
- **Indefinite persistence**: Credentials aren't rotated or revoked automatically
- **Lateral movement**: Agents can discover and exploit access paths developers never anticipated
- **Machine-speed identity creation**: Human approval processes can't keep up

## Key Players (2026)

| Company | Focus |
|---------|-------|
| **Astrix Security** | Agent IAM, NHI discovery and governance |
| **Zenity** | SaaS agent security, real-time policy evaluation |
| **WorkOS FGA** | Fine-grained authorization for agents across SaaS |
| **Auth0 for AI Agents** | Ephemeral credentials, scope-based access |

## Core Capabilities Required

### 1. Ephemeral Credentials
Agents should use **short-lived, automatically revoked credentials** rather than persistent API keys. This limits the blast radius if an agent is compromised.

### 2. Fine-Grained Authorization (FGA)
Instead of broad permissions, agents need **scope-based access**:
```
# Bad: agent has full SaaS access
token.scope = "admin"

# Good: agent has minimal required scope
token.scope = "calendar:read-only,user:read"
```

### 3. Real-Time Policy Evaluation
Policies must be evaluated **at agent runtime**, not just at authentication time. An agent might start with legitimate access but attempt unauthorized actions during execution.

### 4. Behavioral Monitoring
Unlike static NHIs (service accounts, CI/CD pipelines), AI agents are **autonomous and unpredictable**. Monitoring must detect:
- Unusual API access patterns
- Data exfiltration attempts
- Privilege escalation behavior

### 5. Kill Switch Capability
The ability to **immediately revoke all agent tokens** when anomalous behavior is detected. Latency must be under 50ms to prevent data loss.

## Architecture Pattern

```
┌─────────────────────────────────────────────────┐
│                   Agent IAM                      │
│                                                  │
│  ┌──────────────┐  ┌──────────────┐              │
│  │ Identity     │  │ Policy       │              │
│  │ Registry     │  │ Engine       │              │
│  └──────┬───────┘  └──────┬───────┘              │
│         │                 │                       │
│  ┌──────▼─────────────────▼───────┐               │
│  │  Credential Vault & Rotation   │               │
│  └──────────────┬─────────────────┘               │
│                 │                                  │
│  ┌──────────────▼─────────────────┐               │
│  │  Behavioral Monitor & Kill     │               │
│  │  Switch (< 50ms latency)       │               │
│  └────────────────────────────────┘               │
└─────────────────────────────────────────────────┘
```

## Relationship to Agent Architecture

Agent IAM is a critical component of **production-ready agent deployments**. Without proper identity management:

1. **Credential sprawl**: Untracked API keys across agents
2. **Privilege creep**: Agents accumulating unnecessary permissions over time
3. **Audit gaps**: Inability to trace which agent performed which action
4. **Compliance violations**: Data access that violates regulatory requirements

## See Also

- [[concepts/harness-engineering]] — Agent orchestration requires identity management
- [[concepts/ai-agent-security]] — Broader security considerations for agents
- [[concepts/fine-grained-authorization]] — FGA patterns for agent access control
