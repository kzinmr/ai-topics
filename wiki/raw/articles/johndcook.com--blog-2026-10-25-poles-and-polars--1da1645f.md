---
title: "Poles and polars"
url: "https://www.johndcook.com/blog/2026/10/25/poles-and-polars/"
fetched_at: 2026-10-26T10:03:30.487162+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Poles and polars

Source: https://www.johndcook.com/blog/2026/10/25/poles-and-polars/

The previous two posts have been about polar triangles. The first
used
a polar triangle to derive a theorem, and the second showed how to
compute
polars using linear algebra. But what exactly
is
a polar triangle and why is it called that?
Poles and polars on a sphere
Let’s start with a sphere
S
and a great circle
G
. Then
G
is the intersection of
S
with a plane through the center of
S
. The circle
G
has two
poles
, two points on opposite sides of
S
that are as far as possible (i.e. π/2 radians) from
G
. If you rotate the sphere so that
G
is the equator, the poles are the north and south pole.
Conversely, if you start with a point
P
on the sphere
S
, the
polar
of
P
is the great circle for which
P
is a pole. So if you think of
P
as the north pole, the polar of
P
is the equator. The term
equator
would have been more intuitive than
polar
, but the terminology was established a couple centuries ago.
In my opinion it would be clearer to call poles and polars both
duals
. The dual of a great circle is a point, and the dual of a point is a great circle.
Now let’s look at a spherical triangle
ABC
sides
a
,
b
, and
c
. The vertices of the
polar triangle
of
ABC
are the poles of the sides
a
,
b
, and
c
. This definition is essentially correct, but it needs a little refinement.
The pole
A
′ of the side
a
is one of the two poles of the great circle containing
a
, the one that that lies in the same hemisphere as
A
. Define
B
′ and
C
′ similarly, and the polar triangle is the spherical triangle with vertices
A
′
B
′
C
′.
Poles and polars in the plane
The terms
pole
and
polar
were coined for spherical geometry, then generalized to plane (projective) geometry. If you think of great circles as the lines of spherical geometry, then you can carry the idea of poles and polars over to plane geometry where the pole (dual) of a line is a point, and the polar (dual) of a point is a line.
However, in the plane you can’t define the pole of a line without more context. You have to start with a circle (or more generally a conic section) and define the pole of a line
with respect to the circle
and the define the polar of a point
with respect to the same circle
.
Given a circle
S
with center
O
, to find the polar of a point
P
≠
O
, let
Q
be the
inversion
of
P
in
S
, and let ℓ be the line through
Q
perpendicular to the line
OP
.
Conversely, the pole of a line ℓ with respect to a circle
S
is the inversion of
Q
in
S
where
Q
is the intersection of ℓ with
OQ
. Here we assume the line ℓ does not pass through the center of the circle
O
because otherwise
O
=
Q
and it doesn’t make sense to speak of the line
OQ
.
Projective geometry
The definitions above have a couple holes that can be filled in by extending the Euclidean plane to the projective plane.
We defined the pole of a line ℓ except when ℓ passes through the center of the circle. If ℓ passes through
O
then the pole of ℓ is the point at infinity in the direction of ℓ. Similarly, we defined the polar of all points except
O
. In projective geometry, we can define the polar of
O
to the be the line at infinity, the line containing all the points at infinity.
