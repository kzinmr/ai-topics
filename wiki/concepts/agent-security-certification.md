---
title: "Agent Security Certification (AIUC-1)"
type: concept
created: 2026-08-20
updated: 2026-08-20
tags:
  - agent-security
  - agent-safety
  - agent-governance
  - enterprise-ai
aliases: ["AIUC-1", "AI Agent Security Certification", "Agent Security Certification"]
sources:
  - raw/articles/2026-08-18_cursor_aiuc-1.md
  - raw/articles/2026-08-18_elevenlabs_elevenlabs-mcp-in-claude.md
---

# Agent Security Certification (AIUC-1)

**AIUC-1** is the first certification standard for AI agent security, safety, and reliability. It pairs an audit of an organization's documented controls with live adversarial testing of the product itself, filling a gap that traditional security certifications leave open: existing schemes (SOC 2, ISO 27001) attest to how data is stored, protected, and governed, but say nothing about how an agent actually behaves when pushed into hostile or edge-case conditions.

## What It Covers

- **Standards basis**: developed with input from 100+ Fortune 500 CISOs and risk leaders, with technical contributions from MITRE, the Cloud Security Alliance, and Stanford researchers. It operationalizes existing frameworks — NIST AI Risk Management Framework, MITRE ATLAS, and the OWASP agentic threat taxonomy — into testable requirements for live AI systems
- **Coding-agent requirement areas**: secrets protection, secure code generation, MCP security, agent identity and permissions
- **Test methodology**: independent audit of documented controls plus adversarial testing across thousands of scenarios probing the limits of built-in safeguards (rules, hooks, auto-review), across benign and adversarial conditions, over two rounds
- **Recurring evaluation**: certification is not one-time. Holders are retested at least quarterly, with a full audit each year; the standard itself is updated quarterly, so the bar rises as agent capabilities and threat surfaces evolve
- **First authorized auditor**: Schellman, the first ANAB-accredited ISO 42001 certification body, serves as AIUC-1's first authorized auditor

## Adoption

- **Cursor** is the first certified product (announced Aug 13, 2026, blog post by Kenneth Moras). Cursor reported passing across both testing rounds with its safeguards holding under benign and adversarial conditions, in a representative enterprise configuration covering the IDE and cloud agent surfaces. Its report is published on trust.cursor.com. Cursor frames this alongside its SOC 2 Type II attestation, third-party penetration testing, bug bounty program, and work toward ISO 27001 / ISO 42001
- ElevenLabs published an explainer of AIUC-1 in the same period (Aug 18–20, 2026), signaling the standard is spreading beyond the first certifier into the broader agent platform ecosystem

## Significance

This is the agent-era analogue of SOC 2 for agent behavior: enterprises adopting coding and voice agents for consequential work need evidence that safeguards survive adversarial pressure, not just that controls are documented. Two properties make it structurally different from traditional compliance:

1. **Product-level testing, not document-level audit** — the agent itself is attacked, not just the org chart
2. **Quarterly re-certification** — the threat model for agents moves faster than the annual cycle traditional certifications assume

Open questions: whether other agent vendors (coding or voice) will seek certification, whether the quarterly audit cadence is sustainable, and whether "AIUC-1" numbering implies an evolving versioned standard from a standards body rather than a single vendor's initiative.

## Related Pages

- [[concepts/sandbox]] — runtime isolation as a complementary defense layer
- [[concepts/agent-safety]] — broader agent safety frameworks
- [[concepts/security-and-governance/agent-governance]] — governance structures for agent deployment
- [[concepts/security-and-governance/agent-iam]] — agent identity and permissions, an explicit AIUC-1 requirement area
- [[entities/cursor-ai]] — first certified product
- [[entities/elevenlabs]] — early ecosystem adopter of AIUC-1

## Sources

- [Cursor: Cursor earns AIUC-1 certification for agent security and reliability](https://cursor.com/blog/aiuc-1) (Aug 13, 2026) — `raw/articles/2026-08-18_cursor_aiuc-1.md`
- ElevenLabs AIUC-1 explainer (Aug 2026) — `raw/articles/2026-08-20_elevenlabs_what-is-aiuc-1.md` (scrape truncated; cross-referenced via [[entities/elevenlabs]])
