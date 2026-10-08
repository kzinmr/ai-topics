---
title: "Faster Fourier Transform"
url: "https://www.johndcook.com/blog/2026/10/07/faster-fourier-transform/"
fetched_at: 2026-10-08T10:01:34.692877+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Faster Fourier Transform

Source: https://www.johndcook.com/blog/2026/10/07/faster-fourier-transform/

The Fast Fourier Transform (FFT) algorithm can compute the discrete Fourier transform of a sequence of length
n
in time
O
(
n
log
n
).
OpenAI
recently posted a paper saying there is an algorithm that could compute the discrete Fourier transform in
O
(
n
(log
n
)
1 − ε
)
time for ε = 10
−13
.
This result is amazing. It seemed that
O
(
n
log
n
) was as good as you could do, which it provably is for sorting algorithms.
The result is also of absolutely no practical value, for now. But since the theorem shows that our assumptions were wrong, however slightly, about what is possible, maybe we’re in for further surprises. Maybe the ε crack will grow. It wouldn’t be the first time.
Related posts
