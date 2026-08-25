---
title: "Numerical (in)stability of recurrence relations"
url: "https://www.johndcook.com/blog/2026/08/24/numerical-instability-recurrece/"
fetched_at: 2026-08-25T10:01:27.042269+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Numerical (in)stability of recurrence relations

Source: https://www.johndcook.com/blog/2026/08/24/numerical-instability-recurrece/

The
previous post
gave several examples of three-term recurrence relations for special functions. These relations can be computationally useful, but they have to be applied carefully.
Several years ago I wrote a post on
stable and unstable recurrences
. In that post I show that the stability of the recurrence relation for Bessel functions produces depends on which kind of Bessel function and which direction the recurrence is applied.
In the forward direction, computing higher order values from lower order values, works well for Bessel functions of the second kind
Y
n
but not for Bessel functions of the first kind
J
n
. In the reverse direction, the recurrence is stable for
J
n
but not for
Y
n
.
I didn’t explain in that post why this is. In this post I will.
Second order linear difference equations have two independent solutions, just like second order linear differential equations. For both kinds of equations, all solutions are linear combinations of the two solutions. Suppose one solution grows with
n
and the other decays. You may want to compute the decaying solution, but in doing so you might pick up a small component of the growing solution due to rounding error.
This post
illustrates this phenomena for differential equations, and
this post
illustrates it for difference equations.
When you look at a plot of Bessel functions in a text book, you’ll probably see a few plots of
J
n
(
x
) and
Y
n
(
x
) for a few small values of
n
. The functions seem to behave roughly the same way, like sine and cosine. And that’s true,
as functions of
x
.
But it’s not true for
J
n
(
x
) and
Y
n
(
x
) as functions of
n
for fixed
x
. As
n
increases,
J
n
(
x
) decays to zero and
Y
n
(
x
) goes off to −∞.
That’s the source of numerical instability. And there will be similar instability problems for other recurrences where the ratios of the two independent solutions goes to zero or infinity as a function of
n
.
There are techniques for computing the solution that does not diverse, the so-called minimal solution, such as Miller’s algorithm mentioned
here
.
