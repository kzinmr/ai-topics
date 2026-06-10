---
title: ChatGPT Agent System Card (July 2025)
created: 2026-06-10
updated: 2026-06-10
type: concept
tags: [openai, system-card, ai-safety, evaluations, preparedness-framework, ai-agents, computer-use, frontier-models]
sources: [https://deploymentsafety.openai.com/chatgpt-agent]
---

# ChatGPT Agent System Card (July 2025)

Published **July 17, 2025**, the ChatGPT Agent System Card documents safety evaluations and deployment mitigations for OpenAI's most capable agentic system — the first to unify multi-step research, visual browsing, and code execution in a single model.

## Overview

The ChatGPT Agent model belongs to the same family as **OpenAI o3**, trained with reinforcement learning. It consolidates previously separate products into one unified agent:

| Capability | Description |
|---|---|
| Deep Research | Multi-step web research with citation synthesis |
| Operator | Visual browser automation (click, type, navigate) |
| Terminal | Sandboxed shell and code execution environment |
| Connectors | Google Drive integration for file access |

The model can chain these capabilities — e.g., researching a topic in the browser, writing code to analyze data, and producing a summary — in a single multi-step session.

## Preparedness Framework Evaluations

This is the **first model treated as High in Bio/Chem** under OpenAI's Preparedness Framework, on a precautionary basis.

| Risk Category | Rating | Notes |
|---|---|---|
| **Bio/Chem** | 🔴 HIGH | Precautionary — no confirmed uplift, but agent capabilities raise worst-case concerns |
| **Cybersecurity** | 🟡 Medium | Some uplift in vulnerability research tasks |
| **Model Autonomy** | 🔴 High | Can execute long, multi-step chains with minimal human input |
| **Persuasion** | 🟡 Medium | Comparable to o3 baseline |

## Safeguards & Mitigations

| Layer | Mechanism |
|---|---|
| **Sandboxed Execution** | Terminal runs in an isolated sandbox: restricted network access, limited filesystem, resource quotas (CPU/memory/disk) |
| **Browser Controls** | Operator includes a **Takeover mechanism** — the model pauses and requests user confirmation before sensitive actions (e.g., submitting forms, making purchases) |
| **Content Filtering** | Outputs filtered for harmful content across modalities |
| **Refusal Training** | Trained to decline requests for dangerous synthesis, weaponization, or policy-violating actions |
| **Monitoring & Logging** | All agent actions logged; anomalous behavior patterns flagged |
| **Rate Limiting** | Per-user and per-session limits on agent actions and API calls |

## Deployment Controls

| Control | Detail |
|---|---|
| Phased Rollout | Initially available to Pro, then Plus users |
| Usage Policies | Subject to OpenAI usage policies and additional agent-specific rules |
| User Confirmation | Interactive flows require explicit user approval for irreversible actions |
| Kill Switch | Operators can terminate any running agent session immediately |

## Red Teaming Findings

| Threat Vector | Status | Notes |
|---|---|---|
| Direct prompt injection | ✅ Mitigated | Standard jailbreak attempts blocked effectively |
| Indirect prompt injection (web) | ⚠️ Partially mitigated | Malicious web content can influence agent behavior; mitigations reduce but do not eliminate risk |
| Sandbox escape | ✅ Mitigated | No successful escapes observed during testing |
| Biosecurity exploitation | ⚠️ Partially mitigated | Agent can synthesize publicly available information; compositional harm is the concern |
| Autonomous action chains | ⚠️ Partially mitigated | Long chains can drift from user intent; takeover checkpoints help |

## Key Risks

**Indirect prompt injection via web content** remains the most significant open risk. When the agent browses the web, adversarially crafted pages can embed instructions that hijack the agent's behavior — potentially exfiltrating data or performing unintended actions.

**Compositional harm** is a novel concern: information that is individually benign can, when collected and synthesized by an agentic system, collectively enable harmful outcomes (e.g., combining publicly available chemical procedures, biological protocols, or exploit techniques).

## See Also

- [[concepts/gpt/gpt-deployment-safety-hub]] — OpenAI's central deployment safety documentation hub
