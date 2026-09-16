---
title: "Simple approximation for spherical cap area"
url: "https://www.johndcook.com/blog/2026/09/15/simple-approximation-for-spherical-cap-area/"
fetched_at: 2026-09-16T10:01:33.660128+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Simple approximation for spherical cap area

Source: https://www.johndcook.com/blog/2026/09/15/simple-approximation-for-spherical-cap-area/

The
previous post
looked at how to interpret cosine similarity, or equivalently angles between word vectors. In a high-dimensional space, randomly chosen vectors are likely nearly perpendicular, and so relatively large angles, such as 50°, indicate very closely related words.
Another way to look at this, as explained in the previous post, is that in high dimensions, a spherical cap of angular radius θ represents a small portion of a sphere, even for moderately large θ.
The proportion of the area inside the spherical cap, given
here
, involves the “regularized incomplete beta function” and so it’s hard to have an intuition for the value.
For large dimension
n
, the approximation
n
−1/2
sin
n
− 1
(θ)
gives the proportion of the area inside the cap to within an order of magnitude. It’s easy to see that this function goes to zero quickly as
n
increases, provided |θ| < π/2.
If you have the cosine similarity
c
= cos θ rather than θ itself, the approximation becomes
n
−1/2
(1 −
c
²)
(
n
− 1)/2
.
Python script
Let’s try it on the example from the previous post, in which
n
= 200 and θ = 49°.
import numpy as np
from scipy.special import betainc

# Fraction of S^{n-1} inside a spherical cap of angular radius theta
# theta is measured from the pole
# Assume 0 < theta < pi/2

def cap_fraction(theta, n):
    x = np.sin(theta) ** 2
    return 0.5 * betainc(0.5 * (n - 1), 0.5, x)

def cap_fraction_approx(theta, n, degrees=False):
    return n**(-0.5) * np.sin(theta)**(n-1)

theta = np.deg2rad(49)
print(cap_fraction(theta, 200)) 
print(cap_fraction_approx(theta, 200))
This prints 2.03e-26 and 3.37e-26. The order of magnitude is correct as advertised.
