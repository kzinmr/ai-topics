---
title: "Las Vegas, Monte Carlo, and Integer Factorization"
url: "https://www.johndcook.com/blog/2026/11/26/las-vegas-monte-carlo/"
fetched_at: 2026-11-27T10:00:54.835612+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Las Vegas, Monte Carlo, and Integer Factorization

Source: https://www.johndcook.com/blog/2026/11/26/las-vegas-monte-carlo/

Monte Carlo algorithms typically have a fixed runtime but a variable error rate.
Las Vegas algorithms have a variable runtime but a fixed (i.e. zero) error rate.
Stanisław Ulam came up with the idea of Monte Carlo methods in 1946 and Nicholas Metropolis coined the term “Monte Carlo” the next year.
László Babai coined the term “Las Vegas algorithm” in 1979 as a pun on Monte Carlo.
Las Vegas factoring algorithm in the news
There’s a new paper on
GitHub
titled Unconditional Integer Factorization in Time
L
N
[1/3,
O
(1)]. It is a Las Vegas algorithm because it always [1] returns a correct factorization, though the time it takes to execute is random.
What is unconditional about the new algorithm? The analysis of the new algorithm does not depend on any unproven assumptions. Before there was a proof of the (
Generalized
) Riemann Hypothesis, many theorems were conditional because they assumed the GRH. The fastest integer factorization algorithms are not dependent on GRH but are dependent on other widely believed but unproven conjectures.
The notation
L
N
[α,
c
], commonly used in computational number theory, stands for
exp(
c
(log
N
)
α
(log log
N
)
1−α
)
The fastest commonly used factorization method at this time is the
GNFS
(general number field sieve). Its runtime is
L
N
[1/3, (64/9)
1/3
+
o
(1)] ≈
L
N
[1/3, 1.923]
This means that the
c
term is (64/9)
1/3
= 1.923 plus a term that goes to zero as
N
increases.
For the new algorithm, the α term is the same as GNFS but the
c
term is something less than 105. This is a bound on the worst-case expected time. The runtime is not as good as GNFS but the runtime proof does not depend on any unproven assumptions. The best unconditional algorithm before this recent result was
L
N
[1/2, 1].
[1] Las Vegas algorithms halt with probability 1. In practice they terminate, but strictly speaking they are partial functions, functions that give a correct result when they terminate.
