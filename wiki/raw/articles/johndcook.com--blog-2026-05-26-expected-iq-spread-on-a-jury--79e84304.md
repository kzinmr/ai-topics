---
title: "Expected IQ spread on a jury"
url: "https://www.johndcook.com/blog/2026/05/26/expected-iq-spread-on-a-jury/"
fetched_at: 2026-05-27T07:00:54.567534+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Expected IQ spread on a jury

Source: https://www.johndcook.com/blog/2026/05/26/expected-iq-spread-on-a-jury/

There’s been some discussion online lately about how a large difference in IQ makes it difficult for two people to communicate. There have been studies that confirm this effect. The difficulty is not insurmountable, but it takes deliberate effort to overcome.
Someone dismissed this communication difficulty by pointing out that the expected difference in IQ between two individuals is around 17, suggesting that most communication is between people who differ by more than one standard deviation in IQ. But this calculation assumes people are chosen at random, which they usually are not. People tend to live around and work around others of similar intelligence.
However, a jury
is
a random sample. It’s not a perfect random sample. For one thing, it starts with a random sample of people who are registered to vote, or who have a drivers license, not all individuals. Furthermore, the pool of potential jurors is reduced to a jury through the process of
voir dire
, which is not random.
For this post I will make the simplifying assumption that a jury is a random sample from a population with normally distributed IQ with standard deviation σ = 15. The mean doesn’t matter here, but you could assume it’s 100 if you’d like.
By symmetry, the expected range of
n
samples from a normal random variable is twice the maximum. For
n
= 12 the range is about 3.26σ, which corresponds to nearly
50 IQ points
.
This suggests there’s usually a big spread of IQ on a jury. Even if IQ doesn’t measure intelligence, it measures
something
, and that something varies a lot over 12 people chosen at random [1].
Related posts
[1] In case you’re interested in the technical details, the expected range of
n
samples from a standard normal random variable is given by
where φ and Φ are the PDF and CDF of a standard normal. Multiply this by σ to get the range of a normal random variable with standard deviation σ. As for how to calculate
d
n
, see the
next post
.
