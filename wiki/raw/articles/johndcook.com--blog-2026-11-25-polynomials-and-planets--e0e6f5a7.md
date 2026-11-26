---
title: "Polynomials and Planets"
url: "https://www.johndcook.com/blog/2026/11/25/polynomials-and-planets/"
fetched_at: 2026-11-26T10:00:51.326935+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Polynomials and Planets

Source: https://www.johndcook.com/blog/2026/11/25/polynomials-and-planets/

A couple days ago
I wrote about how the force of gravity varies over the surface of an oblate planet. Earth is slightly oblate,
i
.
e
., it has an equatorial bulge, and this oblateness has a significant effect on satellite orbits. More on that
here
.
The fictional planet Mesklin in Hal Clement’s novel
Mission of Gravity
is extremely oblate due to its rapid rotation, and apparent gravity varies by two orders of magnitude between the equator and the poles. As science fiction authors often do, Clement took some aspect of familiar experience and exaggerated it to make it easier to appreciate.
The gravitational potential of an oblate spheroid as a function of the polar angle θ is proportional to
1 −
J
2
P
2
(cos θ)
where
P
2
is the second Legendre polynomial. There are more terms of the form
J
2
n
P
2
n
(cos θ)
but the most significant term is the one with coefficient
J
2
, hence the
J2 effect
.
I learned about Legendre polynomials long before I learned about gravity calculations, and so my first reaction when seeing the result above would be that gravitational calculations are another example of places where Legendre polynomials pop up. While this is true, it’s historically backward. Legendre discovered the polynomials that now bear his name
because
they came up in his gravitational calculations.
It would be more historically informed to say that the polynomials falling out of Legendre’s exploration of gravity have found applications elsewhere, and often for the same reasons: because they fall out of calculations involving radial symmetry. That’s why they appear in E&M, acoustics, and quantum mechanics.
Legendre polynomials also appear in applications that have nothing to do with radial symmetry. For example, the most common form of Gaussian quadrature is based on Legendre polynomials. More on that
here
.
