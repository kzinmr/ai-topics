---
title: "What's new in Claude Sonnet 5"
url: "https://simonwillison.net/2026/Jun/30/claude-sonnet-5/#atom-everything"
fetched_at: 2026-07-01T07:00:52.698898+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# What's new in Claude Sonnet 5

Source: https://simonwillison.net/2026/Jun/30/claude-sonnet-5/#atom-everything

30th June 2026 - Link Blog
What's new in Claude Sonnet 5
(
via
) Claude Sonnet 5 came out
this morning
. I always head straight for the "what's new" developer docs because they tend to have more actionable information than the official announcement post.
Anthropic say of Sonnet 5 that "its performance is close to that of Opus 4.8, but at lower prices". The
system card
helps explain how they were able to release the model without being blocked by the US government:
Sonnet 5 is significantly less capable at cyber tasks than Mythos 5: its safeguards are thus similar to those we apply to Opus 4.7 and Opus 4.8 (models that are more capable than Sonnet 5 but much less capable than Mythos 5).
Of note from the "what's new" API changes:
Sampling parameters
temperature
,
top_p
,
top_k
are no longer supported.
It has a 1 million token context window and 128,000 maximum output tokens.
It features "the same set of tools and platform features as Claude Sonnet 4.6"
Adaptive thinking is on by default, unless you specify
"thinking": {type: "disabled"}
.
The pricing is the same as Sonnet 4.6: $3/million input, $15/million input, with an introductory discount to $2/$10 until 31st August. But...
The model has a new tokenizer, where "The same input text produces approximately 30% more tokens than on Claude Sonnet 4.6." - effectively a 30% price increase.
I used my
Claude Token Counter
tool to try out the new tokenizer. Here are my results for several larger documents:
Document
Sonnet 4.6
Opus 4.7
Sonnet 5
Universal Declaration of Human Rights (English)
2,356
3,347
1.42x
3,341
1.42x
Universal Declaration of Human Rights (Spanish)
3,572
4,753
1.33x
4,747
1.33x
Universal Declaration of Human Rights (Chinese, Mandarin Simplified)
3,334
3,366
1.01x
3,360
1.01x
sqlite_utils/db.py
(4,279 lines of Python)
44,014
56,118
1.28x
56,113
1.27x
So the new token is roughly 1.4x times more expensive for English, 1.33x for Spanish, 1.28x for Python code and effectively the same cost for Simplified Mandarin.
Here's
the pelican
. It's nothing to write home about. Sonnet 5 thinks it looks like a goose.
