---
title: "Spot checking polynomial identities"
url: "https://www.johndcook.com/blog/2026/05/30/schwartz-zippel/"
fetched_at: 2026-05-31T07:01:05.683929+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Spot checking polynomial identities

Source: https://www.johndcook.com/blog/2026/05/30/schwartz-zippel/

If a polynomial identity holds at a few random points, it’s very like true. We’ll make this statement more precise, but first let’s look at some applications.
You may want to test an identity that naturally presents itself as a statement that two polynomials are equal. Or you might use something like
the binomial coefficient trick
to reframe a problem isn’t obviously an identity about polynomials. And with algebraic circuits, you can reformulate a wide range of computations as polynomial identities; this is widely used in zero-knowledge proofs.
The theorem alluded to at the top of the post is the Schwartz-Zippel lemma. It is formulated in terms of the probability of a non-zero polynomial
P
evaluating to zero. To prove that two polynomials
Q
1
and
Q
2
are equal, you can show that
P
= Q
1
(
x
) −
Q
2
(
x
) = 0.
Schwartz-Zippel lemma
Let
F
be a (typically large) finite field and let
P
be a non-zero polynomial in
n
variables
P
(
x
1
,
x
2
,
x
3
, …,
x
n
)
of total degree
d
. If we choose the
x
‘s randomly from
F
then the probability that
P
evaluates to zero is no more than
d
/|
F
|. [1]
If the total degree
d
is small relative to the size of the field, then the probability of
P
evaluating to zero is small. As long as
d
is less than |
F
|, you can evaluate the polynomial
k
times to make
(
d
/ |
F
|)
k
as small as you’d like. If
d
isn’t too large, and
F
is large, like the integers mod
p
= 2
255
− 19 used in cryptography, one polynomial evaluation might be enough to give convincing evidence that the polynomial is zero.
[1] The Schwartz-Zippel lemma in its full generality applies to polynomials over an integral domain
R
with variables drawn from
S
, a finite subset of
R
. Here we’re setting
R
=
S
=
F
.
