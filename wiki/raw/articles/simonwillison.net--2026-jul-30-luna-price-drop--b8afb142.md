---
title: "Advancing the price-performance frontier with GPT‑5.6"
url: "https://simonwillison.net/2026/Jul/30/luna-price-drop/#atom-everything"
fetched_at: 2026-07-31T10:24:10.099366+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Advancing the price-performance frontier with GPT‑5.6

Source: https://simonwillison.net/2026/Jul/30/luna-price-drop/#atom-everything

30th July 2026 - Link Blog
Advancing the price-performance frontier with GPT‑5.6
(
via
) Huge price drop from OpenAI today: GPT-5.6 Terra got a 20% reduction, and GPT-5.6 Luna got a massive 80% drop.
OpenAI credit 5.6 Sol with enabling this: in
How GPT‑5.6 fuses frontier intelligence with frontier efficiency
they describe using 5.6 Sol to optimize load balancing, and more impressively to optimize inference itself:
We also used GPT‑5.6 Sol to optimize the model’s forward pass: the computation that transforms inputs into next-token predictions. Even when individual operations are fast, excess memory movement, synchronization, and inefficient data layouts can leave GPUs idle. To avoid this, GPT‑5.6 Sol found work that could be precomputed, avoided, or parallelized. With Codex, GPT‑5.6 Sol autonomously rewrote and optimized our production kernels, the core code that executes the mathematical operations that make up the model. This worked in part because we’ve trained GPT‑5.6 to be effective at writing and improving kernels in
Triton⁠
and
Gluon⁠
, two open-source GPU programming languages maintained by OpenAI. These efforts, combined with broader kernel advancements from GPT‑5.6 Sol, reduced end-to-end serving costs by 20%.
That Luna price drop completely changes the landscape with respect to lower priced models. At $0.20/million tokens for input and $1.20/million for output Luna is now cheaper than Google's Gemini 3.1 Flash-Lite ($.025/$1.50).
Anthropic's cheapest current model is Claude Haiku 4.5, and that's $1/$5 - Luna is now 1/5th of that for input, previously it cost the same.
My
agent.datasette.io
demo site was running on Gemini 3.1 Flash-Lite. I've switched it over to Luna.
