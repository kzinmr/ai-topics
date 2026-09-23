---
title: "Haversine law"
url: "https://www.johndcook.com/blog/2026/09/21/haversine-law/"
fetched_at: 2026-09-22T10:00:53.712907+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Haversine law

Source: https://www.johndcook.com/blog/2026/09/21/haversine-law/

Suppose you want to solve a triangle. You know two sides and the angle between them. Then you can solve for the third side using the law of cosines.
Now suppose you want to solve a
big
triangle, a triangle on the surface of the earth so large that the curvature of the earth matters. You can still use the law of cosines, but you’ll need
the spherical law of cosines
:
cos(
c
) = cos(
a
) cos(
b
) + sin(
a
) sin(
b
) cos(
C
).
If you know the (angular) lengths of sides
a
and
b
, and (tangential) angle
C
between the two sides, you can solve for
c
by taking the inverse cosine of the right hand side above.
Now suppose you want to solve this big triangle because you’re a
navigator
on a ship a couple centuries ago, doing calculations by looking up trig functions and inverse trig functions in a table. You’re interested in triangles that are so big that you have to account for the fact that you’re living on a sphere. But at the same time, your triangles are still fairly small relative to the size of the globe.
The problem with the law of cosines
The numbers
a
and
b
will often be fairly small, and so their cosines will be near 1 and their sines are near zero. So the calculation
cos(
a
) cos(
b
) + sin(
a
) sin(
b
) cos(
C
)
will add a number near 1 and a number near zero. That’s a problem.
Say you’re working with five decimal place arithmetic. Then if the second term above is less than 10
−5
, its contribution to the sum gets completely lost in the addition to the first term. If the second term is larger than 10
−5
but still small, its contribution to the sum will be partially lost.
Law of haversines
Enter the
haversine
, defined by
hav(θ) = (1 − cos(θ))/2.
The expression 1 − cos θ was called the versine, and so half of the versine is the haversine.
In terms of the haversine, the law of cosines above becomes the law of haversines:
hav(
c
) = hav(
a
−
b
) + sin(
a
) sin(
b
) hav(
C
).
Now suppose you have a table of haversines and inverse haversines. The law of haversines requires a little less work: you have one less table lookup, and you trade a product for a subtraction.
But the primary advantage is numerical accuracy: the terms on the right side have roughly the same size.
Tables
Note that we’re assuming the values in your table of haversines have been calculated correctly to the given precision. If you calculated your own values of haversines from the definition above, you’d lose precision in the subtraction 1 − cos θ, defeating the advantage of the law of haversines [1].
History
According to
Wikipedia
.
The first table of haversines in English was published by James Andrew in 1805, but Florian Cajori credits an earlier use by José de Mendoza y Ríos in 1801. The term
haversine
was coined in 1835 by James Inman.
Experiments
I ran some experiments that carried out arithmetic in float16 (11 bits of precision) to approximate what someone might have done by hand. When the difference between
a
and
b
was on the order of 1° or 0.1°, the law of cosine method often overflowed: the right-hand side evaluated to something larger than 1 even though theoretically it should be less than 1. The haversine method never overflowed.
The median error for the haversine method was a couple orders of magnitude less than that of the cosine method.
Related posts
[1] hav(θ) = (1 − cos(θ))/2 = sin²(θ/2). If you calculated hav θ by looking up sin(θ/2) and squaring it, you’d be doing extra work, but you wouldn’t have numerical problems.
