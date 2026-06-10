---
title: "OpenAI Realtime API"
type: concept
created: 2026-06-02
updated: 2026-06-02
tags:
  - concept
  - openai
  - realtime
  - voice-ai
  - ai-agents
  - streaming
sources:
  - raw/articles/2025-09-12_openai-developers-blog_realtime-api.md
  - raw/articles/2026-03-25_openai-developers-blog_realtime-perplexity-computer.md
  - raw/articles/2025-12-22_openai-developers-blog_updates-audio-models.md
related:
  - concepts/speech-audio-asr-tts-voice
  - entities/openai
  - concepts/openai-agents-sdk
status: active
---

# OpenAI Realtime API

## Overview

The **OpenAI Realtime API** is a WebSocket-based API for building low-latency, multimodal voice and text agents. It enables speech-to-speech (S2S) interactions natively — audio goes in, audio comes out — without separate ASR/TTS pipeline stages. The API graduated to general availability (GA) in 2025 with the `gpt-realtime` model, and has since become a key building block for production voice applications at companies like Perplexity.

Compared to traditional [[concepts/speech-audio-asr-tts-voice|voice agent pipelines]] (ASR → LLM → TTS), the Realtime API collapses the stack into a single model call with streaming audio I/O, reducing latency and eliminating intermediate transcription errors.

## Key Features

### Streaming Audio I/O
- Bidirectional audio streaming over WebSocket or WebRTC
- Server-side Voice Activity Detection (VAD) for automatic turn detection
- Configurable idle timeout to prompt unresponsive users (`idle_timeout_ms`)
- Support for SIP and WebRTC direct connections

### Function Calling in Realtime
- Asynchronous function calling — the model continues the conversation while awaiting tool results
- Automatic placeholder responses ("I'm still waiting on that") to prevent hallucinated tool outputs
- Sideband control channels to keep tool logic on the application server

### Session Management
- Sessions last up to 60 minutes (increased from 30 minutes)
- 32,768 token context window (4,096 max output, 28,672 max input)
- Automatic truncation with configurable retention ratio for cache-friendly behavior
- Hosted prompts with versioning and variable substitution

### Model Variants
| Model | Use Case |
|-------|----------|
| `gpt-realtime` | Full-size, best accuracy for production voice agents |
| `gpt-realtime-mini` | Cost-optimized, near-instant latency |
| `gpt-4o-mini-transcribe` | Streaming ASR via Realtime or Transcription API |
| `gpt-4o-mini-tts` | Text-to-speech via Speech API |

The December 2025 mini snapshots showed +18.6pp instruction-following accuracy and +12.9pp tool-calling accuracy over previous versions.

## Perplexity Case Study: Voice Search at Scale

Perplexity used the Realtime API (Realtime-1.5) to power millions of monthly voice sessions across Perplexity Comet and Perplexity Computer. Key lessons:

1. **Context management**: Large context updates fail in all-or-nothing fashion. Use small ~2,000-token incremental chunks instead of large blocks.
2. **Message role semantics**: Correctly assigning `system`, `user`, and `assistant` roles to context items is critical — wrong roles cause the model to misinterpret who is speaking.
3. **Audio standardization**: Perplexity built a Rust SDK to normalize audio across platforms (Swift, TypeScript, C++) — resampling to 48 kHz mono, echo cancellation, noise reduction before hitting the API.
4. **Voice Activity Detection tuning**: Tune VAD against real-world noisy environments (e.g., a loud bar), not just clean lab conditions.
5. **Voice lock pattern**: Instead of push-to-talk, invert the UX — ambient by default, user locks voice when holding the floor.
6. **Tool discipline**: Keep tools under 10, format outputs as structured JSON (not assistant dialogue), and keep schemas "in distribution" for the model.

## Session Configuration Example

```json
{
  "type": "session.update",
  "session": {
    "type": "realtime",
    "instructions": "You are a helpful assistant.",
    "audio": {
      "input": {
        "turn_detection": {
          "type": "server_vad",
          "idle_timeout_ms": 6000
        }
      }
    },
    "truncation": {
      "type": "retention_ratio",
      "retention_ratio": 0.8
    }
  }
}
```

## Realtime API vs Traditional Pipeline

| Dimension | Realtime API | ASR → LLM → TTS |
|-----------|-------------|------------------|
| Latency | Single model call, sub-second | 3 sequential calls, 1-3s |
| Interruption handling | Native VAD + turn detection | Custom implementation needed |
| Function calling | Async, concurrent with speech | Sequential after transcription |
| Context management | Built-in truncation + caching | Manual across components |
| Complexity | Single WebSocket connection | Multiple service orchestration |

## Related

- [[concepts/speech-audio-asr-tts-voice]] — Broader speech/audio landscape and comparison with other providers
- [[entities/openai]] — OpenAI entity page
- [[concepts/openai/agents-sdk]] — OpenAI's agent framework (can use Realtime API as voice backend)

## Sources

- [Developer notes on the Realtime API (2025-09-12)](https://developers.openai.com/blog/realtime-api/) — GA announcement, API features, session management
- [How Perplexity Brought Voice Search to Millions (2026-03-25)](https://developers.openai.com/blog/realtime-perplexity-computer/) — Perplexity production architecture and lessons
- [Updates for developers building with voice (2025-12-22)](https://developers.openai.com/blog/updates-audio-models/) — New audio model snapshots and improvements
