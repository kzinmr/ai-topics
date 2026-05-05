---
title: "Fibonacci sequence - a tiny, infinite(*) generator"
url: "https://iczelia.net/posts/fib/"
fetched_at: 2026-05-05T07:01:24.008194+00:00
source: "Kamila Szewczyk (iczelia)"
tags: [blog, raw]
---

# Fibonacci sequence - a tiny, infinite(*) generator

Source: https://iczelia.net/posts/fib/

Introduction
⌗
In July of 2020 was working with Ada#0132 on a small, multiprecision fibonacci sequence generator written in C. The final source code I worked out (with a bit of her golfing help - nothing can replace a fresh, sharp eye) follows:
The same algorithm can be represented a bit less concisely:
Closing thoughts
⌗
The algorithm can be optimized (mostly for speed) by setting the type of the memory array to
unsigned char
. Also, the utilisation of memory can be greatly improved (packing digits into nibbles). The initial memory size can also be extended (infinitely, or maybe even dynamically allocated). I’m open for suggestions on making it smaller (preferably, without altering the input buffer length). The goal was to make it fit inside a 160-character SMS message (but sadly, the code currently is 167 characters - it’s 7 too many).
2021 Update
⌗
A StackExchange Code Golf user
Arnauld
provides
a few more golfs
to the initial
idea
:
For each entry a[i] with i > 0, we store the i-th decimal digit of the last Fibonacci term into the bits 0 to 3 and the i-th decimal digit of the penultimate term into the bits 4 to 7. (The convention used here is that the 1st decimal digit is the least significant one). We start with all entries set to 0 except a[1] which is set to 1. For instance, in
a[1]
,
0000001
splits into nibbles
0000
and
0001
- first and only digit of
Fib(1) = 0
, and first and only digit of
Fib(2) = 1
. Each number is printed by iterating from the most significant digit to the least significant one, ignoring leading zeros and ending with a line-feed. We start with
i = 2
and
c = argc
(which is guaranteed to be greater than 0) in order to make sure that the initial 0 is printed. In order to compute the next term
Fib(n+1)
, we iterate through all values stored in
a[]
, this time from least significant to most significant. We add the last digit to the penultimate one, update each entry accordingly and keep track of the carry into c. We have
i = 9999
and
c = 0
at the end of this loop, which are the expected values to print the next number, starting from the 2nd iteration. We also end up with
s = 0
, which means that c will be re-initialized to 0 as expected before the next update.
For deeper insight, check the Arnauld’s answer linked earlier.
