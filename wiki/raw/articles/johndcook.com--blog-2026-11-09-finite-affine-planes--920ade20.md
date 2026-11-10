---
title: "Finite Affine Planes"
url: "https://www.johndcook.com/blog/2026/11/09/finite-affine-planes/"
fetched_at: 2026-11-10T10:01:16.460530+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Finite Affine Planes

Source: https://www.johndcook.com/blog/2026/11/09/finite-affine-planes/

The previous post was on
finite projective planes
. This post will look at finite affine planes and the next will look at
finite hyperbolic planes
.
Affine geometry is essentially what remains of Euclidean geometry if you keep the incidence properties, e.g. wanting to know whether things intersect, and forget about metric properties such as segment lengths and angle measurements. As with projective planes, affine planes can be finite.
The axioms of an affine plane are as follows.
Any two distinct points lie on exactly one line.
For any line ℓ and point
P
not on ℓ, there is exactly one line through
P
that doesn’t intersect ℓ.
There exist three points that are not collinear.
The second axiom says that affine geometry is Euclidean, or maybe Euclidean-lite. It lacks features of Euclidean geometry, but it doesn’t contradict Euclidean geometry.
To construct an example of a finite affine plane, let
p
be an odd prime and construct a
p
×
p
grid with
x
– and
y
-coordinates 0, 1, 2, …,
p
− 1. The affine lines are essentially the Euclidean lines that pass through the grid points, if lines can wrap around the sides, i.e. you’re working on a discrete torus. Algebraically, lines are the solutions to
x
=
c
and
y
=
mx
+
b
mod
p
.
A finite affine plane always has
n
² points and
n
² +
n
lines. The number
n
can be an odd prime, or any prime power greater than 2. It is unknown whether there are examples in which
n
is not a prime power. There are no affine planes of order 6 or 10, and the case of
n
= 12 is open.
