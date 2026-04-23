---
title: "Cybersecurity Proof of Work"
created: 2026-04-14
updated: 2026-04-14
tags: [concept, cybersecurity, llm-economics, claude-mythos, aisafety]
related:
  - concepts/claude-mythos-preview
  - concepts/ai-digital-nato
  - concepts/ai-observability
  - concepts/evals-for-ai-agents
---

# Cybersecurity Proof of Work

## Overview

A concept coined by Drew Breunig in April 2026, observing that as LLMs like **Claude Mythos** become increasingly effective at finding security vulnerabilities, cybersecurity transforms into an economic equation: **the side that spends more tokens on security review wins**.

## Core Insight

The UK's AI Safety Institute (AISI) independently evaluated Claude Mythos and confirmed Anthropic's claims that it is exceptionally effective at identifying security vulnerabilities. Crucially, AISI's methodology showed that **more tokens spent = more vulnerabilities found** — a continuous, scalable relationship with no apparent ceiling.

> *"If Mythos continues to find exploits so long as you keep throwing money at it, security is reduced to a brutally simple equation: to harden a system you need to spend more tokens discovering exploits than attackers will spend exploiting them."*
> — Drew Breunig, April 2026

## Economic Implications

### Defender's Advantage

Unlike traditional security where attackers have the advantage of choosing when and where to strike, LLM-powered security review creates a **defender's economic moat**:

1. **Scalable review** — Defenders can run Mythos (or similar models) against their entire codebase continuously
2. **Shared benefit** — Open source libraries become more valuable because token spending on their security is amortized across all users
3. **Asymmetric cost** — It's cheaper to find and fix a vulnerability proactively than to respond to an exploit

### Open Source Revaluation

This dynamic directly counters the narrative that low-cost "vibe coding" replacements threaten open source:

- Open source libraries gain a **new competitive advantage**: the security tokens spent reviewing them benefit every downstream user
- Commercial alternatives must independently spend tokens on their own security review
- The total cost of ownership for open source drops when security review costs are shared

## Connection to Claude Mythos

Claude Mythos (Anthropic's cybersecurity-focused model) sits at the center of this trend:

- **AISI evaluation** confirmed its exceptional vulnerability-finding capability
- **Project Glasswing** (Anthropic, April 7, 2026) restricts Mythos access to vetted security researchers
- The token-cost relationship means Mythos becomes more valuable the more you're willing to spend

## Industry Response

| Organization | Action | Date |
|--------------|--------|------|
| UK AISI | Independent evaluation of Mythos cyber capabilities | April 2026 |
| Anthropic | Project Glasswing — restricted Mythos access | April 7, 2026 |
| OpenAI | GPT-5.4-Cyber — cyber-permissive model variant | April 14, 2026 |
| Drew Breunig | Coined "Cybersecurity Proof of Work" concept | April 14, 2026 |

## OpenAI's Response: GPT-5.4-Cyber

OpenAI announced **GPT-5.4-Cyber**, a variant fine-tuned specifically for defensive cybersecurity use cases. This is part of their "Trusted Access for Cyber" program:

- Users verify identity via government-issued ID (processed by Persona)
- Verified users get "reduced friction" access to security tools
- Additional access requires a Google Form application (similar to Anthropic's Glasswing)
- OpenAI frames this as "democratizing access" to cybersecurity tools

## Broader Significance

This concept represents a fundamental shift in how we think about AI and security:

1. **Security as a compute problem** — Not just "can you find bugs?" but "how much are you willing to spend?"
2. **LLMs as force multipliers** — A single security engineer with Mythos can review more code than a team without
3. **Economic incentives align** — More spending = more security, creating a sustainable market dynamic

## Sources

- Simon Willison, "Cybersecurity Looks Like Proof of Work Now," simonwillison.net (April 14, 2026)
- Drew Breunig analysis of UK AISI's Claude Mythos evaluation
- UK AISI, "Our evaluation of Claude Mythos Preview's cyber capabilities"
- OpenAI, "Trusted access for the next era of cyber defense" (April 2026)
- Simon Willison, "Trusted access for the next era of cyber defense," simonwillison.net (April 14, 2026)

## See Also

- [[concepts/_index.md]]
- [[concepts/illusion-of-thinking.md]]
- [[concepts/cognitive-cost-of-agents.md]]
- [[concepts/back-of-house-multi-agent-patterns.md]]
- [[concepts/back-of-house-patterns.md]]
