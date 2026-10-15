---
title: "Harmonic triangle"
url: "https://www.johndcook.com/blog/2026/10/13/harmonic-triangle/"
fetched_at: 2026-10-14T10:01:15.324107+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Harmonic triangle

Source: https://www.johndcook.com/blog/2026/10/13/harmonic-triangle/

Pascal’s triangle is the most famous triangular arrangement of numbers. I’ve written about other numerical triangles, such as
Bell’s triangle
and the
trinomial triangle
. There’s another well-known triangle that somehow I never heard of until recently: the harmonic triangle, first explored by Leibniz around 1700.
To create the harmonic triangle, start with the harmonic series
1, 1/2, 1/3, 1/4, 1/5, …
This is the first column of the triangle. Next take the differences of the terms:
(1 − 1/2), (1/2 − 1/3), (1/3 − 1/4), … = 1/2, 1/6, 1/12, …
This, shifted down one space, is the second column of the triangle. Taking differences again gives the third column, and so forth. Column
c
of the triangle consists of the
c
th differences of the harmonic series.
1
    1/2  1/2
    1/3  1/6   1/3
    1/4  1/12  1/12  1/4
    1/5  1/20  1/30  1/20  1/5
    …
Each entry is the difference of the entries to its west and northwest. If we let
L
(
r
,
c
) be the element in the
r
th row and
c
th column, then
Every numerator is 1, though it’s not immediately obvious why this should be the case. And every number is a value of the beta function, the function that gives the normalizing constant for the beta distribution [1].
Related posts
[1] Ayoub B. Ayoub. The Harmonic Triangle and the Beta Function. Mathematics Magazine, Vol. 60, No. 4 (Oct., 1987), pp. 223-225
