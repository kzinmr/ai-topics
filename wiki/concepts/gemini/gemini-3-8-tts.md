---
title: "Gemini 3.8 TTS (flash-tts / flash-lite-tts)"
created: 2026-09-23
updated: 2026-09-23
type: concept
tags:
  - model
  - google
  - multimodal
  - inference
sources:
  - raw/articles/simonwillison.net--2026-sep-23-gemini-tts-playground--4f8b21c7.md
related:
  - concepts/gemini/gemini-3-8-flash
  - concepts/gemini/index
  - entities/google
  - entities/simon-willison
confidence: medium
---

# Gemini 3.8 TTS (flash-tts / flash-lite-tts)

On 2026-09-23 Google released two new text-to-speech models in the Gemini 3.8 family: **`gemini-3.8-flash-tts`** and the cheaper **`gemini-3.8-flash-lite-tts`**. They extend the Sep 1 Gemini Drops release ([[concepts/gemini/gemini-3-8-flash]]) into the speech-synthesis modality.

## Key features

- **Two models**: `gemini-3.8-flash-tts` and the cheaper **`gemini-3.8-flash-lite-tts`** (full Google model list in Willison's post; Gemini API model picker at ai.google.dev).
- **2,000+ voice library**, plus **voice cloning from a 30-second audio sample** ("of your voice or a voice you have the rights to use").
- **Multi-speaker conversations as a first-class API primitive**: define a full conversation between multiple characters, each with a different voice and per-character voice style instructions — no stitching of separate calls.
- **Open CORS policy** on the Gemini API, which enables fully client-side, bring-your-own-key playground tools in the browser.

## Cost & latency (Willison's measurement)

Simon Willison's Gemini 3.8 TTS Playground demo (a GPT-6-Astra-vibe-coded, BYO-key UI; script for the demo conversation written by Claude 4.5 Opus): **~20 seconds to generate 1m18s of multi-voice audio at a cost of 2.74 cents** with the (non-lite) flash-tts model. Super-cheap, near-interactive speech synthesis — a relevant data point for voice-agent economics ([[concepts/token-economics]]).

## See Also

- [[concepts/gemini/gemini-3-8-flash]] — same-day family sibling (text/Flash tier)
- [[concepts/gemini/index]] — Gemini family hub
- [[entities/simon-willison]] — built the reference playground; his Sep 22 post covers the concurrent Anthropic/OpenAI releases

## Sources

- [[raw/articles/simonwillison.net--2026-sep-23-gemini-tts-playground--4f8b21c7.md]] — Tool: Gemini 3.8 TTS Playground (simonwillison.net, Sep 23 2026)
