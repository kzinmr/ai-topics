---
title: "How NASA’s Mariner 9 probe encoded images"
url: "https://www.johndcook.com/blog/2026/08/13/mariner-hadamard/"
fetched_at: 2026-08-14T10:21:52.744922+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# How NASA’s Mariner 9 probe encoded images

Source: https://www.johndcook.com/blog/2026/08/13/mariner-hadamard/

NASA set Mariner 9 to photograph Mars in 1971. The images had to be encoded for transmission using an error-correcting code, otherwise they would be significantly corrupted when they were received on Earth.
The images were encoded for transmission using a code based on Hadamard matrices, specifically a (32, 6, 16) Hadamard code. This means that each 6-bit pixel value was encoded as a 32-bit code word, with all code words differing in at least 16 positions.
The
previous post
explained a way to construct Hadamard matrices of order 2
n
. Use this process to create a 32 × 32 Hadamard matrix
H
and create a 64 × 32 matrix
M
by stacking
H
on top of −
H
. Then form a matrix
M
′ by changing all the −1 entries to 0. The rows of
M
′ are the code words.
For a 6-bit photo pixel value, one of the bits determines whether to read a code word from the top half or bottom half of
M
′. The other five bits determine which row to choose.
So a pixel is transmitted as a 32-bit codeword
c
, one of the 64 rows of
M
′. Ideally
c
would be received, but possibly some corrupted versions
c
′ is received with some of bits flipped.
Replace all the 0’s in
c
′ with −1 to create
c
″. Now multiply
M
by
c
″, thinking of the latter as a column vector. This yields a column vector of length 64. The largest component of this vector corresponds to the row of
M
′ that was most likely sent.
To see this, suppose there was no corruption:
c
was transmitted and
c
was received. Then the product
M
c
″ has a 32 in the entry corresponding to
c
and zeros everywhere else. If no more than 7 bits in
c
were corrupted, the row with the largest entry corresponds to the row that was transmitted.
In practice the product
M
c
″ can be computed using an algorithm analogous to the FFT using fewer operations than it would take to multiply a general 64 × 32 matrix by a 32 × 1 matrix.
