---
title: "Trigger.dev Environment Variable Exposure (Nov 2026)"
type: concept
created: 2026-11-02
updated: 2026-11-02
tags:
  - incident-report
  - vulnerability
  - ai-infra-security
  - ci-cd-security
confidence: high
status: active
sources:
  - raw/articles/2026-11-02_triggerdev_security-disclosure-env-vars.md
related:
  - concepts/software-supply-chain-security
  - concepts/ai-supply-chain-security
---

# Trigger.dev Environment Variable Exposure (Nov 2026)

On Sunday **2026-11-01**, Trigger.dev — the AI-agent task platform (16.7k GitHub stars, "Build and deploy invincible AI agents") — disclosed a security incident in which **an attacker gained unauthorized access to environment variables across a subset of customer organizations** (CTO Eric Allam's disclosure). The exploit was blocked and impacted account owners were emailed rotation steps; no vulnerability class, timeline, or scope was published with the disclosure.

## The "Resolved" controversy

The status page marked the incident **Resolved** almost immediately, which drove the HN thread (95 pts) and became the story's real subject:

- "Yeah we exposed your env vars but we told you about it over email so it's all good... We don't know how or to what extent though" (corvad).
- Industry norm cited (eddythompson80): Mitigated→Resolved should require a postmortem, repair items, and safeguards — not just exploitation-stopped.
- Formal counter (Traubenfuchs): "They are no longer exposing anything, so they no longer have an incident. Their customers now have an incident that will be resolved once their secrets are rotated" — the definitional gap between *platform incident* and *customer incident*.
- Attack-vector speculation in-thread ranged from the month's Linux TCP use-after-free (CVE-2026-98432, CVSS 9.8, HN 716 pts) to the ongoing wave of developer-tooling supply-chain attacks — undisclosed vector, unresolved.
- AI-angle sidebar (asdfsa32 vs Kiro): whether agent-written code is behind the rising SaaS incident volume — "there's a difference between using AI to find bugs and using AI to write bug-free software; AI is as good as the operator."

## Why it matters

- **Secrets remain the soft underbelly of the AI-platform supply chain**: an agent-execution platform's env vars gate every customer's cloud/API estate; a flat read of a subset is a multi-tenant blast radius.
- The disclosure pattern — *blocked exploit, no vector, instant Resolved* — is the same posture criticized in prior 2026 incidents and is hardening community expectations: no postmortem, no resolution.
- For agent-platform operators specifically: env-var exposure in a durable-execution service can compromise not just secrets but the *task definitions and prompts* replayed against them.

## Related

- [[concepts/software-supply-chain-security]] — developer-tooling attack surface
- [[concepts/ai-supply-chain-security]] — AI-tooling-specific supply chain

## Sources

- https://trigger.dev/blog/security-incident-nov-2026
- HN: https://news.ycombinator.com/item?id=50331784
