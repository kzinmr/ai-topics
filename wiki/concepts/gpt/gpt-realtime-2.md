---
title: "OpenAI GPT-Realtime-2"
created: 2026-05-20
updated: 2026-05-20
type: concept
tags:
  - openai
  - voice-ai
  - realtime
  - model
  - translation
  - developer-tooling
  - inference
  - streaming
sources: [raw/articles/2026-05-20_openai_gpt-realtime-2.md]
---

# OpenAI GPT-Realtime-2

A new generation of realtime voice models in OpenAI's API (released May 7, 2026). Three models that shift voice AI from simple call-and-response to interfaces that **listen, reason, translate, transcribe, and take action** during live conversations.

## Three Models

### GPT-Realtime-2 (Reasoning Voice)
GPT-5-class reasoning in voice. Key advances over GPT-Realtime-1.5:

| Feature | Detail |
|---------|--------|
| Context window | **128K** (up from 32K) |
| Reasoning levels | 5: minimal, low, medium, high, xhigh |
| Preambles | "let me check that" before main response |
| Parallel tool calls | Multiple tools simultaneously with voiced transparency |
| Big Bench Audio | +15.2% improvement (high reasoning) |
| Audio MultiChallenge | +13.8% improvement (xhigh reasoning) |

**Production impact (Zillow):** 95% call success rate vs 69% baseline on hardest adversarial benchmark (26-point lift). Stronger Fair Housing compliance.

**Pricing:** $32 / 1M audio input tokens ($0.40 cached), $64 / 1M audio output tokens.

### GPT-Realtime-Translate
Live multilingual voice translation. 70+ input languages → 13 output languages. Preserves meaning while keeping pace with natural speech, regional accents, domain-specific terms.

**BolnaAI benchmark:** 12.5% lower Word Error Rates than any other tested model. Lower fallback rates, higher task completion.

**Pricing:** $0.034 per minute.

### GPT-Realtime-Whisper
Streaming speech-to-text. Transcribes as people speak for live captions, real-time meeting notes, and continuous voice agent understanding.

**Pricing:** $0.017 per minute.

## Three Voice AI Patterns
OpenAI identifies three emerging patterns driving adoption:
1. **Voice-to-action** — User describes need → model reasons, uses tools, completes tasks (e.g., Zillow home search)
2. **Systems-to-voice** — Software produces live spoken guidance from context (e.g., travel app gate change alerts)
3. **Voice-to-voice** — Live cross-language conversation (e.g., Deutsche Telekom multilingual support)

## Safety
- Active classifiers monitor Realtime API sessions
- Harmful content conversations can be halted
- Custom guardrails via Agents SDK
- Usage policies prohibit misuse

## Relationships
- [[entities/openai]] — OpenAI, the creator
- [[concepts/voice-ai]] — Voice AI overview
- [[concepts/speech-to-text]] — Speech recognition
- [[concepts/translation]] — Machine translation
- [[concepts/gemini]] — Google's competing voice + agent capabilities
- [[concepts/ai-agents]] — AI agents (voice-to-action pattern)
