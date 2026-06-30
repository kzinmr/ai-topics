---
title: "Self-Scaffolding LLMs for Agentic Coding"
url: "https://simonwillison.net/2026/Jun/29/ornith/#atom-everything"
fetched_at: 2026-06-30T07:01:00.395100+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Self-Scaffolding LLMs for Agentic Coding

Source: https://simonwillison.net/2026/Jun/29/ornith/#atom-everything

29th June 2026 - Link Blog
Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding
. This is an interesting new open weights (MIT licensed) model, the first model release from DeepReinforce.
[...] with variants including 9B Dense, 31B Dense, 35B MoE, and 397B MoE. Built on top of pretrained Gemma 4 and Qwen 3.5, it achieves state-of-the-art performance among open-source models of comparable size on coding benchmarks.
As far as I can tell the licenses of those underlying models is compatible with being used in this way - Gemma 4 is Apache 2.0 licensed (and not bound by the janky additional
Gemma Terms of Use
that afflicted the previous Gemma models) and Qwen 3.5 is Apache 2.0 licensed as well.
I've been running the model using LM Studio and the
ornith-1.0-35b-Q4_K_M.gguf
(20GB) GGUF, hooked up to
Pi
. Initial impressions are very good - it seems to be able to run the agent harness over many tool calls in a proficient way.
Here's
a terminal session
where I asked it to "find the code that decodes the actor cookie" and then "find the code that opens the insert dialog when thebutton is clicked" against a Datasette checkout, which it handled with ease.
I also had it
draw this pelican
, which came out at 103 tokens/second:
It's a little bit mangled but the pelican is clearly a pelican.
I couldn't find much information about DeepReinforce themselves. The earliest paper I could find from the was
CUDA-L1: Improving CUDA Optimization via Contrastive Reinforcement Learning
from June 2025.
