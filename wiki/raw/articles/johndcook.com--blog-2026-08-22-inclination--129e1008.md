---
title: "The difference orbit inclination makes"
url: "https://www.johndcook.com/blog/2026/08/22/inclination/"
fetched_at: 2026-08-23T10:01:40.507976+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# The difference orbit inclination makes

Source: https://www.johndcook.com/blog/2026/08/22/inclination/

Suppose you wanted to find the distance between Earth and Mars over time. To first approximation, both planets orbit the sun in elliptic orbits in the same plane.
If you wanted to be more accurate, you’d need to take into account the fact that the orbit of Mars is tilted about 1.85° relative to the Earth’s orbit. How much difference does that make?
To simplify things, let’s assume the Earth orbits the sun in a circle of radius 1 and Mars orbits the sun in a circle of radius 1.5. The distance between Earth and Mars over time would be basically sinusoidal.
How much does inclination contribute to this distance? In other words, what is the difference between the distance accounting for the inclination of Mars’ orbit and the distance if we assume the two orbits are in the same plane?
This plot gives the answer.
The effect is not large, about three orders of magnitude smaller than the main effect, but it’s interesting how erratic it is.
The plots were made with the following code.
from numpy import *

R = 1.5
T = R**1.5 # Kepler's third law

def f(t, theta):
    return sqrt(
        (cos(t) - R*cos(t/T)*cos(theta))**2 +
        (sin(t) - R*sin(t/T))**2 +
        (R*sin(theta)*cos(t/T))**2
    )
The first plot graphs
f
(
t
, θ) and the second graphs
f
(
t
, θ) −
f
(
t
, 0).
