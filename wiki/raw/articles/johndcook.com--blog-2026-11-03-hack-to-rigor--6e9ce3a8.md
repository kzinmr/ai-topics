---
title: "From a graphics hack to a rigorous model of the projective plane"
url: "https://www.johndcook.com/blog/2026/11/03/hack-to-rigor/"
fetched_at: 2026-11-04T10:00:59.847499+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# From a graphics hack to a rigorous model of the projective plane

Source: https://www.johndcook.com/blog/2026/11/03/hack-to-rigor/

This post will show how a graphic programmer’s hack could lead to a rigorous definition of the projective plane.
As mentioned in the
previous post
, we start by adding some “points at infinity” to Euclidean plane to take care of exceptional situations. For example, instead of saying most pairs of lines intersect at a single point but some don’t intersect at all, you could say all pairs of lines intersect at a point, but for some pairs of lines, namely parallel lines, that intersection point is “at infinity.”
Suppose you need to write a program to find the intersection of two lines. The usual way of doing this would be to implement a
partial function
that takes two lines as input, and sometimes returns a point of intersection and sometimes does something else: it crashes, or throws an exception, or hangs. But if we add in points at infinity, our program could always return a point.
But how are you going to represent points at infinity? It’s not enough to use a floating point infinity, because different lines intersect at different points at infinity. For example, the lines
y
= 1 and
y
= 2 intersect at the point at infinity in the horizontal direction, but the lines
x
= 1 and
x
= 2 intersect at the point at infinity in the vertical direction. You could say the former lines intersect at (o, inf) and the latter at (inf, 0), but that won’t work in general.
The lines
y
= 3
x
+ 1 and
y
= 3
x
+ 1 intersect at the point at infinity with slope 3, but the lines
y
= 5
x
+ 1 and
y
= 5
x
+ 1 intersect at the point at infinity with slope 5. If you say both pairs of lines meet at (inf, inf) you’ve lost information.
So you come up with a hack. You represent points not as (
x
,
y
) pairs but as (
x
,
y
,
f
) where
x
and
y
are real numbers but
f
is a Boolean flag. Now (
x
,
y
, true) represents the ordinary point (
x
,
y
) and (
x
,
y
, false) represents the point at infinity in the direction of the line from the origin to (
x
,
y
). Problem solved!
After a while, you realize that this hack can be useful for more than just finding the intersection of lines. You discover that if you use a real number instead of a Boolean for the last coordinate, you can implement translations and rotations using matrix multiplication. So you replace true and false with 1 and 0, do your matrix calculation, then divide by the last coordinate so the result ends in 1 or 0 again. And this works really well.
This last coordinate is starting to act more like the other coordinates. You treat it as a peer when you multiply triples by a matrix, but only temporarily. You immediately normalize at the end to get back to more familiar territory.
Maybe it occurs to you after a while that you’re doing something analogous the introduction of imaginary numbers. At first the square root of −1 was seen as a hack that produced correct answers. It wasn’t
really
a number but something
imagined
to be a number as an aid to calculation. Over time mathematicians got more comfortable with these imaginary numbers and explored what would happen if they were treated as first class citizens. Maybe you should do the same with this third coordinate that started out as a hack.
This leads you to homogenous coordinates. A point in the extended plane you’ve created is represented by a triple (
x
,
y
,
z
) with the understanding that given a number λ ≠ 0, (
x
,
y
,
z
) and (λ
x
, λ
y
, λ
z
) represent the same point. This is the natural extension of always dividing by the last coordinate, if it’s not zero, so that the triple always ends in 1. And you discover after a while that you need to add in the requirement that not all the coordinates can be zero at the same time.
You show this to a mathematician friend and he puts your construction in fancier language. He says you’re extended plane is ℝ³ minus the origin, modulo non-zero scalar multiplication. In other words, the points in your extended plane are equivalence classes of points in ℝ³.
Now if you think about this geometrically, your equivalence classes are lines through the origin because that’s what you get when you look at all scalar multiples of a given vector. What started out as the plane with extra points added is now the set of all lines though the origin. That’s one way to define the projective plane: a point in the projective plane corresponds to a line through the origin in ℝ³. Furthermore, a line in the projective plane corresponds to a plane through the origin in ℝ³.
Lines through the origin are determined by where they cross the unit sphere, so you could think of the projective plane as a sphere with one modification: because a line through the origin crosses the sphere in two antipodal points, we consider those two points in ℝ³ to be a single point in the projective plane.
