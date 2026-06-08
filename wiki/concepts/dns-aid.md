---
title: DNS-AID
created: 2026-05-29
updated: 2026-05-29
type: concept
tags:
  - concept
  - protocol
  - infrastructure
  - ai-agents
  - mcp
  - security
sources: [raw/articles/2026-05-27_linux-foundation-dns-aid.md]
---

# DNS-AID: Decentralized AI Agent Discovery

DNS-AID (DNS for AI Discovery) is an open-source protocol and reference implementation that enables secure, decentralized discovery and communication between AI agents and [[concepts/mcp|Model Context Protocol (MCP)]] servers. It leverages the internet's existing Domain Name System (DNS) infrastructure to provide a vendor-neutral, globally scalable directory for the emerging agentic web.

Launched by the **Linux Foundation** on May 27, 2026, and initially developed by Infoblox, DNS-AID addresses the critical bottleneck of agent discovery in an increasingly multi-agent world.

## Problem

AI agent discovery is currently fragmented, relying on:
- Hardcoded URLs or IPs
- Proprietary, centralized registries
- Manual configuration
- "Shadow AI" risks where unvetted agents operate unseen

## How It Works

DNS-AID uses standard DNS records (especially `SVCB` and `HTTPS` records) as a discovery mechanism:
1. Agents publish their capabilities via DNS records
2. Other agents query DNS to discover available services
3. Trust is bootstrapped through DNS-linked attestations, AgentCards, and identity mechanisms

## Components

- **Python SDK**: For developers to integrate agent discovery
- **CLI**: For scripting and testing
- **MCP Server**: Ready-to-run discovery server
- **Implementation-agnostic**: Works with any DNS provider, no vendor lock-in

## Initial Supporters

Cloudflare, CSC, Equinix, GoDaddy, Indeed, Infoblox, Internet Systems Consortium (ISC), WWT.

## Significance

DNS-AID represents a "web-native" approach to AI infrastructure — using the internet's most ubiquitous and trusted infrastructure (DNS) as the foundation for agent routing. This mirrors how the web itself was built on DNS for human-readable addressing.

Key advantages:
- **Decentralization**: No single operator owns the directory
- **Global scalability**: DNS already serves the entire planet
- **Trust bootstrapping**: Links to AgentCards, attestations, identity mechanisms
- **Security**: Enables policy enforcement, verification, and monitoring

## Quotes

> "The Internet already solved the discovery problem decades ago with DNS — it's fast, it scales globally, and every network on earth understands it. By extending this proven architecture to the agentic web, DNS-AID provides the foundational routing layer that autonomous systems need to operate safely and efficiently." — **Dane Knecht**, CTO, Cloudflare

> "The agentic internet is going to be built on the same DNS and public-CA infrastructure that carried the human web for 30 years, and that works because no single operator owns it." — **Scott Courtney**, VP Engineering, GoDaddy

## Related Pages

- [[concepts/mcp]] — Model Context Protocol for AI tool integration
- [[concepts/agent-infrastructure]] — AI agent infrastructure landscape
- [[concepts/ai-agents]] — AI agents overview
- [[concepts/agent-communication-protocol]] — Agent communication protocols
- [[entities/cloudflare]] — Cloudflare, initial supporter
