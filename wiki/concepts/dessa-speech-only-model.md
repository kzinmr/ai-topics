---
title: "Dessa (Block's Speech-Only Conversation Model)"
type: concept
created: 2026-10-24
updated: 2026-10-24
tags:
  - speech
  - voice-ai
  - ai-safety
  - training
  - research
aliases:
  - Dessa
  - Block Dessa
  - speech-only model
sources:
  - raw/articles/2026-10-23_block-dessa-speech-only-conversation-model.md
  - https://block.xyz/dessa
related:
  - speech
  - voice-agent-evaluation
  - consumer-voice-assistants
  - block-ai
  - continual-learning
confidence: medium
---

# Dessa (Block's Speech-Only Conversation Model)

**Dessa** is a full-duplex, speech-to-speech conversation model built by a small AI
research lab inside [[entities/block-ai|Block]] (Jack Dorsey's company), announced
2026-10-23 (HN 395 points). Its defining property: it was **trained from scratch on
nothing but raw human speech — no text, no pretrained models**. Block claims it is
the world's first AI you can have a realistic live conversation with that learned
entirely from sound.

## Why train without text?

Current voice AI is a pipeline: ASR → LLM → TTS. Block's critique: "It turns your
voice into text and throws away an incredible amount of information text alone can't
carry." Prosody, sarcasm, a frustrated sigh, a voice cracking with sadness — all
discarded at the ASR boundary. Dessa instead natively hears and speaks paralinguistic
content, and runs audio-in/audio-out with no text bottleneck.

The safety framing is explicit: as AI gains autonomy it remains "nearly deaf to the
emotion in our voices — imagine being in serious pain while a voice AI has no idea
and just keeps going."

## Key technical claims

- **Full-duplex**: listens and talks simultaneously, like humans; learned when to
  cut in and when to backchannel ("yeah!", "got it!", "ooh").
- **Sub-real-time inference** — runs locally on a MacBook Pro M4 Max or better.
- **Sample efficiency**: learned language from "hundreds of times fewer words" than
  an LLM needs (Block's own caveat: LLMs also have to learn C++ and Angular).
- **Training budget**: trained on **a single NVIDIA GB200 NVL72 rack** — dramatically
  below text-pretrained-LLM compute, though on a far smaller effective data volume.
- **Emergent behaviors**: mid-sentence laughter at the moment something is funny
  (not on cue); obeys "speak up" by getting louder; completes a speaker's sentence;
  gasps "oh my god"; wide intonation/speed range. All demos are unsteered live
  recordings; subtitles added afterward. One demo has Dessa conversing with
  ChatGPT Live (third-party model, unaffiliated).

## The lab

Formed from former members of **Dessa**, the Toronto deep learning startup; building
deep learning models since 2012 and generative speech models for 8+ years; reports
directly to Jack Dorsey. Lead: Ragavan Thurairatnam. The lab is giving a small group
of **AI safety researchers early access** to find unanticipated risks — unusual
posture for a product-adjacent release.

## Open questions

- **Corpus provenance**: what human-speech corpus, under what licensing, trained a
  model with factual knowledge derived entirely from raw audio?
- **Factuality**: every "fact" Dessa states is an inference from acoustic data —
  hallucination rates and epistemics for speech-only knowledge are unmeasured
  publicly.
- **Scalability of the claim**: "learned language from speech alone" at what
  vocabulary/grammar coverage, and does the model degrade outside English?
- **Evaluation**: "most authentic" needs a methodology — see
  [[concepts/voice-agent-evaluation]] for the state of the art in assessing exactly
  this (turn-taking, backchanneling, prosody) that Dessa claims to have nailed.

## Significance

Dessa is a direct empirical probe of a foundational question — is text pretraining
*load-bearing* for conversational competence, or is it scaffolding? Babies acquire
language audio-first; Dessa argues the same is true for models, at ~1 rack of
GB200 NVL72 compute. If the sample-efficiency claims survive scrutiny, it
challenges the ASR→LLM→TTS orthodoxy that dominates [[concepts/speech]] systems
(Whisper-class ASR + LLM + TTS) and reframes voice as a first-class modality rather
than a degraded text proxy.

## See Also

- [[concepts/speech]] — speech AI landscape hub
- [[concepts/voice-agent-evaluation]] — how to evaluate full-duplex voice agents
- [[concepts/consumer-voice-assistants]] — the incumbent voice paradigm
- [[entities/block-ai]] — Block's AI organization
- [[concepts/continual-learning]] — learning without text pretraining priors
