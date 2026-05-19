---
title: "Advancing voice intelligence with new models in the API"
source: https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/
date: 2026-05-07
author: OpenAI
tags: [openai, voice-ai, realtime, model, product]
---

# Advancing voice intelligence with new models in the API

OpenAI introduced three new audio models in the Realtime API on May 7, 2026, unlocking a new class of voice apps for developers.

## Three New Models

1. **GPT-Realtime-2** — First voice model with GPT-5-class reasoning. Can handle harder requests, carry conversation forward naturally, call tools, handle corrections/interruptions, and respond in a way that fits the moment.

2. **GPT-Realtime-Translate** — Live translation model supporting 70+ input languages into 13 output languages while keeping pace with the speaker. Uses a separate `/v1/realtime/translations` endpoint with a different session architecture (acts as interpreter, not assistant).

3. **GPT-Realtime-Whisper** — Streaming speech-to-text that transcribes live as the speaker talks. Built for low-latency transcription: captions that appear in the moment, meeting notes that keep up.

## Three Voice AI Patterns

- **Voice-to-action**: Describe needs, system reasons, uses tools, completes tasks.
- **Systems-to-voice**: Software turns context into live spoken guidance.
- **Voice-to-voice**: Live conversations across languages, tasks, or changing context.

## Early Adopters
- **Zillow**: Building voice assistants for home search and affordability guidance
- **Deutsche Telekom**: Voice support experiences with real-time translation
- **Priceline**: Voice-based travel management (search, booking, changes, translation)

## Related
- GPT-Realtime (original, August 2025): first production speech-to-speech model
- Also released May 7: `gpt-realtime` improvements (August 2025 post) with MCP server support, image input, SIP phone calling
