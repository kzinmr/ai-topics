---
title: "llm-tools-datasette 0.1.1"
url: "https://simonwillison.net/2026/Oct/18/llm-tools-datasette/"
fetched_at: 2026-10-19T10:06:24.491617+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# llm-tools-datasette 0.1.1

Source: https://simonwillison.net/2026/Oct/18/llm-tools-datasette/

When I switched LLM over to
httpx2
in
LLM 0.33
I forget that this would break any plugins which used
httpx
without directly depending on it.
llm-tools-datasette
was one of those plugins, now fixed.
