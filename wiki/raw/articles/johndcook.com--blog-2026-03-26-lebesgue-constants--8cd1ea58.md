---
title: "Lebesgue constants"
url: "https://www.johndcook.com/blog/2026/03/26/lebesgue-constants/"
fetched_at: 2026-04-30T07:02:02.293838+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Lebesgue constants

Source: https://www.johndcook.com/blog/2026/03/26/lebesgue-constants/

I alluded to Lebesgue constants in the
previous post
without giving them a name. There I said that the bound on order
n
interpolation error has the form
where
h
is the spacing between interpolation points and δ is the error in the tabulated values. The constant
c
depends on the function
f
being interpolated, and to a lesser extent on
n
. The constant λ is independent of
f
but depends on
n
and on the relative spacing between the interpolation nodes. This post will look closer at λ.
Given a set of
n
+ 1 nodes
T
define
Then the Lebesgue function is defined by
and the Lebesgue constant for the grid is the maximum value of the Lebesgue function
The values of Λ are difficult to compute, but there are nice asymptotic expressions for Λ when the grid is evenly spaced:
When the grid points are at the roots of a Chebyshev polynomial then
The previous post mentioned the cases
n
= 11 and
n
= 29 for evenly spaced grids. The corresponding values of Λ are approximately 155 and 10995642. So 11th order interpolation is amplifying the rounding error in the tabulated points by a factor of 155, which might be acceptable. But 29th order interpolation is amplifying the rounding error by a factor of over 10 million.
The corresponding values of Λ for Chebyshev-spaced nodes are 2.58 and 3.17. Chebyshev spacing is clearly better for high-order interpolation, when you have that option.
