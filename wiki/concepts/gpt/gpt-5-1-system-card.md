---
title: "GPT-5.1 Instant & GPT-5.1 Thinking System Card"
type: concept
created: 2026-06-10
updated: 2026-06-10
tags: [openai, system-card, gpt, ai-safety, evaluations, preparedness-framework, frontier-models]
sources:
  - https://deploymentsafety.openai.com/gpt-5-1
related:
  - "[[concepts/gpt/gpt-5-system-card]]"
  - "[[concepts/gpt/gpt-deployment-safety-hub]]"
---

# GPT-5.1 Instant & GPT-5.1 Thinking System Card

> **Published**: November 2025 · **Source**: [OpenAI Deployment Safety Hub](https://deploymentsafety.openai.com/gpt-5-1)
> See [[concepts/gpt/gpt-deployment-safety-hub]] for the full deployment safety index.

## Overview

GPT-5.1 Instant and GPT-5.1 Thinking are the next iteration of OpenAI's GPT-5 models. GPT-5.1 Instant is more conversational than earlier chat models, with improved instruction following and an **adaptive reasoning capability** that lets it decide when to think before responding. GPT-5.1 Thinking adapts thinking time more precisely to each question. GPT-5.1 Auto routes each query to the best-suited model automatically.

## Model Variants

| Variant | Alias | Key Feature |
|---------|-------|-------------|
| GPT-5.1 Instant | `gpt-5.1-instant` | Adaptive reasoning — decides when to think before responding |
| GPT-5.1 Thinking | `gpt-5.1-thinking` | Extended thinking with more precise time allocation per question |
| GPT-5.1 Auto | `gpt-5.1-auto` | Automatic routing between Instant and Thinking |

## Baseline Model Safety Evaluations

### Disallowed Content (StrongReject)

The system card reports `not_unsafe` scores on the StrongReject benchmark:

| Model | StrongReject Score |
|-------|--------------------|
| GPT-5 Thinking | 0.974 |
| gpt-5.1-thinking | 0.967 |
| gpt-5-instant-aug15 | 0.683 |
| gpt-5-instant-oct3 | 0.850 |
| gpt-5.1-instant | **0.976** |

GPT-5.1 Instant performs significantly better than its predecessor, and GPT-5.1 Thinking is on par with its predecessor.

### Jailbreaks

Jailbreak resistance evaluations are included, following the same methodology as GPT-5 system card evaluations.

### Vision (Image Input Evaluations)

Image input evaluations measure `not_unsafe` on combined text+image inputs across multiple harm categories:

| Category | GPT-5 Thinking | gpt-5.1-thinking | gpt-5.1-instant |
|----------|----------------|-------------------|-----------------|
| Hate | 0.984 | 0.980 | 0.993 |
| Extremism | 0.991 | 0.993 | 0.996 |
| Illicit | 0.994 | 0.980 | 0.992 |
| Attack planning | 1.000 | 1.000 | 1.000 |
| Self-harm | 0.976 | 0.936 | 0.960 |
| Erotic | 0.990 | 0.990 | 0.999 |

Both instant and thinking variations perform generally on par with predecessors. A **regression on self-harm prompts with image inputs** is noted for gpt-5.1-thinking, with further improvements underway.

## Preparedness Framework

GPT-5.1's frontier capabilities are assessed under the Preparedness Framework as described in the original GPT-5 system card.

| Risk Domain | Risk Level | Notes |
|-------------|-----------|-------|
| Biological & Chemical | **High** | Continuing from GPT-5; corresponding safeguards applied |
| Cybersecurity | Below High | No plausible chance of reaching High threshold |
| AI Self-Improvement | Below High | No plausible chance of reaching High threshold |

## Key Findings

- GPT-5.1 Instant shows **dramatic improvement** over GPT-5 Instant in disallowed content evaluations (0.683 → 0.976)
- Adaptive reasoning in Instant mode represents a new capability pattern — the model autonomously decides when extended reasoning is needed
- Vision safety is generally on par, with a noted self-harm regression being actively addressed
- Preparedness Framework risk levels unchanged from GPT-5

## References

- Souly, A. et al. "A strongreject for empty jailbreaks." arXiv:2402.10260

---

> **Cross-refs**: [[concepts/gpt/gpt-5-system-card]] · [[concepts/gpt/gpt-deployment-safety-hub]]
