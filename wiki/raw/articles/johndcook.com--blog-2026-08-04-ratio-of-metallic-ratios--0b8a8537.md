---
title: "Ratio of metallic ratios"
url: "https://www.johndcook.com/blog/2026/08/04/ratio-of-metallic-ratios/"
fetched_at: 2026-08-05T10:12:32.638450+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Ratio of metallic ratios

Source: https://www.johndcook.com/blog/2026/08/04/ratio-of-metallic-ratios/

The golden ratio is the first and best known of the metallic ratios. I’ve written about the silver ratio a few times, most recently
here
. And I’ve mentioned the
bronze ratio
a couple times. The metallic ratios after bronze don’t have standard names.
The
n
th metallic ratio
M
(
n
) is the number whose continued fraction representation contains all
n
s.
When
n
= 1, 2, and 3 we get the gold, silver, and bronze ratios.
You can approximate any positive real number as a ratio of metallic ratios. To see this, note that for large
n
,
M
(
n
) is approximately
n
. For any positive rational number
a
/
b
,
and so you can make
M
(
na
) /
M
(
nb
) as close to
a
/
b
as you like by taking
n
large enough. And since the rationals are dense in the reals, you can approximate any positive real number as close as you’d like.
Let’s look for metallic ratios whose ratios approximate π to within 0.001 with the following Python code.
from math import pi, sqrt

M = lambda n: 0.5*(n + sqrt(n**2 + 4))

for n in range(1, 100):
    a = round(pi*n)
    b = n
    r = M(a)/M(b)
    if abs(r - pi) < 0.001:
        print(a, b, r)
This shows
π ≈
M
(132) /
M
(42) = 3.1412…
Could we find smaller numbers that work? The following code shows the answer is no.
k = 132 + 42
# loop over numbers whose sum is less than k
for n in range(1, k):
    for a in range(1, n):
        b = n - a
        r = M(a)/M(b)
        if abs(r - pi) < 0.001:
            print(a, b, r)
            exit()
Related posts
