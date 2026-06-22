---
title: "WorkOS Auth.md — Open Protocol for Agent Registration"
created: 2026-06-16
updated: 2026-06-16
type: concept
tags:
  - concept
  - ai-agents
  - architecture
  - security
  - protocol
  - company
  - mcp
  - agent-native
  - agent-identity
sources:
  - https://workos.com/auth-md
  - https://daringfireball.net/2026/06/workos_launches_auth-md_an_open_protocol_for_agent_registration
---

# WorkOS Auth.md — Open Protocol for Agent Registration

**Auth.md** is an open protocol launched by WorkOS (June 2026) that enables AI agents to register users on behalf of their customers, bypassing traditional sign-up forms. It's designed for services that want agents to act as intermediaries for user authentication.

## Overview

Traditional authentication relies on users manually signing up for services. Auth.md recognizes that AI agents increasingly act as intermediaries — creating accounts, managing permissions, and performing actions on behalf of users. The protocol provides a standardized way for agents to:

1. **Register users** without human sign-up forms
2. **Verify agent identity** before granting access
3. **Manage permissions** for agent-mediated interactions
4. **Support identity provider patterns** where platforms' agents act on behalf of users

## Key Design Principles

- **Agent-first authentication**: The protocol treats agents as first-class citizens, not just automated scripts using user credentials
- **Open standard**: Designed for broad adoption across AI agent frameworks and platforms
- **Security model**: Maintains trust boundaries between agents, users, and services
- **Interoperability**: Works with existing identity infrastructure while enabling new agent-centric patterns

## Adoption Signals

- Featured on [Daring Fireball](https://daringfireball.net/2026/06/workos_launches_auth-md_an_open_protocol_for_agent_registration) (John Gruber, June 15, 2026)
- Positioning as the authentication standard for the agent era
- Competes with existing agent authentication patterns in MCP (Model Context Protocol) ecosystems

## Related Concepts

- [[concepts/mcp|MCP (Model Context Protocol)]] — Agent tool-calling protocol
- [[concepts/agent-identity]] — Agent authentication and verification
- [[concepts/security-and-governance/agent-iam]] — Agent identity and access management
