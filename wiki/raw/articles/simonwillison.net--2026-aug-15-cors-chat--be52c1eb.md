---
title: "Tool: CORS Chat"
url: "https://simonwillison.net/2026/Aug/15/cors-chat/"
fetched_at: 2026-08-16T10:14:41.146451+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Tool: CORS Chat

Source: https://simonwillison.net/2026/Aug/15/cors-chat/

I built this today (
with GPT-5.6-Sol xhigh
) to help test Qwen 3.8 27B running in LM Studio on both my M5 MacBook Pro and an NVIDIA DGX Spark.
It provides a web UI for exercising an OpenAI-Responses-compatible chat endpoint. I've tried it against LM Studio with the
--cors
option and OpenRouter, and both work fine.
Conversations are persisted in the browser and can be exported as copy-pasted JSON. One fun detail is that it notices SVG images that are being generated and progressively renders them in the chat while the tokens are still streaming in.
