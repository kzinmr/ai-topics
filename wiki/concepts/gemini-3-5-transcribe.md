---
title: Gemini 3.5 Transcribe
created: 2026-08-27
updated: 2026-08-27
type: concept
tags: [model, speech, voice-ai, gemini, google]
sources:
  - raw/articles/2026-08-26_gemini-3-5-transcribe
  - https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/
  - https://news.ycombinator.com/item?id=49452393
related:
  - [[concepts/gemini/gemini-3-5-flash]]
  - [[concepts/speech-recognition]]
  - [[concepts/real-time-inference]]
  - [[entities/google]]
---

# Gemini 3.5 Transcribe

## Overview

Gemini 3.5 Transcribe is Google's most precise speech-to-text model, released on August 26, 2026. It's designed for intelligent voice interactions, handling background noise, complex jargon, and disfluency cleanup. Unlike conventional speech recognition models, Gemini 3.5 Transcribe converts raw audio directly into accurate, polished, formatted text.

## Key Specifications

- **WER (Word Error Rate)**: 4.0% for streaming, 2.6% for non-streaming (measured by Artificial Analysis)
- **Languages**: 85+ languages with regional accent and dialect support
- **Multi-speaker**: Speaker attribution and identification
- **Word-level**: Word-level timestamps available

## APIs

Gemini 3.5 Transcribe is available across two separate APIs:

### Real-time Streaming
- **Model**: `gemini-3.5-transcribe-live`
- **API**: Live API
- **Latency**: Sub-second
- **Use case**: Interactive voice apps

### Pre-recorded Audio Processing
- **Model**: `gemini-3.5-transcribe`
- **API**: Interactions API
- **Features**: Speaker attribution, word-level timestamps
- **Use case**: Meetings, call logs, post-call analytics

## Key Features

### Smart Transcription
- Seamlessly handles self-corrections ("let's meet Tuesday—no, Wednesday")
- Removes filler words ("ums" and "ahs")
- Auto-formats text

### Function Calling
- The model can delegate complex tasks (image generation, file analysis) to other Gemini models via function calls
- Currently available in the Gemini macOS app

### Custom Vocabulary
- Recognizes specialized jargon and unique spellings
- Adapts transcriptions to your provided custom vocabulary

### Global Language Support
- Automatically detects and transcribes over 85 languages
- Seamlessly handles regional accents and diverse dialects

## Use Cases

- **Voice agents**: Real-time voice interaction
- **Real-time captioning**: Live subtitles for video/audio
- **Post-call analytics**: Meeting transcription and analysis
- **Accessibility**: Real-time transcription for hearing-impaired users
- **Content creation**: Podcast transcription and editing

## Context

This release expands Google's Gemini model family with specialized capabilities. The transcription model complements general-purpose Gemini models with domain-specific optimization. It's already powering features like Rambler on Android and voice capabilities in the Gemini app on macOS.

## See Also

- [[concepts/gemini/gemini-3-5-flash]] — Gemini 3.5 Flash (general-purpose model)
- [[concepts/speech-recognition]] — Speech recognition fundamentals
- [[concepts/real-time-inference]] — Real-time inference architectures
- [[entities/google]] — Google (company)
