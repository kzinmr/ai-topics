---
title: "Mar '26 Notes - Susam Pal"
url: "https://susam.net/26c.html"
fetched_at: 2026-04-25T12:08:55.574633+00:00
source: "susam.net"
tags: [blog, raw]
---

# Mar '26 Notes - Susam Pal

Source: https://susam.net/26c.html

Mar '26 Notes
By
Susam Pal
on 30 Mar 2026
This is my third set of
monthly notes
for this year.  In these notes, I capture various interesting facts
  and ideas I have stumbled upon during the month.  Like in the last
  two months, I have been learning and exploring algebraic graph
  theory.  The two main books I have been reading are
Algebraic
  Graph Theory
by Godsil and Royle and
Algebraic Graph
  Theory
, 2nd ed. by Norman Biggs.  Much of what appears here
  comes from my study of these books as well as my own explorations
  and attempts to distill the ideas.  This post is quite heavy on
  mathematics but there are some non-mathematical, computing-related
  notes towards the end.
The level of exposition is quite uneven throughout these notes.
  After all, they aren't meant to be a polished exposition but rather
  notes I take for myself.  In some places I build concepts from first
  principles, while in others I gloss over details and focus only on
  the main results.
Sometime during the second half of the month, I also
  developed an open-source tool called
Wander Console
on a
  whim.  It lets anyone with a website host a decentralised web
  console that recommends interesting websites from the 'small web' of
  independent, personal websites.  Check my console
  here:
wander/
.
Although the initial version was ready after just about 1.5 hours of
  development during a break I was taking from studying algebraic
  graph theory, the
  subsequent
warm
  reception on Hacker News
and a
growing
  community
around it, along with the resulting feature requests
  and bug fixes, ended up taking more time than I had anticipated, at
  the expense of my algebraic graph theory studies.  With a full-time
  job, it becomes difficult to find time for both open source
  development and mathematical studies.  But eventually, I managed to
  return to my studies while making Wander Console improvements only
  occasionally during breaks from my studies.
Contents
Group Theory
Permutation
Group Homomorphism
Group Homomorphism Preserves Identity
Group Homomorphism Preserves Inverses
Image of a Group Homomorphism
Group Monomorphism
Standard Proof
Alternate Proof
Permutation Representation
Group Action
Why Right Action?
Example 1
Example 2
Group Actions Induce Permutations
Group Actions Determine Permutation Representations
Permutation Representations Determine Group Actions
Bijection Between Group Actions and Permutation Representations
Orbits
Stabilisers
Orbit-Stabiliser Theorem
Faithful Actions
Semiregular Actions
Transitive Actions
Conjugacy
Conjugation as Group Action
Right Conjugation vs Left Conjugation
Conjugate Subgroups
Conjugacy of Stabilisers
Algebraic Graph Theory
Stabiliser Index
Strongly Connected Directed Graph
Shunting
Automorphisms Preserve Successor Relation
Test of \( s \)-arc Transitivity
Moore Graphs
Generalised Polygons
Computing
Select Between Lines, Inclusive
Select Between Lines, Exclusive
Signing and Verification with SSH Key
Block IP Address with nftables
Debian Logrotate Setup
Group Theory
Permutation
A
permutation
of a set \( X \) is a bijection \( X \to X
 .  \)
For example, take \( X = \{ 1, 2, 3, 4, 5, 6 \} \) and define the
  map

  \[
    \pi : X \to X; \; x \mapsto 1 + ((x + 1) \bmod 6).
  \]

  This maps

  \begin{align*}
    1 &\mapsto 3, \\
    2 &\mapsto 4, \\
    3 &\mapsto 5, \\
    4 &\mapsto 6, \\
    5 &\mapsto 1, \\
    6 &\mapsto 2.
  \end{align*}
We can describe permutations more succinctly using cycle notation.
  The cycle notation of a permutation \( \pi \) consists of one or
  more sequences written next to each other such that the sequences
  are pairwise disjoint and \( \alpha \) maps each element in a
  sequence to the next element on its right.  If the sequence is
  finite, then \( \alpha \) maps the final element back to the first
  one.  Any element that does not appear in any sequence is mapped to
  itself.  For example the cycle notation for the above permutation is
  \( (1 3 5)(2 4 6).  \)
Group Homomorphism
A map \( \phi : G \to H \) from a group \( (G, \ast) \) to a group
  \( (H, \cdot) \) is a
group homomorphism
if, for all \( x, y
  \in G, \)

  \[
    \phi(x \ast y) = \phi(x) \cdot \phi(y).
  \]

  We say that a group homomorphism is a map between groups that
preserves
the group operation.  In other words, a group
  homomorphism
sends
products in \( G \) to products in \( H
 .  \)  For example, consider the groups \( (\mathbb{Z}, +) \) and \(
  (\mathbb{Z}_3, +).  \)  Then the map

  \[
    \phi : \mathbb{Z} \to \mathbb{Z}_3; \; n \mapsto n \bmod 3
  \]

  is a group homomorphism because

  \[
    \phi(x + y)
    = (x + y) \bmod 3
    = (x \bmod 3) + (y \bmod 3)
    = \phi(x) + \phi(y)
  \]

   for all \( x, y \in \mathbb{Z}.  \)  As another example, consider
   the groups \( (\mathbb{R}_{\gt 0}, \times) \) and \( (\mathbb{R},
   +).  \)  Then the map

  \[
    \log : \mathbb{R}_{\gt 0} \to \mathbb{R}
  \]

  is a group homomorphism because

  \[
    \log(m \times n) = \log m + \log n.
  \]

  Note that a group homomorphism preserves the identity element.  For
  example, \( 1 \) is the identity element of \( (\mathbb{R}_{\gt 0},
  \times) \) and \( 0 \) is the identity element of \( (\mathbb{R}, +)
  \) and indeed \( \log 1 = 0.  \)  Also, a group homomorphism
  preserves inverses.  Indeed \( \log m^{-1} = -\log m \) for all \( m
  \in \mathbb{R}_{\gt 0}.  \)  These observations are proved in the
  next two sections.
Group Homomorphism Preserves Identity
Let \( \phi : G \to H \) be a group homomorphism from \( (G, \ast)
  \) to \( (H, \cdot).  \)  Let \( e_1 \) be the identity in \( G \)
  and let \( e_2 \) be the identity in \( H.  \)  Then \( \phi(e_1) =
  e_2.  \)


  The proof is straightforward.  Note first that

  \[
    \phi(e_1) \cdot \phi(e_1)
    = \phi(e_1 \ast e_1)
    = \phi(e_1)
  \]

  Multiplying both sides on the right by \( \phi(e_1)^{-1}, \) we get

  \[
    (\phi(e_1) \cdot \phi(e_1)) \cdot \phi(e_1)^{-1}
    = \phi(e_1) \cdot \phi(e_1)^{-1}.
  \]

  Using the associative and inverse properties of groups, we can
  simplify both sides to get

  \[
    \phi(e_1) = e_2.
  \]
Group Homomorphism Preserves Inverses
Let \( \phi : G \to H \) be a group homomorphism from \( (G, \ast)
  \) to \( (H, \cdot).  \)  Let \( e_1 \) be the identity in \( G \)
  and let \( e_2 \) be the identity in \( H.  \)  Then for all \( x \in
  G, \) \(\phi(x^{-1}) = (\phi(x))^{-1}.  \)

  The proof of this is straightforward too.  Note that

  \[
    \phi(x) \cdot \phi(x^{-1})
    = \phi(x \ast x^{-1})
    = \phi(e_1)
    = e_2.
  \]

  Thus \( \phi(x^{-1}) \) is an inverse of \( \phi(x), \) so

  \[
    \phi(x^{-1}) = (\phi(x))^{-1}.
  \]

  The image of the inverse of an element is the inverse of the image
  of that element.
Image of a Group Homomorphism
Let \( \phi : G \to H \) be a group homomorphism.  Then the image of
  the \( \phi, \) denoted

  \[
    \phi(G) = \{ \phi(x) : x \in G \}
  \]

  is a subgroup of \( H.  \)  We will prove this now.
Let \( a, b \in \phi(G).  \)  Then \( a = \phi(x) \) and \( b =
  \phi(y) \) for some \( x, y \in G.  \)  Now \( ab = \phi(x)\phi(y) =
  \phi(xy) \in \phi(G).  \)  Therefore \( \phi(G) \) satisfies the
  closure property.
Let \( e_1 \) and \( e_2 \) be the identities in \( G \) and \( H \)
  respectively.  Since a group homomorphism preserves the identity, \(
  \phi(e_1) = e_2.  \)  Hence the identity of \( H \) lies in \(
  \phi(G).  \)
Finally, let \( a \in \phi(G).  \)  Then \( a = \phi(x) \) for some
  \( x \in G.  \)  Then \( a^{-1} = \phi(x)^{-1} = \phi(x^{-1}) \in
  \phi(G).  \)  Therefore \( \phi(G) \) satisfies the inverse property
  as well.  Therefore \( \phi(G) \) is a subgroup of \( H.  \)
Group Monomorphism
A map \( \phi : G \to H \) from a group \( (G, \ast) \) to a group
  \( (H, \cdot) \) is a
group monomorphism
if \( \phi \) is a
  homomorphism and is injective.  In other words, a homomorphism \(
  \phi \) is called a monomorphism if, for all \( x, y \in G, \)

  \[
  \phi(x) = \phi(y) \implies x = y.
  \]

  Let \( e_1 \) be the identity element of \( G \) and let \( e_2 \)
  be the identity element of \( H.  \)  A useful result in group theory
  states that a homomorphism \( \phi : G \to H \) is a monomorphism if
  and only if its kernel is trivial, i.e.

  \[
    \ker(\phi) = \{ x \in G : \phi(x) = e_2 \} = \{ e_1 \}.
  \]

  Let us prove this now.
Standard Proof
Suppose \( \phi : G \to H \) is a monomorphism.  Since a
  homomorphism preserves the identity element, we have \( \phi(e_1) =
  e_2.  \)  Therefore

  \[
    e_1 \in \ker(\phi).
  \]

  Let \( x \in \ker(\phi).  \)  Then \( \phi(x) = e_2 = \phi(e_1).  \)
  Since \( \phi \) is injective, \( x = e_1.  \)  Therefore

  \[
    \ker(\phi) = \{ e_1 \}.
  \]

  Conversely, suppose \( \ker(\phi) = \{ e_1 \}.  \)  Let \( x, y \in G
  \) such that \( \phi(x) = \phi(y).  \)  Then

  \[
    \phi(x \ast y^{-1})
    = \phi(x) \cdot \phi(y^{-1})
    = \phi(x) \cdot (\phi(y))^{-1}
    = \phi(y) \cdot (\phi(y))^{-1}
    = e_2.
  \]

  Hence

  \[
    x \ast y^{-1} \in \ker(\phi) = \{ e_1 \},
  \]

  so

  \[
    x \ast y^{-1} = e_1.
  \]

  Multiplying both sides on the right by \( y, \) we obtain

  \[
    x = y.
  \]

  This completes the proof.
Alternate Proof
Here I briefly discuss an alternate way to think about the above
  proof.  The above proof is how most texts usually present these
  arguments.  In particular, the proof of injectivity typically
  proceeds by showing that equal images imply equal preimages.  It's a
  standard proof technique.  When I think about these proofs, however,
  the contrapositive argument feels more intuitive to me.  I prefer to
  think about how unequal preimages must have unequal images.
  Mathematically, there is no difference at all but the contrapositive
  argument has always felt the most natural to me.  Let me briefly
  describe how this proof runs in my mind when I think about it more
  intuitively.
Suppose \( \phi \) is a monomophorism.  Since a homomorphism
  preserves the identity element, clearly \( \phi(e_1) = e_2.  \)
  Since \( \phi \) is injective, it cannot map two distinct elements
  of \( G \) to \( e_2.  \)  Thus \( e_1 \) is the only element of \( G
  \) that \( \phi \) maps to \( e_2 \) which means \( \ker(\phi) = \{
  e_1 \}.  \)
To prove the converse, suppose \( \ker(\phi) = \{ e_1 \}.  \)
  Consider distinct elements \( x, y \in G.  \)  Since \( x \ne y, \)
  we have \( x \ast y^{-1} \ne e_1.  \)  Therefore \( x \ast y^{-1}
  \notin \ker(\phi).  \)  Thus \( \phi(x \ast y^{-1}) \ne e_2.  \)
  Since \( \phi \) is a homomorphism,

  \[
    \phi(x \ast y^{-1})
    = \phi(x) \cdot \phi(y^{-1})
    = \phi(x) \cdot \phi(y)^{-1}.
  \]

  Therefore \( \phi(x) \cdot \phi(y)^{-1} \ne e_2 \) which implies

  \[
    \phi(x) \ne \phi(y).
  \]

  This proves that \( \ker(\phi) = \{ e_1 \} \) implies that \( \phi
  \) is injective and thus a monomorphism.
Permutation Representation
Let \( G \) be a group and \( X \) a set.  Then a homomorphism

  \[
    \phi : G \to \operatorname{Sym}(X)
  \]

  is called a
permutation representation
of \( G \) on \( X
 .  \)  The homomorphism \( \phi \) maps each \( g \in G \) to a
  permutation of \( X.  \)  We say that each \( g \in G \)
induces
a permutation of \( X.  \)
For example, let \( G = (\mathbb{Z}_3, +) \) and \( X = \{ 0, 1, 2,
  3, 4, 5 \}.  \)  Define the map \( \phi : G \to \operatorname{Sym}(X)
  \) by

  \begin{align*}
    \phi(0) &= (), \\
    \phi(1) &= (024)(135), \\
    \phi(2) &= (042)(153).
  \end{align*}

  It is easy to verify that this is a homomorphism.  Here is one way
  to verify it:

  \begin{align*}
    \phi(0)\phi(1) &= ()(024)(135) = (024)(135) = \phi(0 + 1), \\
    \phi(0)\phi(2) &= ()(042)(153) = (042)(153) = \phi(0 + 2), \\
    &\;\,\vdots \\
    \phi(2)\phi(1) &= (042)(153)(024)(135) = () = \phi(0) = \phi(2 + 1), \\
    \phi(2)\phi(2) &= (042)(153)(042)(153) = (024)(135) = \phi(1) = \phi(2 + 2).
  \end{align*}

  We will meet this homomorphism again in the form of group action \(
  \alpha \) in the next section.
Group Action
Let \( G \) be a group with identity element \( e.  \)  Let \( X \)
  be a set.  A right action of \( G \) on \( X \) is a map

  \[
    \alpha : X \times G \to X
  \]

  such that

  \begin{align*}
    \alpha(x, e)            &= x, \\
    \alpha(\alpha(x, g), h) &= \alpha(x, gh)
  \end{align*}

  for all \( x \in X \) and all \( g, h \in G.  \)  The two conditions
  above are called the identity and compatibility properties of the
  group action respectively.  Note that in a right action, the product
  \( gh \) is applied left to right: \( g \) acts first and then \( h
  \) acts.  If we denote \( \alpha(x, g) \) as \( x^g, \) then the
  notation for the two conditions can be simplified to \( x^e = x \)
  and \( (x^g)^h = x^{gh} \) for all \( g, h \in G.  \)
Why Right Action?
We discuss right group actions here instead of left group actions
  because we want to use the notation \( \alpha(x, g) = x^g, \) which
  is quite convenient while studying permutations and graph
  automorphisms.  It is perfectly possible to use left group actions
  to study permutations as well.  However, we lose the benefit of the
  convenient \( x^g \) notation.  In a left group action, the
  compatibility property is \( \alpha(g, \alpha(h, x)) = \alpha(gh, x)
 , \) so if we were to use the notation \( \alpha(g, x) = x^g, \) the
  compatibility property would look like \( (x^h)^g = x^{gh}.  \)  This
  reverses the order of exponents which can be confusing.  Right group
  actions avoid this notational inconvenience.
Example 1
Let \( G = \mathbb{Z}_3 \) be the group under addition modulo \( 3
 .  \)  Let \( X = \{ 0, 1, 2, 3, 4, 5 \}.  \)  Define an action \(
  \alpha \) of \( G \) on \( X \) by

  \[
    \alpha(x, g) = x^g = (x + 2g) \bmod 6.
  \]

  Each \( g \in G \) acts as a permutation of \( X.  \)  For example,
  the element \( 0 \in \mathbb{Z}_3 \) acts as the identity
  permutation.  The element \( 1 \in \mathbb{Z}_3 \) acts as the
  permutation \( (0 2 4)(1 3 5).  \)  The element \( 2 \in \mathbb{Z}_3
  \) acts as the permutation \( (0 4 2)(1 5 3).  \)  The following
  table shows how each \( g \in G \) permutes \( X.  \)

  \[
    \begin{array}{c|ccc}
      x_{\downarrow} \backslash g_{\rightarrow} & 0 & 1 & 2 \\
      \hline
      0 & 0 & 2 & 4 \\
      1 & 1 & 3 & 5 \\
      2 & 2 & 4 & 0 \\
      3 & 3 & 5 & 1 \\
      4 & 4 & 0 & 2 \\
      5 & 5 & 1 & 3 \\
    \end{array}
  \]

  From the table we see that each \( g \in G \) permutes the elements
  of \( \{ 0, 2, 4 \} \) among themselves.  Similarly, the elements of
  \( \{ 1, 3, 5 \} \) are permuted among themselves.  These sets \(
  \{0, 2, 4 \} \) and \( \{ 1, 3, 5 \} \) are called the
orbits
of the action.  The concept of orbits is formally
  introduced in its
own section further below
.
Example 2
Now let \( G = \mathbb{Z}_6 \) be the group under addition modulo \(
  6.  \)  Let \( X = \{ 0, 1, \dots, 8 \}.  \)  Define an action \(
  \beta \) of \( G \) on \( X \) by

  \[
    \beta(x, g) = x^g = (x + 3g) \bmod 9.
  \]

  Now the table for the action looks like this:

  \[
    \begin{array}{c|cccccc}
      x_{\downarrow} \backslash g_{\rightarrow} & 0 & 1 & 2 & 3 & 4 & 5 \\
      \hline
      0 & 0 & 3 & 6 & 0 & 3 & 6 \\
      1 & 1 & 4 & 7 & 1 & 4 & 7 \\
      2 & 2 & 5 & 8 & 2 & 5 & 8 \\
      3 & 3 & 6 & 0 & 3 & 6 & 0 \\
      4 & 4 & 7 & 1 & 4 & 7 & 1 \\
      5 & 5 & 8 & 2 & 5 & 8 & 2 \\
      6 & 6 & 0 & 3 & 6 & 0 & 3 \\
      7 & 7 & 1 & 4 & 7 & 1 & 4 \\
      8 & 8 & 2 & 5 & 8 & 2 & 5
    \end{array}
  \]

  This action splits \( X \) into three orbits \( \{ 0, 3, 6 \}, \) \(
  \{ 1, 4, 7 \} \) and \( \{ 2, 5, 8 \}.  \)
Group Actions Induce Permutations
Earlier, we saw an example of a group action and observed that each
  element of the group acts as a permutation.  That was not merely a
  coincidence.  It is indeed a general property of group actions.
  Whenever a group \( G \) acts on a set \( X, \) each element \( g
  \in G \) determines a bijection \( X \to X.  \)  In other words,
  every element of \( G \) acts as a permutation of \( X.  \)  Let us
  see why this must be the case.
Consider the group action \( \alpha : X \times G \to X.  \)  Fix \( g
  \in G \) and let \( x \) vary over \( X \) to obtain the map

  \[
    \alpha_g : X \to X; \; x \mapsto \alpha(x, g).
  \]

  We show that \( \alpha_g \) is a bijection.  First we prove
  injectivity.  Let \( e \) be the identity element of \( G.  \)
  Let \( x, y \in X.  \)  Then

  \begin{align*}
    \alpha_g(x) = \alpha_g(y)
    & \implies \alpha(x, g) = \alpha(y, g) \\
    & \implies \alpha(\alpha(x, g), g^{-1}) = \alpha(\alpha(y, g), g^{-1}) \\
    & \implies \alpha(x, gg^{-1}) = \alpha(y, gg^{-1}) \\
    & \implies \alpha(x, e) = \alpha(y, e) \\
    & \implies x = y.
  \end{align*}

  The \( x^g \) notation allows us to write the above proof more
  conveniently as follows:

  \begin{align*}
    \alpha_g(x) = \alpha_g(y)
    & \implies \alpha(x, g) = \alpha(y, g) \\
    & \implies (x^g)^{g^{-1}} = (y^g)^{g^{-1}} \\
    & \implies x^{g g^{-1}} = y^{g g^{-1}} \\
    & \implies x^e = y^e \\
    & \implies x = y.
  \end{align*}

  This completes the proof of injectivity.  Now we prove surjectivity.
  Let \( y \in X.  \)  Take \( x = \alpha(y, g^{-1}).  \)  Then

  \[
    \alpha_g(x)
    = \alpha(x, g)
    = \alpha(\alpha(y, g^{-1}), g)
    = \alpha(y, g^{-1} g)
    = \alpha(y, e)
    = y.
  \]

  Again, if we write \( x = y^{g^{-1}}, \) the above step can be
  written more succinctly as

  \[
    \alpha_g(x) = x^g = (y^{g^{-1}})^g = y^{(g^{-1} g)} = y^e = y.
  \]

  Thus every element \( y \in X \) has a preimage in \( X \) under \(
  \alpha_g.  \)  Hence \( \alpha_g \) is surjective.  Since we have
  already shown that \( \alpha_g \) is injective, we now conclude that
  \( \alpha_g \) is bijective.  Therefore \( \alpha_g \) is a
  permutation of \( X.  \)  Stated symbolically,

  \[
    \alpha_g \in \operatorname{Sym}(X).
  \]

  Note that

  \[
    \alpha_g(x) = \alpha(x, g) = x^g.
  \]

  Thus both \( \alpha_g(x) \) and \( x^g \) serve as convenient
  shorthands for \( \alpha(x, g).  \)
Group Actions Determine Permutation Representations
We have seen that each group element \( g \in G \) induces (acts as)
  a permutation of \( X.  \)  Precisely speaking, each \( g \in G \)
  determines a permutation \( \alpha_g \) of \( X.  \)  Now define a
  map

  \[
    \phi: G \to \operatorname{Sym}(X); \; g \mapsto \alpha_g.
  \]

  We now show that this map is a homomorphism.  This means that we
  want to show that \( \phi(gh) = \phi(g) \phi(h).  \)  Since \(
  \phi(g), \phi(h) \in \operatorname{Sym}(X), \) the right-hand side
  is a product of permutations of \( X.  \)  We first define the
  product of two permutations \( \pi, \rho : X \to X \) by

  \[
    \pi \rho : X \to X; \; x \mapsto \rho(\pi(x)).
  \]

  In other words, \( \pi \rho = \rho \circ \pi.  \)  Now

  \begin{align*}
    \phi(gh)(x)
    & = \alpha_{gh}(x) \\
    & = \alpha(x, gh) \\
    & = \alpha(\alpha(x, g), h) \\
    & = \alpha_h(\alpha_g(x)) \\
    & = (\alpha_h \circ \alpha_g)(x) \\
    & = (\alpha_g \alpha_h)(x) \\
    & = (\phi(g) \phi(h))(x).
  \end{align*}

  Since the above equality holds for all \( x \in X, \) we conclude
  that

  \[
    \phi(gh) = \phi(g) \phi(h).
  \]

  Hence \( \phi \) is a group homomorphism from \( G \) to \(
  \operatorname{Sym}(X).  \)  Therefore \( \phi \) is a permutation
  representation of \( G \) on \( X.  \)  It maps each group element \(
  g \in G \) to a permutation \( \alpha_g \in \operatorname{Sym}(X).  \)
Note the multiple levels of abstraction here.  The group action \(
  \alpha : X \times G \to X \) determines a permutation representation
  \( \phi : G \to \operatorname{Sym}(X).  \)  Each element \( g \in G
  \) together with the group action \( \alpha \) determines a
  permutation \( \alpha_g : X \to X.  \)
Also note that \( \phi(g)(x) = \alpha_g(x) = \alpha(g, x) = x^g.  \)
  In fact, \( \phi(g) = \alpha_g.  \)
Permutation Representations Determine Group Actions
Consider a permutation representation \( \phi : G \to
  \operatorname{Sym}(X).  \)  Define a map

  \[
    \alpha : X \times G \to X; \; (x, g) \mapsto \phi(g)(x).
  \]

  First we verify the identity property of group actions.  Since \(
  \phi \) is a homomorphism, it preserves the identity element.
  Therefore \( \phi(e) \) is the identity permutation.  Hence

  \[
    \alpha(x, e) = \phi(e)(x) = x
  \]

  Now we verify the compatibility property of the action.  For all \(
  g, h \in G \) and \( x \in X, \) we have

  \begin{align*}
    \alpha(\alpha(x, g), h)
    & = \alpha(\phi(g)(x), h) \\
    & = \phi(h)(\phi(g)(x)) \\
    & = (\phi(h) \circ \phi(g))(x) \\
    & = (\phi(g)\phi(h))(x) \\
    & = \phi(gh)(x) \\
    & = \alpha(x, gh).
  \end{align*}

  This completes the proof of the fact that every permutation
  representation determines a group action.
Bijection Between Group Actions and Permutation Representations
There is a bijection between the group actions \( \alpha : X \times
  G \to X \) and permutation representations \( \phi : G \to
  \operatorname{Sym}(X).  \)  We now show that these two constructions
  are inverses of each other.
Given a right action \( \alpha : X \times G \to X, \) define

  \[
    \phi_{\alpha} : G \to \operatorname{Sym}(X)
    \quad \text{by} \quad
    \phi_{\alpha}(g)(x) = \alpha(x, g).
  \]

  Given a permutation representation \( \phi : G \to
  \operatorname{Sym}(X), \) define

  \[
    \alpha_{\phi} : X \times G \to X
    \quad \text{by} \quad
    \alpha_{\phi}(x, g) = \phi(g)(x).
  \]

  We now show that these two constructions undo each other.  Take an
  arbitrary group action \( \alpha : X \times G \to X \) and construct
  the corresponding permutation representation \( \phi_{\alpha}.  \)
  Then take this permutation representation and construct the group
  action \( \alpha_{\phi_{\alpha}}.  \)  But

  \[
    \alpha_{\phi_{\alpha}}(x, g)
    = \phi_{\alpha}(g)(x)
    = \alpha(x, g).
  \]

  Therefore \( \alpha_{\phi_{\alpha}} = \alpha.  \)  Similarly,
  starting with the permutation representation \( \phi, \) we get

  \[
    \phi_{\alpha_{\phi}}(g)(x)
    = \alpha_{\phi}(x, g)
    = \phi(g)(x).
  \]

  Therefore \( \phi_{\alpha_{\phi}} = \phi.  \)  Hence there is a
  bijection between group actions \( \alpha : X \times G \to X \) and
  permutation representations: \( \phi : G \to \operatorname{Sym}(X)
 .  \)  In fact, a group action and the corresponding permutation
  representation contain the same information, namely how the elements
  \( g \in G \) acts as permutations of \( X.  \)  For this reason,
  many advanced texts do not make any distinction between the group
  action and its permutation representation.  They often use them
  interchangeably even though technically they have different domains.
Orbits
Let \( G \) act on a set \( X.  \)  For an element \( x \in X, \) the
orbit
of \( x \) under the action of \( G \) is the set of
  all elements of \( X \) that can be reached from \( x \) by the
  action of elements of \( G.  \)  Symbolically, the orbit of \( x \)
  is the set

  \[
    x^G = \{ x^g : g \in G \}.
  \]

  In other words, the orbit of \( x \) contains every element of \( X
  \) that \( x \) can be moved to by the group action.  If \( y \in
  x^G, \) then there exists some \( g \in G \) such that \( y = x^g
 .  \)
The orbits of a group action partition the set \( X.  \)  That is,
  every element of \( X \) lies in exactly one orbit and two orbits
  are either identical or disjoint.  Thus the group action decomposes
  the set \( X \) into disjoint subsets (the orbits), each consisting
  of elements that can be transformed into one another by the action
  of \( G.  \)
Stabilisers
Let \( G \) be a group acting on a set \( X.  \)  For an element
  \( x \in X, \) the
stabiliser
of \( x \) is the set

  \[
    G_x = \{ g \in G : x^g = x \}.
  \]

  The stabiliser \( G_x \) consists of all elements of \( G \) that
  fix the element \( x.  \)  The stabiliser \( G_x \) is a subgroup of
  \( G.  \)  Indeed, the identity element \( e \in G \) satisfies \(
  x^e = x, \) so \( e \in G_x.  \)  If \( g, h \in G_x, \) then \(
  x^{gh} = (x^g)^h = x.  \)  If \( g \in G_x, \) then \( x^{g^{-1}} =
  (x^g)^{g^{-1}} = x.  \)
Intuitively, the stabiliser measures how much symmetry of the group
  action leaves the element \( x \) unchanged.  The larger the
  stabiliser, the more elements of \( G \) fix \( x.  \)
Orbit-Stabiliser Theorem
Let \( G \) be a group acting on a set \( X.  \)  The
  orbit-stabiliser theorem states that for any \( x \in X, \)

  \[
    \lvert G_x \rvert \cdot \lvert x^G \rvert = \lvert G \rvert.
  \]

  Stated differently, the index of the stabiliser \( G_x \) in the
  group \( G \) is given by

  \[
    [ G : G_x ]
    = \lvert G_x \backslash G \rvert
    = \lvert G \rvert / \lvert G_x \rvert
    = \lvert x^G \rvert.
  \]

  There is a bijection between the right cosets of \( G_x \) and the
  elements of \( x^G.  \)  Demonstrating this bijection proves the
  above equation.  We will work with right cosets of \( G_x.  \)
  Define

  \[
    \phi : G_x \backslash G \to x^G; \; G_x g \mapsto x^g.
  \]

  We want to show that \( \phi \) is a bijection.  But first we need
  to show that \( \phi \) is well defined.  A coset \( G_x g \in G_x
  \backslash G \) can also be written as

  \[
    G_x g = G_x h
  \]

  for some \( h \in G.  \)  If \( x^g \ne x^h, \) then \( \phi \) would
  not be well defined, since \( \phi \) must assign each coset in \(
  G_x \backslash G \) to exactly one element in the orbit \( x^G \) in
  order to be a function.  This can be shown using the following
  equivalences:

  \begin{align*}
    G_x g = G_x h
    & \iff hg^{-1} \in G_x \\
    & \iff x = x^{h g^{-1}} \\
    & \iff x^g = x^h \\
  \end{align*}

  This proves two things at once.  The fact that

  \[
    G_x g = G_x h \implies x^g = x^h
  \]

  proves that when the same coset is written using two different
  representatives, the image does not change.  Therefore \( \phi \) is
  well defined.  Further

  \[
    x^g = x^h \implies G_x g = G_x h
  \]

  proves that \( \phi \) is injective.  To show that \( \phi \) is
  surjective, let \( y \in x^G.  \)  Then \( y = x^g \) for some \( g
  \in G.  \)  Since \( \phi(G_x g) = x^g, \) we get

  \[
    \phi(G_x g) = y.
  \]

  Thus every element of \( x^G \) is the image of some right coset \(
  G_x g \) under \( \phi.  \)  This completes the proof of a bijection
  between the right cosets of \( G_x \) and the elements of \( x^G.  \)
  Therefore \( \lvert G_x \backslash G \rvert = \lvert x^G \rvert \)
  and hence \( \lvert G \rvert / \lvert G_x \rvert = \lvert x^G \rvert
 , \) which establishes the orbit-stabiliser theorem.
Faithful Actions
Let \( G \) act on a set \( X.  \)  The action is called
faithful
if distinct elements of \( G \) induce distinct
  permutations of \( X.  \)  In other words, the only element of \( G
  \) that acts as the identity permutation of \( X \) is the identity
  element \( e \in G.  \)  Symbolically, the action is faithful if

  \[
    g \ne e \implies \exists x \in X, \; x^g \ne x.
  \]

  Equivalently,

  \[
    \forall x \in X, \; x^g = x \implies g = e.
  \]

  The action is faithful if the only element of \( G \) that fixes
  every element of \( X \) is the identity, i.e.

  \[
    \bigcap_{x \in X} G_x = \{ e \}.
  \]

  Recall that every group action determines a permutation
  representation \( \phi : G \to \operatorname{Sym}(X).  \)  From this
  point of view, the action is faithful precisely when the permutation
  representation is faithful, that is, when the homomorphism \( \phi
  \) is injective (or equivalently when \( \ker(\phi) = \{ e \} \)).
  In other words, the action is faithful if and only if the associated
  homomorphism \( \phi \) is a monomorphism.
Semiregular Actions
A group action of \( G \) on \( X \) is called
semiregular
if no non-identity element of \( G \) fixes any element of \( X.  \)
  In other words, whenever \( g \ne e, \) the permutation of \( X \)
  induced by \( g \) moves every element of \( X.  \)  Symbolically,

  \[
    g \ne e \implies \forall x \in X, \; x^g \ne x.
  \]

  Equivalently,

  \[
    \exists x \in X, \; x^g = x \implies g = e.
  \]

  The action is semiregular if

  \[
    \forall x \in X, \; G_x = \{ e \}.
  \]

  This is a stronger property than faithfulness.  Faithfulness only
  guarantees that when \( g \ne e, \) the element \( g \) moves at
  least one element of \( X.  \)  But semiregularity guarantees that
  when \( g \ne e, \) the element \( g \) moves every element of \( X
 .  \)  Therefore every semiregular action is faithful, but not every
  faithful action is semiregular.
Transitive Actions
Let \( G \) act on a set \( X.  \)  The action is called
transitive
if there is only one orbit.  In other words, the
  action is transitive if every element of \( X \) can be reached from
  any other element by the action of some element of \( G.  \)
  Symbolically, the action is transitive if

  \[
    \forall x, y \in X \; \exists g \in G, \; x^g = y.
  \]

  Equivalently, the action is transitive if

  \[
    x^G = X
  \]

  for some (and hence every) \( x \in X.  \)
Conjugacy
Let \( G \) be a group.  Let \( x, g \in G.  \)  The element

  \[
    g^{-1} x g
  \]

  is called a
conjugate
of \( x \) by \( g.  \)  Any element
  \( y \in G \) that can be written as \( g^{-1} x g \) for some \( g
  \in G \) is said to be a conjugate of \( x.  \)  The conjugacy class
  of \( x \) in \( G \) is the set

  \[
    x^G = \{ g^{-1} x g : g \in G \}.
  \]

  In other words, the conjugacy class of \( x \) is the set of all
  elements of \( G \) that are conjugate to \( x.  \)  At first,
  reusing the orbit notation \( x^G \) for the conjugacy class may
  seem like an abuse of notation.  However, we will see in the next
  section that the conjugacy class is precisely the orbit of \( x \)
  under the action of \( G \) on itself by conjugation.  Thus \( x^G
  \) is in fact a natural and accurate notation for the conjugacy
  class.
Conjugation as Group Action
Conjugation can be seen as an action of a group on itself.  Define
  the map

  \[
    \alpha : G \times G \to G; \; (x, g) \mapsto g^{-1} x g.
  \]

  Note that

  \[
    \alpha(x, e) = e^{-1} x e = x
  \]

  and

  \[
    \alpha(\alpha(x, g), h)
    = h^{-1} (g^{-1} x g) h
    = (gh)^{-1} x (gh)
    = \alpha(x, gh).
  \]

  Therefore \( \alpha \) satisfies the two defining properties of a
  right group action.  The conjugacy class \( x^G \) is precisely the
  orbit of \( x \) under the conjugation action.  Therefore the orbits
  of the conjugation action of \( G \) on itself are the conjugacy
  classes of \( G.  \)
Right Conjugation vs Left Conjugation
We observed above that the conjugation action is a right action of a
  group on itself.  Let \( x, g \in G \) and let

  \[
    y = g^{-1} x g.
  \]

  Now let \( h = g^{-1}.  \)  Then we can write the above equation as

  \[
    y = h x h^{-1}.
  \]

  According to the previous section, \( y \) is the conjugate of \( x
  \) by \( g.  \)  However, many texts call \( y \) the conjugate of \(
  x \) by \( h.  \)  Both are valid perspectives.  In both
  perspectives, \( x \) and \( y \) are conjugates of each other.
  Precisely,
In the first perspective, we have \( y = g^{-1} x g \) and we say
    that \( y \) is a conjugate of \( x \) by \( g.  \)  A corollary is
    that \( x \) is a conjugate of \( y \) by \( g^{-1}.  \)
In the second perspective, we have \( y = h x h^{-1} \) and we say
    that \( y \) is a conjugate of \( x \) by \( h.  \)  A corollary is
    that \( x \) is a conjugate of \( y \) by \( h^{-1}.  \)
Although in both perspectives, \( x \) and \( y \) are conjugates of
  each other, the group element by which one is conjugated to the
  other is different.  This leads to different group actions as well.
When we say that \( y = g^{-1} x g \) is a conjugate of \( x \) by
  \( g, \) the group action

  \[
    \alpha : G \times G \to G; \; (x, g) \mapsto g^{-1} x g.
  \]

  is a right group action as demonstrated in the previous section.
  But when we say that \( y = h x h^{-1} \) is a conjugate of \( x \)
  by \( h, \) the conjugation action is no longer a right group action
  because the compatibility property is violated:

  \[
    \alpha(\alpha(x, g), h)
    = h ( g x g^{-1} ) h^{-1}
    = (hg) x (hg)^{-1}
    = \alpha(x, hg).
  \]

  We get \( \alpha(x, hg) \) instead of the required \( \alpha(x, gh)
 .  \)  So with the second perspective, the group action is no longer a
  right action.  Instead it is a left action since

  \[
    \alpha(g, \alpha(h, x))
    = g (h x h^{-1}) g^{-1}
    = (gh) x (gh)^{-1}
    = \alpha(gh, x).
  \]

  In this post we will work only with the first perspective because we
  will use right actions throughout.
Conjugate Subgroups
Let \( G \) be a group.  Let \( H \le G.  \)  Define

  \[
    g^{-1} H g = \{ g^{-1} h g : h \in H \}.
  \]

  We say that \( g^{-1} H g \) is a conjugate of \( H \) by \( g.  \)
Conjugacy of Stabilisers
Let \( G \) be a group acting on a set \( X.  \)  Let \( x \in X \)
  and \( g \in G.  \)  Then

  \[
    g^{-1} G_x g = G_{x^g}.
  \]

  That is, \( G_{x^g} \) is a conjugate of \( G_x \) by \( g.  \)  This
  result can be summarised as follows: stabilisers of elements in the
  same orbit are conjugate.  Or more explicitly: the stabiliser of \(
  x^g \) is a conjugate of the stabiliser of \( x \) by \( g.  \)  The
  proof is straightforward.  Let \( h \in G.  \)  Then

  \begin{align*}
    h \in g^{-1} G_x g
    & \iff g^{-1} (g h g^{-1}) g \in g^{-1} G_x g \\
    & \iff g h g^{-1} \in G_x \\
    & \iff x^{g h g^{-1}} = x \\
    & \iff (x^g)^h = x^g \\
    & \iff h \in G_{x^g}.
  \end{align*}

  Therefore \( g^{-1} G_x g = G_{x^g}.  \)
Algebraic Graph Theory
Stabiliser Index
In a vertex-transitive graph \( \Gamma, \) for any \( x \in
  V(\Gamma) \) and all \( y \in V(\Gamma), \) there exists \( g \in G
  \) such that \( x^g = y.  \)  Therefore \( x^G = V(\Gamma).  \)  Thus
  by the
orbit-stabiliser
  theorem
,

  \[
    [ G : G_x ]
    = \lvert G_x \backslash G \rvert
    = \lvert x^G \rvert
    = \lvert V(\Gamma) \rvert.
  \]
Strongly Connected Directed Graph
A
path
in a directed graph \( \Gamma \) is a sequence of
  vertices \( v_0, \dots, v_r \) of distinct vertices such that \(
  (v_{i - 1}, v_i) \) is an arc of \( \Gamma \) for \( i = 1, \dots, r
 .  \)
A directed graph is
strongly connected
if for every ordered
  pair of vertices \( (u, v) \) there is a path from \( u \) to \( v
 .  \)
Shunting
Let \( \alpha = ( \alpha_0, \dots, \alpha_s ) \) and \( \beta = (
  \beta_0, \dots, \beta_s ) \) be two \( s \)-arcs in a graph \(
  \Gamma.  \)  We say that \( \beta \) is a successor of \( \alpha \)
  if \( \beta_i = \alpha_{i + 1} \) for \( 0 \le i \le s - 1.  \)  We
  also say that \( \alpha \) can be
shunted
onto \( \beta.  \)
In section 4.2 of Godsil and Royle, there is a rather technical
  setup which first defines \( X^{(s)} \) as the directed graph with
  the \( s \)-arcs of a graph \( X \) as its vertices such that \(
  (\alpha, \beta) \) is an arc of \( X^{(s)} \) if and only if \(
  \alpha \) can be shunted onto \( \beta \) in \( X.  \)  Then it goes
  on to show that if \( X \) is a connected graph with a minimum
  degree two and \( X \) is not a cycle, then \( X^{(s)} \) is
  strongly connected for all \( s \ge 0.  \)
That is a very technical way of saying that in a connected graph \(
  X \) that is not a cycle and has a minimum degree two, any \( s
  \)-arc \( \alpha \) can be sent to any \( s \)-arc \( \beta \) by
  repeated shunting.  The proof is quite technical too and pretty
  long, so I'll omit it here.
Automorphisms Preserve Successor Relation
We will obtain a nifty result here that will prove to be very useful
  in the next section.  Let \( S(\gamma) \) denote the set of all
  successors of the \( s \)-arc \( \gamma \) of a graph.  Let \( g \)
  be an automorphism of the graph.  Then

  \[
    \delta \in S(\gamma) \iff \delta^g \in S(\gamma^g).
  \]

  This follows directly from the fact that automorphisms preserve
  adjacency, so they must preserve successor relation as well.  A
  corollary of this is that for an automorphism \( h, \) we have

  \[
    \delta^{h^{-1}} \in S(\gamma) \iff \delta \in S(\gamma^h).
  \]

  This is the form that will be useful soon.
Test of \( s \)-arc Transitivity
The results in the previous two sections lead to a remarkably simple
  proof of the fact that the Petersen graph is \( 3 \)-arc transitive.
  Let us see how.
Let \( P \) be the Petersen graph whose vertices are the \( 2
  \)-subsets of \( \{ 1, 2, 3, 4, 5 \} \) with adjacency given by
  disjointness of the \( 2 \)-subsets.  Then \( \operatorname{Aut}(P)
  \cong S_5 \) since any permutation of \( \{ 1, 2, 3, 4, 5 \} \)
  induces a permutation of the vertices that preserves disjointness
  and hence adjacency.  We will use the shorthand \( ab \) to
  represent each vertex \( \{ a, b \} \) of \( P.  \)  Consider the \(
  3 \)-arc

  \[
    \alpha = (12, 34, 15, 23).
  \]

  It has exactly two successors, namely

  \[
    \beta_1 = (34, 15, 23, 14), \quad \beta_2 = (34, 15, 23, 45).
  \]

  Let \( g_1 = (13)(245) \) and \( g_2 = (13524).  \)  Then

  \begin{align*}
    \alpha^{g_1}
    & = (12, 34, 15, 23)^{(13)(245)} = (34, 15, 23, 14) = \beta_1, \\
    \alpha^{g_2}
    & = (12, 34, 15, 23)^{(13524)} = (34, 51, 23, 45) = \beta_2.
  \end{align*}

  Let \( H = \langle g_1, g_2 \rangle \le \operatorname{Aut}(P).  \)
  Consider an \( s \)-arc \( \alpha^h \) for some \( h \in H.  \)  Let
  \( \delta \in S(\alpha^h).  \)  Then by the result in the previous
  section, we get

  \[
    \delta^{h^{-1}} \in S(\alpha)
    = \{ \beta_1, \beta_2 \}
    = \{ \alpha^{g_1}, \alpha^{g_2} \}.
  \]

  Therefore

  \[
    \delta \in \{ \alpha^{g_1 h}, \alpha^{g_2 h} \}.
  \]

  Thus

  \[
    \delta \in \alpha^{H}.
  \]

  We started with an \( s \)-arc \( \alpha^h \in \alpha^H \) and
  showed that its successors \( \delta \) also lie in \( \alpha^H.  \)
  Thus the orbit \( \alpha^H \) is closed under taking successors.
Now by the
shunting result
discussed
  previously, \( \alpha \) can be sent to any \( 3 \)-arc of \( P \)
  by repeated shunting.  Therefore all \( 3 \)-arcs of \( P \) belong
  to \( \alpha^H.  \)  Therefore the automorphisms in \( H \) can send
  any \( 3 \)-arc of \( P \) to any other thus making \( P \) \( 3
  \)-arc transitive.
Moore Graphs
Graphs with diameter \( d \) and girth \( 2d + 1 \) are known as
  Moore graphs.
There are an infinite number of Moore graphs with diameter \( 1 \)
  since the complete graphs \( K_n, \) where \( n \ge 3, \) have
  diameter \( 1 \) and girth \( 3.  \)
There are three known Moore graphs of diameter \( 2.  \)  They are \(
  C_5, \) \( J(5, 2, 0) \) also known as the Petersen graph and the
  Hoffman-Singleton graph.  They are respectively \( 2 \)-regular, \(
  3 \)-regular and \( 7 \)-regular.  There is a famous result that
  proves that a Moore graph must be \( 2 \)-regular, \( 3 \)-regular,
  \( 7 \)-regular or \( 57 \)-regular.  It is unknown currently
  whether a \( 57 \)-regular Moore graph of diameter \( 2 \) exists.
There are infinitely many Moore graphs of diameter \( d \ge 3 \)
  because the odd cycles \( C_{2d + 1} \) are \( 2 \)-regular graphs
  with diameter \( d \) and girth \( 2d + 1 \) for all \( d \ge 1.  \)
  However, there are no \( k \)-regular Moore graphs for diameter \( d
  \ge 3 \) when \( k \ge 3.  \)
Generalised Polygons
Bipartite graphs with diameter \( d \) and girth \( 2d \) are known
  as generalised polygons.  This is easy to understand.  If we take a
  classical \( d \)-gon and create the incidence graph of its vertices
  and edges, then the incidence graph is the cycle \( C_{2d} \) which
  has diameter \( d \) and girth \( 2d.  \)
The converse is not always true.  For example,
  the
Heawood
  graph
which has diameter \( d = 3 \) and girth \( 2d = 6.  \)  It
  is the incidence graph of Fano plane, which is a projective plane
  rather than a classical \( d \)-gon.
Although a generalised polygon is not always the incidence graph of
  a classical polygon, the idea behind the definition comes from a
  simple observation.  If we take a classical \( d \)-gon and form the
  incidence graph of its vertices and edges, we obtain the cycle \(
  C_{2d}.  \)  This graph is bipartite and has diameter \( d \) and
  girth \( 2d.  \)  The definition of a generalised polygon abstracts
  these properties.  Any bipartite graph with diameter \( d \) and
  girth \( 2d \) is called a generalised polygon, even when it is not
  the incidence graph of a classical \( d \)-gon.  In this way the
  definition allows much richer graphs than simple cycles.
Computing
Select Between Lines, Inclusive
Select text between two lines, including both lines:
sed '/pattern1/,/pattern2/!d'
sed -n '/pattern1/,/pattern2/p'
Here are some examples:
$
printf 'A\nB\nC\nD\nE\nF\nG\nH\n' | sed '/C/,/F/!d'
C
D
E
F
$
printf 'A\nB\nC\nD\nE\nF\nG\nH\n' | sed -n '/C/,/F/p'
C
D
E
F
Select Between Lines, Exclusive
Select text between two lines, excluding both lines:
sed '/pattern1/,/pattern2/!d; //d'
Here is an example usage:
$
printf 'A\nB\nC\nD\nE\nF\nG\nH\n' | sed '/C/,/F/!d; //d'
D
E
The negated command
!d
deletes everything not matched
  by the 2-address range
/C/,/F/
, i.e. it deletes
  everything before the line matching
/C/
as well as
  everything after the line matching
/F/
.  So we are left
  with only the lines from
C
to
F
,
  inclusive.  Finally,
//
(the empty regular expression)
  reuses the most recently used regular expression.  So
  when
/C/,/F/
matches
C
, the
  command
//d
also matches
C
and deletes it.
  Similarly,
F
is deleted too.  That's how we are left
  with the lines between
C
and
F
, exclusive.
Here are some excerpts from
POSIX.1-2024
that help understand the
!d
and
//d
commands better:
A function can be preceded by a
'!'
character, in which
  case the function shall be applied if the addresses do not select
  the pattern space.  Zero or more <blank> characters shall be
  accepted before the
'!'
character.  It is unspecified
  whether <blank> characters can follow the
'!'
character, and conforming applications shall not follow
  the
'!'
character with <blank> characters.
If an RE is empty (that is, no pattern is specified)
sed
shall behave as if the last RE used in the last command applied
  (either as an address or as part of a substitute command) was
  specified.
Signing and Verification with SSH Key
Here are some minimal commands to demonstrate how we can sign some
  text using SSH key and then later verify it.
ssh-keygen -t ed25519 -f key
echo hello > hello.txt
ssh-keygen -Y sign -f key.pub -n file hello.txt
echo "jdoe $(cat key.pub)" > allowed.txt
ssh-keygen -Y verify -f allowed.txt -I jdoe -n file -s hello.txt.sig < hello.txt
Here are some examples that demonstrate what the outputs and
  signature file look like:
$
ssh-keygen -Y sign -f key.pub -n file hello.txt
Signing file hello.txt
Write signature to hello.txt.sig
$
cat hello.txt.sig
-----BEGIN SSH SIGNATURE-----
U1NIU0lHAAAAAQAAADMAAAALc3NoLWVkMjU1MTkAAAAgAwP6RnmFVrZO0m/nRIHyvr2S19
itsKegj9p/BZKqP1sAAAAEZmlsZQAAAAAAAAAGc2hhNTEyAAAAUwAAAAtzc2gtZWQyNTUx
OQAAAEB8ylqjCLgInF8DvROnLSm1UUWd0VuLPesI+1NhMrV9BjH5lf0w20kHunJW3qRIjw
Jfs9+q/e47KdlR8wBQaHYD
-----END SSH SIGNATURE-----
$
ssh-keygen -Y verify -f allowed.txt -I jdoe -n file -s hello.txt.sig < hello.txt
Good "file" signature for jdoe with ED25519 key SHA256:9ZJuUJNMy1UXo3AlQy8L7baD3LOfEbgQ30ELIt+8wWc
Block IP Address with nftables
Here is a sequence of commands to create an nftables rule from
  scratch to block an IP address:
$
sudo nft list ruleset
$
sudo nft add table inet filter
$
sudo nft list ruleset
table inet filter {
}
$
sudo nft add chain inet filter input { type filter hook input priority 0 \; }
$
sudo nft list ruleset
table inet filter {
        chain input {
                type filter hook input priority filter; policy accept;
        }
}
$
sudo nft add rule inet filter input ip saddr 172.236.0.216 drop
$
sudo nft list ruleset
table inet filter {
        chain input {
                type filter hook input priority filter; policy accept;
                ip saddr 172.236.0.216 drop
        }
}
Here is how to undo the above setup step by step:
$
sudo nft -a list ruleset
table inet filter { # handle 1
        chain input { # handle 1
                type filter hook input priority filter; policy accept;
                ip saddr 172.236.0.216 drop # handle 2
        }
}
$
sudo nft delete rule inet filter input handle 2
$
sudo nft list ruleset
table inet filter {
        chain input {
                type filter hook input priority filter; policy accept;
        }
}
$
sudo nft delete chain inet filter input
$
sudo nft list ruleset
table inet filter {
}
$
sudo nft delete table inet filter
$
sudo nft list ruleset
$
Finally, the following command deletes all rules, chains and tables.
  It wipes the entire ruleset, so use it with care.
$
sudo nft flush ruleset
$
sudo nft list ruleset
$
All outputs above were obtained using nftables v1.1.3 on Debian 13.2
  (Trixie).
Debian Logrotate Setup
Observed on Debian 11.5 (Bullseye) that
logrotate
is
  set up on it via
systemd
.  Here are some outputs that
  show what the setup is like:
$
sudo systemctl status logrotate.service
● logrotate.service - Rotate log files
     Loaded: loaded (/lib/systemd/system/logrotate.service; static)
     Active: inactive (dead) since Mon 2026-03-30 00:00:17 UTC; 19h ago
TriggeredBy:
●
logrotate.timer
       Docs: man:logrotate(8)
             man:logrotate.conf(5)
    Process: 2148235 ExecStart=/usr/sbin/logrotate /etc/logrotate.conf (code=exited, status=0/SUCCESS)
   Main PID: 2148235 (code=exited, status=0/SUCCESS)
        CPU: 574ms

Mar 30 00:00:16 spweb systemd[1]: Starting Rotate log files...
Mar 30 00:00:17 spweb systemd[1]: logrotate.service: Succeeded.
Mar 30 00:00:17 spweb systemd[1]: Finished Rotate log files.
$
sudo systemctl status logrotate.timer
● logrotate.timer - Daily rotation of log files
     Loaded: loaded (/lib/systemd/system/logrotate.timer; enabled; vendor preset: enabled)
     Active: active (waiting) since Mon 2026-01-19 19:19:34 UTC; 2 months 9 days ago
    Trigger: Tue 2026-03-31 00:00:00 UTC; 4h 7min left
   Triggers:
●
logrotate.service
       Docs: man:logrotate(8)
             man:logrotate.conf(5)

Warning: journal has been rotated since unit was started, output may be incomplete.
$
sudo systemctl list-timers logrotate
NEXT                        LEFT         LAST                        PASSED  UNIT            ACTIVATES
Tue 2026-03-31 00:00:00 UTC 4h 7min left Mon 2026-03-30 00:00:16 UTC 19h ago logrotate.timer logrotate.service

1 timers listed.
Pass --all to see loaded but inactive timers, too.
$
head /lib/systemd/system/logrotate.service
[Unit]
Description=Rotate log files
Documentation=man:logrotate(8) man:logrotate.conf(5)
RequiresMountsFor=/var/log
ConditionACPower=true

[Service]
Type=oneshot
ExecStart=/usr/sbin/logrotate /etc/logrotate.conf

$
cat /lib/systemd/system/logrotate.timer
[Unit]
Description=Daily rotation of log files
Documentation=man:logrotate(8) man:logrotate.conf(5)

[Timer]
OnCalendar=daily
AccuracySec=1h
Persistent=true

[Install]
WantedBy=timers.target
$
grep -vE '^#|^$' /etc/logrotate.conf
weekly
rotate 4
create
include /etc/logrotate.d
$
ls -l /etc/logrotate.d/
total 40
-rw-r--r-- 1 root root 120 Aug 21  2022 alternatives
-rw-r--r-- 1 root root 173 Jun 10  2021 apt
-rw-r--r-- 1 root root 130 Oct 14  2019 btmp
-rw-r--r-- 1 root root  82 May 26  2018 certbot
-rw-r--r-- 1 root root 112 Aug 21  2022 dpkg
-rw-r--r-- 1 root root 128 May  4  2021 exim4-base
-rw-r--r-- 1 root root 108 May  4  2021 exim4-paniclog
-rw-r--r-- 1 root root 329 May 29  2021 nginx
-rw-r--r-- 1 root root 374 May 20  2022 rsyslog
lrwxrwxrwx 1 root root  28 Mar 17 01:52
susam
-> /opt/susam.net/etc/logrotate
-rw-r--r-- 1 root root 145 Oct 14  2019 wtmp
To force log rotation right now, execute:
sudo systemctl start logrotate.service
