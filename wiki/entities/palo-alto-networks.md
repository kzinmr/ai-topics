---
title: Palo Alto Networks
created: 2026-05-05
updated: 2026-08-12
type: entity
tags:
  - company
  - security
  - agent-safety
  - agent-security
  - agent-governance
  - control-plane
  - cybersecurity
  - agent-identity
aliases:
  - PANW
  - PAN
  - Palo Alto
  - Prisma
  - Cortex
  - Strata
sources:
  - raw/articles/2026-05-05_ai-agent-news-weekly-apr28-may4.md
  - https://en.wikipedia.org/wiki/Palo_Alto_Networks
  - https://www.paloaltonetworks.in/company/press/2026/palo-alto-networks-to-acquire-portkey-to-secure-the-rise-of-ai-agents
---

# Palo Alto Networks

**Palo Alto Networks, Inc.** (NASDAQ: PANW) is a global cybersecurity company headquartered in Santa Clara, California, serving over 70,000 organizations across 150+ countries, including 85 of the Fortune 100. Founded in 2005 by Nir Zuk (former Check Point and NetScreen engineer) and Rajiv Batra, the company built its franchise on next-generation firewalls and has platformized into network security, SASE, cloud security, security operations, and identity security. In the AI agent context, it is notable for its April 2026 acquisition of [[entities/portkey|Portkey]] — establishing the AI Gateway as a mission-critical control plane for autonomous agents and signaling that AI agent security is maturing into a core enterprise cybersecurity category.

## Company Overview

| Field | Value |
|-------|-------|
| Founded | March 2005 (Santa Clara, CA) |
| Founders | Nir Zuk, Rajiv Batra |
| CEO | Nikesh Arora (since June 2018; ex-Google, ex-SoftBank) |
| Revenue | $9.22B (FY2025), operating income $1.24B |
| Employees | ~16,068 (2025) |
| Listing | NYSE IPO July 2012 ($260M raised); moved to Nasdaq Oct 2021 |
| Market cap | Passed **$200B** for the first time in May 2026 |
| Threat research | Unit 42; hosts the Ignite security conference |

## AI Security Product Portfolio

Palo Alto Networks has reorganized its platform around the AI era, with a dedicated **Prisma AIRS (AI Runtime Security)** family as the AI Security platform:

| Family | Products | Role |
|--------|----------|------|
| **Prisma AIRS** | AI Gateway, AI Model Security, AI Red Teaming, AI Runtime Security, Agent Security, AI Posture Management | The AI Security Platform — secures GenAI tools, models, runtime, and agents |
| **Strata** | Next-Generation Firewall, Strata Cloud Manager, Next-Gen Trust Security | Network security (hardware + software + cloud-delivered) |
| **Prisma SASE** | Prisma Access (ZTNA), SD-WAN, Prisma Browser, SaaS Security, Enterprise DLP | Secure access for hybrid workforces |
| **Cortex** | Cortex XSIAM (AI-driven SOC), XDR, XSOAR, Attack Surface Management | Security operations ("fight AI with AI") |
| **Prisma Cloud** | AI-SPM, cloud security | Code-to-cloud protection |
| **Identity Security (Idira)** | Human, machine, and **agentic identities** | Zero-trust identity for the agent workforce |

## AI Agent Security Strategy

### Portkey Acquisition (announced April 30, 2026; close Q4 FY2026)

Palo Alto Networks agreed to acquire [[entities/portkey|Portkey]], "a pioneer in AI Gateways," which delivers a centralized control plane managing and protecting autonomous AI agents already processing **trillions of tokens per month**. Portkey becomes the **AI Gateway for Prisma AIRS** — described as "the central nervous system that can monitor, route, and secure every AI transaction across the enterprise."

The acquisition is framed as eliminating the trade-off between developer speed and security governance for autonomous agents, which "act as highly privileged insiders, executing a large volume of automated decisions across internal and external systems."

> "As autonomous agents join the enterprise workforce, they also become a new, unmanaged attack surface. By integrating Portkey into Prisma AIRS, organizations will be able to confidently deploy and govern AI agents. With Portkey, we are providing enterprises with visibility into all their agentic traffic, and enabling them to control and protect against agentic threats." — **Lee Klarich, Chief Product & Technology Officer, Palo Alto Networks**

> "Scaling AI in production requires a delicate balance between total flexibility for developers and absolute control for security teams. By joining Palo Alto Networks, we will establish the AI Gateway as the foundational layer of the secure AI enterprise." — **Rohit Agarwal, CEO & Co-Founder of Portkey**

Post-close, Portkey's capabilities anchor the **AI Identity Security** layer: strict least-privilege controls enforced on every agent interaction, with runtime prevention and governance policy enforcement.

### Strategic Position

The Portkey deal places Palo Alto Networks at the center of the [[concepts/security-and-governance/agentic-security|agentic security]] market — the same category where [[entities/palantir|Palantir]] and [[entities/servicenow|ServiceNow]] are building agent control infrastructure from the enterprise-software side. PAN's angle is security-native: gateway inspection, runtime enforcement, and identity control for agent fleets rather than agent orchestration.

## AI-Era Acquisitions (2025–2026)

Palo Alto Networks has executed an aggressive acquisition program to assemble an AI-era security platform:

| Deal | Announced | Completed | Value | Strategic role |
|------|-----------|-----------|-------|----------------|
| Protect AI | Jul 2025 | — | $500M | AI/ML supply chain security |
| CyberArk | Jul 2025 | Feb 2026 | $25B | Identity security (human + machine) |
| Chronosphere | Nov 2025 | Jan 2026 | $3.35B | Observability, unifying security & observability |
| Koi Security | Feb 2026 | — | ~$400M | Israeli security startup |
| **Portkey** | **Apr 2026** | Q4 FY2026 | undisclosed | AI Gateway / agent control plane |

The CyberArk ($25B) and Portkey deals together cover both halves of the agentic identity problem: **who** the agent is (identity, least privilege) and **what** the agent does (traffic inspection, runtime policy).

## Research & Threat Intelligence

- **Unit 42** — PAN's threat intelligence and incident-response team; helped solve the Mirai botnet and clickfraud cases, discovered Gorgon, Xbash, and "Cannon" (Fancy Bear) campaigns; publishes the MSRC-recognized technical reports and the North Korean remote-IT worker interview scripts (Nov 2024).
- **Vertex AI agent weaponization (April 2026)** — PAN researchers demonstrated how AI agents built on Google Cloud Vertex AI could be weaponized for malicious activity due to excessive permissions, prompting Google to address the issues. This research exemplifies the "agents as privileged insiders" threat model underlying PAN's agent security strategy.
- **China review (August 2026)** — China launched a security review of PAN's products in the Chinese market, a geopolitical headwind for the company.

## Connections

- Acquired [[entities/portkey|Portkey]] (April 2026) — the AI Gateway for Prisma AIRS
- Core vendor in [[concepts/security-and-governance/agentic-security|Agentic Security]] — protecting autonomous AI agents at enterprise scale
- Its AI Gateway / control-plane architecture is a concrete implementation of the [[concepts/security-and-governance/agent-control-plane|Agent Control Plane]] pattern
- Enforces [[concepts/security-and-governance/agent-iam|Agent IAM]] — identity and access management for non-human identities (incl. the $25B CyberArk acquisition)
- Addresses the [[concepts/shadow-ai-governance|Shadow AI Governance]] crisis (80% of Fortune 500 have lost control of AI infrastructure)
- Complements [[concepts/zero-trust-agentic-ai|Zero Trust Agentic AI]] architectures — least-privilege enforcement per agent interaction
- Fellow builders of agent control infrastructure: [[entities/palantir|Palantir]], [[entities/servicenow|ServiceNow]] (enterprise-software angle vs PAN's security-native angle)

## Sources

- [Wikipedia: Palo Alto Networks](https://en.wikipedia.org/wiki/Palo_Alto_Networks) — company history, financials, acquisitions (scraped 2026-08-12)
- [Press release: Palo Alto Networks to Acquire Portkey to Secure the Rise of AI Agents (Apr 30, 2026)](https://www.paloaltonetworks.in/company/press/2026/palo-alto-networks-to-acquire-portkey-to-secure-the-rise-of-ai-agents)
- Raw article: `raw/articles/2026-05-05_ai-agent-news-weekly-apr28-may4.md` — original acquisition notice
