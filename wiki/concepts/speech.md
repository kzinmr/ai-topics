---
title: "Speech AI"
type: concept
tags:
  - multimodal
  - tts
  - voice
status: L3
created: 2026-04-27
updated: 2026-04-28
aliases: [Speech AI, Text-to-Speech, Voice AI, TTS]
related: [[concepts/multimodal]], [[concepts/gemini]], [[concepts/gpt-models]], [[entities/mistral-voxtral-tts]]
sources: [https://www.elevenlabs.com/, https://openai.com/index/chatgpt-voice/]
---

# Speech AI

## Summary

Speech AI encompasses the technologies for synthesizing human-like speech from text (Text-to-Speech, TTS), transcribing speech to text (Automatic Speech Recognition, ASR), and enabling real-time voice conversation with AI systems. The 2025-2026 era has seen a convergence of speech and multimodal AI — frontier models like GPT-4o and Gemini natively process audio as a modality, enabling real-time voice conversations with emotional tone, natural pauses, and interruption handling that approach human interaction quality.

## Key Ideas

- **Native Audio Modality**: GPT-4o and Gemini 2.5 process audio natively rather than through cascaded ASR→LLM→TTS pipelines, enabling end-to-end voice interaction with emotional understanding
- **Real-Time Voice Mode**: OpenAI's advanced voice mode (2024) and Gemini Live (2025) support real-time, emotional, interruptible voice conversations — a UX paradigm shift from text-based chat
- **Open-Weight TTS**: Mistral Voxtral TTS (April 2026) demonstrated that high-quality TTS can be achieved with open-weight models, combining autoregressive semantic token generation with flow-matching acoustic synthesis
- **Voice Cloning & Personalization**: Modern TTS systems (ElevenLabs, OpenAI) can clone voices from short samples and generate speech with controllable emotion, pace, and emphasis
- **Zero-Shot Voice Generation**: The latest wave of speech AI (2025-2026) can generate voice from text without speaker-specific training, using latent diffusion models applied to audio
- **Multilingual Speech**: Speech AI now supports 100+ languages with near-native accent quality, driven by massively multilingual training data

## Terminology

- **TTS (Text-to-Speech)**: Generating spoken audio from text input
- **ASR (Automatic Speech Recognition)**: Transcribing spoken audio to text (also called STT, Speech-to-Text)
- **Voice Cloning**: Creating a synthetic voice that matches a specific person's speech patterns, pitch, and timbre
- **Semantic Token Generation**: Autoregressive generation of high-level audio tokens representing linguistic content, used by Mistral Voxtral TTS
- **Flow-Matching**: A generative modeling technique for acoustic token synthesis, producing natural-sounding prosody and intonation
- **End-to-End Voice**: Systems where all voice processing stages (understanding, reasoning, generation) are handled by a single model rather than separate components

## Examples/Applications

- **Voice Assistants**: ChatGPT Voice Mode and Gemini Live enable natural, hands-free interaction with AI assistants
- **Accessibility**: TTS systems read text content aloud for visually impaired users; ASR enables voice-controlled interfaces
- **Content Creation**: AI voiceovers for videos, audiobooks, and podcasts using cloned or synthetic voices
- **Customer Service**: Real-time voice agents handling phone inquiries with natural conversation flow
- **Language Learning**: Interactive dialogue practice with AI that provides pronunciation feedback

## Related Concepts

- [[multimodal]]
- [[gemini]]
- [[gpt-models]]
- [[entities/mistral-voxtral-tts]]
- [[entities/vibevoice]]
- [[decoder-only-gpt]]

## Sources

- [ElevenLabs: Voice AI Platform](https://elevenlabs.io/)
- [ChatGPT Voice Mode | OpenAI](https://openai.com/index/chatgpt-voice/)
- [Mistral Voxtral TTS Announcement | Mistral AI](https://mistral.ai/news/mistral-voxtral-tts/)
