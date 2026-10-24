---
source: https://block.xyz/dessa
author: Block AI research lab (Dessa team; lead Ragavan Thurairatnam)
date: 2026-10-23
fetched: 2026-10-24
type: article
title: "Dessa: Conversation Model trained only on speech"
sha256: pending
tags: [speech, voice-ai, block, ai-safety]
---

# Dessa: Conversation Model trained only on speech

Block (Jack Dorsey's company) product page, Oct 23 2026. HN 395 points.

## Summary

Dessa is described as "the most authentic full-duplex speech model ever built,"
trained **from scratch on nothing but human conversation** — no text, no pretrained
models. Block claims it is the world's first AI you can have a realistic live
conversation with that was trained only from human speech.

## Key claims

- **True speech-to-speech**: audio in, audio out. Full-duplex — listens and talks
  simultaneously; learned to cut in and backchannel ("yeah!", "got it!", "ooh").
- **No text pipeline**: current voice AI turns voice into text and "throws away an
  incredible amount of information text alone can't carry." Dessa natively hears and
  speaks emotion, sarcasm, laughter, frustrated sighs, a voice cracking with sadness.
- **Data efficiency**: learned language from "hundreds of times fewer words" than LLMs
  need (with the caveat that LLMs also have to learn C++ and Angular).
- **Training cost**: trained on only **one NVIDIA GB200 NVL72** rack.
- **Local inference**: runs faster than real time on a MacBook Pro M4 Max or better.
- **Emergent behaviors**: laughs mid-sentence at the moment something's funny;
  gets louder when asked to speak up; finishes a speaker's sentence when they blank
  on a movie title; gasps "oh my god" under its breath; wide range of intonation
  and speed; demoed conversing with ChatGPT Live (GPT-Live-1, third-party, unaffiliated).
- All demos are live recordings of people talking to Dessa with no steering; subtitles
  added afterward.

## Motivation (three reasons given)

1. Curiosity ("aka fun"): babies learn to talk without ever seeing a word written
   down — can a model too? It can, it's just very hard.
2. Better human-AI understanding: speech is the most natural interface to intelligence.
3. **Safety**: AI keeps gaining power while remaining nearly deaf to emotion in
   voices. "Imagine being in serious pain while a voice AI has no idea and just keeps
   going." Dessa is framed as a step toward fixing that.

## Research questions raised

How efficiently do speech-only models learn language and facts compared to text?
How efficiently can they learn new languages? What in-context learning can they perform?

## Lab & safety access

- Small AI research lab inside Block, founded by former members of **Dessa**, the
  Toronto deep learning startup. Building deep learning models since 2012, generative
  speech models for 8+ years. Reports directly to Jack Dorsey.
- Early access being given to a small group of AI safety researchers to find
  unanticipated risks.
- Researchers: Louay Hazami, Hashiam Kadhim, Qi (Alex) Liu, Rayhane Mama, Aydin
  Polat, Marc Tyndel. Interns: Cara Ji, Jibran Iqbal Shah, Dvir Zagury-Grynbaum.
- Former interns: Aryan Sharma, Olivia Yan.

## Notes

- Waitlist-gated; no public weights/API announced at capture time.
- Open questions for the community: training corpus provenance/licensing, evaluation
  methodology for "authenticity," hallucination/factuality profile given all knowledge
  derives from raw audio.
