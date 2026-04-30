---
title: "Andrica's conjecture on the gap between root primes"
url: "https://www.johndcook.com/blog/2026/04/08/andrica/"
fetched_at: 2026-04-30T07:02:00.631820+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Andrica's conjecture on the gap between root primes

Source: https://www.johndcook.com/blog/2026/04/08/andrica/

I recently found out about Andrica’s conjecture: the square roots of consecutive primes are less than 1 apart.
In symbols, Andrica’s conjecture says that if
p
n
and
p
n
+1
are consecutive prime numbers, then
√
p
n
+1
− √
p
n
< 1.
This has been empirically verified for primes up to 2 × 10
19
.
If the conjecture is true, it puts an upper bound on how long you’d have to search to find the next prime:
p
n
+1
< 1 + 2√
p
n
+
p
n
,
which would be an improvement on the Bertrand-Chebyshev theorem that says
p
n
+1
< 2
p
n
.
