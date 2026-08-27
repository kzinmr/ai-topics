---
title: "Junk solutions"
url: "https://www.johndcook.com/blog/2026/08/26/junk-solutions/"
fetched_at: 2026-08-27T10:01:12.147853+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Junk solutions

Source: https://www.johndcook.com/blog/2026/08/26/junk-solutions/

When you’re interested in studying a family of functions, it can be useful to look at a differential equation that the functions solve. This is a theme I’ve written about several times, most recently
here
and
here
, but also three years ago
here
.
Orthogonal polynomials are mathematically elegant as well as very useful in applications [1]. Various families of orthogonal polynomials satisfy various differential equations. These equations have a polynomial and non-polynomial solutions. What use are the latter?
If the differential equation modeled something physical, then the second solution would be necessary to have a complete basis of solutions. But if the differential equation is only instrumental in studying the orthogonal polynomials, what use is a non-polynomial solution?
These non-polynomial solutions turn out to be useful.
Just as “junk” DNA turned out not to be junk, these “junk” solutions are important
. Junk DNA doesn’t directly code for proteins, but it regulates DNA that does code for proteins and serves other purposes. Similarly, these non-polynomial solutions carry information related to the polynomial solutions.
For example, orthogonal polynomials are used to construct numerical integration methods, such as Gaussian quadrature, and the associated non-polynomial solutions describe the error in these integration methods. Incidentally, Gaussian quadrature is based on Legendre polynomials, mentioned in the
previous post
. For every family of orthogonal polynomials there is a corresponding integration method. See
these notes
.
Another tie-in to recent posts is that these non-polynomial solutions are the minimal solution to the polynomial family’s
three-term recurrence
, the solution that takes
extra care
to compute numerically.
This post has been very high-level, alluding to ideas without going into details. I’d like to write future posts that go into more depth regarding the ideas introduced here.
[1] “Real analysts cannot do without Fourier, complex analysts cannot do without Laurent, and numerical analysts cannot do without Chebyshev [polynomials].” — Lloyd N. Trefethen”
