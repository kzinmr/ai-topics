---
title: "Kalman and Bayes average grades"
url: "https://www.johndcook.com/blog/2026/04/04/kalman-bayes/"
fetched_at: 2026-04-28T07:02:47.788770+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Kalman and Bayes average grades

Source: https://www.johndcook.com/blog/2026/04/04/kalman-bayes/

This post will look at the problem of updating an average grade as a very simple special case of Bayesian statistics and of Kalman filtering.
Suppose you’re keeping up with your average grade in a class, and you know your average after
n
tests, all weighted equally.
m
= (
x
1
+
x
2
+
x
3
+ … +
x
n
) /
n
.
Then you get another test grade back and your new average is
m
′ = (
x
1
+
x
2
+
x
3
+ … +
x
n
+
x
n
+1
) / (
n
+ 1).
You don’t need the individual test grades once you’ve computed the average; you can instead remember the average
m
and the number of grades
n
[1]. Then you know the sum of the first
n
grades is
nm
and so
m
′ = (
nm
+
x
n
+1
) / (
n
+ 1).
You could split that into
m
′ =
w
1
m
+
w
2
x
n
+1
where
w
1
=
n
/(
n
+ 1) and
w
2
= 1/(
n
+ 1). In other words, the new mean is the weighted average of the previous mean and the new score.
A
Bayesian
perspective would say that your posterior expected grade
m
′ is a compromise between your prior expected grade
m
and the new data
x
n
+1
. [2]
You could also rewrite the equation above as
m
′ =
m
+ (
x
n
+1
−
m
)/(
n
+ 1) =
m
+
K
Δ
where
K
= 1/(
n
+ 1) and Δ =
x
n
+1
−
m
. In
Kalman
filter terms,
K
is the gain, the proportionality constant for how the change in your state is proportional to the difference between what you saw and what you expected.
Related posts
[1] In statistical terms, the mean is a
sufficient statistic
.
[2] You could flesh this out by using a normal likelihood and a flat improper prior.
