---
title: "Real and imaginary parts"
url: "https://www.johndcook.com/blog/2026/05/23/real-and-imaginary-parts/"
fetched_at: 2026-05-24T07:01:05.608337+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Real and imaginary parts

Source: https://www.johndcook.com/blog/2026/05/23/real-and-imaginary-parts/

The previous post announced some
notes
I wrote up based on an article by Henry Baker implementing functions of a complex variable in terms of functions of a real variable. That is, it finds functions
u
(
x
,
y
) and
v
(
x
,
y
) such that
f
(
x
+
iy
) =
u
(
x
,
y
) +
i
v
(
x
,
y
)
where
x
,
y
,
u
, and
v
are all real-valued. Not only that, but if
f
is an elementary function, so are
u
and
v
. Here “elementary” has a technical meaning, but essentially it means functions that you could evaluate on a scientific calculator. A couple of the functions might be unfamiliar, such as sgn and atan2, but there are no functions like the gamma function that are defined in terms of integrals.
One application of Baker’s equations would be to bootstrap a math library that doesn’t support complex numbers into one that does. But the equations could be useful in pure math when you’d like to have a convenient expression for the real or imaginary part of a function.
The real and imaginary parts of a complex analytic function are harmonic functions. So the functions on the right hand side of Baker’s equations satisfy
Laplace’s equation
:
u
xx
+
u
yy
= 0
and
v
xx
+
v
yy
= 0.
Furthermore, the functions
u
and
v
form harmonic conjugate pairs, meaning each is the
Hilbert transform
of the other.
