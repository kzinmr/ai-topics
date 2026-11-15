---
title: "The longest polynomial level set"
url: "https://www.johndcook.com/blog/2026/11/14/erdos-lemniscate/"
fetched_at: 2026-11-15T10:00:55.836022+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# The longest polynomial level set

Source: https://www.johndcook.com/blog/2026/11/14/erdos-lemniscate/

Let
p
(
z
) be a polynomial with leading coefficient 1, i.e. a monic polynomial. What is the maximum length of the curve
{
z
: |
p
(
z
)| = 1}
for each degree n?
Erdős conjectured that the maximum length was obtained by the polynomial
p
(
z
) =
z
n
− 1. He was right, as Teng Zhang proved
recently
.
Examples
Here’s an example for degree five. The maximum length is obtained by
p
(
z
) =
z
5
− 1.
This curve has length 15.02.
Here’s the corresponding curve for
p
(
z
) =
z
5
−
z
which has length 6.909.
In general the level set {
z
: |
p
(
z
)| = 1} need not be connected, in which case the length is the sum of the lengths of the components.
Here’s an example that tweaks the constant parameter of the optimal curve
p
(
z
) =
z
5
− 1.1.
This curve has (total) length 14.59.
Details
The length of the maximum curve for given
n
is the length for the polynomial
p
(
z
) =
z
n
− 1. The only curves obtaining the maximum length are translations and rotations of this curve.
Note that for
n
= 1 the maximum curve is a circle and for
n
= 2 the curve is the lemniscate of Bernoulli. The general curve is called the Erdős lemniscate of order
n
, generalizing Bernoulli’s lemniscate.
The maximum length for given
n
is
2
1/
n
B
(1/
n
, 1/2
n
)
where
B
is the beta function.
The Erdős lemniscates look similar to the “rose” curves
r
= cos(
n
θ), but these curves are not polynomial level sets.
Related posts
