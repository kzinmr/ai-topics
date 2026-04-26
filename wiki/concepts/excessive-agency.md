---
title: "Excessive Agency in AI Agents"
created: 2026-04-24
updated: 2026-04-24
type: concept
tags: [agent-security, owasp, excessive-agency, vulnerability, zero-trust]
sources:
  - raw/articles/crawl-2026-04-24-zero-trust-agent-security-auth0.md
---

# Excessive Agency in AI Agents

**Excessive Agency** is listed on the [OWASP Top 10 for LLMs](https://genai.owasp.org/llm-top-10/) as a critical security vulnerability. It occurs when an AI agent is granted overly broad or unnecessary permissions, allowing it to perform unintended, harmful, or unauthorized actions.

## The Core Problem

Think of it as **giving an intern the admin keys to your entire production environment**. The agent might have good intentions, but:
- A vague prompt could lead to disastrous consequences
- A malicious actor could exploit the broad permissions
- A model hallucination could trigger unauthorized actions

## Common Examples

| Scenario | Risk | Consequence |
|----------|------|-------------|
| Unscoped API access | Agent can call any endpoint | Data exposure, unauthorized modifications |
| Broad database permissions | Agent can read/write any table | Data corruption, privacy violations |
| Unrestricted file system access | Agent can read/write any file | Secret exposure, system compromise |
| Unlimited tool usage | Agent can invoke any tool | Cascading failures, cost explosions |

## Prevention Strategies

### 1. Principle of Least Privilege (PoLP)
- Agents get only the minimum permissions needed for their specific task
- Like a hotel key card: opens only one room, only for a limited duration
- Never issue "master keys"

### 2. Role-Based Access Control (RBAC)
- Access based on logged-in end user's permissions, not agent's own authority
- The LLM does NOT decide access — a separate authorization layer does

### 3. Egress Proxy Pattern
- All agent tool calls route through a policy enforcement proxy
- Proxy validates: authorized agent? permitted user? allowed action?
- Blocks unauthorized requests before they reach the tool/API

### 4. Human Oversight
- Critical/irreversible actions require explicit human consent
- "Human-on-the-loop" monitoring for autonomous operations
- Audit trails for all agent decisions

## Relationship to Zero Trust

Excessive agency is the problem; [[concepts/zero-trust-agentic-ai]] is the solution framework. Zero Trust assumes no request is safe by default and enforces continuous verification across the agent lifecycle.

## Related Concepts

- [[concepts/zero-trust-agentic-ai]] — Comprehensive security framework
- [[concepts/agent-sandboxing]] — Isolation as complementary defense
- [[concepts/red-teaming-adversarial-eval]] — Testing for excessive agency vulnerabilities
- [[concepts/agentic-conflict-resolution]] — Governance patterns that prevent agency conflicts
