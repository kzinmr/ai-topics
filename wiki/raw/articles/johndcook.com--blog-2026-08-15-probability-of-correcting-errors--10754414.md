---
title: "Probability of correcting errors"
url: "https://www.johndcook.com/blog/2026/08/15/probability-of-correcting-errors/"
fetched_at: 2026-08-16T10:14:41.359939+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Probability of correcting errors

Source: https://www.johndcook.com/blog/2026/08/15/probability-of-correcting-errors/

Error correcting codes are most simply described in terms of the errors they can certainly correct. For example, the Hadamard code used for the
Mariner 9
probe to Mars encoded each 6-bit pixel to a 32-bit codeword in such a way that the original pixel could be recovered if no more than 7 bits were corrupted in transit.
What is the
probability
that a pixel could be repaired if corrupted? That depends on your probability model. We will assume that the probability of each bit being flipped is
p
and that errors are independent.
(Are errors independent, i.e. if a bit flips, is the next bit more or less likely to flip? That would depend on context.)
It’s straight-forward to calculate the probability that 7 or fewer or fewer bits out of 32 flip; this is the cumulative distribution of a binomial random variable. The following Python code will return the probability of
k
or fewer successes out of
n
trials, each with probability of success
p
:
from scipy.stats import binom
    print(binom.cdf(k, n, p))
For example, if there is a 10% chance that each bit will flip, there’s a 98.8% chance that 7 or fewer bits out of 32 will flip.
However this only gives a
lower bound
on the probability of correcting an error. If eight bits flip in transit, we cannot tell with certainty which codeword was sent, but that doesn’t mean all possibilities are equally likely. Here things get messier. For the Hadamard code mentioned above, there’s a 50-50 chance of being able to recover a pixel transmitted with 8 flipped bits in the corresponding code word. The probability of correct recovery gets smaller with more corruption, but it doesn’t go to zero.
Now suppose you’re given a desired error recovery rate and have to determine what value of
p
it can sustain. For example, someone might say they want a 98.8% chance of recovering a pixel correctly, and you could come back and say
p
must be less than or equal to 0.1. This would be a conservative answer because as discussed above,
p
= 0.1 gives a pixel recovery probability of something more than 98.8, though it’s messy to calculate how much more.
You could solve for
p
by trial and error, or you could use some more sophisticated math to compute
p
directly. Given a probability
F
, you can solve for
p
such that the probability of up to
k
successes out of
n
trials using the inverse of the regularized incomplete beta function.
from scipy.special import betaincinv
p = 1 - betaincinv(n - k, k + 1, F)
Calculating
F
given
n
,
k
, and
p
could be a homework exercise in an introductory probability course. Solving for
p
given
F
,
n
, and
k
either requires some numerical programming or special functions and so would be a more challenging problem.
Related posts
