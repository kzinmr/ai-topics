---
title: "Don Zagier's approximation of Markov's diophantine equation"
url: "https://www.johndcook.com/blog/2026/05/19/zagiers-equation/"
fetched_at: 2026-05-20T07:00:49.633995+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Don Zagier's approximation of Markov's diophantine equation

Source: https://www.johndcook.com/blog/2026/05/19/zagiers-equation/

Markov numbers are integer solutions to
x
² +
y
² +
z
² = 3
xyz
.
The Wikipedia article on Markov numbers mentions that Don Zagier studied Markov numbers by looking the approximating equation
x
² +
y
² +
z
² = 3
xyz
+ 4/9
which is equivalent to
f
(
x
) +
f
(
y
) =
f
(
z
)
where
f
(
t
) is defined as arccosh(3
t
/2). It wasn’t clear to me why the two previous equations are equivalent, so I’m writing this post to show that they are equivalent.
Examples
Before showing the equivalence of Zagier’s two equations, let’s look at an example that shows solutions to his second equation approximate solutions to Markov’s equation.
The following code verifies that (5, 13, 194) is a solution to Markov’s equation.
x, y, z = 5, 13, 194
assert(x**2 + y**2 + z**2 == 3*x*y*z)
With the same
x
and
y
above, let’s show that the
z
in Zagier’s second equation is close to the
z
above.
from math import cosh, acosh

f = lambda t: acosh(3*t/2)
g = lambda t: cosh(t)*2/3
z = g(f(x) + f(y))
print(z)
This gives
z
= 194.0023, which is close to the value of
z
in the Markov triple above.
Applying Osborn’s rule
Now suppose
f
(
x
) +
f
(
y
) =
f
(
z
)
which expands to
arccosh(3
x
/2) + arccosh(3
y
/2)  = arccosh(3
z
/2).
It seems sensible to apply cosh to both sides. Is there some identity for cosh of a sum? Maybe you recall the equation for cosine of a sum:
cos(
a
+
b
) = cos(
a
) cos(
b
) − sin(
a
) sin(
b
).
Then
Osborn’s rule
says the corresponding hyperbolic identity is
cosh(
a
+
b
) = cosh(
a
) cosh(
b
) − sinh(
a
) sinh(
b
).
Osborn’s rule also says that the analog of the familiar identity
sin²(
a
) + cos²(
b
) = 1
is
sinh²(
a
) = cosh²(
b
) − 1.
From these two hyperbolic identities we can show that [1]
cosh( arccosh(
a
) + arccosh(
b
) ) =
ab
+ √(
a
² − 1) √(
b
² − 1).
Slug it out
The identity derived above is the tool we need to reduce our task to routine algebra.
If
arccosh(3
x
/2) + arccosh(3
y
/2)  = arccosh(3
z
/2)
then
(3
x
/2)  (3
y
/2)  + √((3
x
/2)² − 1) √((3
y
/2)² − 1) = 3
z
/ 2
which simplifies to Zagier’s equation
x
² +
y
² +
z
² = 3
xyz
+ 4/9.
Related posts
[1] The equation holds at least for
x
> 1 and
y
> 1, which is enough for this post. More general arguments run into complications due to branch cuts.
