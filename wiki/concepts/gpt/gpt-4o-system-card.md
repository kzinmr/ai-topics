---
title: GPT-4o System Card (May 2024)
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
  - multimodal
sources: [https://openai.com/index/gpt-4o-system-card/]
---

# GPT-4o System Card (May 2024)

The **GPT-4o System Card** ([page](https://openai.com/index/gpt-4o-system-card/)) documents OpenAI's first omni-modal model — an autoregressive model accepting and generating text, audio, image, and video. Published May 2024, it represents the multimodal foundation that all subsequent GPT-5 series models build upon.

## Model Overview

| Spec | Detail |
|---|---|
| **Architecture** | Autoregressive omni-modal (text/audio/image/video I/O) |
| **Audio response time** | 232ms (average human conversation pace) |
| **Cost** | 50% cheaper than GPT-4 Turbo |
| **Training** | Pre-trained on internet-scale multimodal data, fine-tuned with SFT + RLHF + Process Reward Models |

## Key Benchmarks

| Benchmark | GPT-4o | GPT-4 Turbo |
|---|---|---|
| MMLU | 88.7% | 86.4% |
| MATH | 76.6% | — |
| HumanEval | 90.2% | — |
| GPQA | 53.6% | — |
| MMMU | 69.1% | — |

## Safety Evaluations

| Metric | GPT-4o | GPT-4 Turbo |
|---|---|---|
| Disallowed content decline rate | 83–87% | — |
| Hallucination rate | 39.2% | 43.4% |
| Toxicity rate | 0.14% | 0.20% |

## Preparedness Framework Assessment

This was an early application of the Preparedness Framework (pre-v2). Categories assessed:

| Category | Level |
|---|---|
| Cybersecurity | Low |
| Chemical & Biological | Medium |
| Persuasion | Medium |
| Model Autonomy | Low |
| **Overall** | **Medium** |

## External Assessments

- **METR**: Found no autonomous replication risk
- **Apollo Research**: Limited strategic deception ability detected

## Mitigations

| Layer | Details |
|---|---|
| System-level | Content filtering, usage policies |
| Model-level | RLHF alignment, refusal training |
| Audio-specific | Watermarking, speaker identification |
| Multimodal-specific | Image/video content filtering |

## Significance

GPT-4o established the multimodal safety evaluation framework that all subsequent cards would use. Key contributions:
- First model to evaluate audio-specific risks (voice cloning, real-time conversation manipulation)
- First to assess multimodal attack vectors (image-based prompt injection)
- Set the baseline Preparedness assessment (Overall Medium) that GPT-5 series would escalate from

## See Also

- [[concepts/gpt/gpt-4o-native-image-generation-system-card]] — GPT-4o image generation addendum (Mar 2025)
- [[concepts/gpt/gpt-5-system-card]] — Successor unified system (Aug 2025)
- [[concepts/gpt/gpt-system-card-milestones]] — Timeline of all milestones
- [[concepts/gpt/gpt-deployment-safety-hub]] — Full index
