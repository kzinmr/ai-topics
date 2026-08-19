---
title: "Big little hexagon"
url: "https://www.johndcook.com/blog/2026/08/18/big-little-hexagon/"
fetched_at: 2026-08-19T10:00:59.099704+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Big little hexagon

Source: https://www.johndcook.com/blog/2026/08/18/big-little-hexagon/

A new paper just came out,
The Maximum-Area Small Polygon Problem
. The paper solves the problem of finding, for each
n
, the
n
-gon with diameter 1 and maximum area.
For odd
n
, the solution is what you might expect: a regular
n
-gon. I would expect this to be the solution for even
n
as well, but it’s not.
In 1974 [1] Ron Graham found a solution for
n
= 6, a hexagon with unit diameter and area larger than a regular hexagon with unit diameter. Polygons with diameter ≤ 1 are called “small”, and he found the “largest” (i.e. maximum area) small hexagon.
The vertices of Graham’s hexagon are given below.
A = (0.0000000000,  0.0000000000)
  C = (0.4023506913, -0.5000000000)
  F = (0.9390533483, -0.3437714489)
  B = (1.0000000000,  0.0000000000)
  E = (0.9390533483,  0.3437714489)
  D = (0.4023506913,  0.5000000000)
You can verify that the distance between any pair of vertices is no more than 1 and that the area of Graham’s hexagon is 0.674981.
The area of a regular hexagon of diameter 1 is (3/8)√3 = 0.649519, and the area of Graham’s hexagon is about 3.9% larger.
[1] R. L. Graham. The Largest Small Hexagon. Journal of Combinatorial Theory (A) 18, 165–170 (1975). The paper was submitted February 22, 1974 and published in 1975.
