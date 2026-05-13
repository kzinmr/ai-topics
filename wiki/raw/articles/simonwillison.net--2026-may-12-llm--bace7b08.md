---
title: "Release: llm 0.32a2"
url: "https://simonwillison.net/2026/May/12/llm/#atom-everything"
fetched_at: 2026-05-13T07:01:24.172454+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Release: llm 0.32a2

Source: https://simonwillison.net/2026/May/12/llm/#atom-everything

A bunch of useful stuff in this
LLM
alpha, but the most important detail is this one:
Most reasoning-capable OpenAI models now use the
/v1/responses
endpoint instead of
/v1/chat/completions
. This enables interleaved reasoning across tool calls for GPT-5 class models.
#1435
This means you can now see the summarized reasoning tokens when you run prompts against an OpenAI model, displayed in a different color to standard error. Use the
-R
or
--hide-reasoning
flags if you don't want to see that.
