---
title: "Radix sort and 32-bit IEEE754 floating point numbers."
url: "https://iczelia.net/posts/radix-float/"
fetched_at: 2026-05-05T07:01:19.391536+00:00
source: "Kamila Szewczyk (iczelia)"
tags: [blog, raw]
---

# Radix sort and 32-bit IEEE754 floating point numbers.

Source: https://iczelia.net/posts/radix-float/

Background
⌗
The computational complexity of an optimal sorting algorithm based on comparisons is
O
(
n
log
⁡
n
)
\mathcal O(n \log n)
O
(
n
lo
g
n
)
. We can prove this by reducing the problem of sorting an array to finding the permutation vector that sorts it. There are
n
!
n!
n
!
possible permutations of the set
{
1
,
2
,
…
,
n
}
\{1, 2, \ldots, n\}
{
1
,
2
,
…
,
n
}
. Each comparison can at best halve the search space of the sorting algorithm. Hence, the amount of comparisons done by an optimal comparison sort is at least
log
⁡
2
(
n
!
)
=
O
(
n
log
⁡
n
)
\log_2 (n!) = \mathcal O(n \log n)
lo
g
2
​
(
n
!)
=
O
(
n
lo
g
n
)
.
Indeed, one such algorithm - the
heap sort
- attains the
O
(
n
log
⁡
n
)
\mathcal O(n \log n)
O
(
n
lo
g
n
)
bound and is used by many sorting routines under the bonnet. To avoid unnecessarily discussing the underlying methods which are already explained great detail by algorithm books and other online resources, I will not provide an abstract explanation of the algorithm, focusing on the implementation:
The heap sort algorithm is pretty slow in practice. Another common algorithm -
quicksort
- doesn’t provide as lucrative guarantees, but generally runs faster than the alternatives:
We can run a simple benchmark to demonstrate this:
On my machine, I get the following timings:
heap sort: 15121146414 cycles, 4.590787 seconds (901 cycles/element)
quick sort: 4824085530 cycles, 1.464595 seconds (287 cycles/element)
More efficient algorithms like TimSort would be able to take better advantage of what linearithmic comparison-based sorts have to offer, but we will cut this story short for now - its performance will
still
be significantly worse than the best we can do.
IEEE754 floats
⌗
Assuming non-degenerate data (i.e. no
NaN
s, infinities, etc.) we can sort IEEE754 floats via naive memory comparisons. This motivates the following concise implementation of the
radix sort
algorithm, which attains linear time:
An alternative implementation of the same idea involves being a bit more wasteful with stack space to avoid superfluous memory accesses and allow batching of operations:
The new timings (including the radix sorts) follow:
radix sort: 352613448 cycles, 0.107044 seconds
radix2 sort: 508113969 cycles, 0.154266 seconds
heap sort: 15164556891 cycles, 4.603966 seconds
quick sort: 4501389717 cycles, 1.366624 seconds
The radix sort implementation is approximately 12 times faster.
