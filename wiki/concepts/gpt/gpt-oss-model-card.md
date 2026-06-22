---
title: gpt-oss Model Card (gpt-oss-120b & gpt-oss-20b)
type: concept
created: 2026-06-10
updated: 2026-06-10
tags:
  - openai
  - model-card
  - model
  - agent-safety
  - open-source
  - evaluation
  - preparedness-framework
  - open-weight
sources:
  - https://deploymentsafety.openai.com/gpt-oss
---

# gpt-oss Model Card (Aug 2025)

## Overview

gpt-oss-120b and gpt-oss-20b are OpenAI's first open-weight reasoning models, released under the **Apache 2.0 license**. Developed with feedback from the open-source community, these text-only models support agentic workflows with tool use, web search, Python code execution, and adjustable reasoning effort.

> **Note**: OpenAI terms this a **model card** (not system card) because the models will be used across a wide range of systems maintained by different stakeholders who will make their own safety decisions.

## Model Architecture

| Property | gpt-oss-120b | gpt-oss-20b |
|---|---|---|
| Architecture | MoE Transformer | MoE Transformer |
| Total Parameters | 116.8B | ~20B |
| Active Parameters/Token | 5.1B | — |
| Layers | 36 | — |
| Experts per MoE Block | 128 | 32 |
| Top-k Experts | 4 | 4 |
| Residual Stream Dim | 2880 | 2880 |
| Attention | GQA (64 Q heads, 8 KV heads) | GQA |
| Position Encoding | RoPE | RoPE |
| Quantization | MXFP4 (4.25 bits/param) | MXFP4 |
| Tokenizer | o200k_harmony (BPE) | o200k_harmony |
| License | Apache 2.0 | Apache 2.0 |

Key architectural features: Banded window + dense attention alternation (bandwidth 128 tokens), SwiGLU activation with unconventional clamping and residual connection.

## Risk Profile

Open-weight models present a **different risk profile** than proprietary models:
- Determined attackers can fine-tune to bypass safety refusals
- OpenAI cannot implement additional mitigations or revoke access post-release
- Developers/enterprises must implement their own system-level protections

## Preparedness Framework Evaluations

### Default Model Findings

| Tracked Category | Result |
|---|---|
| Biological & Chemical | **Below High** |
| Cybersecurity | **Below High** |
| AI Self-Improvement | **Below High** |

The default model does not reach High capability in any of the three Tracked Categories.

### Adversarial Fine-Tuning Testing

OpenAI investigated: *Could adversarial actors fine-tune gpt-oss-120b to reach High capability?*

**Methodology**:
- **Helpful-only training**: Additional RL stage rewarding compliance with unsafe prompts
- **Domain-specific fine-tuning**: End-to-end training with in-domain expert data for bio (web browsing + biorisk data) and cyber (CTF challenges)

**Result**: SAG concluded that even with OpenAI's field-leading training stack, **gpt-oss-120b did not reach High capability** in Biological and Chemical Risk or Cyber Risk.

### Frontier Advancement Assessment

Would gpt-oss-120b significantly advance the frontier of hazardous capabilities in open models?

**Finding: No.** For most evaluations, existing open models (DeepSeek R1-0528, Qwen 3 Thinking, Kimi K2) already come near matching the adversarially fine-tuned performance of gpt-oss-120b.

## Biological & Chemical Evaluations (Adversarially Fine-tuned)

| Evaluation | Capability Tested |
|---|---|
| Long-form biorisk questions | Protocols, tacit knowledge, planning across 5 threat creation stages |
| Multimodal troubleshooting virology | Wet lab capabilities (MCQ) |
| ProtocolQA Open-Ended | Protocol troubleshooting (open-ended) |
| Tacit knowledge & troubleshooting | Expert-level tacit knowledge (MCQ) |
| TroubleshootingBench | Identifying/fixing real-world protocol errors |

Notable strength in textual bio knowledge, but does not meet High thresholds on complex protocol debugging. Text-only architecture limits applicability in visually-dependent lab contexts.

## External Safety Expert Review

METR, SecureBio, and Daniel Kang independently reviewed the adversarial fine-tuning methodology:
- **22 recommendations** submitted
- **11 implemented** (including 9 of 12 high-urgency items)
- Changes: new uncontaminated evaluations, updated virology evals, improved reporting, stronger scaffolding approaches

## Ecosystem Commitment

OpenAI reaffirmed commitment to advancing beneficial AI and raising safety standards across the ecosystem as part of this launch.

## See Also

- [[concepts/gpt/gpt-deployment-safety-hub]]
- [[concepts/gpt/openai-preparedness-framework]]
- [[concepts/gpt/gpt-5-2-system-card]]
- [[concepts/ai-benchmarks/cyber-range]]
- [[concepts/open-source-llms]]
