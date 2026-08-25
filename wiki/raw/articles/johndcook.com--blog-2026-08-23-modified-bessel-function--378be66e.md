---
title: "What exactly is modified about a modified Bessel function?"
url: "https://www.johndcook.com/blog/2026/08/23/modified-bessel-function/"
fetched_at: 2026-08-24T10:32:19.842119+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# What exactly is modified about a modified Bessel function?

Source: https://www.johndcook.com/blog/2026/08/23/modified-bessel-function/

Special functions often have arcane names that not very helpful without some context. The
previous post
goes into some reasons for this. This post will expand on a point at the end of the post about “modified” functions.
Things are given their names for reasons. Discovering those reasons may help you understand their motivation and use.
Pure math perspective
For each integer
n
, the modified Bessel function
I
n
is essentially the Bessel function
J
n
evaluated along the imaginary axis. Specifically,
From a certain shallow perspective, that’s the end of the story: modified Bessel functions are modified in the sense that the argument is multiplied by
i
. And there’s a fiddly constant term up front for no apparent reason.
But of course that’s not the end of the story or else this wouldn’t be worth an entire post.
The equation above is analogous to the relationships between circular and hyperbolic functions
These relationships are interesting because the circular and hyperbolic functions are independently meaningful. If you view these equations merely as definitions you lose their significance. Circular and hyperbolic functions were widely used before Euler discovered the connection between them.
Similarly, there’s a reason the modified Bessel functions were given a name their own. If you were led to Bessel functions and modified Bessel functions separately by different applications, you would regard the equation
as a
discovery
rather than just a definition. The following section explains why someone would be interested in modified Bessel functions.
Before we move on, I’d like to explain the reason for the term
i
−
n
term. In general
for all real ν. The reason for the exp(νπ
i
/2) term is that it makes
I
ν
(
x
) real for all real
x
.
Applied math perspective
Bessel functions often arise from solving problems with
radial symmetry
. Solving the
wave equation
in cylindrical coordinates using separation of variables leads to Bessel’s differential equation
and its solutions
J
n
and
Y
n
, Bessel functions of the first and second kind.
Solving the
heat equation
in cylindrical coordinates with separation of variables leads to the
modified
Bessel equation
and its solutions
I
n
and
K
n
, the
modified
Bessel functions of the first and second kind.
This is the reason behind the complex analysis perspective above: the change of variables sending
x
to
ix
changes the sign of the
x
² term in Bessel’s equation.
Bessel functions describe radially symmetric
oscillations
, such as the vibrations of a drum head. Modified Bessel functions describe radially symmetric
exponential
growth or decay [1], such as in the heat in a cylinder.
Other modified functions
Struve functions
are closely related to Bessel functions. The (modified) Struve functions also satisfy Bessel’s (modified) differential equation, but with a non-zero right hand side. The modified Struve functions are proportional to the unmodified Struve functions evaluated along the imaginary axis, with a proportionality constant that makes the modified Struve functions real for real arguments.
There’s a similar relationship between the
Mathieu functions
and modified Mathieu functions. The general pattern is that “modified” in the context of special functions means “evaluated at
ix
and multiplied by a constant to make the function real for real arguments.”
[1] The functions
I
n
grow exponentially and the functions
K
n
decay exponentially. For this reason,
A&S
didn’t tabulate
I
n
and
K
n
per se. Instead it tabulated
e
−
x
I
n
and
e
x
K
n
because these functions varied less over their range.
