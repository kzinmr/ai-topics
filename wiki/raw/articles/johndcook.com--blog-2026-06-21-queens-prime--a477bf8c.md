---
title: "Queens on a prime order board"
url: "https://www.johndcook.com/blog/2026/06/21/queens-prime/"
fetched_at: 2026-06-22T07:01:36.921824+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Queens on a prime order board

Source: https://www.johndcook.com/blog/2026/06/21/queens-prime/

The
n
queens problem is to place on an
n
×
n
chessboard
n
queens so that none attacks any other. This means there is only one queen on every horizontal, vertical, and diagonal line.
When
n
is a
prime number
≥ 5, it is sufficient to place the queens on a line that has slope 2, 3, 4, …,
n
− 2. (The slope cannot be 1 because that’s a diagonal. And it cannot be
n
− 1 because
n
− 1 = −1 mod
n
is also a diagonal.) [1]
Here we imagine the top and bottom edge being identified. Geometrically, this makes the chessboard a cylinder. Algebraically, the points on a line of slope
s
have the coordinates
(
a
+
k
,
b
+
ks
)
where addition is carried out mod
n
.
All
solutions to the
n
queens problem have this form when
n
= 5.
Some
solutions will have this form for larger prime values of
n
but not all.
For example, when
n
= 7, here is a solution where all the queens are on a line of slope 2.
But here is another solution where the queens do not all lie on a line of constant slope.
Related posts
[1] W. H. Bussey. A Note on the Problem of the Eight Queens. The American Mathematical Monthly, Vol. 29, No. 7 (August 1922), pp. 252–253
