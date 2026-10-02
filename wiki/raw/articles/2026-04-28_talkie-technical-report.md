---
title: "Introducing talkie: a 13B vintage language model from 1930"
url: "https://talkie-lm.com/"
date: 2026-04-28
source: "talkie-lm.com"
authors: ["Nick Levine", "David Duvenaud", "Alec Radford"]
citation: "levine2026talkie"
fetched_at: "2026-09-28"
tags: [raw, technical-report]
---

# Introducing talkie: a 13B vintage language model from 1930

Technical report / launch page. Full body captured 2026-09-28 via r.jina.ai.

## Core facts
- talkie-1930-13b-base: 13B model trained on **260B tokens** of pre-1931 English-language text.
- Largest vintage language model known to authors; plans to scale to GPT-3 level (summer 2026), corpus potentially >1T tokens (GPT-3.5-level).
- License: Apache-2.0. Org: talkie-lm (Hugging Face). Reference code: github.com/talkie-lm/talkie.
- Cutoff chosen at Dec 31, 1930 because that is when works enter US public domain.
- Corpus: books, newspapers, periodicals, scientific journals, patents, case law. Built off Institutional Data Initiative, Internet Archive, Common Pile.
- Framing: "vintage" language models (Owain Evans's phrase); inspired by Calcifer Computing's Temporal Language Models.

## Model variants
- talkie-lm/talkie-1930-13b-base (pretrained)
- talkie-lm/talkie-1930-13b-it (instruction-tuned post-train)
- talkie-lm/talkie-web-13b-base ("modern twin" -- identical architecture, trained on FineWeb instead of pre-1931 text)

## Vintage post-training pipeline (talkie-1930-13b-it)
1. Instruction-response pairs generated from historical texts with regular structure (etiquette manuals, letter-writing manuals, cookbooks, dictionaries, encyclopedias, poetry/fable collections), fine-tuned in a simple chat format.
2. Online DPO on synthetic prompts (summarization, info requests, multi-turn continuation), LLM-as-a-judge (Claude Sonnet 4.6). Judge's avg instruction-following rating rose 2.0 -> 3.4 (5-pt scale).
3. Final SFT on rejection-sampled multi-turn chats between Claude Opus 4.6 and talkie.
- Caveat: RL-with-AI-feedback anachronistically shapes behavior; the 7B version emerged speaking in listicles.

## Challenges documented
- **Temporal leakage**: document-level n-gram anachronism classifier used to filter corpus; imperfect -- earlier 7B knew Roosevelt presidency/New Deal; 13b still aware of some WWII/postwar facts (UN, division of Germany).
- **Data quality / OCR**: conventional OCR gives only 30% of learning efficiency of human-transcribed text at same compute; regex cleaning recovers to 70%. Modern VLM OCR hallucinates modern facts (poisons corpus). Building a dedicated "vintage OCR" system.

## Evaluations
- Surprisingness eval on ~5,000 NYT "On This Day" event descriptions; increased surprisingness after cutoff (esp. 1950s-60s), then plateau.
- Invention rediscovery framing (Demis Hassabis: could a 1911-cutoff model discover General Relativity?).
- HumanEval (Python) test on vintage-vs-modern pairs; vintage dramatically underperforms but slowly improves with scale; correct solutions are simple one-line / minor in-context edits (e.g., rotation-cipher decode by swapping + for -).
- Figure 4: eval accuracy vs training compute for talkie-1930 vs modern twin (FineWeb); filtering anachronistic questions roughly halves the gap. Suspect OCR quality + corpus subject-matter distribution.

## Related vintage-LM projects cited
Ranke-4B, Mr. Chatterbox, Machina Mirabilis.

## Support and acknowledgements
- Funding/compute: Coefficient Giving and Anthropic.
- Acknowledgements include Andrej Karpathy, John Schulman, Ethan Perez, Collin Burns, Ludwig Schmidt, Buck Shlegeris, among others.
- Content consideration: talkie reflects culture/values of training texts; can produce offensive outputs.

