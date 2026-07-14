---
title: "Apple's New Speech API vs Whisper: The First Real Benchmark"
date: 2026-07-13
source: "https://get-inscribe.com/blog/apple-speech-api-benchmark.html"
tags: [speech, benchmark, on-device, apple, model]
---

# Apple's New Speech API vs Whisper: The First Real Benchmark

**Source**: Inscribe Blog, published 2026-07-13
**Author**: Inscribe (get-inscribe.com)

## Summary

Apple shipped SpeechAnalyzer with iOS 26 and macOS 26, replacing the legacy SFSpeechRecognizer API, with no published accuracy numbers. Inscribe, a private on-device AI workspace, benchmarked all five on-device speech engines they ship — Apple SpeechAnalyzer, Apple SFSpeechRecognizer (legacy), and Whisper tiny/base/small via WhisperKit CoreML — on 5,559 LibriSpeech utterances (test-clean: 2,620; test-other: 2,939) on an Apple M2 Pro (32GB, macOS 26.5.1).

## Results

### Word Error Rate (WER) — Lower is Better

| Engine | test-clean WER | test-other WER | Model Size |
|---|---|---|---|
| **Apple SpeechAnalyzer** (iOS/macOS 26) | **2.12%** | **4.56%** | system |
| Whisper Small (WhisperKit CoreML) | 3.74% | 7.95% | ~460MB |
| Whisper Base | 5.42% | 12.51% | ~140MB |
| Whisper Tiny | 7.88% | 17.04% | ~40MB |
| Apple SFSpeechRecognizer (legacy) | 9.02% | 16.25% | system |

### Validation

Whisper results reproduced OpenAI's published LibriSpeech WERs within 0.11 to 0.42 points on all six measurements, validating corpus handling, text normalization, and scoring. Small consistent positive offset attributed to stricter text normalizer plus CoreML quantization.

## Key Findings

1. **SpeechAnalyzer vs Legacy**: 3.5-4x improvement in WER. Legacy API scored 9.02% on clean speech (last place, behind Whisper Tiny's 7.88%). SpeechAnalyzer scored 2.12%.
2. **SpeechAnalyzer vs Whisper**: Beat Whisper Small by comfortable margins on both splits while running ~3x faster per second of audio.
3. **Speed**: All engines ran faster than real-time (12-40x). SpeechAnalyzer ~3x faster than Whisper Small.
4. **Whisper advantages**: Far more languages (100+ vs ~30 locales for SpeechTranscriber); runs on non-Apple platforms.

## Methodology

- Same production code paths used in Inscribe app
- LibriSpeech text normalization: casing, punctuation, digits-to-words, contractions — mirrors OpenAI's English normalizer
- Corpus WER (total errors / total reference words), not averaged WER
- Fully on-device: `requiresOnDeviceRecognition` enforced; harness refused to run without on-device model
- Failures counted: 1 failure in 27,795 transcriptions (legacy, test-other)
- Raw per-utterance transcripts released for independent rescoring

## Limitations

- English only (LibriSpeech is English read speech)
- Read audiobook speech, not meetings (accented/far-field/multi-speaker follow-up needed)
- One machine: M2 Pro, macOS 26.5.1
- Whisper via WhisperKit CoreML (quantized on-device conversions)

## Data Downloads

- summary.json: https://get-inscribe.com/data/speech-benchmark/summary.json
- raw-transcripts-apple.json.gz: https://get-inscribe.com/data/speech-benchmark/raw-transcripts-apple.json.gz
- raw-transcripts-legacy.json.gz: https://get-inscribe.com/data/speech-benchmark/raw-transcripts-legacy.json.gz

## Product Impact

Inscribe changed its Auto engine default: now prefers SpeechAnalyzer for supported languages, Whisper for everything else. The benchmark also found a shipping bug where `finalizeAndFinishThroughEndOfInput()` was never called, causing hangs on Apple-engine file imports — fixed same day.
