---
title: "Release: pwasm 0.2a0"
url: "https://simonwillison.net/2026/Oct/1/pwasm/"
fetched_at: 2026-10-06T10:01:33.875032+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Release: pwasm 0.2a0

Source: https://simonwillison.net/2026/Oct/1/pwasm/

pwasm is one of my folly projects - an entirely vibe-coded pure Python WebAssembly engine that I built in January during my first bout of
AI mania
.
I hadn't touched it since January, so I decided to let Claude Opus 5.5 loose on it and see if it could make any significant improvements:
Evaluate current state of pwasm - then consider what it would take to get the MicroPython and micro JavaScript experiments from the
research repo
working under it - and what it would take to speed it up
42 commits later
(with minimal follow-up prompting) it now handles almost all of the WASM specification, and the wheel from PyPI bundles working WASM builds of
MicroPython
,
QuickJS
and
Micro QuickJS
.
I wouldn't trust this thing at all - hence the alpha version tag - but it's interesting seeing how today's models can improve on the work of models from 10 months ago.
