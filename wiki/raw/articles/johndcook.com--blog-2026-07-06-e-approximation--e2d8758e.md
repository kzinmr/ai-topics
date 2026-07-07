---
title: "e approximation"
url: "https://www.johndcook.com/blog/2026/07/06/e-approximation/"
fetched_at: 2026-07-07T07:01:41.527994+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# e approximation

Source: https://www.johndcook.com/blog/2026/07/06/e-approximation/

I ran across the approximation
e
≈ 2721/1001
recently. What makes this remarkable is its accuracy relative to the size of the denominator.
You can create a trivial approximation just by truncating a decimal expansion
e
≈ 2718/1000
but this is only good to four significant figures, but 2721/1001 is good to seven, almost eight, significant figures.
e         = 2.71828182… 
2721/1001 = 2.71828171…
The comparison is more impressive in binary.
$ bc -l
>>> obase=2
>>> 2721/1001
10.10110111111000010100…
>>> e(1)
10.10110111111000010101…
The denominator is a 10-bit number but the approximation is accurate to 21 bits.
