---
title: "Categorical models of logics"
url: "https://www.johndcook.com/blog/2026/10/12/categorical-models-of-logics/"
fetched_at: 2026-10-13T10:01:08.182557+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Categorical models of logics

Source: https://www.johndcook.com/blog/2026/10/12/categorical-models-of-logics/

A few days ago I wrote about
topological models of modal logic
. If you find general topology more familiar than modal logic, this correspondence could be helpful. If you think the motivation for general topology is evident but the motivation for modal logic is suspect, the correspondence between the two fields might relieve some of your suspicion of the latter.
Topological models, however, are quite limited. You can’t model
provability logic
, for example, by the usual approach to constructing topological models, though there is an alternative construction.
Categorical models are less limited. You can model a wide variety of logics using categories via the Curry-Howard-Lambek correspondence. This may be cold comfort if you find category theory and logic equally mysterious. Even so, there’s something intriguing about a correspondence between two things you find mysterious.
Categorical semantics is deep and broad, but I’ll keep this post brief. The correspondence between logic [1] and categories [2] is summarized in the table below.
It’s interesting how model logic fits into this picture. Axiom K, required by normal modal logics, says
In categorial semantics, this says this says the box operator □ is a functor, mapping objects representing propositions to objects representing propositions, and mapping morphisms representing proofs to mapping morphisms representing proofs.
Related posts
[1] More precisely, intuitionistic propositional calculus.
[2] More precisely, bicartesian closed categories.
