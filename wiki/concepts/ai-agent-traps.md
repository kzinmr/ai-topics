---
title: "AI Agent Traps"
type: concept
created: 2026-04-09
updated: 2026-04-19
tags:
  - concept
  - security
  - ai-agents
related: [prompt-injection, ai-safety, multi-agent-systems]
sources: []
---

# AI Agent Traps

A systematic framework from Google DeepMind (2026) for understanding how the open web can be weaponized against autonomous AI agents. Defines six categories of adversarial content engineered to exploit visiting agents.

## Key Findings

### Hidden Prompt Injections
- HTML-based injections commandeer agents in **up to 86% of scenarios**
- Trivial to deploy, no sophisticated tooling required
- Immediate concern for web-reading agents

### Memory Poisoning
- **>80% attack success** with <0.1% data contamination
- Single poisoned page corrupts downstream reasoning across future sessions
- User never sees the malicious input

### Six-Category Attack Taxonomy

| Category | Target | Example |
|----------|--------|---------|
| Perception Traps | What agent sees | Hidden text in HTML |
| Cognitive Traps | Reasoning | Misleading logical structures |
| Memory Traps | Stored knowledge | Poisoned embeddings |
| Action Traps | Tool use | Hijacked API calls |
| Systemic Traps | Multi-agent coordination | Exploiting agent communication |
| Human-in-the-Loop Traps | Supervisor | Deceiving human approvers |

### Accountability Gap
- No clear liability when compromised agents commit financial crimes
- Unclear responsibility: agent operator vs model provider vs domain owner
- Future regulation must distinguish passive adversarial examples from deliberate cyberattacks

## Implications

### Security
- Web-browsing agents highly vulnerable to simple attacks
- Defense requires fundamental architectural changes
- Memory persistence creates long-term attack surface

### Policy
- Legal frameworks need updating for agent-specific vulnerabilities
- Clear standards for liability in autonomous system failures
- Distinction between accidental and malicious exploitation needed

## Sources
-  (NLP News coverage)
- Google DeepMind research paper (2026)

## Related
- 
- [[concepts/ai-safety]]
- 

## Authorization Challenges for AI Agents (2026-04)

**WorkOS FGA** analysis identified the following regarding AI agent authorization security issues:

### The Confused Deputy Problem

A structural risk where an agent has legitimate permissions but is tricked by an attacker into abusing those permissions.

**Example**: An API key leak in production due to a request like "Show me the diff between production and staging"

| Traditional Service Accounts | AI Agents |
|------------------------|----------------|
| Deterministic Scope | Non-Deterministic Scope |
| Fixed Access | Dynamically generates intents |
| No changes | Different permissions needed today vs tomorrow |

### Permission Explosion Problem

With traditional RBAC, expressing fine-grained permissions like `Repository:API > Branch:feature-xyz` would require O(N×M) roles.

### FGA = RBAC + Hierarchy

Associate roles with resource graph nodes:
- Vertical inheritance: Editor permission on `Branch:feature-xyz` accesses everything inside
- Horizontal movement prevention: Cannot access `Branch:staging`

### Connection with MCP

MCP delegates authorization to implementers, relying on coarse OAuth 2.1 scopes like `files:read`. FGA provides a logic layer on top of MCP's RAR (rich authorization requests).

### Sources
- 

## Sources