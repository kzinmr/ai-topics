---
title: "The Unbalanced Group Theorem"
url: "https://www.johndcook.com/blog/2026/10/28/the-unbalanced-group-theorem/"
fetched_at: 2026-10-29T10:01:27.311831+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# The Unbalanced Group Theorem

Source: https://www.johndcook.com/blog/2026/10/28/the-unbalanced-group-theorem/

The classification of finite simple groups (CFSG) has been called the biggest theorem in mathematics. It is big, not necessarily in terms of its importance, but in the sense that its proof developed over the course of decades and thousands of pages of journal articles.
Two days ago
Axiom
announced it had formalized the proof of CFSG in 43.1 million lines of Lean. If you click on the link for the accompanying paper, you’ll find that the title of the paper is
The Unbalanced Group Theorem
, not The Classification of Finite Simple Groups. Why is that?
The unbalanced group theorem (UGT) is a key component of the CFSG. In the course of their effort to formalize CFSG Axiom found counterexamples to an assertion that the 1986 proof of UGT depends on. The UGT, and the CFSG that depends on it, is correct, but the proof was flawed. Axiom formalized the entire CFSG but focused their paper on their new proof of the UGT.
***
What exactly does the UGT say? For that matter, what is a finite simple group?
A short post like this can only go into so much detail, but I’ll see what I can do.
A group represents some kind of symmetry. Groups can be built out of simple groups sorta like the way integers can be built out of primes. See more on the comparison between simple groups and prime numbers
here
.
The CFSG says that every finite simple group is cyclic, alternating, of Lie type, or sporadic. The UGT is a technical result used in proving that nothing is missing from this list of possibilities.
What does it mean for a group to be “unbalanced”? This depends on a few preliminary definitions.
Define
O
(
G
) to be the largest normal subgroup of
G
with an odd number of elements.
An element
t
in
G
is called an involution if it has order 2:
t
is not the identity but
t
² is.
The centralizer of an element
t
of a group
G
, written
C
G
(
t
), is the set of elements of G that commute with
t
.
A group
G
is
unbalanced
if
O
(
C
G
(
t
)) is a not a subgroup of
O
(
G
) for some involution
t
.
The UGT is a classification theorem for unbalanced groups.
Related posts
