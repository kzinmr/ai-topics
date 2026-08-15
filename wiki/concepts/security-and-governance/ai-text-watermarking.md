---
title: AI Text Watermarking
created: 2026-08-15
updated: 2026-08-15
type: concept
tags:
  - ai-safety
  - policy
  - regulation
  - eu-ai-act
  - disinformation
  - anthropic
  - text-generation
  - llm-output
sources:
  - raw/articles/2026-08-14_anthropic_claude-text-watermarking.md
  - https://www.anthropic.com/news/claude-text-watermark
---

# AI Text Watermarking

A technique for marking model-generated text so its provenance can later be statistically detected, without altering the visible output. Anthropic announced in August 2026 that future Claude models will generate watermarked text — the first frontier lab to ship model-level text watermarking.

## How it works

LLMs generate one word at a time, choosing among candidate next-tokens. For low-stakes choices (e.g. "overcast" vs "grey"), the choice is settled by randomness. Watermarking redirects the *source* of that randomness: instead of an arbitrary RNG, the model uses a secret **key** plus preceding words to settle each choice. Anyone holding the key can check whether a sequence is statistically consistent with Claude's sampling, and assign a probability that Claude wrote it.

Claude's implementation is a version of Google DeepMind's **SynthID-Text** (Nature, 2024), in a family going back to Scott Aaronson's 2022 proposal.

## Properties and limitations

- No quality/content impact; indistinguishable to readers; no hidden characters or extra tokens.
- Carries no identifying information; not traceable to users or chats.
- Weak on small samples and sparse on factual passages or exact-output code (fewer safe choices); translations are fully watermarked.
- Light editing likely preserves the watermark; a full rewrite removes it.

## Motivation: EU AI Act

As of August 2, 2026, the EU requires AI providers serving its market to mark AI-generated content. Anthropic, with ~190 signatories, signed the EU **Code of Practice on Transparency of AI-Generated Content** (July 2026). Applied globally at launch (no durable regional scoping yet). A detection API is planned. For files, Claude attaches **C2PA** content credentials (cryptographically signed metadata), distinct from text watermarking.

## Related

- [[concepts/claude-code/steganographic-watermarking|Steganographic Watermarking (Claude Code)]]
- [[concepts/security-and-governance/ai-safety|AI Safety]]
- [[concepts/ai-governance-political-pressure|AI Governance Political Pressure]]
- [[entities/anthropic|Anthropic]]
