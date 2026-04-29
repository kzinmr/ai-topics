---
title: "Circular arc approximation"
url: "https://www.johndcook.com/blog/2026/04/28/circular-arc-approximation/"
fetched_at: 2026-04-29T07:00:51.599383+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Circular arc approximation

Source: https://www.johndcook.com/blog/2026/04/28/circular-arc-approximation/

Suppose you have an arc
a
, a portion of a circle of radius
r
, and you know two things: the length
c
of the chord of the arc, and the length
b
of the chord of half the arc, illustrated below.
Here θ is the central angle of the arc. Then the length of the arc,
r
θ, is approximately
a
=
r
θ ≈ 12
b
²/(
c
+ 4
b
).
If the arc is moderately small, the approximation is very accurate.
This approximation is simple, accurate, and not obvious, much like the one in
this post
Derivation
Let φ = θ/4. Then the angle between the chords
b
and
c
is φ. This follows from the inscribed angle theorem, illustrated below.
There are two right triangles in the diagram above that have an angle φ: a smaller triangle with hypotenuse
b
and a larger triangle with hypotenuse 2
r
. From the smaller triangle we learn
cos(φ) =
c
/ 2
b
and from the larger triangle we learn
sin(φ) =
b
/ 2
r
.
Now expand in power series.
c
/ 2
b
= cos(φ) = 1 − φ
2
/2! + φ
4
/4! − …
2
b
/
a
= sin(φ) / φ = 1 − φ
2
/3! + φ
4
/5! − …
If we multiply 2
b
/
a
by 3 and subtract
c
/ 2
b
then the φ
2
terms cancel out and we get
6
b
/
a
−
c
/ 2
b
= 2 − φ
4
/60 + …
and so
6
b
/
a
−
c
/ 2
b
≈ 2
to a very high degree of accuracy when φ is small. The approximation follows by solving for
a
.
Example
Let θ = π/3 and so φ = 0.26…, not a particularly small value of φ, but small enough for the approximation to work well.
Set
r
= 1 so
a
= θ. Then
b
= 2 sin(π/12) = 0.51764
and
c
= 2
b
cos(π/12) = 1.
Now in application, we know
b
and
c
, not θ, and so pretend we
measured
b
= 0.51764 and
c
= 1. Then we would approximate
a
by
12
b
²/(
c
+ 4
b
) = 1.04718
while the exact value is 1.04720. Unless you can measure lengths to more than four significant figures, the approximation may has well be exact because approximation error would be less than measurement error.
[1] J. M. Bruce. Approximation to a Circular Arc. The American Mathematical Monthly. Vol. 49, No. 3 (March 1942), pp. 184–185
