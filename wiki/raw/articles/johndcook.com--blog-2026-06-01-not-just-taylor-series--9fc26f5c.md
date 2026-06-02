---
title: "It’s not just Taylor series"
url: "https://www.johndcook.com/blog/2026/06/01/not-just-taylor-series/"
fetched_at: 2026-06-02T07:05:04.657921+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# It’s not just Taylor series

Source: https://www.johndcook.com/blog/2026/06/01/not-just-taylor-series/

There is still active discussion on X about the approximation
exp(−
x
²) ≈ (1 + cos(sin(
x
) +
x
))/2
and some are saying this can just be explained by Taylor series: the series for the two sides differ for the first time at the
x
6
term, so that’s why you get a good approximation. As I wrote
yesterday
, that’s only part of it.
If it were just about Taylor series you could use
exp(−
x
²) ≈ 1 −
x
² +
x
4
/2
which also has error
O
(
x
6
). But this approximation is only good for fairly small
x
, say in [−0.5, 0.5], whereas the approximation at the top of the post is good over [−4, 4]. When
x
= 4, the error in the cosine approximation is 0.002579 but the error in the Taylor approximation is 113, five orders of magnitude larger.
If the accuracy of the cosine approximation were due to Taylor series, then we’d expect the function
exp(−
x
²) − (1 + cos(sin(
x
) +
x
))/2
to be small not just over the interval [−4, 4] but over a disk of radius 4 in the complex plane. But it’s not. When
x
= 4
i
the function is on the order of 10
13
.
Both the cosine approximation and the Taylor approximation are good for small disks, say of radius 0.5. They’re both bad for much larger disks, and in fact the cosine approximation is worse.
