---
title: "The imbalance theorem"
url: "https://www.johndcook.com/blog/2026/08/18/the-imbalance-theorem/"
fetched_at: 2026-08-19T10:00:59.266032+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# The imbalance theorem

Source: https://www.johndcook.com/blog/2026/08/18/the-imbalance-theorem/

The imbalance conjecture is now a theorem. James Alexander Schreib and Yousof Yavari posted a
proof
last week.
What does the
conjecture
theorem say? Start with a graph
G
with no edge between two nodes of the same degree. Then for every edge, calculate the absolute value of the difference of the degree of each end. The imbalance theorem says there exists another graph
H
whose vertices have degrees corresponding to the differences of degrees in
G
.
For example, let
G
be the graph below.
The edges from the top red vertex
A
to each of the blue vertices around it all have degree difference 5 because
A
has degree 6 and the vertices
a
0
to
a
4
have degree 1. The edge between the two red vertices,
A
and
B
, has degree difference 2. The remaining vertices have degree difference 3.
So the
multiset
of degree differences is
{5, 5, 5, 5, 5, 2, 3, 3, 3}
The imbalance theorem says there exists a graph
H
whose nodes have these degrees. Here is an example of such an
H
.
Note that in
H
, the 5 red nodes have degree 5, the single green node has degree 2, and the three blue nodes have degree 3.
More graph posts
