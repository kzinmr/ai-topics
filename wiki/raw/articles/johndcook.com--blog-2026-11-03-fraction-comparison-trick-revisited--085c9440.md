---
title: "Fraction comparison trick revisited"
url: "https://www.johndcook.com/blog/2026/11/03/fraction-comparison-trick-revisited/"
fetched_at: 2026-11-04T10:00:59.831980+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Fraction comparison trick revisited

Source: https://www.johndcook.com/blog/2026/11/03/fraction-comparison-trick-revisited/

A few years ago
I wrote about a curious result:
a
/
b
is usually greater than
c
/
d
when
a
+
d
is greater than
b
+
c
. And “usually” means with probability 11/12.
As stated in the post, you can make this statement rigorous by choosing integers up to size
N
at random and taking the limit as
N
goes to infinity.
We can also choose
a
,
b
,
c
, and
d
uniformly from [0, 1]. This is similar to choosing four integers up to
N
and dividing all the integers by
N
, which doesn’t change the probabilities.
Now
a
/
b
>
c
/
d
if and only if
ad
>
bc
, so another way to state the theorem is that
Prob(
ad
>
bc
|
a
+
d
>
b
+
c
) = 11/12.
Or to state it yet another way, pick two pairs of numbers at random. The probability that the pair with the larger sum also has the larger product is 11/12. That seems more intuitive to me than the original statement.
If
a
+
d
is greater than
b
+
c
, it’s likely that
a
/
b
is greater than
c
/
d
. It seems plausible that if
a
+
d
is
much
greater than
b
+
c
, it’s
more
likely that
a
/
b
is greater than
c
/
d
. Or in terms of cross products, the more the sum of one pair is bigger than the sum of the other, the more likely the product of the former is to be greater than the latter. That is
f
(
r
) = Prob(
ad
>
bc
| (
a
+
d
)/(
b
+
c
) ≥
r
)
should be an increasing function of
r
. We know the probability above equals 11/12 when
r
= 1. We expect that the probability should approach 1 as
r
goes to infinity.
This is indeed the case, as shown in the plot below.
In particular,
f
(2) ≈ 0.99 and
f
(6) ≈ 0.999. So if
a
+
d
is two (or six) times bigger than
b +
c, there is a 0.99 (or 0.999) probability that
ad
is larger than
bc
.
You can calculate
f
(
r
) analytically or estimate it by simulation. I had Claude do both and they produce comparable results. There is a closed-form expression for
f
(
r
) but it’s really complicated.
