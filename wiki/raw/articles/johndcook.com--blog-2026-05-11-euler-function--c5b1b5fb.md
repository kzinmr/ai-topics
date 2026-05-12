---
title: "Euler function in the context of q-series and partitions"
url: "https://www.johndcook.com/blog/2026/05/11/euler-function/"
fetched_at: 2026-05-12T07:00:48.686609+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Euler function in the context of q-series and partitions

Source: https://www.johndcook.com/blog/2026/05/11/euler-function/

This morning I wrote a
post
about the probability that a random matrix over a finite field is invertible. If the field has
q
elements and the matrix has dimensions
n
×
n
then the probability is
In that post I made observation that
p
(
q
,
n
) converges very quickly as a function of
n
[1]. One way to see that the convergence is quick is to note that
and
John Baez pointed out in the comments that
p
(
q
, ∞) = φ(1/
q
) where φ is the Euler function.
Euler was extremely prolific, and many things are named after him. Several functions are known as Euler’s function, the most common being his totient function in number theory. The Euler function we’re interested in here is
for −1 < x < 1. Usually the argument of φ is denoted “
q
” but that would be confusing in our context because our
q
, the number of elements in a field, is the reciprocal of Euler’s
q
, i.e.
x
= 1/
q
.
Euler’s identity [2] (in this context, not to be confused with other Euler identities!) says
This function is easy to calculate because the series converges very quickly. From the alternating series theorem we have
When
q
= 2 and so
x
= 1/2,
N
= 6 is enough to compute φ(
x
) with an error less than 2
−70
, beyond the precision of a floating point number. When
q
is larger, even fewer terms are needed.
To illustrate this, we have the following Python script.
def phi(x, N):
    s = 0
    for n in range(-N, N+1):
        s += (-1)**n * x**((3*n**2 - n)/2)
    return s

print(phi(0.5, 6))
Every digit in the output is correct.
Related posts
[1] I didn’t say that explicitly, but I pointed out that
p
(2, 8) was close to
p
(2, ∞).
[2] This identity is also known as the pentagonal number theorem because of its connection to
pentagonal numbers
.
