---
title: "Online (one-pass) algorithms"
url: "https://www.johndcook.com/blog/2026/05/29/online-one-pass-algorithms/"
fetched_at: 2026-05-30T07:01:26.862487+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Online (one-pass) algorithms

Source: https://www.johndcook.com/blog/2026/05/29/online-one-pass-algorithms/

Canonical example
The sample variance of a set of numbers is defined in terms of the sum of the squared distances from each point to the mean.
So it would seem that you first need to calculate the mean, then go back and compute the squared differences from the mean. And yet sample variance can be computed in one pass through the data.
You’ll find two equivalent equations in statistics books: the one described above and another based on the sum of the data points and the sum of the data points squared.
While this equation is theoretically correct, it is numerically unstable. Code that directly implements this equation can return a negative value for a quantity that is theoretically positive. I’ve seen this happen with real data, causing a program to crash when taking the square root of the variance to get the standard deviation.
However, there is an algorithm that computes mean and variance in one pass that is accurate and numerically stable. This algorithm was developed by B. P. Welford in 1962. I discuss Welford’s algorithm and give code for implementing it
here
.
Online algorithms
Welford’s algorithm is known in computer science as an “online” algorithm. This term was coined well before the Internet. For example, see the paper [1] from 1965.
But of course now “online” means something else, and so the technical and colloquial uses of “online algorithm” have split. Technical literature uses the phrase to describe the kinds of algorithms in this post. Most people would take “online algorithm” to mean code that runs on a remote server. You may see “streaming algorithm” as a contemporary technical term, but I’d still search on “online algorithm” to find papers.
Computing higher moments online
Welford’s algorithm computes the first two moments, mean and variance, of a data set online. It is also possible to
compute skewness and kurtosis online
, as well as higher moments.
Online regression
Simple linear regression is closely related to calculating mean and variance, and it is possible to compute simple regression coefficients online. I have some old notes on this
here
.
This post was motivated by an email asking me about multiple regression. It is also possible to compute multiple regression coefficients online, but I haven’t done this. I found a couple references, [2] and [3], but I have not read them. There is a simple procedure for two predictor variables but I believe things get a little more complicated with three or more predictors, requiring a recursive least squares algorithm.
Related posts
The notion of online algorithms is closely related to the notion of a fold in functional programming. Here are several posts on computing things with folds.
[1] One-Tape, Off-Line Turing Machine Computations by F. C. Hennie. Information and Control. 8, 553-578 (1965). Available
here
. In this paper Hennie writes “In an
on-line computation
the input data are supplied to the machine, one symbol at a time, at a special input terminal. … In an
off-line computation
all of the input symbols are written on one of the machine’s tapes prior to the start of the computation.
[2] Arthur Albert and Robert W. Sittler, “A Method for Computing Least Squares Estimators that Keep Up with the Data,” Journal of the Society for Industrial and Applied Mathematics, Series A: Control, 3(3), 384–417, 1965. DOI: 10.1137/0303026.
[3] Petre Stoica and Per Ashgren. Exact initialization of the recursive least-squares algorithm. Int. J. Adapt. Control Signal Process. 2002; 16:219&ndashh;230.
