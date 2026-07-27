---
title: "exp_q(x) keeps every qth term in the power series for exp(x)"
url: "https://www.johndcook.com/blog/2026/07/26/exp-q/"
fetched_at: 2026-07-27T10:17:11.982272+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# exp_q(x) keeps every qth term in the power series for exp(x)

Source: https://www.johndcook.com/blog/2026/07/26/exp-q/

The function exp
q
(
x
) is defined by taking the power series for exp(
x
) and keeping only the terms whose index is a multiple of
q
. For example, exp
2
(
x
) keeps only the even-numbered terms in the exponential power series and so equals cosh(
x
).
In general,
The first sum uses
Iverson’s bracket notation
: a Boolean expression in brackets denotes the function that returns 1 when the expression is true and zero when it is false. Here the bracket equals 1 when
q
divides
n
and is zero otherwise.
Closed forms
Let ω = exp(2π
i
/
q
). Then
This lets us find closed-form expressions for exp
q
(
x
). For example, when
q
= 4, ω =
i
and
Here’s a proof of the identity above:
In the proof we used the identity
which is important in deriving the properties of the discrete Fourier transform.
Differential equations
The first time I saw the function exp
q
(
x
) was in differential equations, though I didn’t know at the time the function had a name.
When a course in differential equations gets to power series solutions, a common example or homework problem is to solve
for
k
= 3 or 4, i.e. to find a function that equals its third or fourth derivative.
If the initial conditions are
and
the unique solution to
is
y
(
x
) = exp
k
(
x
).
Mathematica and Mittag-Leffler
Mathematica does not have a built-in function implementing exp
q
(
x
), but it does have an implementation of the
Mittag-Leffler function
, and so thanks to a relation between this function and exp
q
(
x
) you can implement the latter as
expq[x_, q_] := MittagLefflerE[q, x^q]
Combinatorics
The first time I saw the
notation
exp
q
(
x
) was in combinatorics. I had intended to include an application from that book here, but I make that the topic for the
next post
.
