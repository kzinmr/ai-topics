---
title: "Left and right shifts are pseudoinverses"
url: "https://www.johndcook.com/blog/2026/05/11/inverse-shift/"
fetched_at: 2026-05-12T07:00:48.640540+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Left and right shifts are pseudoinverses

Source: https://www.johndcook.com/blog/2026/05/11/inverse-shift/

What is the inverse of shifting a sequence to the right? Shifting it to the left, obviously.
But wait a minute. Suppose you have a sequence of eight bits
abcdefgh
and you shift it to the right. You get
0
abcdefg.
If you shift this sequence to the left you get
abcdefg
0
You can’t recover the last element
h
because the right-shift destroyed information about
h
.
A left-shift doesn’t fully recover a right-shift, and yet surely left shift and right shift are in some sense inverses.
Yesterday
I wrote a post about representing bit manipulations, including shifts, as matrix operators. The matrix corresponding to shifting right by
k
bits has 1s on the
k
th diagonal above the main diagonal and 0s everywhere else. For example, here is the matrix for shifting an 8-bit number right two bits. A black square represents a 1 and a white square represents a 0.
This matrix isn’t invertible. When you’d like to take the inverse of a non-invertible matrix, your kneejerk response should be to compute the pseudoinverse. (Technically the
Moore-Penrose pseudoinverse
. There are
other
pseudoinverses, but Moore-Penrose is the most common.)
As you might hope/expect, the pseudoinverse of a right-shift matrix is a left-shift matrix. In this case the pseudoinverse is simply the transpose, though of course that isn’t always the case.
If you’d like to prove that the pseudoinverse of a matrix that shifts right by
k
places is a matrix that shifts left by
k
places, you don’t have to compute the pseudo inverse per se: you can verify your guess.
This post
gives four requirements for a pseudoinverse. You can prove that left shift is the inverse of right shift by showing that it satisfies the four equations.
