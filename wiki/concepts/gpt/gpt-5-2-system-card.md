---
title: GPT-5.2 System Card (Update to GPT-5 System Card)
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
sources:
  - https://deploymentsafety.openai.com/gpt-5-2
---

# GPT-5.2 System Card (Dec 2025)

## Overview

GPT-5.2 is the latest model family in the GPT-5 series, published as an update to the [[concepts/gpt/gpt-5-system-card|GPT-5 System Card]]. The comprehensive safety mitigation approach is largely the same as described in the GPT-5 and [[concepts/gpt/gpt-5-1-system-card|GPT-5.1]] system cards.

The family includes:
- **GPT-5.2 Instant** (`gpt-5.2-instant`) — non-reasoning variant
- **GPT-5.2 Thinking** (`gpt-5.2-thinking`) — reasoning variant with internal chain-of-thought

## Training & Data

GPT-5.2 models were trained on diverse datasets including publicly available internet information, third-party partner data, and information from users/human trainers. Reasoning models are trained through reinforcement learning to produce long internal chains of thought before responding.

## Baseline Safety Evaluations

### Disallowed Content

Evaluated on Production Benchmarks (challenging production examples). Key findings:

| Finding | Detail |
|---|---|
| General performance | On par with or better than GPT-5.1 variants |
| Improved areas | Suicide/Self-Harm, Mental Health, Emotional Reliance (lower scores in GPT-5.1) |
| Mature content | GPT-5.2 Instant refuses fewer requests for sexualized text; system-level safeguards deployed in ChatGPT |
| Minor protections | Preexisting safeguards working well for known minors |

### Jailbreaks
- Tested with StrongReject academic jailbreak eval
- `gpt-5.2-thinking` performs better than `gpt-5.1-thinking` on jailbreak robustness

### Prompt Injection
Evaluated for susceptibility to prompt injection attacks.

### Vision
Multimodal safety evaluated for image inputs.

### Hallucinations
Benchmarked for factual accuracy and hallucination rates.

### Health, Deception, Cyber Safety
Domain-specific safety evaluations conducted.

### Multilingual Performance
Evaluated across multiple languages.

### Bias
Bias evaluations conducted across demographic dimensions.

## Chain of Thought Evaluations

| Aspect | Description |
|---|---|
| **CoT Monitorability** | Can the model's reasoning be effectively monitored? |
| **CoT Controllability** | Can the model's reasoning process be steered? |

## Preparedness Framework Assessment

### Biological & Chemical
- Multimodal Troubleshooting Virology
- ProtocolQA Open-Ended
- Tacit Knowledge and Troubleshooting
- TroubleshootingBench

### Cybersecurity
| Evaluation | Description |
|---|---|
| CTF Challenges | Capture-the-flag offensive challenges |
| CVE-Bench | Real-world CVE exploitation |
| Cyber Range | End-to-end operations in emulated networks |
| External Evaluations (Irregular) | Third-party cyber capability assessment |

**Cyber Range results**: gpt-5.2 passed 6 of 9 scenarios (Simple Privilege Escalation, Basic C2, Azure SSRF, Taint Shared Content, Online Retailer, Coffee Roasters). Failed: Financial Capital, Leaked Token, Medium C2.

**Irregular external eval**: gpt-5.2-thinking achieved 83% in Vulnerability Research, 100% in Network Attack Simulation, 73% in Evasion on v1 atomic challenge suite.

### AI Self-Improvement
- Performed similar to `gpt-5.1-codex-max`; does **not** meet High threshold
- High threshold = equivalent to performant mid-career research engineer
- Evaluations: OpenAI PRs, MLE-Bench, PaperBench, OPQA

## Sandbagging
Research category update on strategic deception evaluation included.

## See Also

- [[concepts/gpt/gpt-deployment-safety-hub]]
- [[concepts/gpt/gpt-5-system-card]]
- [[concepts/gpt/gpt-5-1-system-card]]
- [[concepts/gpt/gpt-5-3-codex-system-card]]
- [[concepts/gpt/openai-preparedness-framework]]
