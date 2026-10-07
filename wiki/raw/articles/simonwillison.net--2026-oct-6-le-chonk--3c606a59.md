---
title: "Introducing Mistral Large 4: Le chonk"
url: "https://simonwillison.net/2026/Oct/6/le-chonk/"
fetched_at: 2026-10-07T10:01:26.852683+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Introducing Mistral Large 4: Le chonk

Source: https://simonwillison.net/2026/Oct/6/le-chonk/

6th October 2026 - Link Blog
Introducing Mistral Large 4: Le chonk
(
via
) Mistral are back in the game. Today they're releasing a preview of Mistral Large 4, a 1 trillion parameter, 49 billion active parameter model trained on their own cluster of 3,800 NVIDIA Grace Blackwell GPUs.
The preview is available via their API. They promise to release the open weights model at the "end of this month".
The model only supports two reasoning levels - "none" and "high" - via the Mistral API. Here are
both pelicans
- the "high" one looks better, though surprisingly it only used 2,717 output tokens compared to "none" which used 3,275:
On Artificial Analysis
it scores 38
, just behind DeepSeek 4.1 Flash, which is a 552B model. It's a
huge
improvement on last December's Mistral Large 3, which drew
this terrible pelican
and
scored 9 on AA
.
It's certainly not a Fable-class model, but it's great to see Mistral put out a model that's back to being maybe about 6 months behind the frontier.
