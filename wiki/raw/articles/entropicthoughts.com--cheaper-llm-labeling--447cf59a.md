---
title: "Cheaper LLM labelling"
url: "https://entropicthoughts.com/cheaper-llm-labeling"
fetched_at: 2026-09-23T10:01:03.431899+00:00
source: "entropicthoughts.com"
tags: [blog, raw]
---

# Cheaper LLM labelling

Source: https://entropicthoughts.com/cheaper-llm-labeling

As written, this runs like a black box, so we’ll likely want to add a routine
that regularly prints statistics about what’s going as the script is working.
When we do, we’ll find that it performs well. Some of the diagnostic output I
added assigns predictions into ten evenly spaced buckets, and prints the error
for each, i.e. the difference in average assigned probability and actual average
probability for each bucket.
5
This loses us some more training data,
unfortunately, because we don’t want to evaluate the final predicted result on
either regression’s training data!
0.05: -0.02
0.15: 0.03
0.25: 0.10
0.35: 0.04
0.45: 0.04
0.55: 0.01
0.65: 0.01
0.75: -0.08
0.85: 0.00
0.95: 0.02
This tells us e.g. that the predictions in the range 20 % to 30 % are on average
10 percentage points too high, meaning the corresponding events happen slightly
less often than predicted. On the other hand, the opposite is true for
predictions in 0 % to 10 % range, which are on average 2 percentage points too
low, i.e. the corresponding events happen a teensy bit more often than
predicted. However, all of these numbers are within the margin of error that
would be expected for however many samples these calibration numbers were drawn
from, meaning there’s no significant deviation from calibration.
6
Had I been
less lazy I would have made the diagnostic print also show the p-value or
something, for each bucket alone, and the combination of them.
The fast classifier is used for roughly 46 % of the classification tasks in my
case, so it roughly doubles the speed at which classification runs. Not amazing,
but it was fun building it anyway. This is definitely a technique to keep in the
back pocket for when there’s something that’s easier to classify, or when the
expensive classifier is more expensive. It could easily speed up (and cheapen)
the process by an order of magnitude or more.
