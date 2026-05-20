---
title: "Gemini 3.5 Flash: more expensive, but Google plan to use it for everything"
url: "https://simonwillison.net/2026/May/19/gemini-35-flash/#atom-everything"
fetched_at: 2026-05-20T07:00:49.121346+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Gemini 3.5 Flash: more expensive, but Google plan to use it for everything

Source: https://simonwillison.net/2026/May/19/gemini-35-flash/#atom-everything

Gemini 3.5 Flash: more expensive, but Google plan to use it for everything
19th May 2026
Today at Google I/O, Google
released Gemini 3.5 Flash
. This one skipped the
-preview
modifier and went straight to general availability, and Google appear to be using it for a whole lot of their key products:
3.5 Flash is available today to billions of people globally:
For everyone via the Gemini app and AI Mode in
Google Search
For developers in our agent-first development platform Google Antigravity and Gemini API in Google AI Studio and Android Studio
For enterprises in Gemini Enterprise Agent Platform and Gemini Enterprise.
As usual with Gemini, the most interesting details are tucked away in the
What’s new in Gemini 3.5 Flash
developer documentation. It mostly has the same set of platform features as the previous Gemini 3.x series, albeit with no
computer use
. The model ID is
gemini-3.5-flash
. The knowledge cut-off is January 2025, and it supports 1,048,576 input tokens and 65,536 maximum output tokens.
Google are also pushing a new
Interactions API
, currently in beta, which looks to me like their version of the patterns introduced by
OpenAI Responses
—in particular server-side history management.
The price has gone up
Gemini 3.5 Flash is accompanied by a notable price bump. The previous models in the “Flash” family were
Gemini 3 Flash Preview
and
Gemini 3.1 Flash-Lite
. The new 3.5 Flash is 3x the price of 3 Flash Preview and 6x the price of 3.1 Flash-Lite (see
price comparison here
).
At $1.50/million input and $9/million output it’s getting close in price to Google’s Gemini 3.1 Pro, which is $2 and $12.
The Gemini team promise that 3.5 Pro will roll out “next month”—presumably at an even higher price.
This fits a trend: OpenAI’s GPT-5.5 was 2x the price of GPT-5.4, and Claude Opus 4.7 is around 1.46x the price of 4.6 when you take the
new tokenizer into account
.
Given the price increase it’s interesting to see Google roll it out for so many of their own free-to-consumer products. It feels like all three of the major AI labs are starting to probe the price tolerance of their API customers.
Artificial Analysis publish the cost to run their proprietary benchmark against models, which is a useful way to take things like tokenization and increased volume of reasoning tokens into account. Some numbers worth comparing:
Running the benchmark for 3.5 Flash (high) cost significantly more than 3.1 Pro Preview!
Here are some numbers from other vendors:
A pelican on a bicycle
I ran “Generate an SVG of a pelican riding a bicycle”
against the Gemini API
and got back this pelican, which is a
lot
:
From the code comments:
<!-- Pelican Eye / Sunglasses (Cool Retro Aviators) -->
hedgehog on Hacker News
:
That pelican looks like it’s in Miami for a crypto conference.
That one cost me 11 input tokens and 14,403 output tokens, for a total cost of
just under 13 cents
.
