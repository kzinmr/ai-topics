---
title: "Triangulation of convex polygons"
url: "https://iczelia.net/posts/polygon-triangulation/"
fetched_at: 2026-05-05T07:01:20.023073+00:00
source: "Kamila Szewczyk (iczelia)"
tags: [blog, raw]
---

# Triangulation of convex polygons

Source: https://iczelia.net/posts/polygon-triangulation/

In this brief article, I will discuss the preliminaries of polygon triangulation using the APL programming language. Triangulation is an important concept in computational geometry, and it has applications in various fields, such as computer graphics, mesh generation, and finite element analysis. Triangular meshes are often used to represent surfaces in computer graphics, and they are also used in finite element analysis to approximate the solution of partial differential equations.
Introduction
⌗
A convex polygon is a polygon in which all its interior angles are less than 180 degrees with vertices defined by
V
=
(
x
1
,
y
1
)
,
(
x
2
,
y
2
)
,
…
,
(
x
n
,
y
n
)
V = {(x_1, y_1), (x_2, y_2), \ldots, (x_n, y_n)}
V
=
(
x
1
​
,
y
1
​
)
,
(
x
2
​
,
y
2
​
)
,
…
,
(
x
n
​
,
y
n
​
)
, where
n
n
n
is the number of vertices. Triangulation is the partitioning of a polygon with
n
n
n
vertices into
n
−
2
n-2
n
−
2
triangles by adding
n
−
3
n-3
n
−
3
non-intersecting diagonals, which connect non-adjacent vertices.
Due to Euler, the total amount of ways to triangulate a
n
n
n
-gon is given by the
(
n
−
2
)
(n-2)
(
n
−
2
)
-th Catalan number:
C
n
=
1
n
+
1
(
2
n
n
)
C_n = \frac{1}{n+1}\binom{2n}{n}
C
n
​
=
n
+
1
1
​
(
n
2
n
​
)
Asymptotically, Catalan numbers grow as:
C
n
∼
4
n
n
3
/
2
π
C_n \sim \frac{4^n}{n^{3/2}\sqrt{\pi}}
C
n
​
∼
n
3/2
π
​
4
n
​
Consequently, the algorithm enumerating all possible triangulations of a polygon is exponential in time complexity.
Unconstrainted triangulation
⌗
If we wish to triangulate a polygon without any constraints, the fan triangulation of any polynomial can be computed in linear time:
Fan triangulation of a septagon
Once we pick a starting vertex
v
0
v_0
v
0
​
, we can connect it to all other vertices
v
1
,
v
2
,
…
,
v
n
−
1
v_1, v_2, \ldots, v_{n-1}
v
1
​
,
v
2
​
,
…
,
v
n
−
1
​
, creating
n
−
2
n-2
n
−
2
triangles.
Another method of unconstrained triangulation is the ear-clipping algorithm, which is computed in
O
(
n
2
)
\mathcal O(n^2)
O
(
n
2
)
time. The algorithm iteratively removes “ears” from the polygon, where an ear is a triangle with two consecutive edges of the polygon and the third edge inside the polygon. We begin the implementation with a function that given three points determines if they form a convex angle:
The next step is to determine, given a point
p
p
p
, whether it lies inside the triangle
a
b
c
abc
ab
c
. For this purpose, we could make use of barycentric coordinates, but the naive method (checking on which side of the half-plane created by the edges the point resides) is sufficient for our purposes:
The method for finding the ears is then straightforward. We return the ear and the rest of the polygon in a tuple. We implement checks in order to determine if the polygon is large enough, then iterate over the consecutive 3-triplets of vertices, to then determine if they form an ear. The first ear found is returned and its vertex is removed from the polygon.
The triangulation function successively removes ears from the polygon until only three vertices remain and returns the resulting triangulation:
To test our code, we will use the following polygon:
We will also plot it using Desmos:
The polygon
The resulting triangulation is given by:
The resulting triangulation
Constrained triangulation
⌗
Suppose that we wish to triangulate a
n
n
n
-gon into
n
−
2
n-2
n
−
2
triangles
T
=
t
1
,
t
2
,
…
,
t
n
−
2
T = {t_1, t_2, \ldots, t_{n-2}}
T
=
t
1
​
,
t
2
​
,
…
,
t
n
−
2
​
, where each triangle
t
i
t_i
t
i
​
is defined by the vertices
v
i
=
v
i
1
,
v
i
2
,
v
i
3
v_i = {v_{i1}, v_{i2}, v_{i3}}
v
i
​
=
v
i
1
​
,
v
i
2
​
,
v
i
3
​
. We can then define a cost function
f
:
T
→
R
f : T \to \mathbb R
f
:
T
→
R
that assigns a cost to each triangle. The cost function can be defined in various ways, such as the area of the triangle, the length of the edges, or the angle between the edges. The constrained triangulation problem is then to find the cost of the triangulation that minimizes the cost function.
Suppose that we have the following cost function, which assigns the cost of a triangle to be the sum of the lengths of its edges:
The naive solution to this problem runs in exponential time through testing all possible triangulations:
Nonetheless, for small polygons, it’s rather fast:
We can improve upon this solution making use of
Dynamic Programming
: Many recursive calls in the naive solution are repeated, so we can store the results of these calls in a table and use them to avoid recomputation. We accomplish it via the use of the
memo
operator from the
dfns
workspace:
