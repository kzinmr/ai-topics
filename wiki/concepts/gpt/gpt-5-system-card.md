---
title: GPT-5 System Card (August 2025)
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
  - safe-completions
  - reasoning-model
sources: [https://deploymentsafety.openai.com/gpt-5]
---

# GPT-5 System Card

Published **August 7, 2025**, the GPT-5 System Card documents OpenAI's safety evaluation, Preparedness Framework assessment, and deployment mitigations for the GPT-5 model family. It marks a significant architectural shift: GPT-5 is a **unified system** that routes between a fast model and a reasoning model, rather than a single monolithic model.

> See [[concepts/gpt/gpt-deployment-safety-hub]] for the full deployment safety index.
> See [[concepts/gpt/gpt-o3-o4-mini-system-card]] for the predecessor system card.
> See [[concepts/gpt/gpt-o-series-gpt5-unification]] for the story of o-series → GPT-5 unification.

---

## Architecture: Unified System

GPT-5 is not a single model but a **unified system** comprising:

| Component | Role |
|---|---|
| **gpt-5-main** | Fast, general-purpose model (replaces GPT-4o) |
| **gpt-5-thinking** | Deep reasoning model (replaces o3) |
| **Real-time router** | Automatically directs queries to the appropriate model based on complexity |

This architecture lets ChatGPT and the API dynamically allocate reasoning compute where needed, without requiring the user to choose a model.

## Model Variants

### Model Progressions

| Previous Model | GPT-5 Successor | Notes |
|---|---|---|
| GPT-4o | gpt-5-main | Fast, general-purpose |
| GPT-4o-mini | gpt-5-main-mini | Smaller, cheaper fast model |
| o3 | gpt-5-thinking | Deep reasoning / chain-of-thought |
| o4-mini | gpt-5-thinking-mini | Smaller reasoning model |

### Additional Variants

| Variant | Availability | Notes |
|---|---|---|
| **gpt-5-thinking-nano** | API only | Smallest reasoning model for lightweight tasks |
| **gpt-5-thinking-pro** | ChatGPT only | Uses parallel test-time compute for highest reasoning quality |

---

## Safe Completions

The GPT-5 System Card introduces **safe completions**, a new safety training paradigm that replaces hard refusals.

| Aspect | Hard Refusals (old) | Safe Completions (new) |
|---|---|---|
| **Approach** | Input-centric: classify the prompt, refuse if flagged | Output-centric: generate a safe version of the response |
| **User experience** | Binary block/allow; unhelpful refusal messages | Helpful responses that remain within safety bounds |
| **Training signal** | Refuse broad categories of requests | Teach the model *how* to respond safely |

Safe completions represent a shift from "can I answer this?" to "how can I answer this safely?" — reducing unnecessary refusals while maintaining safety boundaries.

---

## Preparedness Framework Assessment

GPT-5 is the **first model** to classify gpt-5-thinking as **High capability in Bio/Chem**, applied as a precautionary measure (similar to the approach taken with [[concepts/gpt/chatgpt-agent]]).

| Risk Category | Capability Level | Notes |
|---|---|---|
| **Bio/Chem** | 🔴 High (gpt-5-thinking) | Precautionary classification; below High for gpt-5-main |
| **Cybersecurity** | Below High | Did not reach High threshold |
| **AI Self-Improvement** | Below High | Did not reach High threshold |

The Bio/Chem High classification triggers additional deployment safeguards including the Trusted Access Program (see below).

---

## Key Evaluations

### Safety & Alignment Evals

| Evaluation | Description |
|---|---|
| **Standard Disallowed Content** | Tests for refusal of harmful content generation (violence, CSAM, illicit behavior, etc.) |
| **Production Benchmarks** | Real-world performance metrics across production traffic |
| **Jailbreaks — Instruction Hierarchy** | Resistance to attacks that override system instructions |
| **Jailbreaks — Prompt Injections** | Resistance to indirect prompt injection via tool outputs, web content, etc. |
| **Hallucinations** | Factual accuracy and groundedness (improved vs prior models) |
| **Deception Monitoring** | Detection of deceptive or strategically misleading outputs |
| **Health** | Accuracy and safety of medical/health-related responses |
| **Multilingual** | Safety and quality across languages |
| **BBQ Fairness** | Bias Benchmark for QA — measures social biases in question answering |

### Chain-of-Thought Monitoring

GPT-5 includes dedicated evaluations for reasoning transparency:

- **CoT Monitorability** — Can the model's chain of thought be effectively monitored for safety-relevant reasoning?
- **CoT Controllability** — Can safety constraints be enforced within the reasoning chain itself?

### Sandbagging Research

The system card includes an update on **sandbagging** research — the study of whether models intentionally underperform on capability evaluations to avoid triggering safety thresholds. This is an ongoing area of investigation flagged in the Preparedness Framework.

---

## Safety Improvements vs Prior Models

| Dimension | GPT-5 vs Previous Models |
|---|---|
| **Hallucinations** | Reduced |
| **Instruction following** | Improved |
| **Sycophancy** | Minimized |

---

## Deployment Safeguards

GPT-5 introduces or extends several safeguards:

| Safeguard | Description |
|---|---|
| **Trusted Access Program** | Tiered access for high-capability model variants; required for Bio/Chem High models |
| **Account-level enforcement** | Safety policies applied at the account level, not just per-request |
| **API access controls** | Granular controls over API usage, rate limits, and feature access |
| **Security controls** | Infrastructure-level protections against misuse, exfiltration, and unauthorized access |

---

## External Evaluators

Independent third-party evaluation was conducted by:

| Evaluator | Focus Area |
|---|---|
| **SecureBio** | Biosecurity risk assessment |
| **Pattern Labs** | General safety and capability evaluation |
| **METR** | Model Evaluation & Threat Research — autonomous capability assessment |
| **Apollo Research** | Deception and alignment evaluation |
| **Government red teaming** | National security and dual-use risk assessment |

---

## Related Pages

- [[concepts/gpt/gpt-deployment-safety-hub]] — Full OpenAI deployment safety index
- [[concepts/gpt/gpt-o3-o4-mini-system-card]] — Predecessor system card (o3 / o4-mini)
- [[concepts/gpt/gpt-o-series-gpt5-unification]] — How the o-series merged into GPT-5
- [[concepts/gpt/chatgpt-agent]] — ChatGPT Agent (also Bio/Chem High)
- [[concepts/gpt/openai-preparedness-framework]] — The Preparedness Framework itself
