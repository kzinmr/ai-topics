---
title: "Claude Haiku 5.5"
url: "https://simonwillison.net/2026/Oct/7/claude-haiku-5-5/"
fetched_at: 2026-10-08T10:01:34.372037+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Claude Haiku 5.5

Source: https://simonwillison.net/2026/Oct/7/claude-haiku-5-5/

Claude Haiku 5.5
7th October 2026
As previously
promised
, here’s Anthropic’s new fast, low cost model:
Introducing Claude Haiku 5.5
.
The previous Haiku, 4.5, was very much showing its age. It came out
almost a year ago
, and was priced at $1/million input and $5/million output—relatively expensive even back then, and a full 10x the price of OpenAI’s
GPT-6 Luna
, released last month.
The new Haiku exactly matches the price of GPT-6 Luna—$0.10/$0.50—up to 100,000 tokens. Beyond 100,000 tokens the price increases 5x to $0.50/$2.50. Luna itself has a price increase at 272,000 tokens but only to $0.20/$0.75.
Haiku 5.5 also uses a new, less generous tokenizer. My
Claude Token Counter
tool shows that the same long prompt uses around 1.25x as many tokens with Haiku 5.5 compared to Haiku 4.5, so there’s a hidden price increase there.
If your workloads fit in 100,000 tokens, Haiku is the same price as Luna and reports higher benchmark scores. Above 100,000 tokens, Luna looks like a much better deal.
The
most recent release of llm-anthropic
finally fixed it so I don’t need to ship a new version of that plugin for every new model. I tested the new model like this:
llm install -U llm-anthropic
llm anthropic refresh
llm -m claude-haiku-5.5 "Generate an SVG of a pelican riding a bicycle" -o thinking_effort low
Pelicans
Here are
pelicans for low, medium, high, xhigh, and max
. The new Haiku doesn’t let you disable reasoning, and defaults to
medium
. I got a good bicycle frame for everything beyond
low
. The
low effort pelican
cost 0.0936 cents and took 7 seconds.
This
max
effort pelican (with
a reasoning trace
that starts “This is the classic pelican-on-bicycle SVG test...”) took 5 minutes 9 seconds to generate, but still only cost me
3.3826 cents
:
(Since the reasoning trace exhibits awareness of the benchmark, here’s
Generate an SVG of an armadillo in fishnet tights jaywalking on Mars (on xhigh)
, and the same prompt against
some other recent models
.
Background on that
.)
For comparison, here’s the pelican I got
a year ago
from Haiku 4.5 (for
0.7583 cents
—Haiku 4.5 did not support reasoning levels). It
sucked
at drawing pelicans:
And a generous API credit scheme for subscribers
In addition to Haiku 5.5, Anthropic announced today that they are halving the price of cache reads for Sonnet 5.5. They’ve also added API credits to subscription plans:
Second, this week, we’ll roll out
a new monthly API credit to all Max and Team subscribers for use on the Claude Platform
. Max 5x users will get $100 in credits per month, Max 20x users will get $200, and Team subscribers will receive up to $500, pooled across their users.
Claiming this is pleasantly easy: navigate to
Settings -> Billing
and select the API organization that should benefit from the credits every month:
The API credits exactly match the cost of the subscription itself. This is really generous—it makes it much easier for subscribers to use the API. Anthropic also let you disable auto-reload for the API, with the consequence that “API requests will stop when your balance runs out”—exactly what you want if you’re planning to burn through those API credits without
risk of a nasty billing surprise
.
Note that the monthly credits
do not roll over
—use them or lose them.
OpenAI still allow you to use your Codex subscription for personal API use, which works out as a better deal for heavy API users. This new credit scheme goes at least some way to overcoming that difference.
