---
title: "Release: llm 0.37"
url: "https://simonwillison.net/2026/Nov/2/llm/"
fetched_at: 2026-11-03T10:01:42.817859+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Release: llm 0.37

Source: https://simonwillison.net/2026/Nov/2/llm/

There's a
lot
of stuff in this new release of my LLM CLI tool and Python library, representing around two months of accumulated features and fixes.
I added
gpt-6.1-sol
and
gpt-6.1-terra
, plus a new
llm openai endpoint add
command to make it easier to configure additional models that use OpenAI-compatible endpoints.
I switched the default model (if you have not set your own default) to
gpt-6-luna
- half the price of the previous default,
gpt-5.6-luna
.
LLM's support for embeddings now accepts that different binary content may have different content-type - necessary for models like
Gemini Embedding 2
, which can embed text, audio, images, and video.
A lot of open source maintainers complain about a flood of AI-assisted PRs. LLM is my project that has been most affected by this and, to be honest, I'm not finding it to be a problem. That's mainly because I have Opus 5.5 or GPT-6 Astra help me with triage to spot the most useful fixes!
This release includes fixes from 12 authors - almost all AI-assisted - and the burden of reviewing them wasn't nearly as great as I expected. I really see them as bug reports with attached examples - sometimes I land them, sometimes I implement my own fix.
So thanks to
0d00ciallo0721
,
ac1982
,
Allen Flux
,
Bian Yuhan
,
Bishop Kammeraad
,
Chen Yufeiyang
,
Christopher Krah
,
Ethan Stoner
,
Jiachen Xie
,
Olamide Faniyan
,
Sharat Chandra Sai Boddu
,
nosmile99
for helping out with (or spending tokens on) this release!
