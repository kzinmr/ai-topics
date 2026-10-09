---
title: "Release: ttok 1.0"
url: "https://simonwillison.net/2026/Oct/9/ttok/"
fetched_at: 2026-10-09T10:01:07.920703+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Release: ttok 1.0

Source: https://simonwillison.net/2026/Oct/9/ttok/

I released
ttok 0.4
, ran
uv tool upgrade ttok
, piped a file into the new version... and realized that it was defaulting to the GPT-4 tokenizer when it should very clearly default to GPT-5/GPT-6 instead!
I figured switching the default was a reasonable excuse to finally ship a 1.0.
OpenAI haven't actually confirmed that GPT-6 uses the same tokenizer as the GPT-5 family yet - there's an
angry issue about it
- but I found
this commit
by William Liu which reports on an experiment he ran confirming that the tokenizers are likely the same:
All seven GPT models (5.5, 5.6 Sol/Terra/Luna, 6 Astra/Sol/Luna) report 44,794 tokens and match each other on every one of the 31 fixtures. GPT-6 introduces no input-count change on this corpus.
