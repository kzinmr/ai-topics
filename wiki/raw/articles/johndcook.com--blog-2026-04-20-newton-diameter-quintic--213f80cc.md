---
title: "More on Newton’s diameter theorem"
url: "https://www.johndcook.com/blog/2026/04/20/newton-diameter-quintic/"
fetched_at: 2026-04-29T07:02:06.564201+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# More on Newton’s diameter theorem

Source: https://www.johndcook.com/blog/2026/04/20/newton-diameter-quintic/

A few days ago I wrote a post on
Newton’s diameter theorem
. The theorem says to plot the curve formed by the solutions to
f
(
x
,
y
) = 0 where
f
is a polynomial in
x
and
y
of degree
n
. Next plot several parallel lines that cross the curve at
n
points and find the centroid of the intersections on each line. Then the centroids will fall on a line.
The previous post contained an illustration using a cubic polynomial and three evenly spaced parallel lines. This post uses a fifth degree polynomial, and shows that the parallel lines need not be evenly spaced.
In this post
f
(
x
,
y
) =
y
³ +
y
−
x
(
x
+ 1) (
x
+ 2) (
x
− 3) (
x
− 2).
Here’s an example of three lines that each cross the curve five times.
The lines are
y
=
x
+
k
where
k
= 0.5, −0.5, and −3. The coordinates of the centroids are (0.4, 0.9), (0.4, -0.1), and (0.4, -2.6).
And to show that the requirement that the lines cross five times is necessary, here’s a plot where one of the parallel lines only crosses three times. The top line is now
y
=
x
+ 2 and the centroid on the top line moved to (0.0550019, 2.055).
