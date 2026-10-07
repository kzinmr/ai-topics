---
title: "llm-openai-decisions 0.1a0"
url: "https://simonwillison.net/2026/Oct/6/llm-openai-decisions/"
fetched_at: 2026-10-07T10:01:26.808400+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# llm-openai-decisions 0.1a0

Source: https://simonwillison.net/2026/Oct/6/llm-openai-decisions/

OpenAI released their new Jev-style
Decisions API
, as previously announced at last week's DevDay.
Since I already have an
llm-typesafe
plugin for talking to Jev, I had GPT-6 Astra read the new OpenAI API documentation and build an
llm-openai-decisions
plugin inspired by
llm-typesafe
.
Unlike Jev, the new
gpt-6-luna
decision model supports image input in addition to text. Both models charge for input it and not for output: OpenAI's is 10 cents per million input tokens, Jev's is 4.2 cents per million.
Otherwise the API shape is
very
similar to Jev, at least conceptually. Jev
supports three question types
for yes/no, choices, or scores. OpenAI Decisions supports the same three types.
Install the plugin like this:
llm install llm-openai-decisions
Here's an example query against an image attachment:
llm -m openai-decisions/gpt-6-luna \
  -a https://static.simonwillison.net/static/2025/two-pelicans.jpg \
  -s
'
Does this image contain any mammals?
'
And example output:
{
"type"
:
"
predicate
"
,
"name"
:
"
evaluation
"
,
"probability"
:
0.0
}
Consult
the README
for full details of how to run the other types of questions.
