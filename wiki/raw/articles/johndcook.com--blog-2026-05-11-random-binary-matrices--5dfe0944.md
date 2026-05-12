---
title: "Probability that a random binary matrix is invertible"
url: "https://www.johndcook.com/blog/2026/05/11/random-binary-matrices/"
fetched_at: 2026-05-12T07:00:48.932322+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Probability that a random binary matrix is invertible

Source: https://www.johndcook.com/blog/2026/05/11/random-binary-matrices/

The two latest posts have involved invertible matrices with 0 and 1 entries. If you fill an
n
×
n
matrix with 0s and 1s randomly, how likely is it to be invertible?
What kind of inverse?
There are a couple ways to find the probability that a binary matrix is invertible, depending on what you mean by the inverse.
Suppose you have a matrix
M
filled with 0s and 1s and you’re looking for a matrix
N
such that
MN
is the identity matrix. Do you want the entries of
N
to also be 0s and 1s? And when you multiply the matrices, are you doing ordinary integer arithmetic or are you working mod 2?
In the previous posts we were working over GF(2), the field with two elements, 0 and 1. All the elements of a matrix are either 0 or 1, and arithmetic is carried out mod 2. In that context there’s a nice expression for the probability a square matrix is invertible.
If you’re working over the real numbers, the probability of binary matrix being invertible is higher. One way to see this is that the inverse of a binary matrix is allowed to be binary but it isn’t required to be.
Another way to see this is to look at determinants. If you think of a matrix
M
as a real matrix whose entries happen to only be 0 or 1,
M
is invertible if and only its determinant is non-zero. But if you think of
M
as a matrix over GF(2), the entries are either 0 or 1 out of necessity, and
M
is invertible if and only if its determinant,
computed in
GF(2), is non-zero. If the determinant of
M
as a real matrix is a non-zero even number, then
M
is invertible as a real matrix but not as a matrix over GF(2).
Probability of invertibility in GF(2)
Working over GF(2), what is the probability that a random matrix is invertible? Turns out it’s just as easy to answer a more general question: what is the probability that a random
n
×
n
matrix over GF(
q
), a finite field with
q
elements, is invertible? This is
When
q
= 2 and
n
= 8 this probability is 0.289919. The probability is roughly the same for all larger values of
n
, converging to approximately 0.288788 as
n
→ ∞.
Probability of invertibility in ℝ
What is the probability that an 8 × 8 matrix with random 0 and 1 entries is invertible as a real matrix? We can estimate this by simulation.
import numpy as np

def simulate_prob_invertible_real(n, numreps=1000):
    s = 0
    for _ in range(numreps):
        M = np.random.randint(0, 2, size=(n, n))
        det = np.linalg.det(M)
        if abs(det) > 1e-9:
            s += 1
    return s/numreps
When
n
= 8, I got 0.5477 when running the code with 10,000 reps.
When
n
= 32, I got a probability of 1. Obviously it is possible for a 32 × 32 binary matrix to be singular, but it’s very unlikely: it didn’t happen in 10,000 random draws.
