---
title: "The number of points on an elliptic curve"
url: "https://www.johndcook.com/blog/2026/10/22/the-number-of-points-on-an-elliptic-curve/"
fetched_at: 2026-10-23T10:01:32.631001+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# The number of points on an elliptic curve

Source: https://www.johndcook.com/blog/2026/10/22/the-number-of-points-on-an-elliptic-curve/

An elliptic curve
E
over a finite field
F
consists of the set of points (
x
,
y
) satisfying the equation
y
² =
x
³ +
ax
+
b
with
x
and
y
in
F
. Typically in cryptography the field
F
is the integers mod
p
where
p
is a very large prime number.
The number of points on
E
is roughly the number of elements in
F
. So for a curve over the integers mod
p
, the curve has roughly
p
points.
The next section will give an intuitive argument for why the number of points on
E
should be roughly the number of elements in
F
. Then the next section will give a rigorous bound. Then after that we’ll work through an example.
Hand-wavy estimate
For a prime
p
, half the non-zero integers mod
p
have a square root and half do not. The ones that do have a square root have two square roots. For example, look at the integers mod 7. The numbers 1, 2, and 4 have square roots but the numbers 3, 5, and 6 do not. Here’s a little bit of Python to verify this.
>>> [x**2 % 7 for x in range(1,7)]
[1, 4, 2, 2, 4, 1]
Now if we wanted to count the number of solutions to
y
² =
x
(mod
p
)
we’d find it equals
p
. That’s because (0, 0) is a point on the curve, and for (
p
− 1)/2 values of
x
there are two values of
y
, and for the remaining values of
x
there are no values of
y
.
To put it another way, if we pick a value of
x
at random, it will have two square roots or no square roots with roughly equal probability.
Now suppose we pick an
x
and random and compute
x
³ +
ax
+
b
. We might guess that this process scatters
x
values in an unbiased way, being no more likely to produce a square than a non-square. Our guess turns out to be approximately correct, though there may be a small bias in favor of squares or non-squares.
Precise bound
Hasse’s theorem gives a precise bound on the number of points on an elliptic curve
E
. It says
#
E
=
p
+ 1 −
t
where
|
t
| ≤ 2√
p
.
So if
p
is on the order of 2
n
, the number of points on
E
is also on the order of 2
n
because √
p
is far smaller than
p
. That’s all you need to know at a high level. The rest of this post will look at a particular example in full detail.
Detailed example
The NIST curve
P-384
has been
in the news
lately. For this curve, the based field is integers modulo a 384-bit prime
p
and so the number of points on the curve is also 384-bit number. Specifically
p
= 2
384
− 2
128
− 2
96
+ 2
32
− 1,
and so we know
a priori
that the number of points on the curve equals 2
384
plus or minus a factor less than 2
193
.
The number of points on the elliptic curve P-384 is known to be
n
= 39402006196394479212279040100143613805079739270465446667946905279627659399113263569398956308152294913554433653942643
See NIST SP 800-186, §3.2.1.4⁠.
We can calculate
t
at a Python REPL.
>>> n = 39402006196394479212279040100143613805079739270465446667946905279627659399113263569398956308152294913554433653942643
>>>  p = 2**384 - 2**128 - 2**96 + 2**32 - 1
>>> t = p + 1 - n
>>> t
1388124618062372383606759648309780106643088307173319169677
The fact that
t
is positive means the number of points
n
on our curve is slightly less than
p
. Here “slightly” is relative. The value of
p
−
n
is a huge number, but it’s small relative to
p
.
We can verify that |
t
| is less than our
a priori
bound of 2√
p
.
>>> from math import sqrt
>>> t/(2*sqrt(p))
0.11057050503394951
So the actual value of
t
is about nine times smaller than its bound.
