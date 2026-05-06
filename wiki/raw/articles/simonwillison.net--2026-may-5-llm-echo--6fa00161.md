---
title: "Release: llm-echo 0.5a0"
url: "https://simonwillison.net/2026/May/5/llm-echo/#atom-everything"
fetched_at: 2026-05-06T07:01:08.673136+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Release: llm-echo 0.5a0

Source: https://simonwillison.net/2026/May/5/llm-echo/#atom-everything

New
-o thinking 1
option to help test against
LLM 0.32a0
and higher.
This plugin provides a fake model called "echo" for LLM which doesn't run an LLM at all - it's useful for writing automated tests. You can now do this:
uvx --with llm==0.32a1 --with llm-echo==0.5a0 llm -m echo hi -o thinking 1
This will fake a reasoning block to standard error before returning JSON echoing the prompt.
