---
title: "Poles & polars in projective space with homogeneous coordinates"
url: "https://www.johndcook.com/blog/2026/11/01/projective-poles-and-polars/"
fetched_at: 2026-11-02T10:18:53.202626+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Poles & polars in projective space with homogeneous coordinates

Source: https://www.johndcook.com/blog/2026/11/01/projective-poles-and-polars/

I wrote several posts on poles and polars a few days ago. First, I wrote about the dual of a spherical triangle, called the
polar triangle
. Then I wrote about
poles and polars
in plane geometry and briefly mentioned the extension to projective geometry.
Poles and polars are a little awkward in the plane because you have to pay attention to special cases. Poles and polars are relative to a conic section, and are defined/computed differently depending on whether you’re taking the dual with respect to an
ellipse
, parabola, or hyperbola. Also, the polar of the center of a conic section isn’t defined.
Projective space
If you move from the Euclidean plane to the projective plane, the exceptions go away, though it may not seem so if you’re talking about points at infinity or lines at infinity. If you fully commit to working in projective space, there aren’t any hand-wavy points or lines “at infinity.” There’s not even a distinction between ellipses, parabolas, and hyperbolas.
There’s no such thing as a free lunch, and the cost of this elegant unification is moving to a bigger geometric space with a different coordinate system. Instead of working in the Euclidean spaces
R
² or
R
n
, we work in
P
n
over a field
F
which could be
R
but doesn’t need to be [1].
The coordinates on
P
n
are homogeneous coordinates, (
n
+ 1)-tuples of field elements, not all equal to zero, with two (
n
+ 1)-tuples representing the same point if they are proportional, i.e. one is a non-zero multiple of the other.
We can embed
R
n
in
P
n
by adding an extra coordinate on the end, set equal to 1. You could think of this extra coordinate as a
switch
, set to 1 for finite points and set to 0 for infinite points. But this distinction between finite and infinite points is an artifact of the embedding, not a property of
P
n
: there are no special points in
P
n
. A point that is “at infinity” in one embedding of
R
n
in
P
n
need not be in another embedding.
Poles and polars
Once you accept the need to work in homogeneous coordinates, everything becomes simple and consistent.
A quadric (a conic section when
n
= 2) is the set of points
{
x
:
x
ᵀ
A
x
= 0}
where
A
is a non-singular (
n
+ 1) by (
n
+ 1) symmetric matrix over
F
.
The
polar
of a point
p
is the hyperplane
{
x
:
p
ᵀ
A
x
= 0}
and the
pole
of a hyperplane
H
= {
x
:
u
ᵀ
x
= 0}
is the point
p
=
A
−1
u
.
Notice there’s no mention of “infinity” in this section. All the calculations take place in the field
F
with no points at infinity added.
[1] The only requirement is that the field
F
cannot have characteristic 2. So
F
could be the reals, the rationals, the complex numbers, etc.
F
could even be a finite field as long as the number of elements in
F
is not a power of 2.
