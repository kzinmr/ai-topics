---
title: "Computing sine and cosine of complex arguments with only real functions"
url: "https://www.johndcook.com/blog/2026/03/27/complex-argument/"
fetched_at: 2026-04-30T07:02:02.190759+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Computing sine and cosine of complex arguments with only real functions

Source: https://www.johndcook.com/blog/2026/03/27/complex-argument/

Suppose you have a calculator or math library that only handles real arguments but you need to evaluate sin(3 + 4
i
). What do you do?
If you’re using Python, for example, and you don’t have NumPy installed, you can use the built-in math library, but it will not accept complex inputs.
>>> import math
>>> math.sin(3 + 4j)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: must be real number, not complex
You can use the following identities to calculate sine and cosine for complex arguments using only real functions.
The proof is very simple: just use the addition formulas for sine and cosine, and the following identities.
The following code implements sine and cosine for complex arguments using only the built-in Python functions that accept real arguments. It then tests these against the NumPy versions that accept complex arguments.
from math import *
import numpy as np

def complex_sin(z):
    x, y = z.real, z.imag
    return sin(x)*cosh(y) + 1j*cos(x)*sinh(y)

def complex_cos(z):
    x, y = z.real, z.imag
    return cos(x)*cosh(y) - 1j*sin(x)*sinh(y)

z = 3 + 4j
mysin = complex_sin(z)
mycos = complex_cos(z)
npsin = np.sin(z)
npcos = np.cos(z)
assert(abs(mysin - npsin) < 1e-14)
assert(abs(mycos - npcos) < 1e-14)
Related posts
