---
title: "GPT-6.1 Terra"
url: "https://simonwillison.net/2026/Oct/26/gpt-61-terra/"
fetched_at: 2026-10-27T10:01:03.525513+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# GPT-6.1 Terra

Source: https://simonwillison.net/2026/Oct/26/gpt-61-terra/

GPT-6.1 Terra
(
via
) It's always interesting to note which aspects of a new model are emphasized in the release announcement.
In the case of GPT-6.1 Terra, OpenAI went with visual reasoning and computer use:
We’re introducing
GPT-6.1 Terra
, a fast, efficient model that combines detailed visual reasoning and precise computer use alongside clearer, more natural writing. A significant step up from GPT‑5.6 Terra, it excels at the communication and computer-based tasks that fill the workday, from drafting proposals and interpreting technical drawings to filling out forms and editing videos.
Terra sits in the same position as Sonnet in the Anthropic model collection - not the cheapest or the most expensive, making it harder to decide when to use it.
Computer use is a good example of a task that benefits from a less expensive model, since you might put it to work on automated, repetitive tasks.
OpenAI's Ted Sanders provided some useful advice in
a comment
on Hacker News:
In the case of GPT-6.1 Terra, I'd say Terra is probably better than Astra and Sol at technical communication, similar on vision and computer use (but much faster!), and a bit worse on most other things. For API developers, it's a nice midrange option if you want something cheaper than Sol but a lot smarter than Luna (especially for vision / computer use / communication). For subscribers, it's not a bombshell release - if you're hitting usage limits, maybe it helps you go a bit further, and if you want clearer communication or faster computer use, it can be a nice option to select.
Here are
the pelicans
for the different reasoning levels. This pelican
for "max"
cost
11.3161 cents
and took 4 minutes and 11 seconds:
Here's
a new comparison grid
showing pelicans for every reasoning level of OpenAI's current frontier lineup: GPT-6 Astra, GPT-6.1 Sol, GPT-6.1 Terra, and GPT-6 Luna.
GPT-6.1 Terra is priced at $1/million input tokens and $5/million output - almost half the price of GPT-5.6 Terra and GPT-6.1 Sol, and around 10x the price of GPT-6 Luna.
