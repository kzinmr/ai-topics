---
title: "Distinguishing variables from parameters"
url: "https://www.johndcook.com/blog/2026/06/30/variables-and-parameters/"
fetched_at: 2026-07-01T07:00:52.779150+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Distinguishing variables from parameters

Source: https://www.johndcook.com/blog/2026/06/30/variables-and-parameters/

Imagine the following dialog.
Professor
:
f
is a function of a real variable
x
that takes a real parameter
k
.
Student
: What’s a parameter?
Professor
: It’s a constant that can vary.
Student
: Then if it can vary, isn’t it a variable?
Professor
: Sorta, but no not really.
This conversation plays out over and over, and unfortunately it often ends as it does above, with the student confused. Here’s how I believe the conversation should continue.
Professor
: You’re absolutely right that
f
is a function of two variables,
x
and
k
. But usually
k
is fixed in the context of a specific application and
x
is not. A different application might have a different, but also fixed, value of
k
. So it is helpful to think of
f
(
x
;
k
), a function of
x
with a parameter
k
, rather than
f
(
x
,
k
), a function of two variables. The former carries more information, giving a hint as to how the numbers are used.
Is there really a difference between a parameter and a variable? In a reductionistic sense, no. But in a practical sense, yes, absolutely.
It might sound pedantic to distinguish a variable from a parameter, and it is, in the best sense of the word. Pedant literally means teacher. Usually
pedantic
carries a negative connotation, such as making a distinction without a difference. But here the pedant would be making a helpful distinction.
For example, we might write a probability density function as
f
(
x
; μ, σ). The function gives the probability density at a point
x
. The density depends on parameters μ and σ, and these parameters change between applications, but for a given application they have fixed values.
You find the probability of a random variable taking on values in an interval [
a
,
b
] by integrating
f
over that interval. When I say that, you know that I mean you’d integrate with respect to
x
, because
f
is a function of
x
. It is also, in an abstract sense, a function of μ and σ, but it’s typically not useful to think of it that way.
Hypergeometric functions have two sets of parameters, and so you may see two semicolons, such as
f
(
x
;
a
,
b
;
c
). This denotes a function of the variable
x
, with upper parameters
a
and
b
, and a lower parameter
c
. In some abstract sense this is a function of four variables, but it acts very differently with respect to
x
than with respect to
a
,
b
, and
c
. There’s also a difference between
a
and
b
on the one hand an
c
on the other, one worth paying attention to, though it is less of a difference than between
x
and the parameters collectively.
Sometimes you’ll see a vertical bar rather than a semicolon to separate variables from parameters. This works out even better for probability densities because then
f
(
x
| μ, σ) suggests the probability density of
x
given
μ and σ since the vertical bar is also used for conditional probability. You might also see
f
(
x
|
a, b;
c) for hypergeometric functions, with the vertical bar separating variables from parameters and the semicolon separating two kinds of parameters.
When I first saw a semicolon separating variables from parameters, no explanation was given, and I figured I could mentally replace the semicolon with a comma. Then later I realized that the semicolon was an act of kindness by the author giving the reader additional information.
