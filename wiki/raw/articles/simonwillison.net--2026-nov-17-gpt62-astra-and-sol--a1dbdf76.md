---
title: "GPT‑6.2 Astra and GPT‑6.2 Sol"
url: "https://simonwillison.net/2026/Nov/17/gpt62-astra-and-sol/"
fetched_at: 2026-11-18T10:01:22.010969+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# GPT‑6.2 Astra and GPT‑6.2 Sol

Source: https://simonwillison.net/2026/Nov/17/gpt62-astra-and-sol/

GPT‑6.2 Astra and GPT‑6.2 Sol
. OpenAI:
We’re introducing GPT‑6.2 Astra, our new frontier model for your hardest projects, and GPT‑6.2 Sol, our efficient, versatile model for everyday work.
They're available in the API as
gpt-6.2-astra
and
gpt-6.2-sol
. I shipped
LLM 0.38
with support for the new models.
6.2 Astra is 80% of the price of 6 Astra - $8/MTok input and $40/MTok output, the same price as Claude Fable 5.2 (which was also 80% of its predecessor). 6 Astra and Fable 5 were both $10/$50. The cached price is an even bigger discount - $0.40/million compared to $1/million for the older model. This is great news for longer running agentic sessions.
GPT-6.2 Sol is the same $2/$10 price as 6.1 Sol and 6 Sol - which are half the price of GPT-5.6 Sol ($4/$20).
Here are the pelicans
for GPT-6.2 Sol
and
for GPT-6.2 Astra
. The 6.2 Astra max pelican looks like this:
I have a
full comparison grid here
, but here's how the high/xhigh/max pelicans compare with the previous Sol and Astra releases:
I also ran my most recent benchmark prompt against the two models, using "Ultra' effort levels in the Codex CLI:
Make a three js animation where yonkers stands up as a big mech (cool stand up motion) and stomps around manhattan and queens and Brooklyn, use openstreetmap mapping data
Here's
Sol
and here's
Astra
. Neither of them did a good enough job of morphing Yonkers into a big mech, at least in comparison to
Claude Fable 5.2
and
Gemini 4 Carbon
.
This video showing the Astra and Sol animations playing out at the same time:
I created that video using GPT-6.2 Astra (Ultra) in the Codex desktop app by prompting:
https://static.simonwillison.net/static/2026/yonkers-gpt-6.2-astra-ultra/index.html and https://static.simonwillison.net/static/2026/yonkers-gpt-6.2-sol-ultra/index.html  are two videos of the same thing by two different models
I need a video of the first 10 seconds where the top half of the video plays the first and the bottom half plays the second
I need an overlaid label of "GPT-6.2 Astra" on the top half and "GPT-6.2 Sol" on the bottom half. These labels should be tastefully positioned.
Make the video square and 2000x2000 pixels
Then later:
OK make it 20s
Here's the
exported transcript
.
The buzz around these new models is mixed at the moment. Astra 6.2 isn't scoring quite as high as Fable 5.2 on various benchmarks, and I've seen a few complaints that its communication style can be confusing. Theo Browne's
review
(in the form of a feedback letter he sent OpenAI during pre-release) has this useful example:
When this model is working on long tasks, it can pull in a lot of subagents and manage them pretty well. It will then proceed to randomly
ask you some weird internal implementation detail bullshit that you could not under any earthly circumstance understand, much less have input on
.
I sent "/goal make a new level for Outer Wilds". 2 hours in, it's "blocked" because it wanted to ask me "does r24's reviewer write it's clips to 24_g521.mp4 or 24_p11.mp4?"
