---
title: "Finding a parabola through two points with given slopes"
url: "https://www.johndcook.com/blog/2026/04/14/artz-parabola/"
fetched_at: 2026-05-01T07:02:10.369457+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Finding a parabola through two points with given slopes

Source: https://www.johndcook.com/blog/2026/04/14/artz-parabola/

The Wikipedia article on modern triangle geometry has an image labeled “Artzt parabolas” with no explanation.
A quick search didn’t turn up anything about Artzt parabolas [1], but apparently the parabolas go through pairs of vertices with tangents parallel to the sides.
The general form of a conic section is
ax
² +
bxy
+
cy
² +
dx
+
ey
+
f
= 0
and the constraint
b
² = 4
ac
means the conic will be a parabola.
We have 6 parameters, each determined only up to a scaling factor; you can multiply both sides by any non-zero constant and still have the same conic. So a general conic has 5 degrees of freedom, and the parabola condition
b
² = 4
ac
takes us down to 4. Specifying two points that the parabola passes through takes up 2 more degrees of freedom, and specifying the slopes takes up the last two. So it’s plausible that there is a unique solution to the problem.
There is indeed a solution, unique up to scaling the parameters. The following code finds parameters of a parabola that passes through (
x
i
,
y
i
) with slope
m
i
for
i
= 1, 2.
def solve(x1, y1, m1, x2, y2, m2):
    
    Δx = x2 - x1
    Δy = y2 - y1
    λ = 4*(Δx*m1 - Δy)*(Δx*m2 - Δy)/(m1 - m2)**2
    k = x2*y1 - x1*y2

    a = Δy**2 + λ*m1*m2
    b = -2*Δx*Δy - λ*(m1 + m2)
    c = Δx**2 + λ
    d =  2*k*Δy + λ*(m1*y2 + m2*y1 - m1*m2*(x1 + x2))
    e = -2*k*Δx + λ*(m1*x1 + m2*x2 - y1 - y2)
    f = k**2 + λ*(m1*x1 - y1)*(m2*x2 - y2)

    return (a, b, c, d, e, f)
[1] The page said “Artz” when I first looked at it, but it has since been corrected to “Artzt”. Maybe I didn’t find anything because I was looking for the wrong spelling.
