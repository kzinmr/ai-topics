---
title: "Topological models of modal logic"
url: "https://www.johndcook.com/blog/2026/10/04/topological-models-of-modal-logic/"
fetched_at: 2026-10-05T10:08:35.694156+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Topological models of modal logic

Source: https://www.johndcook.com/blog/2026/10/04/topological-models-of-modal-logic/

The
previous post
discussed a superficial connection between modal logic and topology, that both use the terms
regular
and
normal
to indicate added sets of axioms. McKinsey and Tarski developed a deeper connection between modal logic and topology that we’ll discuss here.
Starting with a topological space
X
and a proposition
p
, define [[
p
]] as the set of points in
X
at which
p
is true. Define □
p
to be true at points in the interior of [[
p
]] and define ◇
p
to be true on the closure of [[
p
]].
You could think of □
p
as the points where
p
is robustly true. Not only is
p
true at
x
, there’s some wiggle room around
x
, i.e. an open set, in which
p
remains true.
You could think of ◇
p
as the points where we cannot rule out the possibility of
p
being true using open sets. If ◇
p
includes
x
, any open set containing
x
also contains part of ◇
p
, though it may also contain points outside of ◇
p.
Regularity
For any topology on
X
, the logic constructed above is normal. The axiom
◇
p
⇔ ¬ (□ ¬
p
)
holds because the closure of a set is the complement of the interior of its complement [1].
Note that this is a regularity result for the modal logic, not the topology. The topology could be arbitrary, and not necessarily regular or normal in the topological sense.
S4
The logic constructed above also satisfies a couple more axioms. We have
□
p
→
p
because the interior of a set is a subset of the set, and
□
p
→ □□
p
because the interior of the interior of a set is simply the interior. This means the modal logic corresponding to a topology satisfies the S4 axioms. You could say S4 is the logic that corresponds to the McKinsey and Tarski logic of all topological spaces.
More logics and more topologies
So S4 is the logic that corresponds to
all
topologies. We could look at more restricted topologies and ask what are their corresponding logics. Or we could start with a modal logic and ask whether there’s a topology that models that logic.
Interesting logics correspond to badly behaved topological spaces. Familiar topological spaces like the real line correspond to S4.
Trivial modal logic
The discrete topology corresponds to the trivial modal logic. All sets are open, and closed, so any set is the same as its interior and its closure. So □
p
and ◇
p
reduce to just
p
.
S5
For the indiscrete topology, □
p
corresponds to a proposition holding everywhere and ◇
p
corresponds to it holding somewhere. If the topological space has infinitely many points, the corresponding modal logic is S5. [2]
Between S4 and S5
The cofinite topology on an infinite set
X
defines a set
U
to be open if the complement of
U
is finite. The McKinsey-Tarski logic of the cofinite topology is somewhere between S4 and S5. You can show that the formula
p
∧ ◇□
p
→ □
p
holds, which doesn’t hold in S4, and the formula
◇
p
→ □◇
p
does not hold, though it must hold in S5.
Related posts
[1] We should also verify that if
A
∩
B
⊂
C
, then Interior(
A
) ∩ Interior(
B
) ⊂ Interior(
C
).
[2] Propositions can only have a finite number of terms. Having infinite points in the topological space prevents the corresponding logic from proving theorems that don’t necessarily hold in S5.
