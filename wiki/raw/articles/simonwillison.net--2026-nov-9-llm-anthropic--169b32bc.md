---
title: "llm-anthropic 0.31"
url: "https://simonwillison.net/2026/Nov/9/llm-anthropic/"
fetched_at: 2026-11-10T10:01:15.999481+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# llm-anthropic 0.31

Source: https://simonwillison.net/2026/Nov/9/llm-anthropic/

Anthropic
released Fable 5.2 and Mythos 5.2
today. Fable 5.2 is currently
ranked first on Artificial Analysis
. Anthropic say it "solved two open problems in the physics of black holes", so clearly their internal benchmarks have become more ambitious!
I've added the new models to
llm-anthropic
, so you can now run prompts through Fable 5.2 like this:
uv tool install llm
llm install llm-anthropic
llm keys set anthropic
# paste key here
llm -m claude-fable-5.2 "Generate an SVG of a pelican riding a bicycle"
I ran pelicans at all five reasoning levels -
low
,
medium
,
high
,
xhigh
, and
max
. You can
see them all here
- here's the best result I got, from
xhigh
:
max
failed to return an image at all, running out of tokens after spending 128,000
thinking about them
. That's the same bug that I saw with
Opus 5.5
- but it's new for the Fable series, both
Fable 5
and
Fable 5.1
returned max effort pelicans just fine.
It's priced at $8/million input and $40/million output, which is a 20% discount on the previous Fable 5.1 ($10/$50).
I also used Fable 5.2 to
help identify the source of a mysterious beep
.
