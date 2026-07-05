---
title: "Does additional data always reduce posterior variance?"
url: "https://www.johndcook.com/blog/2026/07/03/does-additional-data-always-reduce-posterior-variance/"
fetched_at: 2026-07-04T07:01:39.812125+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Does additional data always reduce posterior variance?

Source: https://www.johndcook.com/blog/2026/07/03/does-additional-data-always-reduce-posterior-variance/

A discussion over lunch today brought up the fact that additional data does not always decrease the size of a confidence interval. This post will look at this from a Bayesian perspective.
In general, new information reduces your uncertainty regarding whatever you’re estimating. The posterior distribution becomes more concentrated as more data are collected.
That’s what happens “in general” but does it necessarily happen every time you get new data? Conceivably if you get surprising data, data that is very unlikely given your current prior, posterior uncertainty might increase.
To show that this is the case, suppose the probability of success in some binary trial has parameter θ and that θ has a beta prior. You could imagine this prior to be the posterior after having made some number of previous observations. Can a new observation increase the posterior variance in θ? If so, under what conditions?
The variance of a beta(
a
,
b
) random variable is
ab
/ (
a
+
b
)²(
a
+
b
+ 1).
After observing a successful trial, the posterior distribution on θ is beta(
a
+ 1,
b
). We can calculate the ratio of the posterior variance to the prior variance and ask under what circumstances, if any, the ratio is greater than 1.
If 2
a
≥
b
the posterior variance will be strictly less than the prior variance. This says if the posterior odds against a success are no more than 2 : 1, observing a success will reduce the variance. (So will observing a failure.) But for any value of
b
, you can find a small enough value of
a
that observing a success will increase the variance.
