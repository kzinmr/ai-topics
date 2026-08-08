---
title: "How not to calculate cosine"
url: "https://www.johndcook.com/blog/2026/08/07/how-not-to-calculate-cos/"
fetched_at: 2026-08-08T10:13:47.195588+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# How not to calculate cosine

Source: https://www.johndcook.com/blog/2026/08/07/how-not-to-calculate-cos/

Calculus professors with no experience in numerical computing will tell students that computers calculate trig functions with power series. They don’t. I worked on the implementation of trig functions in hardware, and I can assure you we didn’t just use power series.
Power series are an excellent way to calculate functions
near the center of the series
, such as computing
sine for small angles
. But the further you get from the center, the less useful power series are.
Let’s suppose you want to calculate cos(200) using the power series for cosine. The
n
th term of that series is
(−1)
n
x
2
n
/ (2
n
)!
This is an alternating series, and so the error in truncating the series after
n
terms is bounded by the size of the
n
+1 term,
if
you’ve gone far enough out in the series that the terms are monotonically decreasing in absolute value.
To calculate cos(200) to machine precision, i.e. with an error of less than 2
−52
, we’d need to sum the series up to
n
where
| 200
2
n
+2
/ (2
n
+ 2)! | < 2
−52
Actually, that will ensure that the
absolute
error is small enough, but not that the
relative
error is small enough; if the value of cos(200) is small, we’d need more terms. Let’s ignore that and assume we’re only concerned with absolute error.
Turns out we’d need 287 terms. That’s a lot of terms. But you might say “That’s fine. I’m not in a hurry, and it’s just more work for the computer, not for me.” OK, so let’s try.
from math import *

s = 0
for n in range(288):
    s += (-1)**n * 200**(2*n) / factorial(2*n)
print(s)
This prints -3.6840358571084123e+67. You may suspect the answer is incorrect since values of cosine are on the order of 1, not on the order of 10
67
. Something went spectacularly bad. On closer inspection, it’s remarkable the code didn’t crash.
If you changed
200
to
200.0
above, the code would crash. Calculating
200.0**(2*n)
overflows when
n
= 67. But when we calculate
200**(2*n)
, the result is an integer. And we’re dividing by
factorial(2*n)
, which is also an integer. Both of these integers become too large to fit in a float, but their
ratio
has a maximum value of around 10
80
, smaller than the maximum float, which is on the order of 10
308
.
When we don’t overflow, we have a different problem: catastrophic cancellation. You can’t calculate a number between −1 and 1 as an alternating sum of numbers as large as 10
80
. You’d need more than 80 + 16 = 96 decimal places of precision to compute the sum accurately, and floating point only gives you between 15 and 16 decimal places of precision.
So how
would
you calculate cos(200)? The first step would be to use some sort of range reduction on 200. You could reduce 200 mod 2π to get a smaller number to work with.
>>> from math import cos, pi
>>> x = 200 % (2*pi)
>>> x
5.221255477432827
Using a power series to compute the cosine of 5.221255477432827 is feasible, but not optimal. There’s also another problem: the naive range reduction above loses some precision.
>>> cos(x)
0.48718767500701254
>>> cos(x) - cos(200)
6.661338147750939e-15
The error is small, but it’s still an order of magnitude larger than machine precision. You can’t simply reduce
n
mod 2π with ordinary float division because the integer part of
n
/ 2π pushes some digits of precision off the right end. I intend to write about how range reduction works in future posts.
