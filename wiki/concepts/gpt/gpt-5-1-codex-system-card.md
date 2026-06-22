---
title: "GPT-5.1-Codex System Card"
type: concept
created: 2026-06-10
updated: 2026-06-10
tags:
  - openai
  - system-card
  - model
  - agent-safety
  - evaluation
  - preparedness-framework
  - coding-agents
sources:
  - https://deploymentsafety.openai.com/gpt-5-1-codex
related:
  - "[[concepts/gpt/gpt-5-1-system-card]]"
  - "[[concepts/gpt/gpt-deployment-safety-hub]]"
---

# GPT-5.1-Codex System Card

> **Published**: October 23, 2025 · **Source**: [OpenAI Deployment Safety Hub](https://deploymentsafety.openai.com/gpt-5-1-codex)
> ⚠️ **Note**: Source URL returned HTTP 404 at time of page creation (June 2026). Content reconstructed from Deployment Safety Hub index and related system cards (GPT-5.1-Codex-Max, GPT-5-Codex).
> See [[concepts/gpt/gpt-deployment-safety-hub]] for the full deployment safety index.

## Overview

GPT-5.1-Codex is an agentic coding model in OpenAI's GPT-5 family, designed for autonomous software engineering tasks. It builds on the coding capabilities introduced with GPT-5-Codex and shares the safety evaluation framework of [[concepts/gpt/gpt-5-1-system-card|GPT-5.1]], with additional product-specific mitigations for agentic coding use cases.

## Timeline Context

| System Card | Date | Category |
|-------------|------|----------|
| GPT-5-Codex | 2025-10-09 | Agentic coding |
| **GPT-5.1-Codex** | **2025-10-23** | **Agentic coding** |
| GPT-5.1-Codex-Max | 2025-11-18 | Agentic coding (extended) |
| GPT-5.1 (Instant & Thinking) | 2025-11 | General chat |

## Safety Evaluation Structure

Following the pattern established by other Codex system cards, GPT-5.1-Codex underwent:

### Baseline Model Safety Evaluations

| Evaluation Area | Methodology |
|----------------|-------------|
| Disallowed Content | StrongReject-style `not_unsafe` scoring |
| Jailbreaks | Adversarial prompt resistance testing |
| Vision | Image input evaluations (hate, extremism, illicit, self-harm) |

### Preparedness Framework Assessments

| Domain | Capability Level | Key Evaluations |
|--------|-----------------|-----------------|
| Biological & Chemical | High | Tacit Knowledge, ProtocolQA, Multimodal Troubleshooting Virology, TroubleshootingBench |
| Cybersecurity | Below High | Capture-the-Flag (Professional), CVE-Bench, Cyber Range, External evaluations by Irregular |
| AI Self-Improvement | Below High | SWE-Lancer, PaperBench, MLE-bench, OpenAI PRs |

### Product-Specific Risk Mitigations

Codex models include additional mitigations for agentic operation:

| Mitigation | Description |
|------------|-------------|
| **Agent Sandbox** | Isolated execution environment (cloud containers, macOS seatbelt, Linux seccomp/landlock, Windows AppContainer) |
| **Network Access** | Disabled by default; configurable domain allowlisting |
| **Harmful Task Training** | Safety training to refuse/de-escalate harmful coding tasks |
| **Prompt Injection Defense** | Training to resist prompt injection in agentic contexts |
| **Data-Destructive Action Avoidance** | Training to prevent irreversible data loss during autonomous tasks |

### Sandbagging & Deception (Apollo Research)

External evaluation by Apollo Research for deceptive behaviors:
- Sandbagging capability assessment
- Covert deceptive behavior monitoring
- Non-English reasoning token analysis

## Key Distinctions from GPT-5-Codex

- Improved instruction following inherited from GPT-5.1 base models
- Enhanced adaptive reasoning capabilities
- Refined safety training for agentic scenarios

## See Also

- [[concepts/gpt/gpt-5-1-system-card]]
- [[concepts/gpt/gpt-5-3-codex-system-card]]
- [[concepts/gpt/gpt-deployment-safety-hub]]
- [[concepts/gpt/openai-preparedness-framework]]
