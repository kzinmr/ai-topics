---
title: "Fibonacci product"
url: "https://www.johndcook.com/blog/2026/09/16/fibonacci-product/"
fetched_at: 2026-09-17T10:01:20.145505+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Fibonacci product

Source: https://www.johndcook.com/blog/2026/09/16/fibonacci-product/

The product of four consecutive Fibonacci numbers equals the product of two consecutive integers.
For example,
3 × 5 × 8 × 13 = 39 × 40.
I ran across this theorem in a note [1] that says “The product of any four consecutive Fibonacci numbers is twice a triangular number.” Since triangular numbers have the form
n
(
n
+ 1)/2, twice a triangular number is the product of two consecutive integers.
The note also gives a way to find the numbers on the right hand side. We have
F
n
F
n
+1
F
n
+2
F
n
+3
=
m
(
m
+ 1)
where
m
equals
F
n
+1
F
n
+2
if
n
is odd and
F
n
F
n
+3
if
n
is even.
In the example at the top, 3 is the 4th Fibonacci number, so
n
= 4. Since 4 is even,
m
is the product of the 4th and 7th Fibonacci numbers, i.e.
m
= 3 × 13 = 39.
More Fibonacci posts
[1] K. B. Subramaniam. On a link between Triangular and Fibonacci numbers. The Mathematical Gazette, Vol. 103, No. 558 (November 2019), p. 489.
