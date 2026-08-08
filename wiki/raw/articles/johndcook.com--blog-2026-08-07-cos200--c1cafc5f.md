---
title: "Calculating the cosine of numbers outside the range of floats"
url: "https://www.johndcook.com/blog/2026/08/07/cos200/"
fetched_at: 2026-08-08T10:13:47.173234+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Calculating the cosine of numbers outside the range of floats

Source: https://www.johndcook.com/blog/2026/08/07/cos200/

In a footnote to the
previous post
, I said that Python’s math library can calculate the logarithm of extremely large numbers but not the cosine. This post will expand on that comment.
In this post I’ll use
n
= 200! as my example rather than 1000! because this value of
N
is larger than the largest representable floating point number but small enough to be more convenient to work with.
Suppose someone calculates 200! for you:
78865786736479050355236321393218506229513597768717326329474253324435\
94499634033429203042840119846239041772121389196388302576427902426371\
05061926624952829931113462857270763317237396988943922445621451664240\
25403329186413122742829485327752424240757390324032125740557956866022\
60319041703240623517008587961789222227896237038973747200000000000000\
00000000000000000000000000000000000
You could now calculate log(
n
) using
n
= 7.886578673647905 × 10
374
and so
log(
n
) = log(7.886578673647905 × 10
374
)
= log(7.886578673647905) + 374 log(10) = 863.2319871924055.
The key thing that makes this possible is that the least significant digits of
n
only affect the least significant digits of log(
n
). In the calculation above I kept the first 16 digits of
n
. Python couldn’t make use of any more digits, and had no need of any more digits, in order to produce the logarithm to machine precision.
Cosine doesn’t work that way. The cosine of
n
depends on the remainder when
n
is divided by 2π, and that remainder depends on every single digit of
n
. I’ll illustrate that below.
Using
bc -l
and setting the scale to 400, I can calculated
n
then calculate
cos(
n
+ 10
i
)
for i running from 0 to 374, tweaking each digit one at a time. (Except when a digit is a 9 and the addition results in a carry.)
n = 1
    for (i = 1; i <= 200; i++) n *= i
    scale = 400
    for (i = 1; i <= 374; i++) {
        x = c(n+10^i)
        scale = 16
        print x/1, "\n"
        scale = 400
    }
Here’s what a plot of the results look like.
The value of cos(
n
) is about −0.985, but the values above are all over the map. We can look at the range by projecting all the points over to the left edge then rotating a quarter turn:
The remarkable thing about this image is that there are a few gaps, i.e. a few values the cosine does
not
take on.
Here’s a more sophisticated way to look at it. The sequence 10
i
mod 2π is dense in [0, 2π], and so by going far enough out in the sequence, we can find a value that shifts the phase of
n
by any desired amount within any given tolerance.
Every digit in
n
matters, and changing any digit can change the value of cosine to be essentially any value. You cannot calculate the cosine of an enormous number without using some kind of extended precision arithmetic. There are clever range reduction algorithms that minimize the amount of extended arithmetic necessary, but extended arithmetic cannot be completely eliminated.
