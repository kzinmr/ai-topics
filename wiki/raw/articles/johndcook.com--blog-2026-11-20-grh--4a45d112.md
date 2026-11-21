---
title: "What is the Generalized Riemann Hypothesis?"
url: "https://www.johndcook.com/blog/2026/11/20/grh/"
fetched_at: 2026-11-21T10:01:10.822215+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# What is the Generalized Riemann Hypothesis?

Source: https://www.johndcook.com/blog/2026/11/20/grh/

There were two proofs of the Riemann Hypothesis (RH) announced today: one
AI-generated
and one
human-generated
.Both claimed to prove something more general, the Generalized Riemann Hypothesis (GRH) which of course includes RH as a special case.
The RH says that the all the zero of the Riemann zeta function ζ(
s
) in the critical strip, i.e. the region of the complex plane where
s
has real part between 0 and 1, occur on the central line Re(
s
) = ½.
There is a ladder of conjectures of that replace ζ(
s
) with ever more general families of functions, always with the same conclusion, that all the zeros in the critical strip lie on the central line.
The bottom rung of the latter is the Riemann Hypothesis with ζ(
s
). The next rung up is the Generalized Riemann Hypothesis for the class of functions
L
(
s
, χ). The higher rungs are more abstract than I care to get into.
The Riemann zeta function is defined to be analytic continuation of the function
The expression above is only valid for
s
with real part greater than 1, but the function can be uniquely extended to the entire complex plane, except for the point
s
= 1, by analytic continuation.
The functions
L
(
s
, χ) replace the numerator in the sum above with a function χ(
n
).
Again this function is defined by the series above where the series converges and extended by analytic continuation to the rest of the complex plane. The remaining work is to describe the class of functions the χ belong to. Importantly this class of functions includes the constant function χ(
n
) = 1, which corresponds to ζ(
s
).
The functions χ(
n
) are called Dirichlet characters of modulus
m
, for positive integer
m
, which means χ: ℤ → ℂ satisfies
χ(
ab
) = χ(
a
) χ(
b
)
χ(
a
) = 0 iff gcd(
a
,
m
) > 1
χ has period
m
.
For example, χ could be a
Legendre or Jacobi symbol
with
n
on top and
m
on bottom. For the Legendre symbol
m
must be an odd prime, and for the Jacobi symbol
m
is only required to be an odd number.
