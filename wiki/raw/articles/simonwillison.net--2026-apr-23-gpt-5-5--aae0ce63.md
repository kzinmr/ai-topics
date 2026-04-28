---
title: "A pelican for GPT-5.5 via the semi-official Codex backdoor API"
url: "https://simonwillison.net/2026/Apr/23/gpt-5-5/#atom-everything"
fetched_at: 2026-04-28T07:01:58.936153+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# A pelican for GPT-5.5 via the semi-official Codex backdoor API

Source: https://simonwillison.net/2026/Apr/23/gpt-5-5/#atom-everything

A pelican for GPT-5.5 via the semi-official Codex backdoor API
23rd April 2026
GPT-5.5 is out
. It’s available in OpenAI Codex and is rolling out to paid ChatGPT subscribers. I’ve had some preview access and found it to be a fast, effective and highly capable model. As is usually the case these days, it’s hard to put into words what’s good about it—I ask it to build things and it builds exactly what I ask for!
There’s one notable omission from today’s release—the API:
API deployments require different safeguards and we are working closely with partners and customers on the safety and security requirements for serving it at scale. We’ll bring GPT‑5.5 and GPT‑5.5 Pro to the API very soon.
When I run my
pelican benchmark
I always prefer to use an API, to avoid hidden system prompts in ChatGPT or other agent harnesses from impacting the results.
The OpenClaw backdoor
One of the ongoing tension points in the AI world over the past few months has concerned how agent harnesses like OpenClaw and Pi interact with the APIs provided by the big providers.
Both OpenAI and Anthropic offer popular monthly subscriptions which provide access to their models at a significant discount to their raw API.
OpenClaw integrated directly with this mechanism, and was then
blocked from doing so
by Anthropic. This kicked off a whole thing. OpenAI—who recently hired OpenClaw creator Peter Steinberger—saw an opportunity for an easy karma win and announced that OpenClaw was welcome to continue integrating with OpenAI’s subscriptions via the same mechanism used by their (open source) Codex CLI tool.
Does this mean
anyone
can write code that integrates with OpenAI’s Codex-specific APIs to hook into those existing subscriptions?
The other day
Jeremy Howard asked
:
Anyone know whether OpenAI officially supports the use of the
/backend-api/codex/responses
endpoint that Pi and Opencode (IIUC) uses?
It turned out that on March 30th OpenAI’s Romain Huet
had tweeted
:
We want people to be able to use Codex, and their ChatGPT subscription, wherever they like! That means in the app, in the terminal, but also in JetBrains, Xcode, OpenCode, Pi, and now Claude Code.
That’s why Codex CLI and Codex app server are open source too! 🙂
And Peter Steinberger
replied to Jeremy
that:
OpenAI sub is officially supported.
llm-openai-via-codex
So... I had Claude Code reverse-engineer the
openai/codex
repo, figure out how authentication tokens were stored and build me
llm-openai-via-codex
, a new plugin for
LLM
which picks up your existing Codex subscription and uses it to run prompts!
(With hindsight I wish I’d used GPT-5.4 or the GPT-5.5 preview, it would have been funnier. I genuinely considered rewriting the project from scratch using Codex and GPT-5.5 for the sake of the joke, but decided not to spend any more time on this!)
Here’s how to use it:
Install Codex CLI, buy an OpenAI plan, login to Codex
Install LLM:
uv tool install llm
Install the new plugin:
llm install llm-openai-via-codex
Start prompting:
llm -m openai-codex/gpt-5.5 'Your prompt goes here'
All existing LLM features should also work—use
-a filepath.jpg/URL
to attach an image,
llm chat -m openai-codex/gpt-5.5
to start an ongoing chat,
llm logs
to view logged conversations and
llm --tool ...
to
try it out with tool support
.
And some pelicans
Let’s generate a pelican!
llm install llm-openai-via-codex
llm -m openai-codex/gpt-5.5
'
Generate an SVG of a pelican riding a bicycle
'
Here’s
what I got back
:
I’ve seen better
from GPT-5.4
, so I tagged on
-o reasoning_effort xhigh
and
tried again
:
That one took almost four minutes to generate, but I think it’s a much better effort.
If you compare the SVG code (
default
,
xhigh
) the
xhigh
one took a very different approach, which is much more CSS-heavy—as demonstrated by those gradients.
xhigh
used 9,322 reasoning tokens where the default used just 39.
A few more notes on GPT-5.5
One of the most notable things about GPT-5.5 is the pricing. Once it goes live in the API it’s
going to be priced
at
twice
the cost of GPT-5.4—$5 per 1M input tokens and $30 per 1M output tokens, where 5.4 is $2.5 and $15.
GPT-5.5 Pro will be even more: $30 per 1M input tokens and $180 per 1M output tokens.
GPT-5.4 will remain available. At half the price of 5.5 this feels like 5.4 is to 5.5 as Claude Sonnet is to Claude Opus.
Ethan Mollick has a
detailed review of GPT-5.5
where he put it (and GPT-5.5 Pro) through an array of interesting challenges. His verdict: the jagged frontier continues to hold, with GPT-5.5 excellent at some things and challenged by others in a way that remains difficult to predict.
