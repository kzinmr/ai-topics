---
title: "Introducing Muse Code and Muse Spark 1.2"
url: "https://simonwillison.net/2026/Aug/5/muse-code-and-muse-spark-12/#atom-everything"
fetched_at: 2026-08-06T10:18:23.870558+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Introducing Muse Code and Muse Spark 1.2

Source: https://simonwillison.net/2026/Aug/5/muse-code-and-muse-spark-12/#atom-everything

5th August 2026 - Link Blog
Introducing Muse Code and Muse Spark 1.2
(
via
) Yet more evidence that the most important characteristic of any model these days is long-sequence agentic tool calling. Meta shipped their own coding agent as part of getting that to work!
Muse Spark 1.2 is a coding-focused update to Muse Spark 1.1, with improvements in code generation, complex debugging, codebase understanding, and end-to-end developer workflows. In Muse Spark 1.2, we significantly scaled up training compute on coding tasks while expanding training environment diversity. The model also maintains its strength in other key areas like general agents. [...]
We co-trained Muse Spark 1.2 with Muse Code to ensure the model exhibits its best performance and coding usability when paired together. The training included rejection sampled harness trajectories and recipe optimizations for goals, compaction, and subagents, alongside the integration of the Muse Code toolset to maximize harness compatibility. [...]
Muse Spark 1.2 was extensively trained on long-horizon coding tasks, including whole-repository generation, large end-to-end projects, and auto-research.
Here's a pelican riding a bicycle SVG
produced by Muse Spark 1.2
:
You can see the
Spark 1.1 pelican from 9th July here
. I think the 1.2 pelican is a small but material improvement.
An interesting twist on pricing is that the model
is offered
as two different model IDs.
muse-spark-1.2
is priced at $1.25/million input and $4.25/million output - close to Gemini 3.6 Flash ($1.50/$7.50) - but if you agree to let Meta use your data "to improve our products" you can use
muse-spark-1.2-contributor
which is $0.10/$0.20 - a huge discount, closer to GPT-5.6 Luna ($0.20/$1.20) and Gemini 3.1 Flash-Lite ($0.25/$1.50).
I added those new prices
to llm-prices.com
.
