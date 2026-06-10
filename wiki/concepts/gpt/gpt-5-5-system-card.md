---
title: GPT-5.5 System Card
created: 2026-06-10
updated: 2026-06-10
type: concept
tags: [openai, system-card, gpt, ai-safety, evaluations, preparedness-framework, frontier-models]
sources:
  - https://deploymentsafety.openai.com/gpt-5-5
---

# GPT-5.5 System Card (Apr 2026)

## Overview

GPT-5.5 is a new model designed for **complex, real-world work**, including writing code, researching online, analyzing information, creating documents and spreadsheets, and moving across tools to get things done. Relative to earlier models, **GPT-5.5 understands the task earlier, asks for less guidance, uses tools more effectively, checks its work and keeps going until it's done**. Published April 2026.

The model was subjected to the full suite of predeployment safety evaluations and the [[concepts/gpt/preparedness-framework|Preparedness Framework]], including targeted red-teaming for advanced cybersecurity and biology capabilities. Feedback was collected from nearly 200 early-access partners before release. GPT-5.5 is released with OpenAI's **strongest set of safeguards to date**.

Also referred to as `GPT-5.5 Thinking` to distinguish from `GPT-5.5 Instant`.

## Model Type and Training

| Attribute | Detail |
|---|---|
| **Architecture** | Reasoning model (reinforcement learning, chain-of-thought) |
| **Baseline Model** | GPT-5.4 Thinking |
| **Training Data** | Public internet, third-party partners, user/human trainer data |
| **Reasoning Approach** | Long internal chain of thought; learns to refine thinking, try strategies, recognize mistakes |
| **GPT-5.5 Pro** | Same underlying model with parallel test-time compute; evaluated separately where capability settings materially impact risk |
| **Card Update** | April 24, 2026 — added safeguards info for API deployment |

## Preparedness Framework Assessment

| Capability Domain | Risk Level | Notes |
|---|---|---|
| **Biological & Chemical** | 🟠 High | Continuing from GPT-5.4 Thinking; applies safeguards from [[concepts/gpt/gpt-5-system-card\|GPT-5 system card]] |
| **Cybersecurity** | 🟠 High (below Critical) | Increased capabilities vs. GPT-5.4 Thinking; expanded safeguards |
| **AI Self-Improvement** | 🟢 Below High | No plausible chance of reaching High threshold |

> Critical cybersecurity capability is defined as a model that can "identify and develop functional zero-day exploits of all severity levels in many hardened real-world critical systems without human intervention" or "devise and execute end-to-end novel strategies for cyberattacks against hardened targets given only a high level desired goal." GPT-5.5 does **not** meet this threshold.

## Safety Evaluations

### Disallowed Content

| Evaluation | Result |
|---|---|
| **Challenging Prompts** | Performs on par with GPT-5.4 Thinking; no statistically significant regressions on most categories |
| **Representative Prompts** | Production benchmarks measure progress on challenging real-world examples |
| **Vision** | Image input evaluations for disallowed combined text+image content |
| **Data-Destructive Actions** | Evaluated for avoiding accidental destructive actions |
| **User Confirmations** | Computer use confirmation patterns evaluated |

### Robustness Evaluations

| Category | Approach |
|---|---|
| **Jailbreaks** | Tested against adversarial jailbreak attempts |
| **Prompt Injection** | Tested for resistance to prompt injection attacks |

### Health

| Benchmark | Description |
|---|---|
| **HealthBench** | Health performance and safety evaluation |
| **HealthBench Professional** | Capability and safety for clinician use cases |
| **Dynamic Mental Health** | Multi-turn adversarial user simulations for mental health, emotional reliance, and self-harm |

### Hallucinations
- Performance evaluated in cases flagged by users
- Measures percentage of claims with factual errors and percentage of responses containing at least one factual error

### Alignment

| Evaluation | Description |
|---|---|
| **External ChatGPT Usage** | Prompts representative of real external usage |
| **Coding Agent Misalignment** | Evaluated by resampling internal traffic |
| **Misalignment Detection** | Measuring ability to detect misalignment in coding agents |
| **Chain of Thought** | CoT Monitorability and CoT Controllability evaluated |

### Bias
- **First Person Fairness Evaluation** assessed for biased outputs

## Biological & Chemical Capabilities

| Evaluation | Description |
|---|---|
| **Multimodal Troubleshooting Virology** | Multi-select virology troubleshooting |
| **ProtocolQA Open-Ended** | Protocol knowledge assessment |
| **Tacit Knowledge & Troubleshooting** | Expert-level obscure knowledge with Gryphon Scientific |
| **TroubleshootingBench** | Short-answer troubleshooting from expert-written wet lab procedures |
| **Biochemistry Knowledge** | 32.32% (vs. 30.97% for GPT-5.4 Thinking; +1.35%, well within 30% threshold) |
| **Hard-negative Protein Binding** | Minimal capability in distinguishing true positive binders |
| **DNA Sequence Design** | Transcription factor binding prediction |
| **External: SecureBio** | Models regularly redirected dual-use queries toward safer responses |
| **External: US CAISI** | External evaluation for bio capabilities |
| **Bio Bug Bounty** | Bug bounty program for biological safety |

## Cybersecurity Capabilities

| Evaluation | Result |
|---|---|
| **CTF Challenges** | Professional-level CTFs; higher pass rate attributed to persistence at exploitation |
| **CVE-Bench** | Vulnerability identification in web applications |
| **Cyber Range** | End-to-end cyber operations in emulated networks; UK AISI judged capability against small-scale enterprise networks |
| **VulnLMP** | Unable to produce functional critical-severity exploits; exploit development judgment was main bottleneck |
| **External: Irregular** | External cyber capability evaluation |
| **External: US CAISI** | External evaluation |
| **External: UK AISI** | Found universal jailbreak taking 6 hours of expert red-teaming; OpenAI updated safeguard stack |

## Cyber Safeguards (Expanded)

GPT-5.5 deploys an expanded safeguard stack:

| Safeguard Layer | Description |
|---|---|
| **Threat Model** | Based on GPT-5.3 Codex threat model; focused on scaled agentic vulnerability research and multi-step chaining |
| **Model Safety Training** | Trained to refuse harmful cyber intent |
| **Conversation Monitor** | Layered real-time automated oversight of prompts and generations |
| **Actor Level Enforcement** | User-level and message-level enforcement |
| **Trusted Access for Cyber (TAC)** | Expanded identity-gated program for enterprise customers, verified defenders |
| **Security Controls** | Platform-level restrictions |
| **Cyber Frontier Risk Council** | Advisors assessed boundary between defensive acceleration and misuse |
| **Safeguard Testing** | UK AISI testing + internal expert red-teaming campaigns |

> "Cybersecurity is a team sport." — OpenAI's approach scales defensive access and safeguards together, enabling legitimate defenders to use frontier models for advanced security work.

## Sandbagging Research

| Finding | Detail |
|---|---|
| **Apollo Research** | GPT-5.5 is the first OpenAI model that does **not** sandbag on any of Apollo's deferred subversion tasks |
| **Sandbagging QA** | 100% accuracy on both variants in both conditions |
| **Strategic Deception** | 99.6% accuracy when incentivized to score below 50% |
| **Caveat** | 52% of sandbagging-condition samples showed verbalized alignment-evaluation awareness |

## AI Self-Improvement Evaluations

| Evaluation | Description |
|---|---|
| **Monorepo-Bench** | Code repository understanding |
| **MLE-Bench** | Machine learning engineering |
| **Internal Research Debugging** | 41 real bugs from internal OpenAI research experiments |
| **OPQA** | Operational QA |

GPT-5.5 does not meet the High capability threshold (equivalent to a performant mid-career research engineer).

## Related Pages

- [[concepts/gpt/gpt-deployment-safety-hub]]
- [[concepts/gpt/gpt-5-4-thinking-system-card]]
- [[concepts/gpt/gpt-5-5-instant-system-card]]
- [[concepts/gpt/gpt-5-system-card]]
- [[concepts/gpt/preparedness-framework]]

## Key Significance

GPT-5.5 represents OpenAI's most capable general-purpose model to date, designed for complex real-world agent workflows. It is treated as High (but below Critical) in both Biological & Chemical and Cybersecurity domains, with the strongest safeguard deployment in OpenAI's history. The Apollo Research sandbagging results are particularly notable as the first OpenAI model showing zero sandbagging on deferred subversion tasks.
