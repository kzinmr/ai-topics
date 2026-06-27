---
title: "Writing down harmonic numbers"
url: "https://www.johndcook.com/blog/2026/06/26/writing-down-harmonic-numbers/"
fetched_at: 2026-06-27T07:01:07.499793+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Writing down harmonic numbers

Source: https://www.johndcook.com/blog/2026/06/26/writing-down-harmonic-numbers/

The
n
th harmonic number is the sum of the reciprocals of the first
n
positive integers.
H
n
= 1 + 1/2 + 1/3 + 1/4 + … + 1/
n
The product of all the denominators is
n
!, so you could write
H
n
as a fraction
H
n
=
p
/
q
where
p
=
n
!
H
n
is an integer and
q
=
n
!.
While
p
/
q
is
a
way to write
H
n
as a fraction, it’s not the most efficient because
p
and
n
! will have common factors.
If we write
H
n
as a reduced fraction, the denominator will be the least common multiple of the integers 1 through
n
. That number is asymptotically exp(
n
). That estimate follows from the prime number theorem.
So for large
n
the denominator will be roughly exp(
n
), and in base
b
it would have around
n
/log(
b
)
digits.
The numerator will be exp(
n
)
H
n
, and since
H
n
is asymptotically log(
n
) + γ, the numerator for large
n
will be roughly
exp(
n
) (log(
n
) + γ)
and will have around
(
n
+ log log(
n
) ) / log(
b
)
digits.
Let’s see how well our asymptotic estimates work for
n
= 50. The 50th harmonic number is
H
50
= 13943237577224054960759 / 3099044504245996706400.
This fraction has 23 digits in the numerator and 22 in the denominator. We would have predicted around
(50 + log(log(50)))/log(10) = 22.3
digits in the numerator and
50/log(10) = 21.7
digits in the denominator.
Let’s try a larger example, looking at the 1000th harmonic number in binary. We’ll use the following Python code.
from fractions import Fraction

def bits(n):
    H = sum(Fraction(i, i+1) for i in range(1, n+1))
    p, q = H.numerator, H.denominator
    # subtract 2 because bin returns a string starting with 0b.
    return len(bin(p)) - 2, len(bin(q)) - 2

print(bits(1000))
This returns 1448 and 1438. We would have estimated
(1000 + log(log(1000)))/log(2) = 1445.4
bits in the numerator and
1000/log(2) = 1442.7
bits in the denominator.
Related posts
