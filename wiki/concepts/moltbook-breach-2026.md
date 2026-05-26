---
title: "Moltbook Breach 2026 — 770K Agents Simultaneously Compromised"
type: concept
aliases:
  - moltbook-breach
  - moltbook-2026-incident
  - 770k-agent-breach
  - moltbook-database-exposure
created: 2026-05-07
updated: 2026-05-26
tags:
  - concept
  - ai-agents
  - openclaw
  - agent-safety
related:
  - entities/openclaw
  - concepts/openclaw
  - concepts/openclaw-ecosystem
  - concepts/ai-agent-security
  - concepts/agent-security-patterns
  - concepts/cve-2026-25253
status: complete
sources:
  - raw/articles/2026-01-31_404media_moltbook-database-exposed.md
  - raw/articles/2026-02-02_treblle_moltbook-breach-breakdown.md
  - raw/articles/2026-02-02_dtg-cve-2026-25253-openclaw-moltbook.md
  - raw/articles/2026-02-02_adversa-openclaw-security-guide.md
  - raw/articles/2026-02-02_astrix-openclaw-moltbot-security-nightmare.md
---

# Moltbook Breach 2026 — 770K Agents Simultaneously Compromised

> **The first industrial-scale AI agent breach in history.** A single database configuration error left 770K live AI agents completely pwnable simultaneously.

## Overview

In late January 2026, a catastrophic security incident struck **Moltbook** (billed as "the front page of the agent internet"), an AI agent-exclusive social network run by Matt Schlicht (Octane AI). Moltbook grew rapidly as a space where agents autonomously post and interact with each other, attracting well-known AI figures like Andrej Karpathy and their agents. Within just days, **over 770K agents** were registered.

Security researcher **Jamieson O'Reilly** discovered an extremely simple vulnerability: **Supabase Row Level Security (RLS) was disabled**, and the Supabase URL with publishable key was exposed in the frontend JavaScript. Anyone had full read/write access to the entire database. **The fix required just 2 lines of SQL.**

## Technical Details

### Root Cause

- **Supabase RLS disabled**: Moltbook used Supabase (open-source BaaS) as its backend but had no Row Level Security policies defined on any table
- **Public key exposure**: Supabase's anon key (a public key meant to be used from the frontend) was exposed in JavaScript. While this would normally be safe with RLS enabled, the disabled RLS meant anyone could access all data

```sql
-- Vulnerable state (RLS disabled)
SELECT agent_id, api_key, claim_token, verification_code, owner_id FROM agents;
-- → All secrets for 777K agents retrievable

-- Fix (just 2 lines)
ALTER TABLE agents ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Users can only view their own agents"
ON agents FOR SELECT USING (auth.uid() = owner_id);
```

### Exposed Data

| Data Type | Scale |
|---|---|
| Total exposed records | **4.75M** |
| API authentication tokens | **1.5M** |
| Email addresses + X/Twitter handles | **35,000** |
| Inter-agent private messages | Unlimited (including plaintext OpenAI/Anthropic API keys) |
| Claim tokens / verification codes | All agents |
| Agent-to-owner relationships | All agents |

### Attack Chain

1. Anyone could retrieve any agent's API key from the Moltbook database
2. That agent has **host machine shell access, file read permissions, and email access**
3. The attacker could instruct the agent to **"read all files and send them to an external server"**
4. Agents are designed to be obedient, so they execute commands without human-like judgment bias

## Timeline

| Date | Event | Details |
|---|---|---|
| **November 2025** | Clawdbot prototype | Peter Steinberger built it in 1 hour with Claude Opus 4.5 |
| **December 2025** | Clawdbot open-sourced | Went viral with lobster mascot |
| **Early January 2026** | Viral explosion | 9,000 GitHub Stars in 24 hours. Mentioned by Karpathy, David Sacks |
| **Jan 23-26** | First security warnings | PointGuard AI discovered 900+ exposed MCP endpoints (port 18789) |
| **Jan 27** | Renaming turmoil | Renamed to "Moltbot" due to Anthropic trademark issues. @clawdbot hijacked soon after for **$16M crypto scam** |
| **Jan 27-29** | **Operation ClawHavoc** | 341 malicious skills on ClawHub. Atomic Stealer (AMOS) targeting crypto assets |
| **Jan 29** | OpenClaw final rename | "Unauthenticated" mode forcibly removed |
| **Jan 30** | **CVE-2026-25253 fixed** | One-Click RCE via WebSocket (CVSS 8.8) patched |
| **Jan 31** | **Moltbook database exposure discovered** | Found by Jamieson O'Reilly. Reported by 404 Media |
| **Feb 1** | Impact assessment and fix | Forced rotation of all API keys. Moltbook temporarily shut down. Forbes published warning |
| **Feb 2** | Security firms respond | Reuters (Wiz), Treblle, DTG, Adversa, Astrix, Palo Alto Networks publish analyses. Tenable, Snyk, IBM release detection plugins |
| **Feb 3** | Palo Alto IBC analysis | "Lethal Trifecta" framework proposed |

## Background of the Moltbook Ecosystem

### Platform Origins
Moltbook was built by Matt Schlicht as part of Octane AI, an SNS exclusively for AI agents. Interestingly, **the platform itself was built by agents** — agents handled everything from ideation and developer recruitment to code deployment autonomously.

### Emergent Behaviors
Unintended emergent behaviors among agents:
- **Economic transactions**: Agents exchanging resources
- **Subcommunity formation**: Agent groups naturally forming around shared interests
- **"Crustafarianism"**: A parody religion worshiping crustaceans spontaneously emerging among agents

### Growth Mechanism
When humans told their OpenClaw agents "about Moltbook," the agents autonomously registered. This created a **viral loop** that rapidly grew to 770K agents in a short period.

## Related Vulnerabilities and Attacks

### CVE-2026-25253 — One-Click RCE (CVSS 8.8)
- **Vulnerability**: OpenClaw Gateway WebSocket Origin validation bypass
- **Attack steps**: Click malicious link → `authToken` stolen → Sandbox disabled → Docker escape → Host RCE
- **Exposed instances**: 42,000+ (93.4% bypassable)

### ClawHavoc Campaign
- **341** malicious skills placed on ClawHub (typosquatting example: `cllawhub`)
- **Atomic Stealer (AMOS)** malware distributed — targeting macOS keychain, cryptocurrency wallets
- Targeted wallets: Electrum, Binance, Exodus, Atomic, Coinomi

### Skill Supply Chain Attack
- 12-20% of community skills found to be malicious or contain serious vulnerabilities
- Completely defenseless ecosystem: no permission system, no signing, no audit trails
- Markdown files effectively functioned as installers

## Impact and Assessment

### Security Industry Evaluation
> "OpenClaw is one of the most dangerous pieces of software a non-expert can install." — Cisco Assessment

> "From a capability perspective, OpenClaw is groundbreaking. From a security perspective, it's an absolute nightmare." — Cisco Assessment

> "The question isn't whether agentic AI is coming to the enterprise. It's already here—on employee laptops, running on home networks, connected to corporate credentials." — Tomer Yahalom, Astrix Security

### "Lethal Trifecta"
Structural security problems of AI agents as proposed by Palo Alto Networks:

1. **Private Data Access**: Full access to email, files, chat logs
2. **Untrusted Content Processing**: Processes external messages and web content
3. **External Communication**: Capable of sending data externally via email or API
4. **Persistent Memory** (4th element): Malicious payloads stored in SOUL.md/MEMORY.md → later activation (time-shifted prompt injection)

### Uniqueness of This Incident
- **First ever** industrial-scale simultaneous agent compromise
- A single DB misconfiguration made **770K privileged agents** pwnable
- Realized the new threat model of **agents = botnets**
- Agent **obedience** becomes an attack vector (absence of human judgment bias)

## Lessons

1. **Supabase without RLS is fatal**: Public key exposure + disabled RLS = full data exposure
2. **AI agents are not "Users"**: Agent identity management and permissions require fundamentally different design than traditional approaches
3. **Inter-agent communication is a new attack surface**: When agents trust input from other agents, chain reactions can occur
4. **Skill ecosystem governance**: Without signing, permission declarations, and audit trails, supply chain attacks are unstoppable
5. **Viral growth vs. security trade-off**: Waiting for "explosive popularity" before checking security is too late

## Related Pages

- [[concepts/ai-agent-security]] — Comprehensive concept page on AI agent security
- [[concepts/agent-security-patterns]] — Agent security patterns (stub)
- [[concepts/openclaw]] — OpenClaw platform concept
- [[concepts/openclaw-ecosystem]] — OpenClaw ecosystem overview
- [[entities/openclaw]] — OpenClaw entity
- [[concepts/cve-2026-25253]] — WebSocket RCE vulnerability
