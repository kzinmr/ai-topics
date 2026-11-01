---
title: "datasette-llm 0.1a9"
url: "https://simonwillison.net/2026/Oct/31/datasette-llm/"
fetched_at: 2026-11-01T10:01:32.481443+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# datasette-llm 0.1a9

Source: https://simonwillison.net/2026/Oct/31/datasette-llm/

I have some big upgrades to
Datasette Agent
in the pipeline, but in the meantime here's a tiny user experience improvement to the underlying
datasette-llm
plugin.
It now picks up the default model used by
LLM
, which means you can start using Datasette Agent without needing to explicitly configure a default model:
uvx --with datasette-agent datasette content.db --internal internal.db
Previously you would also need to specify a model with
-s plugins.datasette-agent.default_model gpt-6-astra
.
