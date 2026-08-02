---
title: "Why polynomial coefficients?"
url: "https://www.johndcook.com/blog/2026/08/01/why-polynomial-coefficients/"
fetched_at: 2026-08-02T10:14:20.262727+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Why polynomial coefficients?

Source: https://www.johndcook.com/blog/2026/08/01/why-polynomial-coefficients/

Second order linear differential equations with polynomial coefficients form their own area of study. This seems like a narrow class of equations, but it’s very important in applications.
This class of equations seems like a mathematically natural topic, but why is it so important in applications? I did a PhD in differential equations without ever learning why. The theory of second order linear equations with polynomial coefficients is too complicated for undergraduate courses [0] and too well-established for graduate courses [1].
The explanation that I was missing can be found in the first chapter of [2]. The PDEs that are common in physics are separable in various coordinate systems, meaning that in these coordinate systems the PDEs reduce to ODEs. These ODEs either have polynomial coefficients, or there is a change of variables which makes the ODEs have polynomial coefficients.
See this
writeup
that looks at the Helmholtz and Laplace equations in 11 coordinate systems.
[0] You may see the simplest parts of the theory in a section on solving ODEs with power series. But textbooks don’t go very far for good reasons.
[1] Unfortunately, a lot of really useful topics are left out of the graduate curriculum because they’re too well understood to provide thesis topics. Or the problems that are still open have been open for so long that they’re likely too hard to be cracked by a graduate student.
[2] Gerhard Kristensson. Second Order Differential Equations: Special Functions and their Classification. Springer, 2010.
