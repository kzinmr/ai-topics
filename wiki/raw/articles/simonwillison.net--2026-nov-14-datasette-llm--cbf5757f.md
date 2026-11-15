---
title: "datasette-llm 0.1a11"
url: "https://simonwillison.net/2026/Nov/14/datasette-llm/"
fetched_at: 2026-11-15T10:00:55.700811+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# datasette-llm 0.1a11

Source: https://simonwillison.net/2026/Nov/14/datasette-llm/

datasette-llm
is the intermediate plugin for Datasette that supports configuring LLMs for use with other Datasette plugins.
This release adds support for OpenAI-compatible endpoints, so you can configure Datasette to use an LLM hosted anywhere that talks the OpenAI pseudo-standard web protocol.
This means that if you're running local models with
LM Studio
or
Ollama
or
llama.cpp
(which just hit
v1.0.0
) you can run Datasette via
uvx
like this:
wget https://datasette.io/content.db

uvx --with datasette-agent datasette \
  --root --secret 1 \
  -s plugins.datasette-llm.default_model
'
{
"model": "lmstudio-qwen",
"model_name": "qwen/qwen3.8-27b",
"api_base": "http://localhost:1234/v1"
}
'
content.db
And you'll get a local server running a Datasette Agent instance powered by your local model!
