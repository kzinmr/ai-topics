---
title: "The first known runaway AI agent"
url: "https://simonwillison.net/2026/Jul/23/the-first-known-runaway-ai-agent/#atom-everything"
fetched_at: 2026-07-24T10:13:55.826731+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# The first known runaway AI agent

Source: https://simonwillison.net/2026/Jul/23/the-first-known-runaway-ai-agent/#atom-everything

23rd July 2026 - Link Blog
The first known runaway AI agent - or a very bad marketing stunt?
(
via
) Martin Alderson's commentary on the
OpenAI accidental cyberattack against Hugging Face
includes a couple of details I hadn't considered.
First, Hugging Face offers a truly rich target if you're trying to find potential vulnerabilities that require executing arbitrary code:
Hugging Face has an
enormous
attack surface. They have more interfaces than I can count which run untrusted models and code. While they definitely have invested in defences, by nature of their operating model they do have many more opportunities to be attacked than many other services. I certainly don't envy their cybersecurity teams.
Secondly, one of the things that has puzzled me is how OpenAI didn't notice that their sandbox had been so thoroughly breached by the agent. Surely they'd be monitoring network traffic closely?
Martin points out that:
It's also likely they were running a huge amount of benchmarks simultaneously with ~unlimited token budgets - you want as many samples as possible to figure out how good a model is at a certain benchmark. It may also be they are testing various different checkpoints of the model too, understanding how the model is improving as it goes through the various training stages.
The mistakes made by the OpenAI team running this benchmark are easier to imagine when you think about the scale at which benchmarks of this kind usually operate. For all we know they could have been subjecting a new model to dozens of benchmarks at the same time, in dozens of different environments.
