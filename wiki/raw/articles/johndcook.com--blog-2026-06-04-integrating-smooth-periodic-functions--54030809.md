---
title: "Integrating smooth periodic functions"
url: "https://www.johndcook.com/blog/2026/06/04/integrating-smooth-periodic-functions/"
fetched_at: 2026-06-05T07:01:41.252680+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Integrating smooth periodic functions

Source: https://www.johndcook.com/blog/2026/06/04/integrating-smooth-periodic-functions/

Several posts lately have looked at the function
f
(
x
) = cos(sin(
x
) +
x
).
This post will look at the function from a different angle. It’s a smooth function with period 2π. For reasons I wrote about
here
, this means that the trapezoid rule should find its integral very efficiently.
In general, the error in the trapezoid rule is on the order of 1/
N
² where
N
is the number of integration points. To be more specific, the error in integrating a function
f
over [
a
,
b
] with
N
points is bounded by
(
b
−
a
)³
M
/ 12
N
²
where
M
is the maximum absolute value of the second derivative of
f
. So in our case we should expect the error to be less than 82.67/
N
². In fact we do
much
better than that. The error does not decrease quadratically, as it does in general, but exponentially.
With just 16 integration points, we’ve reached the limit of floating point representation.
