---
title: "Intersecting spheres and GPS"
url: "https://www.johndcook.com/blog/2026/04/14/intersecting-spheres-and-gps/"
fetched_at: 2026-04-28T07:02:46.740420+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Intersecting spheres and GPS

Source: https://www.johndcook.com/blog/2026/04/14/intersecting-spheres-and-gps/

If you know the distance
d
to a satellite, you can compute a circle of points that passes through your location. That’s because you’re at the intersection of two spheres—the earth’s surface and a sphere of radius
d
centered on the satellite—and the intersection of two spheres is a circle. Said another way, one observation of a satellite determines a circle of possible locations.
If you know the distance to a second satellite as well, then you can find two circles that contain your location. The two circles intersect at two points, and you know that you’re at one of two possible positions. If you know your approximate position, you may be able to rule out one of the intersection points.
If you know the distance to three different satellites, now you know three circles that you’re standing on, and the third circle will only pass through one of the two points determined by the first two satellites. Now you know exactly where you are.
Knowing the distance to more satellites is even better. In theory additional observations are redundant but harmless. In practice, they let you partially cancel out inevitable measurement errors.
If you’re not on the earth’s surface, you’re still at the intersection of
n
spheres if you know the distance to
n
satellites. If you’re in an airplane, or on route to the moon, the same principles apply.
Errors and corrections
How do you know the distance to a satellite? The satellite can announce what time it is by its clock, then when you receive the announcement you compare it to the time by your clock. The difference between the two times tells you how long the radio signal traveled. Multiply by the speed of light and you have the distance.
However, your clock will probably not be exactly synchronized with the satellite clock. Observing a fourth satellite can fix the problem of your clock not being synchronized with the satellite clocks. But it doesn’t fix the more subtle problems of special relativity and general relativity. See
this post
by Shri Khalpada for an accessible discussion of the physics.
Numerical computation
Each distance measurement gives you an equation:
||
x
–
s
i
|| =
d
i
where
s
i
is the location of the
i
th satellite and
d
i
is your distance to that satellite. If you square both sides of the equation, you have a quadratic equation. You have to solve a system of nonlinear equations, and yet there is a way to transform the problem into solving linear equations, i.e. using linear algebra. See
this article
for details.
Related posts
