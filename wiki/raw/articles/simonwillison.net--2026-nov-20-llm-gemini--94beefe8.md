---
title: "llm-gemini 0.38.1"
url: "https://simonwillison.net/2026/Nov/20/llm-gemini/"
fetched_at: 2026-11-22T10:01:11.298521+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# llm-gemini 0.38.1

Source: https://simonwillison.net/2026/Nov/20/llm-gemini/

Gemini 4 Carbon only supports
low
,
medium
and
high
reasoning levels - but Gemini 4 Hydrogen and Gemini 4 Neon both have an extra
xhigh
level.
I missed that when I added those models to the
llm-gemini
plugin, which is now fixed in this dot release.
The
xhigh
setting for Hydrogen makes a
significant
difference. I updated my
Gemini 4 comparison grid
- note how Hydrogen at high used 5,311 output tokens and cost 3.99 cents, but the same model at xhigh used 31,477 output tokens, cost 23.61 cents, and produced a pelican that's competitive with Gemini 4 Neon:
