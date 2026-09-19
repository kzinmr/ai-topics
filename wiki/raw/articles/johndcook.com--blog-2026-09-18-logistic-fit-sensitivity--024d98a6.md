---
title: "Why fitting a logistic is nearly impossible from early data"
url: "https://www.johndcook.com/blog/2026/09/18/logistic-fit-sensitivity/"
fetched_at: 2026-09-19T10:00:49.599426+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Why fitting a logistic is nearly impossible from early data

Source: https://www.johndcook.com/blog/2026/09/18/logistic-fit-sensitivity/

Nothing grows exponentially forever. What appears to be an exponential curve often turns out to be some sort of S curve, such as a logistic curve.
Suppose you’re collecting data on the left side of the curve. If there’s even a small amount of error in your data, you won’t be able to predict the asymptotic value with any accuracy. But if you have data on both sides of the inflection point, you can make a good prediction of the limiting value.
I’ve written about this
before
, explaining that the problem is hard, but I didn’t say
why
it’s hard. Here I’d like to give an idea why it’s hard.
Suppose you want to fit a logistic equation
to three distinct values of
t
and the corresponding values of
y
. There is a unique solution, but in general you cannot find a solution in closed form. However, if the values of
t
are evenly spaced
there is a method [1] to solve for the parameters
L
,
k
, and
t
0
. For this post we’re only interested in the limiting value
L
, and it can be found by
independent of
h
.
To find out how small changes in the
y
‘s change the estimate of
L
, we take the partial derivatives of
L
with respect to the
y
‘s and find
and
All three derivatives have the same expression in the denominator:
y
1
² −
y
0
y
2
.
If the function
y
(
t
) were an exponential, this expression would be exactly zero [2]. The function
y
(
t
) is not exactly exponential, but it is
approximately
exponential when the
t
‘s are in the left or right tail of the logistic curve. The further out in either tail the
t
‘s are, the closer the expression is to zero.
So when all the
t
‘s come from the same side of the inflection point,
y
(
t
) is nearly exponential the partial derivatives are huge and so the fitted value of
L
is extremely sensitive to changes in the
y
‘s.
[1] Raymond Pearl and Lowell J. Reed. On the Rate of Growth of the Population of the United States Since 1790 and its Mathematical Representation. Proceedings of the National Academy of Sciences of the United States of America, Vol. 6, No. 6 (Jun. 15, 1920), pp. 275-288
[2] exp(
x
+
h
)² = exp(
x
)² exp(
h
)² = exp(
x
) exp(
x
+ 2
h
)
