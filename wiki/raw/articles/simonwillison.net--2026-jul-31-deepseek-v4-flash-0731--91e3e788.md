---
title: "deepseek-ai/DeepSeek-V4-Flash-0731"
url: "https://simonwillison.net/2026/Jul/31/deepseek-v4-flash-0731/#atom-everything"
fetched_at: 2026-08-01T10:13:00.757208+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# deepseek-ai/DeepSeek-V4-Flash-0731

Source: https://simonwillison.net/2026/Jul/31/deepseek-v4-flash-0731/#atom-everything

31st July 2026 - Link Blog
deepseek-ai/DeepSeek-V4-Flash-0731
(
via
) The latest release in DeepSeek's V4 family, "with substantially enhanced agentic capabilities". It's 304 billion parameters - 167GB on Hugging Face - but it appears to punch
well
above its weight.
Artificial Analysis
rank it
ahead of MiniMax M3 - a 428B model. It's $0.14/million input and $0.27/million output pricing means this may currently be the best value-per-intelligence model out there. It's looking very good on the
Intelligence Index vs. Cost per Intelligence Index Task
chart:
I got
a disappointing pelican
from it using the default reasoning level via OpenRouter:
But when I bumped reasoning level up to high I got
something much better
:
llm -m openrouter/deepseek/deepseek-v4-flash-0731 -t pelican -o reasoning_effort high
