---
title: "llm-anthropic 0.27"
url: "https://simonwillison.net/2026/Aug/24/llm-anthropic/"
fetched_at: 2026-08-25T10:01:26.955620+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# llm-anthropic 0.27

Source: https://simonwillison.net/2026/Aug/24/llm-anthropic/

This release of the Anthropic plugin for
LLM
mainly provides compatibility with the recently released
anthropic v1.0.0
Python library, which switches from
httpx
to
httpx2
. OpenAI made the same change in their
v3.0.0 release
two weeks ago.
Anthropic provide this
migration guide
for upgrading to 1.0, so I prompted Fable 5 in Claude Code with:
Upgrade to anthropic>=1 - read https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/refs/heads/main/MIGRATION.md and get the tests passing
Here's
the resulting PR
.
