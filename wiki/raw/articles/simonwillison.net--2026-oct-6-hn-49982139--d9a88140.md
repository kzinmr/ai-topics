---
title: "Comment: Mistral Large 4"
url: "https://simonwillison.net/2026/Oct/6/hn-49982139/"
fetched_at: 2026-10-07T10:01:26.866535+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Comment: Mistral Large 4

Source: https://simonwillison.net/2026/Oct/6/hn-49982139/

wren6991
: The benchmark is saturated. Frontier models are tested with an armadillo in fishnet tights jaywalking on Mars.
OK well I couldn't resist this one:
llm -m claude-opus-5.5 'Generate an SVG of an armadillo in fishnet tights jaywalking on Mars'
llm -m gpt-6.1-sol 'Generate an SVG of an armadillo in fishnet tights jaywalking on Mars'
llm -m gemini-3.8-flash 'Generate an SVG of an armadillo in fishnet tights jaywalking on Mars'
llm -m mistral/mistral-large-4 'Generate an SVG of an armadillo in fishnet tights jaywalking on Mars'
Default reasoning levels for each:
https://tools.simonwillison.net/markdown-svg-renderer?url=ht...
