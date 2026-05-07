---
source: https://adversa.ai/blog/openclaw-security-101-vulnerabilities-hardening-2026/
title: "OpenClaw Security Guide 2026: Vulnerabilities & Hardening"
author: Adversa AI
date: 2026-02-02
tags:
  - openclaw
  - security
  - hardening
  - cve
  - moltbook
  - clawhavoc
---

# OpenClaw Security Guide 2026

## CVEs
- **CVE-2026-25253:** One-Click RCE (CVSS 8.8) — WebSocket origin validation bypass
- **CVE-2026-24763 & CVE-2026-25157:** Command injection in gateway input fields
- **CVE-2026-22708:** Indirect Prompt Injection via hidden CSS text on webpages

## Moltbook Breach
Supabase RLS disabled — exposed 1.5M API tokens and 35,000 emails.

## Hardening Recommendations
| Action | Implementation |
|--------|---------------|
| Update | v2026.1.29 or later |
| Auth | Set `gateway.auth.password` |
| Isolation | Docker with `--read-only` `--cap-drop=ALL` |
| Network | Bind to 127.0.0.1; use Tailscale for remote |
| Audit | `openclaw security audit --deep --fix` |

## The "Lethal Trifecta" (Simon Willison / Palo Alto Networks)
1. Access to Private Data
2. Untrusted Content Processing
3. External Communication Capability
4. Persistent Memory (time-shifted prompt injection via SOUL.md / MEMORY.md)

## Incident Timeline
- **Jan 23-26:** 900+ exposed MCP endpoints on Shodan (port 18789)
- **Jan 27:** Rebrand to Moltbot; $16M scam via hijacked @clawdbot Twitter
- **Jan 27-29:** ClawHavoc — 335+ malicious skills distributing AMOS
- **Jan 31:** Censys: 21,639 exposed instances (30% on Alibaba Cloud)
- **Feb 1:** Moltbook full database compromise
- **Feb 3:** Tenable, Snyk, IBM release detection plugins
