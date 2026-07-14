---
title: "Apple SpeechAnalyzer"
type: concept
created: 2026-07-14
updated: 2026-07-14
tags: [speech, benchmark, on-device, apple, model, voice-ai]
sources:
  - raw/articles/2026-07-13_getinscribe_apple-speech-api-benchmark.md
---

# Apple SpeechAnalyzer

## What It Is

Apple SpeechAnalyzer is Apple's next-generation on-device speech recognition API, introduced with iOS 26 and macOS 26 as part of the Speech framework. It replaces the legacy SFSpeechRecognizer API with a new engine that delivers substantially higher accuracy while running fully on-device. Alongside it, Apple also introduced SpeechTranscriber, which handles language identification and transcription for approximately 30 locales.

The API is accessible to third-party developers and powers system-level features like dictation, Voice Control, and live captions. Apple published no official accuracy figures for the new engine, leaving developers to benchmark it themselves or migrate blind.

## Benchmark Results (vs Whisper, July 2026)

The first independent benchmark was published by Inscribe on 2026-07-13, measuring all five on-device engines against LibriSpeech test-clean (2,620 utterances) and test-other (2,939 utterances) on an Apple M2 Pro (macOS 26.5.1). All engines ran fully offline with `requiresOnDeviceRecognition` enforced.

| Engine | test-clean WER | test-other WER | Model Size |
|---|---|---|---|
| **Apple SpeechAnalyzer** | **2.12%** | **4.56%** | system |
| [[concepts/whisper|Whisper]] Small (WhisperKit CoreML) | 3.74% | 7.95% | ~460MB |
| Whisper Base | 5.42% | 12.51% | ~140MB |
| Whisper Tiny | 7.88% | 17.04% | ~40MB |
| SFSpeechRecognizer (legacy) | 9.02% | 16.25% | system |

Lower is better. WER = word error rate, percentage of words substituted, dropped, or invented. Corpus WER (total errors ÷ total reference words), not averaged.

### Validation

The benchmark's Whisper results reproduced OpenAI's published LibriSpeech WERs within 0.11–0.42 points on all six measurements, validating the corpus handling, text normalization, and scoring methodology. The small consistent positive offset is attributed to a slightly stricter text normalizer and CoreML quantization.

### Speed

All five engines ran faster than real-time (12–40x on M2 Pro). SpeechAnalyzer was approximately 3× faster than Whisper Small per second of audio while beating it on accuracy.

## On-Device Advantages

SpeechAnalyzer inherits the privacy and reliability benefits of the [[concepts/speech|on-device speech]] paradigm:

- **No network latency**: Transcription begins immediately without round-trip to Apple's servers. This is critical for real-time use cases like live captions and voice commands.
- **Privacy-preserving**: Audio never leaves the device. No data is uploaded, no transcription logs exist server-side. This is the default when `requiresOnDeviceRecognition` is set.
- **No API costs**: Once the OS is installed, there are no per-utterance or per-minute charges. This contrasts with cloud-based ASR services like OpenAI Whisper API, Deepgram, or AssemblyAI.
- **Offline capability**: Works without internet connectivity, making it suitable for fieldwork, flights, and privacy-sensitive environments.

## Limitations and Tradeoffs

- **Language coverage**: SpeechTranscriber supports approximately 30 locales. [[concepts/whisper|Whisper]] supports 100+ languages. For non-English or multilingual use cases, Whisper remains the more capable option.
- **Platform lock-in**: SpeechAnalyzer requires Apple platforms running OS 26+. Unlike Whisper, it cannot run on Windows, Linux, Android, or older macOS/iOS versions.
- **Apple Silicon only**: Accuracy validated on M2 Pro. Performance on Intel Macs or older devices is unknown. While accuracy should transfer across Apple Silicon, speed will vary by chip.
- **English bias in benchmarks**: LibriSpeech is English read audiobook speech. Performance on accented, far-field, or multi-speaker meeting audio is not yet measured.
- **Closed model**: Unlike Whisper (open-weight), SpeechAnalyzer is a black-box system model. Developers cannot inspect, fine-tune, or modify the underlying model.

## Migration from SFSpeechRecognizer

The legacy SFSpeechRecognizer API is substantially worse: 3.5–4× higher WER on the same audio. On clean speech, it finished last (9.02% WER), behind even Whisper Tiny (7.88%), a 40MB model. The new API also produces punctuated, cased text where the legacy engine's output is rougher. Migration is recommended for any app transcribing more than short voice commands.

## Product Impact

Inscribe changed its Auto engine selection based on these results: SpeechAnalyzer is now preferred for supported languages, with Whisper as fallback for everything else. The benchmark also uncovered a shipping bug — `finalizeAndFinishThroughEndOfInput()` was never called, causing hangs on Apple-engine file imports — demonstrating that rigorous benchmarking of one's own product surfaces latent issues.

## Related Pages

- [[concepts/speech]] — Speech AI overview (TTS, ASR, voice interaction)
- [[concepts/whisper]] — OpenAI's open-weight speech recognition model
- on-device AI — On-device AI advantages and ecosystem
- Apple — Apple as an AI/ML entity
