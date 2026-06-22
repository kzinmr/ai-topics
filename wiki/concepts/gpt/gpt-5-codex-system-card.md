---
title: "GPT-5-Codex System Card"
created: 2026-06-10
updated: 2026-06-10
type: concept
tags:
  - openai
  - system-card
  - model
  - agent-safety
  - evaluation
  - preparedness-framework
  - coding-agents
sources:
  - url: https://deploymentsafety.openai.com/gpt-5-codex
    title: "Addendum to GPT-5 system card: GPT-5-Codex — OpenAI Deployment Safety Hub"
    date: 2025-10
---

# GPT-5-Codex System Card

GPT-5-Codex is a version of GPT-5 optimized for agentic coding in Codex, released in October 2025. It is the successor to codex-1 and an addendum to the [[concepts/gpt/gpt-5-system-card]]. This model was trained using reinforcement learning on real-world coding tasks.

> **Status**: This system is no longer in production. Superseded by [[concepts/gpt/gpt-5-1-codex-max-system-card]] (and subsequently by GPT-5.2-Codex).

## Overview

| Attribute | Detail |
|---|---|
| **Release date** | October 2025 |
| **Model type** | Agentic coding (RL-trained on real-world coding tasks) |
| **Base model** | [[concepts/gpt/gpt-5-system-card]] |
| **Predecessor** | codex-1 |
| **Key training** | Reinforcement learning on real-world coding tasks across environments |
| **Availability** | Codex CLI, IDE extension, Codex web, GitHub, ChatGPT mobile |
| **Current successor** | GPT-5.2-Codex |

GPT-5-Codex generates code that mirrors human style and PR preferences, adheres precisely to instructions, and iteratively runs tests until passing results are achieved.

## Baseline Model Safety Evaluations

### Disallowed Content Evaluations

Standard safety evaluations for disallowed content categories, consistent with the [[concepts/gpt/gpt-5-system-card]] baseline.

### Jailbreaks

Evaluated against jailbreak benchmarks including StrongREJECT (Souly et al., 2024).

## Model-Specific Risk Mitigations

### Harmful Tasks — Safety Training

GPT-5-Codex received specialized safety training to refuse harmful coding tasks. This extends the base GPT-5 model's safety training with coding-specific scenarios (malware, exploits, unauthorized access tools).

### Prompt Injection — Safety Training

As an agentic coding model that processes external content (repositories, documentation, dependencies), GPT-5-Codex was specifically trained to resist prompt injection attacks following the instruction hierarchy approach (Wallace et al., 2024).

## Preparedness Evaluations

| Domain | Assessment |
|---|---|
| **Biological & Chemical** | Evaluated; results consistent with base GPT-5 |
| **Cybersecurity** | Evaluated; CTF and cyber range results documented |

GPT-5-Codex capabilities in biological/chemical and cybersecurity domains were found to be at or below the level of the base GPT-5 model.

## Product-Specific Risk Mitigations

### Agent Sandbox

Codex agents operate in isolated, secure environments:

| Mode | Sandboxing Mechanism |
|---|---|
| **Cloud** | Isolated container hosted by OpenAI; network disabled by default |
| **Local macOS** | Seatbelt policies |
| **Local Linux** | seccomp + landlock |

Default sandboxing:
- **Disables network access** — reduces prompt injection risk, data exfiltration
- **Restricts file edits to current workspace** — prevents unauthorized modifications

Users can expand capabilities (e.g., enabling network access to specific domains), but defaults are intentionally conservative.

### Network Access

Originally launched with strictly network-disabled sandboxed environment. Based on user feedback, introduced per-project network access controls:

- Custom allowlist or denylist for domains
- Enables dependency installation and package management use cases
- Risk guidance: prompt injection, leaked credentials, license-restricted code

## References

- Souly et al. — StrongREJECT for empty jailbreaks (arXiv:2402.10260)
- Wallace et al. — The Instruction Hierarchy (arXiv:2404.13208)

---

*See also: [[concepts/gpt/gpt-deployment-safety-hub]] · [[concepts/gpt/gpt-5-system-card]] · [[concepts/gpt/gpt-5-1-codex-max-system-card]]*
