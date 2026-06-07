---
title: "How Kepler's equation led to Bessel functions"
url: "https://www.johndcook.com/blog/2026/06/06/from-kepler-to-bessel/"
fetched_at: 2026-06-07T07:01:35.168277+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# How Kepler's equation led to Bessel functions

Source: https://www.johndcook.com/blog/2026/06/06/from-kepler-to-bessel/

The
previous post
very briefly said that the integral representation for Bessel functions was motived by solving Kepler’s equation. This post will go into more detail.
Kepler’s equation
There are multiple ways to describe the position of a planet in an elliptical orbit around a star. For historical reasons, these descriptions have arcane names such as mean anomaly, true anomaly, and eccentric anomaly.
This post
explains how these three are related.
For this post, it is enough to say that often you know mean anomaly
M
and want to know eccentric anomaly
E
. These are related via Kepler’s equation
where
e
is the eccentricity of the orbit. You’d like to solve for
E
as a function of
M
and
e
, but there’s no elementary way to do that.
One way to solve Kepler’s equation is to take a guess at
E
and plug it into the right hand side of
to get a new
E
, and keep iterating until the two sides are closer together. I write more about this
here
.
Another approach to solving Kepler’s equation is to use Newton’s method. I write more about that
here
.
Still another approach is to expand
E
in a sine series and find the series coefficients. An advantage to this approach is that once you have the coefficients, you have an expression for
E
as a function of
M
, and you can plug in more values of
M
without having to solve Kepler’s equation for each value of
M
separately.
Sine series coefficients
Kepler’s equation is easy to solve at
E
= 0 and at
E
= π. In both cases,
E
=
M
. So the function
E
−
M
is zero at both ends of [0, π], which suggests we try to expand
E
−
M
in a sine series
We then calculate the Fourier coefficients
a
n
as usual.
The second line uses integration by parts. The third line uses Kepler’s equation. The last line uses the definition of the Bessel functions
J
n
given in the previous post.
