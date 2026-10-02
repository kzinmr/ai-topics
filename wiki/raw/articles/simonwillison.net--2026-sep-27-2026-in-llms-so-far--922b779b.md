---
title: "2026 in LLMs (so far)"
url: "https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/"
fetched_at: 2026-09-28T10:02:14.627522+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# 2026 in LLMs (so far)

Source: https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/

#
A few days later, on July 21st, OpenAI
confessed that it was them
.
OpenAI use a training technique called Reinforcement Learning from Verified Rewards—it’s the same technique used by everyone else now, and is the reason we have models that are so good at coding, and mathematics, and finding security holes.
While the model is being trained, you run exercises to see how good it is—and the strongest performers get their weights enforced for the next round. It’s like an evolutionary process that you run.
OpenAI had been running security exercises in a sandbox, and those agents had found holes in the sandbox itself, broken out, and were attacking Hugging Face to try to find ways to solve otherwise impossible problems.
(I’ve been collecting more about this on my
openai-hugging-face-incident
tag.)
Nine days later, Anthropic effectively said “our models can do this as well!”. They had looked through their own training logs and found evidence that their own agents had broken containment during training—and were responsible for the PyPI package we saw earlier,
among other things
.
So now we’ve got both Anthropic and OpenAI with rogue agents running around the internet doing things that they
should not
be doing.
