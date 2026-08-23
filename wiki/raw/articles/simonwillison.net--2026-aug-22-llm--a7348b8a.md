---
title: "Release: llm 0.33"
url: "https://simonwillison.net/2026/Aug/22/llm/"
fetched_at: 2026-08-23T10:01:40.412323+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Release: llm 0.33

Source: https://simonwillison.net/2026/Aug/22/llm/

My highlights from this release:
Upgraded to the OpenAI Python library 3.x and switched the HTTP client dependency from
httpx
to
httpx2
.
#1608
,
#1631
I shipped a quick
0.32.1 fix
for this yesterday, but this is the more comprehensive fix.
llm embed
and
llm embed-multi
now accept
--key
. The Python
EmbeddingModel.embed()
,
EmbeddingModel.embed_multi()
,
Collection.embed()
and
Collection.embed_multi()
methods accept
key=
too, passing the resolved per-call key to embedding plugins without changing shared model state. Existing plugins that read
self.key
continue to work through a compatibility fallback. Thanks,
ChrisJr404
.
#757
,
#1620
The embedding models now use the same pattern for keys that regular LLM models do.
llm prompt -t/--template
can now be repeated to combine templates in order. This allows model configuration and options from one template to be used with a prompt from another.
This unlocks a neat pattern where you can create templates that package a model with a set of default options:
llm -m gpt-5.6-luna -o reasoning_effort high --save lhigh
llm "Generate an SVG of a pelican riding a bicycle" --save pelican
# Combine and run the templates
llm -t lhigh -t pelican
This is particularly useful for exercising different models that provide their own imitation of the OpenAI Responses API.
