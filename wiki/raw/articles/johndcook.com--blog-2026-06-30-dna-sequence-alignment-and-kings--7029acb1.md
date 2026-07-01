---
title: "DNA sequence alignment and Delannoy numbers"
url: "https://www.johndcook.com/blog/2026/06/30/dna-sequence-alignment-and-kings/"
fetched_at: 2026-07-01T07:00:52.868674+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# DNA sequence alignment and Delannoy numbers

Source: https://www.johndcook.com/blog/2026/06/30/dna-sequence-alignment-and-kings/

This morning
I wrote a post that included the central Delannoy numbers. The
n
th central Delannoy number
D
n
counts the number of ways a king can move from one corner of a chessboard to the diagonally opposite corner without backtracking.
The more general Delannoy numbers
D
m
,
n
are the analogy for an
m
×
n
rectangular board, not necessarily square.
D
m
,
n
is also the number of possible sequence alignments for a strand of DNA with
m
base pairs and a strand with
n
base pairs [1]. At each step in the alignment process, you can introduce a gap in the first strand, the second strand or neither, which is analogous to the king who can move N, E, or NE at each step.
The Delannoy numbers can be computed recursively:
def D(m, n):
    if m == 0 or n == 0:
        return 1
    return D(m - 1, n) + D(m, n - 1) + D(m - 1, n - 1)
The code above can be sped up tremendously by adding the decorator
@lru_cache(maxsize=None)
above the function definition to turn on memoization. I did an experiment computing
D
12,15
with and without memoization and the times were 77.1805 seconds and 0.000062 seconds respectively, i.e. memoization made the code over a million times faster.
Incidentally,
D
12,15
= 2653649025 and so there are a
lot
of ways to align even short sequences unless you place some restriction on the permissible alignments.
[1] Torres, A., Cabada, A., & Nieto, J. J. (2003). An exact formula for the number of alignments between two DNA sequences.
DNA Sequence, 14
(6), 427–430. https://doi.org/10.1080/10425170310001617894
