---
title: "Release: llm 0.34"
url: "https://simonwillison.net/2026/Sep/2/llm/"
fetched_at: 2026-09-08T10:01:09.984255+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Release: llm 0.34

Source: https://simonwillison.net/2026/Sep/2/llm/

One new feature:
llm logs --usage
Markdown output now includes the response duration in milliseconds and as a human-readable duration.
llm logs --short
includes a new
duration_ms
field.
#1653
Plus several contributed bug fixes, and a significant performance improvement to
llm logs
thanks to
waveplate
on GitHub, see also
llm-openrouter 0.7.1
.
