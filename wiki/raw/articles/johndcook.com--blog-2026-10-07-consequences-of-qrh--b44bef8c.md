---
title: "Consequences of progress toward the Riemann Hypothesis"
url: "https://www.johndcook.com/blog/2026/10/07/consequences-of-qrh/"
fetched_at: 2026-10-08T10:01:34.430293+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Consequences of progress toward the Riemann Hypothesis

Source: https://www.johndcook.com/blog/2026/10/07/consequences-of-qrh/

The Riemann Hypothesis (RH) is the conjecture that all the zeros of the Riemann zeta function ζ(
s
) in the critical strip, i.e. the region of the complex plane with real part between 0 and 1, have real part equal to ½.
The Quasi Riemann Hypothesis (QRH) says that there exists a constant θ < 1 such that no zeros of ζ(
s
) have real part greater than θ.
OpenAI
has published a paper claiming QRH with θ = 7/8.
The RH is so important to number theory that even partial results can have big consequences. This post will focus on one consequence: the error term in the Prime Number Theorem.
The Prime Number Theorem says that π(
x
), the number of primes less than
x
, is asymptotically equal to Li(
x
). We’d like to know more specifically at what rate π(
x
) approaches Li(
x
).
The best known result before the QRH announcement was
If the QRH holds for some θ, such as OpenAI’s assertion that θ = 7/8,
If RH holds, θ = ½.
Incidentally, you may have seen the Prime Number Theorem stated with
x
/log(
x
) rather than Li(
x
). These two functions are asymptotically equal, so they give the same theorem, if you’re not interested in quantifying the rate of convergence. The function Li(
x
) gives better error bounds.
