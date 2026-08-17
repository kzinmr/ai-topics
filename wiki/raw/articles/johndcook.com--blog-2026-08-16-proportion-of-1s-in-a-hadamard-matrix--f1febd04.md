---
title: "Proportion of 1s in a Hadamard matrix"
url: "https://www.johndcook.com/blog/2026/08/16/proportion-of-1s-in-a-hadamard-matrix/"
fetched_at: 2026-08-17T10:30:54.733759+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Proportion of 1s in a Hadamard matrix

Source: https://www.johndcook.com/blog/2026/08/16/proportion-of-1s-in-a-hadamard-matrix/

The
first post
in the recent series of posts on Hadamard matrices describes a way of constructing new Hadamard matrices from two other Hadamard matrices by taking their
Kronecker product
.
Starting with a Hadamard matrix
H
0
and a Hadamard matrix
G
, you can construct a sequence of Hadamard matrices by
H
n
+1
=
G
⊗
H
n
for  positive integers
n
. This is known as the generalized Sylvester method.
Let
p
n
be the proportion of 1s in
H
n
and let
q
be the proportion of 1s in
G
. Then you can show that the recurrence holds
p
n
+1
=
q
p
n
+ (1 −
q
)(1 −
p
n
).
You can solve the recurrence to show that
lim
n
→ ∞
p
n
= ½
and so as the iterations proceed, the ratio of number of 1s to the number of −1s approaches 1.
This doesn’t say anything Hadamard matrices in general, but it does apply to all Hadamard matrices created by repeatedly applying the generalized Sylvester method.
If you set
G
and
H
equal to the matrix
then
p
0
=
q
= ¾. Then for
n
= 1, 2, 3, …, 8 the values of
p
n
are
0.625
0.5625
0.53125
0.515625
0.5078125
0.50390625
0.501953125
0.5009765625.
