---
title: "Testing pentagonal numbers"
url: "https://www.johndcook.com/blog/2026/06/15/testing-pentagonal-numbers/"
fetched_at: 2026-06-16T07:00:49.141038+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Testing pentagonal numbers

Source: https://www.johndcook.com/blog/2026/06/15/testing-pentagonal-numbers/

The
n
th pentagonal number
P
n
is the number of dots in diagrams like those below with
n
concentric pentagons.
We have the formula
P
n
= (3
n
² −
n
)/2
where
n
is a positive integer. If
n
is an integer but not positive, the equation above defines a
generalized
pentagonal number.
If you’re given an
n
, you can easily compute
P
n
. But suppose you’re given a large number
x
. How would you determine if it is a pentagonal number? And if it is a pentagonal number, how would you find
n
such that
x
=
P
n
?
If
x
=
P
n
= (3
n
² −
n
)/2
then we can solve a quadratic equation for
n
:
n
= (1 ± √(24
x
+ 1))/6.
If 24
x
+ 1 is not a perfect square,
n
is not an integer and
x
is not a pentagonal number, ordinary or generalized. For example,
√(24 × 20260615 + 1)) = 22051.185…
and so 20260615 is not a pentagonal number nor a generalized pentagonal number.
Now suppose
x
= 170141183460469231731687303715884105727.
Is this a pentagonal number? You can’t just compute √(24
x
+ 1) in floating point arithmetic because the result is a 20-digit number, and floating point number have 15 digits of precision, so you can’t tell whether the result is an integer.
However, you can compute
⌊√(24
x
+ 1)⌋
with only integer arithmetic using the
sqrt_floor
function from
this post
.
def sqrt_floor(n):
    a = n
    b = (n + 1) // 2
    while b < a:
        a = b
        b = (a*a + n) // (2*a)
    return a
The following prints a positive number,
x = 2**127 - 1
y = 24*x + 1
r = sqrt_floor(y)
print(y - r**2)
which tells us
y
is not a perfect square.
Now suppose
y
is
a perfect square. Then
(1 ± √(24
x
+ 1))/6
is rational, does it have to be an integer? In fact it one, and only one, of the roots will be an integer. If
24
x
+ 1 =
r
²
then
r
is congruent to ±1 mod 6 because the left side is congruent to 1 mod 6. If
r
= 1 mod 6 then the smaller root is an integer, and if
r
= 5 mod 6 then the larger root is an integer.
So if 24
x
+ 1 =
r
², then
x
is a pentagonal number if
r
= 5 mod 6 and a generalized pentagonal number otherwise.
The function
pentagonal_index
takes a number
x
and return n if
x
=
P
n
and
None
if no such
n
exists.
def pentagonal_index(x):
    y = 24*x + 1
    r = sqrt_floor(y)
    if r*r != y:
        return None
    if r % 6 == 5:
        return (1 + r) // 6
    else:
        return (1 - r) // 6
We can test this with the following code.
P = lambda n: (3*n**2 - n) // 2
for n in [2, 3, -4, -5, 10**200]:
    assert(pentagonal_index(P(n)) == n)
Note that
P(10**200)
is too big to fit into a float, but the code works fine. This is because we use integer division (
//
) everywhere. If we had said
P = lambda n: (3*n**2 - n) / 2
the test above would pass for the small values of
n
but output
OverflowError: integer division result too large for a float
when it came to
n
= 10
200
.
Related posts
