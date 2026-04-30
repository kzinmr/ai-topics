---
title: "Random hexagon fractal"
url: "https://www.johndcook.com/blog/2026/04/09/random-hexagon-fractal/"
fetched_at: 2026-04-30T07:02:00.506470+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Random hexagon fractal

Source: https://www.johndcook.com/blog/2026/04/09/random-hexagon-fractal/

I recently ran across a
post
on X describing a process for creating a random fractal. First, pick a random point
c
inside a hexagon.
Then at each subsequent step, pick a random side of the hexagon and create the triangle formed by that side and
c
. Update
c
to be the center of the new triangle and plot
c
.
Note that you only choose a random
point
inside the hexagon once. After that you randomly choose
sides
.
Now there are
many
ways to define the center of a triangle. I assumed the original meant barycenter (centroid) when it said “center”, and apparently that was correct. I was able to create a similar figure.
But if you define center differently, you get a different image. For example, here’s what you get when you use the incenter, the center of the largest circle inside the triangle.
Related posts
