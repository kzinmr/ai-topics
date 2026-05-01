---
title: "Approximating even functions by powers of cosine"
url: "https://www.johndcook.com/blog/2026/04/30/burmanns-theorem/"
fetched_at: 2026-05-01T07:13:05.326217+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Approximating even functions by powers of cosine

Source: https://www.johndcook.com/blog/2026/04/30/burmanns-theorem/

A couple days ago I wrote a post about t
urning a trick into a technique
, finding another use for a clever way to construct simple, accurate approximations. I used as my example approximating the Bessel function
J
(
x
) with (1 + cos(x))/2. I learned via a helpful
comment
on Mathstodon that my approximation was the first-order part of a more general series
The first-order approximation has error
O
(
x
4
), as shown in the earlier post. Adding the second-order term makes the error
O
(
x
6
), and adding the third-order term makes it
O
(
x
8
).
I’ve written a few times about cosine approximations to the normal probability density. For example, see
this post
. We could use the same idea as the series above to approximate the normal density with a series of powers of cosine. This gives us
and as before, the first, second, and third order truncated series have error
O
(
x
4
),
O
(
x
6
), and
O
(
x
8
).
The general theory behind what’s going on here is an extension of
Bürmann’s theorem
. The original version of the theorem relies on a series inversion theorem that in turn relies on the approximating function, in our case cos(
x
) − 1, not having zero derivative at the center of the series. But there is a more general form of Bürmann’s theorem based on a
more general form of series inversion
. We will always need a more general version of the theorem when working with even functions because even functions have zero derivative at zero.
Here’s another example, this time using the Bessel function
J
1
, an odd function, which does use the original version of Bürmann’s theorem to approximate
J
1
by powers of sine.
In this case truncating the series after sin
k
(
x
) gives an error
O
(
x
k
+ 2
).
You can find more on Bürmann’s theorem in
Whittker and Watson
.
