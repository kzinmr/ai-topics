---
title: "Modal logic and topology"
url: "https://www.johndcook.com/blog/2026/10/04/modal-topology/"
fetched_at: 2026-10-05T10:08:35.705600+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Modal logic and topology

Source: https://www.johndcook.com/blog/2026/10/04/modal-topology/

You can’t say much about modal logic in general. You have to be more specific to get anywhere. You have to choose some axioms. Ideally the axioms you need for your application correspond to a named set of axioms that has been studied before.
The situation is similar in point-set topology. You can’t say very much about a general topological space. You have to specify some separation axioms to get going.
Bare bones
Modal logic
A modal logic is any set of formulas in the modal language that:
contains all propositional tautologies,
is closed under modus ponens, and
is closed under uniform substitution.
In particular, this definition requires
nothing
of the modal operator □ (“box”). You just have propositional logic with a funny symbol added that could mean anything.
Topology
A topological space is a set
X
along with a set of subsets of
X
called open sets. The empty set and the full space
X
are open sets. Furthermore, the set of open sets is closed under finite intersections and arbitrary unions.
There’s not much you can say about topological spaces in general because, for example, the definition includes extreme cases such as the discrete topology (every subset of
X
is open) and the indiscrete topology (only the empty set and
X
are open).
Regular and normal
Like many areas of mathematics, logic and topology use the terms “regular” and “normal” to refer to systems with common choices of extra structure.
Modal logic
A regular modal logic is a normal modal logic with a second modal operator ◇ (“diamond”) that satisfies
◇
p
⇔ ¬ (□ ¬
p
)
and has the inference rule (
p
∧
q
) →
r
implies (□
p
∧ □
q
) → □
r.
A modal logic is normal if it satisfies the axiom
□ (
p
→
q
) → (□
p
→ □
q
)
and the inference rule that if
p
is a theorem, □
p
is also a theorem.
Topology
Topology also uses
regular
and
normal
to refer to adding a few axioms.
A regular topological space is one in which you can separate points from closed sets. Given a point
x
and a closed set
F
not containing
x
, there exist disjoint open sets
U
and
V
such that
x
is contained in
U
and
F
is contained in
V
. [1]
A normal topological space is one in which you can separate disjoint closed sets.
For many mathematicians, a metric space is the weakest topology they’re interested in, and metric spaces are normal. But weaker topologies come up. The Zariski topology in algebraic geometry is not regular, and the weak topology on an infinite dimensional Banach space is regular but not normal.
Related posts
[1] Why do we use
F
to denote a closed set? It’s a convention that goes back to the French word
fermé
for “closed.”
