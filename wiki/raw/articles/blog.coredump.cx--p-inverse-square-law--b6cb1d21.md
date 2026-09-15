---
title: "Inverse-square law"
url: "https://blog.coredump.cx/p/inverse-square-law"
fetched_at: 2026-09-14T10:02:13.124318+00:00
source: "lcamtuf.substack.com"
tags: [blog, raw]
---

# Inverse-square law

Source: https://blog.coredump.cx/p/inverse-square-law

If you’re dabbling in electronics, you might have heard of what’s known as the
inverse-square law.
This law says that the intensity of many types of physical phenomena decreases with the square of the distance to the origin. For example, if you get twice as far from a lightbulb, a handheld light meter will register a four-fold drop in luminance. The same goes for sound, radio transmissions, and so forth.
But… why? Wouldn’t it be more natural if the intensity dropped in direct proportion to how far you are from the source? Or, if it’s about scattering in a three-dimensional space, shouldn’t it be the
cube
of distance? Let’s try to figure it out.
If we want an answer that doesn’t merely kick the can down the road, we need to start with the formula for the surface area of a sphere. From school, you might recall that the equation is:
\(S_{sphere} = 4 \pi r^2\)
That said, I bet your teachers have never explained where the formula comes from. And as with many other “obvious” concepts in elementary mathematics, the answer is not as obvious as it seems — even though it’s been known since the times of Ancient Greeks.
To get going, imagine a thin tube (a cap-less cylinder) constructed by gluing the edges of a rectangular sheet of paper:
Constructing a paper cylinder.
To make the cylinder, we didn’t need to squish or stretch the rectangle, so the process preserved the surface area. The outer surface of this cap-less cylinder is just height (
h
) multiplied by what used to be width (
w
) and is now circumference.
Next, take a sphere with a radius
r
and place it inside such a fitted cylinder of the same circumference and the same height:
The sphere has a radius of
r
, so its circumference — and thus, the circumference of the cylinder — is 2𝜋
r
. It’s just a matter of how 𝜋 is commonly defined.
The height of the cylinder is equal to the sphere’s diameter, or twice the radius. We know that the cylinder’s outer surface area is just circumference times height, so we can write that
S
tube
= 4𝜋
r
2
. Lo and behold — that’s the same formula as what we’ve been given in school for the inscribed sphere. But… how come?
To get to the bottom of this, imagine tiling tiling flat squares on the outer surface of the cylinder, each square measuring
a
×
a
:
This gives us an approximation of the cylinder; we can reduce the error of the approximation as much as we like by decreasing the size of the tiles. In the limit of this refinement process, as
a
becomes infinitesimal (infinitely small), we converge on the exact dimensions and curvature of the shape we intended to create.
The four corners of each square in this tile-based sorta-cylinder can be projected toward the sphere’s vertical axis of symmetry, such that the horizontal coordinates converge toward the center while the vertical component remains unchanged. This projection is a wedge that intersects the surface of the sphere at an angle:
If we repeat this process for every outer square that makes up the cylinder, we end up with a neatly tessellated sphere (below, left):
In this rendering, each of the resulting segments is markedly curved; if we replace them with flat polygonal tiles (right), the shape gets out of whack. That said, once again, we can improve the accuracy of this tiling to an arbitrary extent by projecting a finer-grained pattern of cylinder-side squares. In the limit, the flat approximation converges on a perfect sphere.
A finer tessellation of a sphere.
To recap what we’ve done so far: we’ve taken a cylinder with a known and easily-calculated outer surface area:
S
tube
=
4𝜋
r
2
. We then approximated it with some number of square tiles of size
a
; the number of tiles ideally “tends to” infinity, even if we still have ways to go in the illustrations accompanying this article. Each tile has a surface area of
a
2
.
We also mapped each cylinder-side tile to a polygonal tile constructed on the surface of an inscribed sphere (radius
r
). Each cylinder-side square maps to a sphere-side polygon of some sort; there are no gaps or overlaps. Our next task is to figure out what’s the surface area of these newly-conjured polygons.
At first blush, the polygons look like rectangles, but they’re actually isosceles trapezoids; the top edge is narrower north of the equator and the opposite is true to the south. That said, through simple geometric rearrangement, we can show that the surface area of any trapezoid is equal to the surface area of a rectangle of of the same midpoint width:
Surface area of an isosceles trapezoid is w × h.
In other words, we only need to figure out the midpoint
w
and
h
. We can start with the horizontal dimension: viewed from the above, the wedge that cuts through the sphere is a triangle. It has an initial span of
a
at the surface of cylinder (always at a distance
r
from the center axis) and then converges toward zero as get closer to the axis:
Wedge and its intersections, top view.
If
d
is the distance from the center axis to the midpoint of the sphere-side polygon, the width at the intersection can be trivially calculated by taking
a
and then scaling it depending on where
d
is in proportion to
r:
\(w = a \cdot \frac{d}{r}\)
We don’t know
d
, but we don’t actually need it; the term is going to cancel out down the line.
To calculate the area of the sphere-side trapezoid, we also need to know its height. This is a bit trickier: in the side view, the wedge is is a rectangle, but the polygon on the sphere may be tilted depending on the latitude:
On the drawing, I marked angle
α
that corresponds to the elevation of center of the polygon. From basic trigonometry, we should expect the same angle where the horizontal blue segment (
d
) meets the green diagonal, so I marked this location too.
Together with the
y
axis, the segments marked
d
and
r
form an upside-down triangle shown in the inset. This right triangle has a hypotenuse of length
r
and an adjacent of length
d;
from the definition of cosine, the ratio of these values is the same as cos(
α):
\(cos(\alpha) = \frac{\text{adjacent}}{\text{hypotenuse}} = \frac{d}{r}\)
Next, let’s zoom in on the far end of the wedge:
The green diagonal originates from the center of the sphere, so it necessarily approaches the surface at an angle of 90°. From before, we know that the internal angle between this segment and the blue horizontal line is
α
; the sum of these angles — downward measurement from the blue horizontal line to the orange projection — is obviously 90° +
α.
Let’s mark that result, get rid of the radius line, and then dangle a vertical segment (light green) from the top:
In this image, I also marked an unknown angle
β
. The angle between the horizontal line and the tilted projection is 90° +
α,
and
β
just subtracts 90° from it; in other words,
β = α.
We can now look at the shaded right triangle. Viewed from the top corner, its hypotenuse (orange, diagonal) is equal to the height of the tilted projection (
h
) and the adjacent (green, vertical) is the same as the height of the wedge (
a
). The angle between these segments is
α,
so once again, from the definition of cosine, we can write:
\(cos(\beta) = cos(\alpha) = \frac{\text{adjacent}}{\text{hypotenuse}} = \frac{a}{h}\)
Per the earlier analysis, we also know that cos(
α) = d / r;
this allows us to make substitution to get rid of the cosine and solve for
h:
\(\begin{array}{r l}
\text{After substitution:} & \large \frac{a}{h} = \frac{d}{r}  \\
\text{Dividing both sides by } a \text{:} & \large \frac{1}{h} = \frac{d}{a \cdot r} \\
\text{Flipping the fractions around:} & h = a \cdot \frac{r}{d}
\end{array}\)
We have previously calculated the width of the trapezoid as
w = a · d/r
and we now know that
h = a · r/d
. But all we’re really interested is its surface area,
h × w.
This multiplication cancels out
d
and
r
:
\(S_{trapezoid} = w \cdot h = a \cdot \cancel{\frac{d}{r}} \cdot a \cdot \cancel{\frac{r}{d}} = a^2\)
To understand the significance of this result, again: we divided the outer surface of a cylinder with an area of 4𝜋
r
2
into some number of
a × a
squares. We then mapped each of these squares to a corresponding polygon on the surface of a sphere. As it turns out, each of projected polygons has the same surface area as the originating square:
a
2
. If both the number of segments and their surface areas remain the same, we must conclude that the mapping between the square-based approximation of a cylinder and a trapezoid-based approximation of a sphere is area-preserving. So, here’s our 4𝜋
r
2
.
Huh… who is this? Where am I? Ah, right. Sorry.
Imagine that Sally is carrying a box of marbles and accidentally drops them on the floor. The marbles spread out in all possible directions; some of them roll toward a conveniently-placed bottomless void. How many are going to fall in?
Well, if Sally’s floor happens to one-dimensional — we don’t judge — the distance to the void doesn’t matter. Half the marbles are going to roll to the left and half to the right; either way, 50% is going to end up in the hole:
Yes, it’s just one dimension, but the rent is affordable.
In other words, “marble intensity”, as measured by the inhabitants of the bottomless void, doesn’t depend on distance to the origin. If we wanted to be truly obnoxious, we could say that the number of marbles falling into the hole drops with the zeroth power of distance. This is because
d
0
= 1 for any non-zero
d.
Now, say that Sally splurges and upgrades to a two-dimensional floor. In this situation, if the marbles are dropped perfectly, they should spread around forming a circular front:
Stay at least eight feet away from bottomless voids.
The circumference of the this circle grows proportionally with distance — 2𝜋
r
— but the number of marbles on the ground doesn’t change. It follows that if the distance doubles, the bottomless hole only gets to swallow half as many as before:
The void will not feat tonight.
So, in a two-dimensional world, the falloff in marble-intensity, as witnessed by those living in bottomless hole, decreases with the first power of distance to the origin.
But what if Sally violently loses her marbles in zero gravity? In this case, the moving marble-front is not a circle but the surface of a three-dimensional sphere. As before, the number of marbles can’t change, but the area they spread across now grows with the
square
of distance, 4𝜋
r
2
. Hence, inverse-square law.
The marbles are gone. Model credit:
ingate
.
We have
d
0
for one dimension,
d
1
for two dimensions, and
d
2
for three. Care to guess what would happen in 4D?
I write original articles about electronics, math, computing, and more. In particular, you might enjoy:
If you like it, please subscribe.
