---
title: "Aitken acceleration before Aitken"
url: "https://www.johndcook.com/blog/2026/06/07/aitkin-acceleration-kepler/"
fetched_at: 2026-06-08T07:01:15.171076+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Aitken acceleration before Aitken

Source: https://www.johndcook.com/blog/2026/06/07/aitkin-acceleration-kepler/

Kepler solved his eponymous equation
M
=
E
−
e
sin(
E
)
by finding a fixed point of
E
=
M
+
e
sin(
E
).
So guess a value of
E
and stick it into the right hand side. Then plug that value into the right hand side again. Kepler said a couple iterations should be enough. And a couple iterations
are
enough if the eccentricity
e
is small and you don’t need much accuracy.
The rate of convergence is determined by
e
. Kepler implicitly had in mind small values of
e
because he wasn’t aware of anything orbiting the sun in a highly elliptical orbit. Here’s an example with eccentricity 0.05, about the eccentricity of the orbits of Jupiter and Saturn.
from math import sin

M, E, e = 1, 1, 0.05
for _ in range(5):
    E = M + e*sin(E)
    residual = M - (E - e*sin(E))
    print(residual)
The residual after just two iterations is 2.77 × 10
−5
. If you change
e
to 0.2, the eccentricity of Mercury’s orbit, it takes three iterations to get comparable accuracy. Mercury has the most eccentric orbit of any object Kepler would have known about.
Now suppose you’d like to solve for
E
when
M
= 1 for Halley’s comet, and you’d like an error of less than 10
−8
. Now you need 16 iterations.
C. F. W. Peters discovered a faster algorithm in 1891.
E
1
=
M
+
e
sin(
E
0
)
E
2
=
M
+
e
sin(
E
1
)
E
3
= (
E
2
E
0
−
E
1
²)/(
E
2
− 2
E
1
+
E
0
)
Let’s look at the results of doing three iterations of Peters’ method for Halley’s comet.
M, E0, e = 1, 1, 0.967
for _ in range(3):
    E1 = M + e*sin(E0)
    E2 = M + e*sin(E1)
    E3 = (E2*E0 - E1**2)/(E2 - 2*E1 + E0)
    residual = M - (E - e*sin(E3))
    print(residual)
    E0 = E3 # for next iteration
This gives a residual of −7.23 × 10
−10
. Each iteration of Peters’ method requires a little more than twice as much work as an iteration of Kepler’s method, but 3 iterations of Peters’ method accomplished more than 16 iterations of Kepler’s method.
Peters’ algorithm from 1891 was a special case of Alexander Aitken’s series acceleration method published in 1926.
Related posts
