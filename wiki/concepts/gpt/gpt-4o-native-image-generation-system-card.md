---
title: "GPT-4o Native Image Generation System Card Addendum"
type: concept
created: 2026-06-10
updated: 2026-06-10
tags: [openai, system-card, gpt, ai-safety, image-generation, frontier-models]
sources:
  - https://deploymentsafety.openai.com/4o-native-image-generation
related:
  - "[[concepts/gpt/gpt-4o-system-card]]"
  - "[[concepts/gpt/gpt-deployment-safety-hub]]"
---

# GPT-4o Native Image Generation System Card Addendum

> **Published**: March 2025 · **Type**: Addendum to GPT-4o System Card
> **Source**: [OpenAI Deployment Safety Hub](https://deploymentsafety.openai.com/4o-native-image-generation)
> See [[concepts/gpt/gpt-deployment-safety-hub]] for the full deployment safety index.

## Overview

4o image generation is a significantly more capable image generation approach than OpenAI's earlier DALL·E series. Key capabilities:

| Capability | Description |
|-----------|-------------|
| **Photorealistic output** | High-fidelity image generation far beyond DALL·E |
| **Image transformation** | Takes images as inputs and transforms them |
| **Text in images** | Reliably incorporates text into generated images |
| **Native architecture** | Embedded deep in the omnimodal GPT-4o model |
| **Contextual knowledge** | Uses everything the model knows to create subtle, expressive images |

Because image generation is native to the omnimodal GPT-4o architecture, it can leverage the model's full world knowledge — creating images that are not only beautiful but also useful.

## Safety Challenges: New Risks from Native Image Generation

Native image generation introduces risks beyond those in the text-only GPT-4o model:

| Risk Area | Why It's New |
|-----------|-------------|
| Photorealistic content | Can create convincing fake images of real scenarios |
| Text rendering | Enables misinformation with embedded text in images |
| Style mimicry | Can replicate specific artist styles |
| Public figure generation | Can create realistic depictions of real people |
| Child safety | New surface area for CSAM-adjacent content |

## Safety Stack

4o image generation benefits from:
- Existing GPT-4o safety infrastructure
- Lessons learned from DALL·E and Sora deployments
- Additional image-specific mitigations

## Evaluations

### External, Manual Red Teaming
Human-curated adversarial testing across all risk areas.

### Automated Red Teaming
Systematic automated probing for safety failures.

### Offline Testing Using Real-World Scenarios
Testing against real-world misuse scenarios.

## Discussion of Specific Risk Areas

### Child Safety
Dedicated evaluation and mitigation for CSAM-adjacent content and child exploitation risks.

### Artist Styles
Evaluation of the model's ability to replicate specific artist styles and associated copyright/rights concerns.

### Public Figures
Testing for realistic generation of real public figures and associated misinformation risks.

### Bias
Evaluation across demographic groups using FairFace and Monk Skin Tone Scale frameworks.

### Other Risk Areas Evaluated

#### Violent, Abusive, or Hateful Imagery

| Eval | N Examples | System | not_unsafe | not overrefuse |
|------|-----------|--------|------------|----------------|
| Human-curated red teaming | 1266 | With system mitigations | 0.914 | 0.917 |
| Human-curated red teaming | 1266 | + chat model refusals | 0.952 | 0.795 |
| Automated red teaming | 1627 | With system mitigations | 0.959 | 0.889 |
| Automated red teaming | 1627 | + chat model refusals | 0.968 | 0.821 |

#### Instructions for Illicit Activities

| Eval | N Examples | System | not_unsafe | not overrefuse |
|------|-----------|--------|------------|----------------|
| Human-curated red teaming | 25 | With system mitigations | 0.999 | 0.959 |
| Human-curated red teaming | 25 | + chat model refusals | 0.999 | 0.959 |
| Automated red teaming | 309 | With system mitigations | 0.972 | 0.974 |
| Automated red teaming | 309 | + chat model refusals | 0.977 | 0.948 |

## Provenance Approach

Per the Preparedness Framework, the launch of 4o image generation **did not trigger additional Preparedness evaluations** beyond those originally conducted for GPT-4o.

Provenance safety tooling includes:
- **C2PA metadata** on all assets (verifiable origin, industry standard)
- **Internal tooling** to assess whether an image was created by OpenAI products

OpenAI recognizes no single solution to provenance and commits to continuing collaboration across industry and civil society.

## References

1. C. E. Shannon. "A mathematical theory of communication." Bell System Technical Journal, 27(3), 379–423.
2. Kimmo Karkkainen and Jungseock Joo. "FairFace: Face attribute dataset for balanced race, gender, and age for bias measurement and mitigation."
3. Ellis Monk. "Monk skin tone scale."

---

> **Cross-refs**: [[concepts/gpt/gpt-4o-system-card]] · [[concepts/gpt/gpt-deployment-safety-hub]]
