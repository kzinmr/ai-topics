---
title: "Tool: Gemini 3.8 TTS Playground"
url: "https://simonwillison.net/2026/Sep/23/gemini-tts-playground/"
fetched_at: 2026-09-23T22:40:00+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Tool: Gemini 3.8 TTS Playground

Source: https://simonwillison.net/2026/Sep/23/gemini-tts-playground/ (Simon Willison, 23rd September 2026)

Gemini 3.8 TTS Playground — an interactive playground for Google's Gemini 3.8 text-to-speech API: compose single-voice narration or multi-speaker conversations, preview generated audio, explore request/response details, save compose settings to bookmarkable URLs. Bring-your-own-key.

Key facts from the post:

- Google released **two new Gemini TTS models** today: `gemini-3.8-flash-tts` and `gemini-3.8-flash-lite-tts`.
- Library of **2,000+ voices**, plus custom voice creation from "just a 30-second audio sample of your voice or a voice you have the rights to use".
- Simon **vibe coded the playground with GPT-6 Astra**, taking advantage of the **open CORS policy** of the underlying Gemini API.
- Notable API feature: easy definition of a full conversation between multiple characters, each with different voices and voice style instructions.
- Demo: conversation between two pelicans debating moving to Pacifica Pier — script written by **Claude 4.5 Opus**, rendered via a generated URL.
- Cost/perf: **~20 seconds to generate 1m18s of audio** using Gemini 3.8 Flash TTS (not the cheaper Flash-Lite), **at a cost of 2.74 cents**.

Related posts: "Claude Opus 5.5, GPT-6 Sol, GPT-6 Luna, and a new price war" (Sep 22), "Jev introduces a new shape of LLM - System One, aka Decision Models" (Sep 21).
