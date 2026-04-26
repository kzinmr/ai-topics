---
title: "Whisper — OpenAI's Speech Recognition Model"
tags: [[concepts/speech-asr-openai-whisper-audio]]
created: 2026-04-19
updated: 2026-04-19
type: concept
---

# Whisper — OpenAI's Speech Recognition Model

Whisper is OpenAI's general-purpose speech recognition model, released in 2022. It uses a Transformer encoder-decoder architecture trained on 680k hours of multilingual and multitask supervised data.

## Architecture

- **Model Type:** Transformer encoder-decoder
- **Training Data:** 680k hours of multilingual audio (weak supervision from YouTube)
- **Languages:** 99 languages supported
- **Tasks:** Speech recognition, speech translation, voice activity detection, language identification

## Key Features

1. **Multilingual:** Trained on diverse languages, not just English
2. **Multitask:** Single model handles transcription, translation, and VAD
3. **Robust:** Performs well on noisy audio, accented speech, and technical terminology
4. **Open Weights:** Model weights are publicly available for local deployment

## Quantization & Local Deployment

Whisper is commonly deployed locally using:
- **llama.cpp:** GGUF quantization for CPU/Apple Silicon inference
- **OpenAI API:** Hosted whisper-1 endpoint
- **Faster-Whisper:** CTranslate2-based optimized inference (4x faster, half memory)
- **Whisper.cpp:** Pure C/C++ implementation for edge devices

## Use Cases in AI Agents

- **Voice interfaces:** Speech-to-text for agent input
- **Meeting transcription:** Async processing of audio recordings
- **Accessibility:** Real-time captioning for content
- **Multilingual agents:** Cross-language speech understanding

## Comparison to Alternatives

| Model | Speed | Accuracy | Local | Multilingual |
|-------|-------|----------|-------|--------------|
| Whisper (large-v3) | Medium | High | Yes | 99 languages |
| Faster-Whisper | Fast | High | Yes | Same as Whisper |
| OpenAI Whisper API | Fast | Highest | No | Same as Whisper |
| Vosk | Fast | Medium | Yes | 20+ languages |
| DeepSpeech | Medium | Medium | Yes | English only |

## Sources
- OpenAI Whisper paper (2022)
- OpenAI Whisper GitHub repository
- llama.cpp documentation
- Faster-Whisper project

## See Also

- [[concepts/speech]]
