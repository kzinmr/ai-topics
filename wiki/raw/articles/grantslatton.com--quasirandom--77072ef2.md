---
title: "Quasirandom sequences"
url: "https://grantslatton.com/quasirandom"
fetched_at: 2026-04-29T07:02:17.053679+00:00
source: "grantslatton.com"
tags: [blog, raw]
---

# Quasirandom sequences

Source: https://grantslatton.com/quasirandom

Quasirandom sequences
Pseudorandom points on the left. Quasirandom points on the right.
Pseudorandom number generators
PRNGs are useful when you want to generate values that simulate "real" randomness. Real life random values can be "clumpy" — if you flip a coin 1000 times, you can get a long run of the same face.
Quasirandom number generators
Sometimes the clumpiness of PRNGs is undesirable. QRNGs generate numbers that fill the space with roughly uniform density. This is really useful for processes that would like to explore a space exhaustively, but can't due to unmanageable cardinality. The most common process in this class is a monte-carlo simulation.
If you can't explore exhaustively, often the next best thing is to explore uniformly. The easiest way to uniformly explore a space is with a grid search, but a grid search can lead to statistical artifacts if the problem domain has contours that happen to align to your grid.
QRNGs are a tool that enables roughly uniform exploration while mitigating the risk of correlation between the sampled points and the space being explored.
QRNG's uniform coverage results in a faster-converging monte-carlo simulation. After \(n\) iterations, a PRNG-based monte-carlo will have an error proportional to \(\frac{1}{\sqrt{n}}\), whereas a QRNG-based one will have an error proportional to \(\frac{1}{n}\).
Rust library
I first heard about quasirandom sequences from
this blog post
by Martin Roberts when
it got posted to HN
.
With Rust being my
langue du jour
, I checked
crates.io
and didn't find any existing packages with the functionality, so I implemented and published the
quasirandom
crate.
How it works
Consider the positive real numbers under addition modulo 1. That is, consider the numbers in the range \([0, 1)\) that, when added together, "wrap back around" when they exceed 1 (e.g. \(0.5 + 0.7 = 0.2\)).
Consider the function
$$ f(x, n) = \{ ix \bmod 1\ \mid i = 0, 1, \ldots n \}, \ x \in \mathbb{R}_{\left[0,1\right)}, \ n \in \mathbb{N} $$
As \(n \to \infty\), what value of \(x\) minimizes the average distance between an element's closest neighbors to the left and right?
If \(x\) is rational, the cardinality of the set is finite and the distance between neighbors is the reciprocal of the cardinality. For example, consider \(x = 0.2\).
$$ f(0.2) = \{0.0, 0.2, 0.4, 0.6, 0.8\} $$
If \(x\) is irrational, the cardinality of the set is infinite and the average distance will always approach 0, so if \(n \gg \frac{1}{x}\), any irrational \(x\) will work decently well.
But which one does the
best
? It turns out to be the golden ratio.
$$ \phi = 0.618033\ldots $$
Nonetheless, in the 1-dimensional case, the difference in performance between the golden ratio and any other irrational is insignificant. It's the multidimensional case where Martin's method really shines.
Martin defines a \(d\)-dimensional generalization of the golden ratio.
$$ \phi_d \ \textrm{is the unique positive root of} \ x^{d+1} = x + 1 $$
Then, a generator \(d\)-tuple can be defined
$$ (\phi_d^1, \ \phi_d^2, \enspace \ldots \phi_d^d) $$
The \(i\textrm{-th}\) value of the generated sequence is simply
$$ (n \ \phi_d^1, \ i \ \phi_d^2, \enspace \ldots i \ \phi_d^d) \ \textrm{mod} \ 1 $$
I don't believe there is a general closed-form solution for \(\phi_d\), so I also included some code to find it by binary search.
My library is mostly just a thin wrapper around a table of pre-computed \(\phi_d^i\) values for \(1 \leq d \leq 32 \) and a helper interface for converting from floats in the range \(\left[0, 1\right)\) to arbitrary types.
If you are interested in seeing "advanced" Rust macros, there is some
interesting macro magic
to generate the 32 tuple implementations in a short amount of code.
