---
title: "Distribution of digits in fractions"
url: "https://www.johndcook.com/blog/2026/04/10/fraction-digits/"
fetched_at: 2026-04-30T07:02:00.514326+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Distribution of digits in fractions

Source: https://www.johndcook.com/blog/2026/04/10/fraction-digits/

There’s a lot of mathematics just off the beaten path. You can spend a career in math and yet not know all there is to know about even the most basic areas of math. For example, this post will demonstrate something you may not have seen about decimal forms of fractions.
Let
p
> 5 be a prime number and 0 <
k
<
p
. Then the digits in
k
/
p
might be the same for all
k
, varying only by cyclic permutations. This is the case, for example, when
p
= 7 or
p
= 17. More on these kinds of fractions
here
.
The digits in
k
/
p
repeat for every
k
, but different values of
k
might have sequences of digits that vary by more than cyclic permutations. For example, let’s look at the values of
k
/13.
>>> for i in range(1, 13):
...   print(i/13)
...
 1 0.0769230769230769
 2 0.1538461538461538
 3 0.2307692307692307
 4 0.3076923076923077
 5 0.3846153846153846
 6 0.4615384615384615
 7 0.5384615384615384
 8 0.6153846153846154
 9 0.6923076923076923
10 0.7692307692307693
11 0.8461538461538461
12 0.9230769230769231
One cycle goes through the digits 076923. You’ll see this when
k
= 1, 3, 4, 9, 10, or 11. The other cycle goes through 153846 for the rest of the values of
k
. The cycles 076923 and 153846 are called the
distinct repeating sets
of 13 in [1].
If we look at fractions with denominator 41, thee are six distinct repeating sets.
02439
04878
07317
09756
12195
14634
26829
36585
You could find these by modifying the Python code above. However, in general you’ll need more than default precision to see the full periods. You might want to shift over to
bc
, for example.
When you look at all the distinct repeating sets of a prime number, all digits appear almost the same number of times. Some digits may appear one more time than others, but that’s as uneven as you can get. A corollary in [1] states that if
p
= 10
q
+
r
, with 0 <
r
< 10, then 11 −
r
digits appear
q
times, and
r
− 1 digits appear
q
+ 1 times.
Looking back at the example with
p
= 13, we have
q
= 1 and
r
= 3. The corollary says we should expect 8 digits to appear once and 2 digits to appear twice. And that’s what we see: in the sets 076923 and 153846 we have 3 and 6 repeated twice and the remaining 8 digits appear once.
In the example with
p
= 41, we have
q
= 4 and
r
= 1. So we expect all 10 digits to appear 4 times, which is the case.
Related posts
[1] James K. Schiller. A Theorem in the Decimal Representation of Rationals. The American Mathematical Monthly
Vol. 66, No. 9 (Nov., 1959), pp. 797-798
