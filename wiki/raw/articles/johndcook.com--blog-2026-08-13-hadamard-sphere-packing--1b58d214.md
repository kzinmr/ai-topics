---
title: "Hadamard Codes and Sphere Packing"
url: "https://www.johndcook.com/blog/2026/08/13/hadamard-sphere-packing/"
fetched_at: 2026-08-14T10:21:52.424049+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Hadamard Codes and Sphere Packing

Source: https://www.johndcook.com/blog/2026/08/13/hadamard-sphere-packing/

Yesterday Levent Alpöge announced that he and his colleagues had discovered a new Hadamard matrix using Claude AI. That motivated a post I wrote
this morning
on how to construct Hadamard matrices. I mentioned in that post that these matrices arise in applications.
This evening I gave an example, describing how NASA used a Hadamard matrix of order 32 to transmit photos from the
Mariner 9
spacecraft in 1971. This post will give another application:
sphere packing
.
Conway and Sloane [1] give a correspondence between binary codes and sphere packings that they call Construction A. Given an (
n
,
M
,
d
) binary code
C
, center a sphere on a point
x
if and only if
x
is a congruent (mod 2) to codeword in
C
.
Here (
n
,
M
,
d
) means an error correcting code that encodes
M
bits of data as strings of
n
bits, with a minimum Hamming distance between code words of
d
, i.e. all codewords differ in at least
d
bits.
The previous post described how to create a (32, 6, 16) code by stacking a Hadamard matrix
H
of order 32 on top of −
H
and turning −1’s into 0’s. The analogous construction for a (8, 4, 4) Hadamard code gives
E
8
, the densest packing in ℝ
8
.
We start with the Hadamard matrix
and obtain the matrix
whose centers form the sphere packing.
This doesn’t look like the E8 sphere packing as it is usually presented, but it’s isomorphic.
[1] J. H. Conway and N. J. A. Sloane. Sphere Packings, Lattices and Groups. Springer. 1999.
