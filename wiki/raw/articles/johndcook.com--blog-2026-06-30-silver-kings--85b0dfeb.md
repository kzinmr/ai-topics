---
title: "Silver Rectangles and the Ways of Kings"
url: "https://www.johndcook.com/blog/2026/06/30/silver-kings/"
fetched_at: 2026-07-01T07:00:52.881959+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Silver Rectangles and the Ways of Kings

Source: https://www.johndcook.com/blog/2026/06/30/silver-kings/

Golden rectangles
The defining property of golden rectangle is that if you stick a square on its longer side, you get another golden rectangle.
The smaller vertical rectangle is similar to the larger horizontal rectangle. This means
φ / 1 = (1 + φ) / φ
which tells us φ² = 1 + φ and so the golden ratio φ equals (1 + √5)/2.
Silver rectangles
A silver rectangle is one that if you stick
two
squares on its longer side you get another rectangle with the same aspect ratio.
This tells us
σ / 1 = (1 + 2σ) / σ
and so σ² = 1 + 2σ and the silver ratio is σ = 1 + √2.
Just as you can define a golden ratio and a silver ratio, there’s an analogous way to define a sequence of
metallic ratios
.
Kings and Dellanoy numbers
The silver ratio has several connections to the ways of ways kings. By that I mean the number of ways a king can go from one corner of a chessboard to the diagonally opposite corner without backtracking.
A king can move one space in any direction. If we start with a king in the bottom left corner of the board, the no-backtracking requirement means the king can move up, right, or up and right.
The number of paths a king can take from one corner to the opposite corner of an
n
×
n
chessboard is the
n
th central Delannoy number
D
n
. more generally Dellanoy numbers are defined for an
m
×
n
chessboard, but I’ll stick to the case
m
=
n
called the
central
Dellanoy number, or just Dellanoy numbers for short.
The first Delannoy number is 1 because there’s only one way for a king to get from one corner to the other: do nothing, because the opposite corner is the same corner. The second Delannoy number is 3 because the king can move up then right, or right then up, or move diagonally up and right.
For a 3 × 3 grid things are significantly more complicated, and
D
3
= 13. For an 8 × 8 grid the number of paths is 48,639.
Generating function
How would you estimate the number of paths on an
n
×
n
board for large values of
n
without calculating it exactly? You might start by finding a generating function for the Delannoy numbers, which works out to be
(
x
² − 6
x
+ 1)
−1/2
The radius of convergence
r
for the generating function series is the distance from 0 to the closest singularity of the generating function, which is the smaller root of
x
² − 6
x
+ 1
which is
3 − √8 = (3 + √8)
−1
= (1 + √2)
−2
= 1/σ²
i.e. the radius of convergence is the reciprocal of the silver ratio squared.
Asymptotic estimate
The radius of convergence gives us a first approximation to the asymptotic size of the series coefficients. Since we’re working with the generating function of the Delannoy numbers, these coefficients are the Delannoy numbers. That is,
D
n
~
r
−
n
= (σ
2
)
n
= σ
2
n
.
That’s as good as you can do just knowing the radius of convergence. A more careful analysis would refine this estimate by dividing by a factor proportional to √
n
.
Related posts
