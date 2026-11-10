---
title: "Steiner Systems"
url: "https://www.johndcook.com/blog/2026/11/09/steiner-systems/"
fetched_at: 2026-11-10T10:01:16.218297+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Steiner Systems

Source: https://www.johndcook.com/blog/2026/11/09/steiner-systems/

Steiner triples
Several examples from the
recent
posts
on finite geometry are special cases of Steiner triples.
A Steiner triple system, written STS(
n
), is a collection of three-element subsets, called blocks, of a set
X
with
n
elements, such that every two-element subset of
X
belongs to exactly one block.
STS(7) is the smallest finite projective plane, the Fano plane, and STS(9) is the smallest finite affine plane. In both cases you interpret the elements of
S
as points and the blocks as lines.
Several questions come up naturally. First, for which values of
n
does an STS(
n
) exist? A necessary and sufficient condition for existence is that
n
= 1 or 3 mod 6.
For a given
n
, can there be more than one STS(
n
), i.e. are there Steiner triple systems of the same size that are not isomorphic? Yes indeed. The number of non-isomorphic instances grows rapidly with
n
.
When does (some instance of) STS(
n
) correspond to a projective or affine space? When
n
= 2
k
− 1 for
k
≥ 3. For
n
≥ 13 there are multiple isomorphism classes of STS(
n
), so for
k
> 3 there will be an instance of STS(2
k
− 1) that corresponds to a projective space and other instances that do not. The instance that does correspond to a projective plane will be isomorphic to a finite field analog of the real projective plane.
Steiner systems
Steiner triple systems are a special case of Steiner systems.
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
elements, such that every t-element subset of
X
belongs to exactly one block. Steiner triples are
S
(2, 3,
n
) systems.
Steiner systems often correspond to finite geometries with the blocks interpreted as lines. As with the special case of triples, there can be non-isomorphic instances of Steiner systems, and so when I say below that
S
(
t
,
k
,
n
) corresponds to a certain geometry, I mean that at least one instance corresponds to that geometry.
Projective
The Steiner system
S
(2,
q
+ 1, (
q
d
+ 1
− 1)/(
q
− 1))
with
q
a prime power greater than 2 is a
d
-dimensional projective space.
Affine
The space
S
(2,
q
,
q
d
)
is an affine space. Again
q
> 2 is a prime power.
Hyperbolic
The finite hyperbolic plane given as an example in an earlier post corresponds to
S
(2, 2, 6). Many other Steiner systems are hyperbolic, but I’m not aware of a tidy classification similar to the ones above.
Steiner systems outside geometry
Steiner systems were named after Swiss mathematician Jakob Steiner because he published a highly cited article asking questions about what we now call Steiner triples. His interest in these systems was combinatorial. Others developed the connections to geometry later.
Steiner systems arise in several areas of mathematics outside of geometry, including coding theory, design of experiments, and graph theory.
