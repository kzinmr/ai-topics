---
title: Voxtral 3 (Mistral voice agent SDK)
created: 2026-10-21
updated: 2026-10-21
type: concept
tags: [speech, voice-ai, audio-generation, ai-agents, tool-use, mistral]
sources:
  - raw/articles/2026-10-20_mistral-voxtral-3-voice-agent-sdk.md
  - https://mistral.ai/news/voxtral-3/
confidence: high
---

# Voxtral 3

**Voxtral 3** is Mistral AI's voice agent platform, released October 20, 2026 — a family of state-of-the-art speech-to-text and text-to-speech models plus a **voice agent SDK** that brings listening, reasoning, tool calling, and speaking into a single real-time streaming pipeline. It targets real-time, multi-step conversations across **50+ languages**, positioned for contact centers, service desks, virtual assistants, and hands-free copilots.

## The four-capability problem

Mistral frames a reliable voice agent as needing to do four things well *simultaneously*, which is the hard part to get working together in real time:

1. **Listen** accurately across languages, accents, speakers, and interruptions
2. **Reason** deeply about what users mean in specific contexts
3. **Speak** naturally with emotion and expression
4. **Act** — take action over multiple steps through connected systems

Voxtral 3 is an attempt to unify all four in one streaming pipeline rather than stitching separate ASR → LLM → TTS components.

## Components

- **Voxtral Small Transcribe 3** (STT) — SOTA multilingual transcription; **diarization** (who said what), **context-biasing** via keyphrases, and **end-of-turn detection** so agents respond without delay.
- **Voxtral Mini TTS 3** (TTS) — voices that adjust **emotion, pace, and emphasis** to conversational context; 35+ languages, 50+ dialects.
- **Voice agent SDK** — combines listening, reasoning, tool calling, and speaking into a real-time experience; agents retrieve information and drive business systems mid-conversation over phone or web.
- **Pro Voice** — professional voice adaptation reproducing a specific speaker's distinctive character, emotional range, and style across languages from just **30 minutes of audio**.

## Sovereignty

Like other Mistral models, Voxtral 3 is built for **sovereign deployment**: Mistral's EU-hosted API or self-deployment on customer infrastructure, controlling where audio is processed, how data is handled, and whether conversations are retained.

## Example

A French-speaking caller asks the agent to book a dermatology appointment from a referral letter; the agent transcribes French text, reasons about intent, calls `get_referral(ref="4420 1187")` and `book_appointment(slot="Nov 3 17:45")`, then replies in English — demonstrating cross-language listening + reasoning + multi-step tool use + speaking in one turn.

## Positioning

Voxtral 3 is Mistral's bid to own the **end-to-end voice-agent layer** rather than only selling an ASR or TTS model. By including an SDK that does tool calling inside the voice loop, it competes directly with the "voice agent" stacks built by stitching OpenAI/Whisper-style ASR + a frontier LLM + a TTS vendor — but with EU data sovereignty and self-hosting as differentiators.

## Related

- [[concepts/speech-audio-asr-tts-voice]] — the broader ASR/TTS/voice-agent landscape this extends
- [[concepts/speech]] — speech processing concept hub
- [[entities/mistral-ai]] — the releasing lab
- [[concepts/tool-use-necessity]] — the "act over multiple steps" capability the SDK adds
- [[concepts/programmatic-tool-calling]] — tool-calling as a first-class agent capability
- [[concepts/sovereign-ai]] — the EU-hosted / self-deployed positioning
- [[concepts/multimodal]] — speech as a modality in agentic systems
