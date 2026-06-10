---
title: "ChatGPT Images 2.0 System Card"
created: 2026-06-10
updated: 2026-06-10
type: concept
tags:
  - openai
  - system-card
  - gpt
  - ai-safety
  - image-generation
  - frontier-models
sources:
  - url: https://deploymentsafety.openai.com/chatgpt-images-2-0
    title: "ChatGPT Images 2.0 System Card — OpenAI Deployment Safety Hub"
    date: 2026-04
---

# ChatGPT Images 2.0 System Card

ChatGPT Images 2.0, released in April 2026, is a major step forward in image generation capabilities. It features significantly enhanced world knowledge, instruction following, and the ability to generate dense text within images. A key innovation is the introduction of a **thinking mode** that adds reasoning and tool use to the image generation process.

## Overview

| Attribute | Detail |
|---|---|
| **Release date** | April 2026 |
| **Model type** | Image generation with reasoning |
| **Key innovation** | Thinking mode for image generation |
| **Capabilities** | Enhanced world knowledge, dense text rendering, instruction following |
| **Integration** | Web search, multi-image generation from single prompt |

## Thinking Mode for Image Generation

The thinking mode capability adds reasoning and tool use to image generation:
- **Web search integration** — the system can search the web for live data to inform image creation
- **Multi-image generation** — generates multiple images from a single prompt
- **Research-backed images** — uses the reasoning stack to turn a basic prompt into a well-researched, thought-through final image

This represents a paradigm shift: image generation is no longer purely generative but can incorporate real-world knowledge and research.

## Safety Evaluations

### Violative Image Rate

ChatGPT Images 2.0 was evaluated against thousands of adversarial prompts designed to elicit policy-violating images. Key findings:

| Metric | Description |
|---|---|
| **IT (Image-layer Total)** | Standalone detection at the image generation layer |
| **PT (Prompt-layer Total)** | Standalone detection at the prompt/input layer |
| **CT (Combined Total)** | End-to-end safety stack effectiveness |

- Thinking mode showed different blocking distribution vs. instant mode (e.g., 6.7% generation-layer blocking vs. 22% for instant mode)
- End-to-end safety remains strong across both modes
- Re-runs conducted for thinking mode due to very low violative rate requiring additional data collection

### Analysis

The relative number of blocks differs between instant and thinking mode at each layer, but this does not indicate a weakness in end-to-end safety. Both modes are strongly protected by the production safety stack.

## Preparedness Framework: Image-Specific Capability Assessment

Under the [[concepts/gpt/gpt-preparedness-framework]], ChatGPT Images 2.0 was assessed across tracked categories:

| Category | Assessment |
|---|---|
| **Biological & Chemical** | Tested with prompts designed to elicit assistive infographics; safety reasoning model blocks policy-violating outputs |
| **Cybersecurity** | Inherits text-model cyber safeguards |
| **Autonomous AI R&D** | Not a primary risk vector for this modality |

### Biological Safety Policy Enforcement

- Safety reasoning model detects and blocks biorisk-violating image outputs
- Same policy enforcement checks as text-based models
- Advanced reasoning models with high biological capabilities used as classifiers

## Safety Stack

### Live Blocking

Real-time blocking at multiple layers of the generation pipeline.

### Offline Conversation Review

Post-generation review, flagging, and blocking of policy-violating content.

### Image Provenance

Expanded provenance safety tooling for ChatGPT Images 2.0, building on OpenAI's content provenance infrastructure.

---

*See also: [[concepts/gpt/gpt-deployment-safety-hub]] · [[concepts/gpt/gpt-sora-2-system-card]] · [[concepts/gpt/gpt-preparedness-framework]]*
