---
title: "The Laplace limit"
url: "https://www.johndcook.com/blog/2026/06/07/the-laplace-limit/"
fetched_at: 2026-06-08T07:01:15.474006+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# The Laplace limit

Source: https://www.johndcook.com/blog/2026/06/07/the-laplace-limit/

An
earlier post
discussed how to solve Kepler’s equation
M
=
E
−
e
sin(
E
)
using a sine series. You could also solve Kepler’s equation using a power series, which Lagrange did in 1771. Both approaches express
E
as a function of
e
and
M
, but from different perspectives. Bessel thought of his solution as a sum of sines in
M
, with coefficients that depend on
e
. Lagrange thought of his solution as a power series in
e
whose coefficients involve sines in
M
. You can rearrange the terms of either solution into the other.
The most interesting thing about the power series solution, in my opinion, is that it only converges for
e
less than roughly 2/3 while the sine series solution is valid for all
e
< 1. In astronomical terms, this means the power series solution works for the orbit of some planets but not others!
In our solar system, the planets all have eccentricity well below 2/3, but not all minor planets do. For example, the orbit of Eris has eccentricity 0.4407 but the orbit of Sedna has eccentricity 0.8549. And in other solar systems there are planets with eccentricity much greater than 2/3.
The Laplace limit
The radius of convergence for Lagrange’s power series solution is called the Laplace limit. Its value is
e
L
= 0.6627…. There’s no obvious reason why there’s anything special about this value. There’s no astronomical reason for this value. It’s an artifact of the power series form of the solution.
If the series works for
e
= 0.66, you would reasonably think it works for
e
= 0.67, but that’s not the case. And if you’re observant, you might notice that although the series works for
e
= 0.66, it takes longer to converge than for smaller values of
e
; the rate of convergence is slowing down, warning you of danger ahead.
The exact value of
e
L
is the unique real solution to the equation
There’s no obvious reason for this either. It has to do with finding the largest circle that can fit in a lens-shaped region of convergence. More on that
here
.
We can calculate
e
L
with the following Python code.
from math import exp
from scipy.optimize import root_scalar

def f(x):
    t = (1 + x*x)**0.5
    return x*math.exp(t) - 1 - t

sol = root_scalar(f, bracket=[0, 1], method='brentq')
print(sol.root)
This prints 0.6627434193491817.
Series details
We can use the
Lagrange inversion formula
to find the series, just as Lagrange did two and a half centuries ago.
The powers of sine can be expanded into the sum of sines of various frequencies and differentiated, leading the the equation
