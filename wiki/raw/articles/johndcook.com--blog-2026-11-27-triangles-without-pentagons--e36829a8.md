---
title: "How many triangles can a graph with no pentagons have?"
url: "https://www.johndcook.com/blog/2026/11/27/triangles-without-pentagons/"
fetched_at: 2026-11-28T10:00:44.518912+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# How many triangles can a graph with no pentagons have?

Source: https://www.johndcook.com/blog/2026/11/27/triangles-without-pentagons/

Suppose you have a graph with
n
nodes and no pentagons, how many triangles can it contain?
Here a pentagon means a cycle of length 5 and a triangle means a cycle of length 3. This is an abstract property of the graph, not related to the representation of the graph on a plane, unless the graph can be embedded in a plane with no edge crossings.
A
paper
posted two days ago proves that the maximum number of triangles is bounded by
The notation
o
(1) is a term that goes to zero as
n
grows. See notes
here
.
Roughly speaking, the no-pentagon requirement takes the square root of the maximum number of triangles. The maximum number of triangles in a graph with
n
nodes is
n
(
n
− 1)(
n
− 2)/6 =
O
(
n
³) and the no-pentagon rule cuts this down to
O
(
n
3/2
).
