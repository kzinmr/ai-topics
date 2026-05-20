---
title: "Advancing voice intelligence with new models in the API"
source: https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/
date: 2026-05-07
author: OpenAI
tags: [openai, voice-ai, realtime, model, translation]
---

# Advancing Voice Intelligence with New Realtime Models

OpenAI introduces three audio models in the Realtime API.

## GPT-Realtime-2
- GPT-5-class reasoning in voice
- 128K context window (up from 32K)
- Preambles, parallel tool calls, tool transparency
- 5 reasoning effort levels: minimal to xhigh
- 15.2% improvement on Big Bench Audio over previous gen
- Zillow: 95% call success rate (vs 69% baseline)

## GPT-Realtime-Translate
- 70+ input languages → 13 output languages
- Real-time translation preserving meaning, accents, domain terms
- BolnaAI: 12.5% lower Word Error Rates than competitors
- Deutsche Telekom, Vimeo testing

## GPT-Realtime-Whisper
- Streaming speech-to-text, transcribes as people speak
- For live captions, real-time notes, voice agents

## Pricing
- GPT-Realtime-2: $32/1M audio input, $64/1M audio output tokens
- Translate: $0.034/min
- Whisper: $0.017/min
