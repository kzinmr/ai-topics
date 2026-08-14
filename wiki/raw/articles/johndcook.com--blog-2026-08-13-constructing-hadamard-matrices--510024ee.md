---
title: "Constructing Hadamard matrices"
url: "https://www.johndcook.com/blog/2026/08/13/constructing-hadamard-matrices/"
fetched_at: 2026-08-14T10:21:52.680222+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Constructing Hadamard matrices

Source: https://www.johndcook.com/blog/2026/08/13/constructing-hadamard-matrices/

A Hadamard matrix is an orthogonal matrix whose entires are all either 1 or − 1. For example
is a Hadamard matrix of order 2. True to
Stigler’s law of eponymy
, James Joseph Sylvester investigated Hadamard matrices before Jacques Hadamard. Sylvester saw how to bootstrap the example above into more examples. If
H
is a Hadamard matrix, then the
partitioned matrix
Sylvester’s construction can be generalized as follows. If
H
m
is a Hadamard matrix of order
m
and
H
n
is a Hadamard matrix of order
n
, the the Kronecker product
H
m
⊗
H
n
is a Hadamard matrix of order
mn
. That is, you can form a new Hadamard matrix by taking the matrix
H
m
and replacing ±1 with the matrix ±
H
n
.
Let
S
be the set of all possible Hadamard matrix orders. By the construction above, this set is closed under multiplication. Since 2 is in
S
, every power of 2 is in
S
. Hadamard proved that all
n
≥ 4 in
S
are multiples of 4. That is, the condition 4 |
n
is necessary. He conjectured that it was also sufficient, though that has not been proven.
So the big question is what is the set
S
. Is there some multiple of 4 not in S? Until that question is answered, what is the smallest multiple of 4 not
known
to be in
S
? Hadamard matrices are useful in applications, so
constructing Hadamard matrices of various orders is useful
even while Hadamard’s conjecture remains open. For example, see the
next post
for how NASA used Hadamard matrices to transmit photographic images back from Mars.
Paley’s method
Raymond Paley came up with a way of constructing Hadamard matrices of size
q
+ 1 if
q
is a prime power congruent to 3 mod 4, and of size 2(
q
+ 1) if
q
is a prime power congruent to 1 mod 4. Let’s see what we can squeeze out of this.
If
p
is a prime congruent to 1 mod 4, every power of
p
is also congruent to 1 mod 4, and so there exist Hadamard matrices of order 2(
p
k
+ 1) for every
k
.
If
p
is a prime with
p
= 3 mod 4, then even powers of
p
are congruent to 1 mod 4 and odd powers of
p
are congruent to 3 mod 4. So there are Hadamard matrices of order 2(
p
2
k
+ 1) and of order
p
2
k
+1
+ 1.
Let’s run a script to see what we can learn from this.
from sympy import primerange

s = set()

for p in primerange(20):
    if p % 4 == 1:
        s.update([2*(p**k + 1) for k in range(1, 10)])
    if p % 4 == 3:
        s.update([2*(p**(2*k) + 1) for k in range(1, 6)])
        s.update([p**(2*k + 1) + 1 for k in range(1, 6)])
print(sorted(s)[:20])
This prints
12, 20, 28, 36, 52, 100, 164, 244, 252, 340]
We can add 16 to the list because it’s a power of 2, and we can add 24 because it’s 2 × 12, etc. But there doesn’t seem to be any way to get 44. There
is
a way to create a Hadamard matrix of order 44, but it doesn’t follow from anything we’ve seen so far.
New records
I have a book published in 1996 that says Hadamard’s conjecture had been verified for
n
up to 428. Until yesterday, the smallest multiple of 4 for which nobody had found a corresponding Hadamard matrix was 668. Then Levent Alpöge announced that he and his and collaborators found an example of size 668 and filled in all remaining gaps below 2000.
So now the set
S
is known to contain {1, 2, 4, 8, 12, 16, …, 2000}. It also contains all orders that can be obtained by Paley’s method and other methods. And it contains all products of its elements. But it is not yet known to contain 2004.
Related posts
