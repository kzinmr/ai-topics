---
title: "Pole and polar with respect to an ellipse"
url: "https://www.johndcook.com/blog/2026/10/26/inversion-in-an-ellipse/"
fetched_at: 2026-10-27T10:01:03.720177+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Pole and polar with respect to an ellipse

Source: https://www.johndcook.com/blog/2026/10/26/inversion-in-an-ellipse/

The previous three post have been part of a series on geometric duality. The traditional but somewhat mysterious terminology is the
pole
of a line and the
polar
of a point. As explained
here
, the terminology was first coined in the context of spherical geometry where the term “pole” makes sense. It was then extended to the plane where the meaning is less obvious.
The use of poles and polars is that they preserve certain geometric information, and so they can transform one problem into a dual problem. This was illustrated in the
first post
in the series. Equations in spherical trigonometry have a buy-one-get-one-free property: applying an identity to the dual of a triangle gives another identity.
This post
discussed how to define the pole of a line and the polar of a point with respect to a circle in the plane. The post stated that more generally you can do this in the projective plane. Since there’s no difference between conic sections in the projective plane, anything you can do for a circle you can do for an ellipse or hyperbola.
Given a point
P
, we can define its polar line geometrically or algebraically.
Algebraic approach
Given an ellipse with equation
x
²/
a
² +
y
²/
b
² = 1
where
a
>
b
, the foci are at ±
c
where
c
= √(
a
² −
b
²).
For a point
P
= (
x
0
,
y
0
), its polar with respect to the ellipse is the line
(
x
0
/
a
²)
x
+ (
y
0
/
b
²)
y
= 1.
Geometric approach
To find the polar of a point
P
, we start by inverting
P
in the ellipse. Draw any line through
P
that meets the ellipse at two points
A
and
B
. On that line there is exactly one point Q that divides
AB
harmonically with
P
:
QA/QB = PA/PB
with
Q
on the opposite side of
AB
from
P
if
P
is inside the ellipse, or between
A
and
B
if
P
is outside. The polar is the line through
Q
parallel to the tangent at
R
, where
R
is the point where the ray
OP
meets the ellipse.
Focus and directrix
Plane and projective geometry are very mature and so some of the terminology sounds quaint. One such term is the
directrix
of a conic section, explained
here
. The polar of a focus is a directrix, and the pole of a directrix is a focus.
Related posts
