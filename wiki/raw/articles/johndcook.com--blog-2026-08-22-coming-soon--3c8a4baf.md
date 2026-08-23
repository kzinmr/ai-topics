---
title: "Coming soon"
url: "https://www.johndcook.com/blog/2026/08/22/coming-soon/"
fetched_at: 2026-08-23T10:01:40.654314+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Coming soon

Source: https://www.johndcook.com/blog/2026/08/22/coming-soon/

There’s a pizza shop near my home with a sign out front that says “Coming Soon.” When I drove by it this morning I thought about how you would model the time until an event happens that is “coming soon.”
Suppose I look at the sign one day and guess how many days until the pizza shop will open. When I drive by a week later and guess again, should my guess be smaller? You might argue that the shop will open some day, fixed in time but unknown to me, and so every day I’m one day closer to the eventual opening.
You might model the pizza shop opening like radioactive decay and say that the estimated number of days until it opens is always the same until the day it actually opens.
Now I think this shop has been “coming soon” for over a year. So instead of decreasing, every day I increase my estimate of the time until the shop opens. Something has gone wrong that the owners didn’t expect when they put up the sign.
Maybe the reasonable thing would be for estimated days until opening to decrease over time, but only up to a point. After some point, the longer a business has been “coming soon” the less like that it is coming soon, or coming at all.
This brings up an interesting point about modeling. There are two probability distributions at work: the probability that the shop will eventually open, and the time until opening assuming it eventually opens.
When the sign first goes up saying the business is coming soon, there’s some change that it is in fact not coming. Maybe you’re optimistic and think this probability is small, but it would seem unreasonable to think the probability is zero. That means the
expected
number of days until opening is always infinite. If there’s a probability ε that the shop never opens, the expected time to opening is
ε × ∞ + (1 − ε) × something = ∞.
