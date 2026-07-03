---
title: "Using DSPy to evaluate and improve Datasette Agent's SQL system prompts"
url: "https://simonwillison.net/2026/Jul/2/dspy-datasette-agent-prompts/#atom-everything"
fetched_at: 2026-07-03T07:00:57.291493+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Using DSPy to evaluate and improve Datasette Agent's SQL system prompts

Source: https://simonwillison.net/2026/Jul/2/dspy-datasette-agent-prompts/#atom-everything

One of this morning's AIE keynotes covered
dspy
, which reminded me I've been meaning to see if it could help me improve the system prompt used by
Datasette Agent
- so I fired off an asynchronous research task in Claude Code for web using Claude Fable 5:
Pip install the latest Datasette alpha and datasette-agent and dspy - then figure out how to use dspy to evaluate and improve the main system prompts used by Datasette Agent for the feature where it can execute read only SQL queries to answer user questions about data.
Fable chose to test using GPT 4.1 mini and nano, and identified several promising looking directions for improvements. I particularly like this one:
The schema listing gives only table names; the "don't call describe_table if you already have the information" advice caused column-name guessing (page_count, o.order_id, first_name) and error-retry loops in baseline traces. Either include column names in the prompt's schema listing or soften that advice.
