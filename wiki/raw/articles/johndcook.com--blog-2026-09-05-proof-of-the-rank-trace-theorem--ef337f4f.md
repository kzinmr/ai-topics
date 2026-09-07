---
title: "Proof of the rank-trace theorem"
url: "https://www.johndcook.com/blog/2026/09/05/proof-of-the-rank-trace-theorem/"
fetched_at: 2026-09-06T10:01:20.834090+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Proof of the rank-trace theorem

Source: https://www.johndcook.com/blog/2026/09/05/proof-of-the-rank-trace-theorem/

The
previous post
discussed the motivation for and application of the rank-trace theorem. This post will give a proof.
Suppose
A
is a real symmetric matrix. The rank-trace inequality says
where tr is the trace operator, the sum of the elements along the diagonal of the matrix.
Terse proof
Here’s the proof in a nutshell: diagonalize
A
and use the Cauchy-Schwarz inequality.
Detailed proof
Now let’s unpack that. Any real symmetric matrix
A
is similar to a matrix
D
with the eigenvalues of
A
along the diagonal.
The trace of a matrix stays the same under a similarity transformation, i.e. multiplying by
P
on one side and its inverse on the other side. So without loss of generality we may as well assume
A
is diagonal.
The rank of a matrix equals the number of non-zero eigenvalues, so a vector containing the non-zero eigenvalues of
A
has length
r
where
r
is the rank of
A
. Define
w
to be the vector of dimension
r
consisting of all 1’s.
Then by the Cauchy-Schwarz inequality we have
Cyclic trace property
Why should a matrix
A
and its diagonalization
D
have the same trace?
The trace of a matrix product
AB
equals the trace of the product
BA
. To prove this, write out matrix products and the traces, then note that the two expressions are equal.
Therefore
More generally, trace has the cyclic property
However, not all permutations preserve the trace. For example, let
Then
but
