---
title: "Building complex functions out of real parts"
url: "https://www.johndcook.com/blog/2026/05/22/complex-functions-real-parts/"
fetched_at: 2026-05-23T07:01:05.929772+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Building complex functions out of real parts

Source: https://www.johndcook.com/blog/2026/05/22/complex-functions-real-parts/

A couple months ago
I wrote about how to compute the sine and cosine of a complex number using only real functions of real variables using the equations
You can do something analogous for all the elementary functions, though some of the equations are quite a bit more complicated than the ones above. See the equations
here
.
The equations come from a paper by Henry G. Baker, cited in the linked page. I wrote up Baker’s equations in LaTeX, then used ChatGPT to generate Python code from the LaTeX to numerically verify the equations and my typesetting of them. The test code evaluated the equations at points from each quadrant, implying that Baker and NumPy use the same branch cuts.
