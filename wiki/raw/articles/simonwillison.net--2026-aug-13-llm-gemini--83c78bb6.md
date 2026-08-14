---
title: "Release: llm-gemini 0.33"
url: "https://simonwillison.net/2026/Aug/13/llm-gemini/"
fetched_at: 2026-08-14T10:21:52.150312+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Release: llm-gemini 0.33

Source: https://simonwillison.net/2026/Aug/13/llm-gemini/

It's been a while since the last
llm-gemini
release. This version of the plugin adds support for today's
Gemini 3.7 Flash
release, plus
gemini-3.6-flash
,
gemini-3.5-flash-lite
and two embedding models
gemini-embedding-2
and
gemini-embedding-001
.
The plugin is also upgraded for compatibility with LLM 0.32, which means you can now see reasoning traces and you can also enable server-side tools using this pattern:
llm -m gemini-3.7-flash -T CodeExecution \
  'use python to calculate (factorial of 13) * 3'
I had Gemini 3.7 Flash
draw me some pelicans riding bicycles
at high, medium, and low thinking efforts (minimal, which was an option in 3.6 Flash, has been removed in 3.7.) Here's the high level one, which is pretty great:
One catch though: the pelican I showed here was rendered with Safari. Both Firefox and Chrome render it differently, due to Safari being more tolerant of empty SVG
<filter>
elements than those other two browsers.
They still display the bicycle, but the pelican is missing entirely!
