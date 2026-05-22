---
title: "Couth and uncouth function pairs"
url: "https://www.johndcook.com/blog/2026/05/21/couth-and-uncouth-function-pairs/"
fetched_at: 2026-05-22T07:01:12.357911+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Couth and uncouth function pairs

Source: https://www.johndcook.com/blog/2026/05/21/couth-and-uncouth-function-pairs/

“You can’t always get what you want. But sometimes you get what you need.” — The Rolling Stones
Circular functions and hyperbolic functions aren’t invertible, but we invert them anyway. These functions map many points in the domain to each point in the range, and we invert them by mapping a point in the range back to
some
point in the domain. Often this works as expected, but sometimes it doesn’t.
In the
previous post
I said
You can relate each trig function “foo” with its hyperbolic counterpart “fooh” by applying one of the functions to
iz
then multiplying by a constant
c
that depends on foo:
c
=
i
for sin and tan,
c
= 1 for cos and sec, and
c
= −
i
for csc and cot.
In symbols,
c
foo(
z
) = fooh(
iz
).
Let’s suppose foo and fooh are invertible, ignoring any complications, and solve foo(
z
) =
w
for
z
. We get
i
foo
−1
(
w
) = fooh
−1
(
cw
)
or using “arc” nomenclature for inverse functions
i
arcfoo(
w
) = arcfooh(
cw
).
When the naive calculation above holds, except possibly at a finite number of points, we say the pair (foo, fooh) is
couth
. Otherwise we say the pair is
uncouth
. These term were coined by Robert Corless and his coauthors in their paper [1].
Whether the pair (foo, fooh) is couth depends not only on foo and fooh, but also on the details of how arcfoo and arcfooh are defined.
In Python’s NumPy library, the pairs (sin, sinh) and (tan, tanh) are couth, but the pair (cos, cosh) is uncouth.
Numpy doesn’t define the reciprocal functions sec, sech, csc, csch, cot, and coth. I used to find that annoying, but I’m beginning to think that was wise. These functions cause problems. For example, there may be two reasonable ways to define these functions, one of which forms a couth pair and one of which forms an uncouth pair.
For example, how should you define cot and coth? There would be no disagreement over the definition
cot = lambda x: 1/tan(x)
but there are at least two definitions of coth that you’ll find in practice:
arccot = lambda z: 0.5*pi - arctan(z)
arccot = lambda z: arctan(1/z).
Both definitions have their advantages, but the former is uncouth while the latter is couth. You can verify that both definitions are the same at
z
= 1 but not at
z
= −1.
With the following definitions, the pairs (cos, cosh) and (sec, sech) are uncouth and the rest are couth.
from numpy import *

csc     = lambda x: 1/sin(x)
sec     = lambda x: 1/cos(x)
cot     = lambda x: 1/tan(x)
csch    = lambda x: 1/sinh(x)
sech    = lambda x: 1/cosh(x)
coth    = lambda x: 1/tanh(x)

arccot  = lambda z: arctan(1/z)
arcsec  = lambda z: arccos(1/z)
arccsc  = lambda z: arcsin(1/z)
arccoth = lambda z: arctanh(1/z)
arcsech = lambda z: arccosh(1/z)
arccsch = lambda z: arcsinh(1/z)
[1] “According to Abramowitz and Stegun” or arccoth needn’t be uncouth. Robert M. Corless
et al
. ACM SIGSAM Bulletin, Volume 34, Issue 2, pp 58 – 65 https://doi.org/10.1145/362001.362023
