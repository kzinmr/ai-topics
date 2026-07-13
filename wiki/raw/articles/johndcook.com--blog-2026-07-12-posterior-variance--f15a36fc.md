---
title: "Posterior variance"
url: "https://www.johndcook.com/blog/2026/07/12/posterior-variance/"
fetched_at: 2026-07-13T07:01:30.815014+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Posterior variance

Source: https://www.johndcook.com/blog/2026/07/12/posterior-variance/

A few days ago I wrote a post entitled
Does additional data always reduce posterior variance?
. In a nutshell, the answer is no, not always.
That led the
previous post
which looked at posterior means for three Bayesian models, showing how the posterior mean is a weighted average of the prior mean and the mean of the new data. The weights are
precisions
, which means something different for each model.
For the beta-binomial model, variance may increase when seeing unexpected data (details
here
), but precision always increases.
For the normal-normal model precision is the reciprocal of variance. Every new data point makes precision go up and posterior variance go down.
The Poisson-gamma model may be the most interesting. As stated in the previous post, if data has a Poisson distribution with parameter λ, and λ has a gamma(α
0
, β
0
) prior distribution, then the posterior distribution on λ after observing
k
events over time
t
has a gamma(α
0
+
k
, β
0
+
t
) posterior distribution. Therefore the posterior variance is
(α
0
+
k
) / (β
0
+
t
)².
Note the posterior variance is an increasing function of
k
and a decreasing function of
t
. This means that the posterior variance increases
every time
an event is observed, and it decreases quadratically between observations.
Here’s an illustration. I simulated data from a Poisson process with λ and used a gamma(1, 1) prior on λ. Here’s a plot of the posterior variance.
