---
title: "Turning a trick into a technique"
url: "https://www.johndcook.com/blog/2026/04/28/even-series-trick/"
fetched_at: 2026-04-29T07:00:51.293957+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Turning a trick into a technique

Source: https://www.johndcook.com/blog/2026/04/28/even-series-trick/

Someone said a technique is a trick that works twice.
I wanted to see if I could get anything interesting by turning the trick in the
previous post
into a technique. The trick created a high-order approximation by subtracting a multiple one even function from another. Even functions only have even-order terms, and by using the right multiple you can cancel out the second-order term as well.
For an example, I’d like to approximate the Bessel function
J
0
(
x
) by the better known cosine function. Both are even functions.
J
0
(
x
) = 1 −
x
2
/4 +
x
4
/64 + …
cos(
x
) = 1 −
x
2
/2 +
x
4
/24 + …
and so
2
J
0
(
x
) − cos(
x
) = 1 −
x
4
/96 + …
which means
J
0
(
x
) ≈ (1 + cos(
x
))/2
is an excellent approximation for small
x
.
Let’s try this for a couple examples.
J
0
(0.2) = 0.990025 and (1 + cos(0.2))/2 = 0.990033.
J
0
(0.05) = 0.99937510 and (1 + cos(0.05))/2 = 0.99937513.
