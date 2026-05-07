---
title: "Triangular analog of the squircle"
url: "https://www.johndcook.com/blog/2026/05/06/triangular-analog-of-the-squircle/"
fetched_at: 2026-05-07T07:01:37.610703+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Triangular analog of the squircle

Source: https://www.johndcook.com/blog/2026/05/06/triangular-analog-of-the-squircle/

TimF left a comment on my
guitar pick post
saying the image was a “squircle-ish analog for an isosceles triangle.” That made me wonder what a more direct analog of the squircle might be for a triangle.
A squircle is not exactly a square with rounded corners. The sides are continuously curved, but curved most at the corners. See, for example,
this post
.
Suppose the sides of our triangle are given by
L
1
(
x
,
y
) = 1 for
i
= 1, 2, 3. For example,
We design a function
f
(
x
,
y
) as a soft penalty for points not being on one of the sides and look at the set of points
f
(
x
,
y
) = 1.
You might recognize this as a Lebesgue norm, analogous to the one used to define a squircle.
The larger
p
is, the heavier the penalty for being far from a side and the closer the level set
f
(
x
,
y
) = 1 comes to being a triangle.
