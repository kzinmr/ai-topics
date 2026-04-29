---
title: "Newton diameters"
url: "https://www.johndcook.com/blog/2026/04/16/newton-diameters/"
fetched_at: 2026-04-29T07:02:07.085460+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Newton diameters

Source: https://www.johndcook.com/blog/2026/04/16/newton-diameters/

Let
f
(
x
,
y
) be an
n
th degree polynomial in
x
and
y
. In general, a straight line will cross the zero set of
f
in
n
locations [1].
Newton defined a
diameter
to be any line that crosses the zero set of
f
exactly
n
times. If
f
(
x
,
y
) =
x
² +
y
² − 1
then the zero set of
f
is a circle and diameters of the circle in the usual sense are diameters in Newton’s sense. But Newton’s notion of diameter is more general, including lines the cross the circle without going through the center.
Newton’s theorem of diameters says that if you take several parallel diameters (in his sense of the word), the centroids of the intersections of each diameter with the curve
f
(
x
,
y
) = 0 all line on a line.
To illustrate this theorem, let’s look at the elliptic curve
y
² =
x
³ − 2
x
+ 1,
i.e. the zeros of
f
(
x
,
y
) =
y
² − (
x
³ − 2
x
+ 1). This is a third degree curve, and so in general a straight line will cross the curve three times [2].
The orange, green, and red lines are parallel, each intersecting the blue elliptic curve three times. The dot on each line is the centroid of the intersection points, the center of mass if you imagine each intersection to be a unit point mass. The centroids all lie on a line, a vertical line in this example though in general the line could have any slope.
I hadn’t seen this theorem until I ran across it recently when skimming [3]. Search results suggest the theorem isn’t widely known, which is surprising for a result that goes back to Newton.
Update
: See
this post
for another illustration using a fifth degree polynomial.
Related posts
[1] Bézout’s theorem says a curve of degree
m
and a curve of degee
n
will always intersect in
mn
points. But that includes complex roots, adds a line at infinity, and counts intersections with multiplicity. So a line, a curve of degree 1, will intersect a curve of degree
n
at
n
points in this extended sense.
[2] See the description of Bézout’s theorem in the previous footnote. In the elliptic curve example, the parallel lines meet at a point at infinity. A line that misses the closed component of the elliptic curve and only passes through the second component has 1 real point of intersection but there would be 2 more if we were working in ℂ² rather than ℝ².
In algebraic terms, the system of equations
y
² =
x
³ − 2
x
+ 1
3
y
= 2
x
+
k
has three real solutions for small values of
k
, but for sufficiently large values of |
k
| two of the solutions will be complex.
[3] Mathematics: Its Content, Methods, and Meaning. Edited by A. D. Aleksandrov, A. N. Kolmogorov, and M. A. Lavrent’ev. Volume 1.
