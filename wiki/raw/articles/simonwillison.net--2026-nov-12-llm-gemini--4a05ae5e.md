---
title: "Release: llm-gemini 0.37"
url: "https://simonwillison.net/2026/Nov/12/llm-gemini/"
fetched_at: 2026-11-13T10:01:08.294933+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Release: llm-gemini 0.37

Source: https://simonwillison.net/2026/Nov/12/llm-gemini/

Google launched
Gemini 4 Hydrogen
today - the lowest cost member of the Gemini 4 family.
It's actually not too far off the price of its much bigger siblings, Carbon and Argon. I'm finding Gemini 4's pricing
really
confusing. Here's the pricing scheme:
Model
Dates
Input ($/M)
Cached input
Output
Gemini 4 Carbon
Through Nov 30, 2026
$2.00
$0.10
$10.00
From Dec 1, 2026
$4.00
$0.20
$20.00
Gemini 4 Argon
Through Nov 30, 2026
$2.00
$0.10
$10.00
From Dec 1, 2026
$4.00
$0.20
$20.00
Gemini 4 Hydrogen
$1.50
$0.075
$7.50
Carbon and Argon are
the same price
, and both are scheduled to double in price on December 1st. If they're the same price, why have two different models?
Google says
that Argon "delivers Gemini 4 intelligence with faster responses and lower token spend per turn compared to Gemini 4 Carbon" - so it may be priced the same, but it will use less tokens per task.
Hydrogen, supposedly the cheap model, is currently only a 25% discount on its more capable peers. The Hydrogen price will make more sense after December 1st, when it will represent a 75% discount. It's still considerably more expensive than Claude Haiku 5.5 and GPT-6 Luna - they're both $0.10/$0.50, so Hydrogen is 15x that.
I had Hydrogen
generate some pelicans
. Here's a
full comparison grid
showing the pelicans for all three members of the Gemini 4 family at their three supported effort levels:
Considering how close they are in price, the difference in pelican quality for Hydrogen is quite stark.
Here's
how Google describe
Hydrogen's intended position in their mix of models:
In real-world software development, while teams rely on frontier models like Carbon and Argon for deep architectural judgment when designing systems or untangling subtle bugs, they still need a fast, disciplined execution model for writing code, running tests, and verifying changes. Hydrogen is built to stand on its own as a model for everyday work — or to pair with Carbon and Argon as the high-efficiency execution engine in multi-model workflows.
Most notably, Hydrogen is the new free tier model, and is the model that will power AI features in Google Search.
