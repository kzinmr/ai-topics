---
title: "Gravity on an oblate planet"
url: "https://www.johndcook.com/blog/2026/11/23/oblate-spheroid-gravity/"
fetched_at: 2026-11-24T10:01:25.803109+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Gravity on an oblate planet

Source: https://www.johndcook.com/blog/2026/11/23/oblate-spheroid-gravity/

A spherical planet is not a point mass, but the gravity on the surface is the same as if the mass were concentrated at a point in the center. If a planet is not spherical but rather an oblate spheroid, the point-mass approximation doesn’t work.
Suppose a planet has equatorial radius
a
and polar radius
b
, with
a
significantly larger than
b
. We’ll compare the point-mass model with the uniform density model.
If the surface of the planet were a massless shell, with all the mass concentrated at a point in the center, the force of gravity would be inversely proportional to the square of the distance to the center. Gravity at the poles would be proportional to 1/
b
² and gravity on the equator would be proportional to 1/
a
². The ratio of the polar gravity to equatorial gravity would be (
a
/
b
)².
The model above grossly overestimates the variation in gravity. It’s not even useful for moderately oblate planets, such as the one we live on.
It’s true that if
a
/
b
is nearly 1 then the gravity ratio is also near 1, but the approximation overestimates the effect of flattening by an order of magnitude.
Flattening
is defined to be
ε = 1 −
b
/
a
.
Assuming the planet has uniform density, the ratio of polar gravity to equatorial gravity has the following expansion in ε:
1 + ε/5 + (9/175) ε² + …
Now
a
/
b
= 1/(1 − ε) and so
(
a
/
b
)² = 1/(1 − ε)² = 1 + 2ε + 3ε² + …
To first order approximation, the effect of flattening is ε/5, but the point-mass approximation estimates the effect as 2ε, off by a factor of 10.
I became interested in this problem because I started reading a novel that takes place on an oblate spheroidal planet with enormous variation in gravitational strength from pole to equator [1]. On a more nearly spherical planet like Earth, oblateness still matters a great deal when calculating satellite orbits. This is called the
J2 effect
.
[1] Hal Clement, Mission of Gravity, serialized in 1953, published as a book in 1954. The planet in the novel rotates every 18 minutes, which explains why it is so oblate. The rotation also increases the ratio of apparent gravity because centrifugal force decreases the apparent gravity at the equator.
