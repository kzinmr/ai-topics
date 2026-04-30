---
title: "GPT-5.5 prompting guide"
url: "https://simonwillison.net/2026/Apr/25/gpt-5-5-prompting-guide/#atom-everything"
fetched_at: 2026-04-30T07:01:11.810732+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# GPT-5.5 prompting guide

Source: https://simonwillison.net/2026/Apr/25/gpt-5-5-prompting-guide/#atom-everything

25th April 2026 - Link Blog
GPT-5.5 prompting guide
. Now that GPT-5.5 is
available in the API
, OpenAI have released a wealth of useful tips on how best to prompt the new model.
Here's a neat trick they recommend for applications that might spend considerable time thinking before returning a user-visible response:
Before any tool calls for a multi-step task, send a short user-visible update that acknowledges the request and states the first step. Keep it to one or two sentences.
I've already noticed their Codex app doing this, and it does make longer running tasks feel less like the model has crashed.
OpenAI suggest running the following in Codex to upgrade your existing code using advice embedded in their
openai-docs
skill:
$openai-docs migrate this project to gpt-5.5
The upgrade guide the coding agent will follow
is this one
, which even includes light instructions on how to rewrite prompts to better fit the model.
Also relevant is the
Using GPT-5.5 guide
, which opens with this warning:
To get the most out of GPT-5.5, treat it as a new model family to tune for, not a drop-in replacement for
gpt-5.2
or
gpt-5.4
. Begin migration with a fresh baseline instead of carrying over every instruction from an older prompt stack. Start with the smallest prompt that preserves the product contract, then tune reasoning effort, verbosity, tool descriptions, and output format against representative examples.
Interesting to see OpenAI recommend starting from scratch rather than trusting that existing prompts optimized for previous models will continue to work effectively with GPT-5.5.
