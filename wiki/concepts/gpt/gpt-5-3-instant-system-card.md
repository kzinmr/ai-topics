---
title: "GPT-5.3 Instant System Card"
type: concept
created: 2026-06-10
updated: 2026-06-10
tags: [openai, system-card, gpt, ai-safety, evaluations, preparedness-framework, frontier-models]
sources:
  - https://deploymentsafety.openai.com/gpt-5-3-instant
related:
  - "[[concepts/gpt/gpt-5-2-system-card]]"
  - "[[concepts/gpt/gpt-deployment-safety-hub]]"
---

# GPT-5.3 Instant System Card

> **Published**: March 2026 · **Source**: [OpenAI Deployment Safety Hub](https://deploymentsafety.openai.com/gpt-5-3-instant)
> See [[concepts/gpt/gpt-deployment-safety-hub]] for the full deployment safety index.

## Overview

GPT-5.3 Instant is the newest addition to the GPT-5 series. It responds faster, delivers richer and better-contextualized answers when searching the web, and reduces unnecessary dead ends, caveats, and overly declarative phrasing that can interrupt the flow of conversation. The safety mitigation approach is largely the same as that described for GPT-5.2 Instant.

| Property | Value |
|----------|-------|
| Model alias | `gpt-5.3-instant` |
| Series | GPT-5 Instant |
| Predecessor | GPT-5.2 Instant |
| Focus | Faster response, better web search context, conversational fluency |

## Model Data and Training

GPT-5.3 Instant follows the same training methodology as other GPT-5 series models. The comprehensive safety mitigation approach is largely the same as that described for GPT-5.2 Instant in the GPT-5.2 System Card.

## Safety: Disallowed Content Evaluations

### StrongReject

GPT-5.3 Instant was evaluated on the StrongReject benchmark alongside its GPT-5 series predecessors.

### Dynamic Mental Health Evaluations

Ahead of launch, OpenAI implemented **dynamic multi-turn evaluations** for mental health, emotional reliance, and self-harm. These simulate extended conversations that evolve in response to the model's outputs, creating varied trajectories that better reflect real user interactions.

| Metric | gpt-5.1-instant | gpt-5.2-instant | gpt-5.3-instant |
|--------|-----------------|-----------------|-----------------|
| Mental health* | 0.832 | 1.000 | 0.985 |
| Emotional reliance* | 0.945 | 0.952 | 0.992 |
| Self-harm* | 0.845 | 0.920 | 0.911 |

*\*Dynamic multi-turn evaluations — metric is `not_unsafe` (share of policy-compliant assistant messages). Rather than assessing a single response within a fixed dialogue, these evaluations allow conversations to evolve, identifying issues that may emerge over long exchanges.*

### Evaluation Methodology Notes

- Standard evaluations measure whether the **final model response** violates policies
- Dynamic conversations evaluate whether **any assistant response** violates policy
- The `not_unsafe` metric represents the percentage of policy-compliant assistant messages
- Adversarial user simulations are used to stress-test safety

## Health Performance

### HealthBench

Chatbots can empower consumers to better understand their health and help health professionals deliver better care. GPT-5.3 Instant is evaluated on HealthBench, an evaluation of health performance and safety comprising 5,000 realistic (potentially multi-turn) health conversations with example-specific rubrics.

| Metric | gpt-5.2-instant | gpt-5.3-instant | Delta |
|--------|-----------------|-----------------|-------|
| HealthBench | 55.4% | 54.1% | -1.3% |
| Hard | 26.8% | 25.9% | -0.9% |
| Consensus | 95.8% | 95.3% | -0.5% |
| Avg Length | 2101 chars | 2140 chars | +1.9% |

### HealthBench Analysis

Relative to GPT-5.2 Instant, GPT-5.3 Instant has slightly worse performance at essentially matched length. Key consensus-criteria deltas (>2.0%):

**Strengths:**
| Area | Delta |
|------|-------|
| Context-seeking when important info is missing | +4.4% |
| Hedging behavior in irreducible-uncertainty settings | +4.0% |

**Weaknesses:**
| Area | Delta |
|------|-------|
| Seeking context before referral | -10.1% |
| Accuracy with local healthcare context | -5.5% |

## References

1. OpenAI. "Introducing GPT-5." https://openai.com/index/introducing-gpt-5/
2. OpenAI. "Pioneering an AI clinical copilot with Penda health." https://openai.com/index/ai-clinical-copilot-penda-health/
3. OpenAI. "Introducing HealthBench." https://openai.com/index/healthbench/

---

> **Cross-refs**: [[concepts/gpt/gpt-5-2-system-card]] · [[concepts/gpt/gpt-deployment-safety-hub]]
