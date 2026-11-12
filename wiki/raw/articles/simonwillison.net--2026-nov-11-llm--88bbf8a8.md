---
title: "Release: llm 0.37.2"
url: "https://simonwillison.net/2026/Nov/11/llm/"
fetched_at: 2026-11-12T10:01:09.673068+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Release: llm 0.37.2

Source: https://simonwillison.net/2026/Nov/11/llm/

Fixes a security issue reported by
Daniel de Araujo
in
GHSA-v9h7-jj4g-f862
and
GHSA-r639-rr7r-x72w
.
LLM has a mechanism called
extra-openai-models.yaml
- now managed by the new-in-0.37
llm openai endpoint add
command - for using LLM with OpenAI-compatible API endpoints from other providers.
Daniel reported two ways this could accidentally send your configured OpenAI API key to one of those providers: if the key named by
api_key_name
had never been stored, or if a
responses: true
model was run with
-o chat_completions 1
.
