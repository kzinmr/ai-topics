---
title: "When will the decimals in a/b repeat?"
url: "https://www.johndcook.com/blog/2026/06/27/decimal-period/"
fetched_at: 2026-06-28T07:01:23.235783+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# When will the decimals in a/b repeat?

Source: https://www.johndcook.com/blog/2026/06/27/decimal-period/

The previous post looked at how many digits are in the reduced fraction for the
n
th harmonic number. I was curious about how long the cycle of digits in a harmonic number might be.
I wrote about the period length for the digits of fractions
almost a decade ago
. This post includes code so I can apply it to harmonic demoninators.
from sympy import lcm, factorint, n_order

def period(n):
    factors = factorint(n)
    exp2 = factors.get(2, 0)
    exp5 = factors.get(5, 0)
    r = max(exp2, exp5)

    d = n // (2**exp2 * 5**exp5)
    s = 1 if d == 1 else n_order(10, d)
    return (r, s)
This function returns two numbers:
r
is the number of non-repeating digits at the beginning and
s
is the length of the repeating part.
The following code
from functools import reduce

def lcm_range(n):
    return reduce(lcm, range(1, n + 1))

print( period( lcm_range(50) ) )
prints (5, 1275120) meaning that 1/lcm(1, 2, 3, …, 49, 50) has five non-repeating digits following by 1,275,120 digits that repeat
ad infinitum
. And so the decimals in the expansion of
H
50
go have a cycle length of 1,275,120.
