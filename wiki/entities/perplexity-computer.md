---
title: Perplexity Computer
type: entity
created: 2026-08-26
updated: 2026-08-26
tags:
- entity
- product
- ai-agents
- autonomous-agents
- personal-ai
- vertical-agent
- agent-memory
aliases:
- perplexity-computer
- perplexity-digital-worker
sources:
- raw/articles/2026-03-25_openai-developers-blog_realtime-perplexity-computer.md
- https://open.substack.com/pub/swyx/p/ainews-silicon-valley-gets-serious
- https://www.perplexity.ai/hub/blog/self-improving-memory-for-agents
- entities/perplexity.md
- entities/perplexity-comet.md
---

# Perplexity Computer

**Perplexity Computer** is Perplexity's **general-purpose digital worker** — an autonomous task-execution agent that sits alongside [[entities/perplexity-comet]] (the AI-native browser) in Perplexity's product stack. While Comet handles search-first, intent-driven web interaction inside a browser, Computer is the "powerful, general-purpose digital worker" that performs tasks autonomously.

## Overview

| Field | Details |
|---|---|
| Developer | Perplexity AI |
| Category | General-purpose autonomous agent / digital worker |
| Interface | Voice-first (powered by OpenAI Realtime-1.5 in production) |
| Voice scale | Millions of voice sessions per month (as of March 2026) |
| Vertical | Professional Finance variant (May 2026) |
| Memory system | Brain (self-improving, agent-written, June 2026) |
| Positioning | Autonomous task execution layer of the Perplexity ecosystem |

## Ecosystem Position

Perplexity's product stack is organized around a search-centric core:

```
┌─────────────────┐
│ Perplexity Search│ ← Core AI search engine (brain)
├─────────────────┤
│  Comet Browser  │ ← AI-native browser (interface, search-first)
├─────────────────┤
│ Perplexity Computer│ ← Autonomous task execution (digital worker)
└─────────────────┘
```

Comet is the *interface layer* where users interact with AI inside the browser. Computer is the *execution layer* where tasks are handed off and performed autonomously. The two are complementary: Comet's search-first browsing naturally hands off tasks to Computer's autonomous execution.

## Voice Interface at Scale (Realtime-1.5)

Perplexity built its voice layer on top of OpenAI's Realtime-1.5 API, handling **millions of voice sessions per month** across Comet and Computer. The production engineering lessons (shared in the March 2026 OpenAI Developers blog post) are instructive for anyone building voice-driven agents:

### 1. Context management strategy
Large context updates fail in an all-or-nothing way — a 10k-token update into a 5k-token free window wipes out the entire preceding history. Perplexity's fix: break everything into ~2,000-token incremental chunks. When truncation happens, it trims a bit of history instead of wiping everything.

### 2. Message role semantics
`conversation.item.create` items have three roles: `system`, `user`, `assistant`. Getting these wrong subtly breaks the interaction:
- Too much context as `user` → the model behaves as if the user is narrating every paragraph of a web page out loud
- Too much as `system` → the model loses the distinction between what it "knows", what was supplied, and what the user is asking

The right mental model: the system is *aware of the page in the background* and answers naturally when asked — not the user speaking each paragraph.

### 3. Audio standardization across surfaces
Perplexity has multiple product surfaces (Ask, Comet, Computer) built on different client stacks (Swift, TypeScript, Rust, C++). Each produces different native audio buffers. The fix: a Rust SDK that abstracts platform differences and standardizes the audio contract:
- Resample to 48 kHz mono
- Match Opus codec preference / WebRTC internal rate
- Run through WebRTC APM (echo cancellation, AGC, noise reduction, high-pass filter)
- Encode for transport

### 4. VAD tuning for messy environments
Voice Activity Detection must be calibrated against real microphones, speaker volume, and background noise — not just clean lab conditions. Perplexity's internal test case: a noisy San Francisco bar. "What works in clean conditions often breaks in the real world."

### 5. Voice lock pattern
Instead of traditional push-to-talk (voice off by default, user presses to speak), Perplexity inverts the model:
- **Default**: ambient — the system listens passively
- **User action**: lock the voice to hold the floor

This addresses the common failure where the model treats a user's natural pause (thinking, reading) as the end of their turn and jumps in. Perplexity expects this pattern to become standard as voice interfaces move into more complex workflows.

### 6. Tool discipline
- Narrow the toolset to **under ten** core tools covering the highest-value actions
- Keep tool schemas and outputs *in distribution* for the model — format tool outputs as ordinary structured tool data, not assistant dialogue
- Use structured JSON with clearly separated fields (e.g., `response_text` for user-facing utterance, `require_repeat_verbatim` as a behavior flag) instead of mixing spoken content with inline instructions

## Professional Finance Vertical (May 2026)

Perplexity launched **Perplexity Computer for Professional Finance** — a dedicated AI workstation for financial professionals:

- **35 dedicated analyst workflows**: valuation, due diligence, market research, etc.
- **Licensed financial data**: integration with FactSet, S&P Global, and similar providers
- **Positioning**: An AI-powered Bloomberg Terminal competitor

This mirrors Anthropic's finance agent templates (pitch generation, valuation review, KYC with FactSet/S&P) — both companies are targeting the same high-value vertical simultaneously. See [[entities/perplexity]] for the broader enterprise verticalization trend.

## Brain: Self-Improving Memory System (June 2026)

Perplexity Computer introduced **Brain**, a self-improving memory system for AI agents. Brain allows agents to persist learnings across sessions, improving task execution over time without explicit retraining or prompt updates.

### Key characteristics
- **Self-improving**: Agents automatically refine their contextual knowledge based on task outcomes
- **Persistent memory**: Learnings survive across agent sessions and invocations
- **Agent-native**: Designed for Perplexity Computer's autonomous task execution, complementing Comet's search-first browsing interface

### Distinction from competitors
Brain is **self-improving** rather than statically configured — the agent writes its own memory based on experience. This contrasts with:
- **Google Gemini Enterprise Agent Platform**'s Memory Bank (statically configured memory)
- **Anthropic's** session-centric managed agent architecture

See [[entities/perplexity-comet]] for the full Brain section and cross-references to the competing agent-memory approaches.

## Related Entities

- [[entities/perplexity]] — Parent company; broader verticalization strategy
- [[entities/perplexity-comet]] — The AI-native browser (Comet) and Brain memory system
- [[concepts/openai/realtime-api]] — Realtime-1.5 voice API powering Computer's interface
- [[concepts/ai-agent-memory]] — Agent memory design patterns; Brain as a self-improving variant
- [[concepts/self-evolving-agents]] — Self-improving agents; Brain's self-writing memory as one approach
- [[entities/perplexity]] — Vertical expansion and Bumblebee context (company page)

## Sources

- [How Perplexity Brought Voice Search to Millions Using the Realtime API (OpenAI Developers Blog, 2026-03-25)](https://developers.openai.com/blog/realtime-perplexity-computer/)
- [Perplexity Computer official site](https://perplexity.ai/)
- [Perplexity: Self-improving memory for agents (Brain)](https://www.perplexity.ai/hub/blog/self-improving-memory-for-agents)
- [AINews: Silicon Valley gets Serious about Services (May 6, 2026)](https://open.substack.com/pub/swyx/p/ainews-silicon-valley-gets-serious)
- [[entities/perplexity]] — Vertical expansion and Bumblebee context
