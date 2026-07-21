---
title: "Sum of low squares"
url: "https://www.johndcook.com/blog/2026/07/19/sum-of-low-squares/"
fetched_at: 2026-07-20T07:01:17.667457+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Sum of low squares

Source: https://www.johndcook.com/blog/2026/07/19/sum-of-low-squares/

Squares, high and low
Let
p
be an odd prime number. Then half the numbers from 1 through
p
− 1 are squares and half are not. That is, for half of numbers 1 ≤
k
<
p
, the equation
x
² =
k
mod
p
has a solution. The traditional name for these numbers is “quadratic residues” but we can just say “squares” if the context is clear. So, for example, the numbers 1, 2, and 4 are squares mod 7, and the numbers 3, 5, and 6 are not.
If
k
is a square mod
p
we will call is a
low square
if 0 ≤
k
<
p
/2 and a
high square
if
p
/2 <
k
<
p
.
Signatures
Now let
p
> 3 be an prime congruent to 3 mod 4. Add up all the low squares mod
p
and take the remainder mod
p
. Call this the signature of
p
. Here’s Python code to make this explicit.
from sympy import isprime, factorint, is_quad_residue

def signature(p):
    assert(p > 3)
    assert(isprime(p))
    assert(p % 4 == 3)
    s = 0
    for k in range(1, 1 + p//2):
        if is_quad_residue(k, p):
            s += k
    return s % p
Inverse signatures
Surprisingly, the signature of each
p
is unique. Given the signature of
p
, you can uniquely determine
p
, and in fact you can do so easily. I ran across this in a paper [1] that presented the results in the form of a parlor trick: have someone pick a prime
p
such that
p
= 3 mod 4 and ask them to compute its signature, the sum of the low squares mod
p
. Then you can quickly tell them what their choice of
p
was.
Given a signature
s
, the corresponding prime
p
is the largest prime factor of 16
s
+ 1.
Not only that,
p
= (16
s
+ 1)/
m
where
m
is the smallest of the numbers {3, 7, 11, 15} such that the fraction above is a prime number. In term of Python code, both the following functions should invert the signature of
p
.
def inverse_signature1(s):
    return max(factorint(n).keys())

def inverse_signature2(s):
    n = 16*s + 1
    for m in [3, 7, 11, 15]:
        if n % m == 0 and isprime(n // m):
            return n // m
The following code demonstrates that this is the case for numbers less than 1,000.
for n in range(7, 1000, 4):
    if isprime(n):
        s = signature(n)
        assert(n == inverse_signature1(s))
        assert(n == inverse_signature2(s))
[1] David M. Bloom. A Quadratic Residues Parlor Trick. Mathematics Magazine, Vol. 71, No. 3 (Jun., 1998), pp. 201–203.
