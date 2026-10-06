---
title: "llm-anthropic 0.30"
url: "https://simonwillison.net/2026/Sep/28/llm-anthropic/"
fetched_at: 2026-10-06T10:01:33.868711+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# llm-anthropic 0.30

Source: https://simonwillison.net/2026/Sep/28/llm-anthropic/

In addition to Claude Sonnet 5.5, this release adds the ability to run
llm anthropic refresh
to refresh the list of Anthropic models directly from their API - which means I don't need to push a new release just to add support for a newly released model.
I also added an
llm anthropic count
command which can use their free token counting API to return a count of tokens that will be used by any prompt, before you send that prompt.
