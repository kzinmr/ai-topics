---
title: "Threat Modeling"
type: concept
aliases:
  - threat-modeling
  - threat model
created: 2026-04-25
updated: 2026-11-18
tags:
  - concept
  - security
  - cybersecurity
  - ai-security
  - agent-security
  - software-engineering
  - web-security
  - vulnerability
sources:
  - https://owasp.org/www-community/Threat_Modeling
  - https://en.wikipedia.org/wiki/Threat_modeling
  - https://www.owasp.org/www-project-threat-dragon/
---

# Threat Modeling

**Threat modeling** is the structured practice of reasoning about a system *before* (or while) it is built, in order to enumerate what could go wrong, what an attacker would gain, and what defenses are proportionate. Where penetration testing finds vulnerabilities in a *built* system, threat modeling finds **missing designs** in an *imagined* one — it is a thinking discipline, not a tool, which is why it survives every change in the technology stack (including the agent stack this wiki tracks).

## Core Frameworks

| Framework | Abstraction | Mnemonic / method |
|-----------|------------|-------------------|
| **STRIDE** (Microsoft, 1999) | Per data-flow element | Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege |
| **PASTA** | Risk-centric, 7 stages | Attack → vulnerability → countermeasure → risk quantification |
| **Attack trees** (Schneier) | Goal-centric | AND/OR decomposition from attacker goal down to primitives |
| **Attack graphs / paths** | Network-centric | Composition of footholds (cf. cyber kill chain, lateral movement) |
| **LINDDUN / CARVER** | Privacy- / military-specific | Confidentiality or asset-criticality variants |

The canonical workflow: **decompose** the system (data-flow diagram: entities, processes, data stores, trust boundaries) → **map** threats onto boundaries (STRIDE per boundary crossing) → **rank** by likelihood × impact (DREAD, or qualitative high/med/low) → **assign mitigations** and verify.

## Why trust boundaries are the whole game

The single most durable insight: enumerate **trust boundaries** first. Every vulnerability ultimately reduces to data or control crossing a boundary without adequate validation. This is why the technique ports cleanly to the LLM/agent world, where the boundaries are new but the reasoning is old:

- **Prompt as untrusted input** crossing the model boundary → [[concepts/prompt-injection]] is threat modeling applied to the instruction/data distinction that LLMs blur.
- **Tool/MCP servers** as new processes crossing privilege boundaries → [[concepts/agent-security-patterns]], [[concepts/ai-agent-security]].
- **Memory as a persistence store** that an attacker can poison across sessions → [[concepts/ai-memory-systems]], [[concepts/memory-systems-design-patterns]].
- **Supply chain** as a trust boundary between you and everyone else's code → [[concepts/software-supply-chain-security]], [[concepts/security-and-governance/agent-skill-supply-chain-attacks]].

## Threat modeling for AI agents (2023–)

Agentic systems have forced a re-derivation of the discipline, because the classic assumption — "the program logic is trusted, the input is not" — breaks when the *logic itself* consumes natural-language instructions. Emerging practice:

- **Agent-oriented STRIDE extensions**: add threat categories for tool misuse, memory poisoning, and goal manipulation; treat the LLM as a *confused deputy*.
- **Kill chains for agents**: reconnaissance → prompt injection → privilege via tools → exfiltration (e.g. [[concepts/covert-exfiltration-via-web-fetch]], [[concepts/github-actions-secrets-exfiltration]] patterns).
- **Adversarial red-teaming as operationalized threat modeling** — model red teams (cf. [[concepts/ai-red-teaming-careers]]) enumerate threats at the *model* layer; agent red teams at the *orchestration* layer (cf. [[concepts/autonomous-security-agents]], [[concepts/ai-vulnerability-discovery]], [[concepts/x-agentred-multi-service-red-teaming]]).
- **Shift-left with LLMs themselves**: teams now use coding agents to generate first-pass STRIDE lists from architecture docs — a productivity pattern but also a verification problem (the agent's threat list is itself untrusted).

## Tooling

- **OWASP Threat Dragon** — free, diagram + STRIDE suggestion, the open-source reference implementation
- **Microsoft TMT (Threat Modeling Tool)** — the original STRIDE GUI
- **IriusRisk / Levica / Secureframe-style platforms** — commercial, integration with architecture repos
- **Threat model as code** — emerging pattern: keep threat models in the repo (markdown/YAML), diff them in PRs, so they stay alive instead of dying in a wiki

## Criticism & limits

- Costly without a facilitator; produces paperwork no one reads if not tied to sprint-level mitigations.
- Static models go stale against fast-moving threat landscapes — motivates "continuous threat modeling."
- Common failure: modeling the system as *intended* rather than as *deployed* (config, IAM, dependencies) — the gap where real breaches live.

## Related Concepts

- [[concepts/agent-security-patterns]] / [[concepts/ai-agent-security]] — threat modeling for LLM agents
- [[concepts/prompt-injection]] — the archetypal agent threat
- [[concepts/software-supply-chain-security]] — boundary-of-trust applied to dependencies
- [[concepts/security-and-governance/_index|Security & Governance]] — umbrella section
- [[concepts/browser-security]], [[concepts/capability-based-security]] — design philosophies that answer modeled threats
- [[concepts/ai-red-teaming-careers]] — active counterpart to passive modeling
- [[concepts/formal-methods]] / [[concepts/formal-verification-llm-agents]] — the formalist sibling

## Sources

- [OWASP Threat Modeling Project](https://owasp.org/www-community/Threat_Modeling)
- [OWASP Threat Dragon](https://www.owasp.org/www-project-threat-dragon/)
- Adam Shostack, *Threat Modeling: Designing for Security* (Wiley, 2014)
- Schneier, "Attack Trees" (1999)
