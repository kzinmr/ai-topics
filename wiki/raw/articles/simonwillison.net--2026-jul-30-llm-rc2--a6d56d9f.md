---
title: "Release: llm 0.32rc2"
url: "https://simonwillison.net/2026/Jul/30/llm-rc2/#atom-everything"
fetched_at: 2026-07-31T10:24:10.101011+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Release: llm 0.32rc2

Source: https://simonwillison.net/2026/Jul/30/llm-rc2/#atom-everything

Hot on the heels of
RC1
, this fixes a dependency issue and also adds two neat new features:
The default model for users who have not set their own default is now
GPT-5.6 Luna
. It was previously
GPT-4o mini
. Luna is a much better and more recent model, albeit slightly more expensive - $0.20 per million input tokens and $1.20 per million output tokens, compared to $0.15/$0.60 for 4o mini. You can switch back to 4o mini using
llm models default gpt-4o-mini
, or switch to
GPT-5 nano
, an even cheaper default model ($0.05/$0.40), using
llm models default gpt-5-nano
.
#1576
New
llm openai endpoint
command for running prompts, chats and model listings against arbitrary OpenAI-compatible endpoints without first configuring a model. These calls are not logged.
#1565
The
llm openai endpoint
command is
really
cool. I got frustrated at the lack of an obvious CLI tool for trying out prompts against arbitrary OpenAI Chat Completions imitation endpoints, so I decided to add that to LLM itself.
You don't even have to install LLM to use this. Here's a
uvx
one-liner for running a prompt - with tools - against an
LM Studio
local model:
uvx --pre llm openai endpoint http://127.0.0.1:1234/v1 \
  T llm_version -T llm_time --td \
  -m google/gemma-4-31b 'what is the current LLM version? And the time?'
Output here
.
