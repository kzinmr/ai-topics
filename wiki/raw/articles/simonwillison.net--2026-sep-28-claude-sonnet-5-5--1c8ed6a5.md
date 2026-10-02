---
title: "Claude Sonnet 5.5"
url: "https://simonwillison.net/2026/Sep/28/claude-sonnet-5-5/"
fetched_at: 2026-09-29T10:01:07.725140+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Claude Sonnet 5.5

Source: https://simonwillison.net/2026/Sep/28/claude-sonnet-5-5/

28th September 2026 - Link Blog
Claude Sonnet 5.5
. New Sonnet model from Anthropic today. They say it "runs 30%+ faster, and costs up to 30% less for most work" - it's priced the same as Sonnet 5 but appears to beat it on every benchmark, and should be cheaper to run as well.
Here are some pelicans riding bicycles
. Sonnet 5.5 suffered from
the same bug as Opus 5.5
: the "max" thinking effort pelican thought for 128,000 tokens (at a cost of $1.28) before running out of tokens and failing to produce an SVG.
Here's the pelican it gave me for thinking effort "xhigh", at a cost of 5.74 cents and taking 41 seconds:
Sonnet 5.5 appears to be almost as good as Opus 5.5 on some coding tasks, including various
viral 3D animation tricks
.
The most interesting thing about Sonnet 5.5 is that it's now the model used for the free tier on
claude.ai
. OpenAI's ChatGPT free tier uses Luna 5.6, which means Anthropic currently have a much more capable free offering.
I ran this prompt against that free tier:
build me an HTML page that renders a three-dimensional pelican riding a bicycle using WebGL
And got back
this page
, which is a solid effort.
Anthropic's announcement reiterates that Haiku 5.5 will be available "in the coming weeks". I really hope that one is price-competitive with GPT-6 Luna!
