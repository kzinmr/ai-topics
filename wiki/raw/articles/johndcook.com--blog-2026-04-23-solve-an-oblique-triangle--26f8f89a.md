---
title: "Approximation to solve an oblique triangle"
url: "https://www.johndcook.com/blog/2026/04/23/solve-an-oblique-triangle/"
fetched_at: 2026-04-28T07:02:46.935089+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Approximation to solve an oblique triangle

Source: https://www.johndcook.com/blog/2026/04/23/solve-an-oblique-triangle/

The
previous post
gave a simple and accurate approximation for the smaller angle of a right triangle. Given a right triangle with sides
a
,
b
, and
c
, where
a
is the shortest side and
c
is the hypotenuse, the angle opposite side
a
is approximately
in radians. The previous post worked in degrees, but here we’ll use radians.
If the triangle is oblique rather than a right triangle, there an approximation for the angle
A
that doesn’t require inverse trig functions, though it does require square roots. The approximation is derived in [1] using the same series that is the basis of the approximation in the earlier post, the power series for 2 csc(
x
) + cot(
x
).
For an oblique triangle, the approximation is
where
s
is the semiperimeter.
For comparison, we can find the exact value of
A
using the law of cosines.
and so
Here’s a little Python script to see how accurate the approximation is.
from math import sqrt, acos

def approx(a, b, c):
    "approximate the angle opposite a"
    s = (a + b + c)/2
    return 6*sqrt((s - b)*(s - c)) / (2*sqrt(b*c) + sqrt(s*(s - a)))

def exact(a, b, c):
    "exact value of the angle opposite a"    
    return acos((b**2 + c**2 - a**2)/(2*b*c))

a, b, c = 6, 7, 12
print( approx(a, b, c) )
print( exact(a, b, c) )
This prints
0.36387538476776243
0.36387760856668505
showing that in our example the approximation is good to five decimal places.
[1] H. E. Stelson. Note on the approximate solution of an oblique triangle without tables. American Mathematical Monthly. Vol 56, No. 2 (February, 1949), pp. 84–95.
