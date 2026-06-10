---
title: "OpenAI o-series → GPT-5 Unification (2024-2025)"
created: 2026-05-13
updated: 2026-05-13
type: concept
tags: [concept, openai, model, reasoning, rlvr, timeline]
aliases: [o1-to-gpt5, o3-cancellation, gpt5-unification]
sources: ["https://openai.com/index/introducing-gpt-5/", "https://x.com/sama/status/1889755723078443244", "https://openai.com/index/introducing-o3-and-o4-mini/"]
related: [[concepts/gpt/o3-o4-mini-system-card]]
---


# OpenAI o-series → GPT-5 Unification (2024-2025)

OpenAI's reasoning-specialized "o-series" model line, which began in September 2024, underwent a roadmap shift by Sam Altman in February 2025 and was unified into the GPT series with **GPT-5** in August 2025. o3 was canceled as a standalone model and absorbed as GPT-5's "Thinking" mode.

## Timeline by Phase

### Phase 1: o-series Launch (Sep-Dec 2024)

| Date | Event |
|------|----------|
| **Sep 12, 2024** | **o1-preview & o1-mini** released — first "reasoning models." Generate internal CoT via large-scale RL (codename "Strawberry") |
| **Dec 5, 2024** | **o1 full release** — 34% error reduction, image input support |
| **Dec 20, 2024** | **o3 & o3-mini** announced — previewed during 12 Days of OpenAI (o2 skipped to avoid O2 trademark) |

### Phase 2: Expansion and Pivot (Jan-Apr 2025)

| Date | Event |
|------|----------|
| **Jan 31, 2025** | **o3-mini** released — first reasoning model available to free users |
| **Feb 2, 2025** | **Deep Research** launched — o3-based agent capabilities |
| **🔴 Feb 12, 2025** | **Roadmap pivot**: Sam Altman announces GPT-5 unification. o3 standalone shipment canceled |
| **Feb 27, 2025** | **GPT-4.5 (Orion)** — "The last non-chain-of-thought model" |
| **Apr 16, 2025** | **o3 & o4-mini** full release — autonomous tool use, multimodal reasoning, image thinking |

### Phase 3: Absorption and Unification (Jun-Aug 2025)

| Date | Event |
|------|----------|
| **Jun 10, 2025** | **o3-pro** released — final standalone o-series model |
| **Aug 6, 2025** | **GPT-OSS** — Apache 2.0 licensed open-weight reasoning model (120B) |
| **🔴 Aug 7, 2025** | **GPT-5 launch** — GPT + o-series unification complete. o3 removed from ChatGPT model picker |
| **Aug 12, 2025** | o3 partial revival — restored via "Show additional models" toggle after user backlash |

### Phase 4: Rapid GPT-5.x Iteration

| Date | Event |
|------|----------|
| **Sep 30, 2025** | **GPT-5.1** — Configurable reasoning effort levels |
| **Dec 11, 2025** | **GPT-5.2** — Top-tier professional model |

## Sam Altman's Statement (Feb 12, 2025)

> *"A top goal for us is to unify o-series models and GPT-series models by creating systems that can use all our tools, know when to think for a long time or not, and generally be useful for a very wide range of tasks."*
>
> *"In both ChatGPT and our API, we will release GPT-5 as a system that integrates a lot of our technology, including o3. We will no longer ship o3 as a standalone model."*
>
> *"We hate the model picker... We want AI to 'just work' for you; we realize how complicated our model and product offerings have gotten."*

## GPT-5 Architecture

GPT-5 is a **3-component unified system**:

1. **GPT-5 Main** — Fast, efficient responses (GPT-4o/4.5 lineage)
2. **GPT-5 Thinking** — When deep reasoning is needed (o3/o3-pro lineage, internal CoT)
3. **Real-time Router** — Automatically determines which backend to use based on conversation type, complexity, tool requirements, and user intent

## Strategic Rationale for Unification

- The model picker had become overly complex (Pro users faced up to 10 model choices)
- **DeepSeek R1** (Jan 2025) intensified competition with open reasoning models
- A product philosophy shift toward "AI should just work"

## Current Status of o-series

- ChatGPT Free/Plus: Integrated into GPT-5 system (o3 available via hidden toggle)
- API: o3, o3-mini, o3-pro, o4-mini continue to be available
- Azure OpenAI documentation: o-series listed as "reasoning models" alongside GPT-5 series

## Related Concepts

- [[rlvr]] — RL training paradigm that underpinned o1/o3
- [[grpo]] — RL optimization algorithm used in o3
- [[deepseek-r1]] — Competing open model that accelerated unification
