---
title: "Simple range reduction algorithm by Cody and Waite"
url: "https://www.johndcook.com/blog/2026/08/09/simple-range-reduction/"
fetched_at: 2026-08-10T10:23:23.316700+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Simple range reduction algorithm by Cody and Waite

Source: https://www.johndcook.com/blog/2026/08/09/simple-range-reduction/

At the end of my post on
how not to calculate cosine
I said that the first step in calculating cosine, particularly cosine of a large number, would be to do range reduction. This post will present a simple range reduction method by Cody and Waite that is adequate for moderately large arguments.
If you want to compute the sine or cosine of an angle
x
you could start by reducing
x
mod 2π since that would not change the result. However, accurately reducing a number mod 2π is not trivial; that’s why range reduction is an area of algorithm development.
Range reduction mod π/2
Even better would be to reduce
x
mod π/2. Reducing to a smaller range means that power series method, and other methods such as rational approximation, will be more efficient.
So suppose you can find an integer
k
such that
x
−
k
π/2 =
y
where 0 ≤
y
≤ π/2. Then sin(
x
) is ±sin(
y
) or ±cos(
y
), depending on
k
mod 4 equals 0, 1, 2, or 3.
from math import *

def reduced_sin(x, k):
     match k % 4:
        case 0: return sin(x)
        case 1: return cos(x)
        case 2: return -sin(x)
        case 3: return -cos(x)
Naive range reduction
Now let’s set
x
= 500. Then
k
= 318 because that’s the multiple of π/2 we need to subtract to bring
x
into range, and the sine of
x
should be the negative of the sine of the reduced value
y
because 318 = 2 mod 4.
The following code computes sin(
x
) with naive range reduction
def naive_sin(x):
    k = floor(x / (pi/2))
    y = x % (pi/2)
    return reduced_sin(y, k)
and when
x
= 500 the error is on the order of 1.7 × 10
−14
.
Better range reduction
The value of
k
above is fine, but we’d like to calculate
y
more accurately. The following code is much better.
def Cody_Waite_sin(x):
    C1 = 1686629713 / 2**30
    C2 = 4701928774853425 / 2**86

    k = floor(x / (pi/2))
    y = (x - k*C1) - k*C2
    return reduced_sin(y, k)
This will compute sin(500) to full machine precision. What kind of magic is this?
The trick is that the exact value of C1 + C2 equals π/2 to more precision than is possible in a single float [1]. You can confirm, with
bc
or some other extended precision software, that the difference between C1 + C2 and π/2 is roughly 2
−88
, while the limit of float precision is 2
−52
.
If we compute
y = x - k*(C1 + C2)
then we’re doing the same calculation as
naive_sin
and will get the same error. But if we compute
y = (x - k*C1) - k*C2
we will get a more accurate result, provided
x
isn’t too large.
You can use the following code to play around and see how large
x
can be before errors start to creep in. For small enough
x
, like 500, the Cody and Waite sine returns full precision. For larger
x
it’s better than naive sine but does not return full precision. And for large enough
x
it completely breaks down.
def compare(x):
    y0 = naive_sin(x) 
    y1 = Cody_Waite_sin(x)
    y2 = sin(x)
    print("Naive error:     ", y2 - y0)
    print("Cody Waite error:", y2 - y1)
Now this may seem circular since we’re using
math.sin
as our gold standard. However, this function is calling the sine function on your CPU, which is using sophisticated range reduction to compute its result accurately down to the last bit, assuming you run the code on a computer that’s less than 40 years old.
The Cody and Waite algorithm is inadequate for large
x
, but it’s a good place to begin studying range reduction. It shows there are clever ways of squeezing out more precision than seems possible.
[1] The numerator
n
1
of C1 is ⌊2
30
π/2⌋. The numerator
n
2
of C2 is the solution to
2
86−30
n
1
+
n
2
= ⌊2
86
π/2⌋.
