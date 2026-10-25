---
title: "Introducing Kimi K3.1 Pro"
author: "Simon Willison"
url: "https://simonwillison.net/2026/Oct/23/kimi-k31-pro/"
domain: "simonwillison.net"
source: "x-accounts-scan (@simonw, tweet 2113718487529267593)"
scraped: 2026-10-25
type: raw-article
---

# Introducing Kimi K3.1 Pro

> Link post by Simon Willison, 23rd October 2026.
> Original: https://simonwillison.net/2026/Oct/23/kimi-k31-pro/
> Announced via X: "More notes on Kimi K3.1 - this one is a big deal, first time an open weights
> (well, soon-to-be open weights) model has competed this credibly with the current frontier"

Kimi K3.1 Pro landed on the Kimi API today - it's not yet open weights, but Moonshot promise
"Full model weights will be released by Nov 4, 2026".

They're also offering a "Highspeed" version that's 2-3x faster, at twice the price (except for
input token cache hits, which are priced the same).

The US dollar pricing is $2.00/million tokens for input and $10/million for output - the same as
GPT-6.1 Sol and half the price of Claude Opus 5.5.

Moonshot's own benchmarks show Kimi as approximately level with Opus 5.5 and GPT-6 Astra - beating
them on a few benchmarks, coming close on others.

Artificial Analysis scored Kimi at 55 - ahead of Claude Fable 5.1, GPT-6 Astra, and Gemini 4 Argon
(all at 53) and behind only Claude Opus 5.5 (58).

**This is the first time a (soon-to-be) open weight model has scored this highly against the
frontier.**

I tried it out via the Moonshot API using the `llm openai endpoint` command I added to LLM 0.32
back in August:

```
llm openai endpoint \
  https://api.moonshot.ai/v1 \
  --key kimi \
  -m kimi-k3.1-pro \
  "Generate an SVG of a pelican riding a bicycle" \
  --responses \
  -o reasoning_effort low \
  > kimi-k3.1-pro-pelican-low.stdout.txt \
  2> kimi-k3.1-pro-pelican-low.stderr.txt
```

`llm openai endpoint` can run prompts against any OpenAI-compatible endpoint but doesn't log the
results, hence the extra options to save stdout and stderr (the reasoning trace).

Here are the pelicans I got for Kimi K3.1 Pro on the three reasoning levels it supports - low,
medium and max. This is max:

[SVG image]

For comparison, I ran fresh pelicans against Kimi K3 on those three reasoning levels.

---

Tags (Simon's blog): ai, generative-ai, llms, llm, llm-pricing, pelican-riding-a-bicycle,
llm-release, ai-in-china, moonshot, kimi
