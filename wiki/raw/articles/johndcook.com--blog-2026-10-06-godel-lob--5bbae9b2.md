---
title: "A topological model for provability logic"
url: "https://www.johndcook.com/blog/2026/10/06/godel-lob/"
fetched_at: 2026-10-07T10:01:27.132916+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# A topological model for provability logic

Source: https://www.johndcook.com/blog/2026/10/06/godel-lob/

Gödel’s incompleteness theorem illustrated the need to distinguish between what is true and what is provable. There are true statements that cannot be proven.
Let □
p
denote the assertion that
p
is provable in Peano arithmetic. The logic with this interpretation for the □ operator is the Gödel-Löb logic, also called provability logic. This is a normal modal logic with the additional axiom
□(□
p
→
p
) → □
p
,
known as Löb’s axiom.
A couple days ago I wrote about
topological models
for modal logic. Is there a topological model for Gödel-Löb logic? There is, but it’s not quite the same construction as in the previous post.
A topological model of Gödel-Löb logic associates
p
with a set
P
and ◇
p
with the
derived set
of
P
rather than its closure.
The difference between the closure of
P
and the derived set of
P
is subtle, but important to this discussion. The closure of a set
P
is the union of
P
and all of its limit points. The derived set of
P
is the set of limit points of
P
. The distinction is that not every point of
P
is necessarily a limit point of
P
. A point
x
is a limit point of
P
if every open set containing
x
contains a point of
P
in addition to x itself
.
A topological space
X
that models Gödel-Löb logic must be
scattered
, meaning that every open set must contain an isolated point, a point with no limit points. For example, consider
X
= {0} ∪ {1, ½, ⅓, ¼, …}
with the topology inherited from the ordinary topology on the real line. Then every point except 0 is isolated, and every open set contains isolated points.
A statement in Gödel-Löb logic is true if its topological interpretation holds for
all
scattered spaces.
