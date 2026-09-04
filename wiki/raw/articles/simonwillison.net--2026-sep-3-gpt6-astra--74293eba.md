---
title: "GPT‑6 Astra"
url: "https://simonwillison.net/2026/Sep/3/gpt6-astra/"
fetched_at: 2026-09-04T10:00:43.845988+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# GPT‑6 Astra

Source: https://simonwillison.net/2026/Sep/3/gpt6-astra/

GPT‑6 Astra
(
via
) GPT-6 Astra is "rolling out today to a limited set of organizations and over the coming days will become available to all ChatGPT Plus, Pro, Business, and Enterprise users, as well as through the OpenAI API and AWS" - I've not tried it yet myself, so I don't have a great deal to say about it yet.
It's going to be API priced at the same rate as Claude Fable 5 and 5.1: $10/million input and $50/million output. This is clearly OpenAI's Fable competitor, and appears to score higher than Fable on most of OpenAI's self-reported benchmarks.
Most impressively, Astra scores 99.9% on the recent (released in March)
ARC-AGI 3 benchmark
- though notably Fable 5 does not yet have a published result, and the
ARC-AGI blog notes
that the 99.9% score was achieved for $19K using OpenAI's custom "Provider Adapter harness", while the default ARC-AGI harness scored 62.7% for $26K.
The Provider Adapter harness preserves opaque reasoning state between requests and uses compaction for longer conversations, allowing the model to reuse prior work.
Unsurprisingly, given
the recent Hugging Face incident
, Astra is a beast at security tasks. It scores 100% on ExploitBench (GPT-5.6 Sol got 78.5%), 42.4% on ExploitGym (Sol got 30.3%), and 99.2% within four attempts on SRE-Bench binary reverse engineering compared to Sol's 68.7%.
It's also better at long context: on OpenAI's eight-needle benchmark it got 100% at 256K–512K tokens and 96.3% at 512K–1M tokens. OpenAI may have vanquished one of the ongoing challenges with long context processing.
It doesn't win at everything though.
Artificial Analysis
note that Astra is still beaten by Fable on their Intelligence Index:
Sits beside GPT-5.6 Sol in Intelligence
: GPT-6 Astra scores equal to GPT-5.6 Sol in the Index at 61. This is 5 points lower than Claude Fable 5.1 (max with fallback). The model also trails Meta’s newly released Muse Spark 1.3 (max).
It did better on their Coding Agent Index:
Leads Coding Agent Index cost efficiency frontier
: At max effort, GPT-6 Astra costs about the same as GPT-5.6 Sol (max) while scoring 2 points higher on the Index. Per task, the model is less than half the cost of Claude Fable 5, for the same score.
I'll write more about Astra once I get access to it. The API model label once it rolls out will be
gpt-6-astra
.
