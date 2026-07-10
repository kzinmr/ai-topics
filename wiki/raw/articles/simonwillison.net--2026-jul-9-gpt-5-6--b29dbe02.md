---
title: "The new GPT-5.6 family: Luna, Terra, Sol"
url: "https://simonwillison.net/2026/Jul/9/gpt-5-6/#atom-everything"
fetched_at: 2026-07-10T07:01:41.537443+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# The new GPT-5.6 family: Luna, Terra, Sol

Source: https://simonwillison.net/2026/Jul/9/gpt-5-6/#atom-everything

The new GPT-5.6 family: Luna, Terra, Sol
9th July 2026
OpenAI’s latest flagship model
hit general availability this morning
, and comes in three sizes: Luna, Terra, and Sol (from smallest to largest).
The new models are priced per 1M input/output tokens as Luna $1/$6, Terra $2.50/$15, Sol $5/$30. For comparison, the Claude Opus series are $5/$25 and the Claude Fable 5 is $10/$50, but price-per-million tokens doesn’t tell us much now that the number of reasoning tokens can differ so much between models for the same task.
All three models have a February 16th 2026 knowledge cutoff, a million token context window, and 128,000 maximum output tokens.
OpenAI’s biggest benchmark claim concerns long-running agentic performance, with one benchmark showing all three models outperforming Claude Fable 5:
We trained GPT-5.6 to get more useful work from every token. On
Agents’ Last Exam
, an evaluation of long-running professional workflows across 55 fields, GPT-5.6 Sol sets a new high of 53.6, eclipsing Claude Fable 5 (adaptive reasoning) by 13.1 points. Even at medium reasoning, it beats Fable 5 by 11.4 points at roughly one-quarter the estimated cost. That efficiency extends to smaller models, which are essential to making intelligence more abundant and affordable: GPT-5.6 Terra and GPT-5.6 Luna outperform Fable 5 at around one-sixteenth the cost.
Amusingly, one self-reported benchmark that Fable 5 crushed the GPT-5.6 family on was SWE-Bench Pro, where Fable 5 got 80% compared to GPT-5.6 Sol getting 64.6%. This may help explain why OpenAI chose to publish
this article yesterday
specifically calling out SWE-Bench Pro for problems they found while auditing that benchmark:
In light of these results, we estimate that ~30% of SWE-bench Pro tasks are broken, and advise that model developers carefully examine results
I’ve had some early access to GPT-5.6 Sol—it’s definitely very competent, though so far it hasn’t struck me as better than Fable at the kind of complex coding tasks I’ve been using with Anthropic’s model.
As usual, the
model guidance for using GPT-5.6
has the most interesting details. There are a bunch of new API features that I need to explore (and probably add support for in
LLM
), including:
Programmatic Tool Calling
allows the models to “compose and run JavaScript that orchestrates tool calls”—which sounds to me like it could help bridge the gap between MCPs and full terminal sessions that can compose CLI utilities in useful ways. Also reminiscent of the
dynamic filtering
mechanism Anthropic added to their web search tool, which allows code execution against web results as part of a single model turn.
Multi-agent
lets the model “spin up subagents for parallel, focused work”—the sub-agent pattern now baked into the core API.
Prompt cache breakpoints
brings the Claude model of prompt caching to OpenAI, letting you be explicit about where the cache breakpoints are rather than relying on the API to detect them automatically. Personally I much prefer automatic detection (still supported by OpenAI), but presumably there are optimization cost savings to be had here if you put the work in.
You can now set
detail: original
on image requests to avoid resizing the image at all before it is processed.
Here’s
a full page with 18 different pelicans
—for reasoning efforts none, low, medium, high, xhigh, and max across the three different models. It also lists their token and calculated costs—the least expensive was gpt-5.6-luna at effort none for 0.71 cents, the most expensive was gpt-5.6-sol at max reasoning level for 48.55 cents.
In further pelican news, if you jump to 17:50 in
their livestream from this morning
you’ll see OpenAI’s own demo of 3D pelicans riding a tricycle, a bicycle, a pony, and another pelican!
