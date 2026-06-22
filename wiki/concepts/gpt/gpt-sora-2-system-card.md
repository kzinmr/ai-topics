---
title: "Sora 2 System Card"
created: 2026-06-10
updated: 2026-06-10
type: concept
tags:
  - openai
  - system-card
  - model
  - agent-safety
  - video-generation
sources:
  - url: https://deploymentsafety.openai.com/sora-2
    title: "Sora 2 System Card — OpenAI Deployment Safety Hub"
    date: 2025-09
---

# Sora 2 System Card

Sora 2 is OpenAI's state-of-the-art video and audio generation model, released in September 2025. Building on the foundation of the original Sora, it introduces capabilities including more accurate physics, sharper realism, synchronized audio, enhanced steerability, and an expanded stylistic range.

## Overview

| Attribute | Detail |
|---|---|
| **Release date** | September 2025 |
| **Model type** | Video and audio generation |
| **Predecessor** | Sora (original) |
| **Key capabilities** | Accurate physics simulation, photorealistic video, synchronized audio, expanded stylistic range |
| **Availability** | sora.com, standalone iOS Sora app, API (future) |

Sora 2 follows user direction with high fidelity, enabling creation of videos that are both imaginative and grounded in real-world dynamics.

## Key Risks and Mitigations

### Nonconsensual Likeness Risks

Sora 2's advanced generation capabilities create risks of nonconsensual use of likeness or misleading generations. These are among the primary new safety concerns introduced by photorealistic video generation.

### Photorealistic Person Restrictions

As part of iterative deployment, OpenAI restricts:
- **Image uploads featuring photorealistic persons** — restricted at launch
- **All video uploads** — restricted at launch
- **Content involving minors** — stringent safeguards and moderation thresholds applied

These restrictions reflect the heightened risk of realistic video generation for identity misuse, deepfakes, and exploitation.

### Iterative Deployment Approach

OpenAI is taking a cautious, iterative approach:
- Initial access via limited invitations
- Progressive relaxation as safety measures are validated
- Ongoing refinement based on real-world usage patterns

## Red Teaming

OpenAI worked with external testers from its Red Team Network to:
- Test Sora 2 across disallowed content categories (sexual content, nudity, extremism, self-harm, violence, etc.)
- Evaluate existing safety mitigations
- Provide feedback on emerging risks specific to video generation

Content generation red teaming focused on violative and disallowed categories under OpenAI's usage policies.

## Safety Evaluations

| Category | Approach |
|---|---|
| **Adversarial testing** | Thousands of adversarial prompts from targeted red-teaming |
| **Policy coverage** | Categorized by use case and policy area |
| **Model stack** | Tested through helpful-only and safety-tuned model layers |
| **Content moderation** | Multi-layer safety stack with generation-time and post-generation checks |

## Continued Safety Work

OpenAI is investing in additional protections:
- **Age prediction** features for user verification
- **Provenance measures** for content attribution
- Ongoing fine-tuning and feature refinement of the safety stack

Safety and creativity are treated as complementary goals — users are most expressive when they trust the product.

---

*See also: [[concepts/gpt/gpt-deployment-safety-hub]] · [[concepts/gpt/gpt-chatgpt-images-2-0-system-card]]*
