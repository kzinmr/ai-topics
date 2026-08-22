---
title: "Release: llm 0.32.1"
url: "https://simonwillison.net/2026/Aug/21/llm/"
fetched_at: 2026-08-22T10:01:32.702021+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Release: llm 0.32.1

Source: https://simonwillison.net/2026/Aug/21/llm/

Fresh installs of LLM stopped working the other day because the OpenAI Python library dropped its usage of
httpx
, and it turned out LLM depended on that library but only installed it via a transitive
openai
dependency.
This dot-release fixes that for the moment by pinning to
openai<3
, and a soon-to-drop 0.33 release will switch from
httpx
to
httpx2
.
