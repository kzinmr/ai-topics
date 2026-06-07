---
title: "Mr. Bessel’s eponymous functions"
url: "https://www.johndcook.com/blog/2026/06/05/mr-bessels-eponymous-functions/"
fetched_at: 2026-06-07T07:01:35.647881+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Mr. Bessel’s eponymous functions

Source: https://www.johndcook.com/blog/2026/06/05/mr-bessels-eponymous-functions/

Yesterday I wrote a post showing that the trapezoid rule evaluates the integral
very efficiently. But how do we know what the exact integral is for comparison? If you ask Mathematica, it will tell you the integral equals −2π
J
1
(1) where
J
1
is a Bessel function. This may seem like rabbit out of a hat, but it’s actually a simple calculation given the integral definition of Bessel functions:
Since cosine is even, we can write our integral over [−π, π] as twice the integral over [0, π]. Then a change of variables turns this into the definition of
J
n
(
z
) with
n
= 1 and
z
= 1.
A deeper question is what have we accomplished by just giving a new name to essentially the same problem we started with. Another question is why in the world are Bessel functions defined as above.
As for what we’ve accomplished, we’ve related out integration problem to a very well-studied function. Bessel functions have been studied for two centuries and it’s easy to find software to evaluate them. Even the usually minimalist command line calculator
bc
has a function
j(x, n)
for evaluating
J
n
(
x
) for integer values of
n
. We could calculate our integral to 50 decimal places as follows.
~$ bc -l
>>> scale = 50
>>>  -8*a(1)*j(1,1)
-2.76491937476833705153256665538788207487495025542883
Note that
bc
doesn’t have a value of π built in, but
a(x)
evaluates the arctangent function, and π = 4 arctan(1).
There are multiple ways of defining Bessel functions. The three main ways would be in terms of their power series, in terms of the differential equations they solve, and in terms of their integral representation. Friedrich Bessel defined what we now call Bessel functions of the first kind, the
J
n
functions, in terms of their integral representations.
Why did Bessel care about these integrals? They came out of his calculations in celestial mechanics. One example of this is solving
Kepler’s equation
with Fourier series; the Fourier coefficients are given by Bessel functions. This is worked out in detail in the
next post
.
Bessel functions had occurred in applications before Mr. Bessel drew attention to them. The functions are named after him because he was the first to systematically study them.
Mathematics is developed inductively but taught deductively. It’s common for things to be kicked around for years before someone decides they deserve a name and systematic study. See this post on the
central limit theorem
for another example. The CLT is older than the Gaussian distribution, even older than Gauss.
Related posts
