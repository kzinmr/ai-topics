---
title: GPT-Realtime Voice Models
created: 2026-05-17
updated: 2026-05-17
type: concept
tags: [voice-ai, openai, model, inference, realtime, translation]
sources: [raw/articles/2026-05-07_openai_gpt-realtime-voice-models.md]
---

# GPT-Realtime Voice Models

OpenAI's second-generation Realtime API voice models, released May 7, 2026. Three specialized models that move realtime audio from simple call-and-response to voice interfaces that can listen, reason, translate, transcribe, and take action as a conversation unfolds.

## Models

### GPT-Realtime-2
First voice model with **GPT-5-class reasoning**. Carries conversation forward naturally while reasoning through requests, calling tools, handling corrections/interruptions, and responding appropriately to context. Built on the Realtime API conversation lifecycle (`/v1/realtime`).

### GPT-Realtime-Translate
Live translation model supporting **70+ input languages → 13 output languages**. Uses a dedicated translation session architecture (`/v1/realtime/translations`) — acts as interpreter, not assistant. Streams translated audio + transcript deltas while speaker is still talking.

### GPT-Realtime-Whisper
Streaming speech-to-text model for **low-latency transcription**. Transcribes audio as people speak — captions in the moment, meeting notes that keep up. Uses a transcription session that emits transcript deltas.

## Three Voice AI Patterns

| Pattern | Description | Example |
|---|---|---|
| **Voice-to-action** | Describe needs → system reasons → uses tools → completes task | Zillow: "Find homes within my BuyAbility, avoid busy streets, schedule a tour" |
| **Systems-to-voice** | Software turns context into live spoken guidance | Travel app: "Your flight is delayed, I found the new gate, mapped the route" |
| **Voice-to-voice** | Live conversations across languages, tasks, context | Deutsche Telekom: customer speaks preferred language, model translates in real time |

## Architecture Difference: Conversation vs Translation vs Transcription

| Session Type | Endpoint | Model Role |
|---|---|---|
| Voice-agent | `/v1/realtime` | Assistant (responds, calls tools) |
| Translation | `/v1/realtime/translations` | Interpreter (continuous stream) |
| Transcription | Transcription session | Transcriber (text deltas only) |

## Related Models
- [[concepts/gpt-realtime]] — Original GPT-Realtime (August 2025), now called `gpt-realtime` (first-gen, production voice model)
- [[entities/openai]] — OpenAI company page
- [[concepts/voice-ai]] — Broader voice AI landscape
