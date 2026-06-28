---
title: "Height of harmonic numbers"
url: "https://www.johndcook.com/blog/2026/06/27/height-of-harmonic-numbers/"
fetched_at: 2026-06-28T07:01:23.653633+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Height of harmonic numbers

Source: https://www.johndcook.com/blog/2026/06/27/height-of-harmonic-numbers/

The
previous post
looked at writing the harmonic numbers as reduced fractions and estimating the number of digits in the numerator and denominator based on asymptotics. This is a follow up post with plots.
We’ll choose our base
b
to be 2. And we’ll look at the total number of bits in both the numerator and denominator, which we will use as the
height
of the fractions.
First, let’s look at the actual and estimated heights, using the estimates from the previous post.
Next let’s look at the difference between the actual and estimated heights.
In the previous post I looked at
n
= 50, which was kind of a lucky choice, the error being smaller than usual. I had also looked at, but didn’t publish,
n
= 100, which would be an unlucky choice.
Finally, let’s look at the
relative
error in the estimates, and plot over a larger range of
n
.
The error goes to zero, as predicted by the asymptotic estimates. And it goes noisily, which you’d expect since the heights are related to the distribution of primes.
