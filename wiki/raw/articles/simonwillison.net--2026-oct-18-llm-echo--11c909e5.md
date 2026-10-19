---
title: "Release: llm-echo 0.5"
url: "https://simonwillison.net/2026/Oct/18/llm-echo/"
fetched_at: 2026-10-19T10:06:24.495265+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Release: llm-echo 0.5

Source: https://simonwillison.net/2026/Oct/18/llm-echo/

I'm working towards a new
LLM
release, and testing PRs caused me to revisit the
llm-echo
debug plugin. This plugin provides a "model" which doesn't involve an LLM at all - it just repeats back the prompts that have been fed to it. The new release now updates the simulated token usage counts to take tool calls, system prompts, and reasoning tokens into account.
Example usage:
uvx --with llm-echo llm -m echo 'hi there' -o thinking 1 --usage
Outputs:
First I consider the prompt, then I decide what to say.
{
  "prompt": "hi there",
  "system": "",
  "attachments": [],
  "stream": true,
  "previous": []
}
Token usage: 2 input, 24 output
