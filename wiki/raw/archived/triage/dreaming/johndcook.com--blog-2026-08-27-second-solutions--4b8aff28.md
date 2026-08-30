---
title: "Second solutions"
url: "https://www.johndcook.com/blog/2026/08/27/second-solutions/"
fetched_at: 2026-08-28T10:01:35.362827+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Second solutions

Source: https://www.johndcook.com/blog/2026/08/27/second-solutions/

This post provides a couple examples to go along with two
earlier
posts
.
The pattern we’re illustrating is families of polynomials
p
n
(
x
) that each satisfy a differential equation and a three-term recurrence. The differential equations have a second solution
q
n
(
x
) that is the larger solution with respect to
x
but the smaller solution with respect to
n
.
In both the examples below
p
n
(
x
) is a polynomial, and so bounded on the interval [−1, 1], and
q
n
(
x
) is not a polynomial, with singularities at ±1. This is analogous to the previous examples with Bessel functions
J
n
(
x
) and
Q
n
(
x
) that satisfy the same differential equation but have contrasting behavior with respect to
x
versus
n
.
Legendre polynomials
The differential equation
has two solutions for each
n
,
P
n
(
x
) and
Q
n
(
x
).
The solutions
P
n
(
x
) are the Legendre polynomials. The solutions
Q
n
(
x
) are not polynomials but involve a term log((1 +
x
)/(1 −
x
)) that blows up at 1 and −1. But for fixed
x
and increasing
n
,
P
n
(
x
) grows exponentially and
Q
n
(
x
) decays exponentially, provided |
x
| > 1.
Chebyshev polynomials
The differential equation
has two solutions for each
n
,
T
n
(
x
) and
V
n
(
x
).
The solutions
T
n
(
x
) are the Chebyshev polynomials. The solutions
V
n
(
x
) are not polynomials but involve a term √(
x
² — 1) that become vertical up at 1 and −1. But for fixed
x
with |
x
| > 1 and increasing
n
,
T
n
(
x
) grows exponentially and
V
n
(
x
) decays exponentially.
