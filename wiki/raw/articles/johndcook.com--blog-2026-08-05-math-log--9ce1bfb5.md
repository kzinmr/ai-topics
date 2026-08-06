---
title: "The code that didn’t break"
url: "https://www.johndcook.com/blog/2026/08/05/math-log/"
fetched_at: 2026-08-06T10:18:24.081181+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# The code that didn’t break

Source: https://www.johndcook.com/blog/2026/08/05/math-log/

Last week I wrote a
post
on hiding cryptographic keys in decks of cards. I wrote some code for that post that shouldn’t work, but before fixing I noticed that it in fact did work.
The code computes logarithms for integers larger than the largest representable float. For example, the largest float is on the order of 10
308
, and yet the following code works.
>>> import math
>>> math.log10(10**400)
400.0
The
log
,
log2
, and
log10
functions have some code inside that handles large integers specially. It doesn’t simply convert the integers to floats before taking the logarithm. If it did, it would overflow.
While playing around with this I also noticed that you can define floats larger than the largest float without warnings.
>>> math.log(1e308)
709.1962086421661
>>> math.log(1e309)
inf
This isn’t a feature of
math.log
but of how Python handles scientific notation. The expression
1e308
is the floating point representation of 10
308
. It is a float, not an int.
>>> type(1e308)
<class 'float'>
The expression
1e309
is also a float. But since it’s larger than is possible for a float, Python interprets it as
inf
. The code
math.log(1e309)
returns
inf
based on the reasoning that log(∞) = ∞.
That explains the following behavior:
>>> 1e309 == 1e310
True
The expressions
1e309
and
1e310
are equal because both are alternate ways of writing
inf
.
