---
source: https://astrix.security/learn/blog/openclaw-moltbot-the-rise-chaos-and-security-nightmare-of-the-first-real-ai-agent/
title: "OpenClaw & MoltBot: The First AI Agent Security Nightmare"
author: Astrix Security
date: 2026-02-02
tags:
  - openclaw
  - moltbook
  - security
  - incident
  - shadow-ai
  - moltbot
---

# OpenClaw & MoltBot: The First AI Agent Security Nightmare

**Key Takeaway:** OpenClaw represents a new class of "Shadow AI" risk. Its ability to execute shell commands and manage corporate credentials creates massive remote access vulnerabilities.

## Timeline of Chaos

| Date | Event | Impact |
|------|-------|--------|
| Nov 2025 | Prototype built | Created in 1 hour by Peter Steinberger using Claude Opus 4.5 |
| Dec 2025 | "Clawdbot" launch | Open-sourced; rapid developer traction |
| Jan 2026 | Viral explosion | 9,000 GitHub stars in 24h; endorsed by Karpathy |
| Jan 25-27 | Security alarms | 900+ instances exposed on Shodan (port 18789) |
| Jan 27 | Rebrand disaster | Renamed to Moltbot due to Anthropic trademark issues |
| Jan 27 | $16M scam | Hijacked @clawdbot Twitter launched fake token |
| Jan 29 | OpenClaw rebrand | Removed "unauthenticated" mode |
| Jan 31 | Moltbook breach | 770,000 agents exposed to hijacking |

## Data Exposure Statistics (ClawdHunter scan)
- 42,665 publicly exposed instances
- 93.4% had critical authentication bypass
- 26% of third-party skills contained vulnerabilities
- Exposed: Anthropic API keys, Telegram bot tokens, Slack OAuth, full chat histories

## Enterprise Implications
1. Supply Chain Risk — 1 in 4 plugins are risky
2. Non-Human Identities (NHI) — agents use API keys that bypass MFA
3. Agent-to-Agent Attacks — unmonitored attack surface on Moltbook
