---
title: "Pythagorean Addition"
url: "https://entropicthoughts.com/pythagorean-addition"
fetched_at: 2026-05-19T07:01:16.642838+00:00
source: "entropicthoughts.com"
tags: [blog, raw]
---

# Pythagorean Addition

Source: https://entropicthoughts.com/pythagorean-addition

It turns out I’m not the first person to have thought about this. There’s a
research paper out of
ibm
from the early 1980’s where the authors have come up
with a method for computers to evaluate ⊞ with a high rate of
convergence.
1
Replacing Square Roots by Pythagorean Sums
; Moler & Morrison;
ibm
Journal of Research and Development; 1981.
The method is
very
cool.
Given a point (x,y), the authors have found a way to nudge that point along the
radius of a circle down toward the abscissa, so that when the y-value is
sufficiently small, the x-value is equal to the radius. However, iterative
algorithms like this aren’t well suited for mental arithmetic.
2
I do hear
about people who can refine approximations by running a couple of iterations of
Newton–Raphson in their heads. I want to be like those people, but I am not.
However, there’s also a great method to do it as a human. To evaluate \(a ⊞ b\),
assuming \(a\) is the larger number (if it is not, swap them):
Compute \(\hat{c} = 0.9a + 0.5b\).
If \(\hat{c}\) is smaller than \(a\), set \(\hat{c} = a\).
Done! That’s the result.
This is an estimation and it does come with an error, but the error is at worst
3 %, and on average it is 1.5 %. That’s remarkable for such an easy procedure.
To be clear, we are only shaving a tenth off of the larger number, and adding
back in half of the smaller number, and this is very close to being the square
root of the sum of their squares!
The reason this method is called
alpha-max plus beta-min
is that while we used
\(\alpha=0.9\) and \(\beta=0.5\) because that was convenient for mental maths, other
parameters exist, and some are slightly more accurate.
