---
title: "Release: llm 0.31.1"
url: "https://simonwillison.net/2026/Jul/9/llm/#atom-everything"
fetched_at: 2026-07-10T07:01:41.528450+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Release: llm 0.31.1

Source: https://simonwillison.net/2026/Jul/9/llm/#atom-everything

Fix for a bug with OpenAI Chat Completion endpoints where a tool call with empty arguments could result in a JSON error from some providers.
#1521
This bug came up when I was testing
llm-meta-ai
.
