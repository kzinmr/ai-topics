---
title: "Compressing a Hadamard matrix"
url: "https://www.johndcook.com/blog/2026/08/15/compressing-a-hadamard-matrix/"
fetched_at: 2026-08-16T10:14:41.253846+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Compressing a Hadamard matrix

Source: https://www.johndcook.com/blog/2026/08/15/compressing-a-hadamard-matrix/

Hadamard matrices are in the news following the recent announcement of a newly discovered Hadamard matrix. I’ve written three posts on Hadamard matrices recently, one as a sort of
introduction
and two on applications: the error correcting code used in the
Mariner 9
probe and constructing
sphere packings
.
A Hadamard matrix is an orthogonal matrix with all entries equal to ±1. Jacques Hadamard conjectured that there exist Hadamard matrices of order 4
n
for all positive integers
n
. It’s necessary that the order be divisible by 4, and Hadamard conjectured that this is sufficient [1].
How could you compactly represent a Hadamard matrix? Since the entries are all either 1 or − 1 each entry could be represented by a single bit, and
n
² bits could store an
n
×
n
Hadamard matrix. But we can do better.
Methodical matrices
If the matrix can be produced by an algorithm, you only need to store the name of the algorithm and the argument to the algorithm. So, for a 1024 × 1024 matrix applied by iterating Sylvester’s algorithm could be stored by saying “Apply Sylvester’s algorithm 10 times” rather than storing a megabyte of data.
Paley’s method can create a Hadamard matrix corresponding to every prime power. So you could determine a Paley type matrix by storing the prime and the exponent.
Next in complexity would be hybrid algorithms, such as start with the Paley method applied to 37
6
and then apply Sylvester’s method 3 times.
There are more methods of creating Hadamard matrices than Sylvester’s method and Paley’s method, though they’re harder to describe and parameterize.
Sporadic matrices
If a Hadamard matrix cannot be constructed using an algorithm, you can still store the matrix in fewer than
n
² bits. Since the rows are orthogonal, the last row of the matrix is determined by all the previous rows, up to sign. So you could store a Hadamard matrix using
n
(
n
− 1) + 1 bits.
Some Hadamard matrices are symmetric or skew. A symmetric matrix is determined by its diagonal and the elements above the diagonal. So a symmetric Hadamard matrix could be represented by
n
(
n
+ 1)/2 bits.
A skew Hadamard matrix isn’t quite skew-symmetric. A matrix
M
is skew symmetric if
M
T
= −
M
.
This implies the diagonal elements are 0, and Hadamard matrices cannot contain 0s. A Hadamard matrix
H
is called skew if
H
+
H
T
= 2
I
.
This implies the diagonal elements are all 1s and the elements below the diagonal have the opposite sign of the elements above the diagonal. Since the elements on the diagonal are determined, a skew Hadamard matrix can be sotred using
n
(
n
− 1)/2 bits.
Incidentally, there is a conjecture that there exist skew Hadamard matrices of order 4
n
for all positive
n
.
[1] There are Hadamard matrices of order 1 and 2, but larger orders must be divisible by 4.
