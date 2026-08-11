---
title: "Inverse differential equations"
url: "https://www.johndcook.com/blog/2026/08/10/inverse-differential-equations/"
fetched_at: 2026-08-11T10:16:31.123135+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Inverse differential equations

Source: https://www.johndcook.com/blog/2026/08/10/inverse-differential-equations/

In science and engineering classes, you might describe a system using Newton’s laws and end up with a differential equation. You then solve the differential equation, analytically or numerically, to see how the solutions behave.
You might also do the opposite, especially in a mathematics class: look at what differential equation a set of functions satisfy in order to understand those functions.
Bessel functions came out of solving differential equations from
astronomy
. But then they turned out to be useful, not just in other areas of science, but in pure mathematics as well. So there are Bessel function users who came to the functions first and haven’t seen the differential equation they came from.
You can learn a lot about Bessel functions, and other special functions, by looking at their defining differential equation even if you’re not directly interested in the differential equation or the physical problem that motivated it.
Bessel functions satisfy
x
²
y
″ +
x
y
′ + (
x
² −
n
²)
y
= 0.
You can tell a lot about Bessel functions just by inspecting this equation without solving it. If we divide by
x
² and write the equation in the form
y
″ + (
p
(
x
)/
x
)
y
′ + (
q
(
x
)/
x
²)
y
= 0
then
p
(
x
) = 1 and
q
(
x
) =
x
² −
n
². The indicial equation
r
(
r
− 1) +
p
(0)
r
+
q
(0) = 0
reduces to
r
² =
n
²
and so
r
= ±
n
. That alone tells us there are two solutions, one analytic at zero and one singular at zero. These are
J
n
and
Y
n
respectively. It also tells us the behavior of these functions as
x
goes to zero and as
x
goes to infinity. To find out more, look up “method of Frobinius.”
