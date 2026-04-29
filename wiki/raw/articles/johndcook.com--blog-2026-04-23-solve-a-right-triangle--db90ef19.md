---
title: "Simple approximation for solving a right triangle"
url: "https://www.johndcook.com/blog/2026/04/23/solve-a-right-triangle/"
fetched_at: 2026-04-29T07:02:06.989094+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Simple approximation for solving a right triangle

Source: https://www.johndcook.com/blog/2026/04/23/solve-a-right-triangle/

Suppose you have a right triangle with sides
a
,
b
, and
c
, where
a
is the shortest side and
c
is the hypotenuse. Then the following approximation from [1] for the angle
A
opposite side
a
seems too simple and too accurate to be true. In degrees,
A
≈
a
172° / (
b
+ 2
c
).
The approximation above only involves simple arithmetic. No trig functions. Not even a square root. It could be carried out with pencil and paper or even mentally. And yet it is surprisingly accurate.
If we use the 3, 4, 5 triangle as an example, the exact value of the smallest angle is
A
= arctan(3/4) × 180°/π ≈ 36.8699°
and the approximate value is
A
≈  3 × 172° / (4 + 2×5) = 258°/7 ≈ 36.8571°,
a difference of 0.0128°. When the angle is more acute the approximation is even better.
Derivation
Where does this magical approximation come from? It boils down to the series
2 csc(
x
) + cot(
x
) = 3/
x
+
x
³/60 +
O
(
x
4
)
where
x
is in radians. When
x
is small,
x
³/60 is extremely small and so we have
2 csc(
x
) + cot(
x
) ≈ 3/
x.
Apply this approximation with csc(
x
) =
c
/
a
and cot(
x
) =
b
/
a
. and you have
x
≈ 3
a
/(
b
+ 2
c
)
in radians. Multiply by 180°/π to convert to degrees, and note that 540/π ≈ 172.
Discovery
It’s unmotivated to say “just expand 2 csc(
x
) + cot(
x
) in a series.” Where did
that
come from?
There’s a line in [1] that says “It can been seen, either from tables or from a consideration of power series that the radian measure of a small angle lies approximately one-third of the way from the sine to the tangent.” In other words
3
x
≈ 2 sin(
x
) + tan(
x
)
.
You can verify that by adding the power series and noting that the cubic terms cancel out.
But that’s just the beginning. The author then makes the leap to conjecturing that if the weighted
arithmetic
mean gives a good approximation, maybe the weighted
harmonic
mean gives an even better approximation, and that leads to considering
2 csc(
x
) + cot(
x
) ≈ 3/
x.
Extension
See the
next post
for an extension to oblique triangles. Not as simple, but based on the same trick.
[1] J. S. Frame. Solving a right triangle without tables. The American Mathematical Monthly, Vol. 50, No. 10 (Dec., 1943), pp. 622-626
