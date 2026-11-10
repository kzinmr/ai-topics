---
title: "Combinatorial designs"
url: "https://www.johndcook.com/blog/2026/11/09/combinatorial-designs/"
fetched_at: 2026-11-10T10:01:16.199289+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Combinatorial designs

Source: https://www.johndcook.com/blog/2026/11/09/combinatorial-designs/

The last several posts have been building up to this one, moving from tangible to more abstract.
The posts on
finite geometry
gave examples of Steiner triples and more generally Steiner systems, introduced in the
previous post
. Combinatorial designs take this one step further.
The previous post gave the following definition:
A Steiner triple system, written STS(
n
), is a collection of
three
-element subsets, called blocks, of a set
X
with
n
elements, such that every
two
-element subset of
X
belongs to exactly
one
block.
The post pointed out that the smallest projective plane is STS(7) and the smallest affine plane is STS(9).
The post then defined a general Steiner system:
A Steiner system
S
(
t
,
k
,
n
) is a collection of
k
-element subsets, called blocks, of a set
X
with
n
elements, such that every
t
-element subset of
X
belongs to exactly
one
block.
Moving from Steiner triples to Steiner systems we generalized the size of the blocks from 3 to
k
, and generalized the size of sets contained in a unique block from 2 to
t
.
Combinatorial designs take this one step further by generalizing the number of blocks that a set of
t
elements falls in from 1 to λ.
Unfortunately when we go from Steiner systems to combinatorial designs the notation changes and the order of the parameters changes.
A design with parameters (
n
,
q
,
r
, λ) is a collection of
q
-element subsets of an
n
-element set
X
such that every
r
-element subset of
X
is contained in exactly λ blocks.
So a Steiner system
S
(
t
,
k
,
n
) corresponds to a (
n
,
k
,
t
, 1) design.
Existence of designs
Given a set of parameters (
n
,
q
,
r
, λ) there may or may not exist a design with these parameters. It’s easy to show that a few consistency conditions are necessary. It was long conjectured that these conditions were sufficient, except possibly for a finite number of values of
n
. Peter Keevash proved in 2024 that the conjecture is correct.
Theorem [1]: Fix
q
>
r
≥ 1 and λ ≥ 1. There is an
N
, depending on
q
,
r
, and λ, such that for every
n
>
N
with
for all 0 ≤
i
≤
r
, a design with parameters (
n
,
q
,
r
, λ) exists.
[1] Peter Keevash. The existence of designs. https://arxiv.org/abs/1401.3665v4
