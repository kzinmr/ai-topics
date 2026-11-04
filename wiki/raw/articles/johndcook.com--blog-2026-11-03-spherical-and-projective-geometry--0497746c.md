---
title: "Euclidean, Spherical, and Projective Geometry"
url: "https://www.johndcook.com/blog/2026/11/03/spherical-and-projective-geometry/"
fetched_at: 2026-11-04T10:00:59.856152+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Euclidean, Spherical, and Projective Geometry

Source: https://www.johndcook.com/blog/2026/11/03/spherical-and-projective-geometry/

Spherical geometry is very tangible because we live on a sphere. Projective geometry seems much more exotic, and yet they’re closely related. To show how they’re connected, let’s go back to the origins of non-Euclidean geometry.
Euclidean geometry
Here are Euclid’s five postulates, statements about what geometric objects can be constructred.
To draw a straight line from any point to any point.
To produce (extend) a finite straight line continuously in a straight line.
To describe a circle with any centre and distance (radius).
That all right angles are equal to one another.
That, if a straight line falling on two straight lines makes the interior angles on the same side less than two right angles, the two straight lines, if produced indefinitely, meet on that side on which the angles are less than two right angles.
Clearly there’s something different about the fifth postulate, the parallel postulate. It’s much longer and more complicated than the other postulates. There was speculation from ancient times that the parallel postulate might be unnecessary, that it could be derived as a theorem rather than stated as an axiom.
Non-Euclidean geometry
Giovanni Girolamo Saccheri (1667–1733) tried to prove the fifth postulate by contradiction, and in the process began the study of non-Euclidean geometry. He wasn’t the first to try to prove the fifth postulate. Ptolemy, for example, tried to prove the fifth postulate as a theorem in the second century AD. But Saccheri was the first to try a proof by contradiction, or at least the first to extensively explore contradictions to the parallel postulate.
A more modern formulation of the parallel postulate says
Given a line
ℓ
and a point
P
not on
ℓ
, there is exactly one line through
P
parallel to
ℓ
.
Non-Euclidean geometry replaces this axiom with an alternative, such as saying there are multiple lines parallel to
ℓ
or that there are no lines parallel to
ℓ
.
Note that non-Euclidean geometry is not an arbitrary tinkering with the axioms of geometry just to see what happens. It tinkers with one specific axiom for motivated reasons.
Spherical geometry
You can create models of non-Euclidean geometry using Euclidean geometry. For example, spherical geometry is constructed by defining a (spherical) point as a (Euclidean) point on a sphere, and defining a (spherical) line to be a great circle, the intersection of a (Euclidean) plane with the sphere. In spherical geometry there are no parallel lines: all lines intersect.
This example shows that non-Euclidean geometry need not be non-physical. If you leave general relativity out of the picture and think of physical space as undeniably Euclidean, it can still be useful to think of different geometries to describe objects in Euclidean space.
Projective geometry
In projective geometry, all distinct lines intersect at one point.
In spherical geometry, all distinct lines intersect at two points, on opposite sides of a great circle. If you consider antipodal pairs of points on a sphere to be a single point in the projective plane, now all lines intersect at a single point. Projective geometry is just one step away from spherical geometry.
The recent thread of posts started with a
post
a couple weeks ago about two versions of the law of cosines on a sphere, one for sides and one for angles. You can go from one to the other by going from a spherical triangle to its polar triangle. That started me going down the rabbit hole of poles and polars, first in spherical geometry, then in plane geometry, then in projective geometry, culminating
here
.
Now we have two ways of producing poles and polars on a sphere: the original construction in terms of spherical geometry, and the projective construction. They are consistent: you can do spherical geometry, then identify antipodal points, or you can identify antipodal points, then do projective geometry. You end up at the same place by either path.
One theme in the last few posts has been that projective geometry is not an arbitrary exercise in abstraction but a framework that can simplify how we think about things. For example, when I defined the polar triangle of a spherical triangle
here
, I said that the vertices of the polar triangle are the poles of the sides of the original triangle. Imagine the side as the equator of the sphere and take one of the poles; that’s where the abstract concept of “pole” comes from. But which pole do you take? There is a convention for answering this question, but in projective geometry it doesn’t matter: both (spherical) poles constitute one (projective) point.
Posts in this series
