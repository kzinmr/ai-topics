---
title: Corti
created: 2026-05-26
updated: 2026-05-26
type: entity
tags: [entity, company, voice-ai, model, audio-generation]
sources: [raw/articles/2026-05-20_corti-symphony-speech-to-text.md]
---

# Corti

Healthcare's frontier lab for clinical-grade AI. Develops the Symphony family of clinical-grade AI models for speech recognition and medical reasoning. Headquarters in Copenhagen, with offices in New York and London.

## Scale
Serves over 100 million patients annually across health systems including the NHS (UK). Powers clinical and administrative applications for EHR vendors, virtual care platforms, practice management systems, and life sciences organizations worldwide.

## Symphony for Speech-to-Text (May 2026)

Launched May 20, 2026 as a new generation of clinical-grade speech-to-text models:

### Performance vs General-Purpose Models (English WER)
| System | WER |
|--------|-----|
| **Corti Symphony** | **1.4%** |
| OpenAI | 17.7% |
| ElevenLabs | 18.1% |
| Whisper | 17.4% |
| Parakeet | 18.9% |

- **93% lower WER** vs leading general-purpose speech models
- **98.3% recall** on formatted entities (dosages, measurements, dates) vs 44.3% best baseline
- **Surpasses Dragon Medical One**: 4.6% WER vs 5.7%, medical term recall 93.5% vs 92.9%
- **Multilingual**: 2.4% WER in German, 3.9% WER in French

### Strategic Positioning
> "In the agentic era, speech recognition requires more than simply producing a transcript — we need to give AI systems accurate clinical facts to reason from." — Andreas Cleve, CEO

Corti positions Symphony not as a transcription service but as a **speech layer for clinical AI agents** — providing downstream AI with accurate, structured clinical facts rather than raw transcripts.

## Related Pages
- [[entities/openai]] — Whisper benchmarked against Symphony
- [[entities/elevenlabs]] — Voice AI competitor benchmarked
- [[concepts/ai-agents]] — Agentic healthcare context
