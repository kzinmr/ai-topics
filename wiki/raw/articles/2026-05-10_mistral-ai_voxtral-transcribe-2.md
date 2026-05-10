---
title: "Voxtral transcribes at the speed of sound."
source: "Mistral AI Blog"
url: "https://mistral.ai/news/voxtral-transcribe-2"
scraped: "2026-05-10T01:21:03.330655+00:00"
lastmod: "2026-03-16T19:16:36.123Z"
type: "sitemap"
---

# Voxtral transcribes at the speed of sound.

**Source**: [https://mistral.ai/news/voxtral-transcribe-2](https://mistral.ai/news/voxtral-transcribe-2)

Voxtral
Transcribe 2
Listening...
L
i
s
t
e
n
i
n
g
.
.
.
Voxtral transcribes
at the speed of sound.
Try Voxtral Transcribe 2 in Mistral Studio
Precision diarization, real-time
transcription, and a new audio playground.
Today, we're releasing Voxtral Transcribe 2, two next-generation speech-to-text models with state-of-the-art transcription quality, diarization, and ultra-low latency. The family includes Voxtral Mini Transcribe V2 for batch transcription and Voxtral Realtime for live applications. Voxtral Realtime is open-weights under the Apache 2.0 license.
We're also launching an
audio playground in Mistral Studio
to test transcription instantly, powered by Voxtral Transcribe 2, with diarization and timestamps.
Highlights.
Voxtral Mini Transcribe V2: State-of-the-art transcription with speaker diarization, context biasing, and word-level timestamps in 13 languages.
Voxtral Realtime: Purpose-built for live transcription with latency configurable down to sub-200ms, enabling voice agents and real-time applications.
Best-in-class efficiency: Industry-leading accuracy at a fraction of the cost, with Voxtral Mini Transcribe V2 achieving the lowest word error rate, at the lowest price point.
Open weights: Voxtral Realtime ships under Apache 2.0, deployable on edge for privacy-first applications.
Voxtral Realtime.
Voxtral Realtime is purpose-built for applications where latency matters. Unlike approaches that adapt offline models by processing audio in chunks, Realtime uses a novel streaming architecture that transcribes audio as it arrives. The model delivers transcriptions with delay configurable down to sub-200ms, unlocking a new class of voice-first applications.
Word error rate (lower is better) across languages in the FLEURS transcription benchmark.
At 2.4 seconds delay, ideal for subtitling, Realtime matches Voxtral Mini Transcribe V2, our latest batch model. At 480ms delay, it stays within 1-2% word error rate, enabling voice agents with near-offline accuracy.
The model is natively multilingual, achieving strong transcription performance in 13 languages, including English, Chinese, Hindi, Spanish, Arabic, French, Portuguese, Russian, German, Japanese, Korean, Italian, and Dutch. With a 4B parameter footprint, it runs efficiently on edge devices, ensuring privacy and security for sensitive deployments.
We’re releasing the model weights under Apache 2.0 on the
Hugging Face Hub.
Voxtral Mini Transcribe V2.
Average diarization error rate (lower is better) across five English benchmarks (Switchboard, CallHome, AMI-IHM, AMI-SDM, SBCSAE) and the TalkBank multilingual benchmark (German, Spanish, English, Chinese, Japanese).
Average word error rate (lower is better) across the top-10 languages in the FLEURS transcription benchmark.
Voxtral Mini Transcribe V2 delivers significant improvements in transcription and diarization quality across languages and domains. At approximately 4% word error rate on FLEURS and $0.003/min, Voxtral offers the best price-performance of any transcription API. It outperforms GPT-4o mini Transcribe, Gemini 2.5 Flash, Assembly Universal, and Deepgram Nova on accuracy, and processes audio approximately 3x faster than ElevenLabs’ Scribe v2 while matching on quality at one-fifth the cost.
Model features.
Voxtral Mini Transcribe 2 introduces key capabilities.
Speaker diarization.
Generate transcriptions with speaker labels and precise start/end times. Ideal for meeting transcription, interview analysis, and multi-party call processing. Note: with overlapping speech, the model typically transcribes one speaker.
Context biasing.
Provide up to 100 words or phrases to guide the model toward correct spellings of names, technical terms, or domain-specific vocabulary. Particularly useful for proper nouns or industry terminology that standard models often miss. Context biasing is optimized for English; support for other languages is experimental.
Word-level timestamps.
Generate precise start and end timestamps for each word, enabling applications like subtitle generation, audio search, and content alignment.
Expanded language support.
Like Realtime, this model now supports 13 languages: English, Chinese, Hindi, Spanish, Arabic, French, Portuguese, Russian, German, Japanese, Korean, Italian, and Dutch. Non-English performance significantly outpaces competitors.
Noise robustness.
Maintains transcription accuracy in challenging acoustic environments, such as factory floors, busy call centers, and field recordings.
Longer audio support.
Process recordings up to 3 hours in a single request.
Word error rate (lower is better) across languages in the FLEURS transcription benchmark.
Audio playground.
Test Voxtral Transcribe 2 directly in
Mistral Studio
. Upload up to 10 audio files, toggle diarization, choose timestamp granularity, and add context bias terms for domain-specific vocabulary. Supports .mp3, .wav, .m4a, .flac, .ogg up to 1GB each.
Transforming voice applications.
Voxtral powers voice workflows in diverse applications and industries.
Meeting intelligence.
Transcribe multilingual recordings with speaker diarization that clearly attributes who said what and when. At Voxtral's price point, annotate large volumes of meeting content at industry-leading cost efficiency.
Voice agents and virtual assistants.
Build conversational AI with sub-200ms transcription latency. Connect Voxtral Realtime to your LLM and TTS pipeline for responsive voice interfaces that feel natural.
Contact center automation.
Transcribe calls in real time, enabling AI systems to analyze sentiment, suggest responses, and populate CRM fields while conversations are still happening. Speaker diarization ensures clear attribution between agents and customers.
Media and broadcast.
Generate live multilingual subtitles with minimal latency. Context biasing handles proper nouns and technical terminology that trip up generic transcription services.
Compliance and documentation.
Monitor and transcribe interactions for regulatory compliance, with diarization providing clear speaker attribution and timestamps enabling precise audit trails.
Both models support GDPR and HIPAA-compliant deployments through secure on-premise or private cloud setups.
Get started.
Voxtral Mini Transcribe V2
is available now via API at $0.003 per minute. Try it now in the new Mistral Studio
audio playground
or in
Le Chat
.
Voxtral Realtime
is available via API at $0.006 per minute and as open weights on
Hugging Face
.
Explore documentation
on Mistral’s audio and transcription capabilities.
We’re hiring.
If you're excited about building world-class speech AI and putting frontier models into the hands of developers everywhere, we'd love to hear from you.
Apply to join our team
.
Share this article
More from Mistral AI
News
Models
AI Services
