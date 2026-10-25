---
title: "Duality in spherical trigonometry"
url: "https://www.johndcook.com/blog/2026/10/24/polar-triangle/"
fetched_at: 2026-10-25T10:01:22.665684+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Duality in spherical trigonometry

Source: https://www.johndcook.com/blog/2026/10/24/polar-triangle/

I’ve written before about the
law of cosines on a sphere
:
cos(
c
) = cos(
a
) cos(
b
) + sin(
a
) sin(
b
) cos(
C
).
But that’s just one of two laws of cosines on a sphere. The equation above is the law of cosines
for sides
. The law of cosines
for angles
is typographically very similar, just inverting the case of the letters used as arguments.
cos(
C
) = cos(
A
) cos(
B
) + sin(
A
) sin(
B
) cos(
c
).
Incidentally, the law of cosines for sides shows how the sides of a spherical triangle determine the angles. The law of cosines for angles shows how, unlike in the case of plane geometry, angles determine the sides.
Two kinds of angles
Let’s back up and say what the letters refer to. As is conventional in plane geometry, the sides of a triangle are
a
,
b
, and
c
, and the angles are
A
,
B
, and
C
, with
a
being the side opposite the angle
A
, and similarly for the other letters.
However, unlike plane geometry, the sides are also angles, but of a different sort. The sides
a
,
b
, and
c
are
central angles
, and the “angles”
A
,
B
, and
C
are
dihedral angles
.
The sides are arcs of a great circle. The side
a
, for example, is a portion of a great circle, running between the vertices at
B
and
C
[1]. Think of a plane that contains the center of the sphere
O
and the vertices
B
and
C
. The length of
a
is the angle at
O
.
The angles
A
,
B
, and
C
are the angles at which great circles meet. In the formalism of differential geometry, these angles exist in the tangent plane at the vertices. These angles are
intrinsic
, measured along the (tangent plane of) the surface of the sphere. The central angles are
extrinsic
, measured in a plane that cuts through the sphere to its center.
Polar triangles
Now because sides are angles and vertices are angles, we can interchange the two kinds of angles to form the
polar triangle
of the original triangle. This is a new triangle whose central angles are the complements of the original dihedral angles, and whose dihedral angles are the complements of the original central angles. In symbols,
a
′ = π −
A
b
′ = π −
B
c
′ = π −
C
A
′ = π −
a
B
′ = π −
b
C
′ = π −
c
Now we return to the laws of cosines at the top of the post: the law of cosines for angles is the law of cosines for sides applied to the polar triangle. Every equation in spherical trigonometry has a polar counterpart.
[1] There’s some overloaded terminology here, just as in plane geometry. The symbol
a
is used to denote a side of a triangle and also the length of that side. The symbol
A
is used to denote both a vertex and the dihedral angle at that vertex.
