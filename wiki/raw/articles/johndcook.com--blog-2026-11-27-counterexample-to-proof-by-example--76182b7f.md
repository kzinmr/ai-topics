---
title: "Counterexamples to proof by example"
url: "https://www.johndcook.com/blog/2026/11/27/counterexample-to-proof-by-example/"
fetched_at: 2026-11-28T10:00:44.577756+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Counterexamples to proof by example

Source: https://www.johndcook.com/blog/2026/11/27/counterexample-to-proof-by-example/

There are a few standard examples of statements that appear to be true for a large number of examples but eventually fail. Three that come to mind are prime generating polynomials, the Borwein integrals, and Mercer’s circle problem. I’ll go into each of these briefly before discussing an example I just recently ran across.
Prime generating polynomials
Euler discovered that
p
(
n
) =
n
² −
n
+ 41 is prime for
n
= 1, 2, 3, …, 40 but not for
n
= 41.
Another example is that
q
(
n
) =
n
² − 79
n
+ 1601 is prime for
n
= 1, 2, 3, …, 79 but not for
n
= 80.
Borwein integrals
Define
Then
B
(
n
) = π/2 for
n
= 1, 2, 3, …, 6 but not for
n
= 7, though it
almost
holds for
n
= 7. More
here
.
Moser’s circle problem
This may be the example you’re most likely to see online. Let
f
(
n
) be the maximum number of regions you can divide a circle into by drawing lines between
n
points on the circle. The first five values are
1, 2, 4, 8, 16
and so you might reasonably expect
f
(6) = 32, but in fact
f
(6) = 31.
New example
This morning I saw a
post
from @sphere_homotopy on X giving the following example. For small
n
gcd(
n
17
+ 9, (
n
+ 1)
17
+ 9) = 1.
And by “small,” I mean all
n
less than the 52-digit number
8424432925592889329288197322308900672459420460792433
Needless to say nobody discovered this by trying
n
= 1, 2, 3, … until they got to the value of
n
above. You can find an explanation of the theory behind the example
here
. The same theory can be used to create more examples, such as the following.
It appears that
gcd(n
19
+ 3, (
n
+ 1)
19
+ 3) = 1
for all
n
, and this is true for
n
< 25211925041.
