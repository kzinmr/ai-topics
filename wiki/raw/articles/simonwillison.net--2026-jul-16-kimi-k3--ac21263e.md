---
title: "Kimi K3, and what we can still learn from the pelican benchmark"
url: "https://simonwillison.net/2026/Jul/16/kimi-k3/#atom-everything"
fetched_at: 2026-07-17T07:00:57.739732+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Kimi K3, and what we can still learn from the pelican benchmark

Source: https://simonwillison.net/2026/Jul/16/kimi-k3/#atom-everything

Kimi K3, and what we can still learn from the pelican benchmark
16th July 2026
Chinese AI lab Moonshot AI
announced Kimi K3
this morning, describing it as their “most capable model to date, with 2.8 trillion parameters”. It’s currently available via their website and API, but an open weight release is promised “by July 27, 2026”.
Moonshot are calling this the first “open 3T-class model” (I guess they’re rounding 2.8 trillion up to 3 trillion), taking the crown from
DeepSeek’s 1.6T v4 Pro
. Their
self-reported benchmarks
have K3 mostly beating Claude Opus 4.8 max and GPT-5.5 high, while losing out to Claude Fable 5 and GPT-5.6 Sol.
A few highlights from the
Artificial Analysis report
on the model:
“On our private long-horizon knowledge work evaluation, Kimi K3 reaches an overall Elo of 1547, +732 points from Kimi K2.6 and behind only Claude Fable 5.”
“Cost per task ($0.94) is similar to GPT-5.6 Sol ($1.04), ~1/2 the price of Opus 4.8 ($1.80) and higher than open weights peers”
“Kimi K3’s token usage on the Artificial Analysis Intelligence Index decreased significantly, using 21% fewer output tokens than K2.6.”
The model is also now the
leading model on Arena.ai’s Frontend Code arena
, surpassing even Claude Fable 5.
The new model is notable for the pricing: $3/million input tokens and $15/million output tokens, putting it at the same level as Anthropic’s Claude Sonnet series and making it the most expensive model released by a Chinese AI lab to date. This is a significant increase on their earlier models
such as Kimi K2.6
at $0.95/$4. 2.8 trillion parameters is also more than twice the size of that 1T model.
But how does it pelican?
I used OpenRouter (to avoid signing up for a Moonshot API key) with the
llm-openrouter plugin
to generate an SVG of a pelican riding a bicycle:
llm -m openrouter/moonshotai/kimi-k3 'Generate an SVG of a pelican riding a bicycle'
Here’s
the transcript
. It looks like this:
That pelican took 95 input tokens and 16,658 output tokens (13,241 were reasoning tokens), for a total cost of
25 cents
!
Since K3 accepts image input I ran it against that rendered SVG above (with my
alt text prompt
) and
got back
(for
0.6 cents
):
Cartoon illustration of a white pelican wearing a red scarf, riding a red bicycle along a gray road with white dashed lines; the pelican has a large orange beak and webbed orange feet pedaling, with white motion lines behind it; the background shows a light blue sky with white clouds, a yellow sun, two small black birds in flight, and green grass with tiny white flowers in the foreground
What can we learn from the pelican?
My
Generate an SVG of a pelican riding a bicycle
test is 21 months old now. It was never a particularly great benchmark. It started out as a joke on how absurdly difficult it is to compare these models, but then for the first year it turned out to have a
surprising correlation
to how good the models actually were.
That connection has been mostly severed now. The
GPT-5.6
and
Claude Fable 5
pelicans are outclassed
by GLM-5.2
, and much as I love GLM I don’t think that’s a Fable-class model.
(I’m still not convinced that labs are
training for the benchmark
—if they were, I’d expect much better results. There’s a chance that Gemini has optimized for
any combination of an animal on a vehicle
though!)
The biggest limitation of the pelican is that it doesn’t touch at all on the thing that matters most for today’s model: agentic tool calling and the ability to operate tools reliably as conversations grow in length.
So don’t go using pelicans to compare models!
All of that said, I still get a decent amount of value out of running the benchmark myself.
Firstly, it’s a forcing function for actually trying the model. If I show you a pelican, that means I’ve managed to run a prompt through it. If the model has an official API I’ll use that, if it’s open weight (and small enough to fit a 128GB M5 MacBook Pro) I’ll try running it on my own machine, usually via
llama.cpp
or
LM Studio
or
Ollama
. I’ll frequently use
OpenRouter
since that usually provides a proxy to an official API without me needing a new API key.
Most of my pelicans are generated using
my LLM CLI tool
, which helps encourage me to ensure the latest models are supported by that (via one of its plugins).
More importantly though, even the act of a single prompt to “Generate an SVG of a pelican riding a bicycle” can reveal interesting model characteristics.
Consider
the result
for Kimi K3 today. Running those simple prompts helped emphasize several points about the model.
It only has one reasoning effort right now, “max”—and it shows. The model consumed 13,241 reasoning tokens to output 3,417 tokens of response. This is expensive—the pelican cost 25 cents!
How does the prompt “Generate an SVG of a pelican riding a bicycle” add up to 95 input tokens?  OpenAI’s
tokenizer
counts 10,
Anthropic’s
counts 10 for Opus 4.6, 30 for Opus 4.7 and 25 for Sonnet 5/Fable 5. Prompting “hi”
to Kimi K3
counted 86 tokens, suggesting there may be an 85 token hidden system prompt. It
refused to leak it
though.
Vision works well: the alt text it generated is very good.
K3 currently only has one thinking effort level, but I’ve been deriving quite a bit of value recently from running the same pelican prompt through different effort levels to get a quick idea for what impact those have. Here’s my matrix
for the GPT-5.6 model family
, for example.
Really though the main things I gain from the pelican test are:
It’s a “hello world” exercise for prompting a model
A rough cost and reasoning estimate for a simple task
Confirmation that the model can output valid SVG and has a basic idea of geometry and spatial awareness. This is a much bigger deal for the smaller models that run on my laptop.
It’s still interesting to compare pelicans between releases in the same model family. K3’s pelican is a notable improvement from
Kimi 2.5
.
It’s something I can share that demonstrates I’ve tried it. Plus a comment with a pelican in it is kind of a tradition on Hacker News at this point, any time I’m late I get comments asking where it is!
