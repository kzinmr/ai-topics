---
title: "Refactoring factorials"
url: "https://www.johndcook.com/blog/2026/10/19/refactoring-factorials/"
fetched_at: 2026-10-20T10:01:30.606518+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Refactoring factorials

Source: https://www.johndcook.com/blog/2026/10/19/refactoring-factorials/

Splitting
N
! into
N
factors is trivial. It’s
defined
as the product of
N
integers, the integers 1 through
N
.
Can you still split
N
! into
N
factors if you put a minimum size requirement on the factors?
You can’t split 3! into three factors unless one of the factors is 1, but you can split 4! into factors ≥ 2:
4! = 24 = 2 × 2 × 2 × 3
Define
t
(
N
) as the largest number such that
N
! can be expressed as the product of integers greater than or equal to
t
(
N
). So based on the discussion above,
t
(
N
) ≥ 1 for all
N
,
t
(3) = 1 and
t
(4) = 2. The
t
(
N
) are given in OEIS sequence
A034258
.
Last Thursday an
article
came out proving an asymptotic estimate for
t
(
N
). You can find a
preprint
on arXiv.
An upper bound on
t
(
N
) would be the
N
th root of
N
! because that would correspond to splitting
N
! into
N
factors of equal size. But the
N
th root of
N
! will not be an integer for
N
> 1, so the bound would not be tight.
If we apply Stirling’s approximation for factorial we get
t
(
N
) /
N
≤ 1/
e
+
O
(log(
N
) /
N
).
It was conjectured that for large
N
t
(
N
) /
N
∼ 1/
e
−
c
0
/ log(
N
)
and the new paper proves
t
(
N
) /
N
∼ 1/
e
−
c
0
/ log(
N
) +
O
(1 / log
1 +
c
N
).
.
