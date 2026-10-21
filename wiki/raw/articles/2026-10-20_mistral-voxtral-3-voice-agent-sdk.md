---
title: "Introducing Voxtral 3 — voice agent SDK + SOTA speech models"
url: https://mistral.ai/news/voxtral-3/
source: mistral.ai
date: 2026-10-20
fetched_at: 2026-10-21
type: raw-article
tags: [speech, voice-ai, audio-generation, ai-agents, tool-use, mistral]
confidence: high
---

# Introducing Voxtral 3 (Mistral, Oct 20 2026)

Source: https://mistral.ai/news/voxtral-3/

## Summary
Voxtral 3 is Mistral's voice agent SDK for real-time speech in 50+ languages — accurate transcription, emotional TTS, and deep tool use. EU-hosted or self-deployed.

## Key content
Voxtral 3 introduces a cutting-edge voice agent SDK and state-of-the-art speech models designed for real-time, multi-step conversations across 50+ languages. It combines accurate transcription, natural speech synthesis with emotional adaptability, and deep tool integration for seamless workflow automation. Available via Mistral's EU-hosted API or self-deployment, it ensures data sovereignty while delivering low-latency, human-like interactions for contact centers, virtual assistants, and hands-free copilots.

A reliable voice agent needs to do four things very well (and simultaneously):
1. Listen accurately across languages, accents, speakers, and interruptions,
2. Reason deeply about what users mean in specific contexts,
3. Speak naturally with emotion and expression, and
4. Take action over multiple steps through connected systems.

Voxtral 3 is a new family of state-of-the-art speech-to-text and text-to-speech models, alongside a voice agent SDK that brings listening, thinking, tool calling, and speaking into a single real-time streaming pipeline.

### Highlights
- **Accurate transcription across 50+ languages.** The speech-to-text model, **Voxtral Small Transcribe 3**, is state-of-the-art in multilingual transcription, identifying who said what (diarization), using keyphrases to improve accuracy (context-biasing). It detects when someone has finished speaking so agents can respond without delay (end-of-turn detection).
- **Natural speech that adapts to the conversation.** The text-to-speech model, **Voxtral Mini TTS 3**, introduces new voices that adjust their emotion, pace, and emphasis based on conversational context, with support for 35+ languages and 50+ dialects.
- **Human-like intelligence at your (spoken) command.** The new voice agent SDK combines listening, reasoning, tool calling, and speaking into a real-time experience. Agents can retrieve information, interact with business systems, and complete tasks during live conversations over phone or web.
- **Pro Voice for distinctly accurate voice adaptation.** For professional use cases where basic voice cloning does not suffice, Voxtral's Pro Voice adaptation reproduces a speaker's distinctive character, emotional range, and speaking style across languages, using just 30 minutes of audio.
- **Your voice AI, on your infrastructure.** Use Mistral's EU-hosted API or deploy Voxtral 3 on your own infrastructure. Keep sensitive conversations within your environment and control whether any audio is retained.

### Example flow (multilingual, tool-using voice agent)
A caller (Béatrice) speaks French; the agent transcribes a referral letter ("Merci de recevoir ce patient pour un avis dermatologique…"), reasons about intent, calls `get_referral(ref="4420 1187")`, then `book_appointment(slot="Nov 3 17:45")`, and replies in English — demonstrating cross-language listening, reasoning, multi-step tool use, and speaking in one real-time pipeline.

### Sovereignty positioning
As with other Mistral models, the Voxtral 3 family is designed for sovereign deployment — EU-hosted API or self-hosting, controlling where audio is processed, how data is handled, and whether conversations are retained.

## Notes
- Sibling releases in Mistral's Oct 2026 wave: Timestral (time-series foundation models, Oct 15), CERN strategic partnership (Oct 19).
- Builds on prior Voxtral line (Voxtral TTS, Voxtral Realtime, Voxtral Small Transcribe 2).
