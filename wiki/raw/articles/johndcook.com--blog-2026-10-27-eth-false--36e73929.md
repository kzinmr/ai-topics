---
title: "The Exponential Time Hypothesis is False"
url: "https://www.johndcook.com/blog/2026/10/27/eth-false/"
fetched_at: 2026-10-28T10:01:25.719783+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# The Exponential Time Hypothesis is False

Source: https://www.johndcook.com/blog/2026/10/27/eth-false/

If you have an expression in
n
Boolean variables, how long does it take to find out whether some assignment of values to the variables makes the expression true? There is an obvious upper bound: you can find out in 2
n
steps by exhaustive search, trying all possible ways of setting each variable to true or false.
You can often do better than exhaustive search for a particular problem, but can you
always
do better, even in the worst case? The Monien–Speckenmeyer branching algorithm, published in 1985, is more efficient than exhaustive search, but it still takes exponential time.
3-SAT
The Boolean satisfiability problem (SAT) asks whether a Boolean expression in conjunctive normal form (
CNF
) can be satisfied by some assignment of values to the variables. The
k
-SAT problem is the special case of SAT in which no clause contains more than
k
variables. The 2-SAT problem can be solved in polynomial time, but the case of the 3-SAT problem is unknown.
The 3-SAT problem is NP-complete, and so if there is a polynomial-time algorithm for solving 3-SAT, every NP problem, including the full SAT problem, can be solved in polynomial time, i.e. P = NP.
The Monien–Speckenmeyer algorithm mentioned above can solve a 3-SAT problem in
O
( |
F
| φ
n
)
time, where |
F
| is the length of the input formula and φ is the golden ratio. Now φ < 2, and so this is better than exhaustive search, but the run time is still exponential in the number of variables
n
.
ETH
The exponential time hypothesis (ETH) claims that 3-SAT requires exponential time, which would imply P ≠ NP.
Anthropic
and
OpenAI
have both published proofs that ETH is false. The status of P = NP is still unknown: while 3-SAT does not take exponential time, it still takes more than polynomial time as far as anyone knows.
Yesterday Shiva Kintali posted
A simplified proof of ETH is false
. The abstract of the paper says
For every fixed ε > 0, we give a deterministic 3-SAT algorithm on
n
variables and
m
clauses using
C
ε
(
n
+
m
+ 1)
c
ε
2
εn
bit operations, refuting ETH. Our simplified exposition of OpenAI’s proof combines sparsification, bounded occurrences, spectral replacement, and rational interpolation.
Related posts
