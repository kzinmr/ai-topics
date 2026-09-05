---
title: "Computing a lower bound on matrix rank"
url: "https://www.johndcook.com/blog/2026/09/04/stable-rank/"
fetched_at: 2026-09-05T10:00:48.793907+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Computing a lower bound on matrix rank

Source: https://www.johndcook.com/blog/2026/09/04/stable-rank/

Suppose you want to know the rank of an
n
×
n
matrix
A
, the number of linearly independent rows of
A
, or equivalently the number of linearly independent columns. There are at least three difficulties.
Difficulties in computing rank
First of all, rank is not a continuous function of a matrix. Since rank is an integer, an arbitrarily small change in the matrix could cause a discrete change in the rank [1]. A small error in computing
A
could produce a matrix with a different rank.
Second, finding the rank takes
O
(
n
³) operations, which may or may not be an issue depending on context.
Third, you may not have the matrix
A
in an explicit form. Maybe you’re able to compute products
Av
for vectors
v
but it’s not practical to form the entire matrix
A
.
Rank-trace inequality
If you don’t need to know the rank of
A
per se, but only need to know whether it is above a certain size, a lower bound on the rank may enough.
Suppose
A
is a Hermitian matrix. If
A
is real, this means
A
is symmetric. If
A
is complex, this means
A
equals its conjugate transpose. Then the rank-trace inequality says
The quantity on the right hand side is known as the
stable rank
of
A
. It’s not a rank in any algebraic sense, but it gives a lower bound on rank. And it solves the three problems listed above.
Stability
First of all, trace
is
a continuous function of a matrix, and so stable rank is also a continuous function of a matrix, provided the denominator isn’t zero. A small change to a matrix only makes a small change to its stable rank. That’s why stable rank is called stable.
Efficiency
Second, although computing rank takes
O
(
n
³) operations, computing stable rank takes only
O
(
n
²) operations, though this isn’t immediately obvious.
The trace of
A
takes
n
operations: simply sum the elements on the diagonal of
A
. But how do you take the trace of
A
²? Squaring
A
takes
n
³ operations, and so if you had to square
A
to find the trace of
A
² the rank-trace inequality would have no efficiency advantage over finding the rank of
A
. But you can compute the trace of
A
² via
Formation
Now suppose you don’t have the matrix
A
per se but you do have a way of probing
A
, computing the product of vectors with
A
. Maybe
A
is too large to fit into memory, or explicitly computing the elements of
A
would take too long.
There are Monte Carlo algorithms for estimating the traces of
A
and
A
² that could be used together to estimate the stable rank of
A
.
Demonstration
The following Python code illustrates the discussion above.
import numpy as np

np.random.seed(20260904)
n = 5
B = np.random.randn(n, n)
A = B.T @ B + 1e-8 * np.eye(n)  # Gram matrix plus a tiny shift => SPD

rank_A = np.linalg.matrix_rank(A)
tr_A = np.trace(A)
tr_A2 = np.trace(A @ A) # matrix product 
sum_sq = np.sum(A * A) # element-by-element product
stable_rank = (tr_A ** 2) / tr_A2

print(f"A =\n{A}\n")
print(f"rank(A)              = {rank_A}")
print(f"tr(A)                = {tr_A:.12f}")
print(f"tr(A^2) direct       = {tr_A2:.12f}")
print(f"tr(A^2) indirect     = {sum_sq:.12f}")
print(f"stable rank          = {stable_rank:.12f}")
The code above produces the output below.
A =
[[ 1.09945682  0.4899665   0.98901845  0.66983113 -1.35006341]
 [ 0.4899665   0.98531254  0.35067791  0.89757603 -0.72037507]
 [ 0.98901845  0.35067791  4.31233926  0.94556225 -0.54819048]
 [ 0.66983113  0.89757603  0.94556225  1.3494295  -1.33840786]
 [-1.35006341 -0.72037507 -0.54819048 -1.33840786  3.54858332]]

rank(A)              = 5
tr(A)                = 11.295121449420
tr(A^2) direct       = 51.035447533673
tr(A^2) indirect     = 51.035447533673
stable rank          = 2.499826585688
[1] Topological argument: A map from a connected space (such as ℝ
n
×
n
) onto a discrete space (such as ℤ) cannot be continuous, otherwise the inverse images of the points in the range would partition the connected space into disjoint open sets, violating the definition of a connected space.
