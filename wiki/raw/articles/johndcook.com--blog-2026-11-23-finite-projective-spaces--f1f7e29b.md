---
title: "Finite Projective Spaces"
url: "https://www.johndcook.com/blog/2026/11/23/finite-projective-spaces/"
fetched_at: 2026-11-24T10:01:25.819671+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Finite Projective Spaces

Source: https://www.johndcook.com/blog/2026/11/23/finite-projective-spaces/

Just as there are
finite projective planes
, there are also finite projective spaces of higher dimension.
The axioms of a projective space are
Any two distinct points lie on exactly one line.
If
A
,
B
,
C
, and
D
are distinct points and the lines
AB
and
CD
meet, then the lines
AC
and
BD
also meet.
Every line contains at least three points.
There are at least two lines.
The second axiom is subtly different from its counterpart for projective planes. It allows for skew lines but not parallel lines. There’s no explicit concept of dimension in these axioms, but dimension can be well-defined by induction.
What I find most interesting about finite projective spaces is that they are in some sense simpler than projective planes. Usually higher dimensions allow for more complicated behavior, but at least as far as classification goes, higher dimensional spaces are simpler.
Finite projective planes are not determined by the number of points they contain. As mentioned in
this post
, there are four different projective planes with 10 points. It is unknown how many different projective planes there are with 17 points; there are at least 22. But for dimension
d
≥ 3, there is at most one projective space with a specified number of points.
Given a prime power
q
, there is a unique field
F
with
q
elements, and one can construct a projective space of dimension
d
over
F
analogously to how one constructs a real projective space of dimension
d
: Take the non-zero vectors in
F
d
+ 1
and mod out by non-zero scalar multiples. And up to isomorphism this is the
only
way to construct a finite projective space if
d
≥ 3. In technical terms, finite projective planes can be non-Desarguesian but higher-dimensionsal projective spaces cannot.
Related posts
