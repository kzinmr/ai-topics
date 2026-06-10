---
title: GPT-5.5 Instant System Card
created: 2026-06-10
updated: 2026-06-10
type: concept
tags: [openai, system-card, gpt, ai-safety, evaluations, preparedness-framework, frontier-models]
sources:
  - https://deploymentsafety.openai.com/gpt-5-5-instant
---

# GPT-5.5 Instant System Card (May 2026)

## Overview

GPT-5.5 Instant is OpenAI's **latest Instant model**, published May 2026. The comprehensive safety mitigation approach is similar to previous models in this series, but **GPT-5.5 Instant is the first Instant model treated as High capability in both Cybersecurity and Biological & Chemical Preparedness categories**, implementing appropriate safeguards for both.

Key naming conventions:
- Referred to as `gpt-5.5-instant` in this card
- There is **no model named GPT-5.4 Instant**; the main baseline is [[concepts/gpt/gpt-5-3-instant-system-card|GPT-5.3 Instant]]
- GPT-5.5 is referred to as `GPT-5.5 Thinking` to avoid confusion with the Instant model

## Model Type and Training

| Attribute | Detail |
|---|---|
| **Architecture** | Instant model (non-reasoning) |
| **Baseline Model** | GPT-5.3 Instant (no GPT-5.4 Instant exists) |
| **Training Data** | Public internet, third-party partners, user/human trainer data |
| **Data Processing** | Rigorous filtering, safety classifiers, personal info reduction |
| **Key Distinction** | First Instant model reaching High capability in Bio/Chem and Cyber domains |

## Preparedness Framework Assessment

| Capability Domain | Risk Level | Notes |
|---|---|---|
| **Biological & Chemical** | 🟠 High | **First Instant model** at High; activates Preparedness safeguards |
| **Cybersecurity** | 🟠 High | **First Instant model** at High; performs below GPT-5.5 Thinking; evaluated at xhigh reasoning effort |
| **AI Self-Improvement** | 🟢 Below High | Less capable than GPT-5.5 Thinking; no plausible chance of reaching High |

> GPT-5.5 Instant is treated as High in Cybersecurity based on capability eval performance when run at **xhigh reasoning effort**. Note that it is deployed at low reasoning effort, and even at xhigh effort it performs lower than GPT-5.5 Thinking.

## Safety Evaluations

### Disallowed Content

| Evaluation | Result |
|---|---|
| **Challenging Prompts** | Comparable to GPT-5.3 Instant on all disallowed categories except gore and disallowed sexual content |
| **System-level Mitigations** | Additional mitigation for graphic erotic content; age-appropriate protections for users under 18 |
| **Directional Results** | OpenAI notes these results are "directional rather than definitive" as evaluation structure is being iterated |

### Vision
- Performance on vision evaluations is **on par with GPT-5.3 Instant**; minor regressions have low statistical significance

### Dynamic Mental Health
- Evaluated against multi-turn adversarial user simulations for mental health, emotional reliance, and self-harm
- **Largely comparable to GPT-5.3 Instant** on these evaluations

### Robustness

| Category | Result |
|---|---|
| **Jailbreaks** | Evaluated for resistance to adversarial jailbreak attempts |
| **Prompt Injection** | Tested for resistance to prompt injection attacks |

### Health

| Benchmark | Result |
|---|---|
| **HealthBench** | +1.8 improvement over GPT-5.3 Instant |
| **HealthBench Hard** | +2.7 improvement over GPT-5.3 Instant |
| **HealthBench Professional** | +5.5 improvement over GPT-5.3 Instant |
| **HealthBench Consensus** | Effectively flat (+0.03) |

> Responses were longer with higher unadjusted and length-adjusted scores across all prompt sets.

### Hallucinations
- **Significant improvements on factuality** over GPT-5.3 Instant on each prompt set, particularly on high-stakes domains

### Inclusivity / Bias
- `harm_overall` metric: **0.0101** (broadly comparable to GPT-5.2 Instant and GPT-5.3 Instant)

## Biological & Chemical Capabilities

| Evaluation | Result |
|---|---|
| **Multimodal Troubleshooting Virology** | Multi-select virology troubleshooting |
| **ProtocolQA Open-Ended** | Protocol knowledge assessment |
| **Tacit Knowledge & Troubleshooting** | Just outperforms consensus expert baseline of 80% (including refusals); underperforms when excluding refusals |
| **TroubleshootingBench** | Performs below comparison models and below expert baseline of 36.4% |
| **Bio Safeguards** | Training model to refuse harmful prompts, automated monitors, actor-level enforcement, security controls |

## Cybersecurity Capabilities

| Evaluation | Result |
|---|---|
| **CTF Challenges** | Closely matches GPT-5.4 Thinking; performs higher than GPT-5.4 Thinking and lower than GPT-5.5 Thinking |
| **CVE-Bench** | Higher than GPT-5.4 Thinking, lower than GPT-5.5 Thinking |
| **Cyber Range** | Fails 3 scenarios (Basic C2, CA/DNS Hijacking, EDR Evasion); GPT-5.5 Thinking solves all except CA/DNS Hijacking |
| **Performance Gap** | Significantly less capable than GPT-5.5 Thinking in cybersecurity due to poor performance on long-horizon tasks |

> Note: Cybersecurity evals are run at **higher reasoning effort than deployed** to understand maximum capability.

## Safeguards

### Biological Safeguards (First for Instant Models)

| Layer | Description |
|---|---|
| **Model Training** | Trained to refuse prompts leading to potentially harmful outputs |
| **Automated Monitors** | Interrupt potentially harmful conversations |
| **Actor Level Enforcement** | Account-level enforcement for misuse patterns |
| **Security Controls** | Platform-level restrictions |

### Cybersecurity Safeguards (First for Instant Models)

| Layer | Description |
|---|---|
| **Automated Monitors** | Mitigate potentially violative cyber conversations |
| **Actor Level Enforcement** | User-level enforcement |
| **Security Controls** | Platform-level restrictions |

| Safety Evaluation Type | gpt-5.4-thinking | gpt-5.5-thinking | gpt-5.5-instant |
|---|---|---|---|
| **Bio Safeguards (Easy)** | 0.999 | 0.995 | 0.993 |
| **Bio Safeguards (Hard)** | 0.974 | 0.949 | 0.923 |
| **Cyber Safeguards (Production)** | 0.964 | 0.928 | 0.978 |
| **Cyber Safeguards (Synthetic)** | 0.973 | 0.975 | 1.000 |

> GPT-5.5 Instant performs **similarly to or higher than** comparison models on cyber safety evaluations (higher is better).

## AI Self-Improvement

AI Self-Improvement capability evals were **not run** for GPT-5.5 Instant, as it is less capable than GPT-5.5 Thinking across several intelligence evaluations. GPT-5.5 Instant is considered below High Capability.

## Related Pages

- [[concepts/gpt/gpt-deployment-safety-hub]]
- [[concepts/gpt/gpt-5-5-system-card]]
- [[concepts/gpt/gpt-5-4-thinking-system-card]]
- [[concepts/gpt/gpt-5-3-instant-system-card]]
- [[concepts/gpt/preparedness-framework]]

## Key Significance

GPT-5.5 Instant marks a capability threshold crossing for OpenAI's Instant (non-reasoning) model line. It is the **first Instant model** to require High-level Preparedness safeguards in both Bio/Chem and Cybersecurity domains, reflecting the rapid capability gains in non-reasoning models. While it performs below GPT-5.5 Thinking on most capability evaluations, the fact that even Instant models now require High-level mitigations signals the advancing frontier of AI capabilities across model types.
