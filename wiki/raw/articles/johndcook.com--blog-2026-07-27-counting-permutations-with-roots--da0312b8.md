---
title: "Counting permutations with roots"
url: "https://www.johndcook.com/blog/2026/07/27/counting-permutations-with-roots/"
fetched_at: 2026-07-28T10:08:50.523744+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Counting permutations with roots

Source: https://www.johndcook.com/blog/2026/07/27/counting-permutations-with-roots/

My post from
yesterday
on permutation roots ends with a Mathematica code for finding the probability that a permutation of
n
elements has a
k
th root. This is done by finding the coefficient of
x
n
in the generating function
I wanted to say more about this, and look at implementing the same code in SymPy. I was curious how well SymPy would do because I’ve noticed that LLMs often generate SymPy code since it’s an open source
CAS
.
Wilf [1] describes the infinite product above as the exponential generating function (egf) of
f
(
n
,
k
), the number of permutations of
n
objects that have a
k
th root. Since egfs have a
n
! term in the denominator, this is also the ordinary generating function (ogf) of the
probability
that a randomly chosen permutation on
n
objects has a
k
th root.
My first attempt at using Mathematica to probe the generating function was
expq[x_, q_] := MittagLefflerE[q, x^q]	 
p[n_, k_] :=  SeriesCoefficient[	 
    Product[expq[x^m/m, GCD[m, k]], {m, 1, Infinity}], {x, 0, n}]
This hung forever when I tried to use it on a small example. I realized, but apparently Mathematica did not, that
Infinity
could be replaced by
n
since terms higher than
n
do not contribute to the coefficient of
x
n
. With that change, the code ran quickly.
This morning I tried converting the Mathematica code to Sympy; Claude did this in one shot. I also reproduced the table of
f
(
n
,
k
) values on page 150 of [1] to test the code. Since Wilf tabulated
f
(
n
,
k
), not
f
(
n
,
k
)/
n
!, I multiplied the results by
n
!.
Here is the output:
k = 2 [1, 1, 3, 12, 60, 270, 1890, 14280, 128520, 1096200]
k = 3 [1, 2, 4, 16, 80, 400, 2800, 22400, 181440, 1814400]
k = 4 [1, 1, 3, 12, 60, 270, 1890, 13020, 117180, 1039500]
k = 5 [1, 2, 6, 24, 96, 576, 4032, 32256, 290304, 2612736]
k = 6 [1, 1, 1, 4, 40, 190, 1330, 8680, 52920, 340200]
k = 7 [1, 2, 6, 24, 120, 720, 4320, 34560, 311040, 3110400]
and here is the SymPy code. I edited the main but the rest is verbatim from Claude.
from sympy import symbols, gcd, factorial, Rational, S

x = symbols('x')

def expq_coeffs(m, q, n):
    """
    Truncated (degree <= n) series coefficients of
        expq(x**m/m, q) = MittagLefflerE(q, (x**m/m)**q)
    Since q is a positive integer:
        E_q(y^q) = sum_j y^(q*j) / (q*j)!
    with y = x**m/m, so the term of degree m*q*j has coefficient
        1 / ( m**(q*j) * (q*j)! ).
    Returns a list c[0..n] of coefficients.
    """
    c = [S.Zero] * (n + 1)
    j = 0
    while m * q * j <= n:
        deg = m * q * j
        c[deg] += Rational(1, m**(q * j) * factorial(q * j))
        j += 1
    return c

def poly_mult_trunc(a, b, n):
    """Multiply two series (lists of coeffs, index = degree) truncated to degree n."""
    c = [S.Zero] * (n + 1)
    for i, ai in enumerate(a):
        if ai == 0:
            continue
        max_j = n - i
        for j2 in range(max_j + 1):
            bj = b[j2]
            if bj != 0:
                c[i + j2] += ai * bj
    return c

def p(n, k):
    """
    SymPy equivalent of:
        expq[x_, q_] := MittagLefflerE[q, x^q]
        p[n_, k_] := SeriesCoefficient[
            Product[expq[x^m/m, GCD[m, k]], {m, 1, n}], {x, 0, n}]
    """
    result = [S.Zero] * (n + 1)
    result[0] = S.One
    for m in range(1, n + 1):
        q = gcd(m, k)
        factor = expq_coeffs(m, q, n)
        result = poly_mult_trunc(result, factor, n)
    return result[n]

# example
if __name__ == "__main__":
    for k in range(2, 8):
        print("k =", k, [factorial(n)*p(n, k) for n in range(1,11)])
[1] Herbert Wilf. Generatingfunctionology. Available online
here
.
