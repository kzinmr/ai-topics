---
title: "Anthropic's IPO roadshow video (Tom Brown compute section, Simon Willison transcript)"
type: raw-article
source_url: https://simonwillison.net/2026/Nov/11/anthropic-ipo-roadshow/
author: Simon Willison
published: 2026-11-11
fetched: 2026-11-12
tags: [anthropic, compute-strategy, recursive-self-improvement, gpu, tpu, trainium, amd]
---

# Anthropic IPO roadshow — compute strategy (via Simon Willison, Nov 11 2026)

Anthropic kicked off its IPO roadshow Nov 10, 2026. The roadshow video contains previously unreleased business details. Simon Willison extracted a transcript with MacWhisper (no official transcript).

## Key quotes (Tom Brown, co-founder, "Approach to compute")

- **Multi-chip strategy**: "We train and serve Claude now across all four major chip families" — AWS Trainium, Google TPUs, NVIDIA GPUs, AMD GPUs. An "unconventional bet" early on; each chip needs its own tailored software + inference stack.
- **Mythos AMD port**: "this year, we started working with AMD GPUs for the first time. In the past, bringing on a new chip platform took dozens of engineers months of work. This time, we had Mythos try it out. **It got Claude running on AMD in just three days, with basically no human intervention. Claude ported or wrote almost 100% of the kernels.**"
- **Compute multipliers**: total effective compute = physical capacity × discovered compute multipliers. "Say you need 100 units of compute to train a model of a certain intelligence. A 4x compute multiplier means you can use 25 units to train the exact same model. Or use those hundred physical units to train an even more intelligent model that would have previously required 400 units."
- Multipliers compound/stack — "Each new multiplier we discover has a positive effect on the multipliers before it."
- **RSI framing**: "We believe that this can accelerate even further as we approach recursive self-improvement. **Claude will be able to discover compute multipliers entirely by itself**, allowing the number of compute multipliers to grow faster and faster."

## Simon's context note

Multi-chip strategy was hinted at in Anthropic's September 2025 "postmortem of three recent issues" (bugs affecting only TPU deployments).

## Tags/labels on Simon's post

ai, generative-ai, llms, anthropic, gpus, claude-mythos-fable, recursive-self-improvement
