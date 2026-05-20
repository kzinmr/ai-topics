---
title: "Square root of x² − 1"
url: "https://www.johndcook.com/blog/2026/05/19/square-root-of-x-squared-minus-one/"
fetched_at: 2026-05-20T07:00:49.314803+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Square root of x² − 1

Source: https://www.johndcook.com/blog/2026/05/19/square-root-of-x-squared-minus-one/

How should we define √(
z
² − 1)? Well, you could square
z
, subtract 1, and take the square root. What else would you do?!
The question turns out to be more subtle than it looks.
When
x
is a non-negative real number, √
x
is defined to be the non-negative real number whose square is
x
. When
x
is a complex number √
x
is defined to be
a
function that extends √
x
from the real line to the complex plane by analytic continuation. But we can’t extend √
x
as an analytic function to the entire complex plane ℂ. We have to choose to make a “cut” somewhere, and the conventional choice is to make a cut along the negative real axis.
Using the principle branch
The “principle branch” of the square root function is defined to be the unique function that analytically extends √
x
from the positive reals to ℂ \ (−∞, 0].
Assume for now that by √
x
we mean the principle branch of the square root function. Now what does √(
z
² − 1) mean? It
could
mean just what we said at the top of the post: we square
z
, subtract 1, and apply the (principle branch of the) square root function. If we do that, we must exclude those values of
z
such that (
z
² − 1) is negative. This means we have to cut out the imaginary axis and the interval [−1, 1].
This is what Mathematica will do when asked to evaluate
Sqrt[z^2 - 1]
. The command
ComplexPlot[Sqrt[z^2 - 1], {z, -2 - 2 I, 2 + 2 I}]
makes the branch cuts clear by abrupt changes in color.
A different approach
Now let’s take a different approach. Consider the function √(
z
² − 1) as a whole. Do not think of it procedurally as above, first squaring
z
etc. Instead, think of a it as a black box that takes in
z
and returns a complex number whose square is
z
² − 1.
This function has an obvious definition for
z
> 1. And we can extend this function, via analytic continuation, to more of the complex plane. We can do this
directly
, not by extending the square root function. But as before, we cannot extend the function analytically to all of ℂ. We have to cut something out. A common choice is to cut out [−1, 1]. This eliminates the need for a branch cut along the imaginary axis.
The function
where log has a branch cut along the negative axis extends √(
z
² − 1) the way we want.
The Mathematica code
ComplexPlot[Exp[(1/2) (Log[z - 1 ] + Log[z + 1])], {z, -2 - 2 I, 2 + 2 I}]
shows that our function is now continuous across the imaginary axis, though there’s still a discontinuity as you cross [−1, 1].
We used this analytic extension of √(
z
² − 1) in the
previous post
to eliminate branch cuts in an identity.
Related posts
