---
title: "Mean distance to the sun"
url: "https://www.johndcook.com/blog/2026/08/18/mean-distance-to-the-sun/"
fetched_at: 2026-08-19T10:00:59.093434+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Mean distance to the sun

Source: https://www.johndcook.com/blog/2026/08/18/mean-distance-to-the-sun/

Suppose you have a planet in an elliptical orbit around a star. The math is identical for any light object orbiting a heavy object, such as a moon or satellite orbiting a planet, but we’ll call the heavy object a star and the light object a planet.
The center of the star is not quite the center of the orbit. The planet moves along an ellipse with the star at one focus of that ellipse.
Let
a
be the semi-major axis of planet’s orbit, the maximum distance from the center of the ellipse to a point on the ellipse. Then the distance of a focus to the center of the ellipse is
ae
where
e
is the eccentricity of the ellipse. This defines eccentricity. The center of earth’s orbit is between three and four solar radii away from the center of the sun [1].
The planet is farthest from the star when it is along the major axis of the ellipse on the opposite side as the star. The distance is then
a
+
ae
, the distance to the center plus the distance from the center to the star. The planet is closest to the star on the opposite side of its orbit. There the distance is
a
−
ae
. In summary the maximum distance to the star is
a
(1 +
e
)
and the minimum distance is
a
(1 −
e
).
If you had to guess the
average
distance between the planet and its star,
a
would be a good guess since it’s the average of the maximum and minimum distance. And that’s a good approximation, provided
e
is small. The mean distance over time is
a
(1 + ½
e
²).
See
derivation
. The average distance is greater than
a
because the planet moves faster when nearest the star and slower when further from the star.
The relative error in approximating the mean distance by
a
is then ½
e
². When
e
is small, ½
e
² is very small. For the earth’s orbit,
e
= 0.01671, and so the approximation is off by around 0.014%.
The eccentricity of Pluto’s orbit is 0.2488, and so in that case the approximation is off by about 3.1%. The eccentricity of a Molniya orbit, used by some Russian satellites, is 0.74 [2]. For such satellites the error in approximating the mean distance to earth as the semimajor axis is around 27%.
Related posts
[1] For earth’s orbit,
e
= 0.01671,
a
= 1.496×10
11
m, and the sun’s radius is
r
= 6.957×10
8
m. And so
ea
/
r
= 3.59.
[2] An object in such a highly elliptical orbit will spend a long time at the far side of its orbit, i.e. over Russia. Sort of a poor man’s geostationary orbit.
