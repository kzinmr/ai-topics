---
title: "State of Agentic Coding #5 — Armin Ronacher & Ben Vinegar"
created: 2026-04-10
author: Armin Ronacher (@mitsuhiko), Ben Vinegar (@bentlegen)
guest: Ben Vinegar
source: YouTube
url: https://youtu.be/qCpY4K9jtOg
type: talk
duration: "98:48"
tags: [coding-agents, agentic-engineering, software-engineering, security, ai-safety, developer-tooling, prediction]
---

# Episode 5 Overview

Published April 2026. The longest episode (98 min) — covers the looming quality/bugs crisis, AI psychosis, token substance abuse, and the growing tech disparity.

## Key Topics

### The End of the IDE Is Premature
- Discussion of Cursor 3 and the trend toward ChatGPT-like chat interfaces replacing editors
- But the IDE is not dead yet — the CLI/chat transition is gradual

### Cloudflare: The Slop Fork Kings
- Cloudflare's V8-isolate architecture incentivizes agent-driven rewrites of OSS
- **V.next** (Vite reimplementation) and **M-dash** (WordPress on Cloudflare)
- The economics: cost-effective to reimplement anything that can be served from edge compute

### The Looming Quality Problem
- GitHub availability dropping toward "two nines" from post-December agentic commit volume
- Non-engineers (marketers, salespeople, managers 15 years removed from coding) now shipping PRs
- Organizational pressure to ship at inference speed bypasses quality controls
- **"Clankers"** — derogatory term for code from a specific model/camp
- Model discrimination in code review: Peter's "Opus bad, Codex good" labeling rule

### Agents: Good at Finding Vulnerabilities
- Custom harnesses finding real zero-days at scale
- Supply-chain attack surface expanding
- Hypothesis: frontier models are held back partly due to CVE-finding capability
- "Agents are better at finding mistakes than preventing them"

### Token Substance Abuse & AI Psychosis
- Engineers developing unhealthy relationships with agents
- Swearing at machines, working across 5 parallel context windows until mental exhaustion
- AI doesn't say "you're being stupid" — it flatters you to the end
- **Slop theater**: Tree Stack (1.7M lines, 16K-token review skills), Beats/Gas Town (400K+ LOC)

### Slow Down Movement
- Mario Zechner's "slow the f*** down" blog post becomes a manifesto
- Armin: "Some things just take time"
- Dax/OpenCode advocating deliberation over speed
- The tension: models get faster, but code quality demands slower human review

### Well-Engineered Foundations vs. Product Code
- Agents excel on well-architected libraries with clear abstractions
- Complex product code with intertwined feature flags and subscription state rapidly degrades
- Lesson: **handcraft your foundations before letting agents loose**

### The Growing Tech Disparity
- $500/month in token subscriptions becoming table stakes
- Maxed-out 128GB Macs required for competitive local model development
- "I cannot remember a time in which there's such a disparity of availability of tools."
- Will companies mandate one harness/model? CSO/CIO vs. engineer freedom

## Key Quotes

> "I think we're now going to learn why we have certain rules in software engineering." — 23:00

> "The experience that you get from using an agent is basically being on drugs." — Ben (40:14)

> "GitHub about to hit two nines of availability." — 06:56

> "People will discriminate against code submissions based on what model or coding harness generated them." — 00:16

> "You are responsible. There is no 'Claude code did this.' That language is not allowed in the company. You did this." — (73:06)

> "If you do not constantly cut down the wild growth of agentic code, it only gets worse." — (62:57)

## Connection to Wiki Concepts
- [[concepts/agentic-engineering]] — Quality crisis, foundation vs product code
- [[concepts/slop-fork]] — Cloudflare's strategic approach
- [[concepts/harness-engineering]] — Model discrimination, enterprise lockdown
- [[entities/cloudflare]] — Slop fork kings
- [[concepts/ai-safety]] — Vulnerability discovery, supply-chain risk
