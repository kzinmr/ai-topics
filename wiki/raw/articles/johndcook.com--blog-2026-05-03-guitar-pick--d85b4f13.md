---
title: "The shape of a guitar pick"
url: "https://www.johndcook.com/blog/2026/05/03/guitar-pick/"
fetched_at: 2026-05-04T07:01:10.066510+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# The shape of a guitar pick

Source: https://www.johndcook.com/blog/2026/05/03/guitar-pick/

I saw a
post
on X that plotted the function
(log
x
)² + (log
y
)² = 1.
Of course the plot of
x
² +
y
² = 1
is a circle, but I never thought what taking logs would do to the shape.
Here’s what the contours look like setting the right hand side equal to 1, 2, 3, …, 10.
ContourPlot[Log[x]^2 + Log[y]^2, {x, 0, 10}, {y, 0, 10}, 
    Contours -> Range[10]]
The dark blue contour near the origin reminded me of a guitar pick, so I decided to take a stab at creating an equation for the shape of a guitar pick.
I wanted to rotate the image so the axis of symmetry for the pick is vertical, so I replaced
x
and
y
with
x
+
y
and
x
−
y
.
The aspect ratio was too wide, so I experimented with
log(
y
+
kx
)² + log(
y
−
kx
)² =
r
²
where increasing
k
increases the height-to-width ratio. After a little experimentation I settled on
k
= 1.5 and
r
= 1.
This has an aspect ratio of roughly 5:4, which is about what I measured from a photo of a guitar pick.
Updating: refining the fit
After posting this article on X, Paul Graham
replied
with a photo of a Fender guitar pick with the image above overlaid. The fit was fairly good, but the aspect ratio wasn’t quite right.
So then I did a little research. The shape referred to in this post is known as the “351,” but even for the 351 shape the aspect ratio varies slightly between picks.
Setting
k
= 1.6 gives a better fit to Paul Graham’s pick.
The blue line represents my fit using
k
= 1.5 and the red line represents my fit using
k
= 1.6.
