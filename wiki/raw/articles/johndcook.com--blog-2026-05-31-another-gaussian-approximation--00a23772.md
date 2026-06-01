---
title: "Another Gaussian approximation"
url: "https://www.johndcook.com/blog/2026/05/31/another-gaussian-approximation/"
fetched_at: 2026-06-01T07:14:09.640748+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Another Gaussian approximation

Source: https://www.johndcook.com/blog/2026/05/31/another-gaussian-approximation/

The function
(1 + cos(
x
))/2
gives a fair approximation to the Gaussian density
exp(−
x
²)
You can make the approximation much better by raising it to a power. The function
((1 + cos(
x
))/2)
4
gives a good lower bound and
((1 + cos(
x
))/2)
3.5597
gives a good upper bound. More on that
here
.
There are other ways of improving the cosine approximation to the Gaussian.
Yesterday
I came across one I hadn’t seen before, adding a sin(
x
) term to
x
.
(1 + cos(sin(
x
) +
x
))/2
This function matches the first few terms of the power series for exp(−
x
²) and has an error on the order of
x
6
/240. You can’t see the difference between the two functions in a plot for −4 ≤
x
≤ 4.
***
There’s a tension between the previous two statements. If the error in on the order of
x
6
/240 then we’d expect the error to be huge at
x
= 4. We have
4
6
/240 = 17.07
and yet
exp(−4²) − ((1 + cos(4 + sin(4)))/2) = −0.002579,
i.e. the error is between 3 and 4 orders of magnitude smaller than we might expect.
We have an alternating series, so the truncation error should be roughly equal to the first term after the truncation, right? No, the alternating series theorem doesn’t apply because the absolute values of the terms in the series are not decreasing yet for
x
= 4. The terms have to decrease eventually because the series has infinite radius of convergence, but they’re not decreasing at the 6th term; the terms will get much larger in absolute value before they get smaller.
The basic alternating series theorem gives only an upper bound on truncation error, but there are extensions that also give a lower bound. I wrote about these
extensions
a few weeks ago. But these extentions don’t apply here because the terms have not started decreasing in absolute value.
