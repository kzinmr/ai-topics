---
title: "Consecutive Pythagorean triangle sides"
url: "https://www.johndcook.com/blog/2026/06/25/consecutive-pythagorean/"
fetched_at: 2026-06-26T07:00:57.104893+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Consecutive Pythagorean triangle sides

Source: https://www.johndcook.com/blog/2026/06/25/consecutive-pythagorean/

In this post we find all Pythagorean triples that contain consecutive numbers, all Pythagorean triples (
a
,
b
,
c
) such that
a
+ 1 =
b
or
b
+ 1 = c.
a
+ 1 =
b
George Osborne wrote a paper [1] addressing the question of when the squares of two consecutive numbers is also a square. Geometrically this is asking for primitive Pythagorean triples for which the legs are consecutive integers.
He proved that the sequence shorter legs satisfies the recurrence relation
with initial conditions
u
0
= 0 and
u
1
= 1. This is OEIS sequence
A001652
.
The method for solving recurrences like the one above is analogous to the method for solving linear differential equations. See a solution
here
. This gives us the following formula for the terms:
b
+ 1 =
c
It’s also possible for the longer side and hypotenuse of a Pythagorean triangle to be consecutive numbers, as in the (5, 12, 13) triangle.
All primitive Pythagorean triples are given by Euclid’s formula
with integers
m
>
n
> 0. If
b
and
c
are consecutive numbers, then
and so
m
=
n
+ 1. Therefore all possible values of
b
are given by 2
n
(
n
+ 1) for
n
> 1.
[1] Geo. A. Osborne. A Problem in Number Theory. The American Mathematical Monthly, Vol. 21, No. 5 (May, 1914), pp. 148-150
